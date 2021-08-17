# Databricks notebook source
with open('log4j-active.txt') as json_file:
  print('HelloWorld')

# COMMAND ----------

with open('log4j-active.txt','w') as json_file:
  print('HelloWorld')

# COMMAND ----------

with open('file.txt') as json_file:
  print('HelloWorld')

# COMMAND ----------

with open('file.txt','w') as json_file:
  print('HelloWorld')

# COMMAND ----------

# MAGIC %sh ls

# COMMAND ----------

data = {}
data['people'] = []
data['people'].append({
    'name': 'Scott',
    'website': 'stackabuse.com',
    'from': 'Nebraska'
})
data['people'].append({
    'name': 'Larry',
    'website': 'google.com',
    'from': 'Michigan'
})
data['people'].append({
    'name': 'Tim',
    'website': 'apple.com',
    'from': 'Alabama'
})

with open('data.txt', 'w') as outfile:
    json.dump(data, outfile)

# COMMAND ----------

my_file_handle=open("file.txt")
my_file_handle.read()

# COMMAND ----------

save_path = 's3://srihasr-test'
file_name = "test.txt"

completeName = os.path.join(save_path, file_name)
print(completeName)


file1 = open(completeName, "w")
file1.write("file information")
file1.close()
