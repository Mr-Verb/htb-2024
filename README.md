# htb-2024
Code Repository of all learnings from HTB and CTF events from 2024


## Environment
The `Dockerfile` stored in the `environment` folder is used as the development environment for all HTB/CTF events and it constantly improved to include additional tooling.

### Usage
Navigate to your CTF folder which holds that event's challenges:

```bash
# cd `ctf event folder`
sudo docker pull mrverb/htb-2024-csc:latest
docker run -it --network=host -v "$(pwd)":/ctf mrverb/htb-2024-csc:latest /bin/bash
```