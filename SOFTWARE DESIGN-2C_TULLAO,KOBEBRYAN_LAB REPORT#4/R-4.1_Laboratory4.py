def maxRec(lst):
   if(len(lst) == 1):
      return lst[0]
   else:
      maxVal = maxRec(lst[1:])
      if(maxVal < lst[0]):
         maxVal = lst[0]
      return maxVal

lst = [2, 6, 1, 4, 3]
maxVal = maxRec(lst)
print(maxVal)
