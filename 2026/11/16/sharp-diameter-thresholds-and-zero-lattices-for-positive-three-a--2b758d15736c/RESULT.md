# Sharp diameter thresholds and zero lattices for positive three-atomic Fourier transforms

## Finding

Let \(d\ge 2\), let \(c_1,c_2,c_3\in\mathbb R^d\) be three distinct sites, let \(w_1,w_2,w_3>0\), and put
\[
\mu=\sum_{j=1}^3w_j\delta_{c_j},\qquad
F(\xi)=\widehat\mu(\xi)=\sum_{j=1}^3w_j e^{-2\pi i\xi\cdot c_j},\qquad
D=\max_{j,k}|c_j-c_k|.
\]
Define \(\kappa(\mu)=\inf\{|\xi|:F(\xi)=0\}\), with the infimum of the empty set equal to \(+\infty\).

**Sharp mass-dependent zero-free radius.** Suppose the three weights satisfy the strict triangle inequalities \(w_j<w_k+w_\ell\) for each permutation. Let \(\gamma_j\in(0,\pi)\) be the interior angle opposite the side of length \(w_j\) in the Euclidean triangle with side lengths \((w_1,w_2,w_3)\), and let \(\gamma_* =\min_j\gamma_j\). Then every real Fourier zero satisfies
\[
\boxed{\quad |\xi|D\ge c(w):=\frac12+\frac{\gamma_*}{2\pi}.\quad}
\]
For every such positive weight triple and every \(D>0\), equality is attained by noncollinear, pairwise distinct sites of diameter \(D\). For equal weights, \(c(w)=2/3\), and the equality configurations are exactly those noncollinear isosceles triangles having a longest side as their base. In particular, the dimension-independent constant varies through the interval \((1/2,2/3]\).

**Exact real zero set.** Under the same strict mass-triangle hypothesis, assume the sites are affinely independent. Let \(M\in\mathbb R^{d\times 2}\) have columns \(c_2-c_1\) and \(c_3-c_1\), and let \(G=M^TM\). Define
\[
\theta=\arccos\frac{w_3^2-w_1^2-w_2^2}{2w_1w_2},\qquad
z=-\frac{w_1+w_2e^{i\theta}}{w_3},\qquad
\alpha=\frac{-1}{2\pi}(\theta,\operatorname{Arg}z)^T.
\]
Here \(\theta\in(0,\pi)\), \(|z|=1\), and \(\operatorname{Arg}z\in(-\pi,\pi]\). The complete zero set consists precisely of the affine \((d-2)\)-flats
\[
\boxed{\quad
\bigcup_{\sigma\in\{-1,1\}}\ \bigcup_{n\in\mathbb Z^2}
\left\{MG^{-1}(n+\sigma\alpha)+v:v\in\ker M^T\right\}.\quad}
\]
Consequently, the *exact* nearest-zero radius is the two-coset quadratic minimum
\[
\boxed{\quad
\kappa(\mu)^2=\min_{\sigma=\pm1}\min_{n\in\mathbb Z^2}
(n+\sigma\alpha)^TG^{-1}(n+\sigma\alpha).
\quad}
\]
The two cosets are distinct, and the radius is finite. For collinear sites, the mass-triangle bound still holds, but Fourier zeros need not exist because the two required phase congruences may be incompatible.

**Equality geometry.** For a zero, take the three projected real numbers \(t_j=\xi\cdot c_j\). Equality \(|\xi|D=c(w)\) holds exactly when their range is \(c(w)\), their cyclic phases \(e^{-2\pi i t_j}\) use a *shortest closed circular arc* joining the three cancellation phases without an extra integer winding, and the two sites giving \(\min t_j\) and \(\max t_j\) are endpoints of a diameter segment parallel to \(\xi\). Equivalently, for one cancellation orientation, assign the ordered minimal-arc lifts \(0,s,c(w)\) to the three weights, with \(0<s<c(w)\): the sites assigned to the endpoints must be distance \(D\) apart, and the remaining site must project a fraction \(s/c(w)\) of the way along their diameter segment. This includes all equality configurations, including ties in the smallest weight.

If one weight exceeds the sum of the other two, \(F\) has no real zero for any sites. If equality holds in that weight inequality, cancellation forces the two smaller-weight phases to coincide and to be opposite to the larger-weight phase. This degenerate case is not included in the sharp strict-triangle equality classification.

## Assumptions and scope

Fourier normalization is \(\widehat\mu(\xi)=\int e^{-2\pi i\xi\cdot x}\,d\mu(x)\). All weights are strictly positive, frequencies are real, and Euclidean norms are used. The universal radius bound holds for all triples of distinct sites in every \(d\ge2\); the explicit rank-two zero-lattice formula requires affine independence. The equality construction uses noncollinear sites. There is no assertion about complex-frequency zeros, density of zero sets, or stability under measurement noise.

## Proof

**1. The phasor triangle.** Divide the equation \(F(\xi)=0\) by its nonzero first exponential. The three summands are vectors of lengths \(w_1,w_2,w_3\) closing a Euclidean triangle. If a weight is strictly larger than the other two combined, closure is impossible by the triangle inequality. Under strict triangle inequalities, the three phases are unique up to a common rotation and complex conjugation. Fixing the first phase at one, the cosine rule gives
\[
\cos\theta=\frac{w_3^2-w_1^2-w_2^2}{2w_1w_2},\qquad
w_1+w_2e^{i\theta}+w_3z=0,
\]
so the prescribed pair of relative phases is \((e^{i\theta},z)\), or its conjugate. The three successive circular gaps between the phases, in their cyclic order, are \(\pi-\gamma_1,\pi-\gamma_2,\pi-\gamma_3\). Their sum is \(2\pi\). Therefore the shortest circular arc containing all three phase points has angular length
\[
2\pi-\max_j(\pi-\gamma_j)=\pi+\gamma_*.
\]
This step covers all strict weight triangles; the gaps are strictly between zero and \(\pi\).

