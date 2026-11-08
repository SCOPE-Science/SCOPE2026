# Sharp quadrupole reconstruction from generalized Clifford hypersurfaces

## Finding

For every integer \(m\ge 2\), let \(\mathcal H_2(S^{2m-1};\mathbb C)\) be the complex vector space of homogeneous degree-two harmonic polynomials restricted to the unit sphere in \(\mathbb R^{2m}\), with normalized spherical \(L^2\) norm. For \(0<t<1\) set
\[
T_t=\{(x,y)\in\mathbb R^m\times\mathbb R^m:\ |x|^2=t,\ |y|^2=1-t\},
\]
and give \(T_t\) the product of normalized surface measures. Let \(R_t f=f|_{T_t}\) be the restriction operator.

**Theorem.** The squared singular spectrum of \(R_t\), including multiplicities, is precisely
\[
\begin{array}{c|c}
\text{eigenvalue of }R_t^*R_t&\text{multiplicity}\\\hline
4(m+1)(t-\tfrac12)^2&1\\
\frac{4(m+1)}{m+2}t^2&\frac{(m-1)(m+2)}2\\
\frac{4(m+1)}{m+2}(1-t)^2&\frac{(m-1)(m+2)}2\\
\frac{4(m+1)}m t(1-t)&m^2.
\end{array}
\]
The restriction is injective exactly when \(t\ne\tfrac12\). Define its spectral condition number as the ratio of largest to smallest singular value, with \(+\infty\) when the least value is zero. Then
\[
\boxed{\min_{0<t<1}\kappa(R_t)=1+\frac{2}{\sqrt{m+2}}},
\]
and the **only** minimizing squared radii are
\[
\boxed{t_-=\frac{\sqrt{m+2}}{2(1+\sqrt{m+2})},\qquad t_+=1-t_-.}
\]
The **same two radii** uniquely maximize the least eigenvalue over \(0<t<1\), with the sharp value
\[
\boxed{\max_{0<t<1}\lambda_{\min}(R_t^*R_t)=\frac{m+1}{(1+\sqrt{m+2})^2}}.
\]
In particular, no single such hypersurface is a tight restriction frame on the full quadrupole space, even though the optimal condition number decreases strictly to \(1\) as \(m\to\infty\). For \(m=2\), the sharp condition number is \(2\), attained exactly at \(t=1/3\) and \(t=2/3\).

## Assumptions and scope

Here the ambient sphere is \(S^{2m-1}\subset\mathbb R^{2m}\), not a sphere of real dimension \(2m\). The input norm is the probability-normalized full-sphere \(L^2\) norm, and the output norm is the probability-normalized intrinsic measure on the entire homogeneous hypersurface \(T_t=\sqrt t\,S^{m-1}\times\sqrt{1-t}\,S^{m-1}\). These measures and norms do not depend on the area of the respective surfaces. All quadrupole coefficients may be complex. The theorem optimizes only over this one-parameter family of equal-block product hypersurfaces, not over arbitrary submanifolds or finite point samples.

## Proof

Write a point of \(\mathbb R^{2m}\) as \(z=(x,y)\). Every input is \(f_Q(z)=z^TQz\) for a unique complex symmetric trace-zero matrix \(Q\). The full-sphere second and fourth moments are
\[
\mathbb E[z_i z_j]=\delta_{ij}/n,\qquad
\mathbb E[z_i z_j z_k z_\ell]=
\frac{\delta_{ij}\delta_{k\ell}+\delta_{ik}\delta_{j\ell}+\delta_{i\ell}\delta_{jk}}{n(n+2)},\quad n=2m.
\]
Consequently \(\|f_Q\|_{S^{2m-1}}^2=2\operatorname{tr}(QQ^*)/[2m(2m+2)]\). Use the orthogonal decomposition of complex harmonic quadratics into: the scalar \(Z=|x|^2-|y|^2\); traceless quadratics only in \(x\); traceless quadratics only in \(y\); and mixed bilinear forms \(x^TBy\). Their complex dimensions are respectively \(1\), \((m-1)(m+2)/2\), \((m-1)(m+2)/2\), and \(m^2\). Orthogonality for both input and output follows from separate sign and orthogonal invariance in the two coordinate blocks, or by direct vanishing of their cross-moments.

For traceless \(m\times m\) symmetric \(A\), the full-sphere mean square of \(x^TAx\) is \(2\operatorname{tr}(AA^*)/[2m(2m+2)]\), while its \(T_t\) mean square is \(2t^2\operatorname{tr}(AA^*)/[m(m+2)]\). Their ratio is \(4(m+1)t^2/(m+2)\); replacing \(t\) with \(1-t\) gives the other traceless sector. For a mixed polynomial \(x^TBy\), the full-sphere mean square is \(\operatorname{tr}(BB^*)/[2m(2m+2)]\), and the product-sphere mean square is \(t(1-t)\operatorname{tr}(BB^*)/m^2\); the ratio is \(4(m+1)t(1-t)/m\).

For the scalar sector, let \(U=|x|^2\) at a random point of the full sphere. Then \(U\) has beta distribution with both shape parameters \(m/2\), so \(\mathbb E U=1/2\), \(\operatorname{Var}(U)=1/[4(m+1)]\), and \(\mathbb E Z^2=1/(m+1)\). On \(T_t\), \(Z=2t-1\), giving the ratio \(4(m+1)(t-1/2)^2\). The four ratios and sector dimensions establish the entire singular spectrum. For \(0<t<1\), all values are strictly positive except the scalar one at \(t=1/2\), proving injectivity precisely as stated.

