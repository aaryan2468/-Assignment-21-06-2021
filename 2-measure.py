h1 = int(input("Enter the height of first wall in feet: "))
w1 = int(input("Enter the width of first wall in feet: "))
h2 = int(input("Enter the height of second wall in inches: "))
w2 = int(input("Enter the width of second wall in inches: "))

def area(h,w,conv):
    area = h*w*conv
    return area

area1 = area(h1,w1,0.092903)
area2 = area(h2,w2,0.00064516)

def cost(size):
    cost = 120 * size
    return cost

w1_cost = cost(area1)
w2_cost = cost(area2)

print("Cost of painting first wall : ", w1_cost)
print("Cost of painting second wall : ", w2_cost)
print("Total cost to paint two walls : ", w1_cost+w2_cost)
