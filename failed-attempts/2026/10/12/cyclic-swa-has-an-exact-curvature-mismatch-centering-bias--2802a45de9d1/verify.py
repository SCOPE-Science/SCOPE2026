import random

def formulas(a,b,u,v,eta):
    D=a+b-a*b*eta
    p=(a*(1-eta*b)*u+b*v)/D
    q=(a*u+b*(1-eta*a)*v)/D
    xs=(a*u+b*v)/(a+b)
    swa=(p+q)/2
    bias=a*b*eta*(a-b)*(u-v)/(2*(a+b)*D)
    gap=a*a*b*b*eta*eta*(a-b)**2*(u-v)**2/(16*(a+b)*D*D)
    repair=(a*p+b*q)/(a+b)
    return p,q,xs,swa,bias,gap,repair

random.seed(350082)
for _ in range(2000):
    a=10**random.uniform(-1,1); b=10**random.uniform(-1,1)
    u=random.uniform(-3,3); v=random.uniform(-3,3)
    for _j in range(1000):
        eta=10**random.uniform(-3,0.2)/max(a,b)
        R=(1-eta*a)*(1-eta*b)
        if abs(R)<0.75: break
    p,q,xs,swa,bias,gap,repair=formulas(a,b,u,v,eta)
    assert a+b-a*b*eta>0
    assert abs((swa-xs)-bias)<2e-11*max(1,abs(swa),abs(xs))
    F=lambda x: 0.25*(a*(x-u)**2+b*(x-v)**2)
    assert abs((F(swa)-F(xs))-gap)<2e-11*max(1,abs(gap))
    assert abs(repair-xs)<2e-11*max(1,abs(xs))
    x=random.uniform(-5,5)
    for _k in range(180):
        qs=(1-eta*a)*x+eta*a*u
        ps=(1-eta*b)*qs+eta*b*v
        x=ps
    assert abs(ps-p)<2e-10*max(1,abs(p))
    assert abs(qs-q)<2e-10*max(1,abs(q))

for a in (0.2,1.0,5.0):
    for eta in (0.01/a,0.3/a,1.2/a,1.8/a):
        R=(1-eta*a)**2
        if abs(R)<1:
            p,q,xs,swa,bias,gap,repair=formulas(a,a,-1.7,2.3,eta)
            assert abs(swa-xs)<1e-12 and abs(bias)<1e-12 and abs(gap)<1e-12
            assert abs(repair-xs)<1e-12
print("verification passed")
