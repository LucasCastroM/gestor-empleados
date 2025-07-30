# importaciones de fastapi
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

#importo nuestra base de datos y modelos
from app.database import get_db
from app.models.department import Department

#importo los esquemas
from app.schemas.department_schemas import (
    DepartmentCreate, 
    DepartmentUpdate, 
    Department as DepartmentSchema
)
router = APIRouter(preflix="/deparments", tags=["departments"])

@router.post("/", response_model=DepartmentSchema, status_code=status.HTTP_201_CREATED)
def create_department(
    department: DepartmentCreate,
    db: Session = Depends(get_db)
):
    """
    Crea un nuevo departamento
    """
    #Verificar si el departamento ya existe
    existing_dept = db.query(Department).filter(Department.name == department.name).first()
    if existing_dept:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=f"Ya existe el departamento {department.name}")
    #Crear el nuevo departamento
    db_department = Department(**department.dict())
    db.add(db_department)
    db.commit()
    db.refresh(db_department)

    return db_department

@router.get("/", response_model=List[DepartmentSchema])
def get_departments(
    skip: int = 0, 
    limit: int = 100, 
    db: Session = Depends(get_db)
):
    """
    Obtener lista de departamentos con paginación
    """
    departments = db.query(Department).offset(skip).limit(limit).all()
    return departments  