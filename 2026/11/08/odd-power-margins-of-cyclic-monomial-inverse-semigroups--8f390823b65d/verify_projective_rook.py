"""Independent finite enumeration for marginal power-word equivalence on cyclic monomial inverse semigroups."""
from itertools import combinations, permutations, product
from math import comb, factorial

def elements(m,n):
    out=[(None,)*m]
    for r in range(1,m+1):
        for cols in combinations(range(m),r):
            for rows in permutations(range(m),r):
                for phase in product(range(n),repeat=r):
                    a=[None]*m
                    for col,row,t in zip(cols,rows,phase): a[col]=(row,t)
                    out.append(tuple(a))
    return out

def mul(a,b,n):
    ans=[]
    for v in b:
        if v is None: ans.append(None); continue
        w=a[v[0]]
        ans.append(None if w is None else (w[0],(w[1]+v[1])%n))
    return tuple(ans)

def power(a,n):
    out=a
    for _ in range(1,n):out=mul(out,a,n)
    return out

def equiv_scalar(a,b,n):
    if all(v is None for v in a):return a==b
    for t in range(n):
        if tuple(None if v is None else (v[0],(v[1]+t)%n) for v in b)==a:return True
    return False

def exhaustive(m,n):
    all_a=elements(m,n)
    phases={a:[] for a in all_a}
    for a in all_a:
        sig=[]
        for x in all_a:
            sig.append((power(mul(a,x,n),n), power(mul(x,a,n),n)))
        phases[a]=tuple(sig)
    parts={}
    for a,sig in phases.items():parts.setdefault(sig,[]).append(a)
    for cell in parts.values():
        rep=cell[0]
        assert len(cell)==(n if any(v is not None for v in rep) else 1)
        assert all(equiv_scalar(a,rep,n) for a in cell)
    expected=1+sum(comb(m,r)**2*factorial(r)*n**(r-1) for r in range(1,m+1))
    assert len(parts)==expected,(m,n,len(parts),expected)
    margins=[]
    for a in all_a:
        supp={v[0] for v in a if v is not None}
        dom={j for j,v in enumerate(a) if v is not None}
        if dom!=supp or any(a[j][0]!=j for j in dom):continue
        e=tuple((j,0) if j in dom else None for j in range(m))
        if phases[a]==phases[e]:margins.append(a)
    predicted=1+n*(2**m-1)
    assert len(margins)==predicted,(m,n,len(margins),predicted)
    return (len(all_a),len(parts),len(margins))

for m,n in [(1,3),(2,3),(2,5),(3,3)]:
    size,classes,margin=exhaustive(m,n)
    print(f'ODD_OK m={m} n={n} elements={size} classes={classes} margin={margin}')

# Even exponent: differing diagonal entries can be equivalent.
m,n=2,4
all_a=elements(m,n)
ident=((0,0),(1,0))
twisted=((0,1),(1,3))
assert not equiv_scalar(ident,twisted,n)
assert all(power(mul(ident,x,n),n)==power(mul(twisted,x,n),n) and power(mul(x,ident,n),n)==power(mul(x,twisted,n),n) for x in all_a)
print('EVEN_BOUNDARY_OK m=2 n=4 elements=49 scalar-inequivalent-diagonals-marginally-equivalent')
print('VERIFY_OK')
