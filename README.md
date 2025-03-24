# 🚗 Proyecto API de Gestión de Autos

Este proyecto es un ejemplo funcional de una aplicación web moderna utilizando **FastAPI** como backend y **Next.js** como frontend. La app permite gestionar autos, sus marcas y modelos, utilizando una arquitectura desacoplada y herramientas de desarrollo profesional.

---

## 🧠 Objetivo

Desarrollar una **API REST** para administrar vehículos (autos), marcas y modelos, y construir una interfaz web moderna que consuma dicha API. El proyecto está preparado para escalar y ser desplegado utilizando Docker y CI/CD.

---

## 🏗️ Tecnologías y Frameworks Utilizados

### 📦 Backend

- **FastAPI**: Framework moderno y asincrónico para construir APIs con Python.
- **PostgreSQL**: Base de datos relacional robusta y de alto rendimiento.
- **SQLAlchemy**: ORM que permite mapear clases Python a tablas SQL.
- **Alembic**: Herramienta de migración de base de datos para SQLAlchemy.
- **Pydantic**: Validación de datos mediante tipado fuerte.

### 💻 Frontend

- **Next.js**: Framework basado en React con soporte para SSR, SSG y rutas automáticas.
- **Tailwind CSS**: Framework de diseño utilitario para estilos rápidos y consistentes.
- **Axios** o **React Query**: Librerías para consumir la API REST y manejar el estado de las llamadas HTTP.

### 🛠️ Herramientas Adicionales

- **Docker**: Contenerización del backend y frontend.
- **Nginx**: Servidor web para gestionar el tráfico y servir la app.
- **GitHub Actions**: CI/CD para automatizar tests, builds y despliegue del proyecto.

---

## 📁 Estructura del Proyecto

```text
fastapi_autos_project/
│
├── app/                     # Código principal del backend
│   ├── api/                 # Rutas y controladores (endpoints REST)
│   ├── crud/                # Funciones de acceso a datos (Create, Read, etc.)
│   ├── database/            # Configuración de la base de datos y el engine SQLAlchemy
│   ├── models/              # Declaración de las clases ORM (Tablas)
│   ├── schemas/             # Esquemas Pydantic para validación de datos
│   └── main.py              # Punto de entrada de la aplicación FastAPI
│
├── alembic/                 # Carpeta de migraciones de base de datos
│
├── requirements.txt         # Dependencias del backend
├── README.md                # Documentación del proyecto
│
├── frontend/                # (opcional) Carpeta para el frontend con Next.js
│
└── docker-compose.yml       # (opcional) Configuración de contenedores para backend, frontend y DB
```

---

## 🚀 Cómo comenzar

1. Clonar el repositorio:
   ```bash
   git clone https://github.com/tu-usuario/fastapi_autos_project.git](https://github.com/marcelofassi/CarSalesPOC.git
   cd fastapi_autos_project
   ```

2. Crear y activar entorno virtual:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Instalar dependencias:
   ```bash
   pip install -r requirements.txt
   ```

4. Crear base de datos PostgreSQL y configurar `.env` o `database.py` con las credenciales.

5. Ejecutar servidor de desarrollo:
   ```bash
   uvicorn app.main:app --reload
   ```

---

## 🧪 Próximos pasos

- Añadir autenticación con JWT
- Agregar tests con Pytest
- Configurar CI/CD con GitHub Actions
- Contenerizar todo el stack con Docker + Nginx
- Implementar frontend con Next.js y consumir la API REST

---

## ✨ Contribuciones

¡Las contribuciones están abiertas! Podés abrir un issue o crear un pull request para sugerencias o mejoras.

---

## 📜 Licencia

MIT © 2025 Marcelo
