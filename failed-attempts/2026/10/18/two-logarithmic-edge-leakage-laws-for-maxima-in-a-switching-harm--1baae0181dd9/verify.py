"""Numerical checks for critical extreme-value boundary layers in a switching harmonic trap.

Requires numpy and scipy. The proof is analytic; this program checks the exact
Gaussian-mixture integrals against the proposed endpoint asymptotics.
"""
import math
from scipy.integrate import quad
from scipy.special import gammaln, log_ndtr


def parameters(mu_hi, mu_lo, r_hi_lo, r_lo_hi, diffusion):
    assert mu_hi > mu_lo > 0 and min(r_hi_lo, r_lo_hi, diffusion) > 0
    p = r_hi_lo / (2 * mu_hi)
    q = r_lo_hi / (2 * mu_lo)
    rh = 2 * r_hi_lo * r_lo_hi / (r_hi_lo + r_lo_hi)
    c = math.exp(gammaln(p + q + 1) - gammaln(p + 1) - gammaln(q + 1))
    return dict(p=p, q=q, mu_hi=mu_hi, mu_lo=mu_lo, diffusion=diffusion,
                c=c, rh=rh, a=diffusion/mu_hi, b=diffusion/mu_lo,
                kl=mu_hi/mu_lo-1, kh=1-mu_lo/mu_hi,
                H0=c*rh/(4*mu_hi), H1=c*rh/(4*mu_lo))


def smooth_weight(u, P):
    return P['c']*P['rh']/4 * ((1-u)/P['mu_hi'] + u/P['mu_lo'])


def integration(P, fun):
    return quad(lambda u: smooth_weight(u,P)*fun(u), 0, 1,
                weight='alg', wvar=(P['p']-1,P['q']-1),
                epsabs=2e-11, epsrel=2e-10, limit=500)[0]


def critical_threshold(L, variance, y):
    center=math.sqrt(2*L)-(math.log(L)+math.log(4*math.pi))/(2*math.sqrt(2*L))
    return math.sqrt(variance)*(center + y/math.sqrt(2*L))


def cdf_from_log_n(L, x, variance):
    z=x/math.sqrt(variance)
    log_nq=L+float(log_ndtr(-z))
    if log_nq > 15:
        return 0.0
    if log_nq < -35:
        return 1.0
    q=math.exp(float(log_ndtr(-z)))
    # exp(N*log(1-q)), computed without needing N to fit in a float
    ln_cdf=math.exp(L)*math.log1p(-q) if L<700 else -math.exp(log_nq)
    return math.exp(ln_cdf)


def exceed_from_log_n(L, x, variance):
    z=x/math.sqrt(variance)
    log_nq=L+float(log_ndtr(-z))
    if log_nq > 25:
        return 1.0
    if log_nq < -36:
        return math.exp(log_nq)
    q=math.exp(float(log_ndtr(-z)))
    exponent=math.exp(L)*math.log1p(-q) if L<700 else -math.exp(log_nq)
    return -math.expm1(exponent)


def edge_scaled_exact(P,L,y,side):
    """Split the full finite-N mixture to resolve its narrow active endpoint."""
    power=P['p'] if side=='low' else P['q']
    other=P['q'] if side=='low' else P['p']
    rate=P['kl'] if side=='low' else P['kh']
    cutoff=min(.5*L,max(40.,40./rate))
    x=critical_threshold(L,P['a'] if side=='low' else P['b'],y)
    def smooth(w):
        u=w/L if side=='low' else 1-w/L
        var=P['a']+(P['b']-P['a'])*u
        part=cdf_from_log_n(L,x,var) if side=='low' else exceed_from_log_n(L,x,var)
        return smooth_weight(u,P)*part
    # w^(power-1) * (1-w/L)^(other-1) is the exact changed-variable weight.
    head=quad(lambda w:(1-w/L)**(other-1)*smooth(w),0,cutoff,
              weight='alg',wvar=(power-1,0),
              epsabs=2e-12,epsrel=1e-11,limit=900)[0]
    tail=quad(lambda w:L**(1-other)*w**(power-1)*smooth(w),cutoff,L,
              weight='alg',wvar=(0,other-1),
              epsabs=2e-12,epsrel=1e-11,limit=900)[0]
    return head+tail


def edge_limit(P,y,side):
    if side=='high':
        def fun(w):
            z=-y-P['kh']*w
            return w**(P['q']-1)*(-math.expm1(-math.exp(z))) if z>-730 else 0.0
        # upper cutoff of 200/kappa is more than enough
        return P['H1']*quad(fun,0,max(150,150/P['kh']),epsabs=1e-11,limit=350)[0]
    def fun(w):
        z=-y+P['kl']*w
        return w**(P['p']-1)*math.exp(-math.exp(z)) if z<500 else 0.0
    return P['H0']*quad(fun,0,max(100,100/P['kl']),epsabs=1e-11,limit=350)[0]


def main():
    test_cases=[(2.,1.,4.,2.,1.),(3.,1.,3.,1.,.7),(5.,2.,2.,3.,1.3)]
    checked=0
    for args in test_cases:
        P=parameters(*args)
        assert abs(integration(P, lambda u: 1)-1)<1e-10; checked+=1
        for side in ('low','high'):
            expn=P['p'] if side=='low' else P['q']
            for y in (-1.,0.,1.):
                C=edge_limit(P,y,side)
                assert C>0 and math.isfinite(C);checked+=1
                for L in (120.,400.,1200.):
                    val=edge_scaled_exact(P,L,y,side)
                    err=abs(val/C-1)
                    # Slow logarithmic corrections are expected; only the final scale is tested.
                    print('p q side y L normalized constant error',
                          round(P['p'],4),round(P['q'],4),side,y,L,
                          round(val,8),round(C,8),round(err,6))
                    assert math.isfinite(val) and val>0; checked+=1
                    if L==1200:
                        assert err<0.20, (P,side,y,L,val,C,err)
                        checked+=1
    # The literal (unshifted) edges of the compact first-order support differ
    # from the Gaussian-centered Gumbel edge by a loglog correction.
    for args in test_cases:
        P=parameters(*args)
        for side in ('low','high'):
            ratios=[]
            for L in (120.,400.,1200.):
                y=(math.log(L)+math.log(4*math.pi))/2
                power=P['p'] if side=='low' else P['q']
                exact=edge_scaled_exact(P,L,y,side)/L**power
                if side=='low':
                    asym=P['H0']/P['p']*(math.log(L)/(2*P['kl']*L))**P['p']
                else:
                    asym=P['H1']*math.gamma(P['q'])/(math.sqrt(4*math.pi)*P['kh']**P['q']*L**(P['q']+.5))
                ratio=exact/asym
                print('nominal edge p q side L exact asym ratio',round(P['p'],4),round(P['q'],4),side,L,round(exact,12),round(asym,12),round(ratio,6))
                assert exact>0 and asym>0 and math.isfinite(ratio);checked+=1
                ratios.append(ratio)
                if L==1200.:
                    assert abs(ratio-1)<.4;checked+=1
            assert abs(ratios[-1]-1)<abs(ratios[0]-1);checked+=1
    print('All',checked,'normalization, positivity, and large-N edge checks passed.')

if __name__ == '__main__':
    main()
