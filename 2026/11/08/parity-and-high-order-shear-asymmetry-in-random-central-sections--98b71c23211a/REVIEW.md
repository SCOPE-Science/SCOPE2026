# Independent mathematical audit

## correctness

PASS

The strict interior apex projection makes the hull the union of two pyramids along the ring, with exactly the ring edges and apex-to-ring edges. Almost every central plane avoids vertices; its ring-line cut crosses exactly two ring edges, and each section vertex is a crossing of a genuine edge. Opposite apex signs give n spoke crossings; same signs give twice the number of opposite ring signs. Antipodal pairs then yield even rigidity. For odd n=2q+1 the two possible ring majorities alternate on the n half-circle azimuth intervals. Agreement with the common apex sign is precisely (-1)^q sgn(cos(n psi))=+1 on that half-circle. Conditional on azimuth the Haar vertical coordinate is uniform on [-1,1], giving the stated weight for same-sign apices. Its antiderivative is arcsin(k sin psi); summation with the alternating signs gives the endpoint formula and total mass 2 arctan(lambda)/pi. The differentiated odd sine expansion is absolutely convergent for k<1 (the coefficient sum of each sine power is bounded, and each differentiation costs at most its degree). Integration against the square wave picks only frequencies (2m+1)n: the signs (-1)^q, (-1)^m and (-1)^(q+mn) cancel. The positive coefficient series establishes strict bias; its first term has degree n, and k=lambda+O(lambda^3), giving the exact leading coefficient and next-order remainder. The exceptional intervals each have positive length and strictly increasing positive weight; counting q+1 versus q intervals and dominated convergence give the limits. The inverse formula applies only to the odd law. An independent 80-digit angular quadrature reproduced the endpoint law to 1e-65 at 18 n/lambda combinations and checked the leading coefficient at lambda=.001 for n=3,5,7,9 (ratios within 2.48e-6 of one). Replay: /workspace/branches/33f027af-1a20-4b04-a3bd-6db3813a6af6/independent_replay.py. It is a bounded integration check, not an independent hull simulation or proof of positivity; the all-order proof is analytic. The frozen checker was inspected, not executed.

## originality

PASS

Existence and combinatorial classification of plane sections, and general methods that reduce central slices to sign chambers, are not new here. The supported distinct claim gives evaluated Haar weights for the vertex-aligned skew bipyramid family, their parity dichotomy, and a strictly signed exceptional imbalance with explicit cancellation order and coefficient. The relevant accessible statements did not supply those conclusions. The 1982 section-frequency sources are material but unresolved priority risks, not evidence either for or against coverage.

## value

PASS

The full vertex-count distribution gives information beyond combinatorial attainability: an even-order invariant, a parameter-identifying odd-order probability, and a surprisingly high exact order of the bias between the other two outcomes. The strict sign and sharp coefficient expose how the base symmetry suppresses all lower harmonics and are meaningful geometric information for this natural family.

The dated certificate retains the supplied scientific assessment, sources and limitations.
