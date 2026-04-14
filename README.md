# 🚀 Sistema de Ventas API

Este es mi proyecto inicial de Backend desarrollado con **FastAPI**. El objetivo es gestionar usuarios y productos, aplicando seguridad con autenticación mediante tokens.

---

## ✨ Aprendizajes clave

En este proyecto apliqué conceptos de:

* **FastAPI**: Creación de rutas y documentación automática.
* **SQLAlchemy**: Manejo de base de datos MySQL mediante un ORM.
* **Seguridad**: Hashing de contraseñas con Bcrypt y autenticación con JWT.
* **Pydantic**: Validación de esquemas de datos.

---

## ⚙️ Configuración del proyecto

1. **Crear entorno virtual:**

```bash
python -m venv venv
```

2. **Activar entorno virtual:**

```bash
venv\Scripts\activate
```

3. **Instalar dependencias:**

```bash
pip install -r requirements.txt
```

4. **Configurar variables de entorno (.env):**

```env
DB_USER=root
DB_PASSWORD=tu_password
DB_HOST=127.0.0.1
DB_PORT=3307
DB_NAME=ventas
SECRET_KEY=clave_super_segura
```

5. **Ejecutar el servidor:**

```bash
uvicorn app.main:app --reload
```

---

## 🔐 Autenticación

Para usar los endpoints protegidos:

1. Crear usuario en `/usuarios`
2. Hacer login en `/usuarios/login`
3. Copiar el `access_token`
4. Ir a `/docs`
5. Dar clic en **Authorize**
6. Escribir:

```
Bearer TU_TOKEN
```

---

## 📌 Endpoints principales

### Usuarios

* POST `/usuarios`
* POST `/usuarios/login`

### Productos

* GET `/productos`
* GET `/productos/{id}`
* POST `/productos`
* PUT `/productos/{id}`
* DELETE `/productos/{id}`

---

## 🧠 Nota

Este proyecto forma parte de mi aprendizaje en desarrollo backend. Actualmente estoy mejorando mis conocimientos en APIs y buenas prácticas.

---

## 👨‍💻 Autor

Juan Manuel Maya
