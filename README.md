# 🏢 Gestor de Empleados

Sistema de gestión de empleados con **cálculo automático de salarios** usando FastAPI y herencia de clases.

## 🎯 ¿Qué hace?

- **Gestiona empleados** de diferentes tipos
- **Calcula salarios** automáticamente según el tipo
- **API REST** para crear, leer, actualizar y eliminar

## 📚 Tipos de Empleados

| Tipo | Cálculo de Salario |
|------|-------------------|
| **Tiempo Completo** | Salario fijo |
| **Medio Tiempo** | 50% del salario base |
| **Por Horas** | Horas × Tarifa |
| **Por Comisión** | Base + (Ventas × %) |

## 🛠️ Tecnologías

- **FastAPI** - Framework para APIs
- **SQLAlchemy** - ORM para base de datos
- **Pydantic** - Validación de datos
- **SQLite** - Base de datos

## 🚀 Instalación

```bash
# Crear entorno virtual
python -m venv venv

# Activar (Windows)
.\venv\Scripts\Activate.ps1

# Instalar dependencias
pip install -r requirements.txt
```

## 📁 Estructura

```
app/
├── models/          # Modelos de base de datos
│   ├── department.py
│   └── employee.py  # Con herencia de clases
├── database.py      # Configuración DB
└── requirements.txt # Dependencias
```


**¡Proyecto de aprendizaje en desarrollo! 🚀**
