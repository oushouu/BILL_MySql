
# coding: utf-8

# In[1]:


#difine dictionary context
text_inshokudai =["丼もの","牛丼","親子丼","和風居酒屋"]
text_kaigihi = ["サンドイッチ","カフェ","コーヒー専門店","サンドイッチ"]
text_zapi = ["ホームセンター","宅配便","コンビニ"]


# In[2]:


#difine dictionary
dict_jiyu = {
    '飲食代': text_inshokudai,
    '会議費': text_kaigihi,
    '雑費': text_zapi
}


# In[3]:


ShopTypeStr = 'ホームセンタ'


# In[4]:


ShopTypeList=ShopTypeStr.split(",") #Transfer String to List
print(ShopTypeList)


# In[5]:


#define selector function
def jiyu_classifier(type):
    for jiyu in dict_jiyu:
        text = dict_jiyu.get(jiyu)
        for key in ShopTypeList:
            if key in text:
                print(jiyu)
                result = jiyu
                print(text)
                print(key)
                break
    return result

try:
    reason = jiyu_classifier(ShopTypeList)
except:
    print("not found")
    reason = "その他"


# In[6]:


reason

