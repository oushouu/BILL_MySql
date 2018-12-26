
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


import pymysql.cursors


# In[3]:


conn = pymysql.connect(host='localhost',
                             user='root',
                             password='systemsss',
                             db='testdb',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)


# In[4]:


total_para='582'
date_para='2018/5/28'
name_para='ハンズビーアトレ秋葉原1店'
person_para='入江 和也'


# In[5]:


cur = conn.cursor() 


# In[6]:


def insert(var_1, var_2, var_3, var_4):
    cur.execute("""
        INSERT INTO bill
        VALUES (%s, %s, %s, %s);
        """,
        (var_1, var_2, var_3, var_4)
    )


# In[7]:


try: 
    insert(date_para, total_para, name_para, person_para)
    print('insert success')
except:
    print('insert error')


# In[8]:


conn.commit()


# In[9]:


conn.close()

