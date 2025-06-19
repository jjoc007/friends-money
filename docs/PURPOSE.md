# Propósito del repositorio

Este proyecto contiene la planeación y los primeros documentos para desarrollar **Friends Money**, una aplicación que facilita el manejo de gastos compartidos entre grupos de amigos o familiares. La idea principal es registrar quién paga cada gasto dentro de un evento y distribuirlo entre los participantes para llevar un control de saldos.

El repositorio se estructura en torno a tres áreas principales:

- **Infraestructura**: scripts y configuraciones para desplegar la aplicación en AWS usando Terraform y contenedores Docker.
- **Backend**: servicio en Python (FastAPI) encargado de la autenticación, la gestión de eventos y el cálculo de saldos.
- **Frontend**: aplicación móvil/web basada en React Native que interactúa con el backend para mostrar la información al usuario.

En el archivo [PLAN.md](../PLAN.md) se detallan las épicas y tareas a realizar. Aquí se añaden algunas ideas adicionales para futuras mejoras:

- Soporte para múltiples monedas y tasas de cambio.
- Integración con pasarelas de pago para saldar deudas directamente.
- Modo offline que sincronice los datos cuando el dispositivo recupere conexión.

Estas propuestas pueden evaluarse más adelante según las prioridades del proyecto.
