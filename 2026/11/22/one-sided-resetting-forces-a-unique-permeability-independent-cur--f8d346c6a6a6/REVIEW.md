# Independent mathematical audit

## correctness

PASS

Checked the directed boundary law and signed flux in RESULT.md:18–29, 48–58, 64–124. As an independent sign/normalization check, test Dp''−rp=−rμ with cosh(η(L−x)) and cosh(ηx) and integrate by parts: the equal endpoint derivatives give p(0)=A+gJ and p(L)=B−gJ with g=(cosh(ηL)−1)/(Dη sinh(ηL)). Substitution gives the claimed positive denominator. The explicit Neumann solution plus the flux corrector gives existence and uniqueness; the two positive traces and the positive Dirichlet Green kernel for −D∂xx+r imply interior positivity for a finite Borel source, also for singular continuous μ. Integrating the weak equation gives total mass one. For the left semicircle, the derivative of log(B/A) is the difference of cosh-weighted averages of z tanh(ηz) on opposite sides of L/2 and hence is strictly negative for each η>0. The ratio tends to 1 at zero and to 0 at infinity: positive mass a definite distance left of the midpoint suffices for exponential domination even if the source accumulates at the midpoint. Reflection inverts the ratio. Thus the stated β criteria, current signs, transversality (dη/dr=1/(2Dη)), and absence of κ in the root equation all follow. Integrating the coshes verifies the uniform formulas and expanding them at η=0 verifies the weak-bias coefficient for any fixed eligible source. The numerical example replays as 4*acosh(1.5)**2 = 3.70503712923511. VERIFICATION.md and verify_biased_membrane.py were read, not executed; the reported finite-volume and discrete-source results are auxiliary, not a proof for all Borel sources. This check concerns only the displayed diffusive membrane flux, not reset displacements or two-sided sources.

## originality

PASS

Pass is limited to the biased-interface, strictly one-sided fixed-source sign classification, with a transverse permeability-independent crossover in the competing-bias regimes. The symmetric current transform and the asymmetric interface law separately are antecedents, not discoveries.

## value

PASS

This is a complete sharp phase diagram for competition between directional transmission and the location of reinjection, valid even for singular one-sided sources. It separates what permeability controls (the magnitude) from what it cannot shift (the unique transverse zero when one exists), with a directly evaluable uniform-source threshold. It does not constitute empirical transport validation or a result about winding due to reset jumps.

The dated certificate retains the supplied scientific assessment, sources and limitations.
