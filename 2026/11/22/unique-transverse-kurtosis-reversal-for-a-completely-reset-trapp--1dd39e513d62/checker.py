"""Independent exact-rational moment-hierarchy diagnostic for a completely reset planar active particle."""
from fractions import Fraction as F

def moments(d,r):
    d,r=F(d),F(r)
    a={(0,k):r/(r+d*k*k) for k in range(-4,5)}
    for n in range(1,5):
        for k in range(-4+n,5-n):
            a[n,k]=-F(n,2)*(a[n-1,k+1]-a[n-1,k-1])/(n+d*k*k+r)
    return -a[2,0],a[4,0]

def formulas(d,r):
    d,r=F(d),F(r)
    m2=4*d/((4*d+r)*(r+2)*(d+r+1))
    m4=96*d*d*(144*d*d+79*d*r+124*d+10*r*r+25*r+12)/((4*d+r)*(16*d+r)*(r+2)*(r+4)*(d+r+1)*(d+r+3)*(4*d+r+2)*(9*d+r+1))
    return m2,m4

def polynomial(d,r):
    d,r=F(d),F(r)
    return (576*d**4*r+1252*d**3*r**2+928*d**3*r-4032*d**3+885*d**2*r**3+2430*d**2*r**2+104*d**2*r-2176*d**2+228*d*r**4+972*d*r**3+1156*d*r**2+160*d*r-192*d+19*r**5+100*r**4+179*r**3+122*r**2+24*r)

def denom(d,r):
    d,r=F(d),F(r)
    return (4*d+r)**2*(16*d+r)*(r+2)**2*(r+4)*(d+r+1)**2*(d+r+3)*(4*d+r+2)*(9*d+r+1)

if __name__=='__main__':
    tests=0
    for d in [F(1,100),F(1,5),F(1),F(3,2),F(9),F(50)]:
        for r in [F(1,1000),F(1,7),F(1),F(4),F(27)]:
            m2,m4=moments(d,r)
            assert (m2,m4)==formulas(d,r)
            assert m4-3*m2*m2==48*d*d*polynomial(d,r)/denom(d,r)
            assert m2>0 and m4>0
            tests+=3
    for d in [F(1,100),F(1),F(10),F(100)]:
        coeff=[19,100+228*d,179+972*d+885*d*d,122+1156*d+2430*d*d+1252*d**3,24+160*d+104*d*d+928*d**3+576*d**4]
        constant=-192*d-2176*d*d-4032*d**3
        assert all(x>0 for x in coeff) and constant<0
        tests+=1
    print(f"PASS {tests} exact checks: Fourier recursion, moment formulas, cumulant polynomial, unique positive Descartes crossing")
