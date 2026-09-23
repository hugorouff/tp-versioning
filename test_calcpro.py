from calcpro import mediane, moyenne 
assert moyenne([10, 20]) == 15 
assert moyenne([1.5, 2.5]) == 2.0
assert moyenne([]) == 0 
assert moyenne(None) is None
assert mediane([3, 1, 2]) == 2
assert mediane([4, 1, 3, 2]) == 2.5
assert mediane([]) == 0
assert mediane(None) is None
print('tests OK') 