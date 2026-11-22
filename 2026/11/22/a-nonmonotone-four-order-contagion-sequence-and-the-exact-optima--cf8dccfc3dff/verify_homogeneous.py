"""Independent homogeneous-form incidence construction and exhaustive checking.
The construction enumerates normalized nonzero line forms rather than slopes.
Run: python3 verify_homogeneous.py; standard library only.
"""
from itertools import product,combinations
from collections import Counter

def plane(q,poly=None):
    def plus(a,b):return a^b if poly else (a+b)%q
    def mult(a,b):
        if poly is None:return a*b%q
        z=0
        for i in (0,1):
            if b>>i&1:z^=a<<i
        for i in (3,2):
            if z>>i&1:z^=poly<<(i-2)
        return z
    inv={x:next(y for y in range(1,q) if mult(x,y)==1) for x in range(1,q)}
    P=[(x,y,1) for x in range(q) for y in range(q)]
    L=[]
    for t in product(range(q),repeat=3):
        if t==(0,0,0) or (t[0]==0 and t[1]==0):continue
        a=next(v for v in t if v)
        if t==tuple(mult(v,inv[a]) for v in t):L.append(t)
    n=len(P);assert len(L)==q*(q+1)
    nbr=[0]*(n+len(L))
    for i,Pv in enumerate(P):
        for j,Lv in enumerate(L):
            v=0
            for a,b in zip(Pv,Lv):v=plus(v,mult(a,b))
            if v==0:
                nbr[i]|=1<<(n+j)
                nbr[n+j]|=1<<i
    return nbr,n

def final(seed,nbr):
    a=0
    for k in seed:a |=1<<k
    rounds=0
    while True:
        new=0
        for i,m in enumerate(nbr):
            if (a>>i)&1==0 and (a&m).bit_count()>=2:new|=1<<i
        if not new:return a.bit_count(),rounds
        a|=new;rounds+=1

def census(q,k,expected,poly=None):
    nbr,n=plane(q,poly);N=len(nbr);found=Counter();time=Counter()
    for S in combinations(range(N),k):
        size,t=final(S,nbr)
        if size==N:
            found[sum(i<n for i in S)]+=1
            time[t]+=1
    result=tuple(found[i] for i in range(k+1))
    assert result==expected,(q,k,result,expected)
    print('homogeneous field order %d, k=%d: point counts %s; times %s'%(q,k,result,dict(sorted(time.items()))),flush=True)

if __name__=='__main__':
    census(2,4,(3,4,0,0,1))
    census(3,4,(0,0,0,0,0))
    census(3,5,(396,1224,1404,1080,396,72))
    census(4,4,(0,0,0,0,0),0b111)
    census(4,5,(8448,32640,46080,36480,15840,2688),0b111)
    census(5,4,(9000,32000,0,24000,5000))
    print('HOMOGENEOUS EXHAUSTIVE VERIFICATION PASSED')
