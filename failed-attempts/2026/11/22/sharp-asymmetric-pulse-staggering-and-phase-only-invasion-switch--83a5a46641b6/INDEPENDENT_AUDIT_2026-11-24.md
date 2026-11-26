# Independent mathematical audit

## correctness

PASS

Integrating the wrapped exponential product across the jump at phi gives I_T=C(A exp(b phi)+B exp(-a phi)) with A=exp(-bT)(1-exp(-aT)), B=1-exp(-bT), and C=PQ/[(a+b)(1-exp(-aT))(1-exp(-bT))]. The equal endpoint values identify the synchronized maximum. Strict convexity and derivatives of opposite sign give one interior minimum at the stated logarithm; its offset from T/2 is the logarithmic ratio of sinh(bT/2)/b and sinh(aT/2)/a divided by a+b, with the asserted signs. Integration of the scalar population equation gives log M=L-kappa I_T since each separate integral is phase independent. Exactly two crossings occur only in the strict window kappa I_min<L<kappa I_max; at its boundaries the indicated single phase is merely neutral. For the finite witness let h=exp(-1/2), D=4(1-h^6)(1-h^2). Then I(0)=(1-h^8)/D and I(1/2)=(h+h^3-h^5-h^7)/D. Alternating Taylor sums through degrees 5 and 6 give .606<h<.607 (terminating decimals exact). Thus 25(1-h^8)-8D=-7+32h²+32h^6-57h^8>3.661 using h²>.367 and h^8<.019. Also 8D-25(h+h^3-h^5-h^7)>0.535 using h²<.369, h^3<.224, h^6<.051, h^5>.081 and h^7>.029 and dropping +32h^8. These certify strict reversal at L=8/25 without relying on sampled phases. For fixed doses, T I_T''(T d)→PQ uniformly on d∈[0,1]. The equal endpoints then give [I_T(0)-I_T(T d)]/T→PQ d(1-d)/2 uniformly by twice integrating with zero boundary values. Its maximum is PQ/8. Finally, factoring exp(bT) out of the exact minimizing-phase logarithm gives phi_*=(bT+log(a/b))/(a+b)+o(1); substituting into the exact minimum gives the stated exponential decay and prefactor.

## originality

FAIL

The critical prior alias is exact: (ab/PQ) I_T(phi) is the wrapped asymmetric Laplace density on the T-circle for Exp(a)-Exp(b). Kozubowski–Jammalamadaka (2003) already give that density, its strict decrease and increase around the unique antimode, its exact location relative to the half period and the two exact extreme values. The record's pulse interpretation changes coordinates and scale. Its short- and long-period addenda are leading asymptotics of these explicit formulas; the scalar invasion condition is the level-set classification of the same known density.

## value

FAIL

The overlap and phase question is naturally motivated, but the central exact invariant and extremal behavior are already known in equivalent coordinates. After crediting those, the chosen scalar equation contributes the level-set test for a freely positioned threshold, and the two asymptotic regimes follow by leading expansion of the same exact density. There is no independent new biological mechanism, calibration, or nonroutine mathematical remainder to justify a repair as a distinct finding.

The dated certificate retains the supplied scientific assessment, sources and limitations.
