input_num = int(input())
div = (1 + 5 ** (1 / 2)) / 2
num = input_num
prev_num = num // div

while prev_num > 0:
  tmp = num 
  num = prev_num
  prev_num = tmp - num
if prev_num < 0:
  answer_1 = [round(num), round(tmp)]
else:
  answer_1 = [round(prev_num), round(num)]

num = input_num
prev_num = num // div + 1

while prev_num > 0:
  tmp = num 
  num = prev_num
  prev_num = tmp - num
if prev_num < 0:
  answer_2 = [round(num), round(tmp)]
else:
  answer_2 = [round(prev_num), round(num)]

print("{} {}".format(answer_1[0], answer_1[1])) if sum(answer_1) < sum(answer_2) else print("{} {}".format(answer_2[0], answer_2[1]))