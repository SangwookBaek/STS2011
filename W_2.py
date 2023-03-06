import sys
import datetime
day_list = ["월","화","수","목","금","토","일"]
input_date=datetime.datetime(int(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3]))
print(f"{day_list[input_date.weekday()]}요일")
