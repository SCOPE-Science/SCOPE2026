# Independent mathematical audit

## correctness

FAIL

The boundary in RESULT.md:9 is a union of punctured rays (t>0); none contains the origin. The Dirac measure at (0,0) is invariant and obeys the stated zero-mass condition, yet B_t=0 for all t instead of P(B_t=1)=1/n. The sector-weight step at lines 73–79 is where the missing mass enters. If the origin has mass eta, each of the q open sectors has mass (1-eta)/q and the process is a mixture of the stated cyclic process (weight 1-eta) and the all-zero sequence (weight eta). The ray-orbit and cyclic-overlap calculations themselves check out; excluding the origin would fix the scope, but does not resolve the contribution issues below. The finite support checks do not test the universal invariant-measure hypothesis.

## originality

FAIL

No source is credited with the false quantifier. The only natural corrected claim, the nonzero off-boundary law, is mechanically recoverable from the explicit induced dynamics in Lagarias–Rains Part I, Example 3.2: the negative branch is conjugate to rotation by theta=(n-1)pi/n in its half-plane; every exit into the other half-plane gives n positive steps with action -I. At negative return times, reducing the angle modulo pi therefore gives theta mod pi=-pi/n. Exactly one of the n negative returns does not exit the half-plane (the stay interval has width pi-theta=pi/n); the gaps in the sign word are one gap of 1 and n-1 gaps of n+1. This determines the entire cyclic sign word up to shift, not just its frequency. Stationarity takes the uniform cyclic shifts of that word, and interval overlaps give the displayed two-time classification. The statistics were not found stated verbatim, but their absence from the sources inspected is not evidence of new dynamical content.

## value

FAIL

Sign correlations are a natural observable and exact lag laws can be useful, but here the entire corrected law reduces to the already explicit negative return rotation and its two possible gap lengths, followed by uniform phase and elementary counting. The predictable origin exception fixes a quantifier rather than leaving an independently useful new invariant. No repaired finding is submitted.

The dated certificate retains the supplied scientific assessment, sources and limitations.
