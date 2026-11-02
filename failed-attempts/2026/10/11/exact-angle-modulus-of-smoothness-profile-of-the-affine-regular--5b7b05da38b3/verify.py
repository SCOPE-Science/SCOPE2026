from fractions import Fraction as F

def N(z):
    s,t=z
    return max(abs(s),abs(t),abs(s-t))

def add(x,y):
    return (x[0]+y[0],x[1]+y[1])

def sub(x,y):
    return (x[0]-y[0],x[1]-y[1])

def R(z):
    s,t=z
    return (s-t,s)

def Q(z):
    s,t=z
    return (t,s)

# Exact symmetry checks on a generating finite set of integer vectors.
tests=[(F(a),F(b)) for a in range(-2,3) for b in range(-2,3)]
for z in tests:
    assert N(R(z))==N(z)
    assert N(Q(z))==N(z)

# Same-edge formula.
for u,v in [(F(0),F(1)),(F(1,3),F(2,3)),(F(1),F(1,2))]:
    x=(F(1),u); y=(F(1),v)
    assert N(sub(x,y))==abs(u-v)
    assert N(add(x,y))==2

# Adjacent-edge family attains 2-epsilon/2 for all checked rational parameters.
for e in [F(0),F(1,3),F(1),F(4,3),F(3,2),F(2)]:
    x=(F(1),e/2)
    y=(F(1)-e/2,-e/2)
    assert N(x)==1 and N(y)==1
    assert N(sub(x,y))==e
    assert N(add(x,y))==2-e/2

# Next-nearest family attains 4-2epsilon.
for e in [F(1),F(4,3),F(3,2),F(7,4),F(2)]:
    x=(F(1),e-F(1))
    y=(F(1)-e,-F(1))
    assert N(x)==1 and N(y)==1
    assert N(sub(x,y))==e
    assert N(add(x,y))==4-2*e

# Opposite-edge endpoint.
x=(F(1),F(0)); y=(-F(1),F(0))
assert N(x)==N(y)==1
assert N(sub(x,y))==2
assert N(add(x,y))==0

# Exact branch crossing and values.
e=F(4,3)
assert 2-e/2 == 4-2*e == F(4,3)
def rho_from_m(m):
    return F(1)-m*m/F(2)
assert rho_from_m(F(3,2)) == -F(1,8)  # epsilon=1, adjacent branch
assert rho_from_m(F(4,3)) == F(1,9)
assert rho_from_m(F(0)) == F(1)

print("VERIFY_OK")
