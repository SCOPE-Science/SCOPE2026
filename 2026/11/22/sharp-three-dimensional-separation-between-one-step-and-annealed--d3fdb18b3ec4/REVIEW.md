# Independent mathematical audit

## correctness

PASS

For q=p3, s=1-q and D=p1-p2, the smaller planar eigenvalue of the expected row projector is (s-sqrt(c²s²+(1-c²)D²))/2. The planar lifted top eigenvalue is q+(s+sqrt(c⁴s²+(1-c⁴)D²))/2: the weighted Gram matrix of the two planar rank-one complementary projectors has their Frobenius overlap c². The axial rate is s and the cross-block norm is at most s. The trace test for the annealed factor is valid, also on the boundary: the top plane eigenspace contains a positive combination of the active rank-one projectors (at s=0 the plane map is the identity), and the axial eigenmatrix is itself PSD. Thus the top eigenspace has nonzero projection of I, and the PSD matrices Phi^k(I) have spectral and Frobenius norms within a fixed factor. At each q with s>0 the planar terms are strictly optimized by D=0. For D=0 the lower envelopes are maxima of one strictly decreasing and one strictly increasing affine function; crossing gives the displayed unique laws. At the one-step optimum q is smaller than the annealed crossing, so the axial rate is exactly 2/(3-c). Differentiating the ratio gives sign(c²-6c+3); its unique maximum on (0,1) is at 3-sqrt(6), with value 6-2sqrt(6), and the rational example agrees. For minimal dimension, use planar doubled-angle unit vectors n_i of the complementary projectors: the one-step rate is (1+|E n|)/2 and the lift is half the 3-by-3 moment matrix of (1,n). If zero is in the convex hull, the lift minimum is 1/2 exactly at mean zero. Otherwise let rv be the nearest point of the hull to zero. All n_i·v>=r. The lift Rayleigh quotient at (1,rv) is at least (1+r²)/2, with equality possible only on the supporting chord; equal masses at its two ends attain it, and equality in the eigenvector condition forces zero tangent mean. This is precisely the one-step minimizing mean rv. Dimension one is immediate. The apparent malformed fraction token in the displayed comparison at line 26 does not change the unambiguous rates in the other displays and proof. The frozen numerical checker was inspected, not executed; strict analytic inequalities rather than its finite grid establish uniqueness.

## originality

PASS

The supported distinct contribution is the explicit, unrestricted annealed-versus-one-step separation and family-wise sharp penalty, not either general optimizer formulation or the one-step law alone. No inspected statement supplies this comparison; priority is qualified by unavailable close full texts.

## value

PASS

The planar coincidence makes dimension three the first meaningful setting for an objective mismatch. A correlated pair plus an orthogonal row isolates why the two rates depend on c versus c² and proves that optimizing a standard one-step proxy can incur a sharply quantified loss (even exactly 10 percent at c=3/5). This is an exact guide to the choice of criterion, not a claim about all 3D row systems or about almost-sure rates.

The dated certificate retains the supplied scientific assessment, sources and limitations.
