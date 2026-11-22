"""Recompute the zero-product isotone partial-map census from first principles."""
from itertools import combinations, combinations_with_replacement
from math import comb

def maps(n):
    ans = [()]
    for k in range(1,n+1):
        for D in combinations(range(n),k):
            for Y in combinations_with_replacement(range(n),k):
                ans.append(tuple(zip(D,Y)))
    return ans

def count_formula(d,e,k,r):
    if k==r==0:return 1
    if not (1<=r<=k<=d and r<=e):return 0
    return comb(d,k)*comb(e,r)*comb(k-1,r-1)

def run():
    fib=[0,1]
    for _ in range(20):fib.append(fib[-1]+fib[-2])
    for n in range(2,6):
        m=maps(n); nonzero=[v for v in m if v]
        assert len(m)==sum(comb(n,k)*comb(n+k-1,k) for k in range(n+1))
        for d in range(1,n):
            for D in combinations(range(n),d):
                s=set(D)
                sub=[z for z in m if all(x in s and y not in s for x,y in z)]
                observed={}
                for z in sub:
                    k=len(z); r=len(set(y for _,y in z))
                    observed[k,r]=observed.get((k,r),0)+1
                expected={(k,r):count_formula(d,n-d,k,r) for k in range(d+1) for r in range(k+1)}
                assert all(observed.get(key,0)==val for key,val in expected.items()),(n,D,observed,expected)
                # Every outside element breaks the null property with a member of M(D).
                # It suffices to test singleton maps as witnesses.
                singles=[z for z in sub if len(z)==1]
                for z in nonzero:
                    if z in sub:continue
                    zd={x for x,y in z}; zy={y for x,y in z}
                    assert any((zy & {x}) or (zd & {y}) for ((x,y),) in singles),(n,D,z)
        profile=sum(sum(count_formula(d,n-d,k,r) for k in range(d+1) for r in range(k+1)) for d in range(n))
        assert profile==fib[2*n],(n,profile,fib[2*n])
        print(n,'maps',len(m),'maximal',2**n-2,'profile sum',profile)
    print('VERIFY_OK')
if __name__=='__main__':run()
