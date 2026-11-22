# Sharp dissipativity threshold of a three-site skew path in real \(\ell_4\)

## Finding
For the real Banach space \(X=\ell_4^3(\mathbb R)\), consider the nearest-neighbor skew-symmetric path matrix
\[
S=\begin{pmatrix}0&1&0\\-1&0&1\\0&-1&0\end{pmatrix},\qquad S(x_1,x_2,x_3)=(x_2,x_3-x_1,-x_2).
\]
Define its (one-sided) logarithmic norm, or numerical abscissa, by
\[
\mu_4(S)=\sup_{x\in X\setminus\{0\}}\frac{\sum_{j=1}^3x_j^3(Sx)_j}{\sum_{j=1}^3x_j^4}.
\]
There is a unique \(\rho\in(0,1)\) satisfying \(2\rho^3-6\rho^2-3\rho+1=0\). Put
\[
\gamma=\frac{2\sqrt\rho\,(1-\rho)}{1+2\rho^2}=0.6679394527296159\ldots .
\]
Then **\(\mu_4(S)=\gamma\)**, and its complete set of nonzero maximizing vectors is exactly
\[
\bigl\{\lambda(-\sqrt\rho,1,\sqrt\rho):\lambda\in\mathbb R\setminus\{0\}\bigr\}.
\]
In particular, all numerical-abscissa maximizers are confined to the antisymmetric invariant plane \(x_1=-x_3\), despite the presence of a third (kernel) direction that interacts nonlinearly with the quartic norm.

For every real \(\alpha,\beta\), define \(G_{\alpha,\beta}=-\alpha I+\beta S\). The **optimal exponential bound with prefactor one** is
\[
\inf\{\omega\in\mathbb R:\|e^{tG_{\alpha,\beta}}\|_{4\to4}\le e^{\omega t}\text{ for all }t\ge0\}
=-\alpha+|\beta|\gamma.
\]
Consequently \(e^{tG_{\alpha,\beta}}\) is contractive for all \(t\ge0\) if and only if \(\alpha\ge|\beta|\gamma\). In sharp contrast, \(\|e^{tG_{\alpha,\beta}}\|_{2\to2}=e^{-\alpha t}\). For \(0<\alpha<|\beta|\gamma\), the matrix has spectrum \(\{-\alpha,-\alpha\pm i\sqrt2\beta\}\) and an exponentially stable semigroup but nevertheless initially expands in \(\ell_4^3\).

## Assumptions and scope
All coordinates and scalars are real; \(X\) has the counting-measure norm \(\|x\|_4=(\sum_j|x_j|^4)^{1/4}\). The matrix \(S\) has precisely two nonzero undirected path couplings, of equal magnitude. The numerical abscissa is *one-sided* (supremum without absolute values); for this particular skew path its range is symmetric because the diagonal sign isometry \(D=\operatorname{diag}(1,-1,1)\) satisfies \(DSD=-S\). No complex-space, higher-dimensional, or arbitrary-weight result is asserted.

## Proof
**1. Duality and the quartic reduction.** Smoothness of real \(\ell_4^3\) gives the normalized duality functional \(x^*(h)=\sum_jx_j^3h_j/\|x\|_4^3\) at a nonzero \(x\). Introduce signed variables \(a=(x_1-x_3)/2\), \(w=(x_1+x_3)/2\), and \(b=x_2\). Direct expansion yields
\[
F(x):=\sum_jx_j^3(Sx)_j=2ab(a^2+3w^2-b^2),
\quad Q(x):=\sum_jx_j^4=2a^4+b^4+12a^2w^2+2w^4.
\]
When \(ab=0\), the quotient vanishes. For \(ab\ne0\), homogeneity and taking absolute values permit the variables \(u=|a/b|>0\), \(W=(w/b)^2\ge0\). Since \(x\mapsto Dx\) changes the sign of \(F\) without changing \(Q\), the positive supremum equals the absolute supremum, and the reduced absolute quotient is
\[
H(u,W)=\frac{2u\,|u^2-1+3W|}{2u^4+1+12u^2W+2W^2}.
\]
The denominator, abbreviated \(D(u,W)\), is strictly positive.

**2. Positive-sign branch is strictly suboptimal.** If \(u^2-1+3W\ge0\), then \(H(u,W)\le1/2\). Indeed it suffices to show \(D(u,W)-4u(u^2-1+3W)\ge0\). For \(0\le u\le1\) this difference is the **exact positive decomposition**
\[
2\bigl(W-3u(1-u)\bigr)^2+1+2u\bigl(2(1-u)(2u-1)^2+u\bigr)>0.
\]
For \(u\ge1\), it equals
\[
2W^2+12u(u-1)W+1+2u\left[\left(u-\frac43\right)^2\left(u+\frac23\right)+\frac{22}{27}\right]>0.
\]
Both are direct polynomial identities. Thus the positive-sign branch is everywhere below \(1/2\).

