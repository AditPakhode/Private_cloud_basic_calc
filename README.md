# Private Linux Cloud Calculator

A small Flask calculator packaged as a Docker container for a private cloud computing demonstration.

## What To Demonstrate

- A Linux machine acts as your private cloud node.
- Docker runs the calculator in an isolated container.
- The service is reachable only on your private Wi-Fi/LAN.
- A mobile browser becomes the client device.

## Run On Your Linux Cloud Node

```bash
docker build -t private-cloud-calculator .
docker run -d --name calc-cloud -p 5000:5000 private-cloud-calculator
```

Find the Linux machine's private LAN IP:

```bash
hostname -I
```

On your phone, connect to the same Wi-Fi and open:

```text
http://<linux-lan-ip>:5000
```

Example:

```text
http://192.168.1.20:5000
```

## Useful Demo Commands

```bash
docker ps
docker stop calc-cloud
docker start calc-cloud
docker logs calc-cloud
```

For the private cloud point, do not port-forward this service to the internet. Keep it inside your local network.
