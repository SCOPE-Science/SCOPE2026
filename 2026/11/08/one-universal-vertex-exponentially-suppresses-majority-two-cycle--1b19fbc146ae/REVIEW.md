# Review of the complementary-pair majority classification

## Correctness — PASS

The proof checks the full two-state update including all ties. For the even-order graph, the balanced binomial layer is exactly periodic and everything else reaches unanimity after one update. For the odd-order graph, the first update homogenizes each complementary pair; if the resulting total weight is \(n\) or \(n+1\), the configuration lies on an exact two-cycle, otherwise it reaches unanimity after a further update. A direct vertex-by-vertex enumeration through \(n=8\) checks all \(262128\) labelled initial states and the separate weighted pair-type program checks \(n=2,\ldots,60\). Computation is not used as an infinite proof. Central binomial asymptotics give the ratio of immediate-two probabilities.

## Originality — PASS, with priority reservations

The 1980 symmetric-threshold period-two theorem establishes possible eventual periods, not labelled periodic-point populations. Tamuz and Tessler's 2013 preprint, particularly its Section 3.7 complete-bipartite one-edge-deletion block, and Benjamini et al.'s 2014 full text consider different graph families and general convergence/oscillation rather than the complementary-pair census. The accessible three-part majority formula already covers the smallest \(K_{2,2,2}\) instance. The all-\(n\) formula and the exponential effect of a singleton part are not logically implied by those statements. The 1980 original paper's full text was not inspected; equivalent results under graph aliases may be unindexed. Neither search silence nor the partition of research topics is treated as proof of uniqueness.

## Value — PASS

The cross-polytope skeleton is a natural dense, highly symmetric graph. Its universal one-vertex extension is a minimal perturbation. The exact loss of immediate two-cycle probability by a factor asymptotic to \(\sqrt2\,2^{-n}\) is a substantive dynamical robustness phenomenon, and the formulas simultaneously classify all immediate periodic states and certify sharp uniform transient bounds. The scope is limited to these two graph families and the specified tie rule; no general basin distribution is claimed.

## Closest literature and limits

Goles–Olivos (1980), *Periodic behaviour of generalized threshold functions* (DOI 10.1016/0012-365X(80)90121-1); Tamuz–Tessler, arXiv:1307.4035; Benjamini et al., arXiv:1405.2486. Only the Goles–Olivos abstract was available for material inspection. Self-review is not an independent check, and historical-priority risk is retained.

Self-review: passed. Independent audit: not yet performed.
