# Field-size-universal idempotent laws for triangular perfect evolution algebras in characteristic two

## Finding
Fix integers \(n\ge1\) and \(s\ge1\), put \(q=2^s\), and choose an \(n\times n\) invertible upper-triangular structure matrix uniformly over \(\mathbb F_q\). For the resulting labeled perfect evolution algebra, let \(K_n\) be the number of **nonzero** idempotents over \(\mathbb F_q\). Then, for every \(n,s\),
\[
 K_n=2^{D_n}-1,\qquad 1\le D_n\le n,
\]
where the **complete law** of \(D_n\) is independent of \(q\) and is given by
\[
 \Pr(D_1=1)=1,\qquad
 \Pr(D_{j+1}=d+1\mid D_j=d)=2^{-d},\quad
 \Pr(D_{j+1}=d\mid D_j=d)=1-2^{-d}.
\]
Equivalently, for \(P_j(d)=\Pr(D_j=d)\), with outside-range probabilities zero,
\[
 P_1(1)=1,\qquad
 P_{j+1}(d)=(1-2^{-d})P_j(d)+2^{-(d-1)}P_j(d-1).
\]
In particular,
\[
 \mathbb E K_n=n,\qquad \operatorname{Var}(K_n)=\binom n2,
\]
and the minimum and maximum atoms are
\[
 \Pr(K_n=1)=2^{1-n},\qquad
 \Pr(K_n=2^n-1)=2^{-n(n-1)/2}.
\]
This is a full finite-dimensional law, not merely an asymptotic statement. In contrast to sampling from the entire general linear group, this triangular ensemble has at least one nonzero rational idempotent in **every** realization.

## Assumptions and scope
For a fixed labeled natural basis \(e_1,\dots,e_n\), an evolution algebra has \(e_ie_j=0\) for \(i\ne j\). The matrix convention is \(e_i^2=\sum_{j=i}^n m_{ij}e_j\) with \(m_{ii}\ne0\) and arbitrary \(m_{ij}\in\mathbb F_q\) for \(i<j\). Choose all \(n\) diagonal entries independently uniformly in \(\mathbb F_q^\times\), and all \(\binom n2\) strict-upper entries independently uniformly in \(\mathbb F_q\); equivalently, choose uniformly from invertible upper-triangular matrices. This is sampling labeled structure matrices, **not** sampling isomorphism classes. The matrix is invertible, hence its algebra is perfect (\(A^2=A\)). Idempotents are rational points \(x\in A(\mathbb F_q)\) satisfying \(x^2=x\), not geometric points over an algebraic closure. No assertion is made for odd characteristic, for arbitrary invertible matrices, or for sparse distributions other than the full upper-triangular support.

## Proof
Write \(x=\sum_j x_j e_j\). The idempotent equations are
\[
 x_j=m_{jj}x_j^2+\sum_{i<j}m_{ij}x_i^2\quad (j=1,\ldots,n).
\]
Let \(a_i=m_{ii}\ne0\), \(y_i=a_ix_i\), and \(b_{ij}=a_jm_{ij}/a_i^2\). Multiplication of the \(j\)-th equation by \(a_j\) gives, **because the characteristic is two**,
\[
 \psi(y_j):=y_j^2+y_j=\sum_{i<j}b_{ij}y_i^2.
 \tag{1}
\]
Conditionally on the diagonal, the \(b_{ij}\) are jointly independent uniform elements of \(\mathbb F_q\), and conversely this transformation is bijective on strict-upper entries. Therefore they may be treated as independent uniform field elements.

Let \(\operatorname{Tr}:\mathbb F_q\to\mathbb F_2\) be the absolute field trace. The additive homomorphism \(\psi(y)=y^2+y\) has kernel \(\mathbb F_2\), and image \(\ker\operatorname{Tr}\): both are \(\mathbb F_2\)-subspaces of size \(q/2\), and \(\operatorname{Tr}(y^2+y)=0\). The trace functional is nonzero, because the finite-field trace pairing is nondegenerate (even when \(s\) is even). Thus each trace-zero value has **exactly two** \(\psi\)-preimages.

Let \(S_j\subset\mathbb F_q^j\) denote the solution set to the first \(j\) equations (1). All equations are additive over \(\mathbb F_2\), hence \(S_j\) is an \(\mathbb F_2\)-linear space. At \(j=1\), \(S_1=\mathbb F_2\), so \(D_1:=\dim_{\mathbb F_2}S_1=1\).

Fix the previous coefficients and \(S_{j-1}\) with dimension \(d\). A vector \((y_1,\ldots,y_{j-1})\in S_{j-1}\) extends to a solution of (1) at index \(j\) exactly if
\[
 \ell_j(y)=\operatorname{Tr}\!\left(\sum_{i<j} b_{ij}y_i^2\right)=0.
\]
As the new \(b_{ij}\) vary uniformly, \(\ell_j\) is uniform on the entire \(\mathbb F_2\)-dual of \(S_{j-1}\). To prove this rather than assume it: coordinatewise Frobenius \(y\mapsto y^2\) is an invertible \(\mathbb F_2\)-linear map on \(\mathbb F_q^{j-1}\), and the trace pairing \((b,z)\mapsto \operatorname{Tr}(\sum b_i z_i)\) identifies its first factor with the full \(\mathbb F_2\)-dual of the second. Restriction of all ambient linear functionals to the subspace \(S_{j-1}\) is surjective. Every fiber of this restriction has equal size, proving uniformity.

