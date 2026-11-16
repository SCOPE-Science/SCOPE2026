# Exact quadratic-band Slepian blocks on every spherical positive orthant and a sharp fourth-power conditioning law

## Finding

Fix an integer \(d\ge4\). Let \(\sigma_d\) be normalized surface measure on \(S^{d-1}\), let \(\Omega_d=\{x\in S^{d-1}:x_j>0\text{ for all }j\}\), and let \(V_d=\mathcal H_0\oplus\mathcal H_1\oplus\mathcal H_2\), the complex spherical harmonics of degrees zero through two. The concentration operator \(C_d\) on \(V_d\) is defined by
\[
\langle C_df,g\rangle_{L^2(\sigma_d)}=\int_{\Omega_d}f\overline g\,d\sigma_d.
\]
Put
\[
t=\frac2\pi,\quad h_d=\frac{\Gamma(d/2)}{\sqrt\pi\,\Gamma((d+1)/2)},\quad m=\binom d2,\quad H=d(d+2).
\]
Define the following real symmetric matrices:
\[
B_{0,d}=\begin{pmatrix}
1&dh_d&t\sqrt{m(d+2)/d}\\
dh_d&1+(d-1)t&\dfrac{2h_d\sqrt{mH}}{d+1}\left(1+\dfrac{(d-2)t}{2}\right)\\
t\sqrt{m(d+2)/d}&\dfrac{2h_d\sqrt{mH}}{d+1}\left(1+\dfrac{(d-2)t}{2}\right)&1+2t(d-2)+\dfrac{t^2}{2}(d-2)(d-3)
\end{pmatrix}
\]
and
\[
B_{1,d}=\begin{pmatrix}
1-t&\dfrac{h_d\sqrt{dH/2}}{d+1}&\dfrac{h_d\sqrt{dH(d-2)}}{d+1}(1-t)\\
\dfrac{h_d\sqrt{dH/2}}{d+1}&1&t\sqrt{(d-2)/2}\\
\dfrac{h_d\sqrt{dH(d-2)}}{d+1}(1-t)&t\sqrt{(d-2)/2}&1+(d-4)t-(d-3)t^2
\end{pmatrix}.
\]
The **complete eigenvalue multiset** of \(C_d\), with multiplicities, consists of \(2^{-d}\) times all three eigenvalues of \(B_{0,d}\) (each once), all three eigenvalues of \(B_{1,d}\) (each repeated \(d-1\) times), and \((1-t)^2\) (repeated \(d(d-3)/2\) times). In particular, the entire \(d(d+3)/2\)-dimensional spectral problem reduces to two matrices of order three and one scalar, regardless of \(d\). Every eigenvalue lies strictly between zero and one.

For the condition number of **continuous restriction** \(R_d:V_d\to L^2(\Omega_d,\sigma_d)\), using the inherited, unrenormalized measure on the orthant, the exact sharp value at every \(d\) is the square root of the ratio of the largest to the smallest numbers in this explicit eigenvalue multiset. Moreover,
\[
\boxed{\displaystyle \lim_{d\to\infty}\frac{\kappa(R_d)}{d^2}=\frac{2}{\pi(\pi-3)}.}
\]
Thus squared concentration conditioning grows as the fourth power of dimension, despite the fixed polynomial degree. The unique largest and smallest eigenvalues belong to the symmetric \(B_{0,d}\) block for all sufficiently large \(d\); their conditional (factor \(2^{-d}\) removed) asymptotics are respectively \(2d^2/\pi^2\) and \((\pi-3)^2/(2d^2)\). The claim does not assert a dimension-uniform exact ordering of the six block roots.

## Assumptions and scope

All integrals are with respect to normalized *full-sphere* surface measure; the orthant occupies measure \(2^{-d}\). The concentration eigenvalues equal squared singular values of restriction, so its condition number is the square root of the concentration condition number. The harmonic space includes degrees \(0,1,2\) simultaneously, not pure degree two alone. The result holds for arbitrary complex coefficients by complexification of real symmetric moment matrices. Orthant boundaries have zero measure, so strict or weak coordinate inequalities give the same operator. The asymptotic limit has integer \(d\to\infty\) and fixed cutoff two.

## Proof

**1. Exact moments.** If \(U\) is uniformly distributed on the positive orthant, then \(U=(|G_1|,\ldots,|G_d|)/(\sum G_i^2)^{1/2}\), for independent standard normal random variables \(G_i\). Hence for nonnegative integer exponents \(k_i\),
\[
\mathbb E\prod U_i^{k_i}=\frac{\Gamma(d/2)}{\Gamma((d+\sum k_i)/2)}\prod_i\frac{\Gamma((k_i+1)/2)}{\Gamma(1/2)}.
\]
This identity independently fixes all moments of total degree at most four, and the orthant Gram matrix is \(2^{-d}\) times the conditional Gram matrix.

