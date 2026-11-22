"""Independent finite checks of Gaussian normal-cone chamber counts and collision sums."""
from itertools import permutations, product
from fractions import Fraction
from math import comb, factorial, sqrt, exp, pi
from collections import Counter


def vertices(b):
    n=len(b); s=[]; x=0
    for v in b:
        x+=v;s.append(x)
    out=set()
    for k in range(n+1):
        raw=(1,)*k+tuple(s[k:])
        out.update(permutations(raw))
    return sorted(out)


def expected_angles(n,first):
    angles={}
    for k in range(n+1):
        p=Fraction(1,2**n*factorial(n-k))
        if first==1 and k==0:
            continue
        if first==1 and k==1:
            p+=Fraction(1,2**n*factorial(n))
        angles[k]=p
    return angles


def brute(b):
    n=len(b)
    v=vertices(b)
    counts=Counter()
    seen_sig=0
    for mask in product((-1,1),repeat=n):
        for perm in permutations(range(n)):
            # Positive magnitudes are distinct and algebraically generic for these small cases.
            g=[mask[i] * (1.0 + 0.001*(perm[i]+1) + 0.00001*(perm[i]+1)**2) for i in range(n)]
            scores=[sum(gi*vi for gi,vi in zip(g,vec)) for vec in v]
            a=max(range(len(v)),key=scores.__getitem__)
            # Guard against ties with two different actual vertices.
            s=sorted(scores,reverse=True)
            assert s[0]-s[1]>1e-6, (b,mask,perm,s[0],s[1])
            counts[v[a]]+=1
            seen_sig+=1
    return v,counts,seen_sig


def analytical_collision(n,first):
    c=sum((Fraction(comb(n,j),factorial(j)) for j in range(n+1)), Fraction(0))/(4**n)
    if first==1:c+=Fraction(2*n,factorial(n)*4**n)
    return c


def test():
    cases=0
    for n in range(2,6):
        for b in ((2,)+(1,)*(n-1),(1,)+(1,)*(n-1),(4,)+(2,)*(n-1),(3,)+tuple(i+1 for i in range(1,n))):
            v,ct,t=brute(b)
            ang=expected_angles(n,b[0]); expected_sum=Fraction(0)
            for point in v:
                k=point.count(1)
                predicted=ang[k]
                got=Fraction(ct[point],t)
                assert got==predicted,(n,b,point,got,predicted)
                expected_sum+=got**2
            assert sum(ct.values())==t
            assert expected_sum==analytical_collision(n,b[0]),(n,b,expected_sum,analytical_collision(n,b[0]))
            cases+=1
        print('n',n,'passed four families, full sign/order chamber enumeration')
    for n in (10,25,50,100,400,1600):
        terms=[Fraction(comb(n,j),factorial(j)) for j in range(n+1)]
        z=sum(terms)
        mean=sum(j*terms[j] for j in range(n+1))/z
        var=sum((Fraction(j)-mean)**2*terms[j] for j in range(n+1))/z
        if n>=50:
            assert abs(float(mean)/sqrt(n)-1)<0.25
            assert abs(float(var)/sqrt(n)-0.5)<0.20
        if n>=400:
            import math
            logz=math.log(float(z)) if n<=400 else math.log(float(z))
            target=2*sqrt(n)-.5-.25*math.log(n)-math.log(2*sqrt(pi))
            assert abs(logz-target)<0.20,(n,logz,target)
        print('n',n,'mean j',float(mean),'variance j',float(var))
    print('PARKING_ANGLE_LAGUERRE_EXACT_PASS',cases)

if __name__=='__main__':test()
