# Independent mathematical audit

## correctness

PASS

For the rate-one-per-neighbor CT symmetric lattice walk, the killed-free resolvent is G_r(m,0)=q^m/Delta, G_r(0,0)=1/Delta, Delta=sqrt(r(r+4))=(1-q^2)/q. Rank-one reaction yields f_kappa(r)=kappa q^m/(kappa+Delta), and first-reset renewal gives T=(1-f)/(rf)=(1+q+kappa sum_{1..m}q^j)/(kappa q^m(1-q)). Independent exact differentiation checked the polynomial P_{m,0}+kappa P_{m,1} for m=1..7 and rational q, kappa. Its ordered coefficients have one sign change, while P(0)<0<P(1), establishing exactly one simple minimum over all r>0. U_m/V_m increasing and P signs give q_infty<q_*<q_0 and dq_*/dkappa<0; since dr/dq<0, strict positive reactivity response follows. For m=1, solving the quadratic gives r_*=(kappa+2)/(1+sqrt(kappa+2))~sqrt(kappa); for m>=2 the unique perfect-trap root lies in (0,1). Finite checks only corroborate these full quantifier proofs.

## originality

PASS

Best-of-knowledge: the exact partially reactive lattice mean is explicitly known via Das–Giuggioli, and the perfectly absorbing nearest-neighbor infinite-rate optimum is known via Hartmann–Majumdar. The scoped addition is the nontrivial all-distances global uniqueness, strict monotonic increase of the unique optimal reset rate with reaction strength, and a singular sqrt(kappa) boundary layer for the adjacent case. Neither inspected primary paper states this complete lattice finite-reactivity optimization classification.

## value

PASS

The infinite- versus finite-optimal-reset paradox for the nearest-neighbor trap is a natural physical boundary question, not an arbitrary parameter slice. The exact uniqueness/strict reactivity-monotonicity for every starting distance and singular sqrt(kappa) limit quantify how imperfect reaction regularizes the perfect-trap pathology. These are structural optimization facts beyond simply substituting a known mean formula.

The dated certificate retains the supplied scientific assessment, sources and limitations.
