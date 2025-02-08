import pandas as pd
sales = pd.read_csv('sales.csv')
# Answering some question using data presented in the data file using sql and python 
#1) Which branch has the highest and lowest sales? 
# and represent the on bar graph , also show the market share for 
# each location using pie chart 
sales.groupby('Location').sum()['Total']
# now we plot the sales on bar graph 
location_list = sales.groupby('Location')
location = [x for x,y in location_list]
location
# importing matplotlib.pyplot as plt 
import matplotlib.pyplot as plt 
plt.bar(location,sales.groupby('Location').sum()['Total'])
plt.show()
# ploting the market share on the pie chart 
plt.pie(sales.groupby('Location').sum()['Total'], labels=location, autopct='%1.1f%%')
plt.show()
#2) which location has more female customers and which location has more  male 

location_sales = sales.groupby(['Location','Gender']).count()['Invoice ID']
unstacked_sales = location_sales.unstack(level=0)
unstacked_sales.plot(kind= 'bar')
#3) 
#3.1) Which branch has more members vs which has less members ?
#3.2) which branch has highest rating and which has lowest?

# 3.1
members = location_sales = sales.groupby(['Member','Location']).count()['Invoice ID']
members.unstack(level=0).plot(kind='bar')
#3.2
rating = sales.groupby('Location')['Rating'].mean()
rating.plot(kind='bar')
plt.show()

#4) 
#4.1) Which city has more females shopping?
#4.2) Who spends more men or women?
#4.3) Which type of customer spends more member or non-member?
#4.4) Which product line sells more?
#4.5) Which product line is popular among men vs women

#4.1)
female_shoppers = sales.groupby(['City','Gender']).count()['Invoice ID']
female_shoppers.unstack(level=0).plot(kind='bar')
#4.2)
spend = sales.groupby('Gender').sum()['Total']
spend.plot(kind='bar')
plt.show()
#4.3)

Member = sales.groupby('Member').sum()['Total']
Member
import matplotlib.pyplot as plt
Member.plot(kind= 'bar')
plt.show()

#4.4)

category_sales = sales.groupby('Category').count()['Rating']
category_sales.plot(kind='bar')
plt.show()
#4.5)
sales_m_w = sales.groupby(['Gender','Category']).count()['Rating']
sales_m_w.unstack(level=1).plot(kind='bar')
plt.show()
#5) 
#5.1) what days of the month make most the sales
sales['Day']= pd.to_datetime(sales['Date']).dt.day
day_sales= sales.groupby('Day').sum()['Total']
day_sales.plot()
plt.show()

#5.2)  what  month make most the sales
sales['Month']= pd.to_datetime(sales['Date']).dt.month
Month_sales= sales.groupby('Month').sum()['Total']
Month_sales.plot(kind = 'bar')
plt.show()
#5.3)  what  hours  make most the sales
sales['Hour']= pd.to_datetime(sales['Time']).dt.hour
Hour_sales= sales.groupby('Hour').sum()['Total']
Hour_sales.plot(grid = True)
plt.show()
#5.4) what time people make more epayments and cash payment ?
sales.groupby(['Payment', 'Hour']).count()['Invoice ID'].unstack(level=0).plot(kind= 'bar')
