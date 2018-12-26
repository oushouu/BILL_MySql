
# coding: utf-8

# In[1]:


import pandas as pd
import pymysql.cursors


# In[2]:


conn = pymysql.connect(host='localhost',
                             user='root',
                             password='systemsss',
                             db='testdb',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)


# In[3]:


name_para = 'null'


# In[4]:


sql = """SELECT id, password, name, slack_name FROM pass WHERE slack_name = %(name_para)s;"""


# In[5]:


df = pd.read_sql(sql, conn, params = {'name_para': name_para})


# In[6]:


df


# In[7]:


conn.close()

