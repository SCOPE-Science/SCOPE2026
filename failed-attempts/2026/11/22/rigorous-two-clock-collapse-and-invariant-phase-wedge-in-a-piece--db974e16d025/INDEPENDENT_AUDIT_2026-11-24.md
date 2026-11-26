# Independent mathematical audit

## correctness

PASS

For ordered deviations u>v>=0 write the map as (A/B,|C|/D) with C=2v-u-uv. Both cross-product comparisons are positive, so the ordering persists even across the switching boundary. The larger coordinate decreases strictly within two steps away from the origin (including on the positive diagonal), which by compactness below the initial maximum implies collapse to zero. In the passive branch, C at the image is -2v(1-u)(3-u-v-uv)/(BD), so the exact wedge is invariant. If an orbit stayed in the active branch, after reaching u<=1/4 its relative separation (u-v)/u would grow by at least 39/32 every step, a contradiction. Substitution in the two-step map gives the relative factor 3/4+O(u) on each nonzero coordinate. Eventual geometric decay makes these relative errors summable, so the renormalized larger coordinate has a strictly positive limit, and the smaller has a limit (possibly zero). The one-step expansion on the wedge gives the stated odd amplitude; both parity maxima have positive leading coefficients. The diagonal's reciprocal recurrence gives the closed form, and the origin is fixed. This checks the continuous maxima map, not position-labelled tie-breaking. The supplied exact-rational check.py was inspected, not executed; replay is python3 check.py in the source package. Its finite checks are corroboration, not certification.

## originality

FAIL

A distinct Resultary record proves the same invariant wedge under an exact coordinate conjugacy, finite entry for every asymmetric orbit, both leading vectors and the sharp 3/4 ratio. It also gives a quadratic correction. The diagonal closed form just solves the exact scalar recurrence already in that source. The frozen theorem is sound but is covered; the alternate rational formulas do not isolate a substantive distinct claim. This is statement-level overlap, not an adjudication of priority.

## value

PASS

As a mathematical result, the exact wedge and positive parity amplitudes explain why the critical convergence rate of a nonsmooth orbit differs on and off the diagonal; this is stronger than a numerical rate or a stability bound. This does not confer incremental value on merely changing coordinates in the covered theorem, and no repair is proposed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
