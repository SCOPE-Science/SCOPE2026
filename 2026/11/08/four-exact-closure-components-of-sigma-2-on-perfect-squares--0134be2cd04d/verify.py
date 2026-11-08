"""Independent exact finite checks for a four-component square-input divisor-sum theorem.
Run with Python 3; standard library only. Analytic prime-ratio lemma and infinite
binary-subsum argument are mathematical proof premises, not computer certificates.
"""
from fractions import Fraction as Q
from math import pi


def primes_below(n):
    composite = bytearray(n)
    result = []
    for p in range(2, n):
        if composite[p]:
            continue
        result.append(p)
        for j in range(p*p, n, p):
            composite[j] = 1
    return result

pr = primes_below(150)
assert pr[:10] == [2,3,5,7,11,13,17,19,23,29]
finite = []
for j in range(2, 9):  # zero-based prime indices: p=5,7,11,13,17,19,23
    p = pr[j]
    tail = Q(1)
    for h in range(j+1, len(pr)):
        q = pr[h]
        tail *= Q(q*q + 1, q*q)
        if tail > Q(p*p, p*p-1):
            finite.append((p, q, h-j))
            break
    else:
        raise AssertionError(f"finite inequality fails for {p}")
assert [x[2] for x in finite] == [6,5,2,2,2,2,2]
# If consecutive-prime ratios are < cube_root(2) < 4/3 after index 9,
# the next three factors suffice, using these exact rational checks.
ratio_bound = sum((Q(9,16)**r for r in (1,2,3)), Q(0))
assert ratio_bound == Q(4329,4096)
assert ratio_bound > Q(29*29,29*29-1)

M_lower = Q(2,3)*sum((Q(1,k*k) for k in range(1,9)), Q(0))
M_upper = Q(484, 49*9)  # M=pi^2/9 is between rational bounds
T2_min, T2_max = Q(21,16), Q(4,3)
T3_min, T3_max = Q(91,81), Q(9,8)
assert T2_min == 1+Q(1,4)+Q(1,16)
assert T3_min == 1+Q(1,9)+Q(1,81)
# Adjacent prime-power local choices times the [1,M] tail overlap.
assert T2_max/T2_min == Q(64,63) < M_lower
assert T3_max/T3_min == Q(729,728) < M_lower
# Separation of the three intervening gaps, using pi < 22/7.
pi2_upper = Q(484,49)
assert pi2_upper/Q(9) < T3_min
assert pi2_upper/Q(8) < T2_min
assert Q(4,27)*pi2_upper < T2_min*T3_min
assert T2_min*T3_min == Q(637,432)

# For sampled positive m, sigma_{-2}(m^2) has a value in exactly one interval.
N=60000
spf=list(range(N+1))
for p in range(2, int(N**0.5)+1):
    if spf[p]==p:
        for n in range(p*p,N+1,p):
            if spf[n]==n: spf[n]=p
bounds=[(1., pi*pi/9), (91/81,pi*pi/8), (21/16,4*pi*pi/27), (637/432,pi*pi/6)]
counts=[0,0,0,0]
for m in range(1,N+1):
    r=m; v=1.0; has2=False; has3=False
    while r>1:
        p=spf[r]; a=0
        while r%p==0:
            a+=1; r//=p
        v*=sum((p**(-2*j) for j in range(2*a+1)))
        if p==2: has2=True
        if p==3: has3=True
    branch=(2 if has2 else 0)+(1 if has3 else 0)
    # branch order 00,01,10,11
    assert bounds[branch][0]-1e-10 <= v <= bounds[branch][1]+1e-10, (m,v,branch)
    assert sum(lo-1e-10<=v<=hi+1e-10 for lo,hi in bounds)==1,(m,v)
    counts[branch]+=1
assert sum(counts)==N
print('VERIFY_OK finite_prime_tail_inequalities=7')
print('finite_certificates_p_next_count=', finite)
print('ratio_bound=', ratio_bound, 'pi2_upper=', pi2_upper)
print('four_intervals=',bounds)
print('all_sampled_integer_squares=',N,'branch_counts=',counts)
print('Infinite prime-ratio and binary-subsum steps require the mathematical proof.')