It remains to prove global sharpness, not merely stationarity. Symmetry interchanging the coordinate blocks sends \(t\) to \(1-t\), so assume \(0<t<1/2\). Denote the four spectral values by \(\lambda_Z,\lambda_X,\lambda_Y,\lambda_M\). Throughout this half interval, \(\lambda_X<\lambda_Y\) and
\[
\frac{\lambda_M}{\lambda_X}=\frac{m+2}{m}\frac{1-t}{t}>1.
\]
Hence the least eigenvalue is \(\min\{\lambda_X,\lambda_Z\}\). As \(t\) increases from zero to one half, \(\lambda_X\) increases strictly and \(\lambda_Z\) decreases strictly, meeting exactly at
\[
t_-=\frac{\sqrt{m+2}}{2(1+\sqrt{m+2})}.
\]
This already proves that \(t_-\) uniquely maximizes the least eigenvalue on the half interval. For \(t<t_-\), the denominator of the squared condition number is \(\lambda_X\), and each of \(\lambda_Y/\lambda_X\), \(\lambda_M/\lambda_X\), and \(\lambda_Z/\lambda_X\) decreases strictly with \(t\). For \(t>t_-\), that denominator is \(\lambda_Z\), while each of \(\lambda_X/\lambda_Z\), \(\lambda_Y/\lambda_Z\), and \(\lambda_M/\lambda_Z\) increases strictly. Therefore \(\kappa(R_t)\) strictly decreases until \(t_-\) and strictly increases afterward on the injective portions of this half interval.

At \(t=t_-\), the comparison \(\lambda_Y\ge\lambda_M\) is equivalent to \(\sqrt{m+2}\le m\), true for every integer \(m\ge2\), with equality only when \(m=2\). Thus the largest eigenvalue at \(t_-\) is \(\lambda_Y\), and the smallest is \(\lambda_X=\lambda_Z\). Their square-root ratio is \((1-t_-)/t_-=1+2/\sqrt{m+2}\). Substitution gives the asserted sharp least eigenvalue. Symmetry produces exactly the second optimizer \(t_+=1-t_-\). The two traceless eigenvalues can coincide only at \(t=1/2\), where the scalar eigenvalue is zero; this excludes a tight invertible frame anywhere in this family. All endpoints are excluded from the domain, and their limiting restriction maps are also singular.

## Verification

The accompanying standard-library Python checker, `checker.py`, constructs a complete basis of complexified real harmonic quadratics and compares the ambient and hypersurface Gram forms entry by entry at rational radii for dimensions \(4\), \(6\), and \(8\). It uses explicit, degree-four-exact positive cubature on each sphere (coordinate axes plus the full normalized sign cube), exact rational arithmetic, and an independently assembled product-sphere Gram formula. The checker establishes \(4{,}779\) exact test assertions, including full cross-sector orthogonality, the predicted Gram scalings, the balanced-radius null vector, and representative numerical optimization checks. Execute `python3 checker.py`. The all-dimensional sharpness proof is the analytic argument above; finite tests are corroboration, not its substitute.

## Relationship to prior work

Zandieh, Han, and Avron establish nearly dimension-optimal reconstruction of low-degree spherical harmonic expansions using random full-sphere samples. Bangun, Behboodi, and Mathar study low-coherence deterministic spherical-harmonic sensing matrices. Both provide the mathematical motivation for stable spherical sampling, but their reported theorems concern full-sphere finite-sample reconstruction or mutual coherence, not continuous restriction to a generalized Clifford hypersurface with the present exact all-dimensional spectral optimization. Roddy and McEwen study spherical Slepian functions and localized wavelets on incomplete spheres, a related but different concentration setting. The classical sphere fourth-moment identity and the subgroup-invariant decomposition are standard ingredients; the claim here is the combined four-sector spectral formula and sharp joint optimizer classification for the stated natural family. Equivalent statements under isoparametric or product-sphere terminology remain a historical-priority risk.

## Limitations

No optimality is asserted among arbitrary hypersurfaces, point designs, weighted observations, noisy random sampling schemes, or nonquadratic harmonics. The equatorial balanced product \(t=1/2\) loses precisely the scalar harmonic \(|x|^2-|y|^2\), so it cannot recover all quadrupoles. The small condition number of the optimal product surface as dimension increases is a statement about normalized exact \(L^2\) trace measurements, not experimental robustness to finite spatial discretization. Independent mathematical validation has not been conducted.

## References

1. A. Zandieh, I. Han and H. Avron, *Near Optimal Reconstruction of Spherical Harmonic Expansions*, arXiv:2202.12995, first posted 2022-02-25, https://arxiv.org/html/2202.12995v1.
2. A. Bangun, A. Behboodi and R. Mathar, *Sensing Matrix Design and Sparse Recovery on the Sphere and the Rotation Group*, arXiv:1904.11596, first posted 2019-04-25, https://arxiv.org/html/1904.11596v2.
3. P. J. Roddy and J. D. McEwen, *Slepian Scale-Discretised Wavelets on the Sphere*, arXiv:2106.02023, first posted 2021-06-03, https://arxiv.org/abs/2106.02023.
