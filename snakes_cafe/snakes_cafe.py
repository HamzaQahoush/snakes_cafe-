def cafee():
    print("""$ python snakes_cafe.py
**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
**************************************

Appetizers
----------
Wings
Cookies
Spring Rolls

Entrees
-------
Salmon
Steak
Meat Tornado
A Literal Garden

Desserts
--------
Ice Cream
Cake
Pie

Drinks
------
Coffee
Tea
Unicorn Tears
    """)
cafee()
orders=[]    
order= input("""***********************************
** What would you like to order? **
***********************************
""")  
orders.append(order)
count=orders.count(order)



print (f'**{count} order of {order} added to your meal')
