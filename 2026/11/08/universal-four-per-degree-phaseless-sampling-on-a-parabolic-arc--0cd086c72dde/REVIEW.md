# Self-review

## Correctness — PASS

The proof is a complete identity-and-rational-functions argument for every integer \(d\ge1\), not an induction inferred from numerical tests. The intensity polynomial has degree at most \(4d\) with absent \(T^{4d-1}\) term. Its exact interpolation determinant is the sum of the nodes times the Vandermonde product. If two nonzero polynomial intensities coincide, their rational quotient pulled back to the parameter variable is invariant under both \(T\mapsto i-T\) and \(T\mapsto-i-T\), hence under nonzero translation \(T\mapsto T+2i\). Rational periodicity forces a constant global-phase quotient. The zero signal and all lower-degree cases are covered. In degree one, zero-sum nodes yield a nonzero indefinite Hermitian form in the evaluation kernel, hence a genuine ambiguity. Compactness establishes fixed-node stability. A standalone symbolic checker independently computes exact finite cases and a boundary witness; it is supplementary evidence only.

## Originality — PASS, historical priority provisional

Pohl–Li–Boche (2017, presentation slides 13--18) give another four-per-degree design, but use two concentric circles and do not imply arbitrary nodes on one parabolic arc. Przybyłek–Siedlecki, arXiv:1907.09371, Theorem 4.2, use \((2d+1)^2\) magnitude samples over multiple circles, not arbitrary nodes confined to a single parabolic arc. Liehr, arXiv:2308.05722, Theorem 1.1, treats unions of parallel lines in classes of entire functions. Chalendar–Partington, arXiv:2403.16255, Theorems 2.1 and 2.11, concern intersecting lines or circles, not the present universal finite-node claim. Existing accessible phase-retrieval findings using two rays or two circles have different measurement geometries and do not logically imply the single-arc theorem. Searches for parabola, intensity interpolation, and equivalent Hermitian-nullspace statements returned no result covering this exact theorem. A broader algebraic-curve result could still cover it, so originality is a provisional literature judgment, not a proof of historical priority.

## Mathematical value — PASS

The theorem gives a deterministic, all-node configuration criterion for a natural single-sensor-curve polynomial recovery problem. It reduces a quadratic-size multidimensional polar-grid intensity construction to \(4d\) phaseless evaluations without placing the nodes on multiple curves, proves an exact linear intensity recovery step, and identifies a sharp necessary constraint in the first nontrivial degree. The statement is stronger than genericity; arbitrary short positive parabolic arcs also qualify. Such a design is relevant to spectral interpolation and structured phase retrieval, while finite-node conditioning requires careful sensor placement.

## Limitations and closest literature

The sum constraint is not known to be necessary for higher degrees. Minimality and efficient coefficient-phase factor assignment are not established. Stability is only fixed-design, not uniform for clustered nodes. The cited 2019, 2023, and 2024 primary texts were examined in the relevant sections. No independent mathematical audit or broader generalization is asserted.

Self-review: passed. Independent audit: not yet performed.
