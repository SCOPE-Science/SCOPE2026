# Independent mathematical audit

## correctness

PASS

The complement transform is a single common sinc factor times the sum of the two hole-center phases. The center midpoint offset is h=(a−c)/2, and separation D=b+g, giving the stated intensity identity. DC and known span determine g. The occupied-span transform vanishes at 2π/L, so the sample gives cos²(πD/L) with a nonzero prefactor, hence just D and L−D. For each fixed candidate D, the second derivative determines h² with coefficient 4Lg. For the complementary candidate, set v=a+c and H=h²; the second-order comparison forces H'=H+(b²−v²)/4. Expanding the even analytic difference after factoring out the sinc terms, the fourth coefficient is (b−v)(b+v+3g)(H−v²/4)/24. Here H−v²/4=−ac<0; the prefactor at zero is nonzero, and the lower coefficient has already vanished. Thus the fourth derivative eliminates any genuinely different complementary candidate, including all admissible symmetric and D=L/2 cases. The remaining sign of h is exactly reflection; the phase-magnitude data are translation invariant.

## originality

PASS

The supported distinct claim is global injectivity in the known-span equal-gap three-interval family from these specific four measurements. Neither general full-spectrum phase retrieval, full-spectrum nonuniqueness for unequal gaps, nor the inspected equal-occupied-width or two-interval finite-jet results give that injectivity.

## value

PASS

The natural equal-gap restriction salvages recovery in a component count where even full magnitudes can fail generically as a uniqueness guarantee on the unrestricted class. The proof gives a two-candidate inversion rather than merely establishing abstract uniqueness. The final derivative actually resolves a live ambiguity: at L=9 and g=1, (a,b,c)=(3/2,4,3/2) and ((4+√7)/2,3,(4−√7)/2) match DC, the fundamental intensity and the second derivative but differ in the fourth derivative. This is not a claim of optimal measurement count over all possible designs.

The dated certificate retains the supplied scientific assessment, sources and limitations.
