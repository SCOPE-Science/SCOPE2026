# A sharp two-eigenvalue phase for odd cubic harmonic-Bergman Toeplitz operators

## Finding
Let \(\mathbb D\) be the open unit disk and let \(L_h^2(\mathbb D)\) be the complex harmonic Bergman Hilbert space for normalized area measure \(dA=\pi^{-1}dx\,dy\). For \(a\in\mathbb C\), put \(p_a(z)=z^3+az\) and define \(\mathbb T_{p_a}u=P_h(p_au)\), where \(P_h\) is the orthogonal projection onto \(L_h^2\). Define the sharp parameter
\[
\tau=\frac{2(7+\sqrt{13})}{9}.
\]
Then the **complete spectrum**, including all exceptional isolated points, is
\[
\sigma(\mathbb T_{p_a})=p_a(\partial\mathbb D)\ \cup\ E_a,
\qquad
E_a=\begin{cases}
\left\{\displaystyle\frac{3a}{8}\sqrt{-a},-\frac{3a}{8}\sqrt{-a}\right\},&\tau<|a|<4,\\
\varnothing,&|a|\le\tau\text{ or }|a|\ge4.
\end{cases}
\]
The displayed set is independent of the branch of the square root. In the open phase \(\tau<|a|<4\), its two members are distinct, lie off the essential spectral curve, and are isolated eigenvalues with one-dimensional eigenspaces. In all other parameter regimes there are no off-curve eigenvalues.

For \(\alpha^2=-a/4\) with \(\tau<|a|<4\), the eigenvalue \(\lambda=-3\alpha^3\) has the explicit harmonic eigenfunction
\[
u_\alpha(z)=\frac{1}{(1-\alpha\overline z)^2}
-\frac{z(z+\tfrac52\alpha)}{z^2+\alpha z-3\alpha^2}.
\]
Both poles of the analytic term are strictly outside the closed unit disk in this regime.

## Assumptions and scope
The analytic polynomial is \(z^3+az\), with **arbitrary complex** \(a\), including zero and the two boundary parameter values. The Hilbert space is unweighted harmonic Bergman space, not analytic Bergman space: every harmonic element has the unique decomposition \(f(z)+g(\overline z)\) with \(f\in zL_a^2\) and \(g\in L_a^2\), where \(L_a^2\) denotes analytic Bergman space. The inner product uses normalized area on \(\mathbb D\). The set \(p_a(\partial\mathbb D)\) may self-intersect; the theorem makes no assertion that it is a Jordan curve.

## Proof
**1. Spectral reduction.** The established harmonic Bergman Toeplitz block representation, together with the index-zero Fredholm theorem for continuous symbols, says that the essential spectrum of \(\mathbb T_{p_a}\) is \(p_a(\partial\mathbb D)\). For \(\lambda\notin p_a(\partial\mathbb D)\), write \(\psi=p_a-\lambda\); the Fredholm index is zero. Thus \(\lambda\) belongs to the spectrum exactly when the kernel is nonzero. On \(zL_a^2\oplus L_a^2\), that kernel is governed by
\[
\psi f+P(\psi(z)g(\overline z))=0,
\qquad T_{\widehat\psi}g=0.
\]
Here \(P\) is analytic Bergman projection and \(\widehat\psi(z)=\psi(\overline z)\). For the second equation, its kernel has dimension equal to the number \(N\in\{0,1,2,3\}\) of zeros of \(\psi\) in \(\mathbb D\), counted with multiplicity, and is spanned by the Bergman kernels and their parameter derivatives at the interior roots. The omitted rank-one term in the general block representation vanishes on this kernel: evaluations and the necessary derivatives of \(\psi\) vanish at its roots.

**2. Explicit polynomial interpolation map.** For the analytic Bergman kernel \(K_{\overline w}(z)=(1-wz)^{-2}\), the moment identity
\[
P\left[\frac{z^k-w^k}{(1-w\overline z)^2}\right]
=\frac{z}{k+1}\sum_{j=0}^{k-1}(j+1)(k-j+1)z^{k-j-1}w^j
\]
gives, when \(\psi(w)=0\),
\[
P\bigl[\psi(z)K_{\overline w}(\overline z)\bigr]
=z h(z,w),\quad
h(z,w)=a+z^2+\frac32zw+\frac32w^2.
\]
At repeated roots, differentiation with respect to \(w\) produces the corresponding derivatives of \(h\), because derivatives of \(\psi\) through the root multiplicity vanish. Hence the first equation becomes \(f=-zq(z)/\psi(z)\), where \(q\) is a polynomial of degree at most two assembled from \(h(\cdot,w)\) and its derivatives at all interior roots. Analyticity of \(f\) requires that \(q\) vanish at every such root to at least its multiplicity.

If \(N=0\), then \(g=0\) and \(f=0\). If \(N=3\), the degree bound forces \(q\equiv0\). Writing the coefficients of \(g\) as confluent kernel coordinates, the coefficients of \(q\) in descending powers of \(z\) are an invertible triangular transform of the first three confluent moments (diagonal \(1,3/2,3/2\)). The corresponding Hermite–Vandermonde matrix is invertible for every multiset of three interior roots, so \(g=0\). These arguments include \(a=0\), repeated roots, and the triple zero.

