# Independent mathematical audit

## correctness

PASS

With independent fresh attempts and rate r, a fresh attempt at site i succeeds with probability p_i and has mean duration (1−p_i)/r, including an infinite reset-free arrival time. A geometric bound on the probability of reaching each attempt (using min(a,b)>0) gives finite total mean. For x=1−a, y=1−b and d=bx+ay=a+b−2ab, inversion of the two renewal equations gives Δ=ab+cd and M=(d+4cxy)/(2rΔ). The identity d²−4abxy=(bx−ay)²=(a−b)² gives the derivative including its strictness. Subtracting at c=1/2 and 1 using Δ_(1/2)=(a+b)/2 and Δ_1=a+b−ab gives the exact gain. Uniform initialization preserves the unconditioned pre-generated chain marginal, including at c=0 where uniform need not be the unique invariant law; the surviving marginal is not asserted equal. The ring boundary-value problem D u″=r u with unit data at both absorbing ends gives the stated cosh ratio, so equality of transforms holds exactly for coincident or reflected sites. An independent numerical evaluation gave 0.105246747557, 0.102741917381, 0.101382055515 for the three reported protocols. The frozen symbolic, rational and killed-generator test code in verify.py was inspected, not executed; the derivation, rather than the tests, establishes the arbitrary renewal claim.

## originality

PASS

Pass for the distinct exact dependence and strict ordering across the entire symmetric two-site Markov family with fixed uniform initialization, and its quantitative specialization. The iid Brownian-ring baseline is known. The same-day cycle-vs-iid work is material overlap at the endpoints and should temper any claim that the alternation-vs-iid comparison alone is new; no verified coverage of the full interpolation was found.

## value

PASS

At fixed clock rate and fixed proposed one-index site distribution, the result isolates the influence of serial correlation and provides its exact sensitivity, optimizing protocol and strictness criterion for any renewed attempt law. It is not an optimization achieved by changing the sites or their marginal weights. The result concerns only the mean in this family, not optimality over general reset schedules or a full distributional order.

The dated certificate retains the supplied scientific assessment, sources and limitations.
