# Scientific review: balanced-scroll Grassmann distance degrees

## Correctness — PASS

The result concerns the complex chordal-distance critical count with projector data constrained to the projection Grassmannian, not generic ambient symmetric data. The proof constructs legitimate rank-\(d\) projectors blockwise, proves the induced objective-numerator map dominates the full space of degree-at-most-\(2n\) polynomials modulo addition of a multiple of the denominator, and then applies base-point-free Bertini on \(\mathbb P^1\). It separately excludes the algebraic cut locus; the case \(d=1\) is intentionally excluded from that argument. The displayed determinant \(-4^{n+1}/5^n\) is nonzero for all permitted \(n\), and the denominator is squarefree. The standalone checker supplies independent exact finite examples but is not treated as a proof of the unbounded statement.

## Originality — PASS, subject to historical-priority risk

The closest direct paper is Friedman--Hoşten--Rosana, arXiv:2610.02018, Theorem 2.2, which provides the **ED** count for scroll ruling curves; the present claim concerns the **GD** count under projector-valued data. Its Theorem 4.4 describes expected low-dimensional ED/GD agreement but does not establish the needed dominance or cut-locus exclusion for balanced scrolls. The earlier Friedman--Rosana--Sturmfels arXiv:2601.22843 treats line Grassmannians and generic complete intersections but not these scroll ruling curves. Earlier results on the same ruling curves determine the stationary discriminant for unrestricted symmetric data and the monodromy of the cut divisor, respectively. Neither computes generic GD degree for rank-\(d\) projector data; restricting a discriminant to that nonlinear data variety does not preserve generic nonvanishing without the new dominance argument. A search cannot establish comprehensive priority; a specialized unindexed source remains a residual risk.

## Mathematical value — PASS

This gives the first explicit GD formula for a natural infinite family singled out by the motivating paper's ED computation, resolves the effect of a strong and geometrically meaningful data constraint, and shows that the critical-point count is independent of the number of ruling blocks. The rank-surjective two-block construction is a structural explanation, not simply a numerical substitution into the known ED formula. It does not solve the unbalanced or general-model GD problem.

Self-review: passed. Independent audit: not yet performed.
