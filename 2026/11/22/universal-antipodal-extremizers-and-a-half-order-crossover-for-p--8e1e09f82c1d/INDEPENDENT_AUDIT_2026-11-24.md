# Independent mathematical audit

## correctness

PASS

The Jordan masses of the real signed periodic derivative are both V/2. The product of their normalized laws represents f modulo constants as V/2 times an average of oriented arc indicators: differentiate under the pairing and use that a periodic distribution of zero derivative is constant. The residual kills constants and is an L² contraction by its Fourier multipliers, so the triangle bound reduces the sharp norm to arcs. Parseval, counting both signs of each nonzero integer frequency and dividing by the arc variation squared (4), gives (2π²)^(-1) times the stated arc series. For angles in a compact subset of (0,π), summation by parts gives uniform O(1/M) sine-series tails for q^n/n, all q in [0,1]; hence differentiating the arc series after expanding the two-radius product and averaging is justified even with atoms. Differentiating arg(1-e^(-u)e^(-iθ)) twice yields the stated positive curvature in u>0. The mixed difference is its double integral for finite radii in logarithmic coordinates. For an infinite coordinate, take increasing finite coordinates: the double integral has a strictly positive lower bound on any interior positive rectangle, and the angular terms converge. A zero logarithmic coordinate contributes zero. Nonidentity mass gives strictly positive probability of two positive coordinates, so the unique maximizing length is 1/2 by symmetry. An extremizer's product endpoint law must then be supported on the antipodal relation; conditioning on almost any one endpoint forces the opposite marginal to be a point mass, and conversely. Only the asserted step functions result. The endpoint ν=δ₀ is consistent with the arc variance d(1-d) and sharp C₀=1/4; a mixture of δ₀ with δ₁ scales this constant by its mass at 0, while δ₁ alone is properly excluded. Differentiating the odd dilogarithm gives the log ratio and its left limit gives the stated coefficient as r→1. Positive stable subordination applies to exp(-t|n|^α) with 0<α<1; α=1 is deterministic. For small t the subcritical limit is dominated by the odd-index sum of n^(2α-2). At α=1/2, the error in replacing the low frequencies n≤t^(-2) by t²/n sums to O(t³ sum n^(-1/2))=O(t²), and the upper tail is O(t²); the odd harmonic sum produces log(1/t). Above the threshold, both tails of the odd-mesh Riemann sum are controlled by x^(2α-2) and x^(-2); the mesh gives the factor 1/(4π²). Integration by parts and writing e^(-y)-e^(-2y)=∫₁² y e^(-sy) ds gives 2Γ(2-1/α)∫₁² s^(1/α-2) ds for the integral, equal to the stated gamma expression and to 2 log 2 at α=1. These are fixed-order limits. The script check.py was inspected and not executed; the source-reported 32 consistency assertions are supplementary, not proof or formal verification.

## originality

PASS

Qualified pass for the all-positive-nonidentity-mixture sharp L² residual norm, complete rigidity and sharp fractional-Poisson (multiplier exp(-t|n|^α)) coefficients. The basic arc-reduction paradigm and positive subordination are not the distinct contribution; nor is the semicircle observation already known for a different norm. Closest inspected same-domain records switch kernels and change extremizers. Same-day catalogue records were substantively compared without inferring priority from the date.

## value

PASS

One strict ordering of all arc lengths gives a sharp approximation benchmark and exact attainment for a whole moment-kernel class; it remains valid with endpoint atoms and is not an accident of a single filter. The half-order threshold is quantitative as well as qualitative: it separates a summable low-frequency limit, a logarithmic boundary, and a rescaled high-frequency limit, with explicit leading constants and the same extremizers. This is useful structure beyond a rate estimate or a reused extremizer at one radius.

The dated certificate retains the supplied scientific assessment, sources and limitations.
