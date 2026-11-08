"""Reproducible high-precision diagnostics for a Beta-center Gaussian ensemble.
Only exact density identities and finite-N numerical predictions are tested;
proof of the N->infinity statements is analytical, not delegated to this file.
"""
import mpmath as mp
mp.mp.dps=65

def model(nu,B,sigma,N,threshold):
    nu,B,sigma=map(mp.mpf,(nu,B,sigma)); N=mp.mpf(N)
    c=1/(2*B*mp.beta(nu,nu))
    def integrand(y):
        if y==0 or y==2*B: return mp.mpf(0)
        return c*(y/(2*B))**(nu-1)*(1-y/(2*B))**(nu-1)*mp.erfc((threshold-B+y)*mp.sqrt(N)/(sigma*mp.sqrt(2)))/2
    # substitute y=2B*t to avoid subnormal endpoint behavior
    def f(t):
        if t<=0 or t>=1: return mp.mpf(0)
        return t**(nu-1)*(1-t)**(nu-1)*mp.erfc((threshold-B+2*B*t)*mp.sqrt(N)/(sigma*mp.sqrt(2)))/(2*mp.beta(nu,nu))
    return mp.quad(f,[mp.mpf('0'),mp.mpf('.0001'),mp.mpf('.001'),mp.mpf('.01'),mp.mpf('.1'),mp.mpf('.5'),1])

def k(nu,B): return 1/((2*mp.mpf(B))**mp.mpf(nu)*mp.beta(nu,nu))

def phi_bar(x):return mp.erfc(x/mp.sqrt(2))/2

def edge(nu,B,sigma,N):
    nu=mp.mpf(nu); return k(nu,B)*mp.mpf(sigma)**nu*2**(nu/2-1)*mp.gamma((nu+1)/2)/(nu*mp.sqrt(mp.pi))*mp.mpf(N)**(-nu/2)

def window(nu,B,sigma,N,xi):
    nu=mp.mpf(nu); sig=mp.mpf(sigma)
    return k(nu,B)*mp.mpf(N)**(-nu/2)*mp.quad(lambda y:y**(nu-1)*phi_bar((mp.mpf(xi)+y)/sig),[0,1,3,8,25,mp.inf])

def outer(nu,B,sigma,N,delta):
    nu=mp.mpf(nu);sig=mp.mpf(sigma); d=mp.mpf(delta)
    return (k(nu,B)*mp.gamma(nu)*sig**(2*nu+1)/
        (mp.sqrt(2*mp.pi)*d**(nu+1))*mp.mpf(N)**(-nu-mp.mpf('0.5'))*
        mp.exp(-mp.mpf(N)*d**2/(2*sig**2)))

def near(a,b,rel):
    return abs(a/b-1)<mp.mpf(rel)

def run():
    checks=0
    for nu in ['0.5','1','2','3']:
        for N in [256,4096,65536]:
            p=model(nu,1,1,N,mp.mpf('1'))
            theory=edge(nu,1,1,N)
            print('edge',nu,N,'ratio=',mp.nstr(p/theory,11))
            assert p>0
            checks+=1
            if N==65536:
                assert near(p,theory,'0.04'), (nu,N,p/theory)
                checks+=1
    for nu in ['0.5','1','2']:
        for xi in [-1,0,1]:
            N=20000
            p=model(nu,1,1,N,1+mp.mpf(xi)/mp.sqrt(N))
            asym=window(nu,1,1,N,xi)
            print('window',nu,xi,'ratio=',mp.nstr(p/asym,11))
            assert near(p,asym,'0.08')
            checks+=1
    for nu in ['0.5','1','2']:
        for N in [100,400,1600]:
            d=mp.mpf('0.3')
            p=model(nu,1,1,N,1+d)
            theory=outer(nu,1,1,N,d)
            print('outer',nu,N,'ratio=',mp.nstr(p/theory,11))
            assert p>0
            checks+=1
            if N==1600:
                assert near(p,theory,'0.15'), (nu,N,p/theory)
                checks+=1
    # Exact identity for uniform center density at nu=1, finite N.
    # Integrate normal survivor in closed form via H(z)=z Q(z)-phi(z).
    for N in [7,120,5000]:
        a=mp.sqrt(N)
        H=lambda z:z*phi_bar(z)-mp.exp(-z*z/2)/mp.sqrt(2*mp.pi)
        exact=(H(2*a)-H(0))/(2*a)
        p=model(1,1,1,N,1)
        assert near(p,exact,'1e-40'), (N,p,exact)
        checks+=1
    print('diagnostic_assertions',checks)
if __name__=='__main__':run()

# Supplemental check of the conditional hidden-center boundary layer.
def conditional_center_mean(nu,B,sigma,N):
    nu,B,sigma=map(mp.mpf,(nu,B,sigma)); N=mp.mpf(N)
    def f(t):
        if t<=0 or t>=1:return mp.mpf('0')
        w=2*B*t*mp.sqrt(N)
        return w*t**(nu-1)*(1-t)**(nu-1)*phi_bar(w/sigma)/mp.beta(nu,nu)
    return mp.quad(f,[0,mp.mpf('.0001'),mp.mpf('.001'),mp.mpf('.01'),mp.mpf('.1'),mp.mpf('.5'),1])/model(nu,B,sigma,N,B)

def conditional_limit(nu,sigma):
    nu,sigma=mp.mpf(nu),mp.mpf(sigma)
    # J_{nu+1}(0) / J_nu(0) for J_a = sigma^a E[Z_+^a]/a.
    return (sigma*(nu/(nu+1))*mp.sqrt(2)*mp.gamma((nu+2)/2)/mp.gamma((nu+1)/2))

if __name__=='__main__':
    cchecks=0
    for nu in ['0.5','1','2']:
        for N in [400,1600]:
            v=conditional_center_mean(nu,1,1,N)
            th=conditional_limit(nu,1)
            print('selected-center',nu,N,'ratio=',mp.nstr(v/th,11))
            assert near(v,th,'0.12')
            cchecks+=1
    print('additional_conditional_assertions',cchecks)
