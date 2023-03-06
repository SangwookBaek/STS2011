num = [0,1,2,3,4,5,6,7,8,9,10]
class ScoreError(Exception):
  def __init__(self,msg):
    self._message = msg


while(1):
  key = input("값을 입력받습니다: ")
  try:
    value = num[int(key)]
  except IndexError:
    print(-1)
  except ValueError:
    print("프로그램을 종료합니다")
    break
  else:
    print(value)
