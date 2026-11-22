# Sharp diameter thresholds and zero lattices for positive three-atomic Fourier transforms

## Finding

Let \(d\ge 2\), let \(c_1,c_2,c_3\in\mathbb R^d\) be pairwise distinct, and let \(w_1,w_2,w_3>0\). Define
\[
\mu=\sum_{j=1}^3w_j\delta_{c_j},\qquad
F(\xi)=\sum_{j=1}^3w_j e^{-2\pi i\xi\cdot c_j},\qquad
D=\max_{j,k}|c_j-c_k|,
\]
and \(\kappa(\mu)=\inf\{|\xi|:F(\xi)=0\}\), with \(\inf\varnothing=+\infty\).

Assume the strict triangle inequalities \(w_j<w_k+w_\ell\) for each permutation. Let \(\gamma_j\in(0,\pi)\) be the interior angle opposite side \(w_j\) in the Euclidean weight triangle and \(\gamma_* =\min_j\gamma_j\). Every real Fourier zero obeys the sharp, mass-dependent bound
\[
\boxed{\ |\xi|D\ge c(w):=\frac12+\frac{\gamma_*}{2\pi}.\ }
\]
For every strict weight triple and every \(D>0\), equality is attained by pairwise distinct noncollinear sites of diameter \(D\); collinear equality configurations also exist. For equal weights \(c(w)=2/3\), and equality configurations of sites are precisely the **possibly degenerate isosceles triangles with a longest side as base**: the third site has its orthogonal projection at that base's midpoint, and its distance to either endpoint is at most the base length. This includes the collinear midpoint configuration, omitted by an earlier noncollinear-only classification. At an equality frequency its direction is parallel to that longest base (up to sign).

When the spatial sites are affinely independent, let \(M\in\mathbb R^{d\times2}\) have columns \(c_2-c_1,c_3-c_1\), set \(G=M^TM\), and put
\[
\theta=\arccos\frac{w_3^2-w_1^2-w_2^2}{2w_1w_2},\qquad
z=-\frac{w_1+w_2e^{i\theta}}{w_3},\qquad
\alpha=-\frac1{2\pi}(\theta,\operatorname{Arg}z)^T.
\]
Then \(|z|=1\) and the *complete real zero set* consists of the disjoint affine \((d-2)\)-flats
\[
\boxed{\ \bigcup_{\sigma=\pm1}\ \bigcup_{n\in\mathbb Z^2}
\{MG^{-1}(n+\sigma\alpha)+v:v\in\ker M^T\}.\ }
\]
Its exact nearest-zero radius is
\[
\boxed{\ \kappa(\mu)^2=\min_{\sigma=\pm1}\min_{n\in\mathbb Z^2}
(n+\sigma\alpha)^TG^{-1}(n+\sigma\alpha).\ }
\]
The cosets are distinct and the minimum is finite and positive. For collinear sites the universal bound remains true, but the two phase congruences may be incompatible and zeros need not exist.

## Assumptions and boundary cases

The Fourier convention is \(e^{-2\pi i\xi\cdot x}\); \(\xi\) is a real Euclidean frequency. Weights are strictly positive, sites are pairwise distinct, and only the strict mass-triangle case is covered by the sharp constant and equality classification. In every strict mass triangle \(1/2<c(w)\le2/3\); equality at \(2/3\) holds only for equal weights, and the lower endpoint is approached by nearly degenerate mass triangles. When one weight strictly exceeds the sum of the other two, no Fourier zero is possible for any sites. At equality of a mass-triangle inequality, cancellation can occur only when the two smaller phasors coincide and oppose the largest; such a degenerate case is not covered by the strict-triangle equality theorem.

The complete affine zero-lattice formula requires rank \(M=2\); it does not apply to collinear spatial sites. No conclusion concerns complex frequencies, more than three atoms, nonpositive or complex amplitudes, or noise stability.

## Proof

**1. Triangle of cancellation phases.** Divide a zero equation by the first nonzero exponential. The three complex vectors have prescribed positive lengths \(w_1,w_2,w_3\) and close to a triangle. Under strict triangle inequalities the relative phases are unique up to conjugation and common rotation. With the first phase equal to \(1\), the two possibilities are \((e^{i\theta},z)\) and \((e^{-i\theta},\bar z)\), where \(\theta,z\) are displayed above. This is the cosine rule: \(|w_1+w_2e^{i\theta}|=w_3\).

The cyclic gaps between the three cancelling phase directions are \(\pi-\gamma_1,\pi-\gamma_2,\pi-\gamma_3\). They are all strictly between zero and \(\pi\), and their sum is \(2\pi\). Hence the shortest closed circular arc containing the three directions has length
\[
2\pi-\max_j(\pi-\gamma_j)=\pi+\gamma_*.
\]
In cycles this is precisely \(c(w)\).

**2. Diameter bound and equality geometry.** At any real zero, consider the actual projections \(t_j=\xi\cdot c_j\in\mathbb R\). Their complex phases are \(e^{-2\pi i t_j}\). The image of their containing real interval \([\min_jt_j,\max_jt_j]\) must contain the three cancelling phase directions, so
\[
\max_j t_j-\min_jt_j\ge c(w).
\]
Since for all \(j,k\), \(|t_j-t_k|\le|\xi|\,|c_j-c_k|\le|\xi|D\), we obtain \(|\xi|D\ge c(w)\).

