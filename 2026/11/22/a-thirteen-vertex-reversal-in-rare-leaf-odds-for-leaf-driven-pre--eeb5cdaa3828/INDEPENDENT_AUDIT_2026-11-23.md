# Independent mathematical audit

## correctness

PASS

After the deterministic size-three start, each degree-one vertex has weight a and each leaf contributes one unit to total leaf-neighbor weight; the hold probability is ak/(k+an). For t=2/a, division of the two lowest mass recurrences gives R_{n+1}=3(n+t)R_n/(2n+3t)+(n-2+t)/2. Independent sparse-integer polynomial arithmetic exhaustively checked the derivative numerators for n=4..12 (degrees 2,4,...,18; minima positive from 18 to 457019805007872). Exact fractions give R_13(t=4)-R_13(t=2)=-15421/26112 and R'_14(0)=-696574397/164003840; replay: /workspace/branches/fa4fadcd-c51a-40bc-b2b9-7890a411c7f0/bounded_reproduction.py. In the endpoint derivative recurrence q_{n+1}=3q_n/2+1/2-3r_n/(4n), the r_7=131/16 base and r recursion give r_n>=n from n=7, propagating negativity for n>=14. For each fixed n the odds are rational with linear large-t term (n-3)t/2, hence derivative tending to (n-3)/2. This both rules out monotonicity in either direction at n=13 and gives the opposite endpoint derivative signs at n>=14 after reversing the parameter. The common-uniform coupling preserves order because upward probability decreases in a at equal counts and unit increments cannot cross one-step. Positive-probability size-four separation can persist by common holds. The adjacent probabilities at 2 and 3 directly violate the likelihood-ratio inequality at the two witness offsets. The supplied checker was inspected, not executed; no full small-size likelihood-ratio order is concluded.

## originality

PASS

Credit prior introduction of the tree model and the exact count-chain transition, from which the ordinary stochastic ordering is a short elementary corollary. The supported distinct finding is the exact all-offset finite-size cutoff for two-versus-three-leaf odds and the persistence of nonmonotonicity at every larger size. The strongest comparisons inspected concern asymptotic fluctuations, other leaf-count models, or general order criteria; they do not supply the cutoff or the derivative signs.

## value

PASS

A growth parameter orders every increasing leaf-count risk but fails to order even the adjacent odds of the two minimal nonzero populations at a precise onset size. This is an all-parameter/all-size separation of two practically and mathematically different orders, not a lone reversed sample or an arbitrary isolated finite enumeration.

The dated certificate retains the supplied scientific assessment, sources and limitations.
