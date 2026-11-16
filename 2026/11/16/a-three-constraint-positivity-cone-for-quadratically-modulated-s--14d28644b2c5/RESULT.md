# A three-constraint positivity cone for quadratically modulated spherical Poisson kernels

## Finding
Let \(0<r<1\), \(P_n\) be Legendre polynomials with \(P_n(1)=1\), and \(x,y\in\mathbb S^2\). For any real \(a,b\), consider the isotropic kernel
\[
K_{r,a,b}(x,y)=\frac{1-r^2}{(1-2r\,x\cdot y+r^2)^{3/2}}\bigl(1+aP_1(x\cdot y)+bP_2(x\cdot y)\bigr).
\]
Define three affine functions
\[
\begin{aligned}
L_0&=1+ar+br^2,\\
L_1&=1+a\frac{1+2r^2}{3r}+b\frac{2+3r^2}{5},\\
L_\infty&=1+a\frac{1+r^2}{2r}+b\frac{3r^4+2r^2+3}{8r^2}.
\end{aligned}
\]
Then \(K_{r,a,b}\) is positive semidefinite on **every** finite configuration in \(\mathbb S^2\) if and only if
\[
\boxed{L_0\ge0,\qquad L_1\ge0,\qquad L_\infty\ge0.}
\]
All three conditions are necessary and nonredundant for every \(0<r<1\). The admissible planar region has exactly two finite vertices, corresponding to \((L_0,L_1)=(0,0)\) and \((L_1,L_\infty)=(0,0)\):
\[
\boxed{(a,b)=\left(-\frac6r,\frac5{r^2}\right),\quad
\left(-\frac{9r(3r^2+5)}{6r^4+31r^2+15},\frac{20r^2}{6r^4+31r^2+15}\right).}
\]
Every admissible kernel is **strictly** positive definite on each finite set of pairwise distinct points. It is \(C\)-universal on \(\mathbb S^2\) if and only if \(L_0>0\) and \(L_1>0\) (with \(L_\infty\ge0\) already assumed). Thus the high-degree facet \(L_\infty=0\) can remain universal, whereas equality on either finite-degree facet destroys universality without destroying finite-site strictness.

## Assumptions and scope
The domain is the real unit two-sphere with its ordinary inner product, the real polynomial parameters \(a,b\) are unrestricted, and the Poisson scale is \(0<r<1\). Positive semidefiniteness means nonnegative Hermitian Gram quadratic forms for all finite point sets, allowing repeated points; strict positive definiteness is only asserted for distinct points. The normalized zonal harmonics are \(P_n\), with \(P_0=1\), \(P_1(t)=t\), and \(P_2(t)=(3t^2-1)/2\). No extension to other sphere dimensions or higher modulation degrees is claimed.

## Proof
The classical ball-Poisson expansion and Legendre three-term recurrence are
\[
\frac{1-r^2}{(1-2rt+r^2)^{3/2}}=\sum_{n=0}^\infty(2n+1)r^nP_n(t),\qquad
 tP_k(t)=\frac{k+1}{2k+1}P_{k+1}(t)+\frac{k}{2k+1}P_{k-1}(t).
\]
The series converges absolutely uniformly for fixed \(0<r<1\). Multiplying by \(1+aP_1+bP_2\) and collecting terms gives
\[
K_{r,a,b}(x,y)=\sum_{n=0}^\infty(2n+1)r^n\Lambda_nP_n(x\cdot y),\qquad
\Lambda_n=1+aS_n+bT_n,
\]
where for every integer \(n\ge0\)
\[
S_n=\frac{n/r+(n+1)r}{2n+1}
\]
and
\[
T_n=\frac32\left[
\frac{n(n-1)}{(2n-1)(2n+1)r^2}
+\frac{n^2}{(2n-1)(2n+1)}
+\frac{(n+1)^2}{(2n+1)(2n+3)}
+\frac{(n+1)(n+2)r^2}{(2n+1)(2n+3)}
\right]-\frac12.
\]
The fractions with numerator zero at \(n=0,1\) are interpreted normally; none of their displayed denominators vanishes for integral \(n\ge0\). In particular, \((S_0,T_0)=(r,r^2)\), \((S_1,T_1)=((1+2r^2)/(3r),(2+3r^2)/5)\), and
\[
(S_\infty,T_\infty)=\lim_{n\to\infty}(S_n,T_n)=\left(\frac{1+r^2}{2r},\frac{3r^4+2r^2+3}{8r^2}\right).
\]
Schoenberg's characterization on \(\mathbb S^2\) states that all Legendre coefficients must be nonnegative. Hence positivity requires \(\Lambda_0=L_0\ge0\), \(\Lambda_1=L_1\ge0\), and \(L_\infty=\lim\Lambda_n\ge0\); conversely, the following **exact barycentric identity** establishes sufficiency.

