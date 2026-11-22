# Alternating boundary inertia and sharp conditioning of path unconditional reflexive polytopes

## Finding

For each integer \(n\ge 2\) consider the standard Euclidean polytope
\[
K_n=\{x\in\mathbb R^n:|x_i|+|x_{i+1}|\le1\ (1\le i<n)\}.
\]
Let \(X^{(n)}\) have uniform \(n\)-dimensional Lebesgue volume in \(K_n\), and let \(v_{n,i}=\mathbb E[(X^{(n)}_i)^2]\) for \(1\le i\le n\). Its covariance matrix is diagonal, with entries \(v_{n,i}\), and each entry is an exact rational number computable from a finite polynomial recurrence given below.

For every fixed \(j\ge1\), the left and right boundary variances converge to the same explicit value:
\[
\lim_{n\to\infty}v_{n,j}=\lim_{n\to\infty}v_{n,n+1-j}=v_j,
\]
\[
v_j=\frac13-\frac2{\pi^2}
 +\frac2{\pi^2}\sum_{k=1}^{\infty}
\frac{(-1)^{k(j+1)}}{(2k+1)^j}
\left(\frac1{k^2}-\frac1{(k+1)^2}\right).
\]
Write \(v_{\mathrm{bulk}}=1/3-2/\pi^2\). The excess \(v_j-v_{\mathrm{bulk}}\) is strictly positive for every odd \(j\), and strictly negative for every even \(j\). Moreover
\[
v_j-v_{\mathrm{bulk}}=
\frac{(-1)^{j+1}}{2\pi^2\,3^{j-1}}+O(5^{-j})\qquad(j\to\infty).
\]
The boundary sequence has its strict global maximum at \(j=1\) and strict global minimum at \(j=2\), with
\[
v_1=1-\frac8{\pi^2},\qquad
v_2=\frac8\pi-\frac{24}{\pi^2}.
\]
Consequently the Euclidean covariance condition number, defined as largest eigenvalue divided by smallest eigenvalue, has the sharp limit
\[
\boxed{\lim_{n\to\infty}\kappa(\operatorname{Cov}(X^{(n)}))=
\frac{1-8/\pi^2}{8/\pi-24/\pi^2}=1.6505132449401037\ldots.}
\]
The two terminal coordinates asymptotically carry the largest coordinate variances, the next-to-terminal coordinates the smallest, while all coordinates whose distance from both ends diverges have limiting variance \(v_{\mathrm{bulk}}=0.1306909660486577\ldots\). No claim is made about distinctness or the extremal eigenspaces in every fixed finite dimension.

## Assumptions and scope

Coordinates use the standard orthonormal basis of \(\mathbb R^n\); replacing the embedding by an arbitrary nonsingular affine map changes Euclidean covariance conditioning. Uniform measure means normalized Lebesgue volume, not uniform distribution on vertices. The indexed signed polytope \(K_n\) is the unconditional reflexive polytope associated with the path graph on \(n\) vertices, since this graph is perfect and its maximal clique inequalities have exactly the displayed form. In the first and last coordinate, the absolute value and pair constraint imply \(|x_i|\le1\); this propagates to all coordinates for \(n\ge2\). The nonnegative orthant section is the path stable-set (chain) polytope
\[
C_n=\{y\in[0,1]^n:y_i+y_{i+1}\le1\ \text{for}\ 1\le i<n\}.
\]
The claimed series is absolutely convergent for every integer \(j\ge1\). Here and below \(O(5^{-j})\) has a constant independent of \(j\).

## Proof

**1. Orthant reduction and exact rational moments.** Independent sign reflection preserves both \(K_n\) and volume. For different coordinates, flipping one sign shows \(\mathbb E[X_iX_j]=0\), and central symmetry shows \(\mathbb E[X_i]=0\). Hence the covariance is diagonal. With
\[
p_0(x)=1,\qquad p_{m+1}(x)=\int_0^{1-x}p_m(y)\,dy\quad(m\ge0),
\]
the free left subchain of length \(i-1\) at a prescribed \(y_i=x\) has volume \(p_{i-1}(x)\), and the free right subchain of length \(n-i\) has volume \(p_{n-i}(x)\). Fubini therefore gives, exactly,
\[
v_{n,i}=
\frac{\int_0^1 x^2p_{i-1}(x)p_{n-i}(x)\,dx}
{\int_0^1p_{n-1}(x)\,dx}.
\]
All \(p_m\) have rational polynomial coefficients; the denominator is positive and every \(v_{n,i}\) is rational. Reversal gives \(v_{n,i}=v_{n,n+1-i}\). The full volume is \(2^n\int_0^1p_{n-1}(x)\,dx\). For example, the complete variance lists at \(n=2,3,4\) are respectively \((1/6,1/6)\), \((1/5,1/10,1/5)\), and \((14/75,3/25,3/25,14/75)\).

