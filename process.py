# for line in lines :
#     arr = line.split(' ')
#     for value in arr :
#         print(value)
#     break
from record import Record
import time

def get_board(value):
    return value.split('/')[0]

def get_latest_price(value):
    return float(value[1:])

def get_low(value):
    return float(value)

def get_high(value):
    return float(value)

def get_volume(value):
    return float(value)


def pro(lines) :
    index = 0;
    recordList = list()
    for line in lines :
        if index % 2 == 0 :
            arr = line.lstrip().split(' ')
            board = get_board(arr[0])
            latest_price = get_latest_price(arr[1])
            low = get_low(arr[3])
            high = get_high(arr[4])
            volume = get_volume(arr[5])
            # record = Record(board, latest_price, low, high, volume)
            # print(record.print_record())
            # recordList.append(record)
            sql = "INSERT INTO `coinw`.`coinw_trend` (`board`, `latest_price`, `low`, `high`, `volume`, `create_time`, `modify_time`, `dt`)  " \
                  "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)" % \
                  ('\'' + board + '\'', latest_price, low, high, volume, '\'' + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + '\'', '\'' + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + '\'', '\'' + time.strftime("%Y%m%d", time.localtime()) + '\'')
            recordList.append(sql)
        index = index + 1
    return recordList


f = open('20190323')
lines = f.readlines()
res = pro(lines)
print(res[0])