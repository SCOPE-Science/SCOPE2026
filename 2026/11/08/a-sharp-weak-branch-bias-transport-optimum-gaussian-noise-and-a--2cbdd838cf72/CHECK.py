"""Direct finite-state and canonical checks for a ring with one path branch.
Requires Python 3 standard library only. Assertions test finite algebra and asymptotics,
not an infinite-volume proof.
"""
import math
from itertools import combinations


def sigmoid(x):
    if x >= 0:
        return 1 / (1 + math.exp(-x))
    y = math.exp(x)
    return y / (1 + y)


def chemical_potential(L, M, K, logq):
    assert 0 < K < L + M
    lo, hi = -max(1000, 2*M*abs(logq)+50), max(1000, 2*M*abs(logq)+50)
    for _ in range(140):
        mid = (lo+hi)/2
        s = L*sigmoid(mid) + sum(sigmoid(mid+logq*d) for d in range(1,M+1))
        if s < K: lo = mid
        else: hi = mid
    return (lo+hi)/2


def current_exact(L, M, K, logq, drift=1, with_variance=False):
    mu = chemical_potential(L,M,K,logq)
    p = sigmoid(mu)
    pb = [1.0]
    for d in range(1,M+1):
        z = sigmoid(mu+logq*d)
        next_pb = [0.]*(len(pb)+1)
        for i,v in enumerate(pb):
            next_pb[i] += v*(1-z)
            next_pb[i+1] += v*z
        pb = next_pb
    vals=[]
    for n in range(max(0,K-M),min(K,L)+1):
        bn = math.comb(L,n)*p**n*(1-p)**(L-n)
        vals.append((n,bn*pb[K-n]))
    den=sum(v for n,v in vals)
    assert den>0
    current = drift*sum(n*(L-n)*v for n,v in vals)/(den*L*(L-1))
    mean = sum(n*v for n,v in vals)/den
    variance = sum((n-mean)**2*v for n,v in vals)/den
    if with_variance:return current,mean/L,variance/L
    return current,mean/L


def limiting_f(c,rho,lam):
    def integral(mu):
        if abs(lam)<1.e-9:return c*sigmoid(mu)
        # exact antiderivative of logistic
        def softplus(x):return max(x,0)+math.log1p(math.exp(-abs(x)))
        return (softplus(mu+c*lam)-softplus(mu))/lam
    lo,hi=-1000,1000
    for _ in range(120):
        mid=(lo+hi)/2
        if sigmoid(mid)+integral(mid)<rho:lo=mid
        else:hi=mid
    return sigmoid((lo+hi)/2)


def optimum(c,rho):
    assert .5<rho<c+.5
    # for f=1/2, mu=0; solve for lambda
    lo,hi=-100,100
    for _ in range(120):
        lam=(lo+hi)/2
        if abs(lam)<1e-4: I=c/2+lam*c*c/8-lam**3*c**4/192+lam**5*c**6/2880
        else:
            def softplus(x):return max(x,0)+math.log1p(math.exp(-abs(x)))
            I=(softplus(c*lam)-math.log(2))/lam
        if .5+I < rho: lo=lam
        else: hi=lam
    return (lo+hi)/2


def check_generator(L=5,M=3,K=3,q=1.7,hf=1.3,hb=0.2,ht_base=.9):
    length=L+M
    states=[sum(1<<i for i in comb) for comb in combinations(range(length),K)]
    pi={s:q**sum((i-L+1) for i in range(L,length) if s>>i&1) for s in states}
    normal=sum(pi.values());pi={s:v/normal for s,v in pi.items()}
    edges=[]
    for i in range(L):edges.extend([(i,(i+1)%L,hf),((i+1)%L,i,hb)])
    for i in range(M):
        u=0 if i==0 else L+i-1
        v=L+i
        edges.extend([(u,v,q*ht_base),(v,u,ht_base)])
    residual={s:0.0 for s in states}
    for s in states:
        for a,b,rate in edges:
            if s>>a&1 and not(s>>b&1):
                other = s^(1<<a)^(1<<b)
                residual[s]-=pi[s]*rate
                residual[other]+=pi[s]*rate
    return max(abs(x) for x in residual.values())


def main():
    assertions=0
    assert check_generator() <1e-12; assertions+=1
    for L in (16,32,64,128):
        c=.75;M=math.floor(c*L);rho=.95;K=math.floor(rho*L)
        for lam in (-5.,-2.,0.,2.,5.):
            exact,fb=current_exact(L,M,K,lam/L)
            f=limiting_f(c,rho,lam)
            assert abs(exact-f*(1-f))< .16/math.sqrt(L), (L,lam,exact,f)
            assertions+=1
        lamstar=optimum(c,rho)
        fstar=limiting_f(c,rho,lamstar)
        assert abs(fstar-.5)<1e-12; assertions+=1
        for delta in (-2,-.1,.1,2.):
            assert limiting_f(c,rho,lamstar+delta)*(1-limiting_f(c,rho,lamstar+delta)) <.25
            assertions+=1
    # Positive L^{-1} finite-size current excess at optimal weak branch bias.
    c=.75;rho=.95;lam=optimum(c,rho)
    vbranch=(sigmoid(c*lam)-.5)/lam
    excess=.25*.25/(.25+vbranch)
    for L in (32,64,128,256):
        M=math.floor(c*L);K=math.floor(rho*L)
        j,_=current_exact(L,M,K,lam/L)
        assert j>.25, (L,j)
        assert abs(L*(j-.25)-excess)<.021, (L,j,excess)
        assertions+=2
    c=.75;rho=.95;lam=optimum(c,rho)
    f=limiting_f(c,rho,lam)
    mu=math.log(f/(1-f))
    vb=f*(1-f)
    vt=(sigmoid(mu+c*lam)-sigmoid(mu))/lam
    variance_target=vb*vt/(vb+vt)
    for L in (32,64,128,256):
        M=math.floor(c*L);K=math.floor(rho*L)
        curr,mean,variance=current_exact(L,M,K,lam/L,with_variance=True)
        assert abs(variance-variance_target)<.09/math.sqrt(L), (L,variance,variance_target)
        assertions+=1
        # Identity from exchangeability gives the covariance for two distinct sites.
        cov=(L*variance-L*mean*(1-mean))/(L*(L-1))
        assert abs(L*cov+vb*vb/(vb+vt))<.30/math.sqrt(L),(L,L*cov)
        assertions+=1
    for q in (.75,1.,1.35):
        for rho in (.4, .9, 1.2):
            for L in (20,40,80):
                M=math.floor(.75*L);K=math.floor(rho*L)
                exact,fb=current_exact(L,M,K,math.log(q))
                assert 0<=exact<=L/(4*(L-1))+1e-12
                assertions+=1
            if q>1:limit=max(rho-.75,0);target=limit*(1-limit)
            elif q<1:limit=min(rho,1);target=limit*(1-limit)
            else:limit=rho/1.75;target=limit*(1-limit)
            assert abs(exact-target)<.085,(q,rho,exact,target)
            assertions+=1
    print(f'PASS {assertions} checks; sample c=.75 rho=.95: lambda*={optimum(.75,.95):.12f}; max current=0.25')
    for lam in (-5,0,5):
        print(f' lambda={lam:+g}, f={limiting_f(.75,.95,lam):.9f}, limiting current={limiting_f(.75,.95,lam)*(1-limiting_f(.75,.95,lam)):.9f}')

if __name__ == '__main__':main()
