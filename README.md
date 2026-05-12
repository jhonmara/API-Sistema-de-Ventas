# 🚀 Sistema de Ventas API

API backend desarrollada con **FastAPI** para la gestión de usuarios y productos, implementando autenticación segura mediante JWT.



![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker)
![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=mysql)

---
## 🛠️ Tecnologías utilizadas

- Python
- FastAPI
- Docker
- MySQL
- SQLAlchemy
- Pydantic
- JWT (Autenticación)
- Bcrypt (Hash de contraseñas)
---

## ✨ Funcionalidades

- Registro y login de usuarios
- Autenticación con tokens JWT
- CRUD completo de productos
- Protección de rutas
- Validación de datos
- Manejo de errores

---

### 🛠️ Validaciones y Buenas Prácticas
Para asegurar la integridad de los datos, implementé validaciones personalizadas con **Pydantic**:
* **Limpieza de strings:** Uso de validadores para eliminar espacios accidentales en nombres de usuario (`.strip()`).
* **Restricciones de longitud:** Longitud mínima obligatoria para campos sensibles.
* **Transformación de datos:** Los modelos de respuesta están configurados con `from_attributes = True` para una integración fluida con el ORM.

## 📋 Requisitos previos

- Python 3.11+
- Docker
- Docker Compose
- MySQL 8

## ⚙️ Configuración del proyecto

### 1. Crear entorno virtual

```bash
python -m venv venv
```

### 2. Activar entorno

#### Windows

```bash
venv\Scripts\activate
```

#### Linux / Mac

```bash
source venv/bin/activate
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4. Configurar variables de entorno (.env)
> Crear un archivo `.env` basado en `.env.example`
```env
DB_USER=root
DB_PASSWORD=tu_password
DB_HOST=db
DB_PORT=3306
DB_NAME=ventas
SECRET_KEY=clave_super_segura
```

### 5. Ejecutar servidor

```bash
uvicorn app.main:app --reload
```
---
## 🐳 Ejecutar proyecto con Docker

### 1. Construir y levantar contenedores

```bash
docker compose up --build
```

### 2. Acceder a la API

API FastAPI:

```txt
http://localhost:8000
```

Swagger Docs:

```txt
http://localhost:8000/docs
```

Adminer:

```txt
http://localhost:8080
```

### 3. Detener contenedores

```bash
docker compose down
```

---
## 🔐 Autenticación

Para consumir endpoints protegidos:

1. Crear usuario en `/usuarios`
2. Iniciar sesión en `/usuarios/login`
3. Copiar el `access_token`
4. Ir a `/docs`
5. Clic en **Authorize**
6. Escribir: `Bearer TU_TOKEN`

---

## 📌 Endpoints principales

| Método | Endpoint | Descripción | Protegido |
|---|---|---|---|
| POST | `/usuarios` | Registro de usuarios | ❌ |
| POST | `/usuarios/login` | Login y generación JWT | ❌ |
| GET | `/productos` | Obtener productos | ✅ |
| GET | `/productos/{id}` | Obtener producto por ID | ✅ |
| POST | `/productos` | Crear producto | ✅ |
| PUT | `/productos/{id}` | Actualizar producto | ✅ |
| DELETE | `/productos/{id}` | Eliminar producto | ✅ |
---

## 📂 Estructura del proyecto

```txt
app/
├── auth/
├── core/
├── models/
├── routes/
├── schemas/
├── utils/
├── database.py
└── main.py
```