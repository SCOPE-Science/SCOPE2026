"""Exact Cartier coefficients and normalized Prym determinants in p=11 and p=13.
Requires Python 3 only.
"""

def polynomial_power(p, exponent):
    # Polynomial in x with coefficients in F_p[a,b], encoded by (power_x,power_a,power_b).
    poly={(0,0,0):1}
    for _ in range(exponent):
        z={}
        for (ix,ia,ib),c in poly.items():
            for key in ((ix+4,ia,ib),(ix+2,ia+1,ib),(ix,ia,ib+1)):
                z[key]=(z.get(key,0)+c)%p
        poly={k:v for k,v in z.items() if v}
    return poly

def coeff(poly, x):
    return {(ia,ib): c for (ix,ia,ib),c in poly.items() if ix==x}

for p in (11,13):
    C={}
    for j,i,name in ((2,0,'eta0'),(2,1,'eta1'),(1,0,'theta')):
        jj=next(t for t in (1,2) if (p*t-j)%3==0)
        F=polynomial_power(p,(p*jj-j)//3)
        for m,target in ((0,'eta0' if jj==2 else 'theta'),(1,'eta1' if jj==2 else 'missing')):
            if jj==1 and m==1: continue
            C[(target,name)] = coeff(F,p-1+p*m-i)
    if p==11:
        assert C[('theta','eta0')]=={(1,0):3}
        assert C[('theta','eta1')]=={}
        # -a*b^2*(a^2-4b)^2
        assert C[('eta0','theta')]=={(5,2):10,(3,3):8,(1,4):6}
        assert C[('eta1','theta')]=={}
    else:
        # 2*b^2*(a^2-4b)^2*(a^2+5b)
        assert C[('eta0','eta0')]=={(6,2):2,(4,3):7,(2,4):4,(0,5):4}
        assert C[('eta1','eta0')]=={}
        assert C[('eta0','eta1')]=={}
        assert C[('eta1','eta1')]=={(4,0):5,(2,1):12,(0,2):2}
        assert C[('theta','theta')]=={(2,0):6,(0,1):4}
    print('PICARD_CARTIER_COEFFICIENTS_PASS',p)

# The dimensionless Prym determinant in coordinates t=a^2/b, j=1-t/4.
for p in (11,13):
    for t in range(p):
        if t==4:continue # singular quartic (j=0)
        j=(1-t*pow(4,-1,p))%p
        if p==11:
            det=(3*t*(t-4)**2)%p
            assert det == (5*j*j*(1-j))%p
        else:
            det=(12*(t-4)**2*(t+5)**2)%p
            assert det == (4*j*j*(j+1)**2)%p
print('PICARD_PRYM_HASSE_DIVISORS_PASS')
