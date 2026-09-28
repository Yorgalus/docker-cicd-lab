# Docker & GitLab CI/CD Lab

![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)
![GitLab CI](https://img.shields.io/badge/GitLab%20CI-FC6D26?style=flat-square&logo=gitlab&logoColor=white)
![Nginx](https://img.shields.io/badge/Nginx-009639?style=flat-square&logo=nginx&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=flat-square&logo=flask&logoColor=white)
![Redis](https://img.shields.io/badge/Redis-DC382D?style=flat-square&logo=redis&logoColor=white)

Travaux pratiques sur la conteneurisation avec Docker et l'automatisation de déploiement avec GitLab CI/CD. Conteneurisation d'applications, orchestration multi-conteneurs sécurisée, et construction de pipelines d'intégration continue.

## Pipeline CI/CD

```mermaid
flowchart LR
    DEV["git push"] --> SECU

    subgraph PIPE["Pipeline GitLab CI"]
        direction LR
        SECU["secu<br/>contrôle sécurité"] --> BUILD["build<br/>image alpine"]
        BUILD --> TEST["test<br/>génère un artifact"]
        TEST --> DEPLOY["deploy<br/>lit l'artifact"]
    end

    TEST -. artifact .-> DEPLOY

    classDef s fill:#EDEAF4,stroke:#5B4B8A,color:#1a1a1a
    classDef b fill:#EAF1F8,stroke:#1F6FB2,color:#1a1a1a
    classDef t fill:#F8EFDD,stroke:#B5710B,color:#1a1a1a
    classDef d fill:#E6F2E6,stroke:#2E7D32,color:#1a1a1a
    class SECU s
    class BUILD b
    class TEST t
    class DEPLOY d
```

## Architecture reverse proxy

```mermaid
flowchart TB
    U([Client]) -->|HTTP :80| RP["Reverse Proxy<br/>nginx"]
    RP -->|site-a.lab.local| A["Conteneur<br/>Site A"]
    RP -->|site-b.lab.local| B["Conteneur<br/>Site B"]

    classDef proxy fill:#FBEDEC,stroke:#C0392B,color:#1a1a1a
    classDef site fill:#EAF1F8,stroke:#1F6FB2,color:#1a1a1a
    class RP proxy
    class A,B site
```

## Application Flask + Redis

```mermaid
flowchart LR
    U([Client]) -->|:8000| WEB["Flask<br/>(réseau public + interne)"]
    WEB -->|:6379 mot de passe| REDIS["Redis<br/>(réseau interne uniquement)"]

    subgraph PUB["réseau public"]
        WEB
    end
    subgraph INT["réseau interne (isolé, pas d'accès sortant)"]
        REDIS
    end

    classDef web fill:#EAF1F8,stroke:#1F6FB2,color:#1a1a1a
    classDef db fill:#E6F2E6,stroke:#2E7D32,color:#1a1a1a
    class WEB web
    class REDIS db
```

Redis n'est jamais exposé publiquement : il vit sur un réseau interne isolé, protégé par mot de passe, avec des limites de ressources et un healthcheck côté application.

## Contenu

- **gitlab-ci/** : pipeline GitLab CI (stages, variables, images par job, artifacts, dépendances)
- **reverse-proxy/** : plusieurs sites derrière un reverse proxy nginx qui route selon le domaine
- **flask-redis/** : application Flask couplée à Redis, réseaux isolés, secrets, limites de ressources

## Compétences illustrées

- Écriture de Dockerfiles et de fichiers docker-compose
- Isolation réseau entre conteneurs (base de données non exposée)
- Gestion des secrets via variables d'environnement (.env non versionné)
- Limitation des ressources (CPU, mémoire) et healthchecks
- Architecture reverse proxy multi-services
- Pipelines CI/CD : stages, artifacts, dépendances

## Prérequis

- Docker et Docker Compose
- Un runner GitLab pour la partie CI/CD

## Avertissement

Projet réalisé dans un cadre d'apprentissage. Configurations d'exemple, à adapter et durcir avant tout usage en production.
