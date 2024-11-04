# Over the Wire

## [Bandit](https://overthewire.org/wargames/bandit/)

### Level 0
```bash
ssh bandit0@bandit.labs.overthewire.org -p 2220
# Password bandit0

cat readme
# Password: ZjLjTmM6FvvyRnrb2rfNWOZOTa6ip5If
```

### Level 1
```bash
ssh bandit1@bandit.labs.overthewire.org -p 2220
# Password ZjLjTmM6FvvyRnrb2rfNWOZOTa6ip5If

cat ./-
# Password 263JGJPfgU6LtdEvgfWU1XP5yac29mFx
```
### Level 2
```bash
ssh bandit2@bandit.labs.overthewire.org -p 2220
# Password 263JGJPfgU6LtdEvgfWU1XP5yac29mFx

cat 'spaces in this filename'
# Password: MNk8KNH3Usiio41PRUEoDFPqfxLPlSmx
```

### Level 3
```bash
ssh bandit3@bandit.labs.overthewire.org -p 2220
# Password MNk8KNH3Usiio41PRUEoDFPqfxLPlSmx
ls -al inhere/
cat inhere/...Hiding-From-You
# Password: 2WmrDFRmJIq3IPxneAaMGhap0pFhF3NJ
```

### Level 4
```bash
ssh bandit4@bandit.labs.overthewire.org -p 2220
# Password 2WmrDFRmJIq3IPxneAaMGhap0pFhF3NJ

cd inhere/
file ./*
# Password: 4oQYVPkxZOOEOO5pTW81FB8j8lxXGUQw
```

### Level 5
```bash
ssh bandit5@bandit.labs.overthewire.org -p 2220
# Password 4oQYVPkxZOOEOO5pTW81FB8j8lxXGUQw

cd inhere/
find -size 1033c
cat ./maybehere07/.file2
# Password: HWasnPhtq9AVKe0dmk45nxy20cvUa6EG
```

### Level 6
```bash
ssh bandit6@bandit.labs.overthewire.org -p 2220
# Password HWasnPhtq9AVKe0dmk45nxy20cvUa6EG

find / -size 33c -user bandit7 -group bandit6
cat /var/lib/dpkg/info/bandit7.password

# Password: morbNTDkSW6jIlUc0ymOdMaLnOlFVAaj
```

### Level 7
```bash
ssh bandit7@bandit.labs.overthewire.org -p 2220
# Password morbNTDkSW6jIlUc0ymOdMaLnOlFVAaj

cat data.txt | grep "millionth"

# Password: dfwvzFQi4mU0wfNbFOe9RoWskMLg7eEc
```
### Level 8
```bash
ssh bandit8@bandit.labs.overthewire.org -p 2220
# Password dfwvzFQi4mU0wfNbFOe9RoWskMLg7eEc

sort data.txt | uniq --count
# Password: 4CKMh1JI91bUIZZPXDqGanal4xvAg0JM
```

### Level 9
```bash
ssh bandit9@bandit.labs.overthewire.org -p 2220
# Password 4CKMh1JI91bUIZZPXDqGanal4xvAg0JM

cat data.txt
strings data.txt
# Password: FGUW5ilLVJrxX9kMYMmlN4MgbpfMiqey
```

### Level 10
```bash
ssh bandit10@bandit.labs.overthewire.org -p 2220
# Password FGUW5ilLVJrxX9kMYMmlN4MgbpfMiqey

cat data.txt | base64 -d
# Password: dtR173fZKb0RRsDFSGsg2RWnpNVj3qRr
```

### Level 11
```bash
ssh bandit11@bandit.labs.overthewire.org -p 2220
# Password dtR173fZKb0RRsDFSGsg2RWnpNVj3qRr

cat data.txt | tr '[A-Za-z]' '[N-ZA-Mn-za-m]' # For ROT13 cipher
# Password: 7x16WNeHIi5YkIhWsfFIqoognUTyj9Q4
```

