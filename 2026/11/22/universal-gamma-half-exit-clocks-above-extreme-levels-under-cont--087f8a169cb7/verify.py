import math
from fractions import Fraction

def laplace_weights(c, n):
    q=[c**i for i in range(n)]
    a=[]
    for j in range(n):
        v=Fraction(1)
        for k in range(n):
            if k!=j:
                v/= 1-(q[k]/q[j])**2
        a.append(v)
    return q,a

checks=0
for c in [Fraction(1,2),Fraction(2,3),Fraction(3,4)]:
    for n in range(2,10):
        q,a=laplace_weights(c,n)
        assert sum(a)==1
        checks+=1
        for m in range(1,5):
            # Partial fraction consistency via coefficient of y^m in prod_j (1-q_j^2 y)^-1
            polynomial=[Fraction(1)]+[Fraction(0)]*m
            for qi in q:
                new=[Fraction(0)]*(m+1)
                for i in range(m+1):
                    for j in range(m-i+1):
                        new[i+j]+=polynomial[i]*qi**(2*j)
                polynomial=new
            assert sum(aj*qj**(2*m) for qj,aj in zip(q,a))==polynomial[m]
            checks+=1
        for u in [3.,5.,8.,12.]:
            direct=0.5*sum(float(aj)*math.exp(-u/float(qj)) for qj,aj in zip(q,a))
            assert direct>0
            main=0.5*float(a[0])*math.exp(-u)
            if u==12.: assert abs(direct-main)/main<0.15
            checks+=1

def integrate(f,a,b,steps=12000):
    step=(b-a)/steps
    return step/3*(f(a)+f(b)+4*sum(f(a+(2*j-1)*step) for j in range(1,steps//2+1))+2*sum(f(a+(2*j)*step) for j in range(1,steps//2)))
for r in [.25,1.,3.]:
    for sigma in [.5,2.]:
        lam=math.sqrt(2*r)/sigma
        for t in [.01,.2,1.,3.]:
            f=lambda z:lam*math.exp(-lam*z)*math.erf(z/(sigma*math.sqrt(2*t)))
            actual=integrate(f,0,40/lam,14000)
            theoretical=math.exp(r*t)*math.erfc(math.sqrt(r*t))
            assert abs(actual-theoretical)<1.e-6, (r,sigma,t,actual,theoretical)
            checks+=1
# Half-Gamma mean via survival integral (in units of r)
for r in [.25,1.,3.]:
    # Integrate via y = sqrt(r t), dt = 2y dy/r
    result=integrate(lambda y:(2*y/r)*math.erfc(y),0,8,3000)
    assert abs(result-1/(2*r))<1e-6
    checks+=1
print(f'{checks} deterministic exact-rational/numerical checks passed')
