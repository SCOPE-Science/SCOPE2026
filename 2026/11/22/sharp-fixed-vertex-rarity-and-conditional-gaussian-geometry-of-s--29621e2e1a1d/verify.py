"""Independent exact counting and finite action checks for hypercube-fixing involutions."""
from math import factorial, comb, log, sqrt, exp
from itertools import permutations, product

def A(n,t):
    a,b=1,t
    if n==0:return a
    if n==1:return b
    for j in range(2,n+1):
        a,b=b,t*b+2*(j-1)*a
    return b

def coefficients(n):
    return {n-k: factorial(n)//(factorial(k)*factorial(n-2*k)) for k in range(n//2+1)}

def exhaustive(n):
    B=D=BF=DF=0
    profile={}
    for p in permutations(range(n)):
        if any(p[p[i]]!=i for i in range(n)):continue
        for bits in product((0,1), repeat=n):
            if any(bits[p[i]]!=bits[i] for i in range(n)):continue
            B+=1
            even=sum(bits)%2==0
            D+=int(even)
            fixed=0
            for x in product((0,1),repeat=n):
                if all(x[p[i]]^bits[i]==x[i] for i in range(n)):fixed+=1
            if fixed:
                BF+=1
                DF+=int(even)
                assert even
                profile[fixed]=profile.get(fixed,0)+1
    assert B==A(n,2),(n,B,A(n,2))
    assert D==(A(n,2)+A(n,0))//2,(n,D)
    assert BF==DF==A(n,1),(n,BF,DF,A(n,1))
    assert profile=={2**e:c for e,c in coefficients(n).items()},(n,profile,coefficients(n))
    return B,D,BF,profile

if __name__=='__main__':
    for n in range(1,7):
        B,D,F,prof=exhaustive(n)
        print('dimension',n,'B',B,'D',D,'fix',F,'spectrum',prof)
    for n in (20,50,100,200,500,1000):
        a0,a1,a2=A(n,0),A(n,1),A(n,2)
        logratio=log(a1)-log(a2)
        res=logratio+sqrt(n/2)
        print('asymptotic',n,'logratio+root',round(res,8),'target',0.375,'D/B_ratio',round(2*a2/(a2+a0),8))
    print('HYPERCUBE_FIXED_INVOLUTIONS_CHECKS_PASSED')
