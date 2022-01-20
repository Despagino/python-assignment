open_file = open('CupcakeInvoices.csv')
from matplotlib import pyplot as plt

# for row in open_file: 
#     print(row)

# for row in open_file:
#     result = row.strip()
#     cupcake = result.split(",")
#     print(cupcake[2])

# for row in open_file:
#     cupcake = row.split(",")
#     result = int(cupcake[3]) * float(cupcake[4])
#     print(result)

invoice = 0


# for row in open_file:
#     cupcake = row.split(",")
#     invoice = invoice + (int(cupcake[3]) * float(cupcake[4]))

# print(invoice)



def showResult():

    res = []
    chocolate = 0
    vanilla = 0
    strawberry = 0
    
    for row in open_file:
        cupcake = row.split(",")
        if (cupcake[2] == "Chocolate"):
            chocolate = chocolate + (int(cupcake[3]) * float(cupcake[4]))
        elif (cupcake[2] == "Strawberry"):
            strawberry = strawberry + (int(cupcake[3]) * float(cupcake[4]))
        else:
            vanilla = vanilla + (int(cupcake[3]) * float(cupcake[4]))
    
    res.append(chocolate)
    res.append(strawberry)        
    res.append(vanilla)
    return res

graph = showResult()

# x_value = graph[0]
# y_value = graph[1]
# z_value = graph[2]

plt.plot(graph)
plt.show()



# for row1 in open_file:
#     cupcake = row1.split(",")
#     if (cupcake[2] == "Strawberry"):
#         strawberry = strawberry + (int(cupcake[3]) * float(cupcake[4]))

# print(strawberry)

# for row2 in open_file:
#     cupcake = row2.split(",")
#     if (cupcake[2] == "Vanilla"):
#         vanilla = vanilla + (int(cupcake[3]) * float(cupcake[4]))

# print(vanilla)







# open_file.close()