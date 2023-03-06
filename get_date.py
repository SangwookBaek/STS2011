
def isleap(year):
  if (year % 400) :
    if (year % 100):
      if ( year%4 ):
        return False
      else :
        return True
    else:
      return False
  else :
    return True
def input_date():
    year = input("__년도를 입력하십시오:")
    month = input("__월을 입력하십시오:")
    day = input("__일을 입력하십시오:")
    return year,month,day
def get_day_name(year, month, day):
    total_day = 0
    month_to_date ={"1":31,"3":31,"4":30,"5":31,"6":30,"7":31,"8":31,"9":30,"10":31,"11":30,"12":31}
    day_list = {0:"월",1:"화",2:"수",3:"목",4:"금",5:"토",6:"일"}
    if isleap(year):
        month_to_date["2"] = 29
    else:
        month_to_date["2"] = 28
    for i in range(1,month):
        total_day += month_to_date[str(i)]
    total_day += (day-1)
    leap_year = ((year-1)//4) - ((year-1)//100) + ((year-1)//400)
    year_to_date=year-1 + leap_year
    print(year_to_date)
    total_day+= year_to_date
    return day_list[total_day%7]+"요일"
    
if __name__ =="main":
    
    year,month,day = input_date()
    day_name = get_day_name(year,month,day)
    print(day_name)