**2. Orthogonal symmetry types.** Permutations of coordinates preserve the region. The harmonic polynomial space of degree at most two is the space of restrictions of all polynomials of total degree at most two, since \(\sum x_i^2=1\) on the sphere. It decomposes into three invariant permutation types: three copies of the trivial representation, three copies of the standard \((d-1)\)-dimensional representation, and the orthogonal kernel of the unsigned complete-graph incidence map on edge coordinates, of dimension \(d(d-3)/2\). For a standard unit vector \(u\in\mathbb R^d\) with \(\sum u_i=0\), use the globally orthonormal functions
\[
L_u=\sqrt d\sum_i u_ix_i,\quad D_u=\sqrt{H/2}\sum_i u_ix_i^2,\quad O_u=\sqrt{H/(d-2)}\sum_{i<j}(u_i+u_j)x_ix_j.
\]
In the trivial sector use the globally orthonormal functions
\[
F_0=1,\quad F_1=\sum_i x_i,\quad F_2=\sqrt{H/m}\sum_{i<j}x_ix_j.
\]
The remaining edge-polynomial sector has coefficients \(v_{ij}\) satisfying \(\sum_{j\ne i}v_{ij}=0\) for every vertex \(i\). There are no extra components: the dimensions add to \(3+3(d-1)+d(d-3)/2=d(d+3)/2\).

**3. Entry calculation.** In the \((F_0,F_1,F_2)\) basis, substituting the gamma-moment identity gives exactly \(B_{0,d}\). In each of the \((L_u,D_u,O_u)\) standard triples the same substitution gives \(B_{1,d}\), independently of the chosen unit standard vector; cross terms between distinct standard directions vanish by permutation symmetry and polarization. For edge vectors with zero vertex incidence, the fourth-moment form is \((1-t)^2\) times the global norm, giving the final scalar sector. Every displayed entry may also be reconstructed directly by expanding the products into monomials of degree at most four. The full blocks are therefore exhaustive, with the stated multiplicities.

**4. Positivity and exact stability.** No nonzero polynomial of degree at most two vanishes on an open orthant of a sphere, or on the open complement, by real analyticity. Thus for every nonzero \(f\in V_d\), \(0<\int_{\Omega_d}|f|^2<\int_{S^{d-1}}|f|^2\); all eigenvalues are strictly between zero and one. The spectral formula for the sharp restriction condition number follows from \(R_d^*R_d=C_d\).

**5. Sharp high-dimensional limit.** Write \(S_d=\sum_iU_i\) and \(s_d=\mathbb ES_d=dh_d\). A multivariate central limit theorem, the delta method applied to \(\sum_i|G_i|/\sqrt{\sum_iG_i^2}\), and uniform integrability of fixed powers imply convergence of all moments needed below:
\[
Z_d=S_d-s_d\longrightarrow Z\sim N(0,\nu),\quad \nu=1-\frac3\pi>0,\qquad \frac{s_d}{\sqrt d}\longrightarrow\sqrt{\frac2\pi}.
\]
The trivial basis can equivalently be written \((1,S_d,\alpha_d(S_d^2-1))\), where \(\alpha_d=\sqrt{(d+2)/(2(d-1))}\). Conditional orthogonalization of the monomials \(1,Z_d,Z_d^2\) gives a monic quadratic residual with squared conditional norm tending to \(2\nu^2\). Its coefficient vector in this globally orthonormal basis has squared Euclidean norm asymptotic to \((2/\pi)^2d^2\). The other two conditional orthogonal polynomials have coefficient norms of orders \(1\) and \(\sqrt d\). Expressing the inverse Gram matrix as the sum of the three corresponding rank-one matrices yields
\[
\lambda_{\min}(B_{0,d})\sim\frac{2\nu^2}{(2/\pi)^2d^2}=\frac{(\pi-3)^2}{2d^2}.
\]
Also \(F_2=\alpha_d(S_d^2-1)\) has conditional second moment \((2/\pi)^2d^2/2+O(d)\), while the remaining entries of \(B_{0,d}\) have smaller total trace order. Therefore \(\lambda_{\max}(B_{0,d})\sim2d^2/\pi^2\).

