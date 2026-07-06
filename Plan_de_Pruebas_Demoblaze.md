# Plan de Pruebas — Demoblaze (Product Store)

**URL del sistema bajo prueba (SUT):** https://www.demoblaze.com/
**Versión del documento:** 1.0
**Fecha:** 6 de julio de 2026

---

## 1. Introducción

Demoblaze es un sitio de e-commerce demo que simula una tienda de productos electrónicos (teléfonos, laptops y monitores). Permite registrarse, iniciar sesión, navegar por categorías de productos, agregar ítems al carrito y realizar una compra. Este plan cubre la estrategia, alcance, recursos y criterios para validar sus funcionalidades.

## 2. Objetivos

- Verificar que el registro e inicio de sesión de usuarios funcionan correctamente.
- Validar la navegación por categorías y el detalle de productos.
- Verificar que el carrito de compras agrega, muestra y elimina productos correctamente.
- Validar el flujo completo de compra (checkout).
- Detectar defectos en el manejo de errores ante datos inválidos o incompletos.

## 3. Alcance

### 3.1 Dentro del alcance (In Scope)

- Registro de usuario (Sign up)
- Login y Logout
- Navegación por categorías: Phones, Laptops, Monitors
- Vista de detalle de producto
- Agregar producto al carrito
- Eliminar producto del carrito
- Visualización del carrito
- Proceso de compra (Place Order)
- Formulario de Contacto
- Sección "About us"

### 3.2 Fuera del alcance (Out of Scope)

- Pruebas de carga o performance
- Pruebas de penetración o seguridad avanzada
- Pruebas en aplicaciones móviles nativas
- Integración con pasarelas de pago reales (el sitio es solo demo)

## 4. Estrategia de pruebas

| Tipo de prueba | Descripción | Prioridad |
|---|---|---|
| Funcional | Validar que cada función hace lo que debe (registro, login, compra, etc.) | Alta |
| Negativa / validación | Campos vacíos, credenciales incorrectas, datos inválidos | Alta |
| UI / Usabilidad | Etiquetas, mensajes, navegación, consistencia visual | Media |
| Compatibilidad | Ejecutar casos clave en Chrome, Firefox y Edge | Media |
| Regresión | Re-ejecutar casos críticos tras correcciones | Alta |
| Exploratoria | Sesiones libres buscando comportamientos inesperados | Media |

## 5. Ambiente de pruebas

- **URL:** https://www.demoblaze.com/
- **Navegadores:** Chrome (última versión), Firefox, Edge
- **Resoluciones:** Desktop 1920x1080 y 1366x768
- **Datos de prueba:** Usuarios creados durante la ejecución con emails/usernames aleatorios
- **Herramientas:** Python 3 + Selenium + webdriver-manager

## 6. Criterios de entrada y salida

**Criterios de entrada**
- Plan de pruebas aprobado
- Sitio demo accesible
- Casos de prueba escritos y revisados

**Criterios de salida**
- 100% de los casos de alta prioridad ejecutados
- Sin defectos críticos o bloqueantes abiertos
- Reporte de resultados entregado

## 7. Casos de prueba

### 7.1 Registro de usuario (Sign up)

| ID | Caso de prueba | Pasos | Resultado esperado |
|---|---|---|---|
| TC-01 | Registro exitoso | Completar username y password válidos → Sign up | Alert con mensaje "Sign up successful" |
| TC-02 | Registro con username ya existente | Usar un username ya registrado → Sign up | Alert indicando que el usuario ya existe |
| TC-03 | Registro con campos vacíos | Dejar username y/o password vacíos → Sign up | Alert solicitando completar los campos |

### 7.2 Login y Logout

| ID | Caso de prueba | Pasos | Resultado esperado |
|---|---|---|---|
| TC-04 | Login con credenciales válidas | Username y password correctos → Log in | Menú cambia a "Welcome [usuario]" y aparece "Log out" |
| TC-05 | Login con contraseña incorrecta | Username correcto + password incorrecto → Log in | Alert de error, sin acceso |
| TC-06 | Login con campos vacíos | Dejar ambos campos vacíos → Log in | Alert solicitando completar los campos |
| TC-07 | Logout exitoso | Estando logueado → Log out | Vuelve a mostrar "Log in" y "Sign up" en el menú |

