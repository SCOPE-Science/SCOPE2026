# Universal small-angle false-acceptance law for two-column sketch conditioning

## Finding

Let \(k\ge 2\) and \(K>1\) be fixed. Let \(X,Y\in\mathbb R^k\) be independent random vectors. Assume that \(X\) has a bounded Lebesgue density \(f\) continuous at the origin and that \(\mathbb E\|Y\|_2^k<\infty\). Set
\[
M_\theta=[X,\ (\cos\theta)X+(\sin\theta)Y],\qquad 0<\theta<\pi/2,
\]
and let \(\kappa_2\) be the ratio of largest and smallest singular values, defined to be \(+\infty\) for a rank-deficient two-column matrix. Then
\[
\boxed{\lim_{\theta\downarrow0}\theta^{-k}\Pr\{\kappa_2(M_\theta)\le K\}
=\frac{f(0)\,\mathbb E\|Y\|_2^k}{2^k}\,V_k(K),}
\]
where the strictly positive geometric factor is
\[
\boxed{V_k(K)=\frac{4\pi^{(k-1)/2}}{\Gamma((k-1)/2)}
\int_{1/K}^{K}b^{k-2}\sqrt{(K-b)(b-K^{-1})}\,db.}
\]
The leading coefficient depends on the law of \(X\) only through its density at the origin and on the law of \(Y\) only through one radial moment. When \(f(0)>0\) and \(\Pr\{Y\ne0\}>0\), this is a sharp positive order-\(\theta^k\) asymptotic. The conclusion remains valid if either coefficient vanishes, in which case the probability is \(o(\theta^k)\).

For independent standard Gaussian \(X,Y\),
\[
\lim_{\theta\downarrow0}\theta^{-k}\Pr\{\kappa_2(M_\theta)\le K\}
=\frac{\Gamma(k)}{(4\pi)^{k/2}\Gamma(k/2)}V_k(K).
\]
For \(k=2\), the coefficient is \((K-K^{-1})^2/8\); for \(k=3\), it is \((K-K^{-1})^2(K+K^{-1})/8\).

## Assumptions and scope

All matrices and random vectors are real. The density of \(X\) is essentially bounded on \(\mathbb R^k\) and has a representative continuous at \(0\). The random vectors \(X\) and \(Y\) are independent, but need not be centered, isotropic, Gaussian, identically distributed, or rotationally invariant. The only required tail assumption is \(\mathbb E\|Y\|_2^k<\infty\). We do not normalize the two observed columns individually after forming \(M_\theta\).

One numerical-linear-algebra realization is an orthonormal pair \(u,w\) in \(\mathbb R^N\), with \(N\ge2\), and a real Gaussian sketch \(S\in\mathbb R^{k\times N}\). The unsketched basis \(B_\theta=[u,(\cos\theta)u+(\sin\theta)w]\) has \(\kappa_2(B_\theta)=\cot(\theta/2)\), while \(SB_\theta\) has precisely the distribution of \(M_\theta\), up to a harmless common scale. Thus the event is a fixed-threshold false acceptance of an arbitrarily ill-conditioned raw basis. The theorem is a statement about this conditioning test, not about any particular algorithm's stopping-time distribution.

## Proof

**Step 1: the rare-event scale.** For \(c=\cos\theta\), \(s=\sin\theta\), apply the unit coefficient vector \((-c,1)/\sqrt{1+c^2}\) to the columns of \(M_\theta\). This gives
\[
\sigma_{\min}(M_\theta)\le \frac{s\|Y\|_2}{\sqrt{1+c^2}},
\qquad \sigma_{\max}(M_\theta)\ge\|X\|_2.
\]
Therefore \(\kappa_2(M_\theta)\le K\) implies
\[
\|X\|_2\le\frac{Ks}{\sqrt{1+c^2}}\|Y\|_2
\le K\theta\|Y\|_2.
\]
This localization is the key to justifying the limiting density substitution, not merely a heuristic rare-event argument.

**Step 2: the rescaled integral.** Substitute \(X=\theta z\) in the density integral. With \(q_\theta=\sin\theta/\theta\),
\[
\theta^{-k}\Pr\{\kappa_2(M_\theta)\le K\}
=\mathbb E_Y\int_{\mathbb R^k}f(\theta z)
\mathbf 1\{\kappa_2([z,cz+q_\theta Y])\le K\}\,dz.
\]
By Step 1 the integrand can be nonzero only for \(\|z\|_2\le K\|Y\|_2\). It is bounded by \(\|f\|_\infty\), so its integral is bounded by a constant times \(\|Y\|_2^k\), which is integrable. For each fixed nonzero \(Y\), the conditioning indicator converges for Lebesgue-almost every \(z\): the boundary is a proper algebraic hypersurface determined by the Gram-matrix eigenvalue ratio. For \(Y=0\), the matrix has rank at most one, and both indicators vanish. Dominated convergence gives
\[
\lim_{\theta\downarrow0}\theta^{-k}\Pr\{\kappa_2(M_\theta)\le K\}
=f(0)\mathbb E_Y\operatorname{Vol}_k
\{z:\kappa_2([z,z+Y])\le K\}.
\]

