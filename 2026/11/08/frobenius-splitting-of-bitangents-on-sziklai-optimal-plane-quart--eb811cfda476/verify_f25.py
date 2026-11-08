"""Independent exact census of bitangent lines over F_5 and F_25."""
from math import comb

P=5
# Elements of F25=F5[s]/(s^2-2), encoded as a+5b.
def add(x,y): return ((x%5+y%5)%5)+5*((x//5+y//5)%5)
def neg(x): return ((-x%5)%5)+5*((-x//5)%5)
def mul(x,y):
    a,b=x%5,x//5;c,d=y%5,y//5
    return ((a*c+2*b*d)%5)+5*((a*d+b*c)%5)
def power(x,n):
    r=1
    while n:
        if n&1:r=mul(r,x)
        x=mul(x,x);n//=2
    return r
def inv(x):
    assert x!=0
    return power(x,23)
def sub(x,y): return add(x,neg(y))
def div(x,y): return mul(x,inv(y))
def lines(field):
    # projective representative: first nonzero coefficient equals one
    for j in range(3):
        for tail in __import__('itertools').product(field,repeat=2-j):
            yield (0,)*j + (1,) + tail

def is_projective_square(poly):
    d=max(i for i,v in enumerate(poly) if v!=0)  # coefficient of U^i V^(4-i)
    if d%2: return False
    if d==0:return True
    if d==2:
        a,b,c=poly[2],poly[1],poly[0]
        return sub(mul(b,b),mul(4,mul(a,c)))==0
    # normalized square of U^2+b UV+cV^2, up to a scalar.
    a=poly[4]; b=div(poly[3],mul(2,a))
    c=div(sub(div(poly[2],a),mul(b,b)),2)
    return div(poly[1],a)==mul(2,mul(b,c)) and div(poly[0],a)==mul(c,c)

def restrict(line):
    a,b,c=line
    if c:
        A,B,D=1,1,3
        s,t=neg(div(a,c)),neg(div(b,c))
    elif b:
        A,B,D=1,3,1
        s,t=neg(div(a,b)),neg(div(c,b))
    else:
        A,B,D=1,3,1
        s,t=neg(div(b,a)),neg(div(c,a))
    coeff=[]
    for j in range(5):
        v=mul(D,mul(comb(4,j)%5,mul(power(s,4-j),power(t,j))))
        if j==0:v=add(v,A)
        if j==4:v=add(v,B)
        coeff.append(v)
    return coeff[::-1]

assert all(power(x,25)==x for x in range(25))
assert all(power(x,4)!=2 for x in range(25))
for field,expected in [(range(5),0),(range(25),4)]:
    pts=list(lines(field)); bts=[L for L in pts if is_projective_square(restrict(L))]
    assert len(pts)==len(field)**2+len(field)+1
    assert len(bts)==expected, (len(field),bts)
    if len(field)==25:
        assert all(L[2]==0 for L in bts),bts
    print('F_%d lines=%d bitangents=%d'%(len(field),len(pts),len(bts)))
print('VERIFY_OK')
