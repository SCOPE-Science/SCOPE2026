"""Independent finite checks of sharp 3-tap weighted log-sum-exp variation law.
Uses Python standard library only. Finite checks corroborate, not replace, proof.
"""
import math, random

def op(z, weights, temperature=1.0):
    a,b,c=weights
    out=[]
    for i in range(len(z)-2):
        row=[math.log(a)+z[i]/temperature,math.log(b)+z[i+1]/temperature,math.log(c)+z[i+2]/temperature]
        m=max(row)
        out.append(temperature*(m+math.log(sum(math.exp(v-m) for v in row))))
    return out

def jac(z,weights,temperature=1.0):
    a,b,c=weights
    mat=[]
    for i in range(len(z)-2):
        row=[math.log(a)+z[i]/temperature,math.log(b)+z[i+1]/temperature,math.log(c)+z[i+2]/temperature]
        m=max(row);v=[math.exp(y-m) for y in row];d=sum(v)
        full=[0.0]*len(z)
        for j in range(3): full[i+j]=v[j]/d
        mat.append(full)
    return mat

def tv(z): return sum(abs(z[i+1]-z[i]) for i in range(len(z)-1))

def norm_j(z,weights):
    P=jac(z,weights);vmax=0
    for k in range(1,len(z)):
        H=[sum(r[k:]) for r in P]
        vmax=max(vmax,tv(H))
    return vmax

def target(a,b,c): return 1+2*max(0.,(math.sqrt(a*c)-b)/(math.sqrt(a*c)+b))

random.seed(20261118)
checks=0
for n in range(6,13):
    for j in range(700):
        w=[math.exp(random.uniform(-3,3)) for _ in range(3)]
        z=[random.uniform(-7,7) for _ in range(n)]
        y=[v+random.uniform(-3,3) for v in z]
        K=target(*w)
        assert norm_j(z,w)<=K+2e-12
        outz=op(z,w);outy=op(y,w)
        assert tv([a-b for a,b in zip(outz,outy)])<=K*tv([a-b for a,b in zip(z,y)])+2e-10
        checks+=2
print('FINITE_JACOBIAN_AND_TWO_INPUT_CHECKS_PASS',checks)

for n in [6,7,11,22]:
    for w in [(1.,.5,1.),(4.,1.,9.),(9.,2.,1.),(1.,2.,1.),(1.,1.,1.),(1.,3.,16.)]:
        a,b,c=w;K=target(*w)
        X=math.sqrt(c);Y=math.sqrt(a)
        z=[0.]*n;z[1]=-55;z[2]=math.log(X);z[3]=math.log(Y);z[4]=-55
        NJ=norm_j(z,w)
        assert abs(NJ-K)<1e-9, (n,w,NJ,K)
        # The sharp nonlinear secant is approached along an infinitesimal step.
        h=[0,0,0]+[1]*(n-3)
        eps=1e-4
        oz=op(z,w);oy=op([zz+eps*hh for zz,hh in zip(z,h)],w)
        ratio=tv([yy-xx for xx,yy in zip(oz,oy)])/(eps*tv(h))
        assert abs(ratio-K)<1e-4,(w,ratio,K)
print('SHARPNESS_AND_TEMPERATURE_TESTS_PASS',4*6*2)
for w in [(1.,3.,1.),(1.,1.,1.),(2.,2.,2.),(1.,2.,4.)]:
    for n in [6,8,13]:
        z=[random.uniform(-2,2) for _ in range(n)]
        h=[0.,0.,0.]+[1.]* (n-3)
        u=op(z,w);v=op([a+z for a,z in zip(z,h)],w)
        assert abs(tv([x-y for x,y in zip(v,u)])-tv(h))<1e-10
print('FINITE_NONEXPANSIVE_EQUALITY_CHECKS_PASS',12)
print('ALL_WEIGHTED_LOGSUMEXP_VARIATION_CHECKS_PASS')
