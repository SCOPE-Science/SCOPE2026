# Sharp fixed-spectrum trace dilation of the near-geometric endpoint for two-level positive matrices

## Finding

For positive-definite complex matrices \(A,B\in M_n(\mathbb C)\), put \(S=B^{1/2}\) and define the near-geometric endpoint
\[
C(A,B):=A\star_1 B=A^{1/2}SA^{-1}SA^{1/2}.
\]
The exact **trace dilation identity** in every finite dimension is
\[
\operatorname{tr}C(A,B)-\operatorname{tr}B
=\frac12\|A^{-1/2}[A,S]A^{-1/2}\|_{\mathrm F}^{2}
=\sum_{i<j}\frac{(a_i-a_j)^2}{a_i a_j}|S_{ij}|^2,\tag{1}
\]
where the latter expression uses any orthonormal eigenbasis of \(A\), with eigenvalues \(a_i>0\). Thus equality of traces occurs exactly when \(A\) and \(B\) commute.

More strongly, suppose \(n\ge2\), \(1\le k<n\), and
\[
A=aP+b(I-P),\qquad a>b>0,\quad \operatorname{rank}P=k.
\]
Fix positive numbers \(\beta_1\ge\dots\ge\beta_n>0\), let \(B_0\) be any positive-definite matrix with this spectrum, and put \(r=\min\{k,n-k\}\). As \(U\) ranges over every unitary \(n\times n\) matrix, the trace excess
\[
\Delta(U):=\operatorname{tr}C(A,UB_0U^*)-\operatorname{tr}B_0
\]
attains **every** value in the sharp closed interval
\[
\boxed{\displaystyle
\Delta(U)\in\left[0,\ \frac{(a-b)^2}{4ab}\sum_{j=1}^{r}
\bigl(\sqrt{\beta_j}-\sqrt{\beta_{n-j+1}}\bigr)^2\right].}\tag{2}
\]
An upper-endpoint extremizer is obtained by coupling the \(j\)-th largest and \(j\)-th smallest eigenvalues of \(B_0^{1/2}\) across the \(P\)/(\(I-P\)) split using a balanced \(45^\circ\) two-dimensional rotation for every \(1\le j\le r\), and placing all remaining middle eigenvalues in uncoupled coordinates. The lower endpoint occurs precisely at the commuting inputs. The upper endpoint formula also holds for repeated eigenvalues (when a family of maximizers may exist).

In dimension two, with the eigenvalues of \(A\) equal to \(a>b\), those of \(B\) equal to \(c>d\), and eigenbasis transition probability \(q\in[0,1]\), the entire law is
\[
\boxed{\displaystyle
\operatorname{tr}C-\operatorname{tr}B
=\frac{(a-b)^2}{ab}(\sqrt c-\sqrt d)^2q(1-q)
=\frac{\|[A,B]\|_{\mathrm F}^2}{2\det A\,(\operatorname{tr}B+2\sqrt{\det B})}.}\tag{3}
\]
The maximum occurs exactly at \(q=1/2\), i.e. mutually unbiased eigenbases, and the minimum at \(q\in\{0,1\}\). Since \(\det C=\det B\), the two eigenvalues of \(C\) in this case are exactly
\[
\frac{\tau\pm\sqrt{\tau^2-4\det B}}2,
\qquad \tau=\operatorname{tr}B+\Delta(U).\tag{4}
\]
Thus (3) also gives the exact attainable increase in the larger eigenvalue and the spectral condition number of this endpoint on the fixed-spectrum unitary orbit. In the degenerate-spectrum case the trace excess is identically zero.

## Assumptions and scope

Matrices are complex Hermitian positive definite; \(\|\cdot\|_{\mathrm F}\) is the Frobenius norm and \([A,S]=AS-SA\). The endpoint convention is the near-geometric mean \(A\star_1B=A^{1/2}B^{1/2}A^{-1}B^{1/2}A^{1/2}\), **not** the near-spectral curve's matrix endpoint. The sharp orbit result assumes exactly two distinct spectral values for the first factor, with multiplicities \(k,n-k\). It fixes the complete spectrum of the second factor and varies only its eigenvectors.

## Proof

