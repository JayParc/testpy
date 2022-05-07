import re
import urllib.request
hand=urllib.request.urlopen('http://data.pr4e.org/mbox-short.txt')
for line in hand:
    line = line.decode().strip()#decode는 옆에 붙는 b(byte)를 없애주기 위한 코드
    if re.search('^New',line):
        x = re.findall('\d....',line)#\d....는 32-24이런거 까지 출력이 가능하지만, 숫자만 출력을 원한다면 \d+가 조금 더 활용적이다.
        print(x)
