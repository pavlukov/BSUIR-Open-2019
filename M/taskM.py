input_sum = int(input())
num_1 = [1]
num_2 = [2]

while sum(num_1) < input_sum:
  if num_1[0] == 1:
    num_1 = [2] + num_1 
  else:
    num_1 = [1] + num_1

while sum(num_2) < input_sum:
  if num_2[0] == 1:
    num_2 = [2] + num_2
  else:
    num_2 = [1] + num_2

if sum(num_1) == input_sum and sum(num_2) == input_sum:
  if int(''.join(str(n) for n in num_1)) > int(''.join(str(n) for n in num_2)):
    print(''.join(str(n) for n in num_1))
  else:
    print(''.join(str(n) for n in num_2))
elif sum(num_1) == input_sum:
  print(''.join(str(n) for n in num_1))
else:
  print(''.join(str(n) for n in num_2))