For completeness, the standard sector cannot contain a smaller-order eigenvalue: fix \(u=(e_1-e_2)/\sqrt2\) in its triple. The identity
\[
O_u=\sqrt{\frac{d+2}{d-2}}\,S_dL_u-\sqrt{\frac2{d-2}}D_u
\]
shows that replacing \(O_u\) with \(O_u-\sqrt{(d+2)/(d-2)}\,s_dL_u\) produces a new triple whose conditional Gram converges to the strictly positive Gram of \((L_\infty,D_\infty,ZL_\infty)\): here \(L_\infty=(|G_1|-|G_2|)/\sqrt2\), \(D_\infty=(G_1^2-G_2^2)/2\), and the limiting Gaussian \(Z\) is independent of \((G_1,G_2)\). Positive definiteness follows since \(Z\) has positive variance and \(L_\infty,D_\infty\) are linearly independent in \(L^2\). The change-of-basis matrix has norm \(O(\sqrt d)\), so \(\lambda_{\min}(B_{1,d})=\Omega(d^{-1})\), and \(\lambda_{\max}(B_{1,d})=O(d)\). The scalar sector is fixed positive. Consequently, both global extremes are furnished by the trivial block for sufficiently large \(d\), and
\[
\kappa(R_d)\sim\sqrt{\frac{2d^2/\pi^2}{(\pi-3)^2/(2d^2)}}=\frac{2d^2}{\pi(\pi-3)}.
\]

## Verification

The self-contained `checker.py` constructs a full orthonormal polynomial basis independently of the three-block calculation, evaluates all degree-at-most-four monomial integrals directly from the spherical gamma identity, and compares the entire eigenvalue multiset with the theorem for every dimension from \(3\) to \(9\). It verifies dimensions, traces, and positivity, with \(224\) supplemental checks, and prints large-dimension asymptotic diagnostics. Execute `python checker.py` with NumPy and SciPy available. These finite checks corroborate the explicit block calculation but do not replace its all-dimensional proof or the asymptotic argument.

For example, at \(d=4\) the conditional maximal and minimal block eigenvalues are approximately \(7.76960792506\) and \(0.0000518140446711\); their ratio gives the sharp restriction condition number \(387.236070330\). The common factor \(2^{-4}\) cancels in this condition number.

## Relationship to prior work

The standard spherical Slepian framework defines concentration through a regional harmonic Gram matrix (Simons–Dahlen–Wieczorek, 2004). Roddy–McEwen (2021) develop Slepian-based wavelets for incomplete spherical observations rather than this explicit all-dimensional positive-orthant spectrum. The closest exact orthant result determines **pure degree-two** concentration (without the constant and linear harmonics), with quadratic growth of its concentration condition number. That statement does not determine the nonzero off-diagonal couplings between harmonic degrees. The present full low-pass calculation requires the new trivial and standard three-by-three blocks and identifies an asymptotically quadratic **restriction** condition number, rather than the linear restriction growth for pure degree two. A known exact positive-octant calculation in ambient dimension three is a fixed-dimensional special case, not the formula or stability asymptotic for arbitrary ambient dimension. General kernel formulas allow numerical evaluation but do not directly state these exact blocks or the limiting constant.

## Limitations

The theorem covers a single coordinate orthant and only degrees at most two; it does not cover arbitrary spherical simplices or higher cutoffs. The all-dimensional condition-number formula uses an extremum across explicitly specified small blocks; no exact dimension-uniform ordering of all individual block roots is asserted. Finite numerical tests cannot certify the infinite-dimensional-parameter statement alone. Previously published formulas for pure degree two and the ambient three-dimensional orthant are related, and specialized unlocated exact orthant tables remain a historical-priority risk. This is an independently unaudited mathematical claim and not a claim about noisy finite sampling performance.

## References

1. F. J. Simons, F. A. Dahlen and M. A. Wieczorek, *Spatiospectral concentration on a sphere*, arXiv:math/0408424, first public 2004-08-31. https://arxiv.org/abs/math/0408424
2. P. J. Roddy and J. D. McEwen, *Slepian Scale-Discretised Wavelets on the Sphere*, arXiv:2106.02023, first public 2021-06-03. https://arxiv.org/abs/2106.02023
3. V. Michel, A. Plattner and K. Seibert, *A Unified Approach to Scalar, Vector, and Tensor Slepian Functions on the Sphere and Their Construction by a Commuting Operator*, arXiv:2103.14650, first public 2021-03-26. https://arxiv.org/abs/2103.14650
4. *Exact quadratic spherical-orthant concentration and a sharp dimension-squared stability law*, 2026, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-exact-quadratic-spherical-orthant-concentration-and-a-sharp-dime--043aca2fd738
