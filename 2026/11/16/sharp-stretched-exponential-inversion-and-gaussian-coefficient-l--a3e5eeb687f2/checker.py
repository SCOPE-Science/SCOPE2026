"""Reproducibility checks for stretched-exponential weighted Fourier inversion."""
import math
import random

def parameters(t, alpha, tau):
    beta=math.acosh(1/t)
    r=(tau*alpha/beta)**(1/(1-alpha))
    sigma=math.sqrt(r**(2-alpha)/(tau*alpha*(1-alpha)))
    h=(1-alpha)*tau*r**alpha
    return beta,r,sigma,h

def logsumexp(values):
    m=max(values)
    return m+math.log(sum(math.exp(x-m) for x in values))

def exact_norm(t, alpha, tau, cutoff=None):
    beta,r,sigma,h=parameters(t,alpha,tau)
    if cutoff is None:
        cutoff=math.ceil(max(40, r+12*sigma, 4*r))
    v=[tau*k**alpha-beta*k for k in range(1,cutoff+1)]
    logS=logsumexp(v)
    return -0.5*math.log1p(-t*t)+math.log1p(2*math.exp(logS))

def asymptotic_log(t,alpha,tau):
    beta,r,sigma,h=parameters(t,alpha,tau)
    return -0.5*math.log1p(-t*t)+math.log(2*math.sqrt(2*math.pi)*sigma)+h

def direct_norm(t,alpha,tau,nsteps=160):
    p={0:1.0}; ans=0.0
    for n in range(nsteps):
        ans+= t**n*sum(v*math.exp(tau*abs(k)**alpha) for k,v in p.items())
        q={}
        for k,v in p.items():
            q[k-1]=q.get(k-1,0)+v/2
            q[k+1]=q.get(k+1,0)+v/2
        p=q
    return ans

def exact_green_k(t,k):
    q=(1-math.sqrt(1-t*t))/t
    return q**abs(k)/math.sqrt(1-t*t)

def direct_green_k(t,k,nsteps=180):
    p={0:1.0}; total=0
    for n in range(nsteps):
        total+=t**n*p.get(k,0)
        q={}
        for j,x in p.items():
            q[j-1]=q.get(j-1,0)+x/2
            q[j+1]=q.get(j+1,0)+x/2
        p=q
    return total

def tests():
    cnt=0
    for t in [0.12,0.32,0.55,0.73]:
      for k in range(-5,6):
        got=direct_green_k(t,k,160)
        expected=exact_green_k(t,k)
        assert abs(got-expected)<2e-12, (t,k,got,expected)
        cnt+=1
    for t in [0.12,0.32,0.55]:
      for alpha in [0.25,0.5,0.75]:
        for tau in [0.2,0.65,1.2]:
          got=direct_norm(t,alpha,tau,170)
          expected=math.exp(exact_norm(t,alpha,tau,cutoff=260))
          assert abs(got/expected-1)<2e-9, (t,alpha,tau,got,expected)
          cnt+=1
    # Independently check the saddle ratios in several asymptotic regimes
    for (alpha,tau,t,cap) in [(0.5,1.2,0.999,0.12),(0.5,1.2,0.9999,0.04),
                             (0.25,1.6,0.9999,0.2), (0.75,0.5,0.98,0.20),
                             (0.75,0.5,0.995,0.1)]:
      beta,r,sigma,h=parameters(t,alpha,tau)
      assert r>=10, (alpha,tau,t,r)
      err=abs(exact_norm(t,alpha,tau)-asymptotic_log(t,alpha,tau))
      assert err<cap,(alpha,tau,t,r,err)
      print('saddle',alpha,tau,t,'r',round(r,2),'log-error',round(err,7))
      cnt+=1
    # Independent weighted-marginal checks of Gaussian localization.
    # Finite large-r comparisons are illustrative, not proof of weak convergence.
    for alpha,tau,t in [(0.5,1.2,0.999999),(0.75,0.5,0.9995)]:
      beta,r,sigma,h=parameters(t,alpha,tau)
      lo=max(1,math.floor(r-9*sigma))
      hi=math.ceil(r+9*sigma)
      wsum=mean=second=cdf0=0.0
      for k in range(lo,hi+1):
        w=math.exp(tau*k**alpha-beta*k-h)
        z=(k-r)/sigma
        wsum+=w
        mean+=w*z
        second+=w*z*z
        if z<=0: cdf0+=w
      mean/=wsum
      variance=second/wsum-mean*mean
      cdf0/=wsum
      assert abs(mean)<0.09,(alpha,mean);cnt+=1
      assert abs(variance-1)<0.015,(alpha,variance);cnt+=1
      assert abs(cdf0-0.5)<0.03,(alpha,cdf0);cnt+=1
    print('PASS',cnt,'independent checks')

if __name__=='__main__': tests()
