def commonMember(list1, list2):
  # Check if two lists have at least one common member
  return not set(list1).isdisjoint(list2)  
    #.isdisjoint()checks if two sets have no elements in common. If they do have common elements, it returns False, and the not operator negates it to True.

list_a = [1, 2, 3, 4, 5]
list_b = [5, 6, 7, 8]
list_c = [9, 10, 11]

result1 = commonMember(list_a,list_b)
#runs the function for list_a and list_b

result2 = commonMember(list_a,list_c)
#runs the function for list_a and list_c

print(f"Do list_a and list_b have common members? {result1}")
print(f"Do list_a and list_c have common members? {result2}")