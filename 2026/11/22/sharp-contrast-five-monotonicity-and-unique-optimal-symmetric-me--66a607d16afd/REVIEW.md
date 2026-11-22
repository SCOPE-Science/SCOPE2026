# Self-review

## Correctness — PASS
The natural second-derivative matching equations have determinant \(D=(r+2)(3r+2)>0\). Direct differentiation gives all three cardinal derivative coefficients, including their coefficient-sum normalization. The global uniform-in-data problem reduces to the exact largest negative-coefficient mass \(N_* = \max\{1/(r+2),r/[2(r+2)]\}\). The proof bounds each outer and central interval for all real \(r>0\), gives attaining points, and constructs strictly increasing counterexample data for any greater ratio. Its two branches meet uniquely at \(r=2\). A stand-alone exact-rational verifier passed 5,050 supplementary tests, but the universal quantifiers are proved algebraically, not inferred from tests.

## Originality — PASS (provisional priority)
The closest exact four-knot natural-spline literature checked in full optimizes continuous-versus-discrete **total variation** (record `a68c76ffcd7c`) or computes its equispaced norm (record `287732549e93`); neither quantifies the uniform monotonicity-preserving positive-slope-contrast radius. A clamped-zero-first-derivative four-knot contrast result differs in boundary conditions. Published Fritsch–Carlson local Hermite positivity criteria, Aràndiga–Baeza–Yáñez monotone reconstruction methods, Baeza–Yáñez endpoint-adjustment limitations, and Beatson–Chacko spline-boundary norm comparisons were cross-checked against statements and implications. No equivalent or dominating numerical radius \(R(r)\) or its exact symmetric-mesh optimum was located. Historical priority is not certified: more general classical spline criteria may conceivably contain the result as a corollary, and some older treatments remain unindexed.

## Value — PASS
The exact threshold is a robust shape-preservation design rule for the first naturally coupled cubic-spline geometry: the center-enlarged \((1,2,1)\) mesh provably tolerates slope contrast \(5\), compared with \(4\) on equally spaced knots. Sharp endpoint and central-pocket failure witnesses show that the gain is real and not an artifact of a loose sufficient condition. The assertion is limited to four knots with reflection-symmetric lengths, natural boundaries, and positive secant slopes; it neither gives a general pointwise data criterion nor extends to longer/asymmetric meshes.

## Sources and outstanding limits
Fritsch–Carlson (1980), Aràndiga–Baeza–Yáñez (2021), Baeza–Yáñez (2022), Beatson–Chacko (1990/1992), and two directly comparable published four-knot natural-spline results were examined at the scope described in `AUDIT.json`. Standalone exact arithmetic checked 5,050 diagnostic cases. Publication priority and the proof have not received independent external scrutiny.

Self-review: passed. Independent audit: not yet performed.
