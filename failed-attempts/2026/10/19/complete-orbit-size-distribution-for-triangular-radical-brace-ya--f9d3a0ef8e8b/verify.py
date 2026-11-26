"""Independent finite-field checks of radical-ring brace action orbit spectra.
No nonstandard packages required. Run python verify.py.
"""
from itertools import product
from collections import Counter

def add(x,y,q): return (x^y) if q==4 else (x+y)%q

def neg(x,q): return x if q==4 else (-x)%q

def mul(x,y,q):
    if q!=4: return x*y%q
    r=0
    for bit in range(2):
        if (y>>bit)&1: r ^= x<<bit
    if r&8: r ^= 0b1100  # t^3=t^2+t modulo t^2+t+1
    if r&4: r ^= 0b111   # t^2=t+1
    return r

def inv(x,q):
    if x==0: raise ValueError('divide by zero')
    return next(y for y in range(1,q) if mul(x,y,q)==1)

def rank(mat,q):
    if not mat: return 0
    a=[list(v) for v in mat]
    m=len(a); n=len(a[0]); r=0
    for j in range(n):
        t=next((t for t in range(r,m) if a[t][j]!=0),None)
        if t is None: continue
        a[r],a[t]=a[t],a[r]
        scale=inv(a[r][j],q)
        a[r]=[mul(z,scale,q) for z in a[r]]
        for k in range(m):
            if k!=r and a[k][j]:
                c=a[k][j]
                a[k]=[add(a[k][h],neg(mul(c,a[r][h],q),q),q) for h in range(n)]
        r+=1
        if r==m: break
    return r

def coords(n): return [(i,j) for i in range(n) for j in range(i+1,n)]

def action(A,B,n,q,pos):
    # B + A*B, multiplication explicitly, independent from row-flag formula.
    ret=list(B)
    for u,(i,j) in enumerate(pos):
        s=0
        for k in range(i+1,j):
            s=add(s,mul(A[pos.index((i,k))],B[pos.index((k,j))],q),q)
        ret[u]=add(ret[u],s,q)
    return tuple(ret)

def rank_direct(B,n,q,pos):
    vecs=[]
    for k,(i,j) in enumerate(pos):
        A=[0]*len(pos); A[k]=1
        AB=action(A,B,n,q,pos)
        vecs.append([add(AB[t],neg(B[t],q),q) for t in range(len(B))])
    return rank(vecs,q)

def rank_flags(B,n,q,pos):
    d=0; total=0; rows=[]
    for j in range(n-2,0,-1):
        row=[B[pos.index((j,k))] if k>j else 0 for k in range(n)]
        rows.append(row)
        d=rank(rows,q)
        total+=d
    return total

def expected_counts(n,q):
    # Bottom-up flag transition; key (dimension, orbit exponent).
    dp={(0,0):1}
    for j in range(n-2,0,-1):
        new={}
        for (d,r),count in dp.items():
            for dd,weight in ((d,q**d),(d+1,q**(n-1-j)-q**d)):
                if weight:
                    key=(dd,r+dd)
                    new[key]=new.get(key,0)+count*weight
        dp=new
    counts=Counter()
    for (d,r),v in dp.items(): counts[r]+=v*q**(n-1)
    return dict(counts)

def run(n,q,full_orbits=False):
    pos=coords(n); N=len(pos)
    expected=expected_counts(n,q)
    actual=Counter()
    samples=[]
    for B in product(range(q),repeat=N):
        rd=rank_direct(B,n,q,pos)
        rf=rank_flags(B,n,q,pos)
        assert rd==rf,(n,q,B,rd,rf)
        actual[rd]+=1
        if full_orbits:
            samples.append(B)
    assert dict(actual)==expected,(n,q,dict(actual),expected)
    if full_orbits:
        # Group-orbit sets computed from all elements rather than rank.
        As=list(product(range(q),repeat=N))
        seen=set(); orb_counts=Counter()
        for B in samples:
            if B in seen: continue
            orbit={action(A,B,n,q,pos) for A in As}
            assert B in orbit and len(orbit)==q**rank_direct(B,n,q,pos)
            assert not (seen&orbit)
            seen.update(orbit)
            orb_counts[len(orbit)]+=1
        assert len(seen)==q**N
        assert {q**r:c//(q**r) for r,c in expected.items()}==dict(orb_counts)
    assert expected[0]==q**(n-1)
    if n>2:
        R=(n-1)*(n-2)//2
        assert expected[R]//q**R==q*(q-1)**(n-2)
    print('CHECK n=%d q=%d full_orbits=%s elements=%d orbit_point_counts=%s number_of_orbits=%d PASS'%
          (n,q,full_orbits,q**N,dict(sorted(expected.items())),sum(c//q**r for r,c in expected.items())))

if __name__=='__main__':
    for args in [(2,2,True),(3,2,True),(4,2,True),(4,3,True),(4,4,False),(5,2,False),(6,2,False)]:
        run(*args)
    print('VERIFY_OK')
