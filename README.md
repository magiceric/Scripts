# Scripts
My simple scrits for everything

1. getFirstKinopoiskMovie.py
This simple script just find a first movie id on http://kinopoisk.ru

2. partition.py
Partition STDIN by NUMBER of lines and put them into given string with delimeter.
Usage:
```bash
python3 partition.py NUMBER REPLACE_STRING DELIMETER STRING_TO_INSERT_DATA
```

For exampe:
We have file with database identificators and would like to update data in table by this ids. But there are lots of ids and you would like to split them by 100.

```
cat merge.csv | python3 partition.py 100 __id__ '","' 'UPDATE wm2.catalog_good SET yml_id=7841 WHERE yml_id=2816 AND own_id IN ("__id__"); COMMIT;' > wm2.catalog_good.sql
```
Where:

`merge.csv` -  file where you store identificators looks like:
```
1
2
3
45
33
```
100 - partiton size (how many ids should be in 1 update)





3. English/practice-and-check.sh
Small script for composing an html-page for practice and check your english.
Get tab-separated words from clipboard and compose page like example.html
Useful on mobile phones. For Alexander Baskinov.

4. English/uploadHomework.py
Small python script to get english homework fron ya.disk and download it to nginx folder. (To easy access from mobile devices)