**Trace identity.** Set \(X=A^{1/2}SA^{-1/2}\). Then \(XX^*=C(A,B)\), \(X^2=A^{1/2}BA^{-1/2}\), and \(\operatorname{tr}X^2=\operatorname{tr}B\). Consequently
\[
\begin{aligned}
\operatorname{tr}C-\operatorname{tr}B
&=\operatorname{tr}XX^*-\operatorname{Re}\operatorname{tr}X^2\\
&=\tfrac12\|X-X^*\|_{\mathrm F}^2
=\tfrac12\|A^{-1/2}[A,S]A^{-1/2}\|_{\mathrm F}^2.
\end{aligned}
\]
In an eigenbasis of \(A\), pairing the \((i,j)\) and \((j,i)\) contributions yields (1). Each coefficient is nonnegative, and the gap is zero iff \([A,S]=0\), equivalently \([A,B]=0\), because the positive square root commutes with exactly the matrices commuting with \(B\).

**Reduction to off-diagonal energy.** With \(Q=I-P\), block multiplication and (1) give
\[
\Delta=\frac{(a-b)^2}{ab}\|PSQ\|_{\mathrm F}^2.\tag{5}
\]
Here \(S\) is any positive definite Hermitian matrix with eigenvalues \(s_j=\sqrt{\beta_j}\), in decreasing order, and changing \(B\) by unitary conjugation ranges over all such \(S\).

**Sharp upper bound.** Set \(J=P-Q\), a self-adjoint unitary. In the orthogonal splitting \(\operatorname{ran}P\oplus\operatorname{ran}Q\),
\[
S-JSJ=2\begin{pmatrix}0&PSQ\\QSP&0\end{pmatrix}.
\]
Let \(t_1\ge\dots\ge t_r\ge0\) be the singular values of \(PSQ\). The positive eigenvalues of \(S-JSJ\) are \(2t_1,\dots,2t_r\), completed by zeros when necessary. Ky Fan's eigenvalue inequality for the difference of \(S\) and its unitarily conjugate \(JSJ\) gives, for every \(1\le m\le r\),
\[
2\sum_{j=1}^{m}t_j
\le\sum_{j=1}^{m}(s_j-s_{n-j+1}).\tag{6}
\]
Thus the vector \((2t_j)_{j=1}^r\) is weakly majorized by the nonnegative decreasing vector \((s_j-s_{n-j+1})_{j=1}^r\). Since the square function is increasing and convex on the nonnegative half-line, weak majorization implies
\[
4\sum_{j=1}^{r}t_j^2\le\sum_{j=1}^{r}(s_j-s_{n-j+1})^2.\tag{7}
\]
Equations (5) and (7) give the asserted maximum upper bound. This off-diagonal-block inequality is also a special case of the spectral-spread majorization proved by Li and Mathias (1999), Theorem 2; its mathematical precedence is explicitly acknowledged.

**Attainment.** Choose orthonormal vectors \(p_j\in\operatorname{ran}P\) and \(q_j\in\operatorname{ran}Q\) for \(1\le j\le r\), with the pairs mutually orthogonal. On each plane spanned by \(p_j,q_j\), give \(S\) the \(2\times2\) matrix
\[
\begin{pmatrix}(s_j+s_{n-j+1})/2&(s_j-s_{n-j+1})/2\\
(s_j-s_{n-j+1})/2&(s_j+s_{n-j+1})/2\end{pmatrix}.
\]
This has eigenvalues \(s_j,s_{n-j+1}\) and off-diagonal entry \((s_j-s_{n-j+1})/2\). Assign the remaining middle eigenvalues to the remaining \(|n-2k|\) coordinates. The resulting \(S\) has the prescribed spectrum and attains equality in (7). Choosing \(S\) diagonal gives the zero minimum; (1) shows that zero is possible only at commuting pairs. The unitary group \(U(n)\) is path-connected, and \(\Delta(U)\) is continuous, so its image includes every intermediate value. This proves (2).

