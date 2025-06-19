# Plan de Desarrollo

Este documento describe las épicas, objetivos y tareas para construir la aplicación de gestión de gastos compartidos. Se divide en tres grandes áreas: infraestructura, backend y frontend. Las épicas se presentan en un orden sugerido de ejecución.

## Infraestructura

### Épica 1: Configuración de la infraestructura base
**Objetivo:** disponer de un entorno reproducible en AWS usando _Infrastructure as Code_.

**Tareas principales:**
1.1 Definir y configurar repositorio de Terraform.
1.2 Crear VPC, subredes y grupos de seguridad.
1.3 Provisionar base de datos RDS (PostgreSQL).
1.4 Crear bucket S3 para archivos estáticos.
1.5 Configurar pipelines de CI/CD para aplicar la infraestructura.

### Épica 2: Contenedores y orquestación
**Objetivo:** preparar la ejecución de los servicios mediante contenedores.

**Tareas principales:**
2.1 Crear `Dockerfile` para el backend en Python.
2.2 Crear `Dockerfile` para el frontend (React Native para web o similar).
2.3 Configurar repositorio ECR y subir imágenes.
2.4 Definir un clúster ECS o EKS y desplegar los contenedores.
2.5 Automatizar el despliegue desde la canalización de CI/CD.

## Backend

### Épica 3: Servicio de usuarios y autenticación
**Objetivo:** permitir registro e inicio de sesión mediante usuario/clave y Google OAuth.

**Tareas principales:**
3.1 Seleccionar framework (por ejemplo, FastAPI).
3.2 Crear modelos de usuario y roles en la base de datos.
3.3 Implementar autenticación JWT.
3.4 Integrar autenticación con Google OAuth.
3.5 Añadir pruebas unitarias del flujo de login.

### Épica 4: Gestión de eventos
**Objetivo:** crear eventos y asociar participantes mediante URLs de invitación.

**Tareas principales:**
4.1 Definir modelo de evento y relación con usuarios.
4.2 Endpoint para crear y editar eventos.
4.3 Generar URL única para invitar a otros usuarios.
4.4 Endpoint para unirse a un evento usando la invitación.
4.5 Listar eventos de un usuario.

### Épica 5: Registro de gastos y cálculo de saldos
**Objetivo:** registrar los gastos de un evento y calcular cuánto debe cada participante.

**Tareas principales:**
5.1 Crear modelos de gasto y participación en cada gasto.
5.2 Endpoint para registrar un gasto y su distribución.
5.3 Calcular saldos positivos y negativos por usuario.
5.4 Endpoint para consultar saldo de un evento y de un usuario.
5.5 Pruebas unitarias de la lógica de distribución.

### Épica 6: Reportes y conciliación de pagos
**Objetivo:** facilitar la conciliación de deudas entre participantes.

**Tareas principales:**
6.1 Endpoint para obtener un resumen de quién debe pagar a quién.
6.2 Exportar reportes en formato CSV.
6.3 Notificaciones o recordatorios opcionales.

## Frontend

### Épica 7: Configuración inicial del proyecto móvil/web
**Objetivo:** iniciar la base del frontend compatible con despliegue móvil.

**Tareas principales:**
7.1 Crear proyecto con React Native y TypeScript.
7.2 Configurar navegación y manejo de estado (Redux o similar).
7.3 Conectar con los endpoints del backend.

### Épica 8: Autenticación en la interfaz
**Objetivo:** permitir a los usuarios registrarse e iniciar sesión desde la app.

**Tareas principales:**
8.1 Pantalla de inicio de sesión y registro.
8.2 Integración con Google OAuth.
8.3 Manejo de tokens JWT y persistencia de sesión.

### Épica 9: Gestión de eventos y gastos
**Objetivo:** que los usuarios puedan gestionar eventos y gastos desde la app.

**Tareas principales:**
9.1 Pantalla para crear evento y compartir la invitación.
9.2 Pantalla con lista de eventos del usuario.
9.3 Dentro de un evento: añadir gastos y ver historial.
9.4 Mostrar saldo individual y global del evento.

### Épica 10: Preparación de builds y despliegue
**Objetivo:** distribuir la aplicación y automatizar su entrega.

**Tareas principales:**
10.1 Configurar builds de producción para iOS y Android.
10.2 Si se publica versión web, desplegar en S3 + CloudFront.
10.3 Automatizar publicación mediante la canalización de CI/CD.

## Infraestructura complementaria

### Épica 11: Monitoreo y métricas
**Objetivo:** observar la salud de la aplicación en producción.

**Tareas principales:**
11.1 Configurar CloudWatch Logs y métricas de la aplicación.
11.2 Establecer alarmas básicas para errores y uso de recursos.

### Épica 12: Seguridad y copias de seguridad
**Objetivo:** proteger la información y garantizar su recuperación.

**Tareas principales:**
12.1 Definir roles IAM mínimos necesarios.
12.2 Configurar copias de seguridad automáticas de RDS.
12.3 Revisar políticas de acceso a S3 y secretos.

---

Cada épica puede dividirse en sprints según las prioridades del proyecto. Este plan servirá de guía inicial para comenzar el desarrollo de la aplicación.