Equality requires, and is equivalent to, both of the following: (a) the three *actual* projections are consecutive lifts of a shortest containing circular arc (no extra winding), and (b) their two extreme sites form a diameter segment parallel to \(\xi\). Indeed these exactly characterize equality in the phase-arc inequality and in Cauchy--Schwarz, and the cancellation-phase condition then makes them sufficient.

For sharpness, choose an orientation of the cancelling phases, rotate their common phase and lift the three phases to projected values \(0,s,c(w)\), with \(0<s<c(w)\). Put the two extreme sites at \((0,0)\) and \((D,0)\), and the middle site at \((Ds/c(w),\varepsilon)\) in a Euclidean plane. For sufficiently small \(\varepsilon>0\) the latter two side lengths are less than \(D\). With \(\xi=(c(w)/D,0)\), choosing the phase orientation compatible with the negative Fourier exponential, the transform vanishes and \(|\xi|D=c(w)\). Setting \(\varepsilon=0\) instead also gives three distinct **collinear** equality sites. The argument embeds in every \(d\ge2\).

For equal weights, the three cancelling phases are equally spaced, so the minimal lift is \(0,1/3,2/3\). Thus the middle site projects to the midpoint of the extreme diameter segment; the set of three sites is an isosceles triangle with that segment as its longest side, allowing zero transverse height. Conversely any such (possibly degenerate) isosceles triangle, with frequency of norm \(2/(3D)\) parallel to the base, realizes phases spaced by \(1/3\) cycle and attains the bound. No positive transverse height is required: the collinear midpoint is a valid equality case.

**3. Full zero set when the site differences have rank two.** Removing the common first exponential reduces the Fourier equation to \(w_1+w_2e^{-2\pi i(M^T\xi)_1}+w_3e^{-2\pi i(M^T\xi)_2}=0\). By Step 1 this holds exactly when
\[
M^T\xi\in (\alpha+\mathbb Z^2)\cup(-\alpha+\mathbb Z^2).
\]
For a prescribed right side \(b\), rank two gives all solutions as \(MG^{-1}b+v\), \(v\in\ker M^T\). The first summand is orthogonal to the kernel, and its squared norm is \(b^TG^{-1}b\). This proves both displayed zero-set and nearest-zero formulas. The two cosets are distinct: if \(2\alpha\in\mathbb Z^2\), both nontrivial phases would be real signs, which cannot form a strict positive mass triangle. Their transverse lattice sets are discrete and avoid the origin; hence the minimum exists and is positive.

When the sites are collinear, rank two fails and the two congruences may be incompatible. Nevertheless Steps 1–2, including the equal-weight collinear midpoint example, remain valid. This completes the corrected theorem.

## Verification and limitations

`checks/tri_atomic_zeros.py` provides supplementary finite numerical tests for phasor closure, rank-two zero cosets, and random site triangles; these tests do not prove any universal statement. An independent exact check of the formerly omitted boundary is \(w_1=w_2=w_3=1\), \(c_1=(0,0)\), \(c_2=(D/2,0)\), \(c_3=(D,0)\), \(\xi=(2/(3D),0)\), where
\[
F(\xi)=1+e^{-2\pi i/3}+e^{-4\pi i/3}=0,\qquad |\xi|D=2/3.
\]
Thus any claim excluding all collinear equal-weight equality configurations is false. The corrected classification includes them while retaining the sharp constant and rank-two formula.

The contribution is a mass-sensitive, sharp finite-atom Fourier-zero bound together with its equality geometry and the rank-two two-coset classification. Its historical priority is provisional; a classical result on three-vector phasors, positive finite characteristic functions, diffraction or array factors may state an equivalent bound. Neither finite testing nor this document establishes novelty or external certification.

## Relationship to prior work

Gómez-Serrano, Levitin, Platt and Polterovich (2026), arXiv:2609.10517, optimize Fourier-zero distance for indicators of centrally symmetric convex bodies with a *fixed-volume* constraint. Benguria, Levitin and Parnovski (2009), JFA 257, 2088–2123, also study domain indicators; Kolountzakis and Révész (2006), CJM 58, 401–418, study pointwise positive-definite-function bounds under support constraints. These objects and constraints do not directly imply the sharp three-atom mass-angle constant and geometry. Discrete three-atom Fourier-zero results count torsion-frequency zeros and do not automatically yield a Euclidean nearest-frequency radius. The phasor triangle identity and the circle-arc observation themselves are elementary antecedents, not claimed as original.

## References

1. J. Gómez-Serrano, M. Levitin, D. Platt, I. Polterovich, *An isoperimetric problem for Fourier zeros of centrally symmetric convex bodies*, arXiv:2609.10517 (2026), https://arxiv.org/abs/2609.10517.
2. R. Benguria, M. Levitin, L. Parnovski, *Fourier transform, null variety, and Laplacian's eigenvalues*, Journal of Functional Analysis 257 (2009), 2088–2123, DOI:10.1016/j.jfa.2009.06.022.
3. M. N. Kolountzakis, Sz. Gy. Révész, *On pointwise estimates of positive definite functions with given support*, Canadian Journal of Mathematics 58 (2006), 401–418, DOI:10.4153/CJM-2006-017-8.
