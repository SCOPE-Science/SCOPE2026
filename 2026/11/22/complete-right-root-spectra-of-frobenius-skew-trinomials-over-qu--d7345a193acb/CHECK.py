"""Exhaustive right-Ore-root spectrum checks for Frobenius skew trinomials."""
from collections import Counter
from math import gcd

def prime(p):
    return p >= 2 and all(p % d for d in range(2, int(p**.5)+1))

def check(p,n):
    delta=next(d for d in range(2,p) if pow(d,(p-1)//2,p)==p-1)
    q=p
    def mul(a,b):
        x,y=a; z,w=b
        return ((x*z+delta*y*w)%p,(x*w+y*z)%p)
    def power(a,k):
        b=(1,0)
        while k:
            if k&1:b=mul(b,a)
            a=mul(a,a); k>>=1
        return b
    norm=lambda z:mul(z,power(z,p))
    all_elements=[(x,y) for x in range(p) for y in range(p)]
    nonzero=[z for z in all_elements if z!=(0,0)]
    observed={}
    for a in all_elements:
        hits=0
        for u in nonzero:
            prod=(1,0)
            term_n=None
            frob=power(u,p)
            for j in range(1,2*n+1):
                prod=mul(prod,u if (j % 2) else frob)
                if j==n:
                    term_n=prod
            middle=mul(a,term_n)
            hits+=int((prod[0]+middle[0]+1)%p==0 and (prod[1]+middle[1])%p==0)
        observed[a]=hits
    h=lambda k:set(pow(t,k,p) for t in range(1,p))
    pred={}
    if n%2:
        g=gcd(n,p-1); H=h(n)
        for a in all_elements:
            if a==(0,0):pred[a]=g*(p+1)*int(p-1 in H)
            else:
                B=norm(a)[0]
                pred[a]=g*sum((z+1)**2%p == B*z%p for z in H)
        eps=int(p-1 in H)
        target={g:p+1,2*g:(p+1)*(len(H)-1-eps)//2}
        target[0]=p*p-1-sum(target.values())
        target[g*(p+1)*eps]=target.get(g*(p+1)*eps,0)+1
    else:
        j=n//2; g=gcd(j,p-1); J=h(j)
        for a in all_elements:
            pred[a]=g*(p+1)*sum((z*z+a[0]*z+1)%p==0 for z in J) if a[1]==0 else 0
        eps=int(p-1 in J)
        target={g*(p+1):1+eps, 2*g*(p+1):(len(J)-1-eps)//2}
        target[0]=p*p-sum(target.values())
    assert observed==pred,(p,n,[(a,observed[a],pred[a]) for a in all_elements if observed[a]!=pred[a]][:4])
    assert Counter(observed.values())==Counter({k:v for k,v in target.items() if v>0}),(p,n,Counter(observed.values()),target)
    return len(all_elements)*(len(nonzero))

if __name__=='__main__':
    cases=0; tests=0
    for p in [3,5,7,11,13]:
        for n in range(1,21):
            tests+=check(p,n);cases+=1
    print(f'ORE_ROOTS_OK {cases} cases, {tests} exact right-root evaluations')
