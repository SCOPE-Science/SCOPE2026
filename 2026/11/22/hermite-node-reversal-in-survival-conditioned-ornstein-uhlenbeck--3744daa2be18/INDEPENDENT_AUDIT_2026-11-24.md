# Independent mathematical audit

## correctness

PASS

The conditioned event is endpoint exceedance for an absorbed excursion; the independent no-reset factor cancels. Multiplying the OU path by e^(κt) turns it into Brownian motion with a deterministic clock and the same absorption event, justifying the Gaussian image difference on the half-line. Integrating above a and above zero respectively gives the displayed CDF ratio. Independently, write b=√w, q=e^(−κt), and use the probabilists' Hermites He_j in the odd part of the Mehler kernel. The numerator and denominator after removing their leading terms have coefficients at q^(j−1) equal to A_j=He_j(b)He_{j−1}(b)/(b j!) and B_j=He_j(b)He_{j−1}(0)/(b j!) respectively for odd j, by integrating He_j times the standard Gaussian density. The ratio has limit e^(−w/2), c2=A_3−B_3=w(w−3)/6, and c4=A_5−B_5−B_3 c2=w(3w³−38w²+165w−180)/360. At w=3, c4=(−6)(−9)/120=9/20; analyticity in q² justifies eventual differentiation and all sign conclusions. At short times the unreflected Gaussian tail has argument √w√tanh(κt/2), and the image and survival corrections and their derivatives are exponentially small up to polynomial factors. This gives the stated square-root decrease. For 0<w<3 there are a left and a right interval on which the function falls and rises, respectively, so it attains a minimum in the interior of a suitable compact subinterval; analyticity and nonconstancy isolate such a minimum. No uniqueness or global monotonicity for w≥3 is inferred. Read RESULT.md, VERIFICATION.md and checker.py; the reported finite symbolic/numerical checks were not rerun.

## originality

PASS

The killed kernel, the Rayleigh limit and the vanished third mode as a property of the odd Hermite expansion are not independent originality claims. The supported distinction is the specified moving-with-start threshold event's late-time direction on both sides of the node, nonzero signed next term at the node, and the resulting forced interior turning below it. The checked primary texts give the spectral tools and related functionals, not that event-specific dynamical statement.

## value

PASS

For the natural time-resolved counterpart of above-reset-point occupation, the result separates signed convergence regimes at an exact parameter boundary and establishes genuine nonmonotonicity throughout a full subcritical range. It shows why quasi-stationary convergence and even knowledge of the spectral gap do not describe the finite-age conditional statistic. The useful content is this dynamical classification and strict turning, not only a Taylor coefficient or a restatement of spectral theory.

The dated certificate retains the supplied scientific assessment, sources and limitations.