**2. Diameter obstruction and exact equality.** For a real Fourier zero choose the *actual* real projections \(t_j=\xi\cdot c_j\), not arbitrary representatives modulo integers. The circular phases \(e^{-2\pi i t_j}\) sit in the image of the real interval \([\min_jt_j,\max_jt_j]\) under the exponential map. Hence the length of this interval is at least the length of the shortest circular arc containing the three phases, in cycles:
\[
\max_jt_j-\min_jt_j\ge\frac{\pi+\gamma_*}{2\pi}=c(w).
\]
On the other hand, Cauchy--Schwarz and the diameter assumption yield \(\max_jt_j-\min_jt_j\le|\xi|D\), proving the bound. Equality in these inequalities forces precisely the minimal circular arc with no winding, and equality in Cauchy--Schwarz forces the extreme sites to form a diameter parallel to \(\xi\). These conditions are sufficient as well, since the prescribed phasors then cancel.

To see sharpness with genuinely noncollinear sites, choose one of the two cancellation-phase orientations and lift its three phase arguments, after a common phase rotation, into \(0,s,c(w)\), where \(0<s<c(w)<1\). For arbitrary \(D>0\), place the extreme sites at \((0,0)\) and \((D,0)\) and the middle site at \((Ds/c(w),\varepsilon)\), using the weight-to-phase assignment of the chosen lift. Choose \(\varepsilon>0\) small enough that the two remaining side lengths do not exceed \(D\). Taking \(\xi=(c(w)/D,0)\), with sign chosen to match the phase orientation, yields \(F(\xi)=0\), \(|\xi|D=c(w)\), and a noncollinear triangle. The construction embeds into any higher dimension. For equal weights the three phase spacings are each \(1/3\) cycle, so \(s/c(w)=1/2\); thus the equality triangles are exactly the isosceles triangles whose longest side is the projected diameter.

**3. The complete noncollinear zero set.** Write \(M=[c_2-c_1\ \ c_3-c_1]\). The normalized phasor equation forces
\[
M^T\xi\in(\alpha+\mathbb Z^2)\ \cup\ (-\alpha+\mathbb Z^2).
\]
Affine independence makes \(G=M^TM\) positive definite. All solutions of \(M^T\xi=b\) have the form \(MG^{-1}b+v\), with \(v\in\ker M^T\), orthogonal to the first term. The minimal squared norm on each flat is therefore \(b^TG^{-1}b\), establishing both displayed formulas. The two cosets cannot coincide: otherwise both nontrivial phase differences would be equal to their conjugates, making all three cancellation phases \(\pm1\), impossible for a strictly nondegenerate weight triangle. The lattice cosets are discrete transverse to the kernel, and none contains zero, so the minimum exists and is positive.

## Verification

The standalone checker \(`checks/tri_atomic_zeros.py`\) reconstructs the two phase branches from the cosine rule, checks representative exact phasor cancellations, tests the diameter bound and the quadratic minimum across 500 seeded random noncollinear weighted triples, verifies sharpness by constructing mass-dependent noncollinear extremizers, and tests an equal-weight isosceles family. These finite tests are supplementary: all universal quantifiers and equality cases are established by the preceding analytical argument.

## Relationship to prior work

The Fourier-null-distance functional is motivated by Gómez-Serrano, Levitin, Platt and Polterovich (2026), which studies Fourier transforms of *Lebesgue indicators of centrally symmetric convex bodies* and fixed-volume extremal geometry. Its polygon and bipyramid arguments do not concern discrete three-point Fourier-Stieltjes transforms, unequal positive atom weights, or the present diameter-and-weight invariant. Benguria, Levitin and Parnovski (2009) likewise concern convex-domain indicators. The Kolountzakis--Révész (2006) work addresses positive-definite function bounds under spatial support constraints, rather than the exact zero loci of weighted three-atomic measures. Published results for three-point Fourier signals on *finite cyclic groups* address torsion-constrained zero counts, not continuum Fourier frequencies or a Euclidean diameter extremum.

The argument here is elementary but the conclusion is a complete mass-sensitive classification of a natural Fourier-zero extremal problem; no general convex-body maximization or positive-measure result is inferred. Searches did not establish historical priority. Equivalent treatments of three-vector phasor cancellation in signal processing, diffraction or characteristic-function theory remain a possible source of overlap.

## Limitations

The theorem concerns exactly three strictly positive atoms. Its sharp equality statement assumes strict triangle inequalities; degenerate mass triangles have a separate collinearity-of-phases obstruction. The lower bound can be strict, and for collinear sites the real zero set can be empty. The fixed-configuration lattice formula requires rank two. No claim is made about more than three atoms or nonpositive/complex weights. The result establishes mathematical correctness within its stated hypotheses, not independence, formal certification, or publication priority.

## References

- J. Gómez-Serrano, M. Levitin, D. Platt and I. Polterovich, *An isoperimetric problem for Fourier zeros of centrally symmetric convex bodies*, arXiv:2609.10517 (first public 2026-09-09), https://arxiv.org/abs/2609.10517.
- R. Benguria, M. Levitin and L. Parnovski, *Fourier transform, null variety, and Laplacian's eigenvalues*, Journal of Functional Analysis **257** (2009), 2088--2123, https://doi.org/10.1016/j.jfa.2009.06.022.
- M. N. Kolountzakis and Sz. Gy. Révész, *On pointwise estimates of positive definite functions with given support*, Canadian Journal of Mathematics **58** (2006), 401--418, https://doi.org/10.4153/CJM-2006-017-8.
