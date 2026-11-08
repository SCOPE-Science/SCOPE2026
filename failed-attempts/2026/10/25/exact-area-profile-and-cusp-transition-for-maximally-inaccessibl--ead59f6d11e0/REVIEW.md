# Independent mathematical audit

## correctness

PASS

At Q_h=(0,h)x(0,1), vertical chords show r<=1. Every chord of length <1 must join adjacent sides because opposite-side chords have length >=1. Minimizing u²+v² for x/u+y/v=1 yields (x^(2/3)+y^(2/3))^3 and intercepts u=(x^(2/3)+y^(2/3))x^(1/3), v=...y^(1/3); if the minimum is <1, the intercepts fit the rectangle. The four-corner criterion, reflection, cutoff a, and integral follow. Substituting x=cos³t yields H(t)=3∫_0^t sin⁴s cos²s ds. Differentiating A and comparing a strictly increasing integrand proves (A/h)′>0; H~3t^5/5 and t~sqrt((2−h)/3) give the stated 4/(15sqrt3) coefficient and C² but not C³ regularity. Fresh independently written SciPy quadrature at h=1,1.25,1.5,1.9,1.99,2,2.1,3,20 agrees with H-formula within 3.3e−12, and ε=.1,.01,.001 scaled cusp quotients converge to 0.1539600718. These checks do not prove the infinite claim; the analytic reasoning does.

## originality

FAIL

The decisive full-text comparison is the explicit right-angle bow and rectangle maximizer locus of Calvo–Muñoz (2010, Lemma 6.1, Cor. 6.2 and Fig. 5). The later claim is an elementary area integration of that already-determined exact region, with monotonicity from the increasing slice length and 5/2 regularity from the first nonzero Taylor term at the already-identified aspect-two contact. The earlier paper did not print the evaluated constant or exponent; nevertheless the package offers only a routine quantitative corollary of stronger established geometry rather than an independent original finding. Search absence alone did not determine FAIL.

## value

FAIL

The quantity is naturally motivated (area fraction of points requiring a full shortest-side chord), and the numerical formula and cusp can be useful. However the complete set and aspect-two geometry are already known, and the new work is a single elementary antiderivative, monotone-slice inequality and endpoint Taylor expansion, without an independent structural theorem or nonroutine quantitative obstacle. Under the standard rejecting routine textbook deductions and invariants mechanically implied by known results, the exact area expression does not establish sufficient independent scientific value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
