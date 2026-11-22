# A spectral-hole dichotomy for parent composition on one-ended comb trees

## Finding
Let \(T_{\ell}\) be a rooted comb tree consisting of an infinite ray \(v_0,v_1,\ldots\) and, at each \(v_n\) for \(n\ge1\), one finite terminal tooth of length \(\ell_n\in\mathbb N\). Let \(C\) be composition by the parent map, fixing the root, on the complex tree Lipschitz space \(\mathcal L(T_{\ell})\). The ordinary spectrum is always \(\overline{\mathbb D}\), but its **Fredholm essential spectrum** satisfies the exact dichotomy
\[
\sigma_{\mathrm e}(C)=
\begin{cases}
\{0\}\cup\mathbb T,&\sup_n\ell_n<\infty,\\
\overline{\mathbb D},&\sup_n\ell_n=\infty.
\end{cases}
\]
In the bounded-tooth regime, for each \(0<|\lambda|<1\), the operator \(\lambda I-C\) is Fredholm of index \(-1\), whereas it is not Fredholm at \(\lambda=0\) or anywhere on \(\mathbb T\). In the unbounded-tooth regime it is non-Fredholm for every \(|\lambda|\le1\). It is invertible for \(|\lambda|>1\) in either regime.

In particular, two one-ended trees of uniformly bounded vertex degree, and parent composition operators with identical ordinary spectra, can have respectively a disconnected Fredholm essential spectrum (an isolated point plus a circle) and a filled essential spectral disk.

## Assumptions and scope
The ray vertices are \(v_n\), \(n\ge0\), with root \(v_0\) and parent \(v_{n-1}\) for \(v_n\), \(n\ge1\). For each \(n\ge1\) attach vertices \(w_{n,k}\), \(1\le k\le\ell_n\), with parent of \(w_{n,1}\) equal to \(v_n\), and parent of \(w_{n,k}\) equal to \(w_{n,k-1}\) for \(k\ge2\). No other vertices or edges occur. Each \(\ell_n\) is a finite positive integer; the sequence need not be monotone. These trees are locally finite, have exactly one infinite end, and have degrees at most three.

The complex Banach space \(\mathcal L(T_{\ell})\) consists of all vertex functions \(f\) such that
\[
\|f\|_{\mathcal L}=|f(v_0)|+\sup_{u\ne v_0}|f(u)-f(p(u))|<\infty.
\]
The parent map \(p\) fixes \(v_0\). We put \((Cf)(u)=f(p(u))\). Fredholm essential spectrum is defined here as the set of \(\lambda\) for which \(\lambda I-C\) is not Fredholm; it is not the index-zero Weyl spectrum.

## Proof
**1. Exact Banach-space model.** The coordinate map
\[
Df=\bigl(f(v_0),(f(u)-f(p(u)))_{u\ne v_0}\bigr)
\]
is an isometric bijection from \(\mathcal L(T_{\ell})\) to \(\mathbb C\oplus_1\ell_\infty(T_{\ell}\setminus\{v_0\})\). Surjectivity follows by summing the prescribed edge differences along each unique finite root-to-vertex path; the resulting function is Lipschitz with precisely the prescribed coordinates, even if its point values grow with depth. Under \(D\), \(C\) acts as \(1\oplus B\). For every nonroot vertex \(u\),
\[
(Bx)(u)=\begin{cases}0,&p(u)=v_0,\\x(p(u)),&p(u)\ne v_0.\end{cases}
\]
Thus \(\|B\|=1\). Split coordinates into the spine \(a=(x(v_n))_{n\ge1}\in\ell_\infty(\mathbb N)\) and teeth \(b=(x(w_{n,k}))\in Y=\ell_\infty(\bigsqcup_n\{1,\ldots,\ell_n\})\). The resulting operator on the max-norm direct sum is exactly
\[
B=\begin{pmatrix}U&0\\L&N\end{pmatrix},
\]
where \((Ua)_1=0\), \((Ua)_n=a_{n-1}\) for \(n\ge2\); \((La)_{n,1}=a_n\) and \((La)_{n,k}=0\) for \(k\ge2\); and \((Nb)_{n,1}=0\), \((Nb)_{n,k}=b_{n,k-1}\) for \(k\ge2\). Both \(L\) and \(N\) have norm one. The operator \(N\) is the bounded direct product of the finite nilpotent forward shifts \(J_{\ell_n}\).

**2. Uniformly bounded teeth.** Suppose \(\ell_n\le M\) for all \(n\), for some integer \(M\). Then \(N^M=0\), and, for any nonzero \(\lambda\),
\[
(\lambda I-N)^{-1}=\sum_{j=0}^{M-1}\lambda^{-j-1}N^j.
\]
This is a bounded operator on all of \(Y\), without dependence on the number of teeth. Block Gaussian elimination therefore gives an equivalence, by bounded invertible left and right factors, between \(\lambda I-B\) and the diagonal operator \((\lambda I-U)\oplus(\lambda I-N)\). Consequently their Fredholm indices and Fredholm status agree, and the second summand contributes zero index.

