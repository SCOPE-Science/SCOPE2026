# Mathematical review

## Correctness — PASS

The claim is about the intrinsic sum metric on the unit square flat torus and freely located, closed balls. The quotient-linear change of variables \(u=x+y\), \(v=x-y\) gives a fiber circle of length two and the necessary bound \(2rN(r)\ge\lceil1/r\rceil\) for \(0<r<1/2\). For the newly determined phases, the crucial upper bounds are independently checkable complete covers: `checker.py` exactly tests 128 and 72 rational triangles against integer translates of the four- and five-center diamonds. Every triangle has a single containing translated diamond, so convexity proves all continuous points covered, not merely the test grid. The checker completed all 200 tests. The two-center cover, diameter bound for one center, and monotonicity complete the stated ranges. There is no claim of an exact count below radius \(1/3\).

## Originality — PASS, provisional historical priority

The prior research finding `824df36e-a7bb-4bc5-94fb-f2acb41a752a` already proved the same fiber lower bound and that three balls never suffice. It did **not** exhibit or imply the exact four- and five-ball upper constructions at radii \(3/8\) and \(1/3\), respectively, nor the resulting exclusion of covering number six. The motivating Cieliebak–Cieliebak study concerns covering numbers and sum metrics but does not supply these configurations. Searches for torus taxicab/Manhattan covering, periodic square coverings, and five-ball phase thresholds found no implication-equivalent prior statement. Euclidean-geodesic two-disk covering and lattice/packing results involve different norms, arrangements or invariants. Historical priority under alternative terminology cannot be ruled out completely.

## Value — PASS

The exact two previously undetermined finite covering phases give a natural covering-number spectrum at the first few sites, including the nonoccurrence of six. The five-point configuration is a geometrically nontrivial continuous cover, and the exact endpoint \(N(1/3)=5\) is not derivable from lower bounds alone. The exact finite cutoffs and constructive methods are useful to further metric covering questions without presuming a full formula at smaller radii.

## Limitations and literature

The construction proves neither an exact formula below \(r=1/3\) nor optimizer uniqueness. See K. and M. Cieliebak, *Covering numbers of metric spaces*, arXiv:2611.15599v1 (2026), and the prior research finding `824df36e-a7bb-4bc5-94fb-f2acb41a752a`. Related Euclidean geodesic covering of well-rounded flat tori has a different metric; the recorded comparison is not a proof of global historical uniqueness.

Self-review: passed. Independent audit: not yet performed.
