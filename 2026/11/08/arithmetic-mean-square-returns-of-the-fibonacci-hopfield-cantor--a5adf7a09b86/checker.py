"""Numerical high-precision checks of the analytic Fibonacci return identities.

The all-parameter theorem is proved in RESULT.md; this script independently
integrates finite jump approximations and checks the tail-controlled formula.
"""
import mpmath as mp

mp.mp.dps = 75
phi = (1 + mp.sqrt(5))/2
alpha = (3-mp.sqrt(5))/2
N = 70
points = [mp.frac(k*alpha) for k in range(1,N+1)]
weights = [mp.power(2,-k) for k in range(1,N+1)]

def q(t):
    return sum((w for p,w in zip(points,weights) if p < t),mp.mpf('0'))

def direct_displacement(tau):
    breaks = {mp.mpf('0'),mp.mpf('1'),1-tau}
    for p in points:
        breaks.add(p)
        breaks.add(mp.frac(p-tau))
    breaks = sorted(breaks)
    total=mp.mpf('0')
    for a,b in zip(breaks,breaks[1:]):
        mid=(a+b)/2
        delta=q(mp.frac(mid+tau))-q(mid)
        total+=(b-a)*delta*delta
    return total

def analytic_series(tau,terms=280):
    correction = sum((mp.power(2,1-k)*max(mp.mpf('0'),tau-mp.fabs(mp.frac(k*alpha)-mp.nint(mp.frac(k*alpha)))) for k in range(1,terms+1)),mp.mpf('0'))
    return (mp.mpf(4)/3)*tau-(mp.mpf(2)/3)*correction

assert mp.mpf('0')<alpha<mp.mpf('1')
phi_powers=[]
fs=[0,1]
for j in range(2,14):
    fs.append(fs[-1]+fs[-2])
assert fs[5]==5 and fs[10]==55
for j in range(5,11):
    F=fs[j]
    tau=phi**(-j)
    assert mp.fabs(mp.fabs(F*alpha-mp.nint(F*alpha))-tau)<mp.mpf('1e-65')
    direct=direct_displacement(tau)
    target=analytic_series(tau)
    assert mp.fabs(direct-target)<mp.power(2,-N+5), (j,direct,target)
    err=(mp.mpf(4)/3)*tau-target
    lower=(mp.mpf(2)/3)*mp.power(2,1-fs[j+1])*(tau-phi**(-j-1))
    upper=(mp.mpf(8)/3)*tau*mp.power(2,-fs[j+1])
    assert err>0
    assert lower-mp.mpf('1e-50')<=err<=upper+mp.mpf('1e-50')
    phi_powers.append((j,mp.nstr(target/tau,23)))
print('independent finite-jump integration agrees with the analytic series: 6 checks')
print('Fibonacci bounds and exact approximation identities: 18 checks')
print('ratios:',phi_powers)
