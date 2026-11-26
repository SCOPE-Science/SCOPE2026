# Independent mathematical audit

## correctness

PASS

Termwise integration of the bounded five-tone signal against the integrable Gaussian gives the stated Gaussian and phase prefactor, which is nowhere zero. Multiplying the remaining Laurent polynomial in w=e^z by w² gives a quartic with nonzero leading and constant coefficients, so multiplicities sum to four on the cylinder. In y=w+1/w the polynomial reduces to y²+r^(3/2)y+r²-2. Its discriminant is (r-2)(r²-2r-4); the inverse map ramifies only at y=±2, neither a root, since Q_r(2)>0 and Q_r(-2) has minimum 5/16 at sqrt(r)=3/2. At r=1 the distinct real roots lie strictly between the branch values and remain there up to 2. At the second collision the repeated negative root lies below -2 and neither real branch can cross -2 thereafter. For nonreal y the preimages are exchanged by inversion in w, and conjugation gives the other pair. At each collision the two preimages are individually double, not a single higher zero. V itself is quasiperiodic in time but its zeros descend to the cylinder as claimed. Inspected frozen VERIFICATION.md and CHECK.py without executing the upload. The independent `python3 /workspace/reproductions/frozen_checks.py 2` sampled the original Gaussian integral in all five cases at the predicted locations; the all-r conclusion follows from exact algebra, not quadrature.

## originality

PASS

The strongest available literature excerpts concern Gaussian STFT interference, not an equivalent five-tone zero theorem. Closest Resultary comparisons involve different input or window families; the exact catalogue match is this assigned record itself. No inspected claim supplies the full two-collision result. Pass for the explicit five-case equal-amplitude harmonic classification, not for Gaussian analyticity, polynomial representation, or the existence of STFT phase singularities. The main publication's inaccessible full text is a material residual risk.

## value

PASS

Five consecutive equal harmonics are a natural case where quotienting a reciprocal zero equation by inversion gives two branches rather than one. The result distinguishes four zeros on a central frequency line, a genuinely off-axis quartet, and four zeros on a common time line, with two proved sharp scales and exact collision multiplicities. It provides a continuous-STFT cancellation benchmark without claiming a ridge, stability, or reconstruction theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