For integer \(n\ge2\), set
\[
D_n=(2n-1)(2n+1)(2n+3)(r^2+15)
\]
and
\[
\begin{aligned}
w_{0,n}&=\frac{3(n-1)[(10-2r^2)n+r^2+15]}{D_n},\\
w_{1,n}&=\frac{15n[(2r^2+6)n+9-r^2]}{D_n},\\
w_{\infty,n}&=\frac{4n(n-1)[(2r^2+30)n+45-r^2]}{D_n}.
\end{aligned}
\]
Direct rational simplification yields the three identities
\[
w_{0,n}+w_{1,n}+w_{\infty,n}=1,\quad
S_n=w_{0,n}S_0+w_{1,n}S_1+w_{\infty,n}S_\infty,\quad
T_n=w_{0,n}T_0+w_{1,n}T_1+w_{\infty,n}T_\infty.
\]
Every weight is strictly positive for \(0<r<1\), \(n\ge2\); thus
\[
\boxed{\Lambda_n=w_{0,n}L_0+w_{1,n}L_1+w_{\infty,n}L_\infty>0\quad(n\ge2)}
\]
throughout the admitted region, because the triple \((L_0,L_1,L_\infty)\) cannot vanish simultaneously: the determinant of the three row vectors \((1,S_j,T_j)\), indexed by \(j=0,1,\infty\), is
\[
\frac{(1-r^2)^2(r^2+15)}{120r^3}>0.
\]
This completes the equivalence and also proves positivity of every spectral degree \(n\ge2\), including on every boundary.

All large even and odd Schoenberg coefficients are strictly positive, hence the established strict-positive-definiteness criterion for spheres of dimension at least two implies finite-site strictness. The invariant-kernel universality criterion gives \(C\)-universality precisely when **every** coefficient is positive. Since all degrees at least two already are, this reduces to \(L_0>0\) and \(L_1>0\).

To check sharpness of each finite inequality, solving the pairs \(L_0=L_1=0\) and \(L_1=L_\infty=0\) gives the two displayed parameter vertices. At the first vertex \(L_\infty=(1-r^2)(r^2+15)/(8r^4)>0\); at the second, \(L_0=(1-r^2)(r^2+15)/(6r^4+31r^2+15)>0\). The intersection \(L_0=L_\infty=0\) instead has \(L_1<0\). The two admissible vertices and outward boundary rays therefore expose all three inequalities and establish nonredundancy.

## Verification
An independent standard-library Python checker, `check.py`, validates the rational barycentric identities and strict positivity of their weights over an exact rational grid, reproduces the finite-degree Legendre coefficients through polynomial multiplication, and checks the two vertices. These are supplementary checks; the universal-in-\(n\) argument is the displayed symbolic rational identity and sign analysis. The recurrence and nonzero determinant establish the infinite statement without numerical extrapolation.

## Relationship to prior work
Schoenberg (1942) gives the Legendre coefficient characterization but not a finite parameter test for this particular signed polynomial modulation. The 2026 paper *Universality of kernels on Riemannian symmetric spaces* establishes the relevant coefficientwise \(C\)-universality criterion and gives sphere examples, but not the present three-half-plane Poisson modulation region. Buhmann and Jäger (2021) provide general strict-positivity criteria for spherical kernels without this specialized coefficient cone. An independently published treatment of a **geodesic exponential times one cosine** gives a different baseline and a one-dimensional coefficient threshold, not the present **ball-Poisson times two Legendre modes** or its barycentric reduction. The analytic identity here is parameter-specific, rather than an implication of the general criteria alone.

## Limitations
The result concerns the unit two-sphere, classical ball-Poisson kernel, and polynomial modulation of Legendre degrees one and two only. It does not assert a corresponding three-facet classification in higher sphere dimensions or for higher polynomial degrees. The literature comparison is bounded and does not establish exhaustive priority. No independent mathematical audit has yet been performed.

## References
1. I. J. Schoenberg, *Positive definite functions on spheres*, Duke Mathematical Journal 9 (1942), 96–108.
2. S. Said, N. Da Costa, F. Steinert and C. Mostajeran, *Universality of kernels on Riemannian symmetric spaces* (2026), https://arxiv.org/abs/2608.00010.
3. M. Buhmann and J. Jäger, *Strict positive definiteness of convolutional and axially symmetric kernels on d-dimensional spheres* (2021), https://arxiv.org/abs/2105.02586.
4. D. Chen, V. A. Menegatto and X. Sun, *A necessary and sufficient condition for strictly positive definite functions on spheres*, Proceedings of the American Mathematical Society 131 (2003), 2733–2740.
5. T. Gneiting, *Strictly and non-strictly positive definite functions on spheres* (2013), https://arxiv.org/abs/1111.7077.
