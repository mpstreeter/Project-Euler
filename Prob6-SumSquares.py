
#sum of squares
sum_of_sq = 0

#square of sum
sum_nums = 0
sq_of_sum = 0

for i in range(1,101):
    sum_nums += i
    sum_of_sq += i**2

sq_of_sum = sum_nums**2

print sq_of_sum - sum_of_sq
