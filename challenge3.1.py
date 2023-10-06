def linerSearchProduct(productList,targetProduct):
  indices=[]
for intex,product in enumerate(productList):
  if product==targetProduct:
    indices.append(intex)
    return indices
    product=["shoes","boot","loafer","shoes","sandal","shoes"]
    target="shoes"
    result= linearSearchProduct(product,target)
    print(result)
