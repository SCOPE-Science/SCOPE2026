# Scientific review

## Correctness — PASS

The statement specifies four candidates, three positions, nonempty ballots, all greedy tie branches, the Kelly extension, and the electorate-size range. The recurrence in `RESULT.md` enumerates every greedily reachable set, and integer marginal weights scaled by six are exact because the only denominators are one, two and three. Every anonymous multiset profile appears exactly once among \(\binom{n+14}{14}\) multiplicity vectors and each occupied ballot-type deletion is exhaustively checked. Running `verify.py` produced 170543 profiles and 813960 such deletion tests, identified twelve seven-voter paradox profiles and zero through six voters, and verified a single symmetry orbit. An independent exact-rational recursion agreed in 5075 selected cases. The explicit representative's scores and winning sets were also checked directly. There is no inference from a partial enumeration: the whole finite domain was enumerated by construction. The generalization beyond this finite domain remains unproved.

## Originality — PASS, subject to literature-priority uncertainty

Bullinger et al. (arXiv:2312.08798v1, Theorem 2, Corollary 1, Remark 1) prove general existence of sequential-rule participation failure and the boundary at committee size two; this entails that failure is possible for some instances with three seats, but not that seven voters are minimal or that all four-candidate minimal profiles form the enumerated twelve-element orbit. Their construction uses general profiles and does not provide the claimed finite census. Sánchez-Fernández and Fisteus (arXiv:1710.04246) investigate support-monotonicity and give different, larger examples; Lackner and Skowron (2023, Proposition A.3) analyze related sequential-rule monotonicity, not this exact Kelly no-show census. Relevant mathematical-record comparisons involved no-show, committee, Thiele and participation aliases and identified only distinct single-winner records, not a covering statement. This negative search is not proof of priority: inaccessible or unindexed equivalences remain possible. The precise comparison and residual risks are in `AUDIT.json`.

## Value — PASS

An initial impossibility theorem leaves unanswered the smallest electorate at which its phenomenon can occur in the smallest natural three-seat, four-candidate committee cell. The proved seven-voter threshold, one-orbit structure and exact incidence \(12/116280=1/9690\) quantify that boundary and identify the specific tie mechanism responsible. This is a motivated complete finite classification, not an arbitrary parameter slice or routine rephrasing of non-participation. It informs minimal-counterexample testing and participation robustness for irresolute multiwinner rules. The result is limited in scope and does not claim a general theorem for larger committees or fixed tie-breaking.

Self-review: passed. Independent audit: not yet performed.