**2. Transfer spectrum and uniform bulk bound.** Define the compact self-adjoint operator on \(L^2[0,1]\):
\[
(Tf)(x)=\int_0^{1-x}f(y)\,dy.
\]
It satisfies \(T^m1=p_m\). Direct integration and completeness of the standard mixed-boundary cosine basis give the orthonormal eigenfunctions and signed eigenvalues
\[
\phi_k(x)=\sqrt2\cos((k+1/2)\pi x),\qquad
\lambda_k=\frac{(-1)^k2}{(2k+1)\pi},\quad k=0,1,2,\ldots.
\]
Indeed, \(T\phi_k=\lambda_k\phi_k\), and these eigenfunctions are the complete Sturm--Liouville eigenbasis for \(f'(0)=f(1)=0\). Put \(c_k=\langle1,\phi_k\rangle=\sqrt2(-1)^k/((k+1/2)\pi)\). Then \(c_k/c_0=(-1)^k/(2k+1)\). Factoring out the leading eigenmode yields
\[
p_r=c_0\lambda_0^r(\phi_0+R_r),\qquad
R_r=\sum_{k\ge1}\frac{(-1)^{k(r+1)}}{(2k+1)^{r+1}}\phi_k,
\]
with \(\langle R_r,\phi_0\rangle=0\) and
\[
\|R_r\|_2\le C3^{-r},\qquad
C^2=\sum_{k\ge1}(2k+1)^{-2}=\frac{\pi^2}{8}-1<1.
\]
For \(r=i-1\) and \(s=n-i\) the exact ratio becomes
\[
v_{n,i}=\frac{\langle x^2(\phi_0+R_r),\phi_0+R_s\rangle}
{1+\langle R_r,R_s\rangle}.
\]
The denominator is at least \(1-C^2 3^{-(n-1)}>0\). Since multiplication by \(x^2\) has operator norm at most one, there is an absolute constant \(A\) such that
\[
|v_{n,i}-v_{\mathrm{bulk}}|\le A(3^{-(i-1)}+3^{-(n-i)}),\qquad
v_{\mathrm{bulk}}=\langle x^2\phi_0,\phi_0\rangle=\frac13-\frac2{\pi^2}.
\]
This proves uniform bulk convergence for coordinates whose distances from both ends tend to infinity, and ensures no additional large or small eigenvalues can emerge deep inside the polytope.

**3. Exact boundary series.** Fix \(j\), set \(r=j-1\) and send \(s=n-j\) to infinity in the previous ratio; then \(R_s\to0\) in \(L^2\), hence
\[
v_j=\langle x^2(\phi_0+R_{j-1}),\phi_0\rangle.
\]
Product-to-sum and integration by parts give, for \(k\ge1\),
\[
\langle x^2\phi_k,\phi_0\rangle=
\frac{2(-1)^k}{\pi^2}\left(\frac1{k^2}-\frac1{(k+1)^2}\right).
\]
Substitution proves the displayed absolutely convergent series. Integrating against \(\phi_0\) directly gives the closed \(v_1\). For \(v_2\), the one-step left factor is \(p_1(x)=1-x\), so
\[
v_2=\frac{\int_0^1x^2(1-x)\cos(\pi x/2)\,dx}
{\int_0^1(1-x)\cos(\pi x/2)\,dx}
=\frac8\pi-\frac{24}{\pi^2}.
\]

**4. Sign, extrema, and sharp boundary decay.** Put \(a_k=k^{-2}-(k+1)^{-2}\), which are positive and strictly decreasing. For odd \(j\), all terms in the boundary excess series are positive and decrease individually as \(j\) increases, so \(v_1>v_3>v_5>\cdots>v_{\mathrm{bulk}}\). For even \(j\), the series is alternating with decreasing positive term magnitudes, so \(v_j<v_{\mathrm{bulk}}\). The alternating-series bounds give
\[
\frac{2}{\pi^2}\left(\frac{a_1}{3^2}-\frac{a_2}{5^2}\right)
\le v_{\mathrm{bulk}}-v_2,
\qquad
0<v_{\mathrm{bulk}}-v_j<\frac{2a_1}{\pi^2 3^j}
\quad(j\ge4\text{ even}).
\]
Since \(a_1/9-a_2/25=7/90>a_1/81=1/108\), every even \(j\ge4\) has \(v_j>v_2\). (These rational comparisons are strict.) The first term \(k=1\) is \((-1)^{j+1}/(2\pi^2\,3^{j-1})\); the remaining terms, uniformly bounded by a constant times \(5^{-j}\), prove the sharp alternating boundary decay.

**5. Condition number.** Every sequence of positions \(i_n\in\{1,\ldots,n\}\) has a subsequence whose distance from the nearest end either diverges or is a fixed positive integer \(j\). The corresponding variance converges to \(v_{\mathrm{bulk}}\) or \(v_j\) respectively. Step 4 shows the maximum and minimum of this full collection of subsequential limits are precisely \(v_1\) and \(v_2\), both realized by choosing \(i_n=1\) and \(i_n=2\). Positivity of \(v_2\), clear from its integral representation, permits division, proving the stated limiting condition number. No unproved finite-dimensional spectral claim is used.

## Verification

The accompanying `checker.py` uses Python's standard-library exact rational arithmetic, independently implementing the polynomial transfer recursion. It checks reversal symmetry and positivity for all \(n=2,\ldots,26\), computes the displayed low-dimensional exact profiles, compares six finite-dimensional boundary values against the infinite-series limits, tests alternating signs and extrema for eleven boundary indices, and reproduces the stated numerical condition number. Run with `python3 checker.py` in the same directory. Its finite checks are diagnostics only; the spectral analysis and comparison inequalities above prove the infinitely quantified theorem.

## Relationship to prior work

Kohl, Olsen and Sanyal's 2019 work introduces the unconditional perfect-graph construction, identifying the precise lattice-polytope family. Marchal's earlier 2012 work uses a closely related alternating-permutation Markov kernel and its leading trigonometric eigenfunction. Shonkwiler and Theis (2026), studying the identical positive-orthant chain inequalities under an affine sign convention, establish exact sampling, bulk one-coordinate densities and first moments. The bulk constant here can already be integrated from that known marginal density; it is **not claimed as new by itself**. The contribution here is the exact rational signed-polytope covariance recurrence, complete alternating endpoint variance profile with sharp decay and strict extremizers, and the resulting sharp asymptotic covariance condition number in the standard Euclidean embedding. Related facet-area boundary-layer work on the same unsigned path polytope concerns a different measure (surface area rather than uniform interior-volume covariance).

## Limitations

The finding concerns only the path family in its specified coordinate embedding and uniform **interior** volume, not arbitrary perfect graphs, vertex-uniform measures, or affine-invariant isotropic constants. It proves no finite-dimensional uniqueness of extreme coordinate axes; it proves their exact limits. The transfer operator and bulk marginal density have established antecedents; priority of the new combined endpoint conditioning statement remains provisional pending independent literature review, including possible unindexed treatments of second moments of zigzag order polytopes. Numerical checks cannot establish absence of prior literature.

## References

1. F. Kohl, M. Olsen, and R. Sanyal, *Unconditional Reflexive Polytopes*, arXiv:1906.01469, first submitted 2019-06-03, https://arxiv.org/abs/1906.01469; published in *Discrete & Computational Geometry*, https://doi.org/10.1007/s00454-020-00199-8. Theorem 4.6 gives the unconditional perfect-graph classification.
2. P. Marchal, *Generating Random Alternating Permutations in Time \(n\log n\)* (2012), https://www.math.univ-paris13.fr/~marchal/altperm1.pdf. The Markov kernel and sine eigenfunction are antecedents.
3. C. Shonkwiler and K. Theis, *Direct Sampling of Confined Polygons in Linear Time*, *SIAM Journal on Discrete Mathematics* (2026), https://doi.org/10.1137/25M1747610; open full text https://epubs.siam.org/eprint/KDF2FGIFAMTEXDAGYRI7/full. Sections 3--4, 6 study the same unsigned polytope's sampling and coordinate means.
