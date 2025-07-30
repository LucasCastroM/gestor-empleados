"""
Esquemas de Pydantic para el modelo de departamentos
"""
from pydantic import BaseModel
from datetime import datetime
from typing import Optional, List

class DepartmentBase(BaseModel):
    """
    Esquema base para los departamentos
    """
    name : str # nombre del departamento
    description : Optional[str] = None # descripción del departamento
 
class DepartmentCreate(DepartmentBase):
    """ Esquema para crear un departamento """
    pass # No hace nada, solo para indicar que no se necesita nada más

#Clase para actualizar un departamento
class DepartmentUpdate(BaseModel):
    name: Optional[str] = None 
    description: Optional[str] = None

#esquema para devoler información de un departamento
class Department(DepartmentBase):
    id: int #id unico del departamento
    created_at: datetime # fecha de creación
    updated_at: datetime # fecha de actualización

    class Config:
        from_attributes = True # Permite crear desde objetos SQLAlchemy