### 7.3 Navegación y categorías

| ID | Caso de prueba | Pasos | Resultado esperado |
|---|---|---|---|
| TC-08 | Filtrar por categoría Phones | Clic en "Phones" | Se muestran solo productos de la categoría Phones |
| TC-09 | Filtrar por categoría Laptops | Clic en "Laptops" | Se muestran solo productos de la categoría Laptops |
| TC-10 | Filtrar por categoría Monitors | Clic en "Monitors" | Se muestran solo productos de la categoría Monitors |
| TC-11 | Ver detalle de un producto | Clic sobre cualquier producto | Se muestra nombre, imagen, precio y descripción del producto |

### 7.4 Carrito de compras

| ID | Caso de prueba | Pasos | Resultado esperado |
|---|---|---|---|
| TC-12 | Agregar un producto al carrito | Ir al detalle de un producto → "Add to cart" | Alert de confirmación; el producto aparece en el carrito |
| TC-13 | Agregar múltiples productos al carrito | Repetir el paso anterior con distintos productos | Todos los productos aparecen en el carrito |
| TC-14 | Ver el carrito | Clic en "Cart" en la barra de navegación | Se listan todos los productos agregados con nombre, precio y total |
| TC-15 | Eliminar un producto del carrito | En el carrito → clic en "Delete" sobre un producto | El producto desaparece y el total se actualiza |

### 7.5 Proceso de compra (Place Order)

| ID | Caso de prueba | Pasos | Resultado esperado |
|---|---|---|---|
| TC-16 | Compra exitosa con todos los datos | Carrito con productos → Place Order → completar nombre, tarjeta, mes, año, país, ciudad → Purchase | Alert/modal de confirmación con número de orden |
| TC-17 | Compra con campos obligatorios vacíos | Place Order → dejar campos vacíos → Purchase | Alert indicando que se deben completar los campos |

### 7.6 Contacto y About us

| ID | Caso de prueba | Pasos | Resultado esperado |
|---|---|---|---|
| TC-18 | Enviar mensaje de contacto | Completar email, nombre y mensaje → Send message | Alert de confirmación del mensaje enviado |
| TC-19 | Enviar mensaje de contacto con campos vacíos | Dejar campos vacíos → Send message | Alert o bloqueo indicando campos requeridos |
| TC-20 | Ver sección About us | Clic en "About us" | Se abre modal con video y descripción de la empresa |

### 7.7 Transversales

| ID | Caso de prueba | Resultado esperado |
|---|---|---|
| TC-21 | Verificar que todos los links del menú funcionan | No hay links rotos (404) |
| TC-22 | Probar flujo completo en Chrome, Firefox y Edge | Comportamiento consistente |
| TC-23 | Verificar mensajes de confirmación en cada operación | Mensajes claros y visibles |

## 8. Roles y responsabilidades

| Rol | Responsabilidad |
|---|---|
| Test Lead | Define estrategia, revisa y aprueba el plan |
| QA Tester | Diseña y ejecuta casos de prueba, reporta defectos |

## 9. Cronograma estimado

| Actividad | Duración estimada |
|---|---|
| Diseño de casos de prueba | 0.5 día |
| Ejecución de pruebas funcionales | 1 día |
| Ejecución de pruebas negativas | 0.5 día |
| Pruebas de compatibilidad | 0.5 día |
| Regresión y cierre | 0.5 día |

## 10. Riesgos

| Riesgo | Mitigación |
|---|---|
| El sitio es público y compartido; los datos pueden cambiar entre sesiones | Crear usuarios únicos en cada ejecución con nombres aleatorios |
| Algunos alerts de JavaScript pueden tardar en aparecer | Usar waits explícitos en la automatización |
| El carrito puede persistir datos de sesiones anteriores | Limpiar el carrito al inicio de cada ejecución de prueba |

## 11. Entregables

- Este plan de pruebas
- Script de automatización en Python + Selenium (`test_demoblaze.py`)
- Capturas de pantalla como evidencia de cada caso ejecutado
- README con instrucciones de instalación y ejecución
