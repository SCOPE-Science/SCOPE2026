# Independent mathematical audit

## correctness

PASS

For the specified half-scale quadratic image, linear support is the top eigenvalue of the symmetric hollow matrix with off-diagonal coordinates u_i/2. Rayleigh's principle gives the width as spectral spread. The characteristic polynomial is lambda^3-lambda/4-u_1*u_2*u_3/4; ordering its three trigonometric roots gives cos(arcsin(3 sqrt(3) T)/3). It decreases over the stated T range, so the width CDF is the T survival function at q(w). Haar coordinates give independent uniform azimuth and uniform |U_3|, with T=z(1-z^2)|sin(2 Phi)|/2; azimuthal integration gives the exact formula including endpoints. An alternate endpoint check uses (U_i^2)_i ~ Dirichlet(1/2,1/2,1/2): its Gamma moments, by triplication and moment uniqueness on [0,1], give 27 T^2 as the product of independent Beta(1/2,1/3) and Beta(1/2,2/3). The two-beta convolution reduces by Euler integration to f_T(t)=2 sqrt(3) times 2F1(1/3,2/3;1;1-27t^2). For t near 1/(3 sqrt(3)) the density tends to 2 sqrt(3), and the product cutoff decreases from that endpoint by 2 sqrt(3) epsilon^2+o(epsilon^2), giving 12 epsilon^2. Near t=0 the zero-balanced connection formula gives f_T(t)=(3/pi)[-log(27t^2)+3 log 3]+O(t^2 log(1/t)), since 2 psi(1)-psi(1/3)-psi(2/3)=3 log 3. Thus F_T(q)=(6/pi)q[log(1/q)+1]+o(q), confirming both high-width coefficients under q(1-epsilon)~sqrt(2 epsilon/3). The original endpoint matching can also be justified by substituting the exact monotone endpoint variables 2b(z) near zero and b(z) near one; the Jacobians differ from 1 by quadratic and linear terms, respectively, giving the stated O(q eta^2) and O(q eta) errors. Width minima occur only at the eight signed diagonals, and symmetry equidistributes the conditioned directions there. For high width, outside any fixed neighborhoods of the six axes every zero is regular: one coordinate vanishes and the other two stay bounded away from zero on each local zero segment. A finite tube bound gives O(q) mass there versus q log(1/q) overall, proving the uniform six-axis limit by symmetry. Inspected verify.py and VERIFICATION.md; the reported deterministic tests are not used as proof or claimed as rerun. The result is for directional caliper width, not random points or shadow area.

## originality

PASS

Pass for the geometric width law and its sharp rare-direction description, in particular how the joint directional measure concentrates at the intersections of the maximizing curves rather than on those curves. The support geometry and standard distribution tools are not new. The scalar tail constants are accessible by classical special-function theory once the normalized width-to-product reduction is made, so do not claim an independent discovery of a generic product tail or logarithmic special-function expansion.

## value

PASS

Directional spread is an intrinsic observable of this classical nontrivial hull. The result separates isolated conical minima, with quadratic event probability, from a positive-dimensional maximizing set whose crossings dominate near-maximal views; it supplies precise probabilities and the limiting directions for both. The latter description is not encoded by a marginal product distribution or a convex-hull representation and answers where equally extreme projections are seen, rather than merely re-expressing an existing scalar table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
