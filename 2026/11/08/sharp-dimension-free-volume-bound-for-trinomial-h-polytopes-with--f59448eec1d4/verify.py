"""Exact arithmetic finite obstruction for the two upper-height elements.
This is a standalone verifier using only Python's standard library.
It checks candidate rank-two groups, exact character obstructions,
automorphism orbits, and exact dual witnesses.
"""
from fractions import Fraction as F
from functools import lru_cache
from math import gcd, lcm

ORDERS = {2, 3, 4, 5, 6, 8, 10, 12}
PI_UP = F(22, 7)

@lru_cache(None)
def cos_lower(z):
    z = z % 1
    z = min(z, 1-z)
    if z == F(1,2):
        return F(-1)
    x = 2*PI_UP*z
    # Last term is negative; all subsequent terms form an alternating
    # decreasing series. Therefore this sum is <= cos(2*pi*z).
    term = F(1); val = term
    for j in range(1,20):
        term = -term*x*x/((2*j-1)*(2*j))
        val += term
    return val

def elements(m,n):
    return [(a,b) for a in range(m) for b in range(n)]

def order(g,m,n):
    a,b = g
    return lcm(m//gcd(m,a), n//gcd(n,b))

def excluded_by_character(m,n,x,y):
    for u,v in elements(m,n)[1:]:
        z1 = F(u*x[0],m)+F(v*x[1],n)
        z2 = F(u*y[0],m)+F(v*y[1],n)
        if cos_lower(z1)+cos_lower(z2)>1:
            return True
    return False

# Exact dual vectors: for the representative high elements X,Y,
# y(g)=1_{g!=0}+1_X(g)+1_Y(g),
# v\cdot y=-1, while v\cdot fractional_character >=0 for every character.
CERTS = {
 (2,8):(
  ((0,1),(1,2)),
  {(0,1):F(-1),(0,3):F(1),(0,5):F(1,2),(1,1):F(1,2),(1,2):F(-1,2)}),
 (4,4):(
  ((0,1),(1,0)),
  {(0,1):F(-3,4),(0,3):F(1,4),(1,0):F(-3,4),(1,2):F(1,4),
   (2,1):F(1,4),(2,2):F(-1,2),(2,3):F(1,4),(3,0):F(1,4),
   (3,2):F(1,4),(3,3):F(1)}),
 (3,6):(
  ((0,1),(1,1)),
  {(0,1):F(-2,3),(0,2):F(1,3),(0,3):F(-1),(1,0):F(-1,3),
   (1,1):F(-2,3),(1,3):F(2,3),(1,5):F(2,3),(2,0):F(-1,3),
   (2,1):F(1,3),(2,2):F(1,3),(2,3):F(2,3),(2,4):F(1,3)})
}

def check_dual(m,n,rep,d):
    X,Y = rep
    assert sum(v*(2 if g in rep else 1) for g,v in d.items()) == -1
    for u,v in elements(m,n):
        col = sum(c*((F(u*g[0],m)+F(v*g[1],n))%1) for g,c in d.items())
        assert col>=0, ((m,n),(u,v),col)

def automorphism_orbit(m,n,rep):
    E=elements(m,n)
    orb=set()
    count=0
    for a in E:
        if m*a[0]%m or m*a[1]%n:continue
        for b in E:
            if n*b[0]%m or n*b[1]%n:continue
            images=[((i*a[0]+j*b[0])%m,(i*a[1]+j*b[1])%n) for i,j in E]
            if len(set(images))!=m*n:continue
            image=dict(zip(E,images))
            count+=1
            orb.add(tuple(sorted((image[rep[0]],image[rep[1]]))))
    return orb,count

def main():
    orbits={}
    for (m,n),(rep,d) in CERTS.items():
        check_dual(m,n,rep,d)
        orbits[(m,n)], count=automorphism_orbit(m,n,rep)
        print('certified excluded group',m,n,'automorphisms',count,'orbit size',len(orbits[(m,n)]))
    tested=0; spectral_exclusions=0; dual_exclusions=0
    for n in range(2,145):
        for m in range(1,n+1):
            if n%m or m*n<=12 or m*n>144:
                continue
            E=elements(m,n)
            eligible=[p for p in E[1:] if order(p,m,n) in ORDERS]
            for i,x in enumerate(eligible):
                for y in eligible[i+1:]:
                    tested+=1
                    if excluded_by_character(m,n,x,y):
                        spectral_exclusions+=1
                    else:
                        assert (m,n) in orbits, (m,n,x,y)
                        assert tuple(sorted((x,y))) in orbits[(m,n)], (m,n,x,y)
                        dual_exclusions+=1
    assert dual_exclusions==88, dual_exclusions
    print('EXACT_VERIFICATION_PASS; candidate_pairs_above_12=',tested,
          'spectral_exclusions=',spectral_exclusions,'dual_exclusions=',dual_exclusions)

if __name__=='__main__':main()
