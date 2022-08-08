all:
	hdfs dfs -mkdir -p /user/root
	hdfs dfs -put hello.txt /user/root/
	./user_data/generate_file/random_words.py

generate-input:
	./user_data/generate_file/random_words.py

# SPARK
# 117.32606601715088 s
spark-wordcount-1: 
	spark-submit --master local[1] /user_data/spark/wordcount/app.py hello.txt
# 70.0228099822998 s
spark-wordcount-2: 
	spark-submit --master local[2] /user_data/spark/wordcount/app.py hello.txt
# 43.94349789619446 s
spark-wordcount-5: 
	spark-submit --master local[5] /user_data/spark/wordcount/app.py hello.txt

# 134.02645421028137 s
spark-wordfreq-1: 
	spark-submit --master local[1] /user_data/spark/wordfreq/app.py hello.txt 
# 81.25302600860596 s
spark-wordfreq-2: 
	spark-submit --master local[2] /user_data/spark/wordfreq/app.py hello.txt
# 47.46495199203491 s
spark-wordfreq-5: 
	spark-submit --master local[5] /user_data/spark/wordfreq/app.py hello.txt

# 153.59588980674744 s
spark-spr_freq_count-1: 
	spark-submit --master local[1] /user_data/spark/spr_freq_count/app.py hello.txt 
# 88.21424317359924 s
spark-spr_freq_count-2: 
	spark-submit --master local[2] /user_data/spark/spr_freq_count/app.py hello.txt
# 56.14523100852966 s
spark-spr_freq_count-5: 
	spark-submit --master local[5] /user_data/spark/spr_freq_count/app.py hello.txt

# 146.3046190738678 s
spark-len_string-1: 
	spark-submit --master local[1] /user_data/spark/len_string/app.py hello.txt 
# 83.88262414932251 s
spark-len_string-2: 
	spark-submit --master local[2] /user_data/spark/len_string/app.py hello.txt
# 51.32920598983765 s
spark-len_string-5: 
	spark-submit --master local[5] /user_data/spark/len_string/app.py hello.txt

# HADOOP
# 1 - 3mins, 24sec
# 2 -	2mins, 24sec
# 5 - 2mins, 28sec
hadoop-wordcount: 
	cd /user_data/hadoop/wordcount && mapred streaming -files mapper.py,reducer.py \
	-mapper mapper.py \
	-reducer reducer.py \
	-input /user/root/hello.txt \
	-output /output/ \
	&& cd /user_data/

# 1 - 3mins, 45sec
# 2 - 2mins, 49sec
# 5 - 2mins, 50sec
hadoop-wordfreq: 
	cd /user_data/hadoop/wordfreq && mapred streaming -files mapper.py,reducer.py \
	-mapper mapper.py \
	-reducer reducer.py \
	-input /user/root/hello.txt \
	-output /output/ \
	&& cd /user_data/

# 1 - 59sec
# 2 - 48sec
# 5 - 1mins, 0sec
hadoop-spr_freq_count: 
	cd /user_data/hadoop/spr_freq_count && mapred streaming -files mapper.py,reducer.py \
	-mapper mapper.py \
	-reducer reducer.py \
	-input /user/root/hello.txt \
	-output /output/ \
	&& cd /user_data/

# 1 - 1mins, 4sec
# 2 - 1mins, 3sec
# 5 - 59sec
hadoop-len_string: 
	cd /user_data/hadoop/len_string && mapred streaming -files mapper.py,reducer.py \
	-mapper mapper.py \
	-reducer reducer.py \
	-input /user/root/hello.txt \
	-output /output/ \
	&& cd /user_data/

hadoop-result:
	hdfs dfs -get /output/ /output/
	hdfs dfs -rm -r /output/
