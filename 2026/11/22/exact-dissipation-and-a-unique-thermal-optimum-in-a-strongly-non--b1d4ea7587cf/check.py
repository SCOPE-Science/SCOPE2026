"""Independent finite-ring generator and entropy-rate checks for an asymmetric Glauber ring."""
from itertools import product
from math import exp, log, tanh, isclose


def direct_ring(n, beta, J, K):
    states=list(product((-1,1),repeat=n)); part=sum(exp(beta*J*sum(s[i]*s[(i+1)%n] for i in range(n))) for s in states)
    pi={s:exp(beta*J*sum(s[i]*s[(i+1)%n] for i in range(n)))/part for s in states}
    ge=tanh(2*beta*J); go=tanh(2*beta*K)
    assert ge<1 and abs(go)<1
    flow_div={s:0.0 for s in states}; entropy=0.
    for s in states:
        for i in range(n):
            back=s[(i-1)%n]; ahead=s[(i+1)%n]
            w=.5*(1-s[i]*(ge*(back+ahead)+go*(back-ahead))/2)
            sf=s[:i]+(-s[i],)+s[i+1:]
            wr=.5*(1+ s[i]*(ge*(back+ahead)+go*(back-ahead))/2)
            forward=pi[s]*w; reverse=pi[sf]*wr
            flow_div[s]-=forward; flow_div[sf]+=forward
            entropy+=forward*log(forward/reverse)
    z=tanh(beta*J)
    predicted=beta*K*go*(1-z*z)*(1-z**(n-2))/(1+z**n)
    assert max(abs(x) for x in flow_div.values())<8e-14,(n, max(abs(x) for x in flow_div.values()))
    assert abs(entropy/n-predicted)<2e-9,(n,beta,J,K,entropy/n,predicted)
    def rate(s,i):
        a=s[(i-1)%n]; b=s[(i+1)%n]
        return .5*(1-s[i]*(ge*(a+b)+go*(a-b))/2)
    derivative=sum(v*s[0]*(-2*s[1]*rate(s,1)+2*s[-1]*rate(s,n-1)) for s,v in pi.items())
    assert abs(entropy/n-beta*K*derivative)<2e-9
    return entropy/n

def bisect_root(f, lo, hi):
    assert f(lo)>0>f(hi)
    for _ in range(90):
        mid=(lo+hi)/2
        if f(mid)>0:lo=mid
        else:hi=mid
    return (lo+hi)/2

def opt_root(p):
    # x=beta*J, p=2K/J
    return bisect_root(lambda x: 1/x+(2*p/__import__('math').sinh(2*p*x) if 2*p*x < 500 else 0.)-2*tanh(x),.01,4)

def run_checks():
    tests=0
    for n in range(3,9):
        for beta in (.08,.25,.6,1.2,2):
            for J,K in ((1,.2),(1,1),(1,3),(.35,1)):
                direct_ring(n,beta,J,K); tests+=1
    ps=(.02,.1,.5,1,2,5,20,100)
    roots=[opt_root(p) for p in ps]
    assert all(roots[i]>roots[i+1] for i in range(len(roots)-1))
    slow=bisect_root(lambda x:1-x*tanh(x),.1,2)
    fast=bisect_root(lambda x:1-2*x*tanh(x),.1,2)
    assert all(fast-1e-12<x<slow for x in roots)
    assert abs(opt_root(.00001)-slow)<.0001
    assert abs(opt_root(1000)-fast)<1e-9
    for p,x in zip(ps,roots):
        f=lambda y:y*tanh(p*y)/( __import__('math').cosh(y)**2)
        for d in (-.1,-.001,.001,.1):
            if x+d>0: assert f(x)>f(x+d)
            tests+=1
    print('PASS',tests,'independent tests; optimum x for p=2',opt_root(2),'bounds',fast,slow)

if __name__=='__main__':run_checks()
