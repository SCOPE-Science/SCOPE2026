# Extreme-point geometry of quadratic geometric covariances on homogeneous trees

## Finding
Fix an integer \(q\ge2\) and \(0<r<q^{-1/2}\). On the infinite \((q+1)\)-regular tree \(T_q\), write \(d=d(x,y)\) and consider the normalized radial covariance family
\[
K_{a,b}(x,y)=r^d\left(1+a d+b\binom d2\right),\qquad a,b\in\mathbb R.
\]
Let \(I_q=[-2\sqrt q,2\sqrt q]\), and define polynomials in the real variable \(\lambda\) by
\[
D(\lambda)=1+qr^2-r\lambda,\quad E(\lambda)=2qr-\lambda,\quad u=1-r^2,
\]
\[
\begin{aligned}
N_{a,b}(\lambda)={}&uD(\lambda)^2
+a r\left[-2rD(\lambda)-uE(\lambda)\right]D(\lambda)\\
&+b r^2\left[-D(\lambda)^2+2rD(\lambda)E(\lambda)-quD(\lambda)+uE(\lambda)^2\right].
\end{aligned}
\]
Then \(N_{a,b}\) has degree at most two, and the following is an exact complete admissibility test:
\[
\boxed{K_{a,b}\text{ is positive semidefinite on all finite vertex sets}\iff N_{a,b}(\lambda)\ge0\text{ for every }\lambda\in I_q.}
\]
This is a finite algebraic test: for \(N=A\lambda^2+B\lambda+C\), test both endpoints, and, when \(A>0\) and \(-B/(2A)\in I_q\), test \(C-B^2/(4A)\ge0\).

The admissible parameter body is compact, two-dimensional and convex. Its **entire extreme-point set** consists precisely of a continuous one-parameter family \((a_s,b_s)\), \(s\in I_q\), for which
\[
N_{a_s,b_s}(\lambda)=c_s(\lambda-s)^2,\quad c_s>0,
\]
together with exactly one additional point \((a_\partial,b_\partial)\) for which
\[
N_{a_\partial,b_\partial}(\lambda)=c_\partial(4q-\lambda^2),\quad c_\partial>0.
\]
Every such pair exists uniquely. Thus any spectral frequency in the full tree adjacency band can be realized as an exact **double spectral notch** of an extreme admissible radial covariance. The remaining extreme point has simultaneous zeros at both band edges. All admissible kernels, including every boundary/extreme kernel, are strictly positive definite on every finite set of *distinct* vertices; no finite Gram matrix loses rank at a spectral notch.

For a concrete rational instance, at \(q=4\) and \(r=1/4\), the zero-frequency notch and the two-edge extreme have, respectively,
\[
(a_0,b_0)=\left(\frac{285}{164},\frac{225}{164}\right),\qquad
N_{a_0,b_0}(\lambda)=\frac{1215}{41984}\lambda^2,
\]
\[
(a_\partial,b_\partial)=\left(\frac{195}{236},-\frac{225}{236}\right),\qquad
N_{a_\partial,b_\partial}(\lambda)=\frac{3375}{60416}(16-\lambda^2).
\]
These demonstrate the two qualitatively different spectral singularities within a single natural covariance family.

## Assumptions and scope
The infinite tree has all vertices of degree \(q+1\), with graph metric \(d\), and \(q\) is a finite integer at least two. Positivity means \(\sum_{i,j}\bar z_i z_j K_{a,b}(x_i,x_j)\ge0\) for every finitely supported coefficient family. The decay restriction \(0<r<q^{-1/2}\) is essential to the bounded-operator resolvent method; no positivity classification is claimed at or beyond this radius. Repetitions of vertices may of course create Gram null vectors and are excluded from the finite-site strictness assertion. The polynomial frequency \(\lambda\) is the unnormalized adjacency eigenvalue, not a normalized Laplacian eigenvalue.

