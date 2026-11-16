# The exact fastest fixed-geodesic-step averaging walk on the two-sphere

## Finding

Let \(T_\theta\) average a function on the unit two-sphere over the geodesic circle at angle \(\theta\) from its argument, with normalized uniform arc measure. Let \(L^2_0(S^2)\) be the mean-zero complex \(L^2\) space with normalized area measure. Among **all** fixed angles \(\theta\in[0,\pi]\), the sharp contraction factor is

\[
\min_{0\le\theta\le\pi}\|T_\theta\|_{L^2_0\to L^2_0}
=\rho_*:=\frac{2+3\sqrt6}{25}=0.373938769133981\ldots.
\]

There are exactly two minimizing angles,
\[
\theta=\arccos\frac{\sqrt6-1}{5}\quad\text{or}\quad
\theta=\pi-\arccos\frac{\sqrt6-1}{5},
\]

namely approximately \(73.1481535488^\circ\) and \(106.8518464512^\circ\). At each angle, **exactly the harmonic degrees two and three** attain operator-norm equality; together their eigenspaces have dimension \(5+7=12\). All other nonconstant harmonic degrees contract strictly faster. For every integer \(k\ge1\), the minimum \(k\)-step norm is \(\rho_*^k\), at precisely the same two angles.

## Assumptions and scope

The sphere is \(S^2=\{x\in\mathbb R^3:\|x\|=1\}\). With \(e_1,e_2\) any orthonormal basis of \(x^\perp\), define, for \(0\le\theta\le\pi\),
\[
(T_\theta f)(x)=\frac1{2\pi}\int_0^{2\pi}
 f\!\left(\cos\theta\,x+\sin\theta(\cos t\,e_1+\sin t\,e_2)\right)\,dt.
\]
The definition is independent of the tangent basis. The area measure is normalized to mass one; \(T_\theta\) is a self-adjoint rotation-equivariant Markov operator on \(L^2(S^2)\), fixing constants. \(L^2_0\) is its orthogonal complement of constants. Only **one deterministic geodesic step length**, with uniformly randomized tangent direction at each step, is optimized. The statement does not concern arbitrary mixtures of step lengths, Wasserstein distance, discrepancy, or total variation from a point mass.

## Proof

**1. Exact multipliers.** By the Funk–Hecke spherical convolution formula, the degree-\(\ell\) spherical-harmonic space \(\mathcal H_\ell\) is an eigenspace with scalar eigenvalue \(P_\ell(\cos\theta)\), where \(P_\ell(1)=1\) denotes the Legendre polynomial. The orthogonal Hilbert sum \(L^2_0(S^2)=\bigoplus_{\ell\ge1}\mathcal H_\ell\) therefore gives
\[
\|T_\theta\|_{L^2_0\to L^2_0}=\sup_{\ell\ge1}|P_\ell(\cos\theta)|.
\]
As \(P_\ell(-x)=(-1)^\ell P_\ell(x)\), the objective is even in \(x=\cos\theta\). We need only consider \(0\le x\le1\).

