# The universal astroid law and sharp cusp scaling of random ellipse circumcenters

## Finding

Let three independent eccentric anomalies be uniform on \([0,2\pi)\) on a noncircular ellipse. The Euclidean circumcenter has a shape-independent, explicitly normalized distribution supported on an astroid. This report gives (i) the full absolutely continuous law by a one-angle integral, (ii) every mixed complex moment, and (iii) the sharp probability and conditional geometric law near each astroid cusp. The classical circumcenter identity and the known astroid trace support are credited as prior facts, not presented as new.

Write \(a>b>0\), \(P_j=(a\cos\theta_j,b\sin\theta_j)\), and \(C=(C_x,C_y)\) for the circumcenter of the triangle \(P_1P_2P_3\). With \(d=a^2-b^2\), define
\[
Z=X+iY=\frac{aC_x-i bC_y}{d}.
\]
The noncollinearity assumption holds with probability one. The law is independent of \(a,b\); explicitly, with independent unit-circle uniform \(z_j=e^{i\theta_j}\),
\[
Z=\frac14\bigl(z_1+z_2+z_3+(z_1z_2z_3)^{-1}\bigr).
\]
Its support is exactly the closed astroid \(\{x+iy:|x|^{2/3}+|y|^{2/3}\le1\}\). Let \(f\) be the density with respect to Lebesgue area. For almost all \((x,y)\) it is the following explicit absolutely convergent (where finite) one-dimensional integral:
\[
f(x,y)=\frac1{\pi^3}\int_0^{2\pi}\!\frac{\mathbf1_{\{|x/\cos u+y/\sin u|<1,\ |x/\cos u-y/\sin u|<1\}}}{|\cos u\sin u|\sqrt{1-(x/\cos u+y/\sin u)^2}\sqrt{1-(x/\cos u-y/\sin u)^2}}\,du.
\]
Values at isolated singular parameters are interpreted by measurable limits; the formula is an almost-everywhere density, not a pointwise assertion at all boundary points. It integrates to one and is zero off the astroid.

For all nonnegative integers \(p,q\), define \(r=\max(p,q)\), \(s=\min(p,q)\). Then \(\mathbb E[Z^p\overline Z^q]=0\) unless \(r-s\) is divisible by four. If \(k=(r-s)/4\) is an integer,
\[
\mathbb E[Z^p\overline Z^q]=\frac{r!s!}{4^{r+s}}\sum_{\substack{t_1,\ldots,t_4\ge0\\t_1+\cdots+t_4=s}}\prod_{j=1}^4\frac1{t_j!(t_j+k)!}.
\]
In particular, \(\mathbb E[X^2]=\mathbb E[Y^2]=1/8\), \(\mathbb E[X^4]=\mathbb E[Y^4]=27/512\), \(\mathbb E[X^2Y^2]=1/512\), and \(\mathbb E[Z^4]=3/32\). Compact support implies these moments determine the law.

At the right astroid cusp, as \(t\downarrow0\),
\[
\Pr(X>1-t)=\frac{4\sqrt2}{3\pi^2}\,t^{3/2}\bigl(1+O(t)\bigr).
\]
Choose unique representatives of each \(\theta_j\) in \((-\pi,\pi]\). Conditional on \(X>1-t\), the triple \((\theta_1,\theta_2,\theta_3)/\sqrt t\) converges in total variation to the uniform volume law on
\[
\mathcal E=\left\{v\in\mathbb R^3:\sum_{j=1}^3v_j^2+\left(\sum_{j=1}^3v_j\right)^2<8\right\}.
\]
Consequently, jointly with this convergence, \(((1-X)/t,Y/t^{3/2})\) converges weakly to the pushforward of that same uniform ellipsoid law under
\[
v\longmapsto\left(\frac{\sum_jv_j^2+(\sum_jv_j)^2}{8},\frac{(\sum_jv_j)^3-\sum_jv_j^3}{24}\right).
\]
This is not a statement of total-variation convergence for the latter two-dimensional rescaling. Quarter-turn symmetry yields corresponding cusp statements at the three other cardinal points.

