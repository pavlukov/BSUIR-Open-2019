sum = gets.chomp.to_i

sum % 2 == 0 ? puts(sum/2, sum/2) : puts(sum/2, sum/2+1)