# Independent mathematical audit

## correctness

FAIL

Finding line 14 says a nonconserved zero eigenvalue occurs precisely at a_c. This is false: take L=12, rho=3/4, t=0, a=32r. For m=2, cos(k)=1/2; the Fourier block has exact determinant 0 and trace -22r. Yet a_c=32r/(3 sqrt(3)-2)<32r, and the m=1 block has determinant (480-288 sqrt(3)) r^2<0. There can thus be neutral shorter modes in an already unstable state. Independently derived the blocks from the flow, and checked this counterexample in exact symbolic arithmetic. The determinant divided by positive h is affine increasing for rho>1/2, so the stated first onset, two-dimensional real neutral space at first onset, five-site cutoff, t=0 optimizer and finite-size expansion are otherwise valid. It is the fixed-mass spectral abscissa, not the presence of any zero eigenvalue, that is zero precisely at a_c. Inspected frozen VERIFICATION.md and verify.py: the sampled growth-rate and root-straddling tests do not check the claimed absence of higher-mode zeros; the uploaded code was not executed.

## originality

FAIL

The central finite-ring formulas are materially covered by a distinct exact Resultary record and are a direct determinant-sign corollary of the primary source's exact all-wave-number Jacobian. No historical priority claim is made from the two dates. The additional continuous-density optimization is not stated in the exact matching record but only completes the square in its same zero-diffusion threshold.

## value

FAIL

A genuinely new exact minimum ring size would be a useful finite-size benchmark, but it is the same cutoff in the matching exact finding and a routine corollary of the known symbol. After removing the equivalent central content and the false restriction on neutral eigenvalues, the continuous-density optimizer and expansions are elementary substitutions into the existing threshold, not a substantial independent remainder.

The dated certificate retains the supplied scientific assessment, sources and limitations.
