# Diagramas de Arquitectura

A continuación se muestran diagramas simplificados de la interacción entre la infraestructura, el backend y el frontend de **Friends Money**.

```mermaid
flowchart TD
    subgraph Cliente
        App["App React Native"]
    end

    subgraph AWS
        ALB["Load Balancer"]
        Backend["Contenedor FastAPI"]
        DB[("RDS PostgreSQL")]
        S3[("S3 - Archivos estáticos")]
    end

    App -->|HTTPS| ALB
    ALB --> Backend
    Backend --> DB
    Backend --> S3
```

El diagrama anterior muestra la comunicación básica entre la aplicación del usuario (frontend) y los componentes desplegados en AWS.

```mermaid
flowchart LR
    Dev["Repositorio Git"] --> CI["Pipeline CI/CD"] --> AWS
    AWS -->|Despliegue| ECS["Cluster ECS"]
    AWS -->|Infraestructura| Terraform
```

Este segundo diagrama ilustra cómo el código del repositorio se integra con la canalización de CI/CD para generar los contenedores y aplicarlos en la nube usando Terraform.
