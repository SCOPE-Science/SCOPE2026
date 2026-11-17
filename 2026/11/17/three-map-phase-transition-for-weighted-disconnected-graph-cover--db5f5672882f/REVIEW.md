# Scientific review

## Correctness — PASS
The final claim is the exact three-term operator-norm distance for the weighted union of one trivial sheet and a connected degree-\(d\) graph covering. The proof derives the total-variation overlap formula, separates all possible component allocations of three maps, proves the two matching lower bounds, constructs the one-fiber and two-distinct-fiber covering lemmas by guarded edgewise transport, and compares the resulting exact rational functions. In particular the two-distinct-fiber transition graph is connected for all \(d\ge2\), not merely for the checked finite degrees. The endpoint parameters \(w=0,1\) and the threshold \(w=d/(d+1)\) are included. The finite checker supports arithmetic and connectivity lemmas; no untested finite grid is substituted for the proof.

## Originality — PASS, with residual bibliographic risk
The relevant 2026 primary source [1] proves sharp \(m\)-term distances only for one connected, uniform-degree covering. A publicly accessible research record [2] gives a formula for **two** maps on general componentwise weighted disconnected coverings and explicitly excludes three or more. Neither statement implies the new three-map mixed-covering phase diagram: three maps support two different protected fiber points while a third moves, leading to a mass-dependent switch between component allocations. Published-record and mathematical literature searches showed no equivalent result. Searches cannot prove novelty, and older Markov approximation literature not read in full remains a priority risk.

## Mathematical value — PASS
The exact first three-term case after the two-term disconnected-covering classification is a natural finite-resource Markov approximation invariant. The phase boundary \(w=d/(d+1)\) distinguishes two competing and attained topological strategies, while \(d=2\) has an entire constant-error plateau. The theorem holds for every connected finite graph cover of any degree and yields a structural transport lemma rather than a one-off scalar example. The result does not assert higher-budget generality or uniqueness.

## Closest literature and limits
[1] H. Duru, S. İlter, A. Bilgin, *Sharp Norm Approximation of Covering Markov Operators*, arXiv:2610.35575v1 (2026-10-26), https://arxiv.org/html/2610.35575v1.

[2] *Exact two-map approximation of componentwise-weighted disconnected covering averages* (public record, 2026-11-08), https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-exact-two-map-approximation-of-componentwise-weighted-disconnect--25459b8578e0.

[3] J. R. Brown, *Approximation theorems for Markov operators* (1966), and [4] K. C. Kim, *Approximation theorems for Markov operators* (1972), are older bibliographic risks; their full contents have not been checked against the quantitative phase law. The theory remains limited to a single identity component, one connected nontrivial covering, and three composition maps.

Self-review: passed. Independent audit: not yet performed.
