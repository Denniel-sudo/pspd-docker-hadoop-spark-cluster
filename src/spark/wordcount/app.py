#!/usr/bin/env python3

from datetime import datetime
import sys
from operator import add

from pyspark.sql import SparkSession

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: wordcount <file>", file=sys.stderr)
        sys.exit(-1)

    start = datetime.now()
    
    spark = SparkSession\
        .builder\
        .appName("PythonWordCount")\
        .getOrCreate()

    lines = spark.read.text(sys.argv[1]).rdd.map(lambda r: r[0])

    counts = lines.flatMap(lambda x: x.split()) \
                  .map(lambda x: ('word', 1)) \
                  .reduceByKey(add)
    output = counts.collect()
    
    for (word, count) in output:
        print("%s: %i" % (word, count))
    spark.stop()
    print('[-------------------DONE--------------------]\nexecution time: ', (datetime.now().timestamp() - start.timestamp()))