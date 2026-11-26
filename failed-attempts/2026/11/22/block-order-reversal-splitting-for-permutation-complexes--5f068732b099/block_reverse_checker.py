"""Standalone exact finite-field checks of block-order reversal permutation complexes.
Usage: python block_reverse_checker.py . No packages beyond the standard library.
"""
from itertools import permutations, combinations, product
from functools import lru_cache

def complex_words(facets):
    s = set()
    for w in facets:
        for k in range(1, len(w)+1):
            s.update(tuple(w[i] for i in js) for js in combinations(range(len(w)), k))
    n = len(next(iter(facets)))
    return [sorted(w for w in s if len(w)==k+1) for k in range(n)]

def rank_mod(rows, cols, p):
    pos={x:i for i,x in enumerate(rows)}
    piv={}
    for w in cols:
        c={pos[w[:j]+w[j+1:]]:(-1 if j%2 else 1)%p for j in range(len(w))}
        while c:
            q=min(c)
            if q in piv:
                b=piv[q]
                f=c[q]
                for i,z in b.items():
                    v=(c.get(i,0)-f*z)%p
                    if v: c[i]=v
                    else: c.pop(i,None)
            else:
                inv=pow(c[q],-1,p)
                piv[q]={i:(z*inv)%p for i,z in c.items()}
                break
    return len(piv)

def betti(facets,p):
    w=complex_words(facets)
    r=[rank_mod(w[i-1],w[i],p) for i in range(1,len(w))]
    return [len(w[i])-(r[i-1] if i else 0)-(r[i] if i<len(r) else 0) for i in range(len(w))],tuple(map(len,w))

def predicted(a,b,N):
    # a,b are ordinary Betti vectors of connected complexes
    ans=[0]*N
    ans[0]=ans[1]=1
    for i in range(1,len(a)):
        ans[i+1]+=a[i]
    for j in range(1,len(b)):
        ans[j+1]+=b[j]
    for i in range(1,len(a)):
        for j in range(1,len(b)):
            ans[i+j+1]+=2*a[i]*b[j]
    return ans

def reverse_facets(aa,bb):
    return [u+v for u,v in product(aa,bb)] + [v+u for u,v in product(aa,bb)]

def all_nonempty(P):
    for mask in range(1,1<<len(P)):
        yield [P[i] for i in range(len(P)) if mask>>i &1]

def check(aa,bb,primes=(2,101)):
    for p in primes:
        va,_=betti(aa,p);vb,_=betti(bb,p)
        vc,f=betti(reverse_facets(aa,bb),p)
        expected=predicted(va,vb,len(vc))
        assert vc==expected,(aa,bb,p,vc,expected)
    return f

def run():
    P2=list(permutations(range(2)))
    P3=list(permutations(range(2,5)))
    n=0
    for aa in all_nonempty(P2):
        for bb in all_nonempty(P2):
            bb=[tuple(x+2 for x in q) for q in bb]
            f=check(aa,bb);n+=1
    print('PASS all 9 nonempty pairs on 2+2 letters')
    for aa in all_nonempty(P2):
        for bb in all_nonempty(P3):
            f=check(aa,bb);n+=1
    print('PASS all 189 nonempty pairs on 2+3 letters')
    P3a=list(permutations(range(3)));P3b=list(permutations(range(3,6)))
    choices=[1,3,7,15,31,63]
    for maska in choices:
        for maskb in choices:
            aa=[P3a[i] for i in range(6) if maska>>i&1]
            bb=[P3b[i] for i in range(6) if maskb>>i&1]
            f=check(aa,bb);n+=1
    print('PASS 36 representative pairs on 3+3 letters')
    print('PASS',n,'total exact GF(2)/GF(101) homology comparisons')
    full2=P2;full3=P3
    for aa,bb in [(full2,[tuple(x+2 for x in q) for q in full2]),(full2,full3),(P3a,P3b)]:
        v,f=betti(reverse_facets(aa,bb),101)
        print('full-block case',len(aa[0]),len(bb[0]),'faces',f,'Betti',v)
if __name__=='__main__':run()
