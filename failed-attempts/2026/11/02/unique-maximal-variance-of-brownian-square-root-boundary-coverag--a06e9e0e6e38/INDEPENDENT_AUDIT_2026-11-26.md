# Independent mathematical audit

## correctness

PASS

For 0<s<t, the correlation of the standardized Brownian values is sqrt(s/t). Integrating over both triangles gives E[Z²]=2∫₀¹r q_z(r)dr. Subtracting q_z(0) and integrating by parts yields the weight 1−r² on q′, with the endpoint term zero since q is bounded. The Gaussian density identity ∂_r f=∂_x∂_y f gives two equal positive corners minus two equal negative corners and hence the claimed variance formula. Under the two reciprocal changes of variable the derivative is (D−A)/π with h(s)=sqrt(2s−1)/s². The first moment of the variance kernel is integrable, so V′(0)=∫₀¹2r/[π sqrt(1−r²)]dr=2/π. On a>0 the derivative of log(A/D) is the mean of s on the upper support minus its mean on the lower support, strictly positive. The ratio starts below one and diverges by bounding A below on any compact subinterval of (1/2,1) and D above by a constant times exp(−a). This proves the unique maximum. The upper Laplace piece is O(exp(−a)/a), whereas the lower weight is 8 sqrt(2) sqrt(s−1/2) to leading order, giving the stated Gamma(3/2) constant. Boundedness of coverage proportions gives convergence of their first two moments at each fixed z, not a finite-sample maximizer theorem. Independent quadrature after s=(1+x²)/2 gives a*=0.68810970320346721766…, z*=0.82952378097524559013…, V*=0.08135656185520381043…, nominal coverage 0.59319191415401940057… and SD 0.28523071688582877877…. Independent conditional-Gaussian integration agrees at the displayed threshold.

## originality

FAIL

The distinct indexed finding 9d0d7bb698c8 already states the same compact variance integral and unique global maximum for exactly the same Brownian occupation fraction, the same peak values and the same two endpoint equivalents. Its small-threshold statement is even sharper. The different scalar parameter and presentation of the crossing do not yield a distinct finding. This is demonstrable equivalent coverage, not an allegation about authorship or how the two records arose.

## value

FAIL

The unique peak and endpoint scales are worthwhile mathematical questions, but the frozen record reproduces the exact analytic conclusions of the distinct indexed finding. The supportive numerical rerun and alternative root presentation leave no independently useful new exact invariant, scope extension, or stronger bound to retain as a repaired claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
