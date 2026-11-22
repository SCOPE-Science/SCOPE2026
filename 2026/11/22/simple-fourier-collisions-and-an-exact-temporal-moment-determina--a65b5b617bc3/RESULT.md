# Simple Fourier collisions and an exact temporal-moment determinant for two-step cyclic walks

## Finding
For every integer \(n\ge2\), put \(G=\mathbb Z/n\mathbb Z\) and let
\(\gamma=a\delta_1+b\delta_2\) with real \(a,b>0\), \(a+b=1\) (steps are read modulo \(n\)). Let \(\zeta=e^{2\pi i/n}\), and define the unnormalized Fourier multipliers
\[
\lambda_j=\sum_{x\in G}\gamma(x)\zeta^{jx}=a\zeta^j+b\zeta^{2j},\qquad 0\le j<n.
\]
Let \(V=(\lambda_j^t)_{0\le t,j<n}\). For every \(k\) with \(n/4<k<n/2\), define
\[
r_{n,k}=-2\cos(2\pi k/n),\qquad a_{n,k}=\frac{r_{n,k}}{1+r_{n,k}}.
\]
The \(\lambda_j\) are pairwise distinct unless \(a=a_{n,k}\) for precisely one such \(k\). At that parameter, **the sole collision** is \(\lambda_k=\lambda_{n-k}\), so \(\operatorname{rank}V=n-1\); otherwise \(\operatorname{rank}V=n\). Thus there are exactly
\[N_n=\left\lfloor\frac{n-1}{2}\right\rfloor-\left\lfloor\frac n4\right\rfloor\]
distinct collision biases for each \(n\), all in \((0,2/3)\). The collision biases over all cycle lengths are dense in \((0,2/3)\), whereas every \(a\ge2/3\) is collision-free at all lengths. If \(a,b\) are rational, a collision occurs **if and only if** \(a=b=1/2\) and \(3\mid n\).

Define the one-site temporal-moment matrix \(O\) by \(O_{t,x}=(P^t)_{0,x}\) for \(0\le t,x<n\), where \(P_{x,y}=a\mathbf 1_{\{y=x+1\}}+b\mathbf 1_{\{y=x+2\}}\) on \(G\) (when both steps coincide, their weights add). With
\[
Q_n(a,b)=a^{\varepsilon_n n/2}\prod_{d=1}^{\lfloor(n-1)/2\rfloor}
\left(a^n-(-1)^{n+d}b^n\left(2\cos\frac{\pi d}{n}\right)^n\right),
\qquad \varepsilon_n=\mathbf1_{\{2\mid n\}},
\]
we have the **exact signed determinant**
\[
\boxed{\det O=Q_n(a,b),\qquad |\det V|^2=n^n Q_n(a,b)^2.}
\]
In particular \(Q_n\in\mathbb Z[a,b]\), homogeneous of degree \(n(n-1)/2\), and every zero of \(Q_n(a,1-a)\) in \((0,1)\) is simple. At a collision the unique real unobservable direction for the matrix \(O\) is proportional to \(x\mapsto\sin(2\pi kx/n)\). At \(a=b\) with \(3\mid n\), the colliding Fourier gap satisfies the *exact* identity
\[|\lambda_{n/3}-\lambda_{2n/3}|=\sqrt3\,|a-b|.\]
For fixed such \(n\), this is the smallest pairwise spectral gap in a sufficiently small neighborhood of \(a=b\).

## Assumptions and scope
All times in \(O\) are the integer powers \(t=0,\ldots,n-1\). The Fourier convention uses \(e^{+2\pi i/n}\); changing its sign merely permutes frequencies. The conditions \(a,b>0\), \(a+b=1\) exclude the deterministic boundary walks. The claims concern equality of Fourier eigenvalues, temporal linear identifiability, and its determinant; they **do not** claim that a repeated multiplier by itself implies failure to reconstruct a binary scenery from a stochastic path.

