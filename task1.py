import datetime

def fineBook(expectedDate, returnDate):
    eDateArr = [int(x) for x in expectedDate.split(' ')]
    rDateArr = [int(y) for y in returnDate.split(' ')]
    
    eDate = datetime.datetime(eDateArr[2], eDateArr[1], eDateArr[0])
    rDate = datetime.datetime(rDateArr[2], rDateArr[1], rDateArr[0])

    if (rDate < eDate) or (rDate == eDate):
        fine = 0
    
    if (rDate > eDate) and (rDate.month == eDate.month):
        fine = 15 * (rDate.day - eDate.day)

    if (rDate.month > eDate.month) and (rDate.year == eDate.year):
        fine = 500 * (rDate.month - eDate.month)
    
    if (rDate.year > eDate.year):
        fine = 12000

    return fine

expectedDate = input()
returnDate = input()
print(fineBook(expectedDate, returnDate))

