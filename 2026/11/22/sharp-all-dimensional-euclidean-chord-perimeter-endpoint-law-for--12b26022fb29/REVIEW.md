# Independent mathematical audit

## correctness

PASS

Frozen Finding line 8 did not specify that the equilateral triangle must be on a great circle. Under the ordinary Euclidean meaning the unqualified equality assertion is false: take three equally spaced points at height 1/2 on the sphere, with horizontal radius sqrt(3)/2; their three sides are all 3/2 and the perimeter is 9/2, not 3sqrt(3). The frozen proof already identifies the right locus. The complete repaired RESULT.md states it explicitly; indeed sum ell_ij^2=9-||sum X_i||^2 and equality in Cauchy–Schwarz require equal lengths and zero centroid, equivalent to the three inner products all -1/2. For the remaining claim the reduction in (u,v,s_1) is continuous on a compact product and has that unique maximum at (-1/2,-1/2,-1); hence the entire high-perimeter event enters the nondegenerate chart. Conditioning on the frame selected from the first two points leaves the last point uniform. The resulting f_d(u)f_d(v) density times the single-hemisphere surface Jacobian divided by area(S^{d-2}) is continuous and positive at the maximum. Independently expanding w+1/2 with a=u+1/2 and b=v+1/2 gives -a-b+2(a^2+ab+b^2)/3+3||eta||^2/8+O(||y||^3). The chord expansion then gives deficit (a^2+ab+b^2)/sqrt(3)+sqrt(3)||eta||^2/8+O(||y||^3). The 2x2 Hessian block has determinant 1, and the remaining eigenvalues are sqrt(3)/4. In Hessian coordinates the event is uniformly bounded and its indicator tends off the unit sphere to the unit-ball indicator. The local density at the maximum times 2^(d/2) times ball volume divided by sqrt(det H_d) simplifies to the stated C_d, including d=3,4. The normalized densities converge in L1; the deficit differs from squared mark radius by O(sqrt(epsilon)) on the event, yielding joint weak convergence to the mark and its squared radius, which is Beta(d/2,1). No joint TV assertion is needed. The unchanged probabilistic result and the corrected equality characterization both pass.

## originality

PASS

For the corrected result, the distinct supported claim is the explicit complete-sphere Euclidean chord coefficient for every fixed d>=3 together with the rescaled Euclidean shape's conditional TV law. The deterministic extremum and the dimension-two perimeter endpoint are not new. Earlier exact spherical triangle shape densities are a real implication risk, especially in d=3, but the available passages do not establish coverage of the all-dimensional theorem or of its exact mark.

## value

PASS

The repaired conclusion answers a concrete extreme-value question for the elementary Euclidean perimeter of an isotropic spherical triangle. Tail calibration changes qualitatively from the intrinsic perimeter: the angular gap degrees of freedom are penalized at the chord optimum, producing the extra power of epsilon, not just a change of units. The explicit coefficient and anisotropic conditional mark describe both how rare the event is and what the near-maximizing sample looks like. Clarifying the maximum locus preserves these substantive results.

The dated certificate retains the supplied scientific assessment, sources and limitations.
