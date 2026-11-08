"""Independent floating-point state recursion and large-size scaling checks.
The integer-indexed recursion starts with both marked vertices free.
"""
import math

def p_rec(a,b,lam):
    p=1.0;tot=0.0
    for k in range(min(b,a-2)+1):
        i=a-k;j=b-k
        den=i*j+lam
        tot+=p*lam/den
        p*=((i-2)*j)/den
    return tot

def I(rho):
    if rho==1:return 1.
    return 1-(rho-1)*math.log(rho/(rho-1))

for rho in [.4,.7,1.,1.5,2.5]:
    print('rho=',rho)
    for n in [300,1000,3000]:
        b=round(n*rho)
        p=p_rec(n,b,2.)
        target=(1-rho)**2 if rho<1 else (2*I(rho)/n)
        print(n,'P',p,'target',target,'ratio',p/target)
for c in [-3.,-1.,0,1.,3.]:
    print('c=',c)
    for n in [1000,4000,16000]:
        b=n-round(c*math.sqrt(n))
        p=p_rec(n,b,2.)
        print(n,'nP',n*p,'prediction',2+max(c,0)**2)
