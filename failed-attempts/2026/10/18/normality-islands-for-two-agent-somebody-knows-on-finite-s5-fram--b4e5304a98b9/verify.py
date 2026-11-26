from functools import lru_cache
from math import comb

@lru_cache(None)
def partitions(n):
    if n == 0: return ((),)
    ans=[]
    for p in partitions(n-1):
        for i in range(len(p)):
            t=list(p);t[i]=t[i]+(n-1,);ans.append(tuple(t))
        ans.append(p+((n-1,),))
    return tuple(ans)

def cells(p,n):
    return tuple(next(frozenset(B) for B in p if v in B) for v in range(n))

def b_on(a,b,mask,n):
    S={j for j in range(n) if (mask>>j)&1}
    return sum((1<<v) for v in range(n) if a[v]<=S or b[v]<=S)

def nested(a,b):
    return all(a[v] <= b[v] or b[v] <= a[v] for v in range(len(a)))

def graph_stars(p,q,n):
    A=[frozenset(x) for x in p];B=[frozenset(x) for x in q]
    return all(len([b for b in B if a&b])==1 or len([a2 for a2 in A if a2&b])==1 for a in A for b in B if a&b)

BELLS=[len(partitions(n)) for n in range(8)]
C=[1]
for n in range(1,8):
    C.append(sum(comb(n-1,j-1)*(2*BELLS[j]-1)*C[n-j] for j in range(1,n+1)))
print('bell:',BELLS, 'predicted:',C)
for n in range(1,7):
    pp=partitions(n); cc=[cells(p,n) for p in pp]
    count=0
    for i,p in enumerate(pp):
        for j,q in enumerate(pp):
            a,b=cc[i],cc[j]
            test=nested(a,b)
            assert graph_stars(p,q,n)==test
            if test:
                count+=1
                # exact equality to S5 distributed box for every A
                for mask in range(1<<n):
                    B=b_on(a,b,mask,n)
                    meetcells=tuple(a[v]&b[v] for v in range(n))
                    assert B == b_on(meetcells,meetcells,mask,n)
            if n<=4:
                actual=all(b_on(a,b,x&y,n)==(b_on(a,b,x,n)&b_on(a,b,y,n)) for x in range(1<<n) for y in range(1<<n))
                assert test == actual
    assert count==C[n],(n,count,C[n]);print(n,len(pp)**2,count)
print('BUNDLE_NORMALITY_CENSUS_OK')
