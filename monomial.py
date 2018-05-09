from sympy import Symbol, integrate

def moment(order, x_min, x_max):

    n = len(order)
    assert(len(x_min) == n)
    assert(len(x_max) == n)

    x = []
    moment = 1.
    for i, power in enumerate(order):
        x_i = Symbol('x_' + str(i))
        moment *= x_i**power
        x.append(x_i)

    for i, x_i in enumerate(x):
        moment = integrate(moment, (x_i, x_min[i], x_max[i]))

    return moment