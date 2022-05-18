import cbpro
import sys
from csv import writer
from time import sleep
from os.path import exists
import setproctitle

from datetime import datetime

setproctitle.setproctitle(sys.argv[1])

c = cbpro.PublicClient()

#datetime_object = datetime.datetime.now()
print('herewego')

olddatetimeString = 0
exchange = (sys.argv[1])

while 1:
    ticker_old = c.get_product_ticker(product_id=exchange)
    datetimeString = ticker_old.get("time")
    price = ticker_old.get("price")
    if (datetimeString != olddatetimeString):
        olddatetimeString = datetimeString
        date = datetimeString.split('T')[0]
        time = datetimeString.split('T')[1]
        year = int(date.split('-')[0])
        month = int(date.split('-')[1])
        day = int(date.split('-')[2])
        hour = int(time.split(':')[0])
        minute = int(time.split(':')[1])
        second = int(time.split(':')[2].split('.')[0])
        microsecond = int(time.split(':')[2].split('.')[1][:-1])
        p = datetime(year,month,day,hour,minute,second,microsecond)
        ts = p.timestamp()

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
                writer_object.writerow(('Time','Price','UnixTime'))
                # Close the file object
                f_object.close()
                print('file created')

        with open(filename, 'a', newline='') as f_object:  
            # Pass the CSV  file object to the writer() function
            writer_object = writer(f_object)
            # Result - a writer object
            # Pass the data in the list as an argument into the writerow() function
            writer_object.writerow((time,price,ts))
            # Close the file object
            f_object.close()
    sleep(5)

