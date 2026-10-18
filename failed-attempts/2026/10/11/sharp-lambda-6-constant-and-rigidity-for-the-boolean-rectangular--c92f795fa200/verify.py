from fractions import Fraction as F
from itertools import product

# Complex rationals as (real, imag).
def C(a=0,b=0): return (F(a),F(b))
def add(x,y): return (x[0]+y[0],x[1]+y[1])
def mul(x,y): return (x[0]*y[0]-x[1]*y[1],x[0]*y[1]+x[1]*y[0])
def conj(x): return (x[0],-x[1])
def abs2(x): return x[0]*x[0]+x[1]*x[1]
def smul(q,x): return (q*x[0],q*x[1])
def csum(xs):
    s=C()
    for x in xs: s=add(s,x)
    return s

def inner(x,y):
    return csum(mul(a,conj(b)) for a,b in zip(x,y))

def laurent_mul(p,q):
    r={}
    for i,a in p.items():
        for j,b in q.items():
            r[i+j]=add(r.get(i+j,C()),mul(a,b))
    return r

def laurent_pow(p,n):
    r={0:C(1)}
    for _ in range(n): r=laurent_mul(r,p)
    return r

def hilbert_direct_integral6(x,y):
    A=sum(abs2(t) for t in x)+sum(abs2(t) for t in y)
    c=inner(y,x)
    p={0:C(A),1:c,-1:conj(c)}
    return laurent_pow(p,3).get(0,C())[0]

def hilbert_formula(x,y):
    px=sum(abs2(t) for t in x); py=sum(abs2(t) for t in y); A=px+py
    c=inner(x,y); c2=abs2(c)
    integral=A**3+6*A*c2
    deficit=F(3,2)*A*((px-py)**2+4*(px*py-c2))
    return integral,deficit,F(5,2)*A**3

def conv_cube_moment(coeffs,d):
    freqs=list(product((0,1), repeat=d))
    out={}
    for i,e1 in enumerate(freqs):
        for j,e2 in enumerate(freqs):
            for k,e3 in enumerate(freqs):
                s=tuple(e1[t]+e2[t]+e3[t] for t in range(d))
                v=mul(mul(coeffs[i],coeffs[j]),coeffs[k])
                out[s]=add(out.get(s,C()),v)
    return sum(abs2(v) for v in out.values())

def sharp_rhs(coeffs,d):
    S=sum(abs2(c) for c in coeffs)
    return F(5,2)**d * S**3

def flat_coeffs(d):
    # lambda=1, eta_j alternates i and -1; all unit rational complex phases.
    etas=[C(0,1) if j%2==0 else C(-1,0) for j in range(d)]
    cs=[]
    for e in product((0,1), repeat=d):
        v=C(1)
        for j,b in enumerate(e):
            if b: v=mul(v,etas[j])
        cs.append(v)
    return cs

pairs=[
    ([C(1),C(2,-1)],[C(0,1),C(3)]),
    ([C(1,1),C(-1,2),C(2)],[C(2,-1),C(0,1),C(1,-2)]),
    ([C(3),C(-2,1)],[C(3),C(-2,1)]),
]
for x,y in pairs:
    direct=hilbert_direct_integral6(x,y)
    integ,deficit,top=hilbert_formula(x,y)
    assert direct==integ
    assert top-integ==deficit
    assert deficit>=0

cases={
1:[C(1),C(2,1)],
2:[C(1),C(1,1),C(-1,2),C(2,-1)],
3:[C(1),C(1,1),C(2),C(-1,1),C(0,1),C(2,-1),C(1,-2),C(3)],
}
for d,cs in cases.items():
    lhs=conv_cube_moment(cs,d)
    rhs=sharp_rhs(cs,d)
    assert lhs<=rhs

for d in range(1,5):
    cs=flat_coeffs(d)
    lhs=conv_cube_moment(cs,d)
    rhs=sharp_rhs(cs,d)
    assert lhs==rhs

print('VERIFY_OK dimensions=1..4 exact_hilbert_pairs=3 exact_cube_cases=3 flat_extremizers=4')
