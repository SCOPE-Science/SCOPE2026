"""Exact rank-generating polynomial checks for acyclic orientations of K_(2,2,n)."""
from functools import lru_cache
from math import comb


def add(*xs):
    if not xs:return (0,)
    N=max(map(len,xs))
    return tuple(sum(x[i] if i<len(x) else 0 for x in xs) for i in range(N))


def scaled_shift(p,scale=1,shift=0):
    return (0,)*shift+tuple(scale*x for x in p)


def multiply(a,b):
    z=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        if x:
            for j,y in enumerate(b):
                z[i+j]+=x*y
    return tuple(z)


def power(p,n):
    r=(1,)
    while n:
        if n&1:r=multiply(r,p)
        p=multiply(p,p)
        n//=2
    return r


def closed_formula(n):
    a=(1,0,1,0,1)
    b=(1,1,1,0,1)
    c=(1,1,0,1,1)
    d=(1,0,1,1,1)
    e=(1,1,1,1,1)
    # (t^4+1)[a^n-2b^n-2d^n]-4t^2c^n+4(t^2+1)(t^2+t+1)e^n
    return add(multiply((1,0,0,0,1),add(power(a,n),scaled_shift(power(b,n),-2),scaled_shift(power(d,n),-2))),
               scaled_shift(power(c,n),-4,2),
               multiply((4,4,8,4,4),power(e,n)))


def source_layer_formula(n):
    @lru_cache(None)
    def rec(remaining,last):
        if sum(remaining)==0:return (1,)
        terms=[]
        for i,m in enumerate(remaining):
            if i==last or m==0:continue
            for k in range(1,m+1):
                rem=list(remaining);rem[i]-=k
                terms.append(scaled_shift(rec(tuple(rem),i),comb(m,k),k*sum(remaining[:i])))
        return add(*terms)
    return rec((2,2,n),-1)


def brute(n):
    N=4+n
    color=lambda v:0 if v<2 else (1 if v<4 else 2)
    edges=[(i,j) for i in range(N) for j in range(i+1,N) if color(i)!=color(j)]
    hist=[0]*(len(edges)+1)
    for mask in range(1<<len(edges)):
        indeg=[0]*N; out=[0]*N
        for k,(i,j) in enumerate(edges):
            if mask&(1<<k):i,j=j,i
            indeg[j]+=1; out[i]|=(1<<j)
        stack=[i for i in range(N) if not indeg[i]]
        seen=0
        while stack:
            i=stack.pop();seen+=1
            nbr=out[i]
            while nbr:
                bit=nbr&-nbr;j=bit.bit_length()-1;nbr-=bit
                indeg[j]-=1
                if indeg[j]==0:stack.append(j)
        if seen==N:hist[mask.bit_count()]+=1
    return tuple(hist)



def exact_fourteen_skeleton_certificate():
    """Finite symbolic 14-interleaving reduction, with no algebra package."""
    from itertools import combinations
    from collections import defaultdict
    from math import factorial
    def poly_add(a,b):
        return add(a,b)
    grouped=defaultdict(lambda:(0,))
    count=0
    for A in [(2,),(1,1)]:
        for B in [(2,),(1,1)]:
            for positions in combinations(range(len(A)+len(B)),len(A)):
                ai=iter(A);bi=iter(B)
                blocks=[('A',next(ai)) if j in positions else ('B',next(bi)) for j in range(len(A)+len(B))]
                count+=1
                w=factorial(2)**2
                for _,size in blocks:w//=factorial(size)
                inversions=sum(p*q for i,(letter,p) in enumerate(blocks) for nextletter,q in blocks[i+1:] if letter=='B' and nextletter=='A')
                terms=[((0,),scaled_shift((1,),w,inversions))]
                for gap in range(len(blocks)+1):
                    right=sum(size for _,size in blocks[gap:])
                    mandatory=(0<gap<len(blocks) and blocks[gap-1][0]==blocks[gap][0])
                    newer=[]
                    for exponent,coefficient in terms:
                        newer.append((poly_add(exponent,scaled_shift((1,),1,right)),coefficient))
                        if mandatory:newer.append((exponent,scaled_shift(coefficient,-1)))
                    terms=newer
                for expo,coefficient in terms:
                    grouped[expo]=add(grouped[expo],coefficient)
    grouped={k:v for k,v in grouped.items() if any(v)}
    A=(1,0,1,0,1);B=(1,1,1,0,1);C=(1,1,0,1,1);D=(1,0,1,1,1);E=(1,1,1,1,1)
    expected={A:(1,0,0,0,1),B:(-2,0,0,0,-2),C:(0,0,-4),D:(-2,0,0,0,-2),E:(4,4,8,4,4)}
    assert count==14
    assert {k:tuple(v) for k,v in grouped.items()}==expected, (grouped,expected)
    print('EXACT_14_SKELETON_SYMBOLIC_REDUCTION_OK skeletons=14 profiles=5')


if __name__=='__main__':
    exact_fourteen_skeleton_certificate()
    for n in range(0,13):
        a=closed_formula(n);b=source_layer_formula(n)
        assert a==b,(n,a,b)
        assert len(a)==4+4*n+1
        assert a==a[::-1]
        assert sum(a)==24*5**n-12*4**n+2*3**n
        if n>=1:assert sum((-1)**k*v for k,v in enumerate(a))==2*3**n-8*2**n+8
    print('EXACT_SOURCE_LAYER_AND_FIVE_POWER_FORMULA_OK n=0..12')
    for n in range(0,5):
        actual=brute(n)
        assert actual==closed_formula(n),(n,actual,closed_formula(n))
        print('ALL_EDGE_ORIENTATIONS_OK n=%d edges=%d acyclic=%d'%(n,4+4*n,sum(actual)))
    print('VERIFY_OK')
