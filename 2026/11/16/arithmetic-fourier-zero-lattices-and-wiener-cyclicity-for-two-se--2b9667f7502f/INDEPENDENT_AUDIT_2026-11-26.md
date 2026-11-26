# Independent mathematical audit

## correctness

PASS

The repaired RESULT.md and SLOGAN.txt in repairs/4 credit the prior zero-set theorem and focus on the local Taylor law. The three families are indeed complete: write the endpoint equation as 1+v=u+w for four unit complex numbers. When the common sum is nonzero it determines the unordered pair by its midpoint on the unit circle, so the equal pairs produce Z_0 or Z_+; when it is zero, v=-1,w=-u, producing precisely Z_-. The origin is not a zero. Differentiation gives xi_0 times the slope as a*u-(a+d)*v+(a+b+d)*w; using respectively (u=1,v=w), (v=u,w=1), and (v=-1,w=-u) gives the exact three slopes, agreeing on overlaps. Their reverse-triangle bounds give |a-b| globally for a≠b, with equality at (1,2,1/2), xi_0=1; the Z_+ row actually gives at least a+b. In the equal-length case only Z_0 intersect Z_- can annul the derivative, with phases (1,-1,-1). The endpoint numerator has second derivative -8*pi^2*a*(a+d) there, yielding the claimed nonzero quadratic coefficient and the quartic intensity law. Double zeros require the equal-length phase ratio 2(a+d)/a to have odd reduced numerator; the zeros then have a*xi_0 an odd multiple of its denominator. The contextual Wiener criterion is as stated: the first two resonance planes require rational length or gap ratios, the third requires an odd integer multiple of the relevant ratio, and L2 cyclicity follows from isolated real zeros of a nonzero entire transform. The repaired exact cyclotomic checker repairs/4/verify_multiplicity.py, with replay at evidence/4/replay.txt, independently checks the formulas and all orders on 2,592 rational grid cases, including 402 simple and 24 double zeros; no inference to arbitrary real parameters uses that grid.

## originality

PASS

The frozen central zero-set claim is already in Łaba's Lemma 3.1; the stated Wiener cyclicity classification is a direct corollary and is not accepted as original. The surviving repaired result concerns the exact Taylor law at a zero: branch-dependent slopes with a sharp all-family lower slope bound for unequal lengths and the double-zero quadratic coefficient for equal lengths. This quantitative local invariant was not supplied by the inspected earlier classification, phase retrieval theorem, or Riesz result.

## value

PASS

Knowing a compact-window frequency null does not indicate how quickly amplitude recovers nearby. The revised result supplies an exact quantitative answer on the smallest disconnected indicator family: an all-null slope lower bound tied sharply to the length asymmetry, and the exceptional equal-length law switching the local intensity scale from quadratic to quartic with a computed coefficient. Root orders and strengths are natural invariants for conditioning near zeros. The value is not a repeat of the known real-zero/cyclicity classification or an added finite certificate alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
