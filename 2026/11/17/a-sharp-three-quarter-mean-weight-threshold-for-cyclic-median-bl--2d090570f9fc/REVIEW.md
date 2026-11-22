# Independent mathematical audit

## correctness

PASS

PASS: On every strict-order chamber the centered three-point median selects one input coordinate per output. Its derivative on cyclic first differences has only three rows per column, with selector coefficients (a,1-a-c,c) where a,c are indicators. Blending the three-point mean replaces these by ((1-theta)a+theta/3, (1-theta)(1-a-c)+theta/3, (1-theta)c+theta/3), whose maximum l1 column sum is max(1,3-8theta/3), reached by a=c=1. All rank chambers are finitely piecewise affine and continuous so path integration proves global Lipschitz upper bound for arbitrary x,y and n>=6. Explicit separated rank-chamber interfaces for n=6 and n>=7 attain the bound with finite positive epsilon for every theta, ruling out a merely infinitesimal estimate; ratio returns threshold theta>=3/4. Independently computed exact-rational 18 lengths n=6..23 by six sample theta; all 108 pairs attain exact formula. No infinite-n assertion is based on the finite tests.

## originality

PASS

PASS best of knowledge, with genuinely read exact-object comparators and explicitly bounded coverage risks. The prior first-power endpoint bounds cannot force cancellation of the negative median middle derivative by positive mean coefficients, hence cannot imply phase threshold theta=3/4.

## value

PASS

PASS: Quantifies the exact robust/nonlinear versus linear mixing needed for contraction of differences in a canonical cyclic variation seminorm. The 3/4 threshold cannot be recovered from convexity of separate median and mean endpoint norms (which yields 3-2theta), and is exactly attained, making it a motivated uniform stability calibration.

The dated certificate retains the supplied scientific assessment, sources and limitations.