**3. Exactly one interior root.** If the unique interior root is \(\alpha\), it is simple. The divisibility condition is
\[
h(\alpha,\alpha)=a+4\alpha^2=0.
\]
Consequently \(a=-4\alpha^2\), \(\lambda=p_a(\alpha)=-3\alpha^3\), and
\[
\psi(z)=(z-\alpha)(z^2+\alpha z-3\alpha^2).
\]
The remaining roots are
\[
\beta_{\pm}=\frac{-1\pm\sqrt{13}}2\,\alpha.
\]
They both lie strictly outside the unit disk while \(\alpha\) lies inside precisely when
\[
\frac{2}{\sqrt{13}-1}<|\alpha|<1
\quad\Longleftrightarrow\quad
\tau<|a|<4.
\]
Both possible signs of \(\alpha\) yield an eigenvalue; the kernel dimension equals one because the interior root is unique. Factoring \(h(z,\alpha)=(z-\alpha)(z+\tfrac52\alpha)\) gives the explicit eigenfunction displayed above. If either inequality is an equality, a root lies on \(\partial\mathbb D\), so \(\lambda\) lies on the essential curve and is not an isolated exceptional eigenvalue.

**4. Two distinct interior roots are impossible at an eigenvalue.** Denote them by \(x,y\), the exterior root by \(\gamma\), and write \(s=x+y=-\gamma\), \(t=xy\). The two required interpolation conditions have determinant
\[
\det\begin{pmatrix}h(x,x)&h(x,y)\\h(y,x)&h(y,y)\end{pmatrix}
=-\frac34(x-y)^2(-2a+2x^2+9xy+2y^2).
\]
As \(a=t-s^2\), the vanishing condition for distinct \(x,y\) is \(4s^2+3t=0\). Thus \(t=-4s^2/3\), and the interior roots must be
\[
\{x,y\}=\left\{\frac{1+\sqrt{19/3}}2\,s,\ \frac{1-\sqrt{19/3}}2\,s\right\}.
\]
But \(|\gamma|=|s|>1\); the first displayed root then has modulus greater than one, a contradiction.

**5. Two coinciding interior roots are also impossible.** A double root \(\alpha\) of \(\psi\) satisfies \(a=-3\alpha^2\), and the third root is \(-2\alpha\). The necessary confluent interpolation matrix is
\[
\begin{pmatrix}
 h(\alpha,\alpha)&\partial_w h(\alpha,\alpha)\\
 \partial_z h(\alpha,\alpha)&\partial_z\partial_w h(\alpha,\alpha)
\end{pmatrix},
\]
whose determinant is \(-57\alpha^2/4\), nonzero for a genuine double root \(\alpha\ne0\). If \(\alpha=0\), all three roots coincide in the disk, already excluded in step 2. If a zero of \(\psi\) lies on \(\partial\mathbb D\), then \(\lambda\) is on the essential curve and not under consideration.

The four cases exhaust all possible off-curve spectral points and establish the theorem.

## Verification
Run `python check_cubic.py` with SymPy at least 1.12. The checker verifies the projection polynomial, the two-interior-root determinant factorization, its symmetric-polynomial reduction, the confluent determinant, the one-interior-root factorization and sharp threshold, plus exact sample regimes. An execution returned `ODD_CUBIC_HARMONIC_BERGMAN_CERTIFICATES_OK 31`. The checker verifies algebraic identities; the Fredholm reduction, Hermite interpolation and universal root-location arguments above are analytical and are not inferred from the finite tests.

## Relationship to prior work
Huang, Wang and Zhao (2026, arXiv:2610.09638v1) prove that the spectrum for any analytic polynomial is its boundary image plus at most \((n-1)2^{n-1}\) isolated eigenvalues. Their explicit interpolation kernel \(h\) and reduction to finite determinants are the point of departure, not new results here. The present theorem classifies the entire off-curve spectrum for every complex parameter in the odd cubic family, determines the exact interval in which precisely two isolated eigenvalues occur, and produces their explicit harmonic eigenfunctions. Wang and Zhao (2021) establish Weyl's theorem for certain low-degree polynomial symbols and give disconnected-spectrum examples; the available record does not settle this parameter-wide cubic classification. A relevant full-text comparison with that older paper could not be completed, so priority requires further checking.

## Limitations
Only the unweighted harmonic Bergman space and the odd cubic symbols are classified. The theorem does not calculate resolvent norms or cover general cubics \(z^3+bz^2+az+c\), arbitrary higher degrees, or analytic Bergman Toeplitz operators. Independent mathematical review and a comprehensive historical priority search have not been performed. The proof of the pre-existing Fredholm and block representation statements is cited rather than reproduced.

## References
1. M. Huang, J. Wang and X. Zhao, *The spectral structure of Toeplitz operators with polynomial symbols on the harmonic Bergman space*, arXiv:2610.09638v1 (first posted 2026-10-07), especially Lemma 2.2 and Theorem 3.1. https://arxiv.org/html/2610.09638v1
2. C. Wang and X. Zhao, *Weyl's theorem for Toeplitz operators with polynomial symbols on the harmonic Bergman space*, J. Math. Anal. Appl. 495 (2021), article 124770. https://doi.org/10.1016/j.jmaa.2020.124770
3. K. Guo and D. Zheng, *Toeplitz algebra and Hankel algebra on the harmonic Bergman space*, J. Math. Anal. Appl. 276 (2002), 213–230. (Cited for the essential-spectrum and Fredholm index-zero framework in Reference 1.)
