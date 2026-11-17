# Sharpness at every rank of the nearly invariant defect bound for truncated Toeplitz perturbations

## Finding
For every integer \(r\geq1\), there is a model space for a monomial inner function, a truncated Toeplitz operator with a monomial analytic symbol, and an **exactly rank-\(r\)** perturbation whose kernel has minimal nearly backward-shift-invariance defect **exactly \(2r+1\)**. Thus the universal \(2r+1\) upper bound of Chattopadhyay–Khan, Theorem 5.4 [1], cannot be reduced for any positive rank, even within finite-dimensional polynomial model spaces.

More explicitly, set
\[
N=8r+8,\qquad k=3r+3,\qquad h=N-k=5r+5,
\]
and work in \(\mathcal K_{z^N}=H^2\ominus z^NH^2\), with orthonormal monomials \(e_j=z^j\), \(0\leq j<N\). For \(1\leq i\leq r\), put
\[
a_i=3i+1,\qquad b_i=h+2i.
\]
Define the perturbation
\[
T_r=A_{z^k}^{z^N}-\sum_{i=1}^r(e_{k+a_i}\otimes e_{b_i}),
\qquad (u\otimes v)f=\langle f,v\rangle u.
\]
The perturbation has rank exactly \(r\), and
\[
\dim\frac{\ker T_r+S^*(\ker T_r)}{\ker T_r}=2r+1,
\]
where \(S^*f=(f-f(0))/z\) is the Hardy backward shift. Here the quotient is well-defined because the denominator is a subspace of the numerator. Since all members of \(\ker T_r\) vanish at the origin, this quotient dimension is the minimal possible defect.

## Assumptions and scope
The scalar Hilbert space is the complex Hardy space \(H^2(\mathbb D)\) with normalized monomial basis. The inner function is \(z^N\), and the truncated Toeplitz operator is the compression of multiplication by \(z^k\) to \(\mathcal K_{z^N}\). Rank means complex linear rank. A closed subspace \(M\subset H^2\) has *nearly \(S^*\)-invariance defect* at most \(d\) when there is a \(d\)-dimensional space \(F\) such that \(S^*f\in M+F\) for all \(f\in M\) with \(f(0)=0\). The *minimal defect* is the smallest such \(d\). The assertion holds for **each** integer \(r\ge1\); it is not an asymptotic statement or a computational extrapolation.

## Proof
**1. Factorization and rank.** Let \(S\) be the compressed forward shift on \(\mathcal K_{z^N}\), so \(A_{z^k}^{z^N}=S^k\) and \(\ker S^k=L:=\operatorname{span}\{e_h,\ldots,e_{N-1}\}\). Put
\[
U=\sum_{i=1}^r(e_{a_i}\otimes e_{b_i}).
\]
All \(a_i\) are strictly between \(0\) and \(h\); all \(b_i\) belong to \([h,N-2]\), and both index lists are pairwise distinct. Consequently \(U^2=0\), \(S^kU=\sum_i(e_{k+a_i}\otimes e_{b_i})\), and
\[
T_r=S^k(I-U),\qquad (I-U)^{-1}=I+U.
\]
The vectors \(e_{b_i}\) are orthonormal and the vectors \(e_{k+a_i}\) are distinct orthonormal monomials, so the perturbation has rank \(r\). Also
\[
M_r:=\ker T_r=(I+U)L.
\]
In particular \(M_r\) has the explicit basis
\[
\{e_j:h\le j<N,\ j\notin\{b_1,\ldots,b_r\}\}
\cup\{e_{b_i}+e_{a_i}:1\le i\le r\}.
\]
Every basis vector has zero constant coefficient, hence \(M_r\subset zH^2\).

**2. A complete quotient coordinate map.** Define the surjective linear map \(J:\mathcal K_{z^N}\to\operatorname{span}\{e_0,\ldots,e_{h-1}\}\) by
\[
Jx=\sum_{j=0}^{h-1}\langle x,e_j\rangle e_j
-\sum_{i=1}^r\langle x,e_{b_i}\rangle e_{a_i}.
\]
It is surjective because it is the identity on low-degree monomials. By the displayed basis, \(J\) vanishes on \(M_r\). Moreover \(\dim\ker J=N-h=k=\dim M_r\), so \(\ker J=M_r\). Therefore \(J\) identifies the quotient \(\mathcal K_{z^N}/M_r\) with the low-degree monomial space.