Consequently \(\Pr(\ell_j=0)=2^{-d}\); when \(\ell_j=0\), every previous solution has exactly two extensions and \(D_j=d+1\). When \(\ell_j\ne0\), the kernel has dimension \(d-1\), each of its points has two extensions and \(D_j=d\). This proves the stated Markov transition and the full \(q\)-independent law. Since \(S_n\) has \(2^{D_n}\) elements including the zero idempotent, \(K_n=2^{D_n}-1\).

For the moments put \(Z_j=K_j+1=2^{D_j}\). Conditional on \(D_j=d\), \(Z_{j+1}\) equals \(2Z_j\) with probability \(1/Z_j\), and \(Z_j\) otherwise. Hence
\[
 \mathbb E(Z_{j+1}\mid Z_j)=Z_j+1,\qquad
 \mathbb E(Z_{j+1}^2\mid Z_j)=Z_j^2+3Z_j.
\]
As \(Z_1=2\), induction gives \(\mathbb EZ_n=n+1\) and \(\mathbb EZ_n^2=1+3n(n+1)/2\). Subtracting yields \(\mathbb EK_n=n\) and \(\operatorname{Var}(K_n)=n(n-1)/2\).

Finally \(D_n=1\) iff the dimension never increases, yielding \(\prod_{j=1}^{n-1}(1-2^{-1})=2^{1-n}\). Likewise \(D_n=n\) iff it increases at every step, with probability \(\prod_{d=1}^{n-1}2^{-d}=2^{-n(n-1)/2}\). These prove the two extreme atoms.

## Verification
The standalone exact checker `verify.py` enumerates every allowed triangular structure matrix and every field-valued vector, computes its idempotents directly, and compares the empirical rational probabilities with the proved recurrence, mean, and variance. It implements independent arithmetic in \(\mathbb F_2\), \(\mathbb F_4\), and \(\mathbb F_8\). The complete tested set consists of \(11\) field/dimension combinations and \(36{,}033\) distinct structure matrices; see `verification_output.txt`. Execute `python3 verify.py` using the Python standard library. Tests use no random sampling. These finite tests corroborate rather than substitute for the all-dimensional proof.

## Relationship to prior work
The October 2026 survey by Kaygorodov, Martín González and Viruel (Remark 23, PDF page 19; Question 22, PDF page 23) establishes mean **one** for the number of nonzero idempotents when the structure matrix is uniform over the **entire** general linear group; it asks about distributions of random evolution algebras and sparse graph support. The triangular support here is a genuinely different ensemble: it forces nonzero idempotents, has mean \(n\), and a complete field-size-universal law. The survey does not state the triangular law, variance, or transition probabilities. The 2023 Wei–Zou article counts isomorphism classes of perfect evolution algebras rather than idempotent counts in this labeled triangular ensemble. The 2024 study by Van Peski, *The Rank of a Random Triangular Matrix Over \(\mathbb F_q\)*, develops finite-\(n\) rank laws and asymptotics for uniform strictly triangular matrices. Its binary-field special case covers closely related rank recurrences and may imply the **\(q=2\)** instance here. However the new assertion that the **same nonzero-idempotent law holds over every \(\mathbb F_{2^s}\)** for nonlinear evolution-algebra equations, together with its interpretation and moments, was not identified in that work; its full text could not be inspected, so a stronger implication remains an unresolved originality risk. Mészáros studies persistence diagrams of random triangular matrices; its accessible abstract likewise does not establish this semilinear universality. Historical priority of the binary rank recurrence alone is not claimed.

## Limitations
This theorem treats only the stated uniform invertible triangular model over characteristic-two finite fields and counts field-rational idempotents. It is not a distribution for uniformly random isomorphism classes, the full general linear group, geometric idempotents over an algebraic closure, or odd characteristic. The rank laws of Van Peski (arXiv:2407.19578) may already imply the binary-field special case, and an unforeseen broader semilinear consequence remains a risk; independent historical verification has not been performed. The theorem is proved without relying on experiments beyond finite checks.

## References
1. I. Kaygorodov, C. Martín González and A. Viruel, *Evolution algebras: a survey of results and a list of open problems*, arXiv:2610.22248v1, first public 2026-10-15, Remark 23 and Question 22. https://arxiv.org/abs/2610.22248; full text https://pdfs.assets.alphaxiv.org/2610.22248v1.pdf.
2. G. Mészáros, *Persistence diagrams of random triangular matrices over finite fields*, arXiv:2606.17895, first public 2026-06-16. https://arxiv.org/abs/2606.17895.
3. Y. Wei and Y. Zou, *Isomorphism Classes of Idempotent Evolution Algebras*, arXiv:2310.12368v1, first public 2023-10-18. https://arxiv.org/abs/2310.12368.
4. R. Van Peski, *The Rank of a Random Triangular Matrix Over \(\mathbb F_q\)*, arXiv:2407.19578v1, first public 2024-07-28; published in International Mathematics Research Notices 2026, rnaf371. https://arxiv.org/abs/2407.19578.
5. F. Mukhamedov and I. Qaralleh, *On Extendibility of Evolution Subalgebras Generated by Idempotents*, Mathematics 11 (2023), 2764. https://doi.org/10.3390/math11122764.
