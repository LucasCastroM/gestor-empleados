"""
Esquemas de Pydantic para el modelo de empleados
"""
from optparse import Option
from pydantic import BaseModel, EmailStr, Field
from datetime import datetime
from typing import Optional, Union
from enum import Enum

#import el enum de tipos de empleados
from app.models.employee import EmployeeType

class EmployeeBase(BaseModel):
    """
    Esquema base para los empleados
    """
    first_name: str = Field(..., min_length=3, max_length=50)
    last_name: str = Field(..., min_length=3, max_length=50)
    email: EmailStr = Field(..., unique=True)
    phone: Optional[str] = Field(None, min_length=10, max_length=15)
    hire_date: datetime #fecha de contratación
    department_id: Optional[int] = None #id del departamento

class EmployeeCreate(EmployeeBase):
    """
    Esquema para crear un empleado
    """
    employee_type: EmployeeType #tipo de empleado: full-time, part-time, contractor
    base_salary: Optional[float] = Field(None, ge=0) #salario base
    hourly_rate: Optional[float] = Field(None, ge=0) #tarifa por hora
    commission_rate: Optional[float] = Field(None, ge=0, le=100) #comisión
    hours_worked: Optional[float] = Field(None, ge=0) #horas trabajadas

class EmployeeUpdate(BaseModel):
    """
    Esquema para actualizar un empleado
    """
    first_name: Optional[str] = Field(None, min_length=1, max_length=100)
    last_name: Optional[str] = Field(None, min_length=1, max_length=100)
    email: Optional[EmailStr] = None
    phone: Optional[str] = Field(None, max_length=20)
    department_id: Optional[int] = None
    base_salary: Optional[float] = Field(None, ge=0)
    hourly_rate: Optional[float] = Field(None, ge=0)
    commission_rate: Optional[float] = Field(None, ge=0, le=100)
    hours_worked: Optional[float] = Field(None, ge=0)

class Employee(EmployeeBase):
    """
    Esquema para devolver un empleado
    """
    id: int #id unico del empleado
    employee_type: EmployeeType
    base_salary: float
    hourly_rate: float
    commission_rate: float
    hours_worked: float
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True # para que pydantic pueda convertir los datos de la base de datos a los campos de la clase

