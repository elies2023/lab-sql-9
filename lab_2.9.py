#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# lab 2.9


# In[1]:


import pandas as pd
import numpy as np

import pymysql                        # for getting data from a SQL database
from sqlalchemy import create_engine  # for establishing the connection and authentication

from getpass import getpass  # To get the password without showing the input


# In[2]:


password = getpass()


# In[47]:


connection_string = 'mysql+pymysql://root:'+password+'@localhost/sakila'
engine = create_engine(connection_string)


# In[48]:


type(engine)


# In[49]:


data = pd.read_sql_query('SELECT * FROM sakila.actor', engine)
data.head() 


# In[6]:


#1.How many distinct (different) actors' last names are there?


# In[11]:


query = '''select count(distinct last_name) as "different last_name"
from sakila.actor;'''

data = pd.read_sql_query(query, engine)
data.head()


# In[ ]:


## Add an additional column day_type with values 'weekend' and 'workday' depending on the rental day of the week.


# In[46]:


query = '''SELECT *, 
CASE 
WHEN DATE_FORMAT(rental_date,'%%a') = 'Sat' then 'Weekend'
WHEN DATE_FORMAT(rental_date,'%%a') = 'Sun' then 'Weekend'
ELSE 'Weekday'
END AS day_type
from sakila.rental;'''
print(query)
data = pd.read_sql_query(query, engine)
data


# In[31]:


data['day_type'].tail(50)


# In[22]:



query = "SELECT title FROM sakila.film WHERE title LIKE '%%ARMAGEDDON%%'"

# execute the SQL query using pandas read_sql_query() function
data = pd.read_sql_query(query, engine)

# print the first few rows of the result set
data.head()


# In[25]:


query = "SELECT title, length FROM sakila.film ORDER BY length DESC LIMIT 10;"
data = pd.read_sql_query(query, engine)
data.head()


# In[38]:


query ="select count(special_features) from sakila.film where special_features like '%%Behind the Scenes%%'"
data = pd.read_sql_query(query, engine)
data.head()


# In[41]:


query="SELECT Rating, AVG(Length) AS Mean_Length FROM sakila.film GROUP BY Rating HAVING Mean_Length > 120"
data = pd.read_sql_query(query, engine)
data.head()


# In[44]:


#Rank films by length (filter out the rows that have nulls or 0s in length column). In your output, only select the columns title, length, and the rank

query="SELECT Title, Length, RANK() OVER (ORDER BY Length DESC) AS 'Rank' FROM sakila.film WHERE Length IS NOT NULL AND Length > 0;"
data = pd.read_sql_query(query, engine)
data.head(50)


# In[ ]:




