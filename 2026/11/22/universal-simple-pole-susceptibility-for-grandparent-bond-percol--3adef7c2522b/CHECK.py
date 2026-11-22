"""Finite, reproducible checks for the grandparent-bond susceptibility identity.

Uses only the Python standard library. The infinite theorem is proved analytically
and not inferred from these finite checks.
"""
import math
from fractions import Fraction
from itertools import product

CHECKS = 0

def check(condition, msg):
    global CHECKS
    if not condition:
        raise AssertionError(msg)
    CHECKS += 1


def moments(prob, p):
    """Return U, V, V', f for finite-support offspring probabilities."""
    assert abs(sum(prob.values())-1)<1e-12
    m=sum(k*weight for k, weight in prob.items())
    assert m>1 and 0<p<1/(m*m)
    def phi(t):
        return sum(weight*t**k for k,weight in prob.items())
    def dphi(t):
        return sum(k*weight*t**(k-1) for k,weight in prob.items() if k>=1)
    def ddphi(t):
        return sum(k*(k-1)*weight*t**(k-2) for k,weight in prob.items() if k>=2)
    low,high=0.0,1.0
    for _ in range(85):
        mid=(low+high)/2
        if mid < 1-p+p*(1-p)*phi(mid):
            low=mid
        else:
            high=mid
    t=(low+high)/2
    x=1-p;v=dphi(t);denom=1-(x*p*v)**2
    U=1/(1-m*p)-x*phi(t)/denom
    V=x*m/(1-m*p)-x*x*v/denom
    tprime=(-1+(1-2*p)*phi(t))/(1-p*x*v)
    vprime=ddphi(t)*tprime
    Hp=-2*x*v*(1-p*x**3*v*v)/(denom*denom)
    Hv=x*x*(1+(x*p*v)**2)/(denom*denom)
    Vprime=m*(m-1)/(1-m*p)**2-Hp-Hv*vprime
    return U,V,Vprime,t


def threshold(prob):
    m=sum(k*weight for k,weight in prob.items())
    low=1e-10;high=1/(m*m)
    for _ in range(85):
        mid=(low+high)/2
        if moments(prob,mid)[1]<1:
            low=mid
        else:
            high=mid
    return (low+high)/2


def truncated_binary_expectation(depth, p):
    """Exact finite-graph edge-state enumeration, counting original vertices only."""
    num=2**(depth+1)-1
    edges=[]
    for vertex in range(num):
        parent=(vertex-1)//2 if vertex else -1
        edges.append((parent,vertex))
        if vertex>=1:
            grandparent=(parent-1)//2 if parent else -1
            edges.append((grandparent,vertex))
    out=Fraction(0)
    for config in product((0,1),repeat=len(edges)):
        adjacency={i:[] for i in range(-1,num)}
        for bit,(a,b) in zip(config,edges):
            if bit:
                adjacency[a].append(b)
                adjacency[b].append(a)
        visited={-1};stack=[-1]
        while stack:
            for child in adjacency[stack.pop()]:
                if child not in visited:
                    visited.add(child);stack.append(child)
        n_open=sum(config)
        out+=(len(visited)-1)*p**n_open*(1-p)**(len(edges)-n_open)
    return out


def main():
    binary={2:1.0}
    q=threshold(binary)
    U,V,Vp,t=moments(binary,q)
    amplitude=U/Vp
    check(abs(q-0.15865632604477647)<1e-11,"binary threshold")
    check(abs(amplitude-0.08260628557486904)<1e-11,"binary pole amplitude")
    check(abs(V-1)<1e-12,"binary critical boundary mean")
    check(0<t<1 and U>0 and Vp>0,"critical regularity")
    finite=[truncated_binary_expectation(d,Fraction(1,10)) for d in range(3)]
    check(finite[0]==Fraction(1,10),"depth zero exact count")
    check(finite[1]==Fraction(33753,100000),"depth one exact count")
    check(finite[2]==Fraction(4357733646841,10000000000000),"depth two exact count")
    chi=moments(binary,0.1)
    check(float(finite[-1])<chi[0]/(1-chi[1]),"truncation is below infinite response")
    check(finite[0]<finite[1]<finite[2],"finite depth monotonicity")
    families=[
        {2:1.0},
        {0:.4,2:.6},
        {1:.5,2:.5},
        {1:.7,4:.3},
        {0:.7,5:.3},
        {0:.25,4:.5,8:.25},
        {1:.4,2:.4,6:.2},
    ]
    for prob in families:
        pc=threshold(prob)
        m=sum(k*w for k,w in prob.items())
        check(0<pc<1/m**2,"critical parameter domain")
        Up,Vpmean,derivative,fx=moments(prob,pc)
        check(Up>0 and derivative>0,"positive critical residue")
        check(abs(Vpmean-1)<1e-11,"critical offspring mean")
        for portion in [0.08,0.2,0.4,0.6,0.8,0.95,0.99]:
            p=pc*portion
            U,V,Vprime,t=moments(prob,p)
            check(U>=p-1e-11 and U>0,"positive root block")
            check(0<=V<1 and Vprime>0,"subcritical block process")
            check(1-p<=t<=1-p*p+1e-12,"fixed point bounds")
            h=min(1e-5,p*0.1,(1/m**2-p)*.1)
            finite_derivative=(moments(prob,p+h)[1]-moments(prob,p-h)[1])/(2*h)
            check(abs(finite_derivative-Vprime)<3e-5,"derivative formula")
        a=Up/derivative
        for eps in [1e-3,1e-4,1e-5]:
            h=pc*eps
            R=moments(prob,pc-h)
            scaled=h*R[0]/(1-R[1])
            check(abs(scaled/a-1)<.015,"simple pole numerical limit")
    print("PASS",CHECKS,"deterministic checks")
    print("binary-example: critical_p=%.14f, residue=%.14f"%(q,amplitude))
    print("truncated-binary-cluster-expectations:",*[str(x) for x in finite])

if __name__=='__main__':
    main()