## Proof
**Adjacency and resolvent.** Let \(A\) be the self-adjoint adjacency operator on \(\ell^2(T_q)\). Its spectrum is \(I_q\) and it has purely absolutely continuous spectrum; its root spectral probability measure \(\mu_q\) has strictly positive density on the interior of \(I_q\):
\[
d\mu_q(\lambda)=\frac{q+1}{2\pi}\frac{\sqrt{4q-\lambda^2}}{(q+1)^2-\lambda^2}\,d\lambda.
\]
This classical adjacency/Kesten formula may also be obtained by solving the cavity Green-function recursion \(h(z)=1/(z-qh(z))\) and \(g(z)=1/(z-(q+1)h(z))\). The absence of atoms follows from the same resolvent boundary values.

For each vertex \(y\), the column \(h_y(x)=r^{d(x,y)}\) is square summable since \(qr^2<1\). The tree recurrence gives
\[
(I-rA+qr^2 I)h_y=(1-r^2)\delta_y.
\]
Since \(D(\lambda)=(1-\sqrt q\,r)^2+r(2\sqrt q-\lambda)>0\) on \(I_q\), the associated bounded kernel operator is
\[
F_r(A),\qquad F_r(\lambda)=\frac{1-r^2}{D(\lambda)}.
\]
The kernel entries of \(r\partial_r F_r(A)\) and \(\tfrac12r^2\partial_r^2F_r(A)\) are \(d r^d\) and \(\binom d2r^d\), respectively. Differentiation of the rational resolvent, valid in operator norm on the subcritical open interval, yields exactly
\[
F_r(\lambda)+ar\partial_rF_r(\lambda)+\frac{br^2}{2}\partial_r^2F_r(\lambda)
=\frac{N_{a,b}(\lambda)}{D(\lambda)^3}.
\]
The spectral theorem and \(\sigma(A)=I_q\) establish the stated equivalence: a negative value of \(N\) on any open part of the band makes the operator indefinite, which supplies a finite-support negative witness by density; nonnegative \(N\) gives a positive operator. The explicit quadratic test follows from elementary minimization on a closed interval.

**Affine identification of the covariance body.** Let \(\nu\) be the strictly positive finite measure \(D^{-3}\mu_q\). The multiplier's diagonal matrix element at any vertex is \(K_{a,b}(x,x)=1\); therefore
\[
\int_{I_q}N_{a,b}(\lambda)\,d\nu(\lambda)=1
\quad\text{for all }a,b.
\]
Conversely the real polynomials of degree at most two with \(\int p\,d\nu=1\) form a two-dimensional affine plane. The map \((a,b)\mapsto N_{a,b}\) is injective: if two pairs gave the same multiplier, their kernels would agree at distances one and two, and \(K(1)=r(1+a)\), \(K(2)=r^2(1+2a+b)\) determine \(a,b\) uniquely. Hence this map is an affine bijection onto that entire plane. It restricts to an affine bijection between the admissible parameter body and
\[
\mathcal P_\nu=\{p\in\mathbb R[\lambda]_{\le2}:p\ge0\text{ on }I_q,\ \int p\,d\nu=1\}.
\]
Strict positivity of \(\nu\) on the band interior makes \(\mathcal P_\nu\) compact; a positive constant polynomial proves its two-dimensional interior is nonempty.

**All extreme points.** Write \(L=2\sqrt q\). If a polynomial \(p\in\mathcal P_\nu\) is everywhere positive on \([-L,L]\), it is interior and not extreme. If it has a zero \(s\) in the open band, nonnegativity forces a double zero, hence it is a positive multiple of \((\lambda-s)^2\). In any convex decomposition into two nonnegative quadratics, both summands must vanish at \(s\), with zero first derivative there, hence both are proportional to that square; normalization forces equality. The same argument holds for a double endpoint zero. If a quadratic vanishes at both endpoints, it is a positive multiple of \(L^2-\lambda^2\), and any convex decomposition must also have both endpoint zeros; normalization again forces equality. Finally, if \(p\) has exactly one simple endpoint zero, factor it as \((L+\lambda)\ell(\lambda)\) or \((L-\lambda)\ell(\lambda)\), with \(\ell\) strictly positive on \([-L,L]\). Every positive affine function on this interval is a nonnegative linear combination of \(L+\lambda\) and \(L-\lambda\). Hence \(p\) is a positive combination of the corresponding endpoint square and \(L^2-\lambda^2\); except for the previously classified limiting cases, normalization gives a nontrivial convex decomposition. These exhaust all possible boundary zeros of a nonnegative quadratic.

