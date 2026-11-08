# Phase alignment and a sharp pseudospectral merger for positive bidiagonal Koopman weights

## Finding
Let \(\Omega=\{0,1\}^{\mathbb Z}\) with the fair Bernoulli product measure, let \(\tau\) be its bilateral shift, and let \(M\) be any real \(m\times m\) upper-bidiagonal matrix with pairwise distinct positive diagonal entries \(d_1,\ldots,d_m\) and strictly positive superdiagonal entries \(c_1,\ldots,c_{m-1}\). On \(L^2(\Omega;\mathbb C^m)\), define \((Tf)(\omega)=M f(\tau\omega)\).

The spectrum and exact resolvent norm are
\[
\sigma(T)=\bigcup_{j=1}^{m}\{z\in\mathbb C:|z|=d_j\},\qquad
\|(T-zI)^{-1}\|=\|(M-|z|I)^{-1}\|_2
\quad(z\notin\sigma(T)).
\]
Here \(\|\cdot\|_2\) on a finite matrix denotes the induced Euclidean operator norm. Consequently, with the **open resolvent convention**
\[
\Lambda_\varepsilon(T):=\sigma(T)\cup\{z\notin\sigma(T):\|(T-zI)^{-1}\|>\varepsilon^{-1}\},
\]
we have the exact radial characterization
\[
\Lambda_\varepsilon(T)=\{z\in\mathbb C:\sigma_{\min}(M-|z|I)<\varepsilon\}
\quad(\varepsilon>0).
\]

For \(m=2\), put \(M=\begin{pmatrix}a&\gamma\\0&b\end{pmatrix}\), where \(0<a<b\) and \(\gamma>0\). The two spectral circles belong to **two connected components** of \(\Lambda_\varepsilon(T)\) if and only if
\[
0<\varepsilon\le\varepsilon_*:=\frac{\sqrt{(b-a)^2+\gamma^2}-\gamma}{2}.
\]
For \(\varepsilon>\varepsilon_*\) the pseudospectrum is connected. The threshold is strictly smaller than the normal-weight threshold \((b-a)/2\) and decreases strictly with the coupling \(\gamma\).

## Assumptions and scope
All spaces and operator norms are complex Hilbert-space ones. The shift \(\tau\) acts on two-sided sequences; product measure is invariant, ergodic, and nonatomic. The finite matrix is constant in \(\omega\), invertible (positive diagonal), and upper bidiagonal. No claim is made for arbitrary variable matrix weights, arbitrary triangular matrices, or non-Hilbert Köthe–Bochner norms. The pseudospectral boundary uses strict \(>\) resolvent inequality; with the closed \(\ge\) convention the equality case of the merger criterion changes.

## Proof
**1. Full-circle Koopman spectrum.** The Koopman operator \(Uf=f\circ\tau\) is unitary. The coordinate functions \(v_n(\omega)=(-1)^{\omega_n}\), \(n\in\mathbb Z\), form an orthonormal family and satisfy \(Uv_n=v_{n+1}\) or \(v_{n-1}\), depending on the shift convention. Their closed span reduces \(U\) and is a bilateral-shift copy; hence \(\sigma(U)=\mathbb T\). As \(T\) is unitarily identified with \(U\otimes M\), the spectral theorem for \(U\) gives
\[
\|(T-zI)^{-1}\|=\sup_{|\zeta|=1}\|(\zeta M-zI)^{-1}\|_2
=\sup_{|\eta|=|z|}\|(M-\eta I)^{-1}\|_2
\]
whenever \(z\) avoids the spectral circles. Triangularity proves that these are exactly its spectral circles (invertibility on the complement follows from the same uniform direct-integral formula).

