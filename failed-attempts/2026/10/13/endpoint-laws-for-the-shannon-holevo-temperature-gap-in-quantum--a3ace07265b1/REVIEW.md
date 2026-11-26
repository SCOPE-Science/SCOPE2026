# Independent mathematical audit

## correctness

PASS

The stated inverse-temperature boundary formulas and asymptotics are correct. Substituting the BSC and pure-state channel capacities into the unit-coupling noise map gives the two formulas, with beta_q=atanh(1-2q_R) on the specified branch. For small u, writing t=log(1/h_2^{-1}(u)) gives t=log(1/u)+log t-log(log 2)+o(1), hence t=log(1/u)+log log(1/u)-log(log 2)+o(1). At the other entropy endpoint, 1-h_2(1/2-d)=2d^2/log(2)+O(d^4). Using these and the two endpoint expansions of asech gives the high-rate ratio sqrt(log(1/(1-R))/2) and the low-rate difference (log log(1/R)-log 2)/2+o(1), with low-rate ratio 1 in the limit. The proof is analytic; artifacts/verify.py was inspected, not run, and finite bisection checks are not asymptotic evidence.

## originality

FAIL

The exact unit-coupling capacity-boundary curves are already specified by the primary source. The two endpoint laws are direct asymptotic corollaries of those curves, using only the standard local expansions and inversion of binary entropy. This is prior coverage by implication, not a finding that the source explicitly states the two endpoint comparisons.

## value

FAIL

The multiplicative versus additive comparison is an explanatory way to present the known capacity curves, but here it is obtained by routine endpoint expansions of those exact curves. It is not an independently useful unknown boundary or a new decoding regime, and resolves no achievability question. The low-rate divergence is in inverse temperature, not a divergent difference in physical temperature.

The dated certificate retains the supplied scientific assessment, sources and limitations.
