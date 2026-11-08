# Universal singular spectrum for bilinearly coupled affine finite-field incidence

## Finding
Let \(q\ge3\) be an odd prime power and \(F=\mathbb F_q\). Let \(\alpha,\gamma,\lambda\in F^\times\), \(\beta,\delta\in F\), and let \(J:F\to F\) be any function. Define the \(q^2\)-by-\(q^2\) zero-one incidence matrix \(M\), with rows \((x,t)\in F^2\) and columns \((a,b)\in F^2\), by
\[
 M_{(x,t),(a,b)}=\mathbf1_{\{t=J(x)+a(\alpha x+\beta)+b(\gamma x+\delta)+\lambda ab\}}.
\]
All matrix norms are the ordinary unnormalized counting-measure \(\ell^2\) norms. Write
\[
\Lambda_\pm=\frac{q^2+2q\pm\sqrt{q^4-4q^2+4q}}2.
\]
Then the complete spectrum of \(M^*M\), with multiplicities, is

| Eigenvalue | Multiplicity |
| --- | ---: |
| \(0\) | \(q(q-1)/2\) |
| \(q-\sqrt q\) | \(q-1\) |
| \(q+\sqrt q\) | \(q-1\) |
| \(2q\) | \(q(q-3)/2\) |
| \(\Lambda_-\) | \(1\) |
| \(\Lambda_+\) | \(1\) |

The \(2q\) sector is absent when \(q=3\). Thus \(\operatorname{rank}M=q(q+1)/2\), and the exact positive singular-value range is
\[
\sigma_{\min}^+(M)=\sqrt{q-\sqrt q},\qquad
\sigma_{\max}(M)=\sqrt{\Lambda_+},\qquad
\kappa\bigl(M|_{(\ker M)^\perp}\bigr)=\sqrt{\frac{\Lambda_+}{q-\sqrt q}}.
\]
These quantities are independent of all affine coefficients and of \(J\). In particular, after quotienting the unavoidable two-to-one parameter symmetry, all parameter weights are exactly identifiable, with the stated sharp spectral stability.

## Assumptions and scope
The field has odd characteristic, including nonprime extension fields; \(\alpha\), \(\gamma\), and \(\lambda\) must be nonzero. Distinct ordered parameter pairs are retained as distinct columns, even if they produce identical curves. The output grid is all \(F^2\) and includes all \(q^2\) parameter pairs. The coefficient function \(J\) need not be polynomial. No random sampling, asymptotic limit, or Fourier-transform normalization is involved.

## Proof
**1. Reduction to a universal model.** Put
\[
A=\alpha a,\quad B=\gamma b,\quad
\zeta=\lambda/(\alpha\gamma),\quad d=\beta/\alpha,\quad e=\delta/\gamma.
\]
The incidence condition becomes
\[
t-J(x)=x(A+B)+\zeta AB+dA+eB.
\]
The parameter changes \(u=\zeta A+e\) and \(v=\zeta B+d\) are bijections of \(F^2\). The row change
\[
t'=\zeta(t-J(x))+x(d+e)+de
\]
is a bijection on \(F^2\), since \(\zeta\ne0\). Direct expansion gives
\[
t'=x(u+v)+uv.
\]
Hence all matrices in the theorem are obtained by row and column permutations from the canonical matrix
\[
M^0_{(x,t),(u,v)}=\mathbf1_{\{t=x(u+v)+uv\}}.
\]
Their singular spectra coincide, and the kernels are carried to each other by these permutations.

**2. Geometry of the columns and the exact kernel.** The columns of \(M^0\) are the indicators of the affine nonvertical lines
\[
L_{u,v}=\{(x,t):t=(u+v)x+uv\}.
\]
Since \(\operatorname{char}F\ne2\), the unordered root pair \(\{u,v\}\) is determined uniquely by its slope \(s=u+v\) and intercept \(c=uv\). These two parameters satisfy \(s^2-4c=(u-v)^2\). For every slope \(s\in F\), there are \((q+1)/2\) such intercepts: one with discriminant zero, appearing in the ordered columns once, and \((q-1)/2\) with nonzero square discriminant, each appearing twice. Distinct nonvertical lines with the same slope are disjoint; lines of different slopes meet in exactly one point.

Write \(r=(q+1)/2\) and \(m_0=1\), \(m_i=2\) for \(1\le i<r\). The canonical incidence matrix has one repeated column for each pair \(u\ne v\). Its kernel therefore contains the \(q(q-1)/2\)-dimensional antisymmetric subspace \(f(u,v)=-f(v,u)\). Its orthogonal complement has a basis consisting of the unit orbit sums, on which the compressed columns are \(\sqrt{m_i}\,\mathbf1_{L_{s,i}}\).

**3. Gram block diagonalization.** Set \(D=\operatorname{diag}(1,2,\ldots,2)\) and \(w=(1,\sqrt2,\ldots,\sqrt2)^{\mathsf T}\in\mathbb R^r\). By the line-intersection count, the compressed Gram matrix is exactly
\[
G=I_q\otimes(qD-ww^{\mathsf T})+\mathbf1_q\mathbf1_q^{\mathsf T}\otimes ww^{\mathsf T}.
\]
Fourier characters of the additive slope group \((F,+)\) diagonalize the all-ones factor: the trivial character has eigenvalue \(q\), and the \(q-1\) nontrivial characters have eigenvalue zero. The slope-constant subspace thus yields \(B_+=qD+(q-1)ww^{\mathsf T}\), once; its orthogonal slope-complement yields \(B_-=qD-ww^{\mathsf T}\), with multiplicity \(q-1\). On the \((r-2)\)-dimensional subspace of vectors supported on the last \(r-1\) coordinates and summing to zero, each block acts as \(2qI\).

