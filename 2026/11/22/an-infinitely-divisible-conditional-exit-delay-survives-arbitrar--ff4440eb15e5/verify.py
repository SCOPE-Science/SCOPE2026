"""Numerical checks for the two-target conditional convolution theorem.
This script checks identities, not the validity of the infinite theorem."""
import math


def exit_transforms(a, b, D, r, s):
    k = math.sqrt((r + s) / D)
    return math.sinh(b * k) / math.sinh((a + b) * k), math.sinh(a * k) / math.sinh((a + b) * k)


def delta_transform(a, b, D, r, s):
    kr = math.sqrt(r / D)
    ks = math.sqrt((r + s) / D)
    return math.sinh(a * ks) / math.sinh(b * ks) * math.sinh(b * kr) / math.sinh(a * kr)


def spectral_sum(a, b, D, r, power, N=100000):
    return math.fsum((r + D * math.pi**2 * n*n/(b*b))**(-power) - (r + D * math.pi**2 * n*n/(a*a))**(-power) for n in range(1,N+1))


def run():
    checks = 0
    for a,b,D,r in [(0.7,1.3,0.9,1.2),(1.0,4.0,1.3,0.4),(0.25,0.75,0.3,2.0),(0.8,1.2,2.0,3.0)]:
        f0,f1 = exit_transforms(a,b,D,r,0)
        assert 0 < f0+f1 < 1
        for s in (0.1,0.7,2.0):
            fl,fr=exit_transforms(a,b,D,r,s)
            delay=delta_transform(a,b,D,r,s)
            for w,h in ((0.3,0.1),(0.8,2.1)):
                R=w*math.exp(-s*h)+(1-w)*math.exp(-s*2*h)
                B=r/(r+s)*(1-fl-fr)*R
                B0=1-f0-f1
                # Transform of completed process, normalized by its exit-side probability.
                lapl=(fl/(1-B))/(f0/(1-B0))
                lapr=(fr/(1-B))/(f1/(1-B0))
                assert abs(lapr/lapl-delay)<5e-13,(a,b,D,r,s)
                assert 0<lapr<lapl<=1.0000000001
                checks+=3
            # Laplace transform of conditioned hitting b before 0, r tilted.
            assert abs(delay-(math.sinh(a*math.sqrt((r+s)/D))/math.sinh(b*math.sqrt((r+s)/D)))/(math.sinh(a*math.sqrt(r/D))/math.sinh(b*math.sqrt(r/D))))<1e-12
            checks+=1
            logp=math.fsum(math.log1p(s/(r+D*math.pi**2*n*n/(a*a)))-math.log1p(s/(r+D*math.pi**2*n*n/(b*b))) for n in range(1,50001))
            assert abs(logp-math.log(delay))<0.0002,(a,b,D,r,s,logp,math.log(delay))
            checks+=1
        # All cumulants are positive and have exact spectral expression.
        for k in range(1,5):
            assert spectral_sum(a,b,D,r,k,10000)>0
            checks+=1
        kr=math.sqrt(r/D)
        m=(b/math.tanh(b*kr)-a/math.tanh(a*kr))/(2*D*kr)
        mseries=spectral_sum(a,b,D,r,1,100000)
        assert abs(m-mseries)<0.00003, (m,mseries)
        checks+=1
    # Zero-reset analytic checks for mean and variance from zeta(2), zeta(4).
    for a,b,D in [(1.,2.,1.),(.3,1.6,2.3)]:
        assert abs(spectral_sum(a,b,D,0,1,100000)-(b*b-a*a)/(6*D))<0.00002
        assert abs(spectral_sum(a,b,D,0,2,100000)-(b**4-a**4)/(90*D*D))<1e-8
        checks+=2
    print('PASS:',checks,'numerical identities, mixture-factor/product checks, and positive-cumulant checks')


if __name__=='__main__':
    run()
