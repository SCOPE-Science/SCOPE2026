# Self-review of the first-order two-stage parking correction

## Correctness — PASS

The statement fixes the short length, takes the infinite-substrate limit first, and concerns only sequential Model I. The argument reconstructs a finite-interval renewal recurrence and solves its generating function exactly; the resulting boundary constant is \(-s(1-p_s)\). The first-stage gap integrals and both gap-sum identities follow from the cited primary model. An explicit small-gap bound makes the sum of finite-size errors negligible at order \(k^{-1}\). Finally, Euler–Maclaurin gives the local part of the continuum correction, while the geometric series near scaled distance \(x\asymp k\) gives a **separate negative boundary-layer contribution**. All limiting exchanges are controlled by the stated bounds. Exact-enumeration and quadrature checks support, but do not replace, these proofs. Risk: the asymptotic coefficient would be wrong if one discarded the large-distance tail.

## Originality — PASS under checked evidence

Pinsky (2026), Theorems 4 and 6, supplies an integral representation and the limiting staged coverage but not the inverse-long-rod correction. Klaassen–Runnenburg (2001/2003) addresses joint fixed-rod gap fluctuations, not this two-scale problem. The previously known single-rod continuum correction alone cannot determine the staged correction, which also requires the finite-interval boundary constant and a uniform gap-error estimate. A published result on gap-mass monotonicity compares a different functional. Searches also covered two-size adsorption, asymptotic rates and equivalent formulations. Residual risk: a specialized or unindexed deposition-asymptotics paper could contain the same inverse-length formula.

## Value — PASS

The known staged limiting density does not indicate the rate or side of convergence. The explicit positive coefficient proves eventual below-limit approach for every fixed short-rod length, and isolates a universal finite-gap penalty. This is relevant to continuum approximation of sequential multi-scale packing and supplies asymptotic evidence (without claiming a full proof) for the known monotonicity conjecture. It is a first-order structural correction for a natural family, not a chosen isolated numerical instance.

## Closest literature and scope

- R. G. Pinsky, *A new look at some aspects of one-dimensional random sequential adsorption and its continuum limit*, arXiv:2608.04730, esp. Theorems 1, 2, 4 and 6.
- C. A. J. Klaassen and J. T. Runnenburg, *Discrete Spacings*, arXiv:math/0112056, Theorem 1.1, on fixed-length gap-count normal limits.
- Classical continuum parking and single-length lattice asymptotics, used and explicitly distinguished from the two-stage correction.

The theorem does not establish all-length monotonicity, a growing-short-rod regime, or the simultaneously competing model. Independent mathematical verification has not been performed.

Self-review: passed. Independent audit: not yet performed.