For \(0<|\lambda|<1\), the unilateral forward shift \(U\) on \(\ell_\infty(\mathbb N)\) has closed, injective range under \(\lambda I-U\), since
\[
\|(\lambda I-U)a\|_\infty\ge(1-|\lambda|)\|a\|_\infty.
\]
Its range is the kernel of the nonzero bounded linear functional
\[
F_\lambda(y)=\sum_{n\ge1}\lambda^{n-1}y_n.
\]
Indeed, the finite sum through \(N\) for \(y=(\lambda I-U)a\) equals \(\lambda^N a_N\), tending to zero. Conversely, if \(F_\lambda(y)=0\), set \(a_n=-\sum_{k=n+1}^\infty\lambda^{k-n-1}y_k\); these are bounded and satisfy \((\lambda I-U)a=y\). Hence its cokernel is exactly one-dimensional and its index is \(-1\). At \(\lambda=0\), \(N\) has infinitely many independent kernel vectors (one terminal vertex per tooth), so \(-B\) and \(-C\) cannot be Fredholm. For \(|\lambda|=1\), \(\lambda I-U\) is injective but not bounded below: taking \(\zeta=\lambda\), the unit vectors \(a_n=\zeta^{-n}\min(n/m,1)\) satisfy \(\|(\lambda I-U)a\|_\infty\le1/m\). Therefore the range is nonclosed, and the triangular operator is not Fredholm.

**3. Unbounded tooth lengths.** Suppose \(\sup_n\ell_n=\infty\). For any fixed \(0<|\lambda|<1\), choose a tooth of length \(m\) and put, on just that tooth, \(b_k=\lambda^{-k}|\lambda|^m\), with all other spine and tooth coordinates zero. Then \(\|b\|_\infty=1\), and
\[
\|(\lambda I-N)b\|_\infty=|\lambda|^m.
\]
Letting the chosen lengths tend to infinity makes \(\lambda I-B\) fail to be bounded below. It is injective: its spine equation forces the spine vector to vanish (\(\lambda I-U\) is injective), and each finite tooth equation then forces the corresponding tooth vector to vanish. Thus its range is not closed. The same reasoning applies to \(|\lambda|=1\), using on a tooth of length \(m\) the vector \(b_k=\lambda^{-k}k/m\), whose norm is one and whose residual is \(1/m\). At \(\lambda=0\), the infinitely many terminal-tooth coordinates lie in \(\ker B\), so the operator is not Fredholm.

**4. Exterior and ordinary spectrum.** As \(\|C\|=1\), Neumann inversion makes \(\lambda I-C\) invertible whenever \(|\lambda|>1\). Each \(|\lambda|<1\) lies in the ordinary spectrum in both regimes: if lengths are bounded and \(\lambda\ne0\), the spine equation is not surjective, and at zero there is a nontrivial kernel; in the unbounded regime the nonclosed-range argument applies at nonzero \(\lambda\). At the unit circle the Fredholm failure proved above implies noninvertibility. This proves both the ordinary spectral assertion and the two essential spectral alternatives.

## Verification
The standalone script `check_comb.py` executes 1,085 exact rational assertions checking finite nilpotent-block inverses, the exponentially small residuals of the unbounded-tooth construction, unit-circle ramp residuals, and telescoping identities for the spine range functional. Running `python check_comb.py` prints `COMB_EXACT_FINITE_CHECK_OK 1085`. These finite assertions supplement but do not establish any claim about infinite trees; the uniform-in-length estimates and Banach-space arguments above do that.

## Relationship to prior work
Kong and Liu establish Fredholm criteria and index for a weighted composition operator itself, in particular at the spectral parameter zero. Their classification is consistent with non-Fredholmness of the present parent composition operator at zero, but does not state the Fredholm classification of the pencil \(\lambda I-C\). Rivera-Guasco and Martínez-Avendaño establish the ordinary spectrum of the forward tree shift on tree Lipschitz spaces; this result refines the spectral description by computing the exact Fredholm essential spectrum and the nonzero interior Fredholm index for one-ended comb trees. The distinction between uniformly nilpotent and increasingly long finite Jordan blocks is classical; the claimed contribution is the resulting sharp geometric dichotomy for the specified Lipschitz composition family, not a new general theorem about nilpotent matrices.

## Limitations
The classification concerns the stated one-spine comb with one positive finite tooth at every nonroot spine vertex, on the full (not little) Lipschitz space. It does not assert the same classification for arbitrary trees, weighted parent maps or other essential-spectrum conventions. The bounded-tooth upper bound need not be known in advance; only the existence of a finite bound matters. No claim of independent validation or priority proof is made.

## References
1. J. Kong and L. Liu, *Fredholm weighted composition operators on the Lipschitz space of a tree*, arXiv:2611.11737v1, first public 2026-11-09, https://arxiv.org/html/2611.11737v1 (especially Theorem 4.3).
2. E. Rivera-Guasco and R. A. Martínez-Avendaño, *The forward and backward shift on the Lipschitz space of a tree*, arXiv:1906.02372, first public 2019-06-06, https://arxiv.org/pdf/1906.02372 (especially Theorems 3.3 and 3.6).
3. Standard Banach-space results used: bounded inverse theorem, Neumann series, and invariance of Fredholm index under bounded invertible operator equivalence.
