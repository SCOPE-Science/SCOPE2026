# Independent mathematical audit

## correctness

PASS

Under the one-color-per-positive-vertex rule, a colored hub forces the positive rim support to dominate the cycle, giving k=ceil(n/3) as its attainable minimum size. A zero hub forces independent rim zeros and at least ceil(n/2) positive rim positions; for n≥9 the only non-strict comparison with 1+k is at n=10, where five alternating positive positions would have to alternate colors around an odd cycle. For a fixed hub color, if p rim positions carry the other color, then n−k≤2p. Only n≡1 mod 3 can have p<k; there p=k−1 and coverage is exact. Every gap of other-color vertices then contains exactly two zeros, with the lone same-color vertex between the two zeros in a unique gap. Its fixed rim index gives exactly n choices. In the all-opposite-color case each gap has length 0,1,2, and marking one selected vertex counts each support k times. Thus the counts for one hub color are (n/k)[u^(n−k)](1+u+u²)^k, plus n when n≡1 mod 3. Evaluating the three coefficients and doubling gives 6, n(n+11)/3, and 2n in the stated order. An independent direct census for n=9,10,11,12 returned counts 6,70,22,6 with no zero-hub minimizer; this only corroborates the proof. The supplied verify.py was inspected, not executed.

## originality

PASS

The singleton/dual-server invariant is existing, and the all-opposite-color subcount reduces to ordinary cycle domination. The distinct claim is the full labelled wheel optimizer classification, including exclusion of the zero hub and the exact correction in residue 1. Closest indexed same-model results are about paths and cycles; the strongest journal comparison remains access-limited.

## value

PASS

This is a complete minimum-configuration census on a natural graph class, beyond computing the optimum weight. It explains why a single mixed-color defect is possible in exactly one residue class and separates bounded, linear and quadratic optimizer multiplicities with labels retained.

The dated certificate retains the supplied scientific assessment, sources and limitations.
