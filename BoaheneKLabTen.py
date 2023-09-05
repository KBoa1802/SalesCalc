import example
# My words and actions will reflect Academic Integrity.
# I will not cheat or lie or steal in academic matters.
# I will promote integrity in the UNCG community.
# Student’s Signature: Kwadwo Boahene Date: 10/31/22

# identifiers
TAX_RATE = .07
num1 = 2.5
num2 = 7.2

print('Kwadwo Boahene')
print('Lab Ten')
print()
print('This program will work with functions.\nA function called add will be imported into the program.\n It adds two numbers together.')
print('A function called calculateSales()will use a for loop to ask a user to enter four item prices into a variable called itemSale and calculate a subtotal as the subTotal + itemSale.')
print('A function called salesTax() will calculate a variable called tax to be subTotal * TAX_RATE.')
print('A function called totalSalesPrice() will calculate a variable called totalPrice to be totalSales + taxes.')
print()
print('This is the call to the imported add function.')
print('The addition of', num1, '+', num2, 'is', example.add(num1,num2))
print()
lst=[]
subTotal = 0.0
def calculateSales():
    for times in range(4):
        lst.append(float(input('Enter an item price: ')))
        subTotal = sum(lst)
    print()
    print('The subtotal is %.2f' % subTotal)
calculateSales()
def salesTax():
    subTotal = sum(lst)
    salesTax=float(subTotal*TAX_RATE)
    print('The tax is ', round(salesTax, 2))
salesTax()
def totalSalesPrice():
    subTotal = sum(lst)
    salesTax=float(subTotal*TAX_RATE)
    totalSalesPrice=float(subTotal + salesTax)
    print('The total sales price is $',round(totalSalesPrice, 2))
totalSalesPrice()



        
        
      
    
