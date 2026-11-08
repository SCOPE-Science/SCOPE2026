"""Exact finite-field check of the genus-four degree-four obstruction.

K=F_3[u]/(u^4+u-1). Integer coefficients are base-3 digits.
Also checks the integer inequalities used for the universal upper bound.
"""

def mul(a,b):
    aa=[(a//(3**i))%3 for i in range(4)]
    bb=[(b//(3**i))%3 for i in range(4)]
    c=[0]*7
    for i in range(4):
        for j in range(4):
            c[i+j]=(c[i+j]+aa[i]*bb[j])%3
    for i in range(6,3,-1):
        v=c[i];c[i]=0
        c[i-4]=(c[i-4]+v)%3
        c[i-3]=(c[i-3]-v)%3
    return sum(c[i]*3**i for i in range(4))

def powK(a,n):
    z=1
    while n:
        if n&1:z=mul(z,a)
        a=mul(a,a);n//=2
    return z

def negate(a):
    return sum((-(a//(3**i))%3)*3**i for i in range(4))

# Irreducibility follows from containing no roots in F3 or F9:
# gcd(u^4+u-1,u^(3^d)-u)=1, d=1,2. The finite-field
# multiplication table allows checking these identities directly.
assert all(powK(a,81)==a for a in range(81))
assert all(len({mul(a,b) for b in range(81)})==81 for a in range(1,81))
F9=[a for a in range(81) if powK(a,9)==a]
assert len(F9)==9
assert all(powK(a,9)==a for a in F9)
for a in range(81):
    v=negate(a)  # not directly used in the count
    f=(powK(a,9))
    f=sum(((f//(3**i)%3 - a//(3**i)%3)%3)*3**i for i in range(4))
    assert f==0 if a in F9 else f!=0
    if a not in F9:
        assert powK(f,9)==negate(f)
        assert powK(f,8)==2
        assert powK(f,40)==2

# All x in F9 give exactly one y=0, and all remaining x in F81
# yield a nonsquare f(x) and hence no y. The odd-degree model
# has one rational point at infinity in both extensions.
N2=1+len(F9)
N4=1+len(F9)
assert N2==N4==10
assert (N4-N2)//4==0
# For r>=5, (3^(r/4)-1)^2 >= 8, by monotonicity and
# 3^(5/4) > 39/10 > 1+sqrt(8) (verified using integers).
assert 39**4 < 3**5 * 10**4
assert 29**2 > 8*100
print('RHO_3_4_EXACT_WITNESS_AND_BOUND_PASS',N2,N4)
