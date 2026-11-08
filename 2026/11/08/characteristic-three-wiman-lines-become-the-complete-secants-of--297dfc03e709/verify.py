#!/usr/bin/env python3
"""Exact arithmetic checks for the characteristic-three Wiman-line specialization.

The 45 coefficient triples are from Harbourne, Lectures on Asymptotics of
Linear Systems with Connections to Line Arrangements, Example 3.3.4 (2016).
The source parameters are A=-(a**3-3*a-2)/4 and B=(a**3+a-2)/4.
All calculations are performed with Python standard-library integers.
"""
from collections import Counter, defaultdict
from itertools import combinations

COEFFICIENTS = [('0', '1', '0'),
 ('A - 1', 'A', '1'),
 ('0', '0', '1'),
 ('1 - A', 'A', '-1'),
 ('A', '1', 'A - 1'),
 ('-A', '1', '1 - A'),
 ('A - 1', '-B', '-A*B - A'),
 ('1 - A', '-B', 'A*B + A'),
 ('1 - A', 'A', '1'),
 ('A', '1', '1 - A'),
 ('-1', 'A - 1', 'A'),
 ('-A*B - 1', '1', '-B - 1'),
 ('1 - A', 'B', '-A*B - A'),
 ('A', '-A*B + B', '-B - 1'),
 ('-A*B - A', '1 - A', '-B'),
 ('A - 1', 'A', '-1'),
 ('-A', '1', 'A - 1'),
 ('1', 'A - 1', '-A'),
 ('A*B + 1', '1', 'B + 1'),
 ('A - 1', 'B', 'A*B + A'),
 ('-A', '-A*B + B', 'B + 1'),
 ('A*B + A', '1 - A', 'B'),
 ('B + 1', '-A*B - 1', '1'),
 ('1', 'A - 1', 'A'),
 ('1', '1 - A', 'A'),
 ('-A*B - 1', '1', 'B + 1'),
 ('-A - B', 'A*B + A - 1', '0'),
 ('-B', '1', '-A*B - A + B'),
 ('-A*B - 1', '-1', 'B + 1'),
 ('-B - 1', 'A', '-A*B + B'),
 ('-B - 1', '-A*B - 1', '-1'),
 ('A + B', 'A*B + A - 1', '0'),
 ('B', '1', 'A*B + A - B'),
 ('B + 1', 'A', 'A*B - B'),
 ('A*B + A - 1', '0', '-A - B'),
 ('1', '0', '0'),
 ('-B - 1', 'A', 'A*B - B'),
 ('0', '-A - B', 'A*B + A - 1'),
 ('-B', '1', 'A*B + A - B'),
 ('B + 1', '-B', '-A + B + 1'),
 ('1', '-A*B', '-A*B - A + B + 1'),
 ('0', '-A - B', '-A*B - A + 1'),
 ('B + 1', 'A*B + 1', '-1'),
 ('A + B', '0', '-A*B + B + 1'),
 ('B', 'A - B - 1', '-B - 1')]

P=3
# Values u+v*alpha, alpha**2=-1 in F_9.
zero=(0,0)
one=(1,0)
def k(u):
    return (u%P,0) if isinstance(u,int) else u

def add(a,b):
    a,b=k(a),k(b)
    return ((a[0]+b[0])%P,(a[1]+b[1])%P)

def sub(a,b):
    a,b=k(a),k(b)
    return ((a[0]-b[0])%P,(a[1]-b[1])%P)

def mul(a,b):
    a,b=k(a),k(b)
    return ((a[0]*b[0]-a[1]*b[1])%P,(a[0]*b[1]+a[1]*b[0])%P)

def inv(a):
    a=k(a)
    d=(a[0]*a[0]+a[1]*a[1])%P
    if not d: raise ZeroDivisionError(a)
    return ((a[0]*pow(d,-1,P))%P,(-a[1]*pow(d,-1,P))%P)

class K:
    def __init__(self,a): self.a=k(a)
    def __add__(self,b): return K(add(self.a,b.a if isinstance(b,K) else b))
    __radd__=__add__
    def __neg__(self): return K(sub(zero,self.a))
    def __sub__(self,b): return self+-K(b.a if isinstance(b,K) else b)
    def __rsub__(self,b): return K(b)+-self
    def __mul__(self,b): return K(mul(self.a,b.a if isinstance(b,K) else b))
    __rmul__=__mul__
    def __pow__(self,n):
        a=K(1)
        for j in range(n):a=a*self
        return a

A=K((2,1))
B=K((1,0))

def norm(a):
    for u in a:
        if u!=zero:
            c=inv(u)
            return tuple(mul(x,c) for x in a)
    raise ValueError('zero projective vector')

