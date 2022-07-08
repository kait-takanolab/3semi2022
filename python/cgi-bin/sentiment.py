# -*- coding: utf-8 -*-
from transformers import pipeline, AutoModelForSequenceClassification, BertJapaneseTokenizer
import mysql.connector

bert_model_ja = AutoModelForSequenceClassification.from_pretrained('daigo/bert-base-japanese-sentiment') 
tokenizer_ja = BertJapaneseTokenizer.from_pretrained('cl-tohoku/bert-base-japanese-whole-word-masking')
analyzer_ja = pipeline("sentiment-analysis",model=bert_model_ja,tokenizer=tokenizer_ja)

import cgi, cgitb
form = cgi.FieldStorage()

# Get data from fields
usermsg = form.getvalue('usermsg')

print ("Content-Type: text/plain")
print ("\n")

# print(analyzer_ja("今日のセミナーは楽しい"))
# print(analyzer_ja("先生がいなくて悲しい"))

print(usermsg + "の結果\n")
print(analyzer_ja(usermsg))

print ("Connecting to MySQL....")

sql= ( "insert into sentiment (sentence,posinega,score)" 
       " values (%s, %s, %s);")

sql_data = (usermsg, 0, 0.80)

try:
  cnx = mysql.connector.connect(user='root', password='',
                              host='localhost',
                              database='3semi2022')
  cursor = cnx.cursor()
  cursor.execute(sql, sql_data)

except mysql.connector.Error as err:
  print("DB connection error {}".format(err) )

print("Exit.")
cnx.commit()

cursor.close()
cnx.close()