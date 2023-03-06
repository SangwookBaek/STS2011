
import NameA
print("top-level B.py")
NameA.func()

if __name__ == "__main__":
    print("B.py 직접실행")
else:
    print("B.py 임포트되어 사용됨")
