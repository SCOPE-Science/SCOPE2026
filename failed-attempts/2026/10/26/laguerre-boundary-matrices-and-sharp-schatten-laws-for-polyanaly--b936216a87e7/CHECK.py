from fractions import Fraction as F
from decimal import Decimal, localcontext
from math import factorial

def bmoment(k,m):
    den=1
    for j in range(m):den*=k+2+j
    return F(factorial(m),den)

def scaled_eigs(k,s):
    g01=bmoment(k,1);g11=bmoment(k,2)
    a=bmoment(k,s);b=bmoment(k,s+1);c=bmoment(k,s+2)
    G=g11-g01*g01
    S=a*g11+c-2*b*g01
    D=a*c-b*b
    with localcontext() as ctx:
        ctx.prec=80
        cv=lambda r: Decimal(r.numerator)/Decimal(r.denominator)
        disc=cv(S*S-4*G*D).sqrt()
        eplus=(cv(S)+disc)/(2*cv(G))
        eminus=(cv(S)-disc)/(2*cv(G))
        return (eminus*k**s,eplus*k**s)

with localcontext() as ctx:
 ctx.prec=80
 for s in [1,2]:
    targets=([Decimal(2)-Decimal(2).sqrt(),Decimal(2)+Decimal(2).sqrt()] if s==1 else [Decimal(8)-2*Decimal(13).sqrt(),Decimal(8)+2*Decimal(13).sqrt()])
    for k in [50,100,1000,10000]:
      vals=scaled_eigs(k,s)
      print('sigma',s,'k',k,'scaled',(float(vals[0]),float(vals[1])),'limits',tuple(float(v) for v in targets))
      assert all(abs(vals[i]-targets[i])<Decimal(300)/k for i in range(2))
 print('n2 sigma2 constant=',float(Decimal(16)+4*Decimal(3).sqrt()))
 print('all checks passed')
