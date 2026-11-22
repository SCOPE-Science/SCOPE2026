"""Reproduce the sharp squared-SLEM stability inequality on finite paths.

The universal quantifier is justified by the analytical argument in RESULT.md;
these finite checks independently probe normalization, identities and edge cases.
"""
import numpy as np

def kernel(q):
    n=len(q)+1
    P=np.diag(1-np.r_[0,q]-np.r_[q,0])
    return P+np.diag(q,1)+np.diag(q,-1)

def trial(q):
    n=len(q)+1
    theta=np.pi/n
    c=np.cos(theta)
    y=np.sqrt(2/n)*np.cos((np.arange(n)+.5)*theta)
    P=kernel(q)
    Pstar=kernel(np.full(n-1,.5))
    delta=q-.5
    d=np.diff(-y)
    u=np.r_[0,delta*d,0]
    r=-np.diff(u)
    eig=np.linalg.eigvalsh(P-np.ones((n,n))/n)
    s=np.max(abs(eig))
    h=(1-c)/(n*c)*(c-np.cos((2*np.arange(n)+1)*theta)) if n>=3 else np.zeros(n)
    assert np.max(abs(P.sum(axis=1)-1))<2e-13
    assert abs(y@y-1)<2e-13
    assert abs(y@np.ones(n))<2e-13
    assert np.linalg.norm(Pstar@y-c*y)<2e-13
    assert np.linalg.norm((P-Pstar)@y-r)<2e-13
    assert s*s-c*c+2e-12>=sum(r*r), (n, q, s*s-c*c, sum(r*r))
    if n>=3:
        assert abs(y@P@y-c-np.diag(P)@h)<3e-13
        assert min(h)>-2e-14
        assert min(h[1:-1])>0
    for i in range(1,n):
        dval=np.sqrt(8/n)*np.sin(i*theta)*np.sin(theta/2)
        assert abs(d[i-1]-dval)<1e-13
        lhs=abs(delta[i-1]);rhs=np.sqrt(i*(n-i)/n)*np.sqrt(max(s*s-c*c,0))/dval
        assert lhs<=rhs+2e-11,(n,i,lhs,rhs)
    return s*s-c*c, sum(r*r)

def main():
    rng=np.random.default_rng(20261115)
    tests=0
    for n in range(3,21):
        for t in np.linspace(-.5,.5,21):
            q=np.array([.5+((-1)**i)*t for i in range(n-1)])
            a,b=trial(q);tests+=1
            expected=4*t*t*np.sin(np.pi/n)**2
            assert abs(a-expected)<2e-12,(n,t,a,expected)
            assert abs(b-expected)<2e-12,(n,t,b,expected)
        for _ in range(250):
            q=[]
            for i in range(n-1):
                q.append(rng.uniform(0,1-(q[-1] if i else 0)))
            trial(np.array(q));tests+=1
    for t in np.linspace(-.5,.5,21):
        a,b=trial(np.array([.5+t]));tests+=1
        assert abs(a-b)<2e-12
    print('PASS', tests, 'path matrices; squared SLEM inequality, equality family, strict-slack identities, coordinate bounds')
if __name__=='__main__': main()
