# Self-review

## Correctness — PASS

The vertex-mask multiplicity is exactly the count of perfect matchings on the covered set, yielding odd double factorials. Gaussian even moments reproduce these integer weights without a limiting approximation. The centered-chi-square moment generating function has only positive nonconstant coefficients after order one, establishing \(a_j>0\) for every \(j\ge2\). Expansion in even Gaussian powers then proves the exact nonnegative formula for every Fourier multiplier and isolates precisely \((q,d)=(1,0),(1,1)\) as the zero cases. Binomial alternating-sum identities prove the full inertia. The independent finite checker passed 11,014 exact assertions; the infinite claims rest on the written proof, not the checker.

## Originality — PASS under bounded comparisons

The reviewed 2004 Wagner manuscript, its 2008 rewrite, and Drake's 2009 complete-graph Hermite treatment supply and analyse broad matching polynomials, but they do not explicitly give the \(\pm1\) vertex-coverage sign classification, the exact zero list, or the convolution inertia. The Heilmann–Lieb nonvanishing region used by Wagner excludes the mixed negative-real assignments in the claim; Drake's Hermite moments and orthogonality do not by themselves state the fixed-sign expansion (1). A semantically targeted search of existing mathematical findings found related all-matching *edge*-incidence Walsh results, including complete-graph and \(K_{3,n}\) cases, but not the *covered-vertex* counting kernel or its inertia. The result is a genuine specialization of known enumerative objects, so priority is qualified: an unindexed multivariate identity explicitly evaluated on \(\pm1\) assignments could cover it.

## Value — PASS

The covered-vertex mask is the canonical sufficient statistic recording which vertices participate in a partial matching, and its weight distribution is nontrivial because many matchings share one mask. The theorem characterizes exactly when this loss of edge information still permits invertible Boolean counting convolution and supplies the complete real spectral inertia at every large dimension, including a balanced-sign law at even orders and a central-binomial imbalance at odd orders. These are structural all-order facts that do not follow simply from the total matching count or polynomial real-rootedness. No stronger conditioning or extension beyond complete graphs is claimed.

## Primary literature and residual risk

- Wagner, arXiv:math/0412059, 2004: degree-constrained subgraph enumeration and matching real-rootedness; reviewed Introduction and matching statements.
- Wagner, arXiv:0803.1659, 2008: multivariate matching polynomial, Section 3 and Example 4.1; the positive half-plane is not the mixed-sign cube.
- Drake, arXiv:0909.1655, 2009: Sections 1 and 5, complete graph, Hermite, Gaussian moments, and generating functions; no covered-mask inertia comparison in inspected passages.
- Residual risk: overlooked direct sign-evaluation corollary in the wider matching-polynomial literature, including non-indexed source material. No independent audit has been performed.

Self-review: passed. Independent audit: not yet performed.
