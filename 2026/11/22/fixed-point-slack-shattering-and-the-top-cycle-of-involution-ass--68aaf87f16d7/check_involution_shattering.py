"""Independent exhaustive verification of involution assignment-query shattering."""
from itertools import combinations
from math import factorial

def involutions(n):
    def rec(rest, pairs):
        if not rest:
            p=list(range(n))
            for i,j in pairs: p[i]=j; p[j]=i
            yield tuple(p)
            return
        i=rest[0]
        yield from rec(rest[1:], pairs)
        for j in rest[1:]:
            yield from rec(tuple(k for k in rest[1:] if k!=j), pairs+[(i,j)])
    return list(rec(tuple(range(n)), []))

def predicted(S,n):
    atoms=set(); used=set(); f=0
    for i,j in S:
        a=tuple(sorted((i,j)))
        if a in atoms or i in used or j in used: return False
        atoms.add(a); used.add(i); used.add(j)
        if i==j: f+=1
    return f==0 or len(used)<n

def is_shattered(S,perms):
    traces={tuple(p[i]==j for i,j in S) for p in perms}
    return len(traces)==(1<<len(S))

def main():
    for n in range(1,6):
        perms=involutions(n)
        q=[(i,j) for i in range(n) for j in range(n)]
        counts=[]
        shattered=set()
        for k in range(n+1):
            ans=0
            for S in combinations(q,k):
                pr=predicted(S,n)
                sh=is_shattered(S,perms)
                if pr != sh: raise AssertionError((n,k,S,pr,sh))
                if sh:
                    ans+=1
                    shattered.add(frozenset(S))
            counts.append(ans)
        coeff=[]
        for k in range(n+1):
            c=0
            for e in range(k+1):
                f=k-e
                if 2*e+f>n or (f>0 and 2*e+f==n):continue
                c+=factorial(n)//(factorial(e)*factorial(f)*factorial(n-2*e-f))
            coeff.append(c)
        assert counts==coeff, (n,counts,coeff)
        facets={S for S in shattered if all(S|{q0} not in shattered for q0 in q if q0 not in S)}
        actual_facets={}
        for S in facets:actual_facets[len(S)]=actual_facets.get(len(S),0)+1
        expected_facets={}
        for e in range(n//2+1):
            f=n-1-2*e
            if f>=0:
                k=e+f
                expected_facets[k]=expected_facets.get(k,0)+factorial(n)//(factorial(e)*factorial(f))
        if n%2==0:
            e=n//2
            expected_facets[e]=expected_facets.get(e,0)+factorial(n)//factorial(e)
        if n>1: assert actual_facets==expected_facets,(n,actual_facets,expected_facets)
        print(n,len(perms),counts,'facets',actual_facets,flush=True)
    print('PASS complete all oriented supports for n<=5')
if __name__=='__main__':main()
