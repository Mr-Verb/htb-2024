# Start Dockerfile with host network
docker pull mrverb/htb-2024-csc:latest
docker run -it --network=host -v "/home/adfcsc/Documents/adfcsc":/adfcsc mrverb/htb-2024-csc:latest /bin/bash