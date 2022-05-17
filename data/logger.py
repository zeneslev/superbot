import cbpro
import sys
from csv import writer
from time import sleep
from os.path import exists

import datetime

c = cbpro.PublicClient()

#datetime_object = datetime.datetime.now()
print('herewego')

olddatetime = 0
exchange = (sys.argv[1])

while 1:
    ticker_old = c.get_product_ticker(product_id=exchange)
    datetime = ticker_old.get("time")
    price = ticker_old.get("price")
    if (datetime != olddatetime):
        olddatetime = datetime
        date = datetime.split('T')[0]
        time = datetime.split('T')[1]

        #check if file exists. If it doesn't then make it
        #filename should be something like UST-USD-2022-05-16
        filename = date + '-' + exchange + '.csv'

        if (not(exists(filename))):
            with open(filename, 'a', newline='') as f_object:  
                # Pass the CSV  file object to the writer() function
                writer_object = writer(f_object)
                # Result - a writer object
                # Pass the data in the list as an argument into the writerow() function
                writer_object.writerow((date,exchange))
                # Close the file object
                f_object.close()
                print('file created')

        with open(filename, 'a', newline='') as f_object:  
            # Pass the CSV  file object to the writer() function
            writer_object = writer(f_object)
            # Result - a writer object
            # Pass the data in the list as an argument into the writerow() function
            writer_object.writerow((time,price))
            # Close the file object
            f_object.close()
    sleep(5)

