# Independent mathematical audit

## correctness

PASS

Gaussian Fourier integration gives the nonzero factor exp(−pi xi^2−2 pi i xi x) times 1+2q cosh(w)+2q^4 cosh(2w), where q=exp(−pi Delta^2) and w=2 pi Delta(xi+i x). Exponentiation gives a bijective cylinder coordinate with the reciprocal quartic of degree four and nonzero constant term. The quadratic in cosh(w) has discriminant 4q^2(2s−1)(4s^2+2s−1) with s=q^2. The values at y=±1 stay positive; the minimum of 1−2q+2q^4 for q>0 is 1−3/(2·4^(1/3))>0. Thus the inverse cosh never coalesces at its branch values. The two real roots lie in (−1,1) near s=1, meet at −1/sqrt(2) at s=1/2, become conjugate in the next interval, and meet below −1 at s_B; they remain below −1 for s<s_B. In the conjugate regime the upper-left root has one inverse with positive real part and angle in (pi/2,pi), and reciprocal and conjugate symmetry produce exactly the rectangle. Double roots pull back to double zeros because sinh(w) is nonzero there. Holomorphic multiplicity becomes negative phase winding in the reversed (x,xi) orientation; the nonzero prefactor adds no local winding. As q tends to zero the two root moduli are 1/(2q) and 1/(2q^3) up to relative O(q^2), yielding the stated midpoint errors after applying arcosh. The support script was inspected, not executed; its finite comparisons are not used for completeness.

## originality

FAIL

A distinct indexed Resultary theorem gives the same entire zero classification in rescaled coordinates, including both collision thresholds, multiplicities and all three arrangements. The frozen winding convention and distant-tone asymptotic follow directly from the matched holomorphic factor and explicit quadratic, so they do not supply a materially independent remainder. This is a finding of equivalent indexed coverage as of review, not a claim about historical order or dependence; the catalogue path is later-dated than the frozen path.

## value

PASS

A global classification in a tractable interference model answers where every phase zero is, how zeros collide, and which geometries persist as the frequency gap changes. These are substantively useful statements beyond exhibiting a few zeros or plotting ridge maxima. The frozen package nonetheless does not add a distinct result beyond the exact catalogue coverage.

The dated certificate retains the supplied scientific assessment, sources and limitations.
