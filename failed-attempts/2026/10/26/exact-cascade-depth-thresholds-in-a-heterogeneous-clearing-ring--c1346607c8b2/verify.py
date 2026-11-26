from fractions import Fraction as F

# Four-bank directed Eisenberg-Noe ring. Bank i owes nominal liability 1,
# with share lam[i] owed to bank i+1; the remainder is owed outside the ring.
lam = [F(1,2), F(2,3), F(3,4), F(1,3)]
s = [F(1,10), F(1,20), F(1,20), F(1,100)]
n = len(lam)
x = [1 - lam[(i-1) % n] + s[i] for i in range(n)]

def thresholds(lam, s):
    out = [s[0]]
    prod = F(1)
    for j in range(1, len(s)):
        prod *= lam[j-1]
        out.append(out[-1] + s[j] / prod)
    return out

tau = thresholds(lam, s)
assert tau == [F(1,10), F(1,5), F(7,20), F(39,100)]
assert all(tau[i] < tau[i+1] for i in range(n-1))
assert x[0] == F(23,30)

# Case 1: sigma = 9/25 lies in (tau_2, tau_3], so exactly banks 0,1,2 default.
sigma = F(9,25)
p = [F(37,50), F(23,25), F(299,300), F(1)]
for i in range(n):
    incoming = lam[(i-1) % n] * p[(i-1) % n]
    resources = x[i] - (sigma if i == 0 else 0) + incoming
    assert p[i] == min(F(1), resources)
assert sum(v < 1 for v in p) == 3

# Case 2: sigma = 2/5 exceeds tau_3, so all four banks default.
sigma = F(2,5)
d = [F(331,1100), F(221,2200), F(14,825), F(3,1100)]
p = [1-v for v in d]
for i in range(n):
    incoming = lam[(i-1) % n] * p[(i-1) % n]
    resources = x[i] - (sigma if i == 0 else 0) + incoming
    assert p[i] == resources and p[i] < 1
assert tau[-1] < sigma < x[0]

print('EXACT_RATIONAL_CHECKS_PASS')
print('assets=', [str(v) for v in x])
print('slacks=', [str(v) for v in s])
print('thresholds=', [str(v) for v in tau])
print('three_default_payments=', ['37/50','23/25','299/300','1'])
print('all_default_payments=', [str(v) for v in p])
