# Scientific review of the paired Fermat-quotient theorem

## Correctness — PASS

The original full-period quotient map decomposes exactly into \(p-2\) affine lines via the elementary lift congruence \(q_p(w+pt)=q_p(w)-t/w\pmod p\). Different base residues give distinct nonhorizontal, nonvertical directions of slopes other than one. The Fourier phase formula follows from the unique line annihilated by each frequency away from the three zero sets. For \(m\ge2\), constant words of lift directions have one-dimensional rank, while every mixed word has rank two: these are exhaustive disjoint cases and yield exact pointwise counts, including when \(p\mid m\). Fourier Parseval proves the energy formulas, and a cardinality argument proves that the minimum two-sum count is achieved. The boundary \(p=3\) is explicitly excluded from the two-sum coverage claim. The checker verifies 33 prime/shift cases, but the argument, not those finite cases, covers all primes and all eligible shifts.

## Originality — PASS, with historical risk

The basic Fermat-quotient lifting identity was already standard (Ostafe–Shparlinski 2010); no novelty is assigned to this lemma. The inspected archival literature addresses short-interval distributions, scalar Waring numbers, or pseudorandom scalar-subset estimates. None of their materially read statements covers the joint **full-period** Fourier amplitude-and-zero classification or the complete **pointwise** sum representation law and all even energies. A related higher-precision *image-size* result is relevant but does not assert or imply these additive statistics merely from its image counts. Searches for aliases including simultaneous quotients, correlated spectra, affine-line decompositions, twofold sumsets, and Waring problems located no decisive covering theorem. Unlocated historical work remains a genuine risk, not a proof of uniqueness.

## Mathematical value — PASS

Joint digit-level Fermat-quotient distributions are natural arithmetic pseudorandomness objects. The theorem determines an entire family of additive invariants for all odd primes and distinct shifts, showing simultaneously three zero-frequency directions, exact even moments, and the striking sharp two-sum basis phenomenon (a sparse union of affine lines already sums to the full plane). The input restriction and the exceptional prime are structurally necessary. This is a substantive complete classification rather than a numerical extension of a table.

## References and limitations

- Ostafe–Shparlinski, arXiv:1001.1504 (2010), source of the standard lifting identity and related short-interval joint-distribution questions.
- Shparlinski, arXiv:1104.3909 (2011), single-output Fermat quotient value sets.
- Chen–Winterhof, arXiv:1402.1913 (2014), scalar quotient Waring numbers for inputs in intervals of length at most \(p\).
- Liu–Zhang, DOI:10.5486/PMD.2019.8222 (2019), pseudorandom subset and correlation estimates.

All computations are bounded corroboration; the claimed arbitrary-prime theorem relies on the fully written proof. Independent audit and historical-priority certification were not performed.

Self-review: passed. Independent audit: not yet performed.
