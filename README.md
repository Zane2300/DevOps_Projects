# 🚀 RA5 — DevOps Labs & Automation Suite

[![CI/CD](https://img.shields.io/badge/CI%2FCD-Jenkins-informational)]()
[![Containers](https://img.shields.io/badge/Containers-Docker-blue)]()
[![Provisioning](https://img.shields.io/badge/Provisioning-Ansible-orange)]()
[![Kubernetes](https://img.shields.io/badge/Kubernetes-K3s-326ce5)]()
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

> Conjunto de laboratorios prácticos orientados a **automatización, integración continua, observabilidad y orquestación**. Cada proyecto es independiente y reproducible, con instrucciones mínimas para ejecutarlo en tu máquina.

---

## 🗂️ Estructura del repositorio

| Proyecto | Descripción | Tecnologías |
|---|---|---|
| [📘 RA5.1 — CI/CD con Jenkins y Docker](RA5.1/README.md) | Pipeline automático con pruebas unitarias, build de imagen, ejecución de contenedor y `docker-compose`. Integración con webhooks de GitHub. | Jenkins, Docker, Python (pytest) |
| [📗 RA5.2 — VM Ubuntu + Provisioning con Ansible](RA5.2/README.md) | Provisionamiento de una VM basada en Ubuntu utilizando **Vagrant** + **VirtualBox** y **Ansible** para instalar Apache y desplegar una web. | Vagrant, VirtualBox, Ansible |
| [📙 RA5.3 — Monitoring Stack](RA5.3/README.md) | Observabilidad con **Prometheus + Grafana + Node Exporter** dockerizados. Dashboards listos para métricas del host/contenedores. | Docker, Prometheus, Grafana |
| [📕 RA5.4 — K3s HA Cluster](RA5.4/README.md) | Despliegue de clúster **K3s en Alta Disponibilidad** con datastore PostgreSQL y balanceo **HAProxy**. Incluye `k9s` para operación. | K3s, PostgreSQL, HAProxy, k9s |

> Cada carpeta incluye su propio `README.md` con los pasos detallados, variables, comandos y artefactos necesarios.

---

## 🧠 Objetivos del conjunto

- Diseñar pipelines **CI/CD** reproducibles con **testing automatizado**.  
- Aprovisionar infra y **configurar servidores** con Ansible.  
- Instrumentar **monitorización** y tableros en Grafana.  
- Desplegar **Kubernetes ligero (K3s)** en modo HA.

---

## ⚙️ Requisitos globales

- **Docker** ≥ 24, **Docker Compose**  
- **Jenkins** LTS (para RA5.1)  
- **Vagrant** + **VirtualBox** (para RA5.2)  
- **Ansible** (para RA5.2)  
- **K3s / k9s** (para RA5.4)  
- Consola con permisos `sudo`

---

## ▶️ Arranque rápido (por proyecto)

### RA5.1 — CI/CD con Jenkins
```bash
# En Jenkins
# 1) Configura credenciales y webhook del repo
# 2) Carga el Jenkinsfile y ejecuta la pipeline
```

### RA5.2 — VM + Ansible
```bash
cd RA5.2
vagrant up               # crea VM
ansible-playbook site.yml -i inventory.ini
```

### RA5.3 — Monitoring Stack
```bash
cd RA5.3
docker compose up -d
# Accede a Grafana: http://localhost:3000
```

### RA5.4 — K3s HA
```bash
cd RA5.4
# Sigue los scripts / manifiestos incluidos para bootstrap del clúster
```

---

## 🧪 Pruebas y validaciones

- RA5.1 incluye **pytest** y reporte de resultados en la pipeline.  
- RA5.3 trae dashboards base y alertas opcionales.  
- RA5.4 valida estado con `kubectl get nodes` y `k9s`.

---

## 🤝 Contribuir

1. Haz **fork** del repositorio.  
2. Crea una rama `feature/nueva-mejora`.  
3. Realiza cambios con commits claros.  
4. Abre un **Pull Request** describiendo la motivación y pruebas.

---

## 📄 Licencia

Este repositorio se publica bajo **MIT License**. Consulta el archivo [`LICENSE`](LICENSE).

---

## ✍️ Autor

**Alex Rosell** · Repositorio de prácticas DevOps · 2025
