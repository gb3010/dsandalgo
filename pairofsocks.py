#A solution from online using count inbuilt method of list for pair of socks counting problem

socks = input().strip().split()
pairs = 0

for element in set(socks):
	pairs += socks.count(element) // 2
print(pairs)
