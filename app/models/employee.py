from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Enum, Float   
from sqlalchemy.orm import relationship
from datetime import datetime
import enum
from app.database import Base

# Definir los tipos de empleados con enum
class EmployeeType(enum.Enum):
    """
    Tipos de empleados
    """
    FULL_TIME = "full_time"
    PART_TIME = "part_time"
    HOURLY = "hourly"
    COMMISSION = "commission"

# CLASE BASE PARA LOS EMPLEADOS
class Employee(Base):
    """
    Modelo base que representa la tabla 'employees' en la base de datos
    Esta es la clase padre de la que heredarán todos los tipos de empleados
    """
    # nombre de la tabla en la base de datos
    __tablename__ = "employees"
    
    # Definir las columnas que todos los empleados tienen en común
    id = Column(Integer, primary_key=True, index=True)  # ID único del empleado
    first_name = Column(String(50), nullable=False)  # Nombre del empleado
    last_name = Column(String(50), nullable=False)  # Apellido del empleado
    email = Column(String(100), unique=True, nullable=False)  # Email del empleado
    phone = Column(String(20), nullable=True)  # Teléfono del empleado
    hire_date = Column(DateTime, nullable=False)  # Fecha de contratación del empleado

    # tipo de empleado 
    employee_type = Column(Enum(EmployeeType), nullable=False)  # Tipo de empleado

    # campos específicos de cada tipo de empleado
    base_salary = Column(Float, default=0.0)  # Salario base del empleado
    hourly_rate = Column(Float, default=0.0)  # Tarifa por hora del empleado
    commission_rate = Column(Float, default=0.0)  # Tasa de comisión del empleado
    hours_worked = Column(Float, default=0.0)  # Horas trabajadas del empleado

    # Relación con el departamento al que pertenece el empleado
    department_id = Column(Integer, ForeignKey("departments.id"))  # ID del departamento
    department = relationship("Department", back_populates="employees")  # Relación con el departamento

    # campos de auditoría
    created_at = Column(DateTime, default=datetime.utcnow)  # Fecha de creación del empleado
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)  # Fecha de actualización

    def __repr__(self):
        """Representación en string del empleado"""
        return f"<Employee(id={self.id}, name='{self.first_name} {self.last_name}')>"
    
    @property
    def full_name(self):
        """Nombre completo del empleado"""
        return f"{self.first_name} {self.last_name}"

    def calculate_salary(self):
        """Calcula el salario total del empleado"""
        raise NotImplementedError("Las subclases deben implementar calculate_salary")

# CLASES HEREDADAS - Diferentes tipos de empleados

class FullTimeEmployee(Employee):
    """
    Empleado de tiempo completo con salario fijo mensual
    Hereda de Employee y sobrescribe el método calculate_salary
    """
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)  # Llamar al constructor de la clase padre
        self.employee_type = EmployeeType.FULL_TIME  # Establecer el tipo automáticamente
    
    def calculate_salary(self):
        """
        Calcula el salario mensual para empleados de tiempo completo
        Retorna el salario base directamente
        """
        return self.base_salary

class PartTimeEmployee(Employee):
    """
    Empleado de medio tiempo con salario proporcional
    Hereda de Employee y calcula 50% del salario de tiempo completo
    """
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)  # Llamar al constructor de la clase padre
        self.employee_type = EmployeeType.PART_TIME  # Establecer el tipo automáticamente
    
    def calculate_salary(self):
        """
        Calcula el salario mensual para empleados de medio tiempo
        Retorna 50% del salario base
        """
        return self.base_salary * 0.5

class HourlyEmployee(Employee):
    """
    Empleado por horas
    Hereda de Employee y calcula salario basado en horas trabajadas
    """
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)  # Llamar al constructor de la clase padre
        self.employee_type = EmployeeType.HOURLY  # Establecer el tipo automáticamente
    
    def calculate_salary(self):
        """
        Calcula el salario basado en horas trabajadas
        Retorna: tarifa por hora × horas trabajadas
        """
        return self.hourly_rate * self.hours_worked
    
    def add_hours(self, hours):
        """
        Agrega horas trabajadas al empleado
        Útil para actualizar las horas al final del mes
        """
        self.hours_worked += hours

class CommissionEmployee(Employee):
    """
    Empleado por comisión
    Hereda de Employee y calcula salario base + comisiones
    """
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)  # Llamar al constructor de la clase padre
        self.employee_type = EmployeeType.COMMISSION  # Establecer el tipo automáticamente
    
    def calculate_salary(self, sales_amount=0):
        """
        Calcula el salario basado en comisiones por ventas
        Retorna: salario base + (ventas × tasa de comisión)
        """
        commission = sales_amount * (self.commission_rate / 100)  # Calcular comisión
        return self.base_salary + commission  # Salario base + comisión