## Proof
1. **Collision rigidity.** For distinct \(j,\ell\), factor
\[
\lambda_j-\lambda_\ell=(\zeta^j-\zeta^\ell)\bigl(a+b(\zeta^j+\zeta^\ell)\bigr).
\]
Thus equality requires \(\zeta^j+\zeta^\ell=-a/b\in(-\infty,0)\). If \(z,w\) are distinct unit-modulus numbers and \(z+w\) is real, then \((z+w)(1-(zw)^{-1})=0\). The possibility \(z+w=0\) is impossible here, hence \(zw=1\): the two frequencies are conjugate. They must be \(k,n-k\), where \(0<k<n/2\); the negative-sum condition is exactly \(n/4<k<n/2\). The cosine is strictly decreasing on this interval, so at most one conjugate pair collides for any fixed bias. Solving \(a/b=-2\cos(2\pi k/n)\) gives the claimed parameters and rank. Counting possible integers \(k\) gives \(N_n\). The map \(x\mapsto-2\cos(2\pi x)\) sends \((1/4,1/2)\) continuously and strictly increasingly onto \((0,2)\), proving the range, density, and sharp universal interval \(a\ge2/3\).
2. **Rational bias.** If \(a/b\in\mathbb Q\), then \(\zeta^k+\zeta^{-k}=-a/b\) is both rational and an algebraic integer, hence an integer. It is strictly between \(-2\) and \(0\), so it must equal \(-1\); this is equivalent to a primitive third root of unity, \(3\mid n\), and \(a/b=1\). Conversely that pair indeed collides.
3. **Determinant via Fourier diagonalization.** Let \(F_{x,j}=\zeta^{xj}\), which is invertible. The transition matrix obeys \(PF=F\operatorname{diag}(\lambda_0,\ldots,\lambda_{n-1})\), and because the observation is at vertex \(0\), \(OF=V\). Hence
\[
\det O=\frac{\det V}{\det F}
=\prod_{0\le j<\ell<n}\frac{\lambda_\ell-\lambda_j}{\zeta^\ell-\zeta^j}
=\prod_{j<\ell}\bigl(a+b(\zeta^j+\zeta^\ell)\bigr).
\]
For each difference \(d=1,\ldots,\lfloor(n-1)/2\rfloor\), the \(n\) unordered pairs \(\{j,j+d\}\) as \(j\) ranges modulo \(n\) are distinct. Their product is
\[
\prod_{j=0}^{n-1}\bigl(a+b(1+\zeta^d)\zeta^j\bigr)
=a^n-(-b(1+\zeta^d))^n
=a^n-(-1)^{n+d}b^n\left(2\cos\frac{\pi d}{n}\right)^n,
\]
using \(1+\zeta^d=2\cos(\pi d/n)e^{\pi i d/n}\). When \(n\) is even, the \(n/2\) remaining antipodal pairs contribute \(a^{n/2}\). This proves the factorization. The product before factoring is fixed by permutations of the roots of \(z^n-1\), hence has integer coefficients; alternatively it is the quotient of two Vandermonde determinants expressed as a symmetric polynomial in the integral roots. The standard root-of-unity Vandermonde identity \(|\det F|^2=n^n\) proves the displayed magnitude identity.
4. **Simple zeros and missing mode.** Each possible collision is one pair and the factor \(a+b(\zeta^k+\zeta^{-k})\) is affine and has a nonzero derivative along \(b=1-a\); all other factors remain nonzero there. Thus each zero of \(Q_n(a,1-a)\) is simple, and the Vandermonde rank loss is one. At resonance the real sine vector is a difference of the colliding Fourier eigenvectors with value zero at the observed coordinate; it spans the real kernel. If \(3\mid n\), the two colliding roots have difference of modulus \(\sqrt3\) and sum \(-1\), proving the final exact-gap identity. The other finitely many gaps are positive at \(a=b\), giving local minimality by continuity.

## Verification
The standalone `verify.py` carries out exact rational Gaussian elimination on the observation matrices for all \(2\le n\le12\) and four biases, comparing determinants with two independently evaluated product expressions. It tests the predicted unique-collision pairs through \(n=18\) and the exact local gap through \(n=15\). The script uses only Python 3 standard-library modules. It verifies finite samples, not the infinite-parametric theorem, which follows from the preceding proof.

## Relationship to prior work
Finucane, Tamuz and Yaari (2011 preprint) study Fourier-multiplier distinctness as a criterion for reconstructing sceneries, and explicitly give an irrational two-step collision on \(\mathbb Z/7\mathbb Z\) (Theorem 5.1). That example is a special case of the collision locus above; it is not claimed as new. Matzinger and Lember (2006) study the same one-or-two-step scenery walk and establish reconstruction for an appropriate bias range, but their full text was not available for a complete implication comparison. The present claim is instead the all-length classification of *every* Fourier collision, its single-defect rank law, and an exact signed temporal-moment determinant; probabilistic scenery reconstruction is not being re-proved. The cycle-observability literature for symmetric Laplacian consensus systems concerns a different transition operator and does not by its published abstract imply this determinant.

## Limitations
No claim is made about full statistical scenery reconstruction at singular biases, noise robustness bounds from the determinant alone, or general steps other than \(1,2\). The full 2006 Matzinger–Lember paper has not been inspected, leaving a historical-priority risk for statements about the same two-step walk. This proof is a finite-dimensional algebraic argument, not an independent external validation.

## References
- H. Finucane, O. Tamuz, Y. Yaari, *Scenery Reconstruction on Finite Abelian Groups*, arXiv:1105.5569, publicly posted 2011-05-27, https://arxiv.org/abs/1105.5569.
- H. Matzinger, J. Lember, *Reconstruction of periodic sceneries seen along a random walk*, Stochastic Processes and their Applications 116 (2006), 1584–1599, https://doi.org/10.1016/j.spa.2006.03.006.
- G. Parlangeli, G. Notarstefano, *On the observability of path and cycle graphs*, IEEE CDC (2010), https://doi.org/10.1109/CDC.2010.5717507.
