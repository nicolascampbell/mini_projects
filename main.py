import math
from texttable import Texttable

def get_manhattan_distance(a:tuple,b:tuple)->float:
  if(len(a)!=len(b)):
    raise Exception("Parameters have diferent dimensions")
  dimension= len(a)
  sum=0
  for i in range(dimension):
    sum+=math.fabs(a[i]-b[i])
  distance = sum
  return distance


def get_euclidean_distance(a:tuple,b:tuple)->float:
  if(len(a)!=len(b)):
    raise Exception("Parameters have diferent dimensions")
  dimension= len(a)
  sum=0
  for i in range(dimension):
    sum+=math.pow(a[i]-b[i],2)
  distance = math.sqrt(sum)
  return distance

"""
Given a list of points and a method to calculate distance between them.
Builds up a table with the distances.
"""
def get_distance_table(points:list, method):
  #where to start the leters
  A_val=65
  #just making a row for col headers
  head_col=[" "]
  for j in range(len(points)):
    head_col.append(chr(A_val+j))
  t = Texttable()
  t.add_row(head_col)

  #build rows for each point
  new_row=[]
  for i in range(len(points)):
    new_row.append(chr(A_val+i))
    for j in range(len(points)):
      if(i==j):
        new_row.append('0')
      else:
        #.2f just takes the first 2 nums after coma, doesnt round
        new_row.append("%.2f" % method(points[i],points[j]))
    t.add_row(new_row)
    new_row=[]

  print(t.draw())
  return 0


if __name__ == '__main__':
  #add the points
  points=[
    (9,6,5,7) ,
    (2,8,8,6),
    (7,8,1,8),
    (5,1,6,1)
    ]
  #choose method for distance
  get_distance_table(points,get_manhattan_distance)


