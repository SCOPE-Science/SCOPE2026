# Independent mathematical audit

## correctness

PASS

For fixed 0<α<1 and positive integer n, direct integration of both arcs gives L|sin(παt)|/(π|t||L−t|), with L=n/(1−α), t=n−k, and respective coincident-pole magnitudes α and 1−α. The exact identity αt=t−n−(1−α)(t−L) bounds every distance-less-than-one term at the moving pole even for very good rational approximations. Each of the four shoulders is a harmonic sum with the same mean; uniformity in the shifting block follows from finite trigonometric approximation and bounded geometric sums in the irrational case, and from bounded periodic discrepancy in the rational case. Summation by parts yields the respective o(log n) and Oα(1) errors, and the middle and exterior away from the shoulders contribute O(1). The means are cot(π/(2q))/q and 2/π, so the factor is four times the mean divided by π. The symmetric identity follows by telescoping each exterior odd reciprocal sum and splitting the interior into two copies of the first n odd reciprocals; the resonances add 1. Monotonicity of x cot x and finiteness of rationals of bounded denominator in (0,1) give the stated continuity pattern. The irrational remainder is only asserted at fixed α; indeed an unbounded remainder can occur, since fixed-n norms are continuous in α by W^{1,2} continuity, and the smaller rational leading constants give arbitrarily large deficits on dense open sets of parameters. Replay the four regions in RESULT.md §§1–4; checks/verify_tent_phase.py was inspected, not executed, and is a supplementary finite diagnostic.

## originality

PASS

The supported distinction is the sharp coefficient across the asymmetric family and its arithmetic discontinuity, including the bounded rational error. The exact symmetric Fourier coefficients and the consequent symmetric leading constant are already covered; the general logarithmic growth scale is classical. No distinct equivalent or stronger result was established in the inspected evidence.

## value

PASS

The sharp constant for the basic nonsymmetric two-breakpoint family determines information the logarithmic growth theorem loses: its dependence on the denominator of the cut point, its exact jump at each rational, and the universal irrational value. Controlling a second moving resonance is required even when the cut ratio is extremely well approximated by rationals. This makes a useful benchmark for stronger Wiener asymptotic results without claiming the symmetric example or the growth scale as new.

The dated certificate retains the supplied scientific assessment, sources and limitations.
