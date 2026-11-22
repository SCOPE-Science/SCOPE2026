"""Independent exact-arithmetic checks for a seven-site three-orientation update.

Run: python3 verify.py.  No external packages required.
"""
from fractions import Fraction as F
from itertools import product
from math import comb, factorial

A = [F(1), F(2,3), F(4,3), F(4,3), F(40,27), F(140,81), F(1330,729)]
T = [F(0), F(1,3), F(0), F(2,9), F(2,27), F(10,81), F(80,729)]


def majority_and_tie_derivatives(m):
    a = F(0); t = F(0)
    for n1 in range(m+1):
        for n2 in range(m-n1+1):
            n3 = m-n1-n2
            p = F(factorial(m),factorial(n1)*factorial(n2)*factorial(n3)*3**m)
            score = 3*(n1-n2)
            if n1 > max(n2,n3):
                a += p*score
            if max(n1,n2,n3) in (n1,n2,n3) and sum(z==max(n1,n2,n3) for z in (n1,n2,n3))>1:
                t += p*score*F(n1,m)
    return a,t

for m in range(1,8):
    assert majority_and_tie_derivatives(m) == (A[m-1], T[m-1]), (m, majority_and_tie_derivatives(m))


def pt(rho):
    p=sum(F(comb(6,k))*rho**k*(1-rho)**(6-k)*A[k] for k in range(7))
    t=sum(F(comb(6,k))*rho**k*(1-rho)**(6-k)*T[k] for k in range(7))
    return p,t


def poly_eval(coeff,x):
    return sum(F(v)*x**i for i,v in enumerate(coeff))

pcoeff = [729,-1458,10935,-24300,27135,-14634,2923]
tcoeff = [0,1458,-7290,17820,-23490,15930,-4348]


def exhaustive_derivative(rho, eta, incumbent):
    # Center definitely occupied; six neighbors independent empty/color.
    # At f=(1/3,1/3,1/3), the delta directional logarithmic score is
    # 3*(N_1-N_2), valid for both center and occupied neighbors.
    base_c=F(1,3)
    weights=(1-rho,rho/3,rho/3,rho/3)
    total=F(0)
    for center in (1,2,3):
        for neighbors in product(range(4), repeat=6):
            counts=[0,0,0,0]
            counts[center]+=1
            prob=base_c
            for z in neighbors:
                prob *= weights[z]
                if z: counts[z]+=1
            mx=max(counts[1:]); winners=[j for j in (1,2,3) if counts[j]==mx]
            if len(winners)==1:
                p1 = 1-eta if winners[0]==1 else eta/2
            elif incumbent:
                p1 = 1-F(2,3)*eta if center==1 else eta/3
            else:
                p1 = F(1,3)
            total += prob * 3*(counts[1]-counts[2]) * p1
    return total

for rho in (F(1,10), F(1,5), F(1,2), F(3,4), F(1)):
    p,t=pt(rho)
    assert p == poly_eval([F(z,729) for z in pcoeff],rho)
    assert t == poly_eval([F(z,729) for z in tcoeff],rho)
    for eta in (F(0),F(1,7),F(2,5)):
        expected_random=(1-F(3,2)*eta)*p
        expected_incumbent=(1-F(3,2)*eta)*p+(1-eta)*t
        assert exhaustive_derivative(rho,eta,False)==expected_random,(rho,eta,expected_random)
        assert exhaustive_derivative(rho,eta,True)==expected_incumbent,(rho,eta,expected_incumbent)

# Sharp positive threshold for randomized ties; after t=rho/(1-rho),
# transformed quintic has one negative coefficient and all subsequent positive.
# It is strictly increasing for t>=0 and crosses zero exactly once.
G=[-1458,10935,-24300,27135,-14634,2923]
transformed=[-1458,3645,4860,5265,3186,601]
for t in (F(0),F(1,50),F(1,4),F(1),F(7,3),F(100)):
    assert poly_eval(G,t/(1+t))*(1+t)**5 == poly_eval(transformed,t)
assert poly_eval(G,F(1,5))<0 and poly_eval(G,F(1,4))>0

# For the incumbent-tie convention, A-1 = rho^2 H(rho)/243
# and H(rho) >= 255 - 43 = 212 for rho in [0,1].
H=[1215,-2160,1215,432,-475]
for rho in (F(0),F(1,20),F(1,2),F(3,4),F(1)):
    p,t=pt(rho)
    assert p+t-1 == rho*rho*poly_eval(H,rho)/243
assert pt(F(1))[0]==F(1330,729)
assert pt(F(1))[1]==F(80,729)
assert (pt(F(1))[0]+pt(F(1))[1]-1)/(F(3,2)*pt(F(1))[0]+pt(F(1))[1])==F(681,2075)
assert F(2,3)*(1-1/pt(F(1))[0])==F(601,1995)
print('PASS: 7 exact voter-count derivatives; 30 independent 12,288-configuration event enumerations; polynomial identities; unique positive dilution threshold; incumbent-tie positivity and endpoints.')
