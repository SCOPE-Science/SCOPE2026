# Independent mathematical audit

## correctness

PASS

Forced consecutive blocks are full components, so different occurrences have disjoint supports. Each specified orientation on a four-site block gives a unique reinsertion into each unrestricted pair of remaining matchings. Laying out labeled intervals of lengths 2 and 4 and distributing the remaining vertices in gaps gives (2n-4)(2n-5) mixed placements, exactly the displayed expression; the two equal-length counts follow by the same argument. Exact rational algebra (python3 /workspace/evidence/5_covariances.py) reproduced both finite covariance formulas, positive shifted numerators at n=4+x, and all covariance and concentration limits. Independently switching each four-site block preserves outside arcs, all supports, and the uniform measure. Thus conditioning on information invariant under every such switch gives independent fair signs, not unconditional independence of the two counts. Since Y_n/n tends to 1/64 in L^2, the conditional characteristic function of D_n/sqrt(n) tends boundedly in probability to exp(-s^2/128). Multiplying by the short-loop phase and using Janson–Thévenin Eq. (3.8) establishes exactly the independent signed bivariate limit; it does not require a full three-dimensional CLT. The frozen finite checker was inspected, not executed.

## originality

FAIL

The marked statement is not verbatim in the strongest inspected Resultary record, but its decisive content is mechanically implied by that record's unrestricted deletion/reinsertion for each orientation, full joint factorial-moment array, and joint unsigned Gaussian law. This is demonstrable current-corpus coverage by a distinct work, not an assertion of historical priority or copying. The 2023 Janson–Thévenin paper alone does not provide that coverage.

## value

FAIL

The marked-versus-unmarked distinction is meaningful, and the exact conditioning has a useful interpretation. But in the inspected coverage every mark assignment is already a free local completion, and the unmarked array and Gaussian law are known for the same counts. The residual computations merely unfold those completions into binomial moments and the immediate Gaussian projection; no independent obstacle or surviving nonmechanical invariant is supplied. A full vector theorem for other shapes is not part of the frozen claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
