# Friends Money

Aplicación para gestionar gastos compartidos entre amigos. Permite registrar eventos (como viajes, cenas o actividades grupales) y distribuir los gastos entre los participantes. Cada usuario podrá ver su saldo y conocer a quién debe pagar para saldar sus deudas.

Este repositorio servirá de guía para construir la infraestructura, el backend y el frontend de la aplicación. Consulta el archivo [PLAN.md](PLAN.md) para ver el detalle de épicas y tareas previstas.

## Funcionalidades clave

- **Autenticación** con usuario/clave y opción de acceso mediante Google.
- **Eventos** con enlaces de invitación para que otros usuarios se unan fácilmente.
- **Registro de gastos** indicando quién pagó y cómo se reparte cada gasto.
- **Cálculo automático de saldos** para saber quién debe a quién dentro de cada evento.
- **Reportes** y conciliación de pagos para cerrar las cuentas.

## Próximos pasos

1. Definir la infraestructura base con Terraform y configurar un entorno reproducible en AWS.
2. Implementar el servicio de autenticación y modelos de usuario con FastAPI.
3. Crear las pantallas iniciales del frontend en React Native y conectar con el backend.

Para más detalles consulta el plan de desarrollo incluido en este repositorio.

## Infraestructura con Terraform

La carpeta `terraform` define una infraestructura **serverless** que crea funciones Lambda, una API Gateway HTTP, una tabla DynamoDB en modo `PAY_PER_REQUEST` y un bucket S3 para archivos estáticos. Para inicializar y revisar el plan de cambios ejecuta:

```bash
terraform init
terraform plan
```

Tambien se incluye un workflow de GitHub Actions que valida la configuracion en cada _pull request_.
