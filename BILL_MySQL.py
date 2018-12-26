
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


import matplotlib.pyplot as plt


# In[3]:


import pymysql.cursors


# In[4]:


conn = pymysql.connect(host='localhost',
                             user='root',
                             password='systemsss',
                             db='testdb',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)


# In[5]:


df = pd.read_sql('SELECT date, AVG(total), SUM(total), MAX(total), MIN(total) FROM bill WHERE date BETWEEN \'2018-07-01\' AND \'2018-07-31\' GROUP BY date', conn)


# In[6]:


ddate = df['date']
statis = ('total','SUM(total)','MAX(total)','MIN(total)','AVG(total)')
labels = list()

for sta in statis:
    if sta in df.columns:        
        sta = sta.replace('SUM(total)', '総計申請金額')
        sta = sta.replace('MAX(total)', '最大申請金額')
        sta = sta.replace('MIN(total)', '最小申請金額')
        sta = sta.replace('AVG(total)', '平均申請金額')
        labels.append(sta)


# In[7]:


if 'total' in df.columns:
    iftotal = 1
    dtotal = df['total']
else:
    iftotal = 0

if 'SUM(total)' in df.columns:
    ifsum = 1
    dsum = df['SUM(total)']
else:
    ifsum = 0
    
if 'MAX(total)' in df.columns:
    ifmax = 1
    dmax = df['MAX(total)']
else:
    ifmax = 0
    
if 'MIN(total)' in df.columns:
    ifmin = 1
    dmin = df['MIN(total)']
else:
    ifmin = 0
    
if 'AVG(total)' in df.columns:
    ifavg = 1
    davg = df['AVG(total)']
else:
    ifavg = 0
    
#print(iftotal)
#print(ifsum)
#print(ifmax)
#print(ifmin)
#print(ifavg)
plt.style.use('ggplot')


# In[8]:


plt.figure(figsize=(20,10))
plt.plot(ddate,dsum)
plt.plot(ddate,dmax)
plt.plot(ddate,dmin)
plt.plot(ddate,davg)
plt.xlabel('日付')
plt.ylabel('円')
plt.title('経費統計折り線図')
plt.legend(labels)
plt.savefig('desktop/foo.png')
plt.show()


# In[9]:


df


# In[10]:


df.to_html('desktop/view.html')


# In[11]:


#Pie and Bar Chart


# In[12]:


start_date = '2018-07-01'
end_date = '2018-07-31'


# In[13]:


sql = """SELECT person, AVG(total), SUM(total), MAX(total), MIN(total) FROM bill WHERE date BETWEEN %(start_date)s AND %(end_date)s GROUP BY person;"""


# In[14]:


df1 = pd.read_sql(sql, conn, params = {'start_date': start_date, 'end_date': end_date})


# In[15]:


df1


# In[16]:


pie_data = df1['SUM(total)']
bar_data = df1['AVG(total)']
labels1 = df1['person']
plt.style.use('ggplot')


# In[17]:


import numpy as np
def func(pct, allvals):
    absolute = int(pct/100*np.sum(allvals))
    return "{:.1f}%\n({:d} 円)".format(pct, absolute)


# In[18]:


explode = list()
for k in labels1:
    explode.append(0.05)


# In[19]:


plt.figure(figsize=(20,10))

plt.subplot(1,2,1) #set 1 row, 2 columns, 1st place
plt.pie(pie_data , shadow=True, startangle=90, autopct=lambda pct: func(pct, pie_data), explode = explode)
plt.title("個人申請経費_総計")
plt.axis("equal")
plt.legend(labels1)

plt.subplot(1,2,2) #set 1 row, 2 columns, 2ed place
plt.bar(labels1, bar_data)
plt.style.use('ggplot')
for xx, yy in zip(labels1,bar_data):
    plt.text(xx, yy, str(round(yy))+"円", ha='center')
plt.title("個人申請経費_一回当たり")
plt.savefig('desktop/charts.png')
plt.show()


# In[20]:


# wordcloud


# In[21]:


sql = """SELECT name, COUNT(name) FROM bill WHERE date BETWEEN %(start_date)s AND %(end_date)s GROUP BY name;"""


# In[22]:


df2 = pd.read_sql(sql, conn, params = {'start_date': start_date, 'end_date': end_date})


# In[23]:


df2


# In[24]:


from pyecharts import WordCloud #事前にAnaconda Terminalでpip install pyecharts必要
name_list = []
count_list = []
for name in df2['name']:
    name_list.append(name)
for count in df2['COUNT(name)']:
    count_list.append(count)
    
wordcloud = WordCloud("消費の場所",width=900, height=500)
wordcloud.add("", name_list, count_list, word_size_range=[20,80])
wordcloud.render(path='desktop/view.html')
wordcloud


# In[25]:


conn.close()

