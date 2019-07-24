import pymysql
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

def createSql(lines) :
    index = 0
    recordList = list()
    for line in lines :
        if index % 2 == 0 :
            arr = line.lstrip().split(' ')
            board = get_board(arr[0])
            latest_price = get_latest_price(arr[1])
            low = get_low(arr[3])
            high = get_high(arr[4])
            volume = get_volume(arr[5])
            sql = "INSERT INTO `coinw`.`coinw_trend` (`board`, `latest_price`, `low`, `high`, `volume`, `create_time`, `modify_time`, `dt`)  " \
                  "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)" % \
                  ('\'' + board + '\'', latest_price, low, high, volume,
                   '\'' + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + '\'',
                   '\'' + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + '\'',
                   '\'' + time.strftime("%Y%m%d", time.localtime()) + '\'')
            recordList.append(sql)
        index = index + 1
    return recordList
# INSERT INTO `coinw`.`coinw_trend` (`board`, `latest_price`, `low`, `high`, `volume`, `create_time`, `modify_time`, `dt`)
# VALUES ('TNT', '0.13', '0.129', '0.146', '32596942', '2019-03-18 22:53:50', '2019-03-18 22:53:50', '20190318');
# 打开数据库连接
db = pymysql.connect(host="192.168.2.100", port=3306, user="root", password="heaven",database="coinw")

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

# 使用 execute()  方法执行 SQL 查询
f = open('./doc/20190724')
if f.name == "./doc/" + time.strftime("%Y%m%d", time.localtime()):
    lines = f.readlines()
    sqlList = createSql(lines)
    for sql in sqlList:
        print(sql)
        cursor.execute(sql)
else:
    print("file name is not equals date!!!")
# 关闭数据库连接
db.close()
