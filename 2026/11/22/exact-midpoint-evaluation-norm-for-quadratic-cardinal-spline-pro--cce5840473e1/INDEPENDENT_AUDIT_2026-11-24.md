# Independent mathematical audit

## correctness

PASS

The Gram entries are those of the spline with unit integral and support [0,3]; after substituting u=z+z^(-1), the symbol is (u²+26u+64)/120, positive on the unit circle. Its inverse has the stated decaying Green functions at the two inside roots. At x=1/2 the three active basis values are 1/8, 3/4, 1/8; recentering gives the even kernel with coefficient symbol 15(u+6)/((u−u_1)(u−u_2)). Both partial fraction residues in u are positive because u_1>−6>u_2. Dividing the residues by sqrt(u_i²−4) gives positive amplitudes in a_j=alpha q^j+gamma p^j with 0<p<q<0.44, even for j=0. The ratios a_(j+1)/a_j are nondecreasing and bounded above by q; an outward integer-interval calculation verified the stated lower bounds (0.31 at j=0 and 0.40 at j=1). On each cell the left quadratic is concave with strictly positive endpoints (use 1/0.31+0.44<6, and a_(-1)=a_1); the right quadratic is convex with opposite endpoint signs by the same inequality. Hence it has exactly one interior sign change. Integrating the absolute value, with reflection, gives the asserted series. The kernel has total mass one, by the partition of unity and the inverse symbol at z=1. The sign of the kernel attains the functional norm; its positive and negative indicators give the sharp excursions for [0,1] data. For M≥2, only indices j≥M−1 contribute on t≥M and the geometric envelope bounds the two-sided tail by 2 a_(M−1)/(1−q). Independent outward-rounded integer intervals and sign bisection on seventy cells enclose the partial sum starting at 1.756763783953966826198190050476811, with analytic tail <2.478×10^(-25), proving the stated decimal bracket. These checks do not execute the frozen verifier.

## originality

PASS

Best-of-knowledge pass for the exact midpoint integral of the absolute kernel and consequent sharp excursions. The kernel, its exact inverse-Gram representation and its quadratic tail pieces for this same projector have a direct earlier catalog antecedent; they are not credited as new. The midpoint-specific sign analysis and integrated sharp constant are distinct from the earlier cell supremum and from broader stability bounds.

## value

PASS

The midpoint is a natural reflection-symmetric point of the standard uniform-grid projection. The invariant answers a pointwise stability and range-preservation question exactly: it identifies the greatest possible overshoot and undershoot on bounded nonnegative data and gives extremizing sign sets via a verified root in each cell. The result requires more than evaluating a signed sum or quoting a global boundedness theorem; it is a sharp benchmark for quadratic projection even without a global maximizer theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
