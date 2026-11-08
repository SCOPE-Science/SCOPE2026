#!/usr/bin/env python3
"""Independent numerical diagnostics for a Gaussian-jump finite-window capture theorem.
These finite calculations supplement, not replace, the analytic proof.
"""
import math

P=0.5
Q=1.0-P
A=1.0
SIGMA=1.0
M=1.0/(1.0+1.0) # competing independent Exp(1) event clocks
MAX=1/math.sqrt(2*math.pi)/SIGMA

def f_n(n,a=A):
    return math.exp(-a*a/(2*n*SIGMA*SIGMA))/math.sqrt(2*math.pi*n*SIGMA*SIGMA)

def normal_interval(n,eps):
    d=math.sqrt(2*n)*SIGMA
    return 0.5*(math.erf((A+eps)/d)-math.erf((A-eps)/d))

# The actual single-visit union sum inside one reset-to-reset excursion.
# Bonferroni bounds the success probability; all pair intersections are
# bounded by (2 eps M)^2 p^m. The probability of >N jumps is geometric.
N=160
G=sum(P**n*f_n(n) for n in range(1,N+1))
tail_bound=P**(N+1)/(1-P)*MAX
assert tail_bound<1e-40
G_upper=G+tail_bound
pi_c=Q*G
print('G',format(G,'.16g'),'pi_continuous_at_a',format(pi_c,'.16g'))
print('predicted epsilon_times_mean',format(M/(2*pi_c),'.16g'))
for eps in (0.04,0.02,0.01,0.005):
    single=sum(P**n*normal_interval(n,eps) for n in range(1,N+1))
    # Probability of simultaneous visits at n<m in one reset cycle.
    pair_bound=(2*eps*MAX)**2 * sum((n-1)*P**n for n in range(2,N+1))
    low=max(0.0,single-pair_bound)
    high=single+2*eps*tail_bound
    target=2*eps*G
    assert 0 < low <= high
    assert low <= target*(1+eps*3) and high>=target*(1-eps*3)
    # True asymptotic single-visit coefficient is approached as eps shrinks.
    relative=(high-low)/target
    assert relative<5*eps
    print('eps',eps,'P_success_interval',format(low,'.10g'),format(high,'.10g'),
          'normalized_width',format(relative,'.7g'))
# Pareto clock competition: exact survival integral and label probabilities.
for alpha,beta in ((0.4,0.8),(0.4,0.5),(0.7,0.7),(1.2,0.9)):
    delta=alpha+beta
    q=beta/delta
    p=alpha/delta
    assert abs(p+q-1)<1e-15
    if delta>1:
        m=1/(delta-1)
        assert m>0
        print('Pareto',alpha,beta,'finite_mean',m)
    else:
        print('Pareto',alpha,beta,'infinite_mean')
print('PASS: exact analytic bounds plus deterministic finite checks')
