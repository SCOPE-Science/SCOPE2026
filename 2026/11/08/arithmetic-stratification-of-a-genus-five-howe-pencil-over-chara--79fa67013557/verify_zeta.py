"""Exact zeta numerators of a five-member genus-five Howe family over F7.
Only Python standard library is required. Run: python verify_zeta.py
Independent irreducible binomials are used for every nonprime extension field.
"""
from itertools import product
P = 7
PARAMETERS = (2,3,4,5,6)
EXPECTED_C = {2:(8,88,344),3:(4,88,364),4:(8,88,344),5:(12,88,324),6:(8,120,344)}
EXPECTED_H = {2:(8,60,344),3:(4,60,364),4:(8,60,344),5:(12,60,324),6:(8,92,344)}

def finite_field(n,c):
    # F_7[t]/(t^n-c), with x^2-c irreducible for c in {5,6}
    # and x^3-c irreducible for c in {2,3}.
    zero=(0,)*n;one=(1,)+(0,)*(n-1)
    def mul(x,y):
        out=[0]*(2*n-1)
        for i in range(n):
            for j in range(n):out[i+j]+=x[i]*y[j]
        for d in range(2*n-2,n-1,-1):out[d-n]+=c*out[d]
        return tuple(v%P for v in out[:n])
    def power(x,e):
        y=one
        while e:
            if e&1:y=mul(y,x)
            x=mul(x,x);e>>=1
        return y
    def character(x):
        if x==zero:return 0
        return 1 if power(x,(P**n-1)//2)==one else -1
    return list(product(range(P),repeat=n)),mul,power,character

def count(n,c,a):
    elements,mul,power,chi=finite_field(n,c)
    # Both quartic covers have leading coefficient 1; there are four
    # points at infinity on their normalized fiber product, two on H.
    count_C=4;count_H=2
    for x in elements:
        xx=power(x,4)
        u=((xx[0]-1)%P,)+xx[1:]
        v=((xx[0]-a)%P,)+xx[1:]
        count_C+=(1+chi(u))*(1+chi(v))
        count_H+=1+chi(mul(u,v))
    return count_C,count_H

def multiply(A,B):
    C=[0]*(len(A)+len(B)-1)
    for i,a in enumerate(A):
        for j,b in enumerate(B):C[i+j]+=a*b
    return C

def expected_LH(a):
    E0=[1,0,7];Eplus=[1,-4,7];Eminus=[1,4,7]
    A=[1,0,6,0,49]
    factors={2:[E0,Eplus,Eminus],3:[Eplus,A],4:[E0,Eplus,Eminus],5:[Eminus,A],6:[E0,E0,E0]}[a]
    res=[1]
    for f in factors:res=multiply(res,f)
    return res

for n,choices in ((1,(1,)),(2,(5,6)),(3,(2,3))):
    for c in choices:
        for a in PARAMETERS:
            NC,NH=count(n,c,a)
            assert NC==EXPECTED_C[a][n-1],(n,c,a,'C',NC)
            assert NH==EXPECTED_H[a][n-1],(n,c,a,'H',NH)
            assert NC-NH==(28 if n==2 else 0),(n,c,a,'quotient isogeny')

for a in PARAMETERS:
    N=EXPECTED_H[a]
    s=[7**i+1-N[i-1] for i in (1,2,3)]
    e1=-s[0]
    e2=(s[0]**2-s[1])//2
    e3=(-s[0]**3+3*s[0]*s[1]-2*s[2])//6
    L=[1,e1,e2,e3,7*e2,49*e1,343]
    assert L==expected_LH(a),(a,L,expected_LH(a))
    LC=multiply([1,0,14,0,49],L)
    assert len(LC)==11 and LC[-1]==7**5
    if a==6:assert LC==[1,0,35,0,490,0,3430,0,12005,0,16807]
    print('a=',a,'N_C=',EXPECTED_C[a],'L_C=',LC)
print('ZETA_EXACT_OK')
