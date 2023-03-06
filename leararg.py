
import sys
class DayName():
    def __init__(self,year,month,day):
        self.year = year
        self.month = month
        self.day = day

    def isleap(self):
      if (self.year % 400) :
        if (self.year % 100):
          if (self.year%4 ):
            return False
          else :
            return True
        else:
          return False
      else :
        return True
    
    def get_name(self):
        total_day = 0
        month_to_date ={"1":31,"3":31,"4":30,"5":31,"6":30,"7":31,"8":31,"9":30,"10":31,"11":30,"12":31}
        day_list = {0:"월",1:"화",2:"수",3:"목",4:"금",5:"토",6:"일"}
        if self.isleap():
            month_to_date["2"] = 29
        else:
            month_to_date["2"] = 28
        for i in range(1,self.month):
            total_day += month_to_date[str(i)]
        total_day += (self.day-1)
        leap_year = ((self.year-1)//4) - ((self.year-1)//100) + ((self.year-1)//400)
        year_to_date=self.year-1 + leap_year
        total_day+= year_to_date
        return day_list[total_day%7]+"요일"

if __name__ =="__main__":
    year,month,day =  int(sys.argv[1]), int(sys.argv[2]),int(sys.argv[3])
    day_name = DayName(year, month, day)
    print(day_name.get_name()) 
