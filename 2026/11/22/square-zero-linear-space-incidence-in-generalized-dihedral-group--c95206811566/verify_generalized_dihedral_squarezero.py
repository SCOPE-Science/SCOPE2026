"""Standalone verification of square-zero and left-multiplication-rank counts
in small generalized dihedral group algebras, in characteristic two.
No external dependencies.
"""
from itertools import product
from collections import Counter
from math import prod

# GF(2) and GF(4) with a^2=a+1, represented by binary polynomials.
def mul(a,b,q):
    if q==2: return a & b
    z=0
    for i in range(2):
        if (b>>i)&1: z^=a<<i
    if z&8: z^=0b1100
    if z&4: z^=0b111
    return z

def inverse_signature(H,q):
    # Each character is labeled by a tuple of exponents in the dual abelian group.
    chars=list(product(*(range(m) for m in H)))
    zero=tuple(0 for m in H)
    inverse=lambda x:tuple((-xi)%mi for xi,mi in zip(x,H))
    frob=lambda x:tuple((q*xi)%mi for xi,mi in zip(x,H))
    unseen=set(chars)-{zero}
    ds=[]
    while unseen:
        x=min(unseen)
        orbit=set()
        while x not in orbit:
            orbit.add(x); orbit.add(inverse(x))
            x=frob(x)
        unseen-=orbit
        ds.append(len(orbit)//2)
    assert sum(ds)==(prod(H)-1)//2
    return sorted(ds)

def algebra_structure(H):
    h=list(product(*(range(m) for m in H)))
    m=len(h); idx={x:i for i,x in enumerate(h)}
    # (a,e)*(b,f) = (a+(-1)^e b, e+f).
    tab=[]
    for e in range(2):
        for a in h:
            row=[]
            for f in range(2):
                for b in h:
                    c=tuple((ai+(-1 if e else 1)*bi)%mod for ai,bi,mod in zip(a,b,H))
                    row.append(((e^f)*m+idx[c]))
            tab.append(row)
    return tab

def square_zero_binary(H, return_set=False):
    tab=algebra_structure(H); n=len(tab)
    count=Counter(); total=0; zeroset=set()
    for a in range(1<<n):
        bs=[i for i in range(n) if (a>>i)&1]
        sq=0
        for i in bs:
            for j in bs:
                sq^=1<<tab[i][j]
        if sq: continue
        total+=1; zeroset.add(a)
        # Left-multiplication matrix columns in GF2, computed via group algebra.
        pivots={}
        for j in range(n):
            col=0
            for i in bs: col^=1<<tab[i][j]
            while col:
                k=col.bit_length()-1
                if k in pivots: col^=pivots[k]
                else:
                    pivots[k]=col; break
        count[len(pivots)]+=1
    return (total, dict(sorted(count.items())), zeroset) if return_set else (total, dict(sorted(count.items())))

def square_zero_gf4_c3():
    H=(3,); tab=algebra_structure(H); n=len(tab); q=4
    total=0; count=Counter()
    for coeff in product(range(q),repeat=n):
        sq=[0]*n
        for i,a in enumerate(coeff):
            if not a: continue
            for j,b in enumerate(coeff):
                if b:sq[tab[i][j]]^=mul(a,b,q)
        if any(sq):continue
        total+=1
        cols=[]
        for j in range(n):
            v=[0]*n
            for i,a in enumerate(coeff):
                if a:v[tab[i][j]]^=a
            cols.append(v)
        piv=[]
        for col in cols:
            col=col[:]
            for row, v in piv:
                if col[row]:
                    factor=col[row]
                    for k in range(n):col[k]^=mul(factor,v[k],4)
            if any(col):
                row=next(k for k,x in enumerate(col) if x)
                inverse=next(a for a in range(1,4) if mul(a,col[row],4)==1)
                col=[mul(x,inverse,4) for x in col]
                piv.append((row,col));piv.sort()
        count[len(piv)]+=1
    return total,dict(sorted(count.items()))

def polynomial(H,q):
    ds=inverse_signature(H,q)
    p={0:1}
    for d in ds:
        nxt=Counter()
        for r,c in p.items():nxt[r]+=c;nxt[r+2*d]+=c*(q**(2*d)-1)
        p=dict(nxt)
    nxt=Counter()
    for r,c in p.items():nxt[r]+=c;nxt[r+1]+=c*(q-1)
    return dict(sorted(nxt.items())),ds



def maximal_binary_squarezero_spaces(H):
    from itertools import combinations
    _,_,X=square_zero_binary(H,return_set=True)
    flats={frozenset({0})}
    frontier=[frozenset({0})]
    while frontier:
        S=frontier.pop()
        for v in X-S:
            T=frozenset(S | {u^v for u in S})
            if T <= X and T not in flats:
                flats.add(T);frontier.append(T)
    maximal=[S for S in flats if not any(S<T for T in flats)]
    ds=inverse_signature(H,2)
    predicted_number=prod(2**d+1 for d in ds)
    predicted_size=2**(1+sum(ds))
    assert len(maximal)==predicted_number,(H,len(maximal),predicted_number)
    assert all(len(S)==predicted_size for S in maximal)
    intersections=Counter(len(U&V) for U,V in combinations(maximal,2))
    predicted=Counter()
    from itertools import product as cartesian_product
    choices=[(True,False) for _ in ds]
    for keep in cartesian_product(*choices):
        n=prod((1 if a else 2**d) for a,d in zip(keep,ds))
        if all(keep):continue
        intersection_size=2**(1+sum(d for a,d in zip(keep,ds) if a))
        predicted[intersection_size]+=predicted_number*n//2
    assert intersections==predicted,(H,intersections,predicted)
    print(f'linear_spaces q=2 H={H} number={len(maximal)} dimension={predicted_size.bit_length()-1} intersection_size_pairs={dict(sorted(intersections.items()))}')

def main():
    for H in [(3,),(5,),(7,),(3,3)]:
        expected,ds=polynomial(H,2)
        observed_total,observed=square_zero_binary(H)
        assert observed==expected,(H,ds,observed,expected)
        assert observed_total==2**prod(H)
        print(f'q=2 H={H} orbit_degrees={ds} total={observed_total} ranks={observed}')
    expected,ds=polynomial((3,),4)
    total,observed=square_zero_gf4_c3()
    assert observed==expected,(ds,observed,expected)
    assert total==4**3
    print(f'q=4 H=(3,) orbit_degrees={ds} total={total} ranks={observed}')
    for H in [(3,),(5,),(7,)]: maximal_binary_squarezero_spaces(H)
    print('VERIFY_OK')

if __name__=='__main__':main()
