# Exact quadratic Walsh concentration on Hamming balls and the sharp minimal-sampling instability

## Finding
Let \(n\ge5\), let \(\Omega_n=\{-1,1\}^n\) have uniform probability measure, and let \(V_{\le2}\) be the space spanned by the Walsh characters \(\chi_I(x)=\prod_{i\in I}x_i\) with \(|I|\le2\). For each radius \(0\le r\le n\), define the Hamming ball \(B_r=\{x:\#\{i:x_i=-1\}\le r\}\) and the concentration operator \(C_{n,r}=P_{\le2}M_{\mathbf1_{B_r}}P_{\le2}|_{V_{\le2}}\). The theorem gives **its complete spectrum at every radius** through two explicit matrices of sizes three and two and one scalar, with exact multiplicities.

Write \(D=1+n+\binom n2\), \(c=\binom n2\), and set
\[
 a_j=2^{-n}\sum_{h=0}^{r}\sum_{\ell=0}^{j}(-1)^\ell\binom j\ell\binom{n-j}{h-\ell}\quad(0\le j\le4),
\]
with out-of-range binomial coefficients zero. Define the real symmetric matrices
\[
S=\begin{pmatrix}
a_0&\sqrt n\,a_1&\sqrt c\,a_2\\
\sqrt n\,a_1&a_0+(n-1)a_2&\sqrt{c/n}\,[2a_1+(n-2)a_3]\\
\sqrt c\,a_2&\sqrt{c/n}\,[2a_1+(n-2)a_3]&a_0+2(n-2)a_2+\binom{n-2}{2}a_4
\end{pmatrix},
\]
\[
T=\begin{pmatrix}
a_0-a_2&\sqrt{n-2}(a_1-a_3)\\
\sqrt{n-2}(a_1-a_3)&a_0+(n-4)a_2-(n-3)a_4
\end{pmatrix},\qquad u=a_0-2a_2+a_4.
\]
Then the complete multiset of eigenvalues of \(C_{n,r}\) is the three eigenvalues of \(S\), **once each**, both eigenvalues of \(T\), **each repeated \(n-1\) times**, and \(u\), **repeated \(n(n-3)/2\) times**. Equal eigenvalues across blocks are combined. In particular, the restriction \(R_{n,r}:V_{\le2}\to L^2(B_r,2^{-n}\text{counting measure})\) is injective exactly when \(r\ge2\): radius two is the smallest sampling ball that reconstructs all quadratic Walsh coefficients.

At this **minimal radius**, the entire spectrum simplifies to roots of two explicit polynomials plus a constant. Put \(\widetilde S=2^n S\), \(\widetilde T=2^n T\) and \(z\) for an indeterminate. The characteristic polynomials are
\[
\begin{aligned}
\det(zI_3-\widetilde S)&=z^3-\frac{n^4-14n^3+85n^2-204n+212}{4}z^2\\
&\quad+(n^4-2n^3+13n^2-60n+116)z-64,\\
\det(zI_2-\widetilde T)&=z^2-4((n-3)^2+4)z+64,\\
2^nu&=16.
\end{aligned}
\]
The determinant of the full concentration operator is exactly
\[
\boxed{\det C_{n,2}=2^{-nD+2n+4\binom n2}.}
\]
Despite this nonzero determinant and the minimal number \(D\) of observation points, the sharp asymptotic spectral condition number grows as the **eighth power of dimension**:
\[
\boxed{\frac{\lambda_{\max}(C_{n,2})}{\lambda_{\min}(C_{n,2})}\sim\frac{n^8}{256},\qquad
\kappa_2(R_{n,2})\sim\frac{n^4}{16}.}
\]
Equivalently, \(\lambda_{\max}(C_{n,2})\sim n^4/(4\cdot2^n)\) and \(\lambda_{\min}(C_{n,2})\sim64/(2^n n^4)\). The condition number here refers to the nonzero singular values of the **square restriction map**; it is not a noise-robustness theorem for a different sampling geometry.

## Assumptions and scope
All formulas use normalized global Walsh orthonormality \(2^{-n}\sum_{x\in\Omega_n}\), with **no renormalization by the size of the ball**. The integer \(n\ge5\) and every integer \(r\in[0,n]\) are allowed, including degenerate end radii. The dimensions of the three invariant sectors are \(3\), \(2(n-1)\), and \(n(n-3)/2\), summing to \(D\). The spectrum concerns the spatial compression of the entire degree-at-most-two Fourier band, not the induced adjacency operator on the ball and not the compression to a single fixed-weight shell. Singular values of the restriction map are square roots of the concentration eigenvalues. The asymptotics keep the Walsh degree and sampling radius fixed at two while \(n\to\infty\).

## Proof
**1. The exact Gram matrix.** For subsets \(I,J\subset[n]\) of cardinality at most two, the matrix entry is
\[
\langle C_{n,r}\chi_J,\chi_I\rangle=2^{-n}\sum_{x\in B_r}\chi_{I\triangle J}(x)=a_{|I\triangle J|}.
\]
The displayed binomial formula follows by choosing \(\ell\) negative coordinates in the \(j\)-element symmetric difference and \(h-\ell\) elsewhere. Thus every entry of the entire \(D\)-dimensional Gram matrix is known from five exact binomial tails.

**2. Three invariant sectors.** The coordinate-permutation action preserves the operator. The coefficient space decomposes orthogonally into: (i) the three-dimensional radial span of the empty-set character, normalized sum of singleton characters, and normalized sum of pair characters; (ii) two equivalent \((n-1)\)-dimensional standard sectors, represented for each \(\sum_i v_i=0\) by \(\sum_i v_i\chi_i\) and \(\sum_{i<j}(v_i+v_j)\chi_{ij}/\sqrt{n-2}\); and (iii) the quadratic edge-weight sector consisting of arrays \((q_{ij})\) whose row sums \(\sum_{j\ne i}q_{ij}\) are all zero, of dimension \(\binom n2-n=n(n-3)/2\). The latter has no constant or linear components. These sectors are pairwise orthogonal and exhaust all \(D\) dimensions.

On the radial basis, direct counting of pairs that coincide, overlap in one coordinate, or are disjoint gives precisely \(S\). For a unit standard coefficient vector \(v\), the two displayed normalized vectors are orthogonal and each has norm one; evaluating the same intersection counts gives \(T\), independently of \(v\). On the row-sum-zero quadratic arrays, the pair-overlap adjacency sum equals \(-2q_{ij}\), and the disjoint-pair sum equals \(q_{ij}\), yielding the scalar \(u=a_0-2a_2+a_4\). Therefore there are no missing eigenvalues, and their multiplicities are exactly those claimed. This is an explicit block computation, not an assumption that distinct blocks have distinct spectra.

**3. Exact interpolation threshold and determinant.** Use binary coordinates \(b_i=(1-x_i)/2\). Every Walsh polynomial of degree at most two is a unique multilinear polynomial in the \(b_i\) of degree at most two. Its evaluations at the all-zero point, every one-point support, and every two-point support determine the constant, each linear coefficient, and each quadratic coefficient successively by inclusion-exclusion. Consequently restriction to \(B_2\) is an isomorphism, restriction to \(B_1\) has rank \(n+1\), and restriction to \(B_0\) has rank one. Larger balls contain \(B_2\) and hence have full column rank.

Ordering the monomial basis and the corresponding \(D\) observations by support size, the monomial evaluation matrix is the triangular subset-incidence matrix of determinant one. The change from Walsh characters \(\chi_I=\prod_{i\in I}(1-2b_i)\) to these monomials is triangular with diagonal entries \((-2)^{|I|}\). Hence the absolute determinant of the unnormalized \(D\)-by-\(D\) evaluation matrix is \(2^{n+2\binom n2}\). Since \(C_{n,2}=2^{-n}E^*E\), its determinant is exactly the displayed \(2^{-nD+2n+4\binom n2}\).

**4. Minimal-ball characteristic polynomials.** When \(r=2\), direct enumeration of zero, one, and two negative coordinates gives
\[
2^n a_j=D-2j(n-j+1),\qquad j=0,1,2,3,4.
\]
Substitution in \(S,T,u\), expansion of the \(3\)-by-\(3\) and \(2\)-by-\(2\) determinants, and simplification give the displayed two characteristic polynomials and \(2^n u=16\). The cubic product is \(64\); the quadratic product is \(64\). Independently, their products and multiplicities recover the full determinant from step 3, providing a second exact check of all normalization powers.

**5. Sharp instability constant.** The three positive roots of the cubic, in increasing order \(s_1\le s_2\le s_3\), satisfy
\[
 s_1+s_2+s_3=\tfrac14n^4+O(n^3),\quad
 s_1s_2+s_1s_3+s_2s_3=n^4+O(n^3),\quad s_1s_2s_3=64.
\]
The radial pair-sector diagonal entry is
\[
2^n S_{33}=2^n\left(a_0+2(n-2)a_2+\binom{n-2}{2}a_4\right)
=\tfrac14n^4+O(n^3).
\]
The Rayleigh principle bounds \(s_3\) below by this entry and above by the cubic trace, so \(s_3=\tfrac14n^4(1+O(n^{-1}))\). The product identity now gives \(s_1s_2=64/s_3=O(n^{-4})\). From the exact second elementary symmetric identity,
\[
s_1+s_2=\frac{(s_1s_2+s_1s_3+s_2s_3)-s_1s_2}{s_3}
=\frac{n^4+O(n^3)-64/s_3}{s_3}=4+O(n^{-1}).
\]
Because \(s_1,s_2>0\), these sum and product estimates imply \(s_2=4+O(n^{-1})\) and \(s_1=64n^{-4}(1+O(n^{-1}))\). The two positive roots of the quadratic have product \(64\) and sum \(4((n-3)^2+4)\), hence are asymptotic to \(4n^2\) and \(16n^{-2}\). The remaining scaled eigenvalue is \(16\). Thus, for all sufficiently large dimensions, the largest and smallest eigenvalues both lie in the radial cubic sector, and the eigenvalue and singular-value ratios have the displayed sharp asymptotic constants.

## Verification
The included standalone `verify.py` uses Python 3 standard-library **integer arithmetic only**. It reconstructs the actual full restricted Walsh Gram matrices for **all radii and every dimension \(5\le n\le10\)** by enumeration of cube vertices. It checks every matrix entry against the binomial moment formula, verifies invariant-sector actions on explicit radial, standard and row-sum-zero quadratic vectors, and checks the three minimal-radius characteristic coefficients and both block determinants. In dimensions five and six it additionally computes the entire minimal-ball Gram determinant via fraction-free elimination, independently of the block formulas. Executing `python3 verify.py` gives `WALSH_QUADRATIC_BALL_EXACT_CHECKS_PASS 80228`. The proof above, not the finite enumeration, establishes all-dimension assertions.

## Relationship to prior work
Hogan and Lakey, *Spatio-spectral limiting on hypercubes: eigenspaces*, arXiv:1812.08905v1 (first publicly posted 2018-12-21), study the **same general Boolean-cube space/frequency concentration problem** and derive a reduced-matrix eigenspace procedure (notably Corollary 9). Their contribution is the pre-existing general reduction, which is explicitly credited. The present explicit all-radius quadratic \(3+2+1\) spectral matrix, exact minimal-radius determinant and, especially, the sharp \(n^8/256\) eigenvalue condition growth are not stated in the inspected material. Their later 2021 article continues the invariant-subspace treatment. That article's publisher preview was checked, but its complete main text was inaccessible, so a stronger implicit or explicit comparison there remains a priority risk.

The full published result *Exact first-Walsh-band concentration spectra on Boolean Hamming balls* (2026) concerns **degree at most one** and has a two-dimensional radial block, not the quadratic band. The full published result *Square-dimension spectral resonances for quadratic-band Walsh concentration on Hamming shells* (2026) concerns a **single fixed-weight shell**, with zero modes; summing shell eigenvalues does not determine ball eigenvalues, since the shell eigendirections in their multi-copy sectors are radius-dependent. These are important close comparisons, not claims of absent antecedents. Kirshner and Samorodnitsky's work on Krawtchouk polynomials and Hamming spheres motivates the use of binomial geometry but concerns high-moment bounds, not this square restriction map. An equivalent derivation from a general Terwilliger-block representation remains possible; novelty is best understood as the exact quantified sampling instability and complete small-block specialization rather than invention of the general symmetry decomposition.

## Limitations
The result is exact for the binary cube, complete Walsh bandwidth at most two, and Hamming balls about a vertex. It does not optimize over other observation sets of the same cardinality, give a noise recovery theorem, prove a uniform asymptotic when the radius grows with dimension, or classify spectra for larger Fourier bandwidths. It is not independently audited. Full text of the 2021 Hogan–Lakey continuation was unavailable from the checked sources, leaving historical-priority risk; no claim of worldwide novelty follows merely from searches.

## References
1. J. A. Hogan and J. D. Lakey, *Spatio-spectral limiting on hypercubes: eigenspaces*, arXiv:1812.08905v1, first publicly posted **2018-12-21**, especially Section 1, Corollary 9, and numerical eigenspace procedure. https://arxiv.org/abs/1812.08905
2. J. A. Hogan and J. D. Lakey, *Spatio-Spectral Limiting on Boolean Cubes*, J. Fourier Anal. Appl. 27 (2021), article 40, published **2021-04-21**, DOI: 10.1007/s00041-021-09845-y. https://doi.org/10.1007/s00041-021-09845-y
3. J. A. Hogan and J. D. Lakey, *An Analogue of Slepian Vectors on Boolean Hypercubes*, J. Fourier Anal. Appl. 25 (2019), 2004–2020, first published **2018-11-20**, DOI: 10.1007/s00041-018-09654-w. https://doi.org/10.1007/s00041-018-09654-w
4. N. Kirshner and A. Samorodnitsky, *A Moment Ratio Bound for Polynomials and Some Extremal Properties of Krawchouk Polynomials and Hamming Spheres*, arXiv:1909.11929v1 (2019-09-26); IEEE Trans. Inform. Theory 67 (2021), 3509–3541. https://arxiv.org/abs/1909.11929
5. *Exact first-Walsh-band concentration spectra on Boolean Hamming balls* (2026), published result, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-first-walsh-band-concentration-spectra-on-boolean-hamming--a2f5ddac5a0f
6. *Square-dimension spectral resonances for quadratic-band Walsh concentration on Hamming shells* (2026), published result, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-square-dimension-spectral-resonances-for-quadratic-band-walsh-co--7e1319aedf95
