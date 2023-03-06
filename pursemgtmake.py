
from pursemake import Purse
import time

class verbose():
    def __init__(self,f):
        self.f = f
    def __call__(self,*args):
        start=time.time()
        self.f(*args)
        print(f"\n실행 시간은: {time.time() - start}")

class PurseMgtSystem():
    def __init__(self):
        pass
    
    @staticmethod
    def register_purse(num,name,coins_dic):
        a = Purse()
        a.num = num
        a.name = name
        a.coins = coins_dic
        return a
    @staticmethod
    def process(object_list):
        fp = open("purse_output.txt","wt",encoding="UTF-8")
        double_list = []
        for i in object_list:
            total = 0
            for key,value in i.coins.items():
                total += key*value
            double_list.append([i.num,i.name,i.coins,total])
        double_list.sort(key = lambda x: x[3],reverse = True)
        rank = 0
        compare = double_list[0][3]+1
        for i in double_list:
            if i[3] < compare:
                rank += 1
                compare = i[3]
                fp.write(f"번호:{i[0]+1} 이름:{i[1]} 500원:{i[2].get(500,0)} 100원:{i[2].get(100,0)} 50원:{i[2].get(50,0)} 10원:{i[2].get(10,0)} 1원:{i[2].get(1,0)} 총액:{i[3]:4d} 순위:{rank}\n")
                print(f"번호:{i[0]+1} 이름:{i[1]} 500원:{i[2].get(500,0)} 100원:{i[2].get(100,0)} 50원:{i[2].get(50,0)} 10원:{i[2].get(10,0)} 1원:{i[2].get(1,0)} 총액:{i[3]:4d} 순위:{rank}")
            elif i[3] == compare:
                fp.write(f"번호:{i[0]+1} 이름:{i[1]} 500원:{i[2].get(500,0)} 100원:{i[2].get(100,0)} 50원:{i[2].get(50,0)} 10원:{i[2].get(10,0)} 1원:{i[2].get(1,0)} 총액:{i[3]:4d} 순위:{rank}\n")
                print(f"번호:{i[0]+1} 이름:{i[1]} 500원:{i[2].get(500,0)} 100원:{i[2].get(100,0)} 50원:{i[2].get(50,0)} 10원:{i[2].get(10,0)} 1원:{i[2].get(1,0)} 총액:{i[3]:4d} 순위:{rank}")
                rank +=1
        return double_list,fp
    @staticmethod
    @verbose
    def count_coins(coin,double_list,fp):
        owner = []
        owns = 0
        for i in double_list:
            if i[2].get(coin,0) > owns:
                owner = [[i[0],i[1],i[2].get(coin,0)]]
                owns = i[2].get(coin,0)
            elif i[2].get(coin,0) == owns:
                owner.append([i[0],i[1],i[2].get(coin,0)])
        fp.write("\n최다 보유자들\n")
        print("최다 보유자들")
        for j in owner:
            fp.write(f"번호: {j[0]+1}, 이름:{j[1]}, 개수: {j[2]}\n")
            print(f"번호: {j[0]+1}, 이름:{j[1]}, 개수: {j[2]}")
        fp.close()
        
    @staticmethod    
    def checkifdeserve(wish,double_list):
        product = wish[0]
        price = wish[1]
        for i in double_list:
            if (i[3] >= int(price)):
                print(f"{i[1]}는 보유 금액이 {i[3]}원이므로 {product}를 구매할 수 있습니다\n")
