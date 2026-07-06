[README_demoblaze.md](https://github.com/user-attachments/files/29719256/README_demoblaze.md)
# Automatización de Pruebas — Demoblaze (Product Store)

Script de Selenium en Python que automatiza los casos de prueba principales del sitio e-commerce demo Demoblaze.

**Sitio bajo prueba:** https://www.demoblaze.com/

---

## Qué hace el script

`test_demoblaze.py` ejecuta automáticamente los siguientes casos de prueba:

| Caso | Descripción |
|---|---|
| TC-01 | Registro de usuario nuevo exitoso |
| TC-03 | Registro con campos vacíos (caso negativo) |
| TC-04 | Login con credenciales válidas |
| TC-05 | Login con contraseña incorrecta (caso negativo) |
| TC-07 | Logout exitoso |
| TC-08 | Filtrar productos por categoría Phones |
| TC-12 | Agregar un producto al carrito |
| TC-14 | Verificar contenido del carrito |
| TC-16 | Compra completa (Place Order → Purchase) |
| TC-18 | Enviar mensaje de contacto |

Al finalizar imprime **PASS** o **FAIL** por cada caso y guarda una captura `resultado_compra.png` como evidencia.

---

## Requisitos previos

- **Python 3** instalado
- **Google Chrome** instalado
- Librerías instaladas (ver instalación abajo)

---

## Instalación

```powershell
pip install -r requirements.txt
```

---

## Ejecución

```powershell
python test_demoblaze.py
```

El script genera automáticamente un usuario de prueba único (no hace falta ingresar credenciales manualmente).

Ejemplo de salida en consola:

```
Usuario de prueba generado: testuser_abcxyz

[TC-01] PASS — Usuario 'testuser_abcxyz' registrado. Alert: 'Sign up successful.'
[TC-03] PASS — El sistema alerta ante campos vacíos: 'Please fill out Username and Password.'
[TC-04] PASS — Login exitoso. Texto de bienvenida: 'Welcome testuser_abcxyz'
[TC-05] PASS — Sistema rechaza contraseña incorrecta. Alert: 'Wrong password.'
[TC-08] PASS — Se muestran 7 productos: ['Samsung galaxy s6', ...]
[TC-12] PASS — 'Samsung galaxy s6' agregado al carrito. Alert: 'Product added.'
[TC-14] PASS — El carrito tiene 1 producto(s):
         → Samsung galaxy s6 — $360
[TC-16] PASS — Compra confirmada: 'Thank you for your purchase!'
[TC-18] PASS — Mensaje enviado. Alert: 'Thanks for the message!!'
[TC-07] PASS — Logout exitoso, botón 'Log in' visible nuevamente

=== Ejecución finalizada. Revisar capturas para evidencia visual. ===
```

---

## Archivos del proyecto

| Archivo | Descripción |
|---|---|
| `test_demoblaze.py` | Script principal de automatización |
| `requirements.txt` | Dependencias de Python |
| `Plan_de_Pruebas_Demoblaze.md` | Plan de pruebas completo (23 casos) |
| `resultado_compra.png` | Evidencia: confirmación de compra |
| `README.md` | Este archivo |
