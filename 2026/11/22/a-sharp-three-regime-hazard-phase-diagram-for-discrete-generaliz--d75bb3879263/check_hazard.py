"""Independent numerical and rational sanity checks for a discrete hazard phase diagram.
The infinite-support claims rely on the analytic proof, not these finite diagnostics.
Requires mpmath; Python 3.10+."""
from fractions import Fraction
import mpmath as mp

mp.mp.dps = 85
checks = 0

def require(ok, message):
    global checks
    if not ok:
        raise AssertionError(message)
    checks += 1

def log_bounds(r, N=36):
    r = Fraction(r)
    z = (r - 1) / (r + 1)
    require(0 < z < 1, 'positive atanh argument')
    lower = 2 * sum((z**(2*j+1)/Fraction(2*j+1) for j in range(N)), Fraction(0))
    error = 2*z**(2*N+1) / (Fraction(2*N+1)*(1-z*z))
    return lower, lower+error

l2, u2 = log_bounds(Fraction(2))
l3, u3 = log_bounds(Fraction(3))
l43, u43 = log_bounds(Fraction(4,3))
l98, u98 = log_bounds(Fraction(9,8))
l1615, u1615 = log_bounds(Fraction(16,15))
require((3*u3 - 4*l2)/(2*l2) < l98/u43,
        'verified exact rational initial ratio separation')
require(u1615*(2*u2) < l43*(10*l2 - 6*u3),
        'verified exact rational T2<T0 near beta=1')

B=lambda k:mp.log(mp.mpf((k+2)**2)/((k+1)*(k+3)))
def D(k, beta):
    return mp.power(k+2,beta)-2*mp.power(k+1,beta)+mp.power(k,beta)
def T(k,beta): return B(k)/D(k,beta)
def eq(beta): return B(0)*D(1,beta)-B(1)*D(0,beta)
beta_star=mp.findroot(eq, (mp.mpf('1.06'),mp.mpf('1.07')))
t_star=T(0,beta_star)
require(mp.mpf('1.06526633486050')<beta_star<mp.mpf('1.06526633486052'), 'critical shape bracket')
require(abs(T(0,beta_star)-T(1,beta_star))<mp.mpf('1e-75'), 'critical equality')
require(T(2,beta_star)<t_star, 'critical tail dominance')
for beta_str in ['1.0001','1.01','1.05','1.06','1.07','1.1','1.5','2','5','10']:
    beta=mp.mpf(beta_str)
    thresholds=[T(k,beta) for k in range(20)]
    require(all(thresholds[k+1]<thresholds[k] for k in range(1,19)), 'tail threshold strict monotonicity')
    require((thresholds[0]<thresholds[1]) == (beta<beta_star), 'early threshold inversion')
    require(thresholds[2]<thresholds[0], 'second tail threshold below origin')
    for k in range(18):
        B_direct=mp.log(1+mp.mpf(1)/((k+1)*(k+3)))
        require(abs(B_direct-B(k))<mp.mpf('1e-75'), 'log formula consistency')

h=lambda k,beta,t:1-mp.mpf(k+1)/(k+2)*mp.exp(-t*(mp.power(k+1,beta)-mp.power(k,beta)))

def labels(beta,t,n=100):
    seq=[h(k,beta,t) for k in range(n+1)]
    return ['+' if seq[k+1]>seq[k] else '-' if seq[k+1]<seq[k] else '0' for k in range(n)]

b=mp.mpf('1.05'); t=mp.mpf('4.11')
z=labels(b,t,100)
require(z[0]=='+' and z[1]=='-' and all(x=='+' for x in z[2:]), 'up-down-up example')
for b,t,kind in [('.75','1','decreasing'),('2','.1','bathtub'),('2','1','increasing'),('1.05','4.11','up_down_up'),('1.05','1','bathtub')]:
    z=labels(mp.mpf(b),mp.mpf(t),60)
    changes=sum(z[i]!=z[i+1] for i in range(59))
    require(changes == {'decreasing':0,'increasing':0,'bathtub':1,'up_down_up':2}[kind], f'{kind} signs')

critical_h=[h(k,beta_star,t_star) for k in range(4)]
require(abs(critical_h[0]-critical_h[1])<mp.mpf('1e-75') and abs(critical_h[1]-critical_h[2])<mp.mpf('1e-75'), 'three-way plateau')
require(critical_h[3]>critical_h[2], 'post-critical increase')

for beta_str in ['1.05','1.5','2','3','6']:
    beta=mp.mpf(beta_str)
    for k in [1000,10000]:
        v=mp.power(k,beta)*T(k,beta)
        want=1/(beta*(beta-1))
        require(abs(v/want-1)<mp.mpf('0.009'), 'asymptotic leading constant')

print('PASS',checks,'checks')
print('beta_star =',mp.nstr(beta_star,38))
print('t_star =',mp.nstr(t_star,38))
print('pi_star =',mp.nstr(mp.exp(-t_star),38))
print('h(0),h(1),h(2),h(3) at beta=1.05,t=4.11 =',*[mp.nstr(h(k,b,mp.mpf('4.11')),22) for k in range(4)])
