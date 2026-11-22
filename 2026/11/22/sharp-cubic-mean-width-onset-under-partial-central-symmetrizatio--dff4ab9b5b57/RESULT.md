# Sharp cubic mean-width onset under partial central symmetrization of the Veronese orbitope

## Finding

Let \(E=\{A\in\operatorname{Sym}_3(\mathbb R):\operatorname{tr}A=0\}\) carry the Frobenius inner product \(\langle A,B\rangle=\operatorname{tr}(AB)\), so \(\dim E=5\). Let
\[
p(u)=\frac{uu^{\mathsf T}-I/3}{\sqrt2}\quad(u\in S^2),\qquad K=\operatorname{conv}\{p(u):u\in S^2\}.
\]
For \(0\le t\le1\) set \(K_t=\operatorname{conv}(K\cup(-tK))\). With \(d\sigma\) the uniform **probability** measure on the Frobenius unit sphere \(S(E)\), define the Euclidean mean width
\[
\mathcal W(t)=\int_{S(E)}[h_{K_t}(A)+h_{K_t}(-A)]\,d\sigma(A),\qquad h_C(A)=\max_{x\in C}\langle A,x\rangle.
\]
Then \(K_t=K\) if and only if \(0\le t\le1/2\). Moreover, throughout the full interval \(0\le t\le1\),
\[
\boxed{\mathcal W(t)=\frac{9\sqrt3}{16}+\begin{cases}
0,&0\le t\le\frac12,\\[2pt]
\displaystyle\frac{\sqrt3(2t-1)^3}{4[3+(2t-1)^2]},&\frac12<t\le1.
\end{cases}}
\]
Consequently \(\mathcal W\) is constant on \([0,1/2]\), strictly increasing on \((1/2,1]\), and is \(C^2\) but not \(C^3\) at \(t=1/2\), with sharp onset
\[
\mathcal W(\tfrac12+\delta)-\mathcal W(\tfrac12)=\frac{2}{\sqrt3}\delta^3+O(\delta^5)
\quad(\delta\downarrow0).
\]
At the fully centrally symmetrized endpoint, \(\mathcal W(1)=5\sqrt3/8\).

## Assumptions and scope

All matrices are real and symmetric. Eigenvalues are ordered \(\lambda_+\ge\lambda_0\ge\lambda_-\), all scalar products and widths use the Frobenius Euclidean metric, and \(S(E)\) is the **four-dimensional unit sphere** in the five-dimensional space \(E\). The set \(K\) has diameter one; its extreme points form the classical real-projective Veronese projector surface. The convex hull operation \(K_t\) is the specified *partial reflection hull*, not a Minkowski average or a centered dilation. Statements apply exactly for \(0\le t\le1\); no extension outside this range is claimed.

## Proof

**1. Spectrahedral containment and threshold.** Every \(Q\succeq0\) with \(\operatorname{tr}Q=1\) is a convex combination of rank-one projectors, hence
\[
K=\left\{\frac{Q-I/3}{\sqrt2}:Q\succeq0,\ \operatorname{tr}Q=1\right\}.
\]
For an extreme point \(p(u)\), the point \(-t p(u)\) corresponds to
\[
Q_t=(1+t)I/3-tuu^{\mathsf T}.
\]
Its eigenvalues are \((1-2t)/3\) once and \((1+t)/3\) twice. Thus \(-t p(u)\in K\) precisely when \(t\le1/2\). By convexity this is equivalent to \(-tK\subset K\), and for \(t>1/2\) any such \(-tp(u)\notin K\) proves strict enlargement.

**2. Direct support in any direction.** If \(A\in S(E)\) has largest and smallest eigenvalues \(L>0\) and \(\ell<0\), the Rayleigh principle gives
\[
h_K(A)=L/\sqrt2,\quad h_K(-A)=-\ell/\sqrt2,
\quad w_t(A)=\frac{\max\{L,-t\ell\}+\max\{-\ell,tL\}}{\sqrt2}.
\]
Equal eigenvalues are harmless since they form a zero-measure subset and the formula remains continuous.

**3. Exact spherical eigenvalue law.** Orthogonal diagonalization writes \(A=R\operatorname{diag}(\lambda_i)R^{\mathsf T}\). On distinct-spectrum matrices, the off-diagonal derivatives with respect to the infinitesimal rotation coordinates \(\Omega_{ij}\) are \((\lambda_j-\lambda_i)\Omega_{ij}\), so the invariant Euclidean volume Jacobian contains \(\prod_{i<j}|\lambda_i-\lambda_j|\). The trace-zero and Frobenius-one constraints reduce the eigenvalues to one angular coordinate, with constant angular speed. For \(0\le\theta\le\pi/3\) an ordered parametrization is
\[
L=\sqrt{\frac23}\cos\theta,\quad
\ell=\sqrt{\frac23}\cos(\theta+\tfrac{2\pi}{3}),\quad
\lambda_0=\sqrt{\frac23}\cos(\theta+\tfrac{4\pi}{3}).
\]
The Vandermonde product is proportional to \(\sin3\theta\), and \(\int_0^{\pi/3}\sin3\theta\,d\theta=2/3\); therefore **the exact probability density** of \(\theta\) is \(\frac32\sin3\theta\). This also follows directly by combining the Jacobian of conjugation with normalized Haar measure on eigenframes; no unnormalized Gaussian scale is introduced.

