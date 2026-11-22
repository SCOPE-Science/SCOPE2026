"""Reproducible finite exact checks for special-linear two-sum fibers over small characteristic-two chain rings."""
from collections import Counter
from itertools import product

def fq4_mul(a,b):
    z=0
    for i in range(2):
        if (b>>i)&1:z^=a<<i
    if z&8: raise ValueError('degree unexpectedly high')
    if z&4:z^=7
    return z

def mul(a,b,k,q):
    if q==4:
        assert k==1
        return fq4_mul(a,b)
    z=0
    for i in range(k):
        if (b>>i)&1:z^=a<<i
    return z&((1<<k)-1)

def det(M,k,q):
    a,b,c,d=M
    return mul(a,d,k,q)^mul(b,c,k,q)

def classify(A,k,q):
    if q==4:
        a,b,c,d=A
        if A==(0,0,0,0):return 'zero'
        delta=det(A,k,q)
        if delta==0:return 'primitive_rank1'
        # absolute trace of delta^{-1} in F4; all nonzero elements have inverse delta^2
        inv=mul(delta,delta,1,4)
        tr=inv^mul(inv,inv,1,4)
        return 'invertible_trace1' if tr==1 else 'invertible_trace0'
    if A==(0,0,0,0):return 'zero'
    s=min(next(i for i in range(k) if (a>>i)&1) for a in A if a)
    # leading binary coefficient matrix rank
    B=tuple((a>>s)&1 for a in A)
    rank2=(B[0]*B[3])^(B[1]*B[2])
    if not rank2:return ('primitive_rank1' if s==0 else f'valuation{s}_rank1')
    if s:return f'valuation{s}_rank2'
    # only q2 invertible case, determinant necessarily 1; Tr_F2(1)=1
    return 'invertible_trace1'

def check(k,q):
    cardinal=q**k if q==2 else 4
    mats=list(product(range(cardinal),repeat=4))
    G=[A for A in mats if det(A,k,q)==1]
    counts=Counter(tuple(x^y for x,y in zip(A,B)) for A in G for B in G)
    assert sum(counts.values())==len(G)**2
    expected_size=q**(3*k-2)*(q*q-1)
    assert len(G)==expected_size,(k,q,len(G),expected_size)
    expected_min=q**(2*k-1)*(q-1)
    assert min(counts.values())==expected_min
    classes=Counter()
    for A in mats:
        typ=classify(A,k,q)
        got=counts[A]
        classes[typ]+=1
        if typ=='zero':wanted=len(G)
        elif typ=='primitive_rank1':wanted=expected_min
        elif typ=='invertible_trace1':wanted=expected_min
        elif typ=='invertible_trace0':wanted=q**(2*k-1)*(q+1)
        elif typ.startswith('valuation'):
            s=int(typ.split('_')[0].removeprefix('valuation'))
            if typ.endswith('rank1'):wanted=q**(2*k+s-1)*(q-1)
            else:
                wanted=q**(2*k+s-2)*(q*q-1)
                assert got>=wanted,(A,got,wanted)
                continue
        else:raise AssertionError(typ)
        assert got==wanted,(q,k,A,typ,got,wanted)
    print(f'q={q} k={k} |SL2|={len(G)} targets={len(mats)} min={expected_min} minimizers={sum(1 for A in mats if counts[A]==expected_min)} classes={dict(sorted(classes.items()))}')

for k,q in [(1,2),(2,2),(3,2),(1,4)]:check(k,q)
print('VERIFY_OK')

def gf4_dual_mul(a,b):
    a0,a1=a&3,(a>>2)&3
    b0,b1=b&3,(b>>2)&3
    return fq4_mul(a0,b0)|((fq4_mul(a0,b1)^fq4_mul(a1,b0))<<2)

def gf4_dual_det(M):
    a,b,c,d=M
    return gf4_dual_mul(a,d)^gf4_dual_mul(b,c)

D=[M for M in product(range(16),repeat=4) if gf4_dual_det(M)==1]
assert len(D)==3840
cases=[
    ((1,0,0,0),192), # rank-one primitive
    ((1,0,0,1),320), # split invertible reduction
    ((1,0,0,2),192), # irreducible invertible reduction
    ((4,0,0,0),768), # valuation-one, rank-one leading term
    ((0,0,0,0),3840),
]
for A,want in cases:
    count=sum(gf4_dual_det(tuple(a^u for a,u in zip(A,U)))==1 for U in D)
    assert count==want,(A,count,want)
    print(f'q=4 k=2 target={A} representations={count}')
print('VERIFY_DUAL_OK')
