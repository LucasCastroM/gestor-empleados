#esto es un modelo de departamento, es decir, una tabla en la base de datos
#funciona como plantilla para crear las tablas en la base de datos
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import Base

class Department(Base):
    """
    Modelo que representa la tabla 'departments' en la base de datos
    Un departamento puede tener muchos empleados, por eso se usa relationship
    para relacionar el departamento con los empleados que pertenecen a ese departamento
    """
    #nombre de la tabla en la base de datos
    __tablename__ = "departments"
    #Definir las columnas de la tabla
    id = Column(Integer, primary_key=True, index=True)# ID único del departamento
    name = Column(String(100), nullable=False)# Nombre del departamento
    description = Column(String(255), nullable=True)# Descripción del departamento

    #Campos de auditoría
    #orígenes de datos (fecha de creación y actualización)
    created_at = Column(DateTime, default=datetime.utcnow)# Fecha de creación del departamento
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)# Fecha de actualización del departamento

    # Relación con empleados (un departamento puede tener muchos empleados)
    employees = relationship("Employee", back_populates="department")

    def __repr__(self):
        """Representación en string del departamento (útil para debugging)"""
        return f"<Department(id={self.id}, name='{self.name}')>"