**4. The switch region.** At \(t\le1/2\), Step 1 implies \(w_t=w_0\). Step 2 and the angular parametrization give
\[
w_0(\theta)=\sin(\theta+\pi/3),\qquad
\mathcal W(0)=\frac32\int_0^{\pi/3} \sin(\theta+\pi/3)\sin3\theta\,d\theta=\frac{9\sqrt3}{16}.
\]
For \(t>1/2\), put \(k=(2t-1)/\sqrt3\) and \(\alpha=\arctan k\). Since \(0<\alpha\le\pi/6\), the two disjoint switching intervals are \([0,\alpha]\) and \([\pi/3-\alpha,\pi/3]\). On the first one, the \(tL\) branch replaces \(-\ell\), and the exact increase over \(w_0\) is
\[
\frac{1+t}{\sqrt3}\cos\theta-\sin(\theta+\pi/3)
=\frac12(k\cos\theta-\sin\theta).
\]
The other interval gives the same contribution by \(\theta\leftrightarrow\pi/3-\theta\). Thus
\[
\mathcal W(t)-\mathcal W(0)
=\frac32\int_0^{\alpha}(k\cos\theta-\sin\theta)\sin3\theta\,d\theta.
\]
Elementary product-to-sum integration gives the antiderivative result
\[
\frac{9k}{16}-\frac{3(3k-k^3)}{16(1+k^2)}=\frac{3k^3}{4(1+k^2)}.
\]
Substituting \(k=(2t-1)/\sqrt3\) gives the stated closed expression, for every \(t\) in the asserted interval.

**5. Monotonicity and regularity.** The increment \(3k^3/[4(1+k^2)]\) has derivative \(3k^2(3+k^2)/[4(1+k^2)^2]>0\) for \(k>0\). Its expansion is \(3k^3/4+O(k^5)\), yielding the stated cubic coefficient and second-order contact at \(t=1/2\). The third derivative in \(t\) jumps from zero on the left to \(4\sqrt3\) on the right. Setting \(t=1\) yields \(5\sqrt3/8\).

## Verification

Run `python verify.py` from the same directory. The self-contained checker numerically integrates the **direct maximum-of-eigenvalues support function** over the exact angular eigenvalue density, comparing with the closed formula at nine parameters. If NumPy is installed, a separate 160,000-sample experiment draws uniform directions from the entire five-dimensional Frobenius unit sphere, builds their matrices in an orthonormal basis, diagonalizes numerically, and compares mean widths at seven parameters. Both verifications passed. Numerical integration and sampling corroborate, but do not replace, the exact analytic argument.

## Relationship to prior work

Arman–Bondarenko–Prymak–Radchenko (2026) introduce this diameter-one five-dimensional Veronese projector model and prove a six-ball noncovering theorem. Their Section 2 gives its spectrahedral convex hull and studies ball preimages, not partial reflection hulls or mean width. Sanyal–Sottile–Sturmfels (2011) develop general orbitopes, concentrating in the Veronese section on high-degree forms and algebraic structure; their results do not give the displayed phase profile. Sanyal–Saunderson (2025) give general spectral convex-set calculus and a Steiner-polynomial integral formula; this is relevant broader background, but they do not state this particular one-parameter reflection-hull width, threshold, or sharp cubic constant. The eigenvalue-Jacobian method is standard, and no priority is asserted for it. The candidate contribution is the **explicit complete shape-response law and the exact third-order onset**.

## Limitations

The calculation is specific to the trace-zero real symmetric \(3\times3\) rank-one projector hull and Euclidean mean width. It does not imply an analogous law for higher matrix ranks, complex-Hermitian spectrahedra, surface area, volume, ball-covering numbers, or other symmetrization conventions. The originality assessment rests on accessible published sources and searchable records; earlier unindexed versions or equivalent special-function formulas may exist. The numerical certificate is finite; the all-parameter statement is justified by the proof above. Independent audit has not been performed.

## References

1. A. Arman, A. Bondarenko, A. Prymak, D. Radchenko, *A diameter-one set in \(\mathbb R^5\) that cannot be covered by six diameter-one balls*, arXiv:2611.08198v1 (first public 5 November 2026), https://arxiv.org/html/2611.08198v1.
2. R. Sanyal, F. Sottile, B. Sturmfels, *Orbitopes*, Mathematika 57 (2011), 275–314, arXiv:0911.5436, https://franksottile.github.io/research/pdf/Orbitope.pdf.
3. R. Sanyal, J. Saunderson, *Spectral Polyhedra*, Forum of Mathematics, Sigma 13 (2025), e30, https://doi.org/10.1017/fms.2024.62.
