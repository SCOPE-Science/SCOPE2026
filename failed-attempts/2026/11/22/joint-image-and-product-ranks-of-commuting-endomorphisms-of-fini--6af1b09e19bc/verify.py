"""Independent finite checks of commuting affine tuples and clique coefficients."""
from itertools import product, combinations
from math import comb, prod

def local_T(p,e,t):
    h=(e-1)//2
    c=(p+1)*sum(p**(e-1-2*v) for v in range(h+1))
    a=c+(e%2==0)
    b=1-a
    return a*p**(e*t)+b*p**((e-1)*t)

def count_direct(n,t):
    el=list(product(range(n),repeat=2))
    ans=0
    for x in product(el,repeat=t):
        if all(((a-1)*d-(c-1)*b)%n==0 for i,(a,b) in enumerate(x) for c,d in x[i+1:]):
            ans+=1
    return ans

def local_coeffs(n):
    F=[1]
    m=n
    for p in range(2,n+1):
        if m%p:continue
        e=0
        while m%p==0:
            m//=p;e+=1
        h=(e-1)//2
        c=(p+1)*sum(p**(e-1-2*v) for v in range(h+1))
        A=c+(e%2==0)
        # polynomial expansion in powers of exponentials, (coef, base)
        if F==[1]:F=[(1,1)]
        F=[(u*v,x*y) for u,x in F for v,y in [(A,p**e),(1-A,p**(e-1))]]
    return F if F != [1] else [(1,1)]

def coeffs_clique(n):
    return [sum(c*comb(s,k) for c,s in local_coeffs(n) if s>=k) for k in range(n+1)]

def brute_cliques(n):
    el=list(product(range(n),repeat=2))
    # Count subsets via mask if up to 16 vertices.
    out=[0]*(n+1)
    for mask in range(1<<len(el)):
        inds=[j for j in range(len(el)) if (mask>>j)&1]
        if len(inds)>n:continue
        if all(((el[i][0]-1)*el[j][1]-(el[j][0]-1)*el[i][1])%n==0
               for k,i in enumerate(inds) for j in inds[k+1:]):
            out[len(inds)]+=1
    return out

def main():
    for n,t in [(2,2),(2,4),(3,2),(3,3),(3,4),(4,2),(4,3),(5,2),(6,2),(8,2),(9,2)]:
        direct=count_direct(n,t)
        expect=sum(c*s**t for c,s in local_coeffs(n))
        assert direct==expect,(n,t,direct,expect)
        print('tuple',n,t,direct)
    for n in [1,2,3,4]:
        exp=coeffs_clique(n)
        got=brute_cliques(n)
        assert exp==got,(n,exp,got)
        assert exp[n]==sum(c for c,s in local_coeffs(n) if s==n)
        print('cliques',n,got)
    # Directly verify the quandle endomorphism classification by all functions for n<=5
    for n in [2,3,4,5]:
        good=[]
        for f in product(range(n),repeat=n):
            if all(f[(2*y-x)%n]==(2*f[y]-f[x])%n for x in range(n) for y in range(n)):
                good.append(f)
        affine={tuple((a*x+b)%n for x in range(n)) for a,b in product(range(n),repeat=2)}
        assert set(good)==affine,(n,len(good),len(affine))
        print('quandle',n,len(good))
    print('ALL_CHECKS_PASSED')
if __name__=='__main__':main()