In particular the extreme polynomials are precisely
\[
\frac{(\lambda-s)^2}{\int_{I_q}(u-s)^2\,d\nu(u)}\quad (s\in[-L,L]),
\qquad
\frac{L^2-\lambda^2}{\int_{I_q}(L^2-u^2)\,d\nu(u)}.
\]
The affine bijection supplies existence, uniqueness, and the asserted parameter classification. The concrete rational examples follow by setting \(N(0)=N'(0)=0\) and \(N(\pm4)=0\), respectively.

**Strict finite-site positivity.** Any admissible multiplier \(N/D^3\) is positive on the open band apart from at most two spectral points. Since the adjacency operator has purely absolutely continuous spectrum, this multiplier has trivial operator kernel. Thus \(\langle f,K_{a,b}f\rangle>0\) for every nonzero finitely supported \(f\), as required. This proves all assertions. \(\square\)

## Verification
The self-contained script `verify_tree_quadratic.py` uses SymPy for exact symbolic differentiation and rational factoring. It verifies the displayed degree-two rational numerator for symbolic \(q,r,a,b\), both explicit extreme pairs at \(q=4,r=1/4\), the diagonal-normalization coefficients, and direct finite-tree Gram checks. The finite Gram examples are corroborations, not substitutes for the full spectral/convex-geometric proof. The spectral interval and its nonatomicity are classical analytic facts, not inferred from finite sampling.

## Relationship to prior work
Kashaeva (2026) analyzes heat kernels and spectral resolution on free-product Cayley graphs, including homogeneous regular trees as a special case; this motivates finite-parameter harmonic analysis on such noncompact graphs but does not give polynomial-distance covariance admissibility or the extreme-point body considered here. Vergara (2019, Theorem 1.2) gives a general characterization of all positive definite radial tree kernels via positive measures and a trace-class matrix; its Section 6 example concerns an alternating even-distance profile, not this family. A related published first-order classification of \(r^d(1+a d)\) on regular trees gives sharp subcritical intervals and a critical-radius collapse. Its \(b=0\) slice is recovered here, but its statement does not determine the quadratic two-parameter body's continuum of double-notch extreme points, the distinct endpoint extreme, or the exact all-boundary finite-site strictness result. General results are credited; no uniqueness claim is inferred merely from keyword searches.

## Limitations
No claim is made for \(r\ge q^{-1/2}\), irregular trees, other distance profiles, or sharp finite-graph spectral conditioning rates. The spectrum has continuous rather than discrete endpoint frequencies, so vanishing of the infinite-operator multiplier is not a finite Gram singularity. Polynomial positivity is checked exactly, not inferred from finite grids. Priority remains subject to older tree-covariance and truncated moment-cone literature; this is a self-review, not independent validation.

## References
1. K. Kashaeva, *Heat Kernels on Cayley Graphs of Free Products of Finite Groups*, arXiv:2609.28774v1, first public 2026-09-23; https://arxiv.org/abs/2609.28774.
2. I. Vergara, *Positive Definite Radial Kernels on Homogeneous Trees and Products*, arXiv:1907.11476, first public 2019-07-26, especially Theorem 1.2 and Section 6; https://arxiv.org/abs/1907.11476.
3. *A sharp positive-definiteness cone and its collapse for first-order exponential kernels on regular trees*, public mathematical result (2026-10-25); https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-a-sharp-positive-definiteness-cone-and-its-collapse-for-first-or--0ea4651dd31d.
4. H. Kesten, *Symmetric random walks on groups*, Trans. Amer. Math. Soc. 92 (1959), 336–354, for the regular-tree adjacency spectral law.
