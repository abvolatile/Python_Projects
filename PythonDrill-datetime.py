#
# PYTHON:   version 2.7.13
# AUTHOR:   Annie M Bowman
# PURPOSE:  Tech Academy Python Course DRILL #62
#               Use datetime to get local time in NY & London 
#               based on current time @ Portland HQ and check
#               to see whether NY and/or London branches are open
#               (all branches are open from 9am to 9pm local time)
#

from datetime import *

def open_or_closed():
    portland_time = datetime.now().strftime('%H:%M')
    (h, m) = portland_time.split(':')
    
    check = True
    while check:
        print "Welcome to HQ! The current time in Portland is {}.\n".format(portland_time)
        branch = raw_input("We also have branches in New York and London!"
                           "\nAll branches are open from 09:00 to 21:00 local time."
                           "\n\nTo find out if your local branch is open right now,"
                           "\ntype in the city name: ").title()
        if branch == 'New York':
            if h >= '00' and h < '21':
                    ny_chg = int(h) + 3
            elif h >= '21':
                    ny_chg = '0'+str(int(h) - 21)
            ny_time = ':'.join([str(ny_chg), m])
            
            if portland_time > '06:00' and portland_time < '18:00':
                print "Local time is {}. The New York branch is open!".format(ny_time)
            else:
                print "Local time is {}. The New York branch is closed.".format(ny_time)
                
        elif branch == 'London':
            if h >= '00' and h < '16':
                lon_chg = int(h) + 8
            elif h >= '16':
                lon_chg = '0'+str(int(h) - 16)
            lon_time = ':'.join([str(lon_chg), m])
    
            if portland_time > '01:00' and portland_time < '13:00':
                print "Local time is {}. The London branch is open!".format(lon_time)
            else:
                print "Local time is {}. The London branch is closed.".format(lon_time)
                
        else:
            print "Please enter either 'New York' or 'London'."
            
        again = raw_input("Would you like to check again? (y/n): ").lower()
        if again == 'n':
            print "Ok, have a great day!"
            check = False
        


if __name__ == '__main__':
    open_or_closed()
