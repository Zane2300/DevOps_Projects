# RA5.4 - Despliegue K3s con Alta Disponibilidad y Balanceo de Carga

Este proyecto demuestra la instalación, configuración y validación de un clúster Kubernetes ligero (`k3s`) en modo de Alta Disponibilidad (HA) con base de datos externa, así como el despliegue de servicios balanceados con HAProxy.

## Estructura del repositorio

```
.
├── manifests/      # Archivos YAML para desplegar los servicios en K3s
├── assets/         # Capturas de pantalla que demuestran el funcionamiento
└── README.md       # Este documento
```

---

## Actividad 5.1 - K3s en modo Single Node + Nginx

Se instaló K3s mediante un solo binario, usando el script oficial:

```bash
curl -sfL https://get.k3s.io | sh -
```

Se desplegó un servicio `nginx` con 2 réplicas mediante el siguiente manifiesto: [`nginx-deploy.yaml`](manifests/nginx-deploy.yaml)

La verificación se realizó usando K9s:

![k9s nginx y haproxy](assets/k9s-nginx&haproxy.png)

---

## Actividad 5.2 - K3s en modo HA con PostgreSQL externo

Se instaló PostgreSQL localmente y se configuró con:

```bash
CREATE USER k3suser WITH ENCRYPTED PASSWORD '123';
CREATE DATABASE k3sdb OWNER k3suser;
```

Y se instaló `k3s` usando esa base de datos:

```bash
curl -sfL https://get.k3s.io | INSTALL_K3S_EXEC="server --datastore-endpoint='postgres://k3suser:123@127.0.0.1:5432/k3sdb'" sh -
```

Comprobación del nodo activo:

![Estado del nodo](assets/k3s-ha-status.png)

---

## Actividad 5.3 - Conversión de Docker Compose a Kubernetes

Se tomó como base el siguiente `docker-compose.yml`:

```yaml
version: '3'
services:
  web1:
    image: nginx
  web2:
    image: nginx
  lb:
    image: dockercloud/haproxy
    links:
      - web1
      - web2
    ports:
      - 80:80
    environment:
      - MODE=http
      - BACKENDS=web1,web2
      - BALANCE=roundrobin
```

Y se convirtió a los siguientes manifiestos:
- [`web1-deploy.yaml`](manifests/web1-deploy.yaml)
- [`web2-deploy.yaml`](manifests/web2-deploy.yaml)
- [`haproxy-deploy.yaml`](manifests/haproxy-deploy.yaml)

---

### Acceso y Validación

El servicio `haproxy` fue expuesto por NodePort y se validó con:

```bash
curl http://localhost:32129
```

Captura de validación:

![Curl test](assets/curl-test.png)

---

## Conclusión

Este proyecto demuestra:
- Instalación de `k3s` en modo standalone y HA
- Integración con PostgreSQL como datastore externo
- Conversión de `docker-compose` a manifiestos Kubernetes
- Uso de K9s para gestión visual del clúster
- Validación de balanceo de carga con HAProxy
