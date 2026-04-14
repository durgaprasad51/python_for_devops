info = {}  # empty dictionary
days = set()      # empty set
days = {"Saturday","Sunday","Saturday","Sunday"}  ## Set will remove the duplicate entries.

nums = [1,1,1,1,2,2,2,2,3,3,3,4,4,4,6.5,6.5,-1,-1,-4] # list

nums = set(nums)  # to remove the diplicacy from the above list we we put set infront but it became set
print(nums)
print(type(nums))
nums = list(set(nums))  # Here list will remain but without duplicacy
print(nums)
print(type(nums))

print(type(info))
print(type(days))
print(days)

