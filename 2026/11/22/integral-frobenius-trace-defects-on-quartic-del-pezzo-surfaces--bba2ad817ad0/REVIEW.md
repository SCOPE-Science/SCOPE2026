# Self-review

## Correctness (C): PASS

A six-dimensional integral intersection lattice and all sixteen exceptional classes are defined explicitly, including signs and a canonical-class test. Five root reflections generate exactly \(1920\) distinct Weyl permutations; exhaustive conjugation yields eighteen classes. For each class an integer orbit-sum matrix has precisely the fixed-lattice rational rank. The fixed kernel is saturated, so the gcd of all maximal minors computes its **exact** index. An independently organized symbolic Smith-normal-form spot check gave the same index spectrum. All exact checks are reproducible from the attached standalone Python implementation and eighteen-row CSV; finite experiments are not used to infer an infinite statement. The geometric effective-cone step uses finite group averaging.

## Originality (O): PASS, with residual risk

The closest mathematical source is A. Trepalin, *Del Pezzo surfaces over finite fields*, arXiv:1803.07421, whose degree-four eighteen-class table gives conjugacy classes, eigenvalues and invariant ranks, but no integral orbit-trace saturation index. Blache–Hallouin, arXiv:2301.13582, discuss Weyl types and zeta functions without this integer-index classification. An existing degree-five Frobenius-trace lattice result addresses an inequivalent root lattice \(A_4\); a sixteen-line boundary Picard-torus result concerns an entirely different scheme. Crucially, two types with the same invariant rank and identical finite line zeta data have indices two and four; no rational-character or line-permutation table can itself imply the index. Residual risk: an unindexed older integral Picard-lattice calculation may have given an equivalent conclusion.

## Mathematical value (V): PASS

The exact finite-index defect is a natural arithmetic geometric invariant: it measures how far rational divisor classes built from exceptional-curve orbit traces are from being an integral basis of the whole arithmetic Picard lattice. The classification reveals maximal defect sixteen and a structural failure of any reconstruction from the exceptional-line zeta function, even after supplying Picard rank. This is not a restatement of a known rational representation or a narrow arbitrary computational slice.

## Limits

The result classifies all possible Frobenius types but does not claim all types occur over each small field. It classifies integer span, not the semigroup of effective rational divisors. The exact program is a mathematical certificate of finite exhaustion, not an independent audit.

Self-review: passed. Independent audit: not yet performed.
