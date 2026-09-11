def two_sum(target,arr):
    seen = {}
    for index,num in enumerate(arr):
        needed = target - num

        if needed in seen:
            return[seen[needed],index]

        seen[num] = index

nums = [2, 7, 11, 15]
target = 9

print(two_sum(target,nums))