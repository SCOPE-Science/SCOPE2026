# Arithmetic spectral law for commutators of two integer block averages

## Finding

For each integer \(p\ge 1\), let \(E_p\) be the orthogonal projection on \(\ell^2(\mathbb N_0)\) onto the sequences constant on each consecutive block \(\{pj,\ldots,pj+p-1\}\). Equivalently, with \(W_pf(z)=(1+z+\cdots+z^{p-1})f(z^p)\) acting on the Hardy space \(H^2\), identify the Taylor coefficients with \(\ell^2\) and put \(E_p=p^{-1}W_pW_p^*\).

Take integers \(p,q\ge2\) and let \(g=\gcd(p,q)\), \(m=\min(p,q)/g\), and \(n=\max(p,q)/g\). If \(m=1\), then \([E_p,E_q]=0\). Otherwise \(2\le m<n\) and \(m,n\) are coprime. For \(1\le j<m\), let \(r_j\in\{1,\ldots,m-1\}\) be the residue of \(jn\) modulo \(m\), and construct the real \(m\)-by-\(m\) path Laplacian

\[
\langle u,L_{m,n}u\rangle=\sum_{j=1}^{m-1}\frac{r_j(m-r_j)}{m}|u_j-u_{j-1}|^2,\qquad u=(u_0,\ldots,u_{m-1})\in\mathbb C^m.
\]

Its eigenvalues are simple and obey \(0=\mu_0<\mu_1<\cdots<\mu_{m-1}<n\). Put \(\eta_k=\mu_k/n\). The complete spectrum and Fredholm essential spectrum of the skew-adjoint commutator \(C_{p,q}=[E_p,E_q]\) are identical:

\[
\sigma(C_{p,q})=\sigma_{\mathrm{ess}}(C_{p,q})=
\{0\}\cup\left\{\pm i\sqrt{\eta_k(1-\eta_k)}:1\le k<m\right\}.
\]

Every displayed spectral value is an eigenvalue of infinite multiplicity (with multiplicities summed if distinct indices give the same value), and

\[
\|C_{p,q}\|=\|C_{p,q}\|_{\mathrm{ess}}
=\max_{1\le k<m}\sqrt{\eta_k(1-\eta_k)}\in(0,1/2].
\]

Consequently the two block averages commute **if and only if** one of \(p,q\) divides the other; otherwise their commutator is noncompact and belongs to no finite Schatten class.

When \(n\equiv 1\) or \(-1\pmod m\), the entire path spectrum has the **closed form**

\[
\mu_k=\frac{k(k+1)}{m},\quad 0\le k<m;
\qquad
\|C_{p,q}\|=\max_{1\le k<m}
\sqrt{\frac{k(k+1)}{mn}\left(1-\frac{k(k+1)}{mn}\right)}.
\]

In particular, if also \(n\ge2(m-1)\), this gives the exact sharp norm

\[
\boxed{\|C_{p,q}\|=\frac{\sqrt{(m-1)(n-m+1)}}{n}.}
\]

For any fixed \(m\ge2\) and any reduced residue \(r\) modulo \(m\), the matrix \(L_{m,n}\) is constant along integers \(n\equiv r\pmod m\). If \(\mu_*(m,r)\) denotes its largest eigenvalue, then along that congruence class

\[
\lim_{n\to\infty,\ n\equiv r\ (\mathrm{mod}\ m)}
\sqrt n\,\|[E_m,E_n]\|=\sqrt{\mu_*(m,r)}.
\]

The coefficient equals \(\sqrt{m-1}\) for \(r=\pm1\).

## Assumptions and scope

The Hilbert space is complex \(\ell^2(\mathbb N_0)\), although all matrices and formulas admit real versions. Every block starts at index zero; a shifted partition is a different operator. The commutator convention is \([A,B]=AB-BA\). All integers are positive, and the reduction by the greatest common divisor is carried out before forming the modular path. The essential spectrum is Fredholm essential spectrum. Norms are Hilbert-space operator norms, not coordinate maximum norms.

## Proof

**1. Reduction and periodicity.** On identifying each group of \(g\) coordinates with \(\mathbb C^g\), write \(R_g\) for projection onto the normalized all-ones vector. Then \(E_{ga}=E_a\otimes R_g\) on \(\ell^2(\mathbb N_0)\otimes\mathbb C^g\). Hence \([E_p,E_q]\) is unitarily equivalent to \([E_m,E_n]\otimes R_g\). If \(m=1\), the reduced projections are nested and commute. If \(m,n\) are coprime, both are direct sums of the same finite pair of projections over consecutive cells of length \(mn\). Thus the full commutator is an orthogonal infinite direct sum of one finite skew-adjoint matrix; the spectrum is pure point, every spectral value has infinite multiplicity, and the essential norm equals the operator norm.

**2. Exact compression to a modular path.** On one length-\(mn\) cell, \(E_n\) has rank \(m\) and \(E_m\) has rank \(n\). For \(u\in\mathbb C^m\), define the isometric embedding \(Uu\) to be constant with value \(u_j/\sqrt n\) on the \(j\)-th \(n\)-block. The only \(m\)-blocks on which \(Uu\) is not constant are those crossed by the interior boundaries \(jn\), \(1\le j<m\). These boundaries lie in distinct \(m\)-blocks because \(n>m\); coprimality makes each crossing strict, with \(r_j\) coordinates to the left and \(m-r_j\) to the right. The elementary two-value variance identity

\[
\sum_{a=1}^{r}|v-\bar v|^2+\sum_{a=r+1}^{m}|w-\bar v|^2
=\frac{r(m-r)}m|v-w|^2
\]

implies, exactly and without an asymptotic remainder,

