import os
import time
import pandas

filepath = 'files/temp.csv'
while True:
    if os.path.exists(filepath):
        # with open(filepath) as file:
        #     print(file.read())
        data = pandas.read_csv(filepath)
        print (type(data))
        print (data)
        print ('The mean is \n {}'.format(data.mean()))
        print('Station one: {}'.format(data.mean()['st1']))
        break
    else:
        print('File {} not found'.format(filepath))
    time.sleep(2)