**Step 3: an exact universal geometric volume.** Right-multiply \([z,z+Y]\) by the orthogonal matrix with columns \((1,1)^\mathsf T/\sqrt2\) and \((-1,1)^\mathsf T/\sqrt2\). This produces \([r,s]\) with \(r=(2z+Y)/\sqrt2\) and \(s=Y/\sqrt2\). For fixed \(Y\), the change in volume is \(dz=2^{-k/2}\,dr\). By orthogonal invariance and homogeneity, the volume of all \(r\) satisfying \(\kappa_2([r,s])\le K\) equals \(\|s\|_2^k V_k(K)\), where \(V_k(K)\) is the corresponding volume when \(s=e_1\). Consequently,
\[
\operatorname{Vol}_k\{z:\kappa_2([z,z+Y])\le K\}
=2^{-k}\|Y\|_2^k V_k(K).
\]
To calculate \(V_k(K)\), decompose \(r=ae_1+v\), with \(v\perp e_1\) and \(b=\|v\|_2\). The trace and determinant of the \(2\times2\) Gram matrix of \([r,e_1]\) are \(1+a^2+b^2\) and \(b^2\). Since its eigenvalue ratio is at most \(K^2\) exactly when
\[
\frac{b^2}{(1+a^2+b^2)^2}\ge\frac{K^2}{(1+K^2)^2},
\]
this condition is equivalent to
\[
K^{-1}\le b\le K,
\qquad a^2\le(K-b)(b-K^{-1}).
\]
Integrating first in \(a\) and then in polar coordinates in \(e_1^\perp\) gives the stated integral, since the surface area of the unit sphere in \(\mathbb R^{k-1}\) is \(2\pi^{(k-1)/2}/\Gamma((k-1)/2)\). Combining Steps 2 and 3 proves the theorem.

**Step 4: Gaussian constants.** For standard Gaussian \(X\), \(f(0)=(2\pi)^{-k/2}\). Independently, \(\|Y\|_2\) has the chi distribution with \(k\) degrees of freedom, and
\[
\mathbb E\|Y\|_2^k=2^{k/2}\Gamma(k)/\Gamma(k/2).
\]
For \(k=2\) and \(k=3\), the remaining one-dimensional volume integral reduces respectively to the displayed elementary expressions. This completes the proof.

## Verification

The standalone `verify.py` recomputes the geometric integral by adaptive quadrature, checks the \(k=2,3\) Gaussian formulas against exact-rational values at \(K=5/2\), and uses importance sampling in the rare-event scale to compare the predicted leading coefficients with small positive \(\theta\). It includes Gaussian, uniform-cube, and product-Laplace densities for \(X\), with Gaussian \(Y\), to check the distribution-free dependence. Run `python verify.py` with Python 3, NumPy and SciPy. These finite computations illustrate and check the constants; the limit is established by the analytic dominated-convergence proof above.

## Relationship to prior work

Güttel, Liu and Nyman (arXiv:2607.10354v1, July 11, 2026; v2 October 27) use sketch-estimated basis conditioning to choose adaptive restart dimensions for matrix-function Krylov methods. Their framework motivates distinguishing the true basis condition number from the sketched threshold event. The present theorem does not analyze their complete algorithm and is not stated to be an improvement to its convergence guarantees. Güttel and Simunec (arXiv:2306.03592) study conditioning and selection in sketched Arnoldi bases. Classical Gaussian/Wishart condition-number distributions (Edelman; Anderson and Wells) are concerned with iid Gaussian matrices, while Wirtz and Guhr analyze correlated Gaussian Wishart eigenvalues; none of those models alone supplies the theorem's distribution-free density-at-zero and radial-moment law for independently sampled \(X,Y\). This comparison is about the stated scopes, not a claim that no alternate derivation exists.

## Limitations

The limit holds with \(k\) and \(K\) fixed as \(\theta\downarrow0\); it is not uniform in sketch width or threshold. It requires independent \(X\) and \(Y\), a bounded density of \(X\) continuous at the origin, and a finite \(k\)th moment of \(Y\). It does not directly cover structured sketches that induce dependence between the projected orthogonal directions, individually renormalized columns, floating-point conditioning estimates, or multi-step stopping histories. It gives an exact rare-event asymptotic, not a finite-angle deterministic upper bound. Historical priority remains subject to possible unindexed equivalent small-noise condition-number analyses.

## References

1. S. Güttel, J. Liu, L. Nyman, *Sketch-and-Restart: Randomized Sketching in Quadrature-Based Restarting for Matrix Functions*, arXiv:2607.10354, first posted July 11, 2026. https://arxiv.org/abs/2607.10354
2. S. Güttel, I. Simunec, *A sketch-and-select Arnoldi process*, arXiv:2306.03592, June 6, 2023. https://arxiv.org/abs/2306.03592
3. A. Edelman, *Eigenvalues and Condition Numbers of Random Matrices*, SIAM J. Matrix Anal. Appl. 9 (1988), 543–560. https://doi.org/10.1137/0609045
4. W. Anderson, M. Wells, *The Exact Distribution of the Condition Number of a Gaussian Matrix*, SIAM J. Matrix Anal. Appl. 31 (2009), 1125–1130. https://doi.org/10.1137/070698932
5. T. Wirtz, T. Guhr, *Distribution of the Smallest Eigenvalue in the Correlated Wishart Model*, arXiv:1306.4790 (2013). https://arxiv.org/abs/1306.4790