\[
U^*E_n(I-E_m)E_nU=U^*(I-E_m)U=\frac1nL_{m,n}.
\]

All path weights are positive, so the path Laplacian has a simple zero eigenvalue and \(m-1\) simple positive eigenvalues. To prove \(\mu_{m-1}<n\), suppose \(E_mUu=0\). The first \(m\)-block lies wholly inside the first \(n\)-block and forces \(u_0=0\). The \(m\)-block containing \(jn\), for increasing \(j\), has nonzero pieces from the adjacent \(n\)-blocks and forces \(u_j=0\) once \(u_{j-1}=0\). Thus \(U^*E_mU=I-L_{m,n}/n\) is positive definite. It follows that \(0<\eta_k<1\) for each \(k\ge1\).

**3. Two-projection spectral decomposition.** The squared principal cosines between \(\operatorname{ran}E_m\) and \(\operatorname{ran}E_n\) are the eigenvalues of \(U^*E_mU=I-L_{m,n}/n\). For each \(0<\eta_k<1\), the canonical two-dimensional block for the pair of projections has squared sine \(\eta_k\) and squared cosine \(1-\eta_k\). Its commutator is skew-adjoint with eigenvalues \(\pm i\sqrt{\eta_k(1-\eta_k)}\). The constant vector gives the sole common direction on the \(m\)-dimensional range of \(E_n\); all remaining directions give zero. This produces the stated complete spectrum, sharp norm, rank within a cell, and essential-spectrum conclusions.

**4. Exact congruence class.** If \(n\equiv\pm1\pmod m\), then \(r_j=j\) or \(m-j\) and the path edge weights become \(j(m-j)/m\). At vertex \(x\in\{0,\ldots,m-1\}\), its Jacobi operator is

\[
(Lf)(x)=\frac{x(m-x)}m\bigl(f(x)-f(x-1)\bigr)
+\frac{(x+1)(m-x-1)}m\bigl(f(x)-f(x+1)\bigr).
\]

The endpoint coefficients vanish, making this valid at both boundaries. Direct finite-difference expansion shows that it preserves polynomials of degree at most \(k\) and acts on the highest-degree term of a degree-\(k\) polynomial as multiplication by \(k(k+1)/m\). The evaluations of \(1,x,\ldots,x^{m-1}\) form a basis on the \(m\) vertices, so triangularization proves the full eigenvalue list \(k(k+1)/m\). When \(n\ge2(m-1)\), every \(\eta_k\le1/2\); the function \(\eta\mapsto\sqrt{\eta(1-\eta)}\) is increasing there, giving the closed norm formula. For fixed \(m\) and reduced residue \(r\), the path matrix is independent of \(n\); expanding \(\sqrt{\eta(1-\eta)}\) at \(\eta=0\) proves the stated congruence-class limit.

## Verification

The supplied `check.py` uses only NumPy to compare the modular-path compression against direct block-overlap Gram matrices and, independently, to diagonalize full finite commutators in representative parameter pairs. The checker completed 396 assertions, including the greatest-common-divisor reduction, the full congruence-class eigenvalues, and the sharp norm formula. Run `python check.py` in a directory with NumPy installed; `requirements.txt` records the numerical dependency. The code checks finite matrices only: the infinite direct-sum and essential-spectrum assertions follow from the proof above, not from any finite computation.

## Relationship to prior work

The 2021 preprint of Manzur, Noor, and Santos establishes the Hardy weighted-composition operators \(W_p\), their adjoint block-sum formula, and \(W_p^*W_p=pI\). The present operators \(E_p=p^{-1}W_pW_p^*\) therefore arise canonically from that family, but the spectral problem for commutators of two distinct range projections is different from the individual-shift and invariant-subspace questions treated there.

Classical two-projection geometry, surveyed and extended by Loring, supplies the general principal-angle-to-commutator relation; it does not supply the modular path compression or the arithmetic eigenvalues. Shabtai studies sharp commutator norms for spin spectral projections, again a different pair of projections. Work of Bailey, Cameron, Praeger, and Schneider on uniform partitions discusses compatibility of partitions, but does not determine these Hilbert-space commutator spectra. The specific substantive step here is the exact residue-weighted path reduction, including the full congruence-class diagonalization; general formulas for commutators of arbitrary projections alone do not yield its arithmetic values without that calculation.

## Limitations

The theorem fixes partitions at index zero and assumes unit weights within each consecutive integer block; arbitrary shifted or nonuniform partitions are not classified. The general case gives a finite explicit Jacobi matrix rather than radicals for every arithmetic residue. The sharp norm in fully closed elementary form is specified for the two reduced congruence classes and the stated scale range; outside them the exact finite eigenvalue maximum applies. Numerical tests are supplementary. The literature comparison is not a formal proof of historical priority: closely related published mathematical-record summaries were available, but their complete underlying public files could not all be inspected.

## References

1. J. Manzur, W. Noor, C. F. Santos, *A weighted composition semigroup related to three open problems*, arXiv:2111.05398, first posted 9 November 2021, https://arxiv.org/html/2111.05398v2.
2. T. A. Loring, *Principal angles and approximation for quaternionic projections*, arXiv:1306.1923, 2013, https://arxiv.org/abs/1306.1923.
3. O. Shabtai, *Commutators of spectral projections of spin operators*, arXiv:2008.00221, 2020, https://arxiv.org/abs/2008.00221.
4. R. A. Bailey, P. J. Cameron, C. E. Praeger, C. Schneider, *The geometry of diagonal groups*, 2020 preprint, https://api.newton.ac.uk/website/v0/events/preprints/NI19024 (Section 2 on uniform partitions).