## Assumptions and scope

The ellipse is noncircular and nondegenerate (\(a>b>0\)); uniform eccentric anomaly is also uniform *equiaffine* arclength, since \(\kappa^{1/3}ds=(ab)^{1/3}d\theta\). Independent sampling permits repeated anomalies with probability zero. The limiting cusp statements keep \(a,b\) fixed, but normalization makes them universal. The construction samples the maximal diagonal torus of \(\mathrm{SU}(4)\), **not** Haar-random matrices in the full group. Circumcenter coordinates use the conventional Euclidean metric.

## Proof

**1. Classical circumcenter reduction.** The 1959 solution to Klamkin–Miller E1348 writes the circumcenter of any triangle inscribed in an ellipse in terms of the three eccentric angles and their sum. Its two real component formulas, with the stated sign of the ordinate, give precisely the displayed complex trace identity. This identity can also be independently checked by the equal-distance linear equations \(2C\cdot(P_j-P_1)=\|P_j\|^2-\|P_1\|^2\) for \(j=2,3\). None of the later distributional conclusions is contained in that identity alone.

**2. Independent-angle representation and support.** The torus homomorphism
\[
(\theta_1,\theta_2,\theta_3)=(u+v,u-v,-u+w)\pmod{2\pi}
\]
has nonzero integer determinant and maps normalized Haar measure to normalized Haar measure. Thus independent uniform \(u,v,w\) give the required joint angles; substituting yields
\[
X=\tfrac12(\cos v+\cos w)\cos u,\qquad Y=\tfrac12(\cos v-\cos w)\sin u.
\]
Writing \(p=\cos v\), \(q=\cos w\), the pair is independent with density \(1/(\pi^2\sqrt{1-p^2}\sqrt{1-q^2})\). Given \(u\), the inverse is \(p=x/\cos u+y/\sin u\), \(q=x/\cos u-y/\sin u\), and the absolute Jacobian of the forward map is \(|\cos u\sin u|/2\). Integrating the conditional density over uniform \(u\) proves the stated formula. Since this is a pushforward of a probability distribution it normalizes to one.

For some \(p,q\in[-1,1]\), the coordinates are feasible at \(u\) precisely when \(|x/\cos u|+|y/\sin u|\le1\). Minimizing the left side over a first-quadrant \(u\) gives \((|x|^{2/3}+|y|^{2/3})^{3/2}\); the boundary axes follow by continuity. This proves the exact compact support, with strict interior occupied with positive probability. The support statement itself is also known through the \(\mathrm{SU}(4)\) trace astroid and is not advanced as a novelty claim.

**3. Every moment.** Expand \((4Z)^p(4\overline Z)^q\) in the four unit phases \((z_1,z_2,z_3,(z_1z_2z_3)^{-1})\). Fourier orthogonality for the three independent angles makes a term survive exactly when all four net phase exponents coincide. If \(p-q=4k\ge0\), write the four exponents in the conjugate multinomial as \(t_j\); the nonconjugate ones are \(t_j+k\), proving the factorial sum. Complex conjugation handles \(q>p\). The displayed small moments follow by substitution and separating real/imaginary components, and polynomial density on compact support ensures moment determinacy.

