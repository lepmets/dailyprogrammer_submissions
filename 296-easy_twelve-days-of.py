#! /usr/bin/python3
"""[EASY] #296 Twelve days of .."""
# coding: utf-8

dayOfChristmas = ['First', 'Second', 'Third', 'Fourth', 'Fifth', 'Sixth',
                  'Seventh', 'Eighth', 'Ninth', 'Tenth', 'Eleventh', 'Twelth']
gifts = ['Drummers Drumming', 'Pipers Piping', 'Lords a Leaping',
         'Ladies Dancing', 'Maids a milking', 'Swans a Swimming',
         'Geese a Laying', 'Golden Rings', 'Calling Birds',
         'French Hens', 'Turtle doves', 'Partridge in a Pear Tree']

for day in dayOfChristmas:
    print('')
    print('On the ' + day +
          ' day of christmas' + '\nmy true love sent to me:')
    numOfGifts = dayOfChristmas.index(day)+1
    for gift in gifts[(len(gifts)-1)-dayOfChristmas.index(day):len(gifts)]:
        if numOfGifts == 1:
            print('And ' + str(numOfGifts) + ' ' + gifts[len(gifts)-1])
        else:
            print(str(numOfGifts) + ' ' + gift)
        numOfGifts -= 1
    print('')