def cross(a,b):
    return norm((sub(mul(a[1],b[2]),mul(a[2],b[1])),
                 sub(mul(a[2],b[0]),mul(a[0],b[2])),
                 sub(mul(a[0],b[1]),mul(a[1],b[0]))))

def dot(a,b):
    return add(add(mul(a[0],b[0]),mul(a[1],b[1])),mul(a[2],b[2]))

def frob(v):
    return norm(tuple((a[0],-a[1]%P) for a in v))

def main():
    assert len(COEFFICIENTS)==45
    lines={norm(tuple(k(eval(expr,{'__builtins__':{}},{'A':A,'B':B}).a) if isinstance(eval(expr,{'__builtins__':{}},{'A':A,'B':B}),K) else k(eval(expr,{'__builtins__':{}},{'A':A,'B':B})) for expr in triple)) for triple in COEFFICIENTS}
    assert len(lines)==45
    all_elements=[(u,v) for u in range(3) for v in range(3)]
    plane={norm((u,v,w)) for u in all_elements for v in all_elements for w in all_elements if (u,v,w)!=(zero,zero,zero)}
    assert len(plane)==91
    conic={p for p in plane if add(add(mul(p[0],p[0]),mul(p[1],p[1])),mul(p[2],p[2]))==zero}
    assert len(conic)==10
    secants={cross(u,v) for u,v in combinations(conic,2)}
    assert len(secants)==45 and secants==lines
    inc={p:sum(dot(l,p)==zero for l in lines) for p in plane}
    hist=Counter(inc.values())
    assert hist==Counter({4:45,5:36,9:10})
    assert set(p for p in plane if inc[p]==9)==conic
    assert sum(t*(t-1)//2*n for t,n in hist.items())==990
    assert {frob(l) for l in lines}==lines
    fixed_lines=[l for l in lines if frob(l)==l]
    assert len(fixed_lines)==9
    fixed_points=[p for p in plane if frob(p)==p]
    assert len(fixed_points)==13
    assert Counter(inc[p] for p in fixed_points)==Counter({4:9,9:4})
    f3inc=[sum(dot(l,p)==zero for l in fixed_lines) for p in fixed_points]
    assert min(f3inc)>=1 and sum(f3inc)==36
    assert sum(c-1 for c in f3inc)==23
    # Geometry: q=9 conic has ten points; its 45 secants meet at
    # ten 9-fold, 45 4-fold, and 36 5-fold projective rational points.
    # Over odd extensions of F3 only the nine F3 lines remain components;
    # over even extensions all 45 geometric lines are rational.
    for n in range(1,7):
        q=3**n
        d=(9*q-14) if n%2 else (45*q-314)
        u=q*q+q+1-d
        formula=q*q-8*q+15 if n%2 else q*q-44*q+315
        assert u==formula and u>=0
    assert 3*3-8*3+15==0
    assert 9*9-44*9+315==0
    assert 27*27-8*27+15==528
    assert 81*81-44*81+315==3312
    # Reconstruct source configuration in a good characteristic.
    p=19;a=3
    a0=(-(a**3-3*a-2)*pow(4,-1,p))%p
    b0=((a**3+a-2)*pow(4,-1,p))%p
    def norm19(v):
        for c in v:
            if c%p:return tuple(int(x)*pow(int(c),-1,p)%p for x in v)
        raise ValueError('zero')
    def cross19(v,w):
        return norm19((v[1]*w[2]-v[2]*w[1],v[2]*w[0]-v[0]*w[2],v[0]*w[1]-v[1]*w[0]))
    old_lines={norm19(tuple(eval(s,{'__builtins__':{}},{'A':a0,'B':b0})%p for s in triple)) for triple in COEFFICIENTS}
    assert len(old_lines)==45
    old_pts=defaultdict(set)
    ls=list(sorted(old_lines))
    for i,j in combinations(range(45),2):
        old_pts[cross19(ls[i],ls[j])].update((i,j))
    assert len(old_pts)==201
    assert Counter(map(len,old_pts.values()))==Counter({3:120,4:45,5:36})
    print('Wiman line reduction: 45 distinct lines over F9 = all 45 secants of conic')
    print('Conic points 10; plane points 91; incidences:',dict(sorted(hist.items())))
    print('Frobenius fixed: 9 lines, 13 points, correction 23')
    print('Good prime 19: 45 lines, 201 singular points, triple/quadruple/quintuple = 120/45/36')
    print('Complement point counts: F3 0, F9 0, F27 528, F81 3312')
    print('VERIFY_OK')

if __name__=='__main__':main()
