import re
import pandas as pd

df = pd.read_csv('car(1).data', encoding_errors='ignore', sep=',')

print(df.head())

print(df.tail())

print(df.company.unique().size)

print(df.loc[df.company == 'toyota'])

df['price'] = pd.to_numeric(df['price'], errors='coerce', downcast='integer').fillna(0).astype('int')

cars = df.groupby('company')
print(cars['company'].count())
print(cars['price'].max())

#Cars['company'].value_counts()
# print(cars.groups)

print(df.loc[df['price'].idxmax()])


#############################
##########REGEX##############

pattern_num = '[0-9]{1,3}(,[0-9]{3})*(\.[0-9]+)?\b|\.[0-9]+\b'

Data1 = '34.54  Hello world, it’s time 01:12:22 41,432,454  to go to 32,345 out 134  23,234,233,430  02:22:13  11,11,11'


Data2 = "Hello this is the end. That is another one"
number = []
number = re.findall('(\d{1,3}(?:,\d{3})+)', Data1)

time = re.findall('[0-9]{1,2}:[0-9]{1,2}:[0-9]{1,2}',Data1)

words = re.findall('[a-zA-Z]+', Data2)