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
The following file was created to unpack different compressed files:
```sh
#! /bin/bash
function first_check() {
type=$(file hexdump_data | grep ASCII)
result=$?
if [ $result -eq 0 ]
then
search=$(cat hexdump_data | head | grep  1f8b)
if [ -z  "$search" ]
then
echo "not gz"
search=$(cat hexdump_data | head | grep  425a)
if [ -z  "$search" ]
then
echo "not bz2"
else
echo "bz2"
xxd -r hexdump_data compressed_data
mv compressed_data compressed_data.bz2
bzip2 -d compressed_data.bz2
xxd compressed_data hexdump_data
fi
else
echo "gz"
xxd -r hexdump_data compressed_data
mv compressed_data compressed_data.gz
gzip -d compressed_data.gz
xxd compressed_data hexdump_data
fi
fi
}

first_check

input=true
while [ input ]
do
type=$(file compressed_data | grep  gzip)
result=$?
if [ $result -eq 0 ]
then
echo "gz"
xxd -r hexdump_data compressed_data
mv compressed_data compressed_data.gz
gzip -d compressed_data.gz
xxd compressed_data hexdump_data
fi
type=$(file compressed_data | grep  bzip2)
result=$?
if [ $result -eq 0 ]
then
echo "bz2"
xxd -r hexdump_data compressed_data
mv compressed_data compressed_data.bz2
bzip2 -d compressed_data.bz2
xxd compressed_data hexdump_data
fi

type=$(file compressed_data | grep  tar)
result=$?
if [ $result -eq 0 ]
then
echo "tar"
xxd -r hexdump_data compressed_data
mv compressed_data compressed_data.tar
mv $(tar -xvf compressed_data.tar) compressed_data
xxd compressed_data hexdump_data
fi

cat hexdump_data
read -p "continue?" input
done
```
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