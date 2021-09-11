"""Set solutions """
# #question 1
# sampleSet = {"Yellow", "Orange", "Black"}
# sampleList = ["Blue", "Green", "Red"]
# sampleSet.update(sampleList)
# print(sampleSet)


# #qyestion 2
# set1 = {10, 20, 30, 40, 50}
# set2 = {30, 40, 50, 60, 70}
#
# print(set1.intersection(set2))

# #question 3
# set1 = {10, 20, 30}
# set2 = {20, 40, 50}
#
# set1.difference_update(set2)
# print(set1)

# # question 4
# set1 = {10, 20, 30, 40, 50}
# set2 = {30, 40, 50, 60, 70}
#
# print(set1.union(set2))

# #5
# set1 = {10, 20, 30, 40, 50}
# set1.difference_update({10, 20, 30})
# print(set1)

# #6
# set1 = {10, 20, 30, 40, 50}
# set2 = {30, 40, 50, 60, 70}
#
# print(set1.symmetric_difference(set2))
# #7
# set1 = {10, 20, 30, 40, 50}
# set2 = {60, 70, 80, 90, 10}
#
# if set1.isdisjoint(set2):
#   print("Two sets have no items in common")
# else:
#   print("Two sets have items in common")
#   print(set1.intersection(set2))
#  #8
# set1 = {10, 20, 30, 40, 50}
# set2 = {30, 40, 50, 60, 70}
#
# set1.symmetric_difference_update(set2)
# print(set1)
#
# #9
# set1 = {10, 20, 30, 40, 50}
# set2 = {30, 40, 50, 60, 70}
#
# set1.intersection_update(set2)
# print(set1)