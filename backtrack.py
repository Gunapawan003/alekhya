import re

st = "30/12/2019"

res = re.search(r'([0-2][1-9]|[1-3][0-1])/([0-1][1-2]|[0][1-9]|[1][0-2])/([0-9][9][0-9][0-9]|[2-9][0-9][0-9][0-9])',st)

if(res):
    print("Match Found")
    print(res.group(0))
    print(res.group(1))
    print(res.group(3))
else:
    print("Match not found")