**4. Sharp cusp probability.** The real part equals
\[
X=\tfrac14\left(\cos\theta_1+\cos\theta_2+\cos\theta_3+\cos(\theta_1+\theta_2+\theta_3)\right).
\]
It reaches one only when the three representative angles are all zero, modulo full turns, since it is an average of four cosines. Compactness therefore localizes the event \(\{X>1-t\}\) to a shrinking neighborhood of that triple. With \(S=\theta_1+\theta_2+\theta_3\), uniform Taylor expansion there gives
\[
1-X=\frac{\sum_j\theta_j^2+S^2}{8}+O(\|\theta\|^4),\qquad
Y=\frac{S^3-\sum_j\theta_j^3}{24}+O(\|\theta\|^5).
\]
The quadratic form \(\theta^{\mathsf T}(I_3+\mathbf1\mathbf1^{\mathsf T})\theta\) is positive definite, with determinant four. Under \(\theta=\sqrt t\,v\), the indicator of \(\{X>1-t\}\) converges almost everywhere to \(\mathbf1_{\mathcal E}\), and for sufficiently small \(t\) its support lies in one fixed bounded set of \(v\). Dominated convergence gives both the leading volume and convergence in \(L^1\) of the normalized conditional densities; this is total-variation convergence. The volume equals \((4\pi/3)8^{3/2}/2=32\pi\sqrt2/3\), hence division by the original uniform-angle volume \((2\pi)^3\) gives \(4\sqrt2/(3\pi^2)\). A symmetric fourth-order Taylor remainder and a uniform radial boundary comparison yield the relative error \(O(t)\). The continuous-mapping theorem with the displayed Taylor expansions gives the joint scaled weak limit. Multiplying all four phase terms by \(i\) via a common quarter turn in the three input angles proves the fourfold symmetry.

## Verification

Run `python check_circumcenter_astroid.py` with Python 3.10+ and NumPy 1.24+. The checker independently reconstructs circumcenters by Euclidean equal-distance equations for three ellipse aspect ratios, tests exact rational mixed moments against large Monte Carlo samples, checks the two-angle-arcsine representation and sharp support, verifies the local quadratic and cubic Taylor expansions, and compares the cusp coefficient against three sample thresholds. The recorded run completed all checks successfully and printed `ELLIPSE_CIRCUMCENTER_ASTROID_CHECKS_OK`. Finite computations corroborate but are not infinite proofs.

## Relationship to prior work

The actual circumcenter trigonometric identity appears in the solution by Sister Mary Stephanie to E1348 (1959), itself citing C. Smith (1937); it is explicitly not claimed as new. The trace support of \(\mathrm{SU}(4)\) is known to be the filled astroid (Baez, 2012, reporting Egan, Bhardwaj and Wolbach); that support statement is also not claimed as new. The present claim is the *probability measure* created by independently uniform ellipse anomalies: its normalized density, every mixed moment and sharp marked cusp asymptotic. Inspected ellipse-billiard-center literature treats special 3-periodic billiard triangles or fixed-vertex loci, not the independent three-vertex model. A trace-of-random-maximal-torus law in a different literature could imply this result, and historical priority cannot be independently certified by searching.

## Limitations

No claim of absolute historical novelty is made. The old published circumcenter identity and astroid support are inherited. The density formula is an almost-everywhere integral and is not asserted to have a finite continuous extension to astroid cusps. The circular case is excluded because normalization divides by the ellipse's squared-axis difference. The cusp relative error is an asymptotic statement, not a uniform finite-sample bound for arbitrary target thresholds. The report supplies mathematical argument and a numerical checker, without independent expert validation.

## References

- Sister Mary Stephanie, solution to E1348 proposed by M. S. Klamkin and Raphael Miller, *American Mathematical Monthly* **66** (1959), 62. Reproduced in R. K. Guy's Klamkin compilation: https://carmamaths.org/resources/jon/Preprints/Books/Klamkin/komplete.pdf (printed page 60).
- John C. Baez, *Rolling Circles and Balls (Part 3)*, September 11, 2012: https://math.ucr.edu/home/baez/rolling/rolling_3.html .
- Olga Romaskevich, *On the incenters of triangular orbits in elliptic billiard*, arXiv:1304.7588 (2013): https://arxiv.org/abs/1304.7588 .
- Ronaldo Garcia, *The locus of the incenter of triangular orbits in an elliptic billiard*, arXiv:1607.00179 (2016): https://arxiv.org/abs/1607.00179 .
- Mark Helman, Ronaldo Garcia, Dan Reznik, ellipse-related triangle-center loci, arXiv:2010.09408 (2020): https://arxiv.org/abs/2010.09408 .
- Eric W. Weisstein, *Ellipse Evolute*, archived geometry reference (public archive dated May 25, 1999): https://archive.lib.msu.edu/crcmath/math/math/e/e070.htm .
