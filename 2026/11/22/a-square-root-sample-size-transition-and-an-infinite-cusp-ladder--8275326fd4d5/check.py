"""Independent numerical checks of a Poisson empirical L1 critical-limit formula.

This script checks finite binomial identities, Gaussian quadrature, monotonicity,
small-window cusp coefficients, and finite-sample convergence. Its finite checks
are supporting tests, not substitutes for the analytic limit proofs.
"""
import math
from scipy.integrate import quad
from scipy.stats import poisson, binom
from scipy.special import gammaln
from scipy.stats import norm

COUNTS={'finite_binomial':0,'absolute_poisson':0,'monotone':0,'limits':0,'cusp':0,'finite_n':0}


def check(test, kind, msg):
    assert test, f'{kind}: {msg}'
    COUNTS[kind]+=1


def phi(z):
    return math.exp(-0.5*z*z)/math.sqrt(2*math.pi)


def modal_probability(t):
    return poisson.pmf(math.floor(t),t)


def critical_limit(kappa):
    peak=phi(0)/math.sqrt(kappa)
    cuts=[0.,12.]+[math.sqrt(2*math.log(peak/j)) for j in range(1, math.floor(peak)+1) if peak>j]
    cuts=sorted(cuts)
    return sum(quad(lambda z:4*phi(z)*modal_probability(peak*math.exp(-z*z/2)),
                    a,b,epsabs=2e-12,epsrel=2e-12)[0] for a,b in zip(cuts,cuts[1:]))


def binomial_central_truncated_mean(n,lam):
    # Sum of exact E|Bin(n,q_k)-nq_k|/n over the central Poisson range.
    lo=max(0,int(lam-13*math.sqrt(lam)-30))
    hi=int(lam+13*math.sqrt(lam)+30)
    ans=0.
    for k in range(lo,hi+1):
        p=poisson.pmf(k,lam)
        if p==0.:continue
        ans+=2*p*(1-p)*binom.pmf(math.floor(n*p),n-1,p)
    return ans


def baseline(kappa):
    # Analytic branch when peak expected occupancy is less than one.
    peak=phi(0)/math.sqrt(kappa)
    return quad(lambda z:4*phi(z)*math.exp(-peak*math.exp(-z*z/2)),0,12,
                epsabs=2e-12,epsrel=2e-12)[0]

# Exact finite binomial positive-part identity, independently enumerated.
for n in [1,2,3,4,7,11,25]:
    for p in [.01,.03,.12,.25,.49,.5,.7,.9,.99]:
        direct=sum(abs(k-n*p)*binom.pmf(k,n,p) for k in range(n+1))
        formula=2*n*p*(1-p)*binom.pmf(math.floor(n*p),n-1,p)
        check(abs(direct-formula)<1e-10,'finite_binomial',f'n={n},p={p}, {direct} vs {formula}')

# Exact Poisson absolute-deviation identity by finite-tail summation.
for t in [.003,.03,.2,.5,.95,1.,1.001,1.9,2.,3.,4.,6.2,9.]:
    val=sum(abs(k-t)*poisson.pmf(k,t) for k in range(130))
    eq=2*t*modal_probability(t)
    check(abs(val-eq)<1e-10,'absolute_poisson',f't={t}, {val} vs {eq}')

# Profile is continuous and strictly increasing.
ks=[0.0005,.001,.002,.004,.008,.015,.03,.06,.1,1/(2*math.pi),.2,.4,.8,1.5,3.,10.,40.,200.]
vals=[critical_limit(x) for x in ks]
for a,b in zip(vals,vals[1:]):check(b>a,'monotone',f'non-increase {a}->{b}')
for k,v in zip(ks,vals):check(0<v<2,'limits',f'not in (0,2): {k}, {v}')
check(vals[0]<.28,'limits','small-kappa limit not small')
check(vals[-1]>1.95,'limits','large-kappa limit not close to two')

# Sharp 3/2 singularity at the first modal threshold: coefficient calculated
# from the one-sided derivative jump, not fitted to quadrature values.
kstar=1/(2*math.pi)
pstar=math.exp(-1)
coeff=4*phi(0)*pstar/(3*kstar**1.5)
for delta,rtol in [(1e-2,.04),(1e-3,.005),(1e-4,.0005),(1e-5,.00006)]:
    ratio=(critical_limit(kstar-delta)-baseline(kstar-delta))/delta**1.5
    check(abs(ratio/coeff-1)<rtol,'cusp',f'coefficient at {delta}: {ratio}, {coeff}')
for d in [1e-4,1e-3,1e-2]:
    check(abs(critical_limit(kstar+d)-baseline(kstar+d))<1e-10,'cusp',f'right branch {d}')

# Direct expected L1 from binomial marginals approaches the continuum profile.
for kappa in [.2,1.]:
    lim=critical_limit(kappa)
    for n in [80,200,500]:
        finite=binomial_central_truncated_mean(n,kappa*n*n)
        check(abs(finite-lim)<.06,'finite_n',f'kappa={kappa},n={n}, {finite} vs {lim}')

print('SUCCESS',sum(COUNTS.values()),'assertions',COUNTS)
print('PROFILE',[(k,round(critical_limit(k),12)) for k in [.01,.1,kstar,.2,1.,10.]])
print('FIRST_CRITICAL_KAPPA',format(kstar,'.14f'),'CUSP_COEFFICIENT',format(coeff,'.12f'))
