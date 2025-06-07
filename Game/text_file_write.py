#import datetime and random
import datetime
import random

#use a function to create file name
def statistics(text):
# Get the current date
    current_date = datetime.datetime.now().strftime("%Y_%m_%d")

# Get the current time
    current_time = datetime.datetime.now().strftime("%H_%M_%S")

# Generate a random number between 0000 and 9999
    random_number = str(random.randrange(0,10000)).zfill(4)

# Combine the parts
    text_file_name = f"{current_date}_{current_time}_{random_number}.txt"



    #write in text file
    with open(text_file_name,"w") as fo:
        fo.write(text)