**Dimension-two refinement.** Write \(q=|\langle u_a,u_c\rangle|^2\), the squared overlap between the eigenvector for \(a\) and that for \(c\). Diagonalizing \(B\) gives \(|S_{12}|^2=(\sqrt c-\sqrt d)^2q(1-q)\). Substitution into (1) gives the first equality of (3) and identifies all extremizing overlap magnitudes for nondegenerate spectra. For positive \(2\times2\) matrices, Cayley–Hamilton gives
\[
B^{1/2}=\frac{B+\sqrt{\det B}\,I}{\sqrt{\operatorname{tr}B+2\sqrt{\det B}}}.
\]
Hence \([A,S]=[A,B]/\sqrt{\operatorname{tr}B+2\sqrt{\det B}}\). Evaluating (1) on two eigenvalues of \(A\) produces the second equality in (3). Finally, determinant multiplicativity gives \(\det C=\det B\) and the quadratic formula proves (4).

## Verification

The self-contained `verify.py` uses only the Python standard library and exact rational arithmetic; run `python3 verify.py`. It tests (1) on symmetric positive definite matrices with nontrivial mixing in dimensions \(2\) through \(8\), verifies exact equality of the bound with the explicit matched-pair construction for dimensions \(2\) through \(10\) and every admissible rank, and checks (3) and its sharp upper bound on rationally parametrized planar rotations. The script reports 2,950 exact identities and bound comparisons. These are finite checks; the universal statements follow from the preceding proof and the standard Ky Fan majorization step.

## Relationship to prior work

Franco–Gan–Kim (2025) introduced the near-geometric mean. Ibrahim–Huang (arXiv:2610.23736v1, first public 2026-10-16) records the endpoint \(A\star_1B\) in (2.5), proves order and log-majorization results for near-geometric and near-spectral curves, and treats an explicit \(2\times2\) determinant-one near-spectral expression in Proposition 4.13. In particular, its Theorem 4.3 establishes \(B\prec_{\log}A^{-1}\star_1B\). The two endpoints \(A\star_1B\) and \(A^{-1}\star_1B\) are respectively \(XX^*\) and \(X^*X\), and therefore isospectral; this yields the *known qualitative* log-majorization \(B\prec_{\log}C(A,B)\), not claimed new here. The present claim is the exact quantitative trace identity and the sharp two-level fixed-spectrum orbit interval for that endpoint. Neither the qualitative log-majorization nor a pointwise matrix formula gives an explicit sharp orbit extremum without the additional spectral-spread argument.

Li–Mathias (1999), Theorem 2, already proves the spectral-spread majorization for off-diagonal blocks of Hermitian matrices, including sharpness of the block bound; (6)–(7) are not claimed as new. The new conclusion identifies this **known sharp block energy** as the exact maximal trace dilation of the near-geometric endpoint for two-level first factors. The proof synthesizes the endpoint trace-defect identity with that majorization. The scope is not a new general inequality for off-diagonal blocks.

## Limitations

The fixed-spectrum optimum (2) is established only when \(A\) has two distinct eigenvalues. The general-dimensional identity (1) does not by itself solve the analogous optimization for \(A\) with three or more distinct eigenvalues. The claim is finite-dimensional; no infinite-dimensional trace hypothesis is asserted. No uniqueness of all upper-endpoint maximizing matrices is claimed when spectral multiplicities exist, and no novel spectral-spread inequality is claimed. The complete text of Franco–Gan–Kim (2025) could not be checked through accessible channels; an equivalent trace identity or application in that paper or other unindexed work is a residual priority risk. The result is not an independent external certification.

## References

1. M. Ibrahim and H. Huang, *Order Relations for the Near Geometric and Near Spectral Geometric Curves*, arXiv:2610.23736v1, 2026-10-16, https://arxiv.org/html/2610.23736v1; notably §§2.5, 3, Theorem 4.3 and Proposition 4.13. Primary MSC2020: 47A64.
2. J. A. Franco, L. Gan and S. Kim, *Near-geometric mean of positive definite operators*, Positivity **29** (2025), article 54, DOI:10.1007/s11117-025-01147-7.
3. C.-K. Li and R. Mathias, *Inequalities on the singular values of an off-diagonal block of a Hermitian matrix*, Journal of Inequalities and Applications **3** (1999), 137–142, DOI:10.1155/S1025583499000090; especially Theorem 2 and the sharpness construction.
4. R. A. Horn and C. R. Johnson, *Matrix Analysis*, 2nd ed., Cambridge University Press, 2013; Ky Fan's eigenvalue inequality and majorization basics.
