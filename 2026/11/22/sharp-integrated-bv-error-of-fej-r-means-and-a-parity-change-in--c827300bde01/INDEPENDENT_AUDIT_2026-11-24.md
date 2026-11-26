# Independent mathematical audit

## correctness

PASS

The frozen mathematics is correct. With unnormalized arc length, an indicator's error equals twice its outgoing kernel flux. For a single arc the flux at shift t contributes min(|t|,d), d the smaller of the arc and complementary lengths. This yields C_n(d)=2 integral_0^pi K_n(t) min(t,d) dt, strictly increasing up to pi. Splitting any finite union of arcs counts extra strictly positive flux between components when there is more than one component; coarea and nested superlevels then force all nontrivial levels of an extremizer to coincide with one semicircle. The deficit equals 2 integral_0^delta (delta−u)K_n(pi−u) du, giving the stated quadratic/quartic coefficients by antipodal Taylor expansion. The repair narrows the contribution to the parity-resolved cubic asymptotic. Its self-contained moment evaluation uses the sharp BV translation bound and equality for a semicircle indicator (all translated residuals share a sign); this gives exactly 2 integral_0^pi tK_n(t) dt. Fourier integration and the odd reciprocal-square sum pi²/8 reduce this to 4(R_m+S_m/n)/pi. Independently, the Euler–Maclaurin expansions of H_M and the reciprocal-square tail give S_m=log(4m)/2+gamma/2+1/(48m²)+O(m^−4) and R_m=1/(4m)−1/(48m³)+O(m^−5). In terms of b=2m, pi*n*C_n/2 is log(2b)+gamma+n/b+1/(6b²)−n/(3b³)+O(n^−4). For b=n the n^−2 coefficient is −1/6. For b=n−1 the Taylor expansion has vanishing n^−1 and n^−3 coefficients and n^−2 coefficient +1/3. Rescaling proves the claimed opposite-sign cubic corrections with the O(n^−5) remainder. The large-degree expansions do not require m>0 at n=1; the exact first moment there is pi/2. Verification.md and the Python checker were read, not executed; none of their numerical tests is used as proof.

## originality

PASS

PASS for the narrowed contribution in repairs/4/RESULT.md, not for the original originality scope. The universal same-day convolution lemma directly covers the exact moment and implies the harmonic evaluation with the standard Fejér multipliers. Its rigidity argument uses only positivity almost everywhere, so its conclusion also covers Fejér's finitely many zeros. The powered Fejér theorem excludes q=1 in its statement but the parity calculation extends mechanically by specializing the displayed formula and proof. These are overlaps of substance, not a priority ordering by date. The ordinary kernel's signed cubic asymptotic with O(n^−5) remainder survives the overlap check and is the finding stated in the repair.

## value

PASS

The surviving claim describes the first signed finite-degree bias of the sharp integrated Fejér BV budget, distinguishing two parities even though the logarithmic leading law is the same. It shows that the logarithmic formula overestimates at sufficiently large even indices and underestimates at odd indices, with no n^−2 or n^−4 term masking the effect. This precise parity correction for a canonical positive Fourier kernel is a motivated exact invariant, not a numerical recalculation of the known moment.

The dated certificate retains the supplied scientific assessment, sources and limitations.
