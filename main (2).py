""" write  a function called linear_search _product that taks the list of product and a target product name as input .The function  should perform a linear search to fins the target production  the list and return  a list of indices of all occurences of the product  if foundor an empty list if the product  is not found.
"""


def Linearsearchproduct(product  List,target):
indices:[]

for index,product  in enumerate(product list):

if product=target product: 
indices.append(index)

return indices


# example usage:
product=["shoes","boot","loafer","shoes","sandal","shoes"]
target1="shoes"
target2="apple" 
result=Linearsearchproduct(product, target)
print(result) 