# Scientific review

## Correctness — PASS

The object is a simple positively weighted cycle with at least two fixed terminals, and deletion size rather than deleted length is counted. For each consecutive terminal pair, the clockwise terminal gap is a shortest path precisely when its total weight does not exceed half of total circumference. Necessity requires one deleted edge in each such gap. Sufficiency uses the fact that every simple terminal-terminal path is a union of entire consecutive gaps, while at most one gap can weigh more than half the circumference; its solitary arc is strictly longer than the complementary route. Independent selection in each mandatory gap gives the exact polynomial and its leading coefficient. Cyclotomic factorization proves the complete complex-root description; Toeplitz total-positivity and convolution prove log-concavity of the positive support. The boundary equality case and the exceptional nonseparating optimum are addressed explicitly. Exact independent shortest-path enumeration passed 340,304 unweighted and 333,120 positively weighted terminal/deletion comparisons; these finite computations are corroboration only.

## Originality — PASS, historical priority provisional

Bosek, Serra and Vena, *Structural properties of semi-cutting sets* (arXiv:2611.20287v1, first public 2026-11-15) define the notion and prove the sharp general lower bound, but the inspected primary text does not state or imply the all-cardinality terminal-gap factorization for arbitrary weighted cycles. Their theorem gives a one-sided inequality, not the necessity-and-sufficiency threshold, exact number of optimum sets, real-rootedness boundary or cyclotomic root geometry. Manuel, Brešar and Klavžar, *The geodesic-transversal problem* (arXiv:2101.08042), use vertices to hit maximal geodesics, a different quantified family. The relevant published mathematical-record matches also concern vertex geodesic transversals or maximal-geodesic edge transversals of other graph families, not fixed-terminal edge-disruption spectra. Search failures are not regarded as a uniqueness proof; unindexed literature and possible general hypergraph-transversal reformulations remain historical-priority risks.

## Value — PASS

The motivating recent work explicitly asks for structure of equality cases and minimum semi-cutting sets. The theorem answers those questions completely on the natural cycle family for *every* terminal position and even for arbitrary positive edge lengths. It identifies precisely when the universal \(|T|-1\) bound is achieved versus a stronger \(|T|\) requirement, distinguishes distance-increasing nonseparating deletions from terminal multiway cuts, counts every feasible deletion cardinality, and deduces a cyclotomic zero locus and log-concavity. This is a natural classification and is not a computation on an arbitrarily chosen tiny graph or parameter slice.

## Closest literature and scientific limitations

- Bartłomiej Bosek, Oriol Serra, Lluís Vena, *Structural properties of semi-cutting sets*, arXiv:2611.20287v1, https://arxiv.org/pdf/2611.20287 . Theorem 4.1 and Lemma 2.6 are foundational; no terminal-gap spectrum is stated in the inspected sections and references.
- P. D. Manuel, B. Brešar, S. Klavžar, *The geodesic-transversal problem*, arXiv:2101.08042v1, https://arxiv.org/pdf/2101.08042 . Its maximal-geodesic vertex-hitting object differs from fixed-terminal shortest-path edge transversals.
- Sylvain Guillemot, *FPT algorithms for path-transversal and cycle-transversal problems*, *Discrete Optimization* 8 (2011), 61–71, https://doi.org/10.1016/j.disopt.2010.05.003 . Generic path systems and algorithmic transversals are related, but no equivalent marked-cycle cardinality spectrum was located in accessible material.
- Earlier published studies of cycle geodesic-transversal spectra are related but count vertex hitting sets for a different path family; the accessible search summaries do not certify full-document noncoverage.

Risks: an earlier indexed or unindexed shortest-path edge-transversal treatment might contain this special family under another name; that possibility has not been eliminated. The proof assumes strictly positive edge lengths and does not address weighted deletion costs or arbitrary topology.

Self-review: passed. Independent audit: not yet performed.
