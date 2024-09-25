#!/bin/bash
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

# Invoke first function
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