**3. Exact defect.** Apply \(JS^*\) to the displayed basis of \(M_r\). The only nonzero classes are
\[
JS^*e_h=e_{h-1},\quad
JS^*e_{b_i+1}=-e_{a_i},\quad
JS^*(e_{b_i}+e_{a_i})=e_{a_i-1}.
\]
Here each \(e_{b_i+1}\) is an allowed unperturbed basis vector, since \(b_i+1<N\) and no \(b_i+1\) belongs to the even-spaced set \(\{b_j\}\); likewise \(b_i-1\) is not in that set. For any other unperturbed basis vector, its backward shift remains a high-degree monomial not selected by \(J\) and yields zero. The \(2r+1\) indices
\[
h-1,\quad a_1,\ldots,a_r,\quad a_1-1,\ldots,a_r-1
\]
are pairwise distinct because \(a_i=3i+1\) and \(a_r<h-1\). Thus the displayed \(2r+1\) quotient images are linearly independent and span \(JS^*M_r\). Hence
\[
\dim((M_r+S^*M_r)/M_r)=\dim(JS^*M_r)=2r+1.
\]
For every possible finite-dimensional defect space \(F\), the inclusion \(S^*M_r\subseteq M_r+F\) forces \(\dim F\ge2r+1\). Conversely the orthogonal projection of \(S^*M_r\) onto \(M_r^\perp\) provides a defect space of exactly this dimension. Since all \(f\in M_r\) satisfy \(f(0)=0\), this is precisely the minimal nearly invariant defect.

**4. Universality of sharpness.** Theorem 5.4 of [1] gives a bound at most \(2r+1\) for the kernel of *any* rank-at-most-\(r\) truncated Toeplitz perturbation. Steps 1–3 furnish an exact-rank-\(r\) example meeting this bound, for every integer \(r\ge1\). Thus the upper bound is universally optimal.

## Verification
The included `verify.py` uses only the Python standard library. Run `python3 verify.py`; it constructs the exact integer matrices of the perturbed truncated Toeplitz operators, their explicit kernel bases and quotient maps, and computes ranks using rational Gaussian elimination for \(1\le r\le7\). It checks \(T_rM_r=0\), \(JM_r=0\), the kernel dimension, perturbation rank and the exact quotient defect. These finite checks corroborate, but are **not** the proof of, the theorem for all ranks.

## Relationship to prior work
Chattopadhyay and Khan [1, Theorem 5.4 and Remark 5.6] prove the \(2r+1\) upper bound and tabulate its values, but do not construct rank-\(r\) kernels attaining it. This result determines the sharpness question by an explicit all-ranks family. O’Loughlin [2] develops general representations for nearly invariant subspaces and unperturbed truncated Toeplitz kernels. Liang–Partington [3] treat finite-rank perturbations of **ordinary** Toeplitz operators on full \(H^2\), with distinct symbol-dependent defect estimates. Neither of those statements supplies the exact minimal defect for the finite-dimensional compressed operators constructed here.

## Limitations
This result determines the optimal universal constant and builds sharp witnesses, but does not classify which perturbations attain maximal defect, nor address multiband-space bounds. It depends on the existing universal upper bound of [1]; all new lower-bound and equality computations are proved directly here. Publication-priority searches are not exhaustive, and independent external mathematical validation has not been performed.

## References
[1] A. Chattopadhyay and A. Khan, *Perturbations of Truncated Toeplitz operators*, arXiv:2610.40295v1 (first posted 2026-10-29), https://arxiv.org/html/2610.40295v1, especially Theorem 5.4 and Remark 5.6.

[2] R. O’Loughlin, *Nearly Invariant Subspaces with Applications to Truncated Toeplitz Operators*, Complex Analysis and Operator Theory 14, article 86 (2020), https://doi.org/10.1007/s11785-020-01049-4.

[3] Y. Liang and J. R. Partington, *Representing Kernels of Perturbations of Toeplitz Operators by Backward Shift-Invariant Subspaces*, Integral Equations and Operator Theory 92, article 35 (2020), https://doi.org/10.1007/s00020-020-02592-7; author-accepted version https://eprints.whiterose.ac.uk/162175/1/perturbations-of-Toeplitz-operators28.pdf.
