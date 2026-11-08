# Self-review

**Exact claim reviewed.** For a unit-circumradius regular heptagon, the minimum area among quadrilaterals whose sides are parallel to chords is \(\cos^2(\pi/7)[\tan(\pi/7)+3\tan(2\pi/7)]\), equivalently an area ratio \(\frac{8c^2-1}{7(2c^2-1)}\) with \(c=\cos(\pi/7)\). Exactly seven minimizers use four supporting edges with cyclic edge-index gaps \((1,2,2,2)\).

## Correctness — PASS

The fourteen available oriented chord normals and the supporting heights \(1,c\) are established geometrically. The area identity follows by solving adjacent support lines. The script `heptagon_cert.py` implements a fully finite rational certificate: it checks exactly 511 bounded choices, all support-line intersection inequalities, the algebraically zero slacks, and strict positive area gaps for every nonoptimal choice. The optimum's exact trigonometric value follows from its four tangent edges. The computation is exhaustive over the finite set, and the proof explains why every feasible chord quadrilateral reduces to that set; no extrapolation from numerical experiments is used.

## Originality — PASS (historical priority provisional)

Vígh (arXiv:2610.08168v1) defines the restricted functional, enumerates candidates in general and records the **numerical** 1.2588... regular-heptagon figure; these are acknowledged prior contributions. The new specific results are the exact algebraic evaluation and complete sevenfold optimizer classification with a rational sign certificate. Fodor–Grundbacher's universal unrestricted bound and the classical pentagon theorem do not imply this exact value. Published result records for enclosing parallelograms of regular polygons, a truncated pentagon enclosure, and translative polygon hulls do not encompass the four-independent-side heptagon problem. Remaining risk: an older specialist source might already state these exact cases.

## Mathematical value — PASS

This is a natural exact geometric approximation invariant connected to the 2026 chord conjecture, not an arbitrary parameter slice: the regular heptagon is explicitly singled out by source numerical extremal experiments. The theorem locates all optimizers and replaces a numerical estimate by a fully certified algebraic expression, providing a sharp reference shape for testing constructions and inequalities. It is an exact bounded-family result, not a solution of the unrestricted or general convex-body problem.

## Limitations and verification status

The result concerns chord-restricted convex quadrilaterals of affine-regular heptagons only. It does not establish the unrestricted minimum, a global bound over arbitrary heptagons, or the chord conjecture for all polygons. Numerical output from the verifier is a display of rational comparisons, not a stand-alone infinite-domain proof. Neither independent validation nor external audit has been performed.

Self-review: passed. Independent audit: not yet performed.