**3. Negative-sign branch and unique extremizer.** If \(u^2-1+3W<0\), necessarily \(0<u<1\) and \(0\le W<(1-u^2)/3\). Its numerator \(2u(1-u^2-3W)\) is strictly decreasing in \(W\), whereas its denominator is nondecreasing. Thus
\[
H(u,W)\le H(u,0)=f(u):=\frac{2u(1-u^2)}{1+2u^4},
\]
with equality only at \(W=0\). At \(u=1/2\), \(f(u)=2/3>1/2\); hence the global maximizer lies in this branch and has \(W=0\), equivalently \(x_1=-x_3\). Differentiation gives
\[
f'(u)=\frac{2(2u^6-6u^4-3u^2+1)}{(1+2u^4)^2}.
\]
The polynomial \(p(z)=2z^3-6z^2-3z+1\) decreases strictly on \([0,1]\), because \(p'(z)=6(z-1)^2-9\le-3\), and \(p(0)=1>0>p(1)=-6\). Therefore it has precisely one root \(\rho\in(0,1)\); \(f\) rises then falls and has its unique maximum at \(u=\sqrt\rho\). The endpoint values are zero, giving \(\max H=\gamma\). Equality forces \(W=0\), \(u=\sqrt\rho\) and \(F(x)>0\). This last sign selects precisely the scalar multiples of \((-\sqrt\rho,1,\sqrt\rho)\) claimed above.

**4. Sharp semigroup rate.** For a differentiable solution \(x'(t)=G_{\alpha,\beta}x(t)\), direct differentiation yields
\[
\frac14\frac{d}{dt}\|x(t)\|_4^4=\sum_jx_j(t)^3(G_{\alpha,\beta}x(t))_j\le(-\alpha+|\beta|\gamma)\|x(t)\|_4^4.
\]
The symmetry \(DSD=-S\) handles negative \(\beta\). Integrating gives the asserted uniform exponential norm bound. Conversely a maximizing initial vector has right derivative of its normalized \(\ell_4\) norm equal to \(-\alpha+|\beta|\gamma\), so any smaller exponential rate with prefactor one fails for sufficiently small positive \(t\). Finally \(S^\top=-S\) implies \(e^{t\beta S}\) is Euclidean orthogonal; \(S\) has characteristic polynomial \(\lambda(\lambda^2+2)\). This proves both the Hilbert norm identity and the spectral-versus-contractivity assertion.

## Verification
The bundled standard-library script `verify_path_skew.py` enumerates nonzero integer triples in \([-8,8]^3\), checks the exact quartic and numerator identities and a rational bound strictly above the sharp constant, tests the positive-branch polynomial decompositions on rational grids, independently solves the isolating cubic by bisection, and checks the extremizing vector and four finite-difference semigroup slopes. It reports `THREE_SITE_SKEW_PATH_CHECKS_OK 15626`. This finite diagnostic is **not** used as a proof of the supremum or the semigroup claim; those are established analytically above.

## Relationship to prior work
Boubaker, Gernandt and Selmi (2026) develop numerical ranges of linear relations in Banach spaces and numerical-abscissa semigroup estimates; their Section 5 uses a distinct two-dimensional \(L^1/L^2\) multiplication example rather than the real \(\ell_4^3\) skew path. Martín, Merí and Popov (2010) provide general Lebesgue-space numerical-radius inequalities and the classical two-coordinate skew-rotation benchmark; those formulas do not establish that all norming vectors for a three-coordinate path lie in its invariant two-plane. The previously published exact three-point conditional-expectation commutator result concerns a triangular **three-edge** skew matrix, with \(K=\frac14\begin{psmallmatrix}0&-1&1\\1&0&-1\\-1&1&0\end{psmallmatrix}\), not this **two-edge** path. A signed-permutation isometry of real \(\ell_4^3\) preserves the edge-support pattern, so its exact scalar value and normers do not imply the path computation. The proof here requires the separate strict positive-branch inequality and yields a distinct exact cubic constant and complete path normer classification.

## Limitations
The theorem treats only real \(\ell_4^3\) and two equal neighboring skew couplings, with arbitrary real scalar damping and strength. The formula does not give the full numerical range, norms with arbitrary prefactors, nonuniform skew weights, or other exponents; the term "optimal exponential" refers precisely to rate bounds with prefactor one for every nonnegative time. Existing published results about other geometries are credited, and a bibliographically unindexed equivalent may exist. 
## References
1. W. Boubaker, H. Gernandt, W. Selmi, *On the Numerical Range of Linear Relations in Banach Spaces*, arXiv:2608.19913v1 (first public 2026-08-20), https://arxiv.org/abs/2608.19913 ; full HTML https://arxiv.org/html/2608.19913 .
2. M. Martín, J. Merí, M. Popov, *On the numerical radius of operators in Lebesgue spaces*, arXiv:1011.4785v1 (first public 2010-11-22), https://arxiv.org/html/1011.4785v1 .
3. *Sharp numerical radius of a three-point conditional-expectation commutator*, published-finding corpus public research record (2026-10-11), https://github.com/published-finding corpus/2026/blob/main/2026/10/11/SCOPE-sharp-numerical-radius-of-a-three-point-conditional-expectation--d81ced4c9642/RESULT.md .
