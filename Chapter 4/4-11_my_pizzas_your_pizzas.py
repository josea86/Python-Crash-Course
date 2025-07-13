my_pizzas = ["margheritta" , "calzone" , "4 formaggi"]
your_pizzas = my_pizzas[:]

my_pizzas.append("diavola")
your_pizzas.append("barbacoa")

for pizza in my_pizzas:
    print ("Me encanta la pizza " + pizza.title())
    
for pizza in your_pizzas:
    print ("A mis amigos les encanta la pizza " + pizza.title())
    
print (my_pizzas)
print (your_pizzas)