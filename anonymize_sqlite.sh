#!/bin/bash

if [ "$#" -ne 1 ]; then
    echo "Usage: ./anonymize_sqlite.sh [database.db]"
    exit;
fi

cp $1 anonymized_$1

cat << EOF | sqlite3 anonymized_$1
update tasks set name=substr(quote(randomblob(20)), 3, 19), content=substr(quote(randomblob(20)), 3, 19), uuid="", additional_entries="";
update tag set name=substr(quote(randomblob(20)), 3, 19);
update special_lists set name=substr(quote(randomblob(20)), 3, 19);
update lists set name=substr(quote(randomblob(20)), 3, 19);
update semantic_conditions set condition=substr(quote(randomblob(20)), 3, 19);


EOF
echo "Success!"
echo "Please send us now the file anonymized_$1 to mirakel@azapps.de"
