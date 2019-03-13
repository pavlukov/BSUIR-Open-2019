sum = gets.chomp.to_i
num_1 = [1]
num_2 = [2]
while num_1.sum < sum
  num_1.first == 1 ? num_1.unshift(2) : num_1.unshift(1)
end

while num_2.sum < sum
  num_2.first == 1 ? num_2.unshift(2) : num_2.unshift(1)
end

if num_1.sum == sum && num_2.sum == sum
  num_1.join > num_2.join ? puts(num_1.join) : puts(num_2.join)
elsif num_1.sum == sum
  puts num_1.join
else
  puts num_2.join
end