**2. Phase alignment.** For \(\eta\notin\{d_1,\ldots,d_m\}\), the only nonzero entries of the upper-triangular inverse are
\[
[(M-\eta I)^{-1}]_{ij}
=\frac{(-1)^{j-i}\prod_{k=i}^{j-1}c_k}{\prod_{k=i}^{j}(d_k-\eta)},\qquad i\le j.
\]
For \(|\eta|=r\) not on a spectral circle, positivity of \(d_k\) gives \(|d_k-\eta|\ge|d_k-r|\). Thus the entrywise moduli of the inverse are bounded by those at \(\eta=r\). Because an upper-bidiagonal inverse has a unique path per nonzero entry, its real signs factor as one row sign times one column sign: writing \(s_k=\operatorname{sgn}(d_k-r)\), the entry sign equals
\[
(-1)^{j-i}\prod_{k=i}^{j}s_k
=\Bigl((-1)^i\prod_{k<i}s_k\Bigr)
\Bigl((-1)^j\prod_{k\le j}s_k\Bigr).
\]
Hence diagonal unitary sign matrices conjugate the real inverse **on its two sides** to its nonnegative entrywise modulus; the Euclidean operator norms agree. For matrices \(A,B\) with \(|A_{ij}|\le B_{ij}\), \(B\ge0\), the inequality \(|Ax|\le B|x|\) gives \(\|A\|_2\le\|B\|_2\). Applying this to the inverses yields
\[
\sup_{|\eta|=r}\|(M-\eta I)^{-1}\|_2=\|(M-rI)^{-1}\|_2.
\]
At a spectral radius, both sides of the equivalent singular-value formula vanish by continuity. This proves the first assertions.

**3. Exact merger criterion.** Put \(h=(b-a)/2\), \(x=r-(a+b)/2\), \(c=\gamma^2/2\). On the closed radial gap \(a\le r\le b\), taking the smaller eigenvalue of \((M-rI)^*(M-rI)\) gives
\[
g(r)^2:=\sigma_{\min}(M-rI)^2=x^2+h^2+c-\sqrt{(2h^2+c)(2x^2+c)}.
\]
As a function of \(u=x^2\in[0,h^2]\), this has derivative
\[
1-\sqrt{\frac{2h^2+c}{2u+c}}<0\quad(0\le u<h^2).
\]
Therefore \(g\) has its unique maximum on \([a,b]\) at \(r_0=(a+b)/2\), where direct simplification yields
\[
g(r_0)=\sqrt{h^2+\gamma^2/4}-\gamma/2=\varepsilon_*.
\]
For \(0\le r<a\), all positive entries of the entrywise modulus of \((M-rI)^{-1}\) increase with \(r\), so \(g(r)\) decreases; for \(r>b\), they decrease with \(r\), so \(g(r)\) increases. Thus the radial set \(\{r\ge0:g(r)<\varepsilon\}\) has exactly two interval components when \(\varepsilon\le\varepsilon_*\), separated by the omitted midpoint circle, and is a single interval when \(\varepsilon>\varepsilon_*\). For radial subsets of the plane, these are exactly the asserted connected-component cases. Finally, \(\sqrt{(b-a)^2+\gamma^2}-\gamma\) is strictly decreasing in \(\gamma>0\).

## Verification
The included `check.py` evaluates induced Euclidean inverse norms for many positive bidiagonal matrices and complex phases; it also independently compares the \(2\times2\) singular-value and threshold identities against direct singular-value decompositions. Its diagnostics are finite spot checks only. The proof above, not these checks, establishes the universal statements.

## Relationship to prior work
Duru, İlter, Kitover, and Orhon (arXiv:2610.24853, first submitted 2026-10-17), Corollary 3.8, prove an upper bound of \(m\) on the number of spectral connected components of an ergodic invertible matrix-weighted composition operator. Our constant positive bidiagonal example realizes \(m\) **spectral** circles, and the new focus is its exact *resolvent norm at every complex argument* and the sharp threshold for *pseudospectral* merger. The earlier theorem does not assert either quantitative property. Trefethen, Contedini, and Embree (2001) analyze pseudospectra of random finite/infinite bidiagonal matrices and give elementary inverse-entry tools relevant to our proof; we do not claim those tools as new. The full extent to which broader bidiagonal pseudospectrum theorems may subsume the constant-fiber result remains a priority caveat.

## Limitations
The conclusion is about strict open pseudospectra and complex \(L^2\), and the exact merger threshold is only classified for fiber dimension two. This is a self-review, not an independent audit, formal certificate, or a proof of global literature novelty. Some nonrandom matrix-theory formulations may imply the radial phase-alignment identity as a special case.

## References
1. H. Duru, S. İlter, A. Kitover, and M. Orhon, *Operators commuting with \(L^\infty\) on Köthe–Bochner spaces*, arXiv:2610.24853 (first public 2026-10-17), especially Corollary 3.8 and Remark 3.10. https://arxiv.org/abs/2610.24853
2. L. N. Trefethen, M. Contedini, and M. Embree, *Spectra, Pseudospectra, and Localization for Random Bidiagonal Matrices*, Communications on Pure and Applied Mathematics **54** (2001), 595–623. https://people.maths.ox.ac.uk/trefethen/publication/PDF/2001_96.pdf
