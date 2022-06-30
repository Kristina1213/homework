# 12.1
def num_sum(num1, num2):
    result = num1 + num2
    return result

print(num_sum(12,10))
print(num_sum(15,48))
print(num_sum(5,13))
print(num_sum(41,11))
print(num_sum(9,21))


#12.2
def num_cube(num):
    return num*num*num

print(num_cube(2))
print(num_cube(3))
print(num_cube(4))


#12.3
def step_counter(distance_m, step_length_m):
    result = int(distance_m / step_length_m)
    return result

print(step_counter(6000,0.8))


#12.4
def absolut_dif(a, b):
    if a > b:
        return a - b
    else:
        return b - a

print(absolut_dif(a=4, b=2))
print(absolut_dif(a=3, b=8))


