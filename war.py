'''
https://fivethirtyeight.com/features/riddler-nation-goes-to-war/
'''
def beats(order, order2):
    wins = 0
    loses = 0
    for (i,j) in zip(order, order2):
        if j>i:
            wins+=1
        elif i>j:
            loses+=1
    print wins, loses
    return wins > loses
        

def beats_others(new_order, orders):
    for order in orders:
        if not beats(order, new_order):
            return False
    return True

def maybe_add_order(new_order):
    if beats_others(new_order, orders):
        orders.append(new_order)
    
def create_and_swap(base, i, j, k):
    new_order = list(base[:])
    new_order[i], new_order[j], new_order[k] = new_order[j], new_order[k], new_order[i]
    return tuple(new_order)
    
def three_way_swap_and_add(base):
    for i in xrange(13):
        for j in xrange(13):
            for k in xrange(13):
                if i != j and i != k and j != k:
                    new_order = create_and_swap(base, i, j, k)
                    maybe_add_order(new_order)

def iterate(i=-1):
    old_len = len(orders)
    three_way_swap_and_add(orders[i])
    new_len = len(orders)
    diff = new_len-old_len
    return diff

# Add the two starting orders
order = [2,3,4,5,6,7,8,9,10,11,12,13,14]
order2 = order[::-1]
orders = [order, order2]

# Keep doing all possible 3 way swaps of the last item
while iterate() > 0:
    pass

print orders[-1]
beats(orders[0], orders[-1])
beats(orders[1], orders[-1])


