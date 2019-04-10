# do_fizzbuzz.py
# 1부터 100까지 수가 증가하면서
# 그 수가 3의 배수라면 "Fizz"
# 5의 배수라면 "Buzz"
# 15의 배수라면 "FizzBuzz"
# 나머지 경우는 그 수를 출력

for i in range(1,100+1):
    if i%15 == 0:
        print(str(i) + ": Fizzbuzz")
    elif i%5 == 0:
        print(str(i) + ": Buzz")
    elif i%3 == 0:
        print(str(i) + ": Fizz")