### Level 12
```bash
ssh bandit12@bandit.labs.overthewire.org -p 2220
# Password 7x16WNeHIi5YkIhWsfFIqoognUTyj9Q4
mktemp -d
cd temp_dir_that_was_created
cp ~/data.txt .
mv data.txt hexdump_data

# Decompress the file
xxd -r hexdump_data compressed_data

# Using the following page: https://en.wikipedia.org/wiki/List_of_file_signatures which corresponds to the first byte of the file of the hexdump
cat hexdump_data | head
# 00000000: 1f8b 0808 dfcd eb66 0203 6461 7461 322e  .......f..data2.
# 1f8b is the file type, which corresponds to a .gz file
```
The [hexdump_decompression.sh](../utils/hexdump_decompression.sh) file was used to decompress the 

```bash
# Password: FO5dwFsc0cbaIiH0h8J2eUks2vdTDwAn
```

### Level 13
```bash
ssh bandit13@bandit.labs.overthewire.org -p 2220
# Password FO5dwFsc0cbaIiH0h8J2eUks2vdTDwAn
```
Initial thoughs:
Use ssh to log into the localhose using the private key in order to impersonate bandit14
```bash
ssh bandit14@localhost -p 2220 -i sshkey.private
cat /etc/bandit_pass/bandit14
# Password: MU4VWeTyJk8ROof1qqmcBPaLh7lDCPvS
```

### Level 14
```bash
ssh bandit14@bandit.labs.overthewire.org -p 2220
# Password: MU4VWeTyJk8ROof1qqmcBPaLh7lDCPvS
nc -v localhost 30000
MU4VWeTyJk8ROof1qqmcBPaLh7lDCPvS


# Password: 8xCjnmgoKbGLhHFAZlGE5Tmu4M2tKJQo
```


### Level 15
```bash
ssh bandit15@bandit.labs.overthewire.org -p 2220
# Password: 8xCjnmgoKbGLhHFAZlGE5Tmu4M2tKJQo

ncat --ssl localhost 30001
8xCjnmgoKbGLhHFAZlGE5Tmu4M2tKJQo

# Password: kSkvUpMQ7lBYyCM4GBPvCvT1BfWRy0Dx
```

