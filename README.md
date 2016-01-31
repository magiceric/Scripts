# Scripts
My simple scrits for everything

##getFirstKinopoiskMovie.py
This simple script just find a first movie id on http://kinopoisk.ru

##partition.py
Partition STDIN by NUMBER of lines and put them into given string with delimeter.
####Usage
```bash
python3 partition.py NUMBER REPLACE_STRING DELIMETER STRING_TO_INSERT_DATA
```

####For exampe
We have file with database identificators and would like to update data in table by this ids. But there are lots of ids and you would like to split them by 100.

```bash
cat merge.csv | python3 partition.py 2 __id__ '","' 'UPDATE wm2.catalog_good SET yml_id=7841 WHERE yml_id=2816 AND own_id IN ("__id__"); COMMIT;' > wm2.catalog_good.sql
```
#####Where

`merge.csv` -  file where you store identificators looks like:
```
1
2
3
45
33
```

`2` - partiton size (how many ids should be in 1 update)

`__id__` - string to replace in STRING_TO_INSERT_DATA

`'","'` - delimeter

`UPDATE wm2.catalog_good SET yml_id=7841 WHERE yml_id=2816 AND own_id IN ("__id__"); COMMIT;'` - string where we place our ids from `merge.csv`, at place marked as `__id__` with delimeter `'","'` splitted by 2 elements

#####Result
File with content like:
```sql
UPDATE wm2.catalog_good SET yml_id=7841 WHERE yml_id=2816 AND own_id IN ("1", "2"); COMMIT;
UPDATE wm2.catalog_good SET yml_id=7841 WHERE yml_id=2816 AND own_id IN ("3", "45"); COMMIT;
UPDATE wm2.catalog_good SET yml_id=7841 WHERE yml_id=2816 AND own_id IN ("33"); COMMIT;
```

##tail-via-http.sh
Emulate tail over http. To get updatable data via http. Useful if you have access to logs only over http. 
####Usage
```bash
./tail-via-http.sh http://server.io/access.log OFFSET UPDATE_TIME
```
####Exapmle
You have log on server http://server.io/access.log
```bash
./tail-via-http.sh http://server.io/access.log 30000 1
```
#####Where
`http://server.io/access.log` - file address

`30000` - offset in 30000 bytes

`1` - file will update every 1 second

#####Result
You viewing file updates in realtime. Like you use `tail -f` command


#For Alexey Baskinov

##English/practice-and-check.sh
Small script for composing an html-page for practice and check your english.
Get tab-separated words from clipboard and compose page like example.html
Useful on mobile phones. 

##English/uploadHomework.py
Small python script to get english homework fron ya.disk and download it to nginx folder. (To easy access from mobile devices)

