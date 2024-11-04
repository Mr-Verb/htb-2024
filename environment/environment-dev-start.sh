# Build Dockerfile
docker build -t temp-adfcsc:latest .
docker run -it --network=host -v "/home/adfcsc/Documents/adfcsc":/adfcsc temp-adfcsc:latest /bin/bash