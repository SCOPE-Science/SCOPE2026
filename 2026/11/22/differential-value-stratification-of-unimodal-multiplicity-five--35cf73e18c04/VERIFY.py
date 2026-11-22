"""Standalone exact truncated-jet computation of differential values in a parametrized branch.
This checks specified rational parameter examples; the proof of all parameters is algebraic.
"""
from fractions import Fraction as Q
from itertools import product
N=14  # coefficients for powers t^0,...,t^13; differential coefficient to t^12

def poly(terms):
    a=[Q(0)]*N
    for d,c in terms.items():
        if d<N: a[d]+=Q(c)
    return tuple(a)
def mul(a,b):
    z=[Q(0)]*N
    for i,x in enumerate(a):
        if x:
            for j,y in enumerate(b[:N-i]):
                if y: z[i+j]+=x*y
    return tuple(z)
def derivative(a):
    return tuple((i+1)*a[i+1] for i in range(N-1))+(Q(0),)
def ords(a):
    return next((i for i,x in enumerate(a) if x),N)

def basis_indices(forms):
    # Gaussian elimination with leading low-degree coefficient; only coefficients t^0..t^12 count.
    basis={}
    for form in forms:
        row=list(form[:N-1]);
        while True:
            j=next((i for i,a in enumerate(row) if a),None)
            if j is None: break
            if j not in basis:
                scale=row[j]; basis[j]=[u/scale for u in row]; break
            a=row[j]; row=[v-a*w for v,w in zip(row,basis[j])]
    return sorted(i+1 for i in basis)
def compute(x,y,z):
    # All coefficient monomials whose valuation is <=8 suffice to detect values <=13.
    seen={(0,0,0)}
    q=[(poly({0:1}),(0,0,0))]; all_m=[]
    while q:
        p,ind=q.pop(0)
        if ords(p)>8: continue
        all_m.append(p)
        for i,f in enumerate((x,y,z)):
            ix=tuple(ind[j]+(j==i) for j in range(3))
            if ix not in seen:
                seen.add(ix); q.append((mul(p,f),ix))
    forms=[mul(m,derivative(f)) for m,f in product(all_m,(x,y,z))]
    return basis_indices(forms)

def assert_check(x,y,z,expected,name):
    got=compute(poly(x),poly(y),poly(z)); assert got==expected, (name,got,expected)
    print(name,got)

G567=[5,6,7,10,11,12,13]
G568=[5,6,8,10,11,12,13]
G569=[5,6,9,10,11,12]
G578=[5,7,8,10,12,13]
for a in [-3,0,1,2,5]:
    assert_check({5:1},{6:1,8:1,9:a},{7:1},G567,f'<5,6,7> I a={a}')
for a in [0,1]:
    assert_check({5:1},{6:1,9:a},{7:1},G567,f'<5,6,7> II a={a}')
for a in [0,1]:
    assert_check({5:1},{6:1,7:a},{8:1},G568,f'<5,6,8> a={a}')
for b in [-2,0,1,Q(13,12),Q(11,6),3]:
    assert_check({5:1},{6:1,7:1,8:b},{9:1},G569 + ([] if b==Q(13,12) else [13]),f'<5,6,9> I b={b}')
for c in [0,1]:
    assert_check({5:1},{6:1,8:c},{9:1},G569 + ([13] if c else []),f'<5,6,9> II c={c}')
for b,c in product([0,1,2],repeat=2):
    assert_check({5:1},{7:1,11:b},{8:1,9:c},G578,f'<5,7,8> I b={b},c={c}')
for a,b in product([0,1,2],repeat=2):
    assert_check({5:1},{7:1,9:a,11:b},{8:1,9:1},G578,f'<5,7,8> II a={a},b={b}')
print('PASS: all checked characteristic-zero rational cases have the predicted truncated differential values.')
