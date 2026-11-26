# Independent mathematical audit

## correctness

PASS

Writing the grounded matrix as a block diagonal matrix with blocks d I+J_{f_i} minus the global all-ones matrix gives within-part zero-sum modes at d and the part-constant block diag(d+f_i)-uu^T, u_i=sqrt(f_i). Padding the empty parts by the eigenvalue d is exactly canceled by (F-r)/d. Each f_i/(d+f_i)<=1/r, with a strict inequality in at least one part, so the rank-one inversion denominator is positive. For a fixed pair sum s, set B=(d+x)(d+y), T=2d+s, U=4d+s, c=1+S_0. Then the pair reciprocals sum to T/B, its contribution to G is (UB-dT^2)/B^2, and 1-S=(dT-cB)/B. Combining gives the stated linear fraction and its derivative numerator G_0 dT+c(U-cT). Since U-cT=2d-S_0T>=2n, this is strictly positive also at admissible boundary counts. Every unequalizing transfer from y<=x changes xy by epsilon(y-x)-epsilon^2<0. Such transfers reach a bound and reduce the number of interior counts until the canonical profile is reached. This gives both directions of the optimizer classification; part permutation symmetry is the only freedom in counts. Standard pair transfers also give strict Schur-concavity on the fixed-sum slice. The t=0 padding and one-follower cases agree with substitution in the closed formula. An independent exact check of 289 allocations, including every budget for four parameter pairs, compared the trace with ratios of grounded determinants and principal cofactors and recovered exactly the specified minimizers. Replay: python3 /tmp/opencode/balanced_leader_audit.py. The analytical comparison, not these cases, proves the unrestricted theorem. The O(r) claim counts rational operations, not bit complexity.

## originality

PASS

Best of knowledge: no inspected equivalent or stronger result gives the all-budget optimizer classification and strict transfer for arbitrary r>=3 equal-sized parts. General exact formulas specify the criterion, not this optimizer; the nearest graph-family results either use other graphs or give only two parts or two leaders. World priority is not established.

## value

PASS

The result classifies every optimal placement for all budgets on a standard infinite class of community graphs, rather than producing a bound or one candidate. It gives a counterpoint to spacing-based rules on paths and cycles: concentration in whole parts is strictly better than any noncanonical count vector. The all-size pair comparison, equality classification, and exact cost give a reusable benchmark for selection algorithms on this family.

The dated certificate retains the supplied scientific assessment, sources and limitations.