### Level 16
```bash
ssh bandit16@bandit.labs.overthewire.org -p 2220
# Password: kSkvUpMQ7lBYyCM4GBPvCvT1BfWRy0Dx
nmap -v -A localhost

```
```bash
#!/bin/bash
# Take first argument as command to run
# Take second argument as password to use
echo "This bash script takes a nmap command and tries to send the provided password via ssl with ncat."
command="$1"
password="$2"
port_array=()
while IFS= read -r line; do
if [[ "$line" =~ ^([0-9]*)\/.* ]]; then
port=${BASH_REMATCH[1]}
echo "$port"
port_array+=( "$port" )
fi
done < <( $command )
for i in "${!port_array[@]}";do
echo "$password" | ncat --ssl localhost ${port_array[i]}
done
```
```bash
# Password: 
-----BEGIN RSA PRIVATE KEY-----
MIIEogIBAAKCAQEAvmOkuifmMg6HL2YPIOjon6iWfbp7c3jx34YkYWqUH57SUdyJ
imZzeyGC0gtZPGujUSxiJSWI/oTqexh+cAMTSMlOJf7+BrJObArnxd9Y7YT2bRPQ
Ja6Lzb558YW3FZl87ORiO+rW4LCDCNd2lUvLE/GL2GWyuKN0K5iCd5TbtJzEkQTu
DSt2mcNn4rhAL+JFr56o4T6z8WWAW18BR6yGrMq7Q/kALHYW3OekePQAzL0VUYbW
JGTi65CxbCnzc/w4+mqQyvmzpWtMAzJTzAzQxNbkR2MBGySxDLrjg0LWN6sK7wNX
x0YVztz/zbIkPjfkU1jHS+9EbVNj+D1XFOJuaQIDAQABAoIBABagpxpM1aoLWfvD
KHcj10nqcoBc4oE11aFYQwik7xfW+24pRNuDE6SFthOar69jp5RlLwD1NhPx3iBl
J9nOM8OJ0VToum43UOS8YxF8WwhXriYGnc1sskbwpXOUDc9uX4+UESzH22P29ovd
d8WErY0gPxun8pbJLmxkAtWNhpMvfe0050vk9TL5wqbu9AlbssgTcCXkMQnPw9nC
YNN6DDP2lbcBrvgT9YCNL6C+ZKufD52yOQ9qOkwFTEQpjtF4uNtJom+asvlpmS8A
vLY9r60wYSvmZhNqBUrj7lyCtXMIu1kkd4w7F77k+DjHoAXyxcUp1DGL51sOmama
+TOWWgECgYEA8JtPxP0GRJ+IQkX262jM3dEIkza8ky5moIwUqYdsx0NxHgRRhORT
8c8hAuRBb2G82so8vUHk/fur85OEfc9TncnCY2crpoqsghifKLxrLgtT+qDpfZnx
SatLdt8GfQ85yA7hnWWJ2MxF3NaeSDm75Lsm+tBbAiyc9P2jGRNtMSkCgYEAypHd
HCctNi/FwjulhttFx/rHYKhLidZDFYeiE/v45bN4yFm8x7R/b0iE7KaszX+Exdvt
SghaTdcG0Knyw1bpJVyusavPzpaJMjdJ6tcFhVAbAjm7enCIvGCSx+X3l5SiWg0A
R57hJglezIiVjv3aGwHwvlZvtszK6zV6oXFAu0ECgYAbjo46T4hyP5tJi93V5HDi
Ttiek7xRVxUl+iU7rWkGAXFpMLFteQEsRr7PJ/lemmEY5eTDAFMLy9FL2m9oQWCg
R8VdwSk8r9FGLS+9aKcV5PI/WEKlwgXinB3OhYimtiG2Cg5JCqIZFHxD6MjEGOiu
L8ktHMPvodBwNsSBULpG0QKBgBAplTfC1HOnWiMGOU3KPwYWt0O6CdTkmJOmL8Ni
blh9elyZ9FsGxsgtRBXRsqXuz7wtsQAgLHxbdLq/ZJQ7YfzOKU4ZxEnabvXnvWkU
YOdjHdSOoKvDQNWu6ucyLRAWFuISeXw9a/9p7ftpxm0TSgyvmfLF2MIAEwyzRqaM
77pBAoGAMmjmIJdjp+Ez8duyn3ieo36yrttF5NSsJLAbxFpdlc1gvtGCWW+9Cq0b
dxviW8+TFVEBl1O4f7HVm6EpTscdDxU+bCXWkfjuRb7Dy9GOtt9JPsX8MBTakzh3
vBgsyi/sN3RqRBcGU40fOoZyfAMT8s1m/uYv52O6IgeuZ/ujbjY=
-----END RSA PRIVATE KEY-----
```

### Level 17
```bash
ssh bandit17@bandit.labs.overthewire.org -p 2220 -i sshkey.private
# Pasword: private key from level 16
diff passwords.new passwords.old
# Password: x2gLTTjFwMOhQ8oWNbMN362QKxfRqGlO
```

### Level 18
```bash
ssh bandit18@bandit.labs.overthewire.org -p 2220 -f "cat readme"
# Password: x2gLTTjFwMOhQ8oWNbMN362QKxfRqGlO

# Password: cGWpMaKXVwDUNgPAVJbWYuGHVn9zl3j8
```

### Level 19
```bash
ssh bandit19@bandit.labs.overthewire.org -p 2220
# Password: cGWpMaKXVwDUNgPAVJbWYuGHVn9zl3j8
./bandit20-do cat /etc/bandit_pass/bandit20

# Password: 0qXahG8ZjOVMN9Ghs7iOWsCfZyXOUbYO
```

### Level 20
```bash
ssh bandit20@bandit.labs.overthewire.org -p 2220
# Password: 0qXahG8ZjOVMN9Ghs7iOWsCfZyXOUbYO
tmux new-session
### New tmux session ###
nc -l 12345 < /etc/bandit_pass/bandit20
# Ctrl + b + d to detatch from session without killing it
./suconnect 12345
# connect back to tmux session
tmux attach session
# Password: EeoULMCra2q0dSkYj561DX7s1CpBuOBt
```

