# Sharp finite-exchange sampling spectra and block-instability laws for discrete Hardy boundary data

## Finding

Let \(H^2\) be the discrete-holomorphic Hardy space on the square upper half-lattice with the canonical boundary norm \(\|f\|_{H^2}^2=\sum_{n\in\mathbb Z}|f(n)|^2\), as defined in [1]. For finite sets \(J,L\subset\mathbb Z\), define the boundary sampling set
\[
\Lambda_{J,L}=\{2j:j\in\mathbb Z\setminus J\}\,\cup\,\{2k+1:k\in L\}.
\]
Write \(m=|J|\), \(\ell=|L|\). The system samples \(H^2\), meaning there are \(0<A\le B<\infty\) such that
\[
A\|f\|_{H^2}^2\le\sum_{n\in\Lambda_{J,L}}|f(n)|^2\le B\|f\|_{H^2}^2\quad(f\in H^2),
\]
**if and only if** \(\ell\ge m\). If \(\ell<m\), the nullspace of the sampling map has dimension exactly \(m-\ell\).

For \(m\ge1\) and \(\ell\ge m\), enumerate \(J=\{j_1,\ldots,j_m\}\), \(L=\{k_1,\ldots,k_\ell\}\) and put
\[
C_{rs}=\frac{2i}{\pi(2(k_r-j_s)+1)},\qquad\sigma_* =\sigma_{\min}(C)>0.
\]
The **optimal** squared-norm sampling bounds are
\[
\boxed{A_{J,L}=\frac{1-\sqrt{1-\sigma_*^2}}2,\qquad
B_{J,L}=\begin{cases}\frac{1+\sqrt{1-\sigma_*^2}}2,&\ell=m,\\1,&\ell>m.\end{cases}}
\]
For \(m=0\), the optimal lower bound is \(1/2\), and the optimal upper bound is \(1/2\) if \(\ell=0\) and \(1\) otherwise.

More precisely, when \(\ell\ge m\ge1\), if \(\sigma_1,\ldots,\sigma_m\) are all singular values of \(C\), the sample-frame operator has nontrivial eigenvalues
\[
\frac{1\pm\sqrt{1-\sigma_j^2}}2\quad(1\le j\le m),
\]
plus eigenvalue \(1\) of multiplicity \(\ell-m\) when \(\ell>m\), and essential spectral value \(1/2\). For \(\ell<m\) there are exactly \(m-\ell\) zero eigenvalues.

For the **contiguous distant-block exchange**
\[
J=\{0,1,\ldots,m-1\},\qquad L=\{N,N+1,\ldots,N+m-1\},
\]
with fixed \(m\ge1\) and positive integer \(N\to\infty\), define
\[
S_m=\sum_{j=0}^{m-1}\frac1{j!^2(m-1-j)!^2}
=\frac{\binom{2m-2}{m-1}}{((m-1)!)^2}.
\]
Then the least singular value and sharp lower frame bound have the exact asymptotics
\[
\boxed{\sigma_*(N)\sim\frac{N^{-(2m-1)}}{\pi S_m},\qquad
A_{J,L}\sim\frac{N^{-(4m-2)}}{4\pi^2 S_m^2}.}
\]
Thus a fixed-size replacement always preserves sampling, but the deterioration exponent grows linearly with the number of consecutive deleted sites.

## Assumptions and scope

The Hilbert norm is **exactly** the unweighted \(\ell^2(\mathbb Z)\) norm of the complete boundary trace. All node sets are finite, with no repeated indices. Upper/lower frame bounds refer to the **unscaled** physical sample sum and are squared-norm bounds. The Hardy model's parity-sampling and boundary relation are taken from [1, Proposition 7.2 and equation (52)] and checked against relevant sections of its full public manuscript. No claim is made about interior horizontal lines or \(H^p\) for \(p\ne2\).

## Proof

**Step 1 (unitary boundary coordinates).** Proposition 7.2 of [1] gives
\[
\sum_{j\in\mathbb Z}|f(2j)|^2=\sum_{k\in\mathbb Z}|f(2k+1)|^2=\frac12\|f\|_{H^2}^2.
\]
The Paley--Wiener characterization in [1] identifies \(H^2\) with \(L^2(0,\pi)\); the even exponentials form an orthonormal basis, as do the odd exponentials. Hence \(x_j=\sqrt2f(2j)\) ranges over all of \(\ell^2(\mathbb Z)\), isometrically. The odd coordinates \(y_k=\sqrt2 f(2k+1)\) satisfy \(y=Ux\), where the matrix of the unitary change of bases is [1, equation (52)]
\[
U_{kj}=\frac{2i}{\pi(2(k-j)+1)}.
\]
The matrix can also be obtained by integrating a half-integer Fourier frequency against the even basis on \((0,\pi)\). Thus the sample operator, transported to \(\ell^2(\mathbb Z)\), is
\[
\mathcal T_{J,L}=\frac12\bigl(I-P_J+U^*P_LU\bigr),
\]
with \(P_J,P_L\) the coordinate projections. Every statement below concerns this exact operator, not a finite-section surrogate.

