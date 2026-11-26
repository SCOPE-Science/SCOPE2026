"""Exact integer checks for the infinity-boundary formulas of uv^p+v=f(u).

This checks the Newton supports and algebraic identities, not the
geometric branch theorem or the infinitude of the parameter family.
"""
from math import gcd


def analyze(p,n):
    d=(p**(2*n)-1)//(2*(p-1))
    exponents=[(p**(2*i)-1)//(2*(p-1)) for i in range(1,n+1)]
    assert exponents[-1]==d and exponents==sorted(set(exponents))
    assert d>p+1 and gcd(p,d-1)==1
    a=d-p-1
    b=d-1
    assert gcd(a,b)==1 and a>1 and b>a
    # Newton initial edges: a^d--a*b^a and a*b^a--b^(d-1)
    # We denote local coordinates by A,B and exponent a by alpha.
    Pedge=lambda i,j: a*i+b*j
    Qedge=lambda i,j: p*i+j
    assert Pedge(d,0)==Pedge(1,a)==a*d
    assert Qedge(1,a)==Qedge(0,d-1)==d-1
    # Other support points of the homogenized polynomial lie strictly above both edges.
    others=[(0,d)] + [(e,d-e) for e in exponents[:-1]]
    for i,j in others:
        assert Pedge(i,j)>a*d
        assert Qedge(i,j)>d-1
    assert Pedge(0,d-1)>a*d
    assert Qedge(d,0)>d-1
    # Local cusp, intersection, conductor, global genus, adjunction.
    delta_P=(a-1)*(b-1)//2
    intersection=a
    delta=delta_P+intersection
    c_P=2*delta_P+intersection
    c_Q=intersection
    genus=(d-1)*(d-2)//2-delta
    assert 2*delta==c_P+c_Q
    assert genus==(p-1)*d//2==(p**(2*n)-1)//4
    K_P=(d-3)*b-c_P
    K_Q=(d-3)-c_Q
    assert K_P==(p-1)*d-p and K_Q==p-2
    assert K_P+K_Q==2*genus-2
    return d,a,b,delta_P,delta,c_P,c_Q,genus,K_P,K_Q

for p in [3,5,7,11,13,17,19]:
    for n in range(2,7):
        z=analyze(p,n)
        if n==2 and p in [3,5,7]:
            print('p,n,d,alpha,beta,delta,cP,cQ,g,K_P,K_Q:',p,n,z)
assert analyze(3,2)==(20,16,19,135,151,286,16,20,37,1)
assert analyze(5,2)==(78,72,77,2698,2770,5468,72,156,307,3)
print('VERIFY_OK: Newton supports and conductor/genus/adjunction formulas checked')
