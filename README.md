# 🚀 Sistema de Ventas API

API backend desarrollada con **FastAPI** para la gestión de usuarios y productos, implementando autenticación segura mediante JWT.

---

## 🛠️ Tecnologías utilizadas

- FastAPI
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

## ⚙️ Configuración del proyecto

### 1. Crear entorno virtual

```bash
python -m venv venv
```

### 2. Activar entorno

```bash
venv\Scripts\activate
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4. Configurar variables de entorno (.env)

```env
DB_USER=root
DB_PASSWORD=tu_password
DB_HOST=127.0.0.1
DB_PORT=3307
DB_NAME=ventas
SECRET_KEY=clave_super_segura
```

### 5. Ejecutar servidor

```bash
uvicorn app.main:app --reload
```
## 🔐 Autenticación

Para consumir endpoints protegidos:

1. Crear usuario en `/usuarios`
2. Iniciar sesión en `/usuarios/login`
3. Copiar el `access_token`
4. Ir a `/docs`
5. Clic en **Authorize**
6. Escribir: Bearer TU_TOKEN
---

## 📌 Endpoints principales

### Usuarios
- POST `/usuarios`
- POST `/usuarios/login`

### Productos
- GET `/productos`
- GET `/productos/{id}`
- POST `/productos`
- PUT `/productos/{id}`
- DELETE `/productos/{id}`