**2. Global lower bound and uniqueness of the candidate.** Put
\[
a=\frac{\sqrt6-1}{5},\qquad r=\frac{2+3\sqrt6}{25}.
\]
Direct substitution into \(P_1(x)=x\), \(P_2(x)=(3x^2-1)/2\), and \(P_3(x)=(5x^3-3x)/2\) shows
\[
0<a<r<\frac25<\frac1{\sqrt5},\qquad
P_2(a)=P_3(a)=-r.
\]
For \(0\le x<a\), strict monotonicity of \(P_2\) on nonnegative \(x\) gives \(|P_2(x)|>r\). For \(a<x\le r\), \(P_3'(x)=(15x^2-3)/2<0\) on \([a,r]\), giving \(P_3(x)<-r\). For \(x>r\), \(|P_1(x)|=x>r\). Thus \(\sup_{\ell\ge1}|P_\ell(x)|\ge r\) everywhere, and equality can hold only at \(x=a\). Evenness then leaves only \(x=\pm a\) as possible minimizers.

**3. All higher degrees are strictly smaller at the candidate.** The first two degrees have \(P_1(a)=a<r\) and \(|P_2(a)|=|P_3(a)|=r\). The next two are exactly
\[
P_4(a)=\frac{-41+26\sqrt6}{250},\qquad
P_5(a)=\frac{2173-3\sqrt6}{6250}.
\]
Both are positive and strictly smaller than \(r\). Indeed
\[
r-P_4(a)=\frac{61+4\sqrt6}{250}>0,\qquad
r-P_5(a)=\frac{753\sqrt6-1673}{6250}>0.
\]
For the entire remaining infinite family use Laplace's exact integral representation for Legendre polynomials. Let \(b=\sqrt{1-a^2}\). For every integer \(\ell\ge0\),
\[
P_\ell(a)=\frac1\pi\int_0^\pi(a+ib\cos t)^\ell\,dt.
\]
For completeness, summing the integrals against \(z^\ell\) for sufficiently small \(|z|\), then integrating the geometric series, gives \((1-2az+z^2)^{-1/2}\), the Legendre generating function. Since \(|a+ib\cos t|^2=a^2+(1-a^2)\cos^2t\le1\), every \(\ell\ge6\) satisfies
\[
|P_\ell(a)|\le\frac1\pi\int_0^\pi
\big(a^2+(1-a^2)\cos^2t\big)^3\,dt=:B_6.
\]
Using the exact cosine even moments \(\frac1\pi\int_0^\pi\cos^{2j}t\,dt=\binom{2j}{j}/4^j\) for \(j=0,1,2,3\), expansion yields
\[
B_6=\frac{1262}{3125}-\frac{189\sqrt6}{6250}
=0.329767430178236\ldots<r,
\quad
r-B_6=\frac{939\sqrt6-2024}{6250}>0.
\]
Consequently **every** degree \(\ell\ge6\) is strictly below \(r\); no finite enumeration is being used to infer an infinite bound. Combining all degrees proves \(\|T_\theta\|\) has sharp minimum \(r\) only at \(\cos\theta=\pm a\), with equality restricted to \(\mathcal H_2\oplus\mathcal H_3\). At \(x=a\) both eigenvalues are \(-r\); at \(x=-a\) the degree-two multiplier is \(-r\) and the degree-three multiplier is \(+r\). Their dimensions are \(2\ell+1=5,7\).

**4. Iteration.** Self-adjoint harmonic diagonalization gives \(\|T_\theta^k\|_{L^2_0\to L^2_0}=\sup_{\ell\ge1}|P_\ell(\cos\theta)|^k=\|T_\theta\|^k\) for each positive integer \(k\). Strict monotonicity of raising a nonnegative number to \(k\) preserves exactly the same optimizers.

## Verification

The accompanying standalone \(verify.py\), using only the Python standard library, checks the exact rational-quadratic identities, the strict inequalities through rational enclosures \(2449/1000<\sqrt6<49/20\), and 1,510 supplemental Legendre/angle comparisons. Running `python verify.py` reports PASS. In particular the code checks the exact \(B_6\) formula, while the analytical Laplace estimate above establishes the infinitely many higher-degree bounds. Numerical tests alone are not used as proof.

## Relationship to prior work

The fixed-angle walk is the same model as Francis Edward Su's 2001 study of spherical drunkard walks [1], which explicitly obtains the Legendre multiplier \(P_\ell(\cos\theta)\) and derives discrepancy mixing bounds. The inspected main theorems, estimates, conclusion, and relevant appendix of [1] address discrepancy rates rather than the exact minimax of the complete \(L^2\) spectrum over the angle, and do not state the two algebraic optimum angles.

Mangoubi and Smith [2] analyze geodesic walks on positive-curvature manifolds by Wasserstein contraction, using a fixed geodesic integration time; their inspected Algorithm 1 and Theorem 5 give general-manifold mixing bounds, not the sharp fixed-angle \(S^2\) spectral minimax. Schär and Stier [3] analyze a different geodesic-slice walk, uniformizing the angle along a selected great circle, and establish dimension-independent Wasserstein contraction. The present exact single-step-angle \(L^2\) optimization is neither a special case nor a numerical sharpening of that Wasserstein theorem. Related group-conjugacy random walks have character-ratio spectra rather than the \(SO(3)/SO(2)\) Legendre spectrum; their optimizing parameters do not imply the present statement. The analytical ingredients (Funk–Hecke formula, Legendre identities) are classical; novelty is asserted only for their sharp global fixed-angle spectral-design consequence, subject to the limitation below.

## Limitations

This theorem optimizes the induced mean-zero \(L^2\) operator norm, not convergence in total variation, discrepancy or Wasserstein metrics. It assumes an exactly uniform tangent direction and precisely one deterministic step length in \([0,\pi]\). It does not optimize mixtures of step lengths, non-isotropic moves, other sphere dimensions or group conjugacy kernels. Although relevant full-text works were compared by claims and implications, an earlier specialized Legendre-polynomial minimax result outside the searched literature might subsume the exact optimum; historical priority has not been independently established.

## References

[1] Francis Edward Su, *Discrepancy convergence for the drunkard's walk on the sphere*, 2001, https://arxiv.org/abs/math/0102205 (initial public preprint February 27, 2001).

[2] Oren Mangoubi and Aaron Smith, *Rapid Mixing of Geodesic Walks on Manifolds with Positive Curvature*, 2016, https://arxiv.org/abs/1609.02901 (initial public preprint September 9, 2016).

[3] Philip Schär and Thilo D. Stier, *A Dimension-Independent Bound on the Wasserstein Contraction Rate of a Geodesic Random Walk on the Sphere*, 2023, https://arxiv.org/abs/2309.09097 (initial public preprint September 16, 2023).