**Step 2 (rank and strict principal angles).** The finite compression \(C=P_LU|_{\operatorname{ran}P_J}\) has the displayed Cauchy entries. Every square minor of maximal possible size is nonzero, since distinct half-integer-shifted nodes give the Cauchy determinant
\[
\bigl|\det C_{K,J}\bigr|=\pi^{-m}\frac{\prod_{r<s}|k_s-k_r|\prod_{r<s}|j_s-j_r|}
{\prod_{r,s}|k_r-j_s+\tfrac12|}\quad(\ell=m).
\]
Thus \(\operatorname{rank}C=\min(m,\ell)\). Moreover each singular value is strictly less than one whenever \(m,\ell\) are positive: if a nonzero finitely supported \(x\) in \(J\) had \(\|P_LUx\|=\|x\|\), the sequence \((Ux)_k=\frac{i}{\pi}\sum_{j\in J}x_j/(k-j+1/2)\) would vanish at all but finitely many integers. Its rational function in \(k\) would then be identically zero, forcing all residues \(x_j\) to vanish, a contradiction.

**Step 3 (two-projection spectrum).** Write \(P=P_J\), \(Q=U^*P_LU\). The principal-angle decomposition of two finite-rank orthogonal projections gives a two-dimensional reducing block for each positive singular value \(\sigma_j\) of \(PQ\). In a suitable orthonormal basis,
\[
P=\begin{pmatrix}1&0\\0&0\end{pmatrix},\qquad
Q=\begin{pmatrix}\sigma_j^2&\sigma_j\sqrt{1-\sigma_j^2}\\
\sigma_j\sqrt{1-\sigma_j^2}&1-\sigma_j^2\end{pmatrix}.
\]
Therefore \(I-P+Q\) has eigenvalues \(1\pm\sqrt{1-\sigma_j^2}\). If \(\ell>m\), the \(\ell-m\) excess directions in \(\operatorname{ran}Q\cap\ker P\) give eigenvalue \(2\); if \(\ell<m\), the \(m-\ell\) unmatched directions in \(\operatorname{ran}P\cap\ker Q\) give eigenvalue \(0\). On the infinite-dimensional orthogonal complement of both ranges the eigenvalue is \(1\). Divide by two to recover the frame-operator spectrum and take its minimum and maximum. This proves the classification, multiplicities, and **optimal** constants.

**Step 4 (block asymptotics).** For the distant consecutive blocks, let \(B_N\) be the real \(m\)-by-\(m\) matrix
\[
(B_N)_{rs}=\frac1{N+r-s+\tfrac12}\quad(0\le r,s<m),\qquad C_N=\frac{i}{\pi}B_N.
\]
Cauchy interpolation gives its **exact inverse**, with row index \(s\), column index \(r\):
\[
(B_N^{-1})_{sr}=
\frac{\displaystyle\prod_{h=0}^{m-1}(N+r+\tfrac12-h)
\displaystyle\prod_{h\ne r}(s-N-h-\tfrac12)}
{\displaystyle\prod_{h\ne r}(r-h)
\displaystyle\prod_{h\ne s}(s-h)}.
\]
For fixed \(m\), dividing entrywise by \(N^{2m-1}\) yields the rank-one matrix with entries
\[
(-1)^{m-1+r+s}\,
\frac1{r!(m-1-r)!s!(m-1-s)!}.
\]
Its sole nonzero singular value is \(S_m\). Since all norms are equivalent in fixed dimension,
\[
\|B_N^{-1}\|\sim S_m N^{2m-1},\qquad
\sigma_{\min}(C_N)=\frac1{\pi\|B_N^{-1}\|}
\sim\frac{N^{-(2m-1)}}{\pi S_m}.
\]
Finally \((1-\sqrt{1-u^2})/2\sim u^2/4\) as \(u\downarrow0\), proving the asserted sharp decay exponent and coefficient. The combinatorial expression for \(S_m\) is Vandermonde's identity.

## Verification

`CHECK.py` reproduces Cauchy determinants and inverses by exact rational arithmetic, checks the projection spectral formula on finite-dimensional model blocks, and computes convergence of the normalized smallest singular values using arbitrary precision. None of these finite checks substitutes for Steps 1--4, which prove the infinite-dimensional assertions.

## Relationship to prior work

[1] supplies the discrete Hardy norm, parity sampling identities, and parity-boundary Hilbert transform. It does **not** give the sharp spectrum for arbitrary finite exchanged parity sites or the distant-block instability exponent. [2] concerns a different discrete entire-function Paley--Wiener space and qualitative sampling questions. Classical finite perturbations of exponential Riesz bases and the two-projection principal-angle principle underlie the method; neither alone states the exact constants for this discrete Hardy model. The Cauchy determinant is classical; its use here is not claimed as an independent new identity.

## Limitations

The work is restricted to finitely many removed and added **boundary** nodes, and only the fixed-block-size distant-shift limit is quantified. For other configurations, the singular-value formula is exact but not necessarily reducible to elementary radicals. Existing classical nonharmonic Fourier-series theory may contain equivalent specializations under different nomenclature; no independent publication-priority review has been performed.

## References

[1] E. Dellepiane, A. Monguzzi, M. Monti, *Hardy spaces of discrete holomorphic functions on the upper half-lattice*, arXiv:2607.17726, initially public 2026-07-20; Sections 4 and 7, particularly equation (52), Proposition 7.2.

[2] A. Monguzzi and M. Monti, *On discrete holomorphic Paley--Wiener spaces and sampling on the square lattice*, arXiv:2501.18390, initially public 2025-01-30; Section 4.

[3] R. M. Young, *An Introduction to Nonharmonic Fourier Series*, Academic Press, 1980 (background on exponential Riesz bases and finite perturbations).