### Level 21
```bash
ssh bandit21@bandit.labs.overthewire.org -p 2220
# Password: EeoULMCra2q0dSkYj561DX7s1CpBuOBt
ls /etc/cron.d
cat /etc/cron.d/cronjob_bandit22
cat /usr/bin/cronjob_bandit22.sh
cat /tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv
# Password: tRae0UfB9v0UzbCdn9cY0gQnds9GF58Q
```

### Level 22
```bash
ssh bandit22@bandit.labs.overthewire.org -p 2220
# Password: tRae0UfB9v0UzbCdn9cY0gQnds9GF58Q
ls /etc/cron.d
cat /etc/cron.d/cronjob_bandit23
cat /usr/bin/cronjob_bandit23.sh
# After reading through the cronjob, it looks like the user creates a hash from the first string and cuts away the white space, before saving the password to the file at /tmp/$hash.
# The hash is equal to: $(echo I am user bandit23 | md5sum | cut -d ' ' -f 1)
cat /tmp/$(echo I am user bandit23 | md5sum | cut -d ' ' -f 1) 

# Password: 0Zf11ioIjMVN551jX3CmStKLYqjk54Ga
```

### Level 23
```bash
ssh bandit23@bandit.labs.overthewire.org -p 2220
# Password: 0Zf11ioIjMVN551jX3CmStKLYqjk54Ga
ls /etc/cron.d
cat /etc/cron.d/cronjob_bandit24
cat /usr/bin/cronjob_bandit24.sh

# Will need to write a shell script that cats out the password file and saves it to the temp folder
mktemp -d
cd # temp dir
# Very scuffed way of doing things here. We're going to need two ssh sessions open both in the temp dir
# ssh session 1
nc -l -p 50860 -q 1 > password.txt < /dev/null
# ssh session 2
chmod 0760 # new temp directory
touch script.sh
chmod +x script.sh
vim script.sh
### SCRIPT
#!/bin/bash
cat /etc/bandit_pass/bandit24 | netcat localhost 50860
# ls -al /etc/bandit_pass > /tmp/tmp.ZnvbxGaVfo/password_perms.txt
# cat /etc/bandit_pass/bandit24 > /tmp/tmp.kd9eVN0u6z/password.txt
### SCRIPT
cp script.sh run.sh
mv run.sh /var/spool/bandit24/foo

# password: gb8KRRCsshuZXI0tUuR6ypOFjiZbf3G8
```

### Level 24
```bash
ssh bandit24@bandit.labs.overthewire.org -p 2220
# password: gb8KRRCsshuZXI0tUuR6ypOFjiZbf3G8

### script
mktemp -d
cd # temp dir
touch run.sh && chmod +x run.sh  && vim run.sh
### SCRIPT
# This forloop creates 10000 combinations of the 4 digit password
for i in $(seq 0 1 9);
do
    for j in $(seq 0 1 9);
    do
        for k in $(seq 0 1 9);
        do
            for l in $(seq 0 1 9);
            do
                echo "$i$j$k$l"
                echo "gb8KRRCsshuZXI0tUuR6ypOFjiZbf3G8 $i$j$k$l" >> attempts.txt
            done
        done
    done
done
cat attempts.txt | netcat localhost 30002 
### SCRIPT
./run.sh

# Password: iCi86ttT4KSNe1armKiwbQNmB3YJP3q4
```

### Level 25
```bash
ssh bandit25@bandit.labs.overthewire.org -p 2220
# password: iCi86ttT4KSNe1armKiwbQNmB3YJP3q4
mktemp -d
cd # temp dir
cat /etc/passwd | grep bandit26
cat /usr/bin/showtext
# In CMD with a shrunken screen, more requires a small screen in order to work properly if your screen is larger than the total page size
ssh bandit26@bandit.labs.overthewire.org -p 2220 -i bandit26.sshkey
# press "v" to go into vim from more
# press ":e /etc/band_pass/bandit26 to edit the bandit26 password file
# password: s0773xxkk0MXfdqOfPRVr9L3jJBUOgCZ
```

### Level 26
```bash
ssh bandit26@bandit.labs.overthewire.org -p 2220
# password: s0773xxkk0MXfdqOfPRVr9L3jJBUOgCZ