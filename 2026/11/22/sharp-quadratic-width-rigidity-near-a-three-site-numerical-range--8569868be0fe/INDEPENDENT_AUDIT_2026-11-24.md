# Independent mathematical audit

## correctness

PASS

Diagonal unitary conjugation gives support h(theta)=f(epsilon cos theta) for f(t)=lambda_max(H+tD), so widths are g(epsilon cos theta) with g(t)=f(t)+f(-t). Evenness and convexity of g locate the endpoints of its angular range at t=0 and t=|epsilon|. The top eigenvector of H has no zero entries. Equality of g(t) with 2f(0) at nonzero t would make that vector maximize both pencils by the Rayleigh bounds; the resulting equations force every diagonal entry of D to agree. For the simple top eigenvalue at zero, its squared couplings to the middle and lower eigenvectors are (d_0-d_2)^2/8 and (d_0+d_2-2d_1)^2/16, divided in the second-order formula by gaps 1/sqrt(2) and sqrt(2), respectively. The even sum doubles this coefficient to Q with an O(epsilon^4) error. In the orthonormal traceless diagonal basis given in the source the resulting quadratic form has eigenvalues 1/sqrt(2) and 3/(4 sqrt(2)), giving exactly the stated equality lines. Hausdorff error u from a disk implies width error at most 2u from its constant width, hence u>=Omega/4 exactly. The disk matching the constant and first harmonic of the support expansion leaves a second harmonic of amplitude Q epsilon^2/4 and a uniform O(|epsilon|^3) error, attaining the coefficient. For diag(1,-2,1), the upper branch in the reflection-even block stays above the reflection-odd eigenvalue t since sqrt(2+9t^2)>3|t|. Its support is that of an ellipse centered at -epsilon/2 with semiaxes sqrt(2+9epsilon^2)/2 and 1/sqrt(2). A concentric disk of mean semiaxis radius has error half the semiaxis gap, attaining the width lower bound. Scalar D translates the disk. The least-detectable statement is about the quadratic term at unit traceless norm, not finite-coupling minimization among directions; the analytic remainder is uniform on that compact set.

## originality

PASS

General constant-width rigidity, the support-pencil method, and ordinary second-order eigenvalue perturbation are prior; nor does the appearance of an ellipse by itself warrant a new contribution. The supported distinct quantitative result is the optimized width quadratic form for all real diagonal directions together with the sharp Hausdorff-to-disk coefficient and the exact benchmark in the least quadratic direction. No earlier equivalent quantitative result was found in the inspected sources.

## value

PASS

The unperturbed Jordan shift is a canonical numerical-range disk, and removing scalar translations is necessary to ask about genuine transverse deformation. The two sharp direction-dependent rates distinguish perturbations that first-order support changes would mistake for translations. The optimal disk coefficient connects a directional width observable to a geometric approximation error, and the exact ellipse verifies equality in this comparison at every scale along the least quadratic direction. This is a quantitative benchmark for local disk rigidity, rather than a restatement of the qualitative theorem or ellipse classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