On the remaining two-dimensional subspace, use \(e_0\) and the normalized sum of the last \(r-1\) coordinate vectors. Since \(2(r-1)=q-1\), the two blocks are
\[
 B_-^{(2)}=\begin{pmatrix}q-1&-\sqrt{q-1}\\-\sqrt{q-1}&q+1\end{pmatrix},\qquad
 B_+^{(2)}=\begin{pmatrix}2q-1&(q-1)\sqrt{q-1}\\(q-1)\sqrt{q-1}&q^2+1\end{pmatrix}.
\]
The first has characteristic polynomial \(z^2-2qz+q(q-1)\), with roots \(q\pm\sqrt q\). The second has characteristic polynomial
\[
z^2-q(q+2)z+q(q^2+2q-1),
\]
with roots \(\Lambda_\pm\). The zero sector is the antisymmetric kernel already exhibited. All positive roots are strictly positive, proving that this is the entire kernel. The dimensions add to
\[
\frac{q(q-1)}2+2(q-1)+\frac{q(q-3)}2+2=q^2.
\]

**4. Sharp stability bounds.** Since \(B_+=B_-+qww^{\mathsf T}\), the least eigenvalue of \(B_+\) cannot lie below \(q-\sqrt q\), the least eigenvalue of \(B_-\). The eigenvalues \(2q\) and \(q+\sqrt q\) are also larger than \(q-\sqrt q\). Thus the least positive Gram eigenvalue is \(q-\sqrt q\). On the other hand, the top eigenvalue \(\Lambda_+\) of \(B_+\) is at least its lower-right diagonal entry \(q^2+1>2q\), and it dominates all the remaining eigenvalues. These two extrema yield the sharp condition number. Singular-value decomposition then gives exact reconstruction of every input orthogonal to the antisymmetric kernel, with optimal inverse norm \((q-\sqrt q)^{-1/2}\).

## Verification
Execute \(\texttt{python3 CHECK.py}\) using only the Python standard library. The program directly constructs the canonical zero-one matrix over fields of orders \(3,5,7,9\), including the genuine quadratic extension \(\mathbb F_9\). It independently counts all pairwise column intersections, checks an exact integer annihilating polynomial of the full Gram matrix, and matches trace power sums for powers zero through five to the predicted spectral multiplicities. It also directly verifies the affine row/column normalization with nontrivial offsets and coupling. On execution the program prints \(\texttt{CHECK_OK}\) with the exact assertion count. This is finite corroboration of the displayed all-field proof, not an attempt to infer infinite-field coverage from experiments.

## Relationship to prior work
Vinh's point-line incidence theorem supplies the classical affine-plane spectral context. Murphy and Petridis obtain an incidence second-moment identity for the full point-line design, which does not distinguish this constrained discriminant-square line selection. Kong and Tamo analyze singular spectra of an unrestricted point-variety family, not the bilinearly constrained two-parameter columns here. Zhi (2026) studies the exact parameterized incidence model with general nonconstant \(F,G\) and nonzero bilinear coupling and proves uniform discrepancy estimates; the published low-degree discussion includes constant-symbol estimates and a reduction to point-line incidence but does not state the full exact singular spectrum, its multiplicities, the precise kernel, or this coefficient-universality theorem. The new assertion is the **complete** six-sector spectral resolution for the entire affine coefficient family; the elementary affine-line intersection rules themselves are classical.

## Limitations
The result concerns the full unweighted parameterized incidence operator in odd characteristic, not arbitrary subsets of input parameters or output points. It requires both coefficient functions to have nonzero affine slopes and the bilinear coupling to be nonzero; different nonlinear coefficient curves may have different spectra. The singular-value bounds hold on the identifiable quotient, not on the full space where antisymmetric inputs are invisible. This is an exact linear inverse/spectral theorem, not a claim about nonlinear phase retrieval. Prior literature may contain an equivalent weighted-line formulation under a different terminology; no independent audit has been performed.

## References
1. Y. Zhi, *Spectral Incidence Bounds for Bilinearly Coupled Polynomial Families over Finite Fields*, arXiv:2610.03819, first submitted 2026-10-02. https://arxiv.org/abs/2610.03819 .
2. L. A. Vinh, *The Szemerédi–Trotter type theorem and the sum-product estimate in finite fields*, European Journal of Combinatorics 32 (2011), 1177–1181; arXiv:0711.4427. https://arxiv.org/abs/0711.4427 .
3. X. Kong and I. Tamo, *A point-variety incidence theorem over finite fields, and its applications*, arXiv:2408.10977 (2024; updated 2025). https://arxiv.org/html/2408.10977v2 .
4. B. Murphy and G. Petridis, *A point-line incidence identity in finite fields, and applications*, arXiv:1601.03981 (2016). https://arxiv.org/html/1601.03981v3 .
