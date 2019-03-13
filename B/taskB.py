def calc_first_nums(num, prev_num):
  while prev_num > 0:
    tmp = num 
    num = prev_num
    prev_num = tmp - num
  if prev_num < 0:
    return [round(num), round(tmp)]
  else:
    return [round(prev_num), round(num)]

num = int(input())
div = (1 + 5 ** (1 / 2)) / 2

prev_num = num // div
answer_1 = calc_first_nums(num, prev_num)

prev_num = num // div + 1
answer_2 = calc_first_nums(num, prev_num)

print("{} {}".format(answer_1[0], answer_1[1])) if sum(answer_1) < sum(answer_2) else print("{} {}".format(answer_2[0], answer_2[1]))