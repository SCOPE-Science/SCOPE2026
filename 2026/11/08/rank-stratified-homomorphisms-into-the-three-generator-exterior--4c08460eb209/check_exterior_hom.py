"""Direct exterior multiplication checks for maps to the 3-generator exterior algebra.
Uses no closed-form fiber equations when deciding whether images define a homomorphism.
Run: python check_exterior_hom.py
"""
from itertools import product
from math import prod

PAIRS=[(a,b) for a in range(1,8) for b in range(1,8) if (a&b)==0]
SIGN={}
for a,b in PAIRS:
    inversions=sum((a>>i&1)*(b&((1<<i)-1)).bit_count() for i in range(3))
    SIGN[a,b]=-1 if inversions%2 else 1

def mul(x,y,q):
    z=[0]*8
    for a,b in PAIRS:
        z[a|b]=(z[a|b]+SIGN[a,b]*x[a]*y[b])%q
    return z

def is_map(images,q):
    zero=[0]*8
    for i,u in enumerate(images):
        if mul(u,u,q)!=zero:
            return False
        for v in images[:i]:
            p=mul(u,v,q); t=mul(v,u,q)
            if any((a+b)%q for a,b in zip(p,t)):
                return False
    return True

def rank(V,q):
    rows=[list(row) for row in V]
    if not rows:return 0
    k=0;n=len(rows[0])
    for j in range(n):
        p=next((i for i in range(k,len(rows)) if rows[i][j]%q),None)
        if p is None: continue
        rows[k],rows[p]=rows[p],rows[k]
        inv=pow(rows[k][j],-1,q)
        rows[k]=[(v*inv)%q for v in rows[k]]
        for i in range(len(rows)):
            if i!=k and rows[i][j]:
                b=rows[i][j]
                rows[i]=[(a-b*v)%q for a,v in zip(rows[i],rows[k])]
        k+=1
        if k==len(rows):break
    return k

def predicted(m,q):
    out={}
    for r in range(min(3,m)+1):
        count=prod((q**3-q**i)*(q**m-q**i) for i in range(r))//prod(q**r-q**i for i in range(r))
        out[r]=count*q**(m*(4-r)+r*(r-1)//2)
    return out

def direct(m,q):
    observed={r:0 for r in range(min(m,3)+1)}
    for linear in product(range(q),repeat=3*m):
        vv=[linear[3*i:3*i+3] for i in range(m)]
        rr=rank(vv,q)
        for quadratic in product(range(q),repeat=3*m):
            images=[]
            for i in range(m):
                a,b,c=vv[i]
                d,e,f=quadratic[3*i:3*i+3]
                images.append((0,a,b,d,c,e,f,0))
            if is_map(images,q):observed[rr]+=1
    got={r:v*q**m for r,v in observed.items()}  # arbitrary cubic terms
    want=predicted(m,q) if q%2 else {r:None for r in got}
    if q%2:
        assert got==want,(m,q,got,want)
    else:
        assert sum(got.values())==q**(7*m),(m,q,got)
    print(f'DIRECT_EXTERIOR: m={m} q={q} counts_by_linear_rank={got} total={sum(got.values())} OK')

def canonical(m,q):
    observed={}
    for r in range(min(m,3)+1):
        v=[[1 if j==i and i<r else 0 for j in range(3)] for i in range(m)]
        count=0
        for quadratic in product(range(q),repeat=3*m):
            imgs=[]
            for i in range(m):
                a,b,c=v[i];d,e,f=quadratic[3*i:3*i+3]
                imgs.append((0,a,b,d,c,e,f,0))
            if is_map(imgs,q):count+=1
        target=q**(m*(3-r)+r*(r-1)//2)
        assert count==target,(m,r,q,count,target)
        observed[r]=count
    print(f'CANONICAL_FIBERS: m={m} q={q} quadratic_counts={observed} OK')

if __name__=='__main__':
    direct(1,3)
    direct(2,3)
    direct(2,2)
    direct(1,5)
    canonical(3,3)
    print('EXTERIOR_HOM_DIRECT_CHECK_OK')
