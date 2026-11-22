## HT: Item In Common ( ** Interview Question)
# Write a function item_in_common(list1, list2) that takes two lists as input 
# and returns True if there is at least one common item between the two lists, 
# False otherwise.

def common_in_list(list1, list2):
  my_dict = {}
  for i in list1:
    my_dict[i] = True
  for j in list2:
    if j in my_dict:
      return True
  return False

list1 = [1, 2, 3]
list2 = [2, 4, 5]

print(common_in_list(list1, list2))

list2 = [4, 5, 6]
print(common_in_list(list1, list2))
