docker run -d -p 8080:80 --network=host --name=cyberchef ghcr.io/gchq/cyberchef:latest
sleep 2
firefox --new-window http://localhost