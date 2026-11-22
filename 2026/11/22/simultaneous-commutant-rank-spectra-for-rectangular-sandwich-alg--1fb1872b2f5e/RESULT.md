# Simultaneous commutant rank spectra for rectangular sandwich algebras

## Finding

Let \(K=\mathbb F_q\) be any finite field, \(m,n\geq1\), and \(A\in M_{n\times m}(K)\) have rank \(r\), where \(0\leq r\leq\min(m,n)\). On \(S=M_{m\times n}(K)\) use the associative sandwich multiplication \(X\star Y=XAY\). For each integer \(t\geq1\), consider an **ordered**, pairwise-commuting tuple \(\mathbf e=(e_1,\ldots,e_t)\) of sandwich-idempotents, meaning \(e_iAe_i=e_i\) and \(e_iAe_j=e_jAe_i\) for all indices.

Write \(\Sigma=\{0,1\}^t\), \(\boldsymbol0=(0,\ldots,0)\), and \(\tau=m+n-2r\). Each such tuple has canonical simultaneous core eigenspace multiplicities \(d_\sigma\geq0\), one for every \(\sigma\in\Sigma\), with \(\sum_\sigma d_\sigma=r\). Put \(D=\sum_{\sigma\ne\boldsymbol0}d_\sigma=r-d_{\boldsymbol0}\). These multiplicities are defined by the joint eigenspaces of the commuting projections \(Ae_i\) on the image of \(A\), equivalently by the upper-left \(r\times r\) blocks after any rank-normalization of \(A\).

Let \(G_j(q)=|\operatorname{GL}_j(K)|=\prod_{i=0}^{j-1}(q^j-q^i)\), with \(G_0(q)=1\), and let
\[
R_{a,b}(z)=\sum_{j=0}^{\min(a,b)}\left(\prod_{i=0}^{j-1}\frac{(q^a-q^i)(q^b-q^i)}{q^j-q^i}\right)z^j.
\]
The empty product equals one, including when either dimension is zero. Thus \(R_{a,b}\) is the ordinary matrix-rank polynomial of \(M_{a\times b}(K)\).

**Theorem (mixed commuting-tuple and unrestricted-commutant census).** For every admissible vector \(\mathbf d=(d_\sigma)_{\sigma\in\Sigma}\):

1. The number of ordered commuting sandwich-idempotent tuples of simultaneous type \(\mathbf d\) is exactly
\[
N(\mathbf d)=\frac{G_r(q)}{\prod_{\sigma\in\Sigma}G_{d_\sigma}(q)}\,q^{\tau D}.
\]
2. For **each individual tuple** of type \(\mathbf d\), its simultaneous centralizer
\[
C_S(\mathbf e)=\{Y\in S: Y\star e_i=e_i\star Y\ \text{for all }i\}
\]
is, as a sandwich algebra/semigroup, isomorphic to the direct product of ordinary square matrix algebras \(M_{d_\sigma}(K)\) over nonzero signatures and a residual rectangular sandwich algebra of dimensions \((m-D)\times(n-D)\) with sandwich rank \(d_{\boldsymbol0}\). This isomorphism preserves the **ordinary matrix rank as the sum of ranks of the components**. Therefore its complete ordinary-rank polynomial is
\[
\boxed{\sum_{Y\in C_S(\mathbf e)}z^{\operatorname{rank}Y}
=R_{m-D,n-D}(z)\prod_{\sigma\ne\boldsymbol0}R_{d_\sigma,d_\sigma}(z).}
\]
In particular, its size is exactly
\[
\boxed{|C_S(\mathbf e)|=q^{(m-D)(n-D)+\sum_{\sigma\ne\boldsymbol0}d_\sigma^2}.}
\]
3. Consequently the **complete mixed rank enumerator**, weighting the ranks of all idempotents and the rank of one completely unrestricted centralizing element, equals
\[
\boxed{\begin{aligned}
\mathcal H_t(u_1,\ldots,u_t;z)
={}&\sum_{\substack{d_\sigma\geq0\\\sum_\sigma d_\sigma=r}}
\frac{G_r(q)}{\prod_\sigma G_{d_\sigma}(q)}\,q^{\tau D}
\left(\prod_{i=1}^t u_i^{\sum_{\sigma:\sigma_i=1}d_\sigma}\right)\\[-1mm]
&\quad\cdot R_{m-D,n-D}(z)
\prod_{\sigma\ne\boldsymbol0}R_{d_\sigma,d_\sigma}(z).
\end{aligned}}
\]
The polynomial on the left is defined directly as the sum of \(u_1^{\operatorname{rank}e_1}\cdots u_t^{\operatorname{rank}e_t}z^{\operatorname{rank}Y}\) over all the indicated tuples and all \(Y\in C_S(\mathbf e)\).

A notable consequence of part 2 is that **conditional on the simultaneous type, the entire commutant rank distribution is independent of the sandwich-matrix rank \(r\)**. For \(t=1\) and an idempotent of ordinary rank \(k\), the centralizer polynomial simplifies to \(R_{k,k}(z)R_{m-k,n-k}(z)\), of size \(q^{k^2+(m-k)(n-k)}\), even if the rank of \(A\) varies subject to \(r\geq k\).

## Assumptions and scope

All dimensions are nonnegative integers and matrices of dimension zero form the one-element zero algebra when they occur as factors. The ground field is finite for the enumerative claims; the structural normal form holds over an arbitrary field. Ordinary matrix rank must not be confused with the sandwich rank of \(A\). The centralizing element \(Y\) is **not** required to be idempotent, regular, invertible, or of bounded sandwich rank. The tuple is ordered, and repetitions and zero idempotents are permitted. The case \(r=0\) has only the all-zero idempotent tuple and centralizer equal to the full \(M_{m\times n}(K)\).

The signature \(\sigma\) has its \(i\)-th coordinate equal to the eigenvalue of the core projection corresponding to \(e_i\). If \(A\) is replaced by a rank-equivalent matrix, an invertible left/right matrix change gives an algebra isomorphism preserving each ordinary matrix rank, so the multiplicities and enumerators are well-defined.

## Proof

**1. Rank normalization and idempotent normal forms.** By invertible row/column changes we may assume
\[
A=\begin{pmatrix}I_r&0\\0&0\end{pmatrix}\in M_{n\times m}(K).
\]
Write \(p=m-r\), \(s=n-r\). An arbitrary matrix in \(S\) has blocks \(X=\begin{pmatrix}B&C\\D&E\end{pmatrix}\) of respective sizes \(r\times r\), \(r\times s\), \(p\times r\), \(p\times s\). The equation \(XAX=X\) is equivalent to
\[
B^2=B,\qquad BC=C,\qquad DB=D,\qquad E=DC.
\]
For two such idempotents the upper-left projections commute whenever the original matrices commute, since the upper-left block of their sandwich product is their ordinary product.

**2. Joint eigenspace decomposition.** Let \(B_1,\ldots,B_t\) be the commuting core projections. For each \(\sigma\in\Sigma\), define
\[
P_\sigma=\prod_{i:\sigma_i=1}B_i\prod_{i:\sigma_i=0}(I_r-B_i).
\]
The \(P_\sigma\) are pairwise orthogonal idempotents, sum to \(I_r\), and decompose the core \(K^r=\bigoplus_\sigma W_\sigma\), where \(W_\sigma=\operatorname{im}P_\sigma\) has dimension \(d_\sigma\). This works in every characteristic. Conversely any ordered direct-sum decomposition into the \(2^t\) color spaces uniquely gives the commuting projections \(B_i=\sum_{\sigma:\sigma_i=1}P_\sigma\). The number of these decompositions is \(G_r(q)/\prod_\sigma G_{d_\sigma}(q)\).

**3. Counting off-core lifts.** Write the remaining blocks for \(e_i\) as \(C_i,D_i,E_i\). Idempotence gives \(C_i=B_iC_i\), \(D_i=D_iB_i\), \(E_i=D_iC_i\). Comparing upper-right blocks of \(e_iAe_j=e_jAe_i\) gives \(B_iC_j=B_jC_i\). On \(W_\sigma\), every \(C_i\) vanishes if \(\sigma_i=0\); if \(\sigma\ne\boldsymbol0\), any one index with \(\sigma_i=1\) fixes a **single shared** column map \(C_\sigma\), and the \(\sigma\)-component of \(C_i\) is \(\sigma_iC_\sigma\). The zero-signature component vanishes. Comparing lower-left blocks yields the dual shared maps \(D_\sigma\) with \(\sigma_iD_\sigma\) in \(D_i\). The lower-right commutation condition follows automatically because the common maps give \(D_iC_j=D_jC_i\).

Equivalently there are unique maps \(C\in M_{r\times s}(K)\) and \(D\in M_{p\times r}(K)\), zero on the signature-zero core space, such that
\[
e_i=\begin{pmatrix}B_i&B_iC\\DB_i&DB_iC\end{pmatrix}.
\]
Their free parameters number \(sD+pD=\tau D\), giving exactly \(q^{\tau D}\) lifts of each core decomposition and proving part 1. No division by automorphisms occurs.

**4. Simultaneous untwisting.** Define the invertible matrices
\[
L=\begin{pmatrix}I_r&0\\D&I_p\end{pmatrix},\qquad
R=\begin{pmatrix}I_r&C\\0&I_s\end{pmatrix}.
\]
They satisfy \(RAL=A\) and \(e_i=L\operatorname{diag}(B_i,0)R\). The rank-preserving change \(Y\mapsto L^{-1}YR^{-1}\) is a sandwich-algebra automorphism, because \(R^{-1}AL^{-1}=A\), and sends every \(e_i\) to \(\operatorname{diag}(B_i,0)\). An additional simultaneous change of core basis diagonalizes all the \(B_i\) without changing \(A\). Thus it suffices to calculate the common commutant of \(e_i^0=\operatorname{diag}(B_i,0)\) with all core projections diagonal by signature.

**5. Exact centralizer blocks and matrix rank.** For \(Y=\begin{pmatrix}H&U\\V&Z\end{pmatrix}\), the equations \(e_i^0 A Y=Y A e_i^0\) say precisely
\[
B_iH=HB_i,\qquad B_iU=0,\qquad VB_i=0\quad(1\leq i\leq t).
\]
The first condition eliminates every block of \(H\) between different signatures. The second and third allow off-core blocks only from, respectively into, \(W_{\boldsymbol0}\); the lower-right \(Z\) is unrestricted. Consequently \(Y\) is block diagonal, after grouping \(W_{\boldsymbol0}\) with the external row and column spaces, with arbitrary square blocks of sizes \(d_\sigma\) for each \(\sigma\ne\boldsymbol0\), and one arbitrary rectangular block of size \((m-D)\times(n-D)\). The corresponding restricted sandwich matrix is the identity on each nonzero square block and has rank \(d_{\boldsymbol0}\) on the residual rectangular block. Ordinary matrix rank adds across these disjoint blocks. This establishes the algebra product decomposition, the rank-polynomial factorization, and the size formula in part 2.

**6. Complete mixed census.** The ordinary rank of \(e_i\) is \(\sum_{\sigma:\sigma_i=1}d_\sigma\), by the factorization in step 3. Multiply the number of tuples of each type from step 3 by the complete rank polynomial of its common centralizer from step 5 and by these rank monomials. Sum over all \(\mathbf d\) of total dimension \(r\). This proves part 3 without an asymptotic assumption.

## Verification

The standalone `checker.py` directly enumerates the original \(m\times n\) matrices and computes the sandwich products, idempotents, all ordered commuting tuples and their **unrestricted** common centralizers. It independently obtains matrix ranks by prime-field Gaussian elimination. Separately it computes the claimed normal-form multiplicities and the rank polynomials from their explicit finite products; it checks every signature-type multiplicity and every coefficient of each individual common-centralizer rank polynomial, not merely totals.

The tested parameter tuples \((q,m,n,r,t)\) include \((2,2,2,0,2)\), \((2,2,2,1,2)\), \((2,2,2,2,2)\), \((2,2,2,1,3)\), \((2,3,2,1,2)\), \((2,2,3,1,2)\), \((3,2,2,1,2)\), \((2,3,3,2,2)\), \((2,2,2,2,3)\), and \((3,2,2,2,2)\). Every check passed. For \((q,m,n,r,t)=(2,3,3,2,2)\), there are \(409\) ordered commuting pairs of idempotents and exactly \(6656\) ordered triples consisting of such a pair and an unrestricted common centralizer element. The latter number counts repeats and all ordinary ranks of the third element.

At these same ambient dimensions, take commuting rank-one idempotents \(e_1=e_2=\operatorname{diag}(1,0,0)\) and compare them to \(e_1=\operatorname{diag}(1,0,0)\), \(e_2=\operatorname{diag}(0,1,0)\), with the rank-two diagonal sandwich matrix. Both pairs have marginal ranks \((1,1)\), but their common centralizers have sizes \(32\) and \(8\), respectively: the former has one nonzero signature block, while the latter has two. Thus marginal ranks alone do not determine this new invariant.

Run `python checker.py` beside this document. The checker handles prime fields \(\mathbb F_2\) and \(\mathbb F_3\) in the listed cases; its finite checks do not prove the theorem for other fields or all dimensions. The complete proof above supplies that quantification.

## Relationship to prior work

Dolinka and East, *Semigroups of rectangular matrices under a sandwich operation* (arXiv:1503.03139, first publicly submitted 2015-03-11), develop exactly this sandwich-semigroup setting. Their Proposition 7.2 counts idempotents of each rank, and Lemma 4.1 identifies rank-equivalent sandwich matrices. These facts are used and are **not** claimed as new. Their inspected introduction, Sections 4 and 7 and text search do not state a rank-refined common commutant of an arbitrary tuple against unrestricted elements.

A published result titled *Joint matrix-rank spectrum of commuting idempotents in rectangular sandwich semigroups* supplies the bivariate joint-rank census for **two idempotent factors**. The \(t=2\) idempotent-only count of part 1 specializes to this already covered formula; it is not independently claimed. That work restricts both coordinates to idempotents. The genuinely additional statistic here is the complete ordinary rank of an **arbitrary** element centralizing all tuple members, with its individual product decomposition, and the resulting mixed census for every tuple arity. This cannot be obtained by simply interpreting the second idempotent in the previous theorem as an arbitrary matrix.

The broader published theorem *Simultaneous idempotent spectra of split basic algebras and an inverse random-cluster invariant* counts idempotent tuples with left/right regular ranks in **unital split-basic algebras**. General rectangular sandwich algebras need not be unital or split basic, and that theorem neither counts unrestricted common-centralizer elements nor their ordinary matrix ranks. Standard simultaneous spectral and Peirce decompositions explain the underlying mechanism, but do not alone provide the explicit all-arity rectangular-sandwich mixed rank polynomial.

A historical equivalent may still be implicit in generalized-matrix-algebra commutant theory; priority is not independently certified.

## Limitations

The formula counts common centralizers of a **pairwise-commuting idempotent tuple**; it does not enumerate centralizers of arbitrary nonidempotent tuples, classify the entire unrestricted commuting graph, or describe isomorphism classes of ambient sandwich algebras beyond rank-equivalence. The residual sandwich-factor multiplication depends on \(d_{\boldsymbol0}\), even though its **ordinary rank census** depends only on its rectangular dimensions. Over infinite fields the block decomposition remains valid but the finite-field polynomials no longer represent finite cardinalities. The computation tests only selected prime fields and small dimensions; historical priority and independent validation are not established.

## References

1. I. Dolinka and J. East, *Semigroups of rectangular matrices under a sandwich operation*, arXiv:1503.03139 (2015-03-11), especially Lemma 4.1 and Proposition 7.2. https://arxiv.org/abs/1503.03139
2. *Joint matrix-rank spectrum of commuting idempotents in rectangular sandwich semigroups* (2026), publicly available research result, https://github.com/published-finding corpus/2026/tree/main/2026/10/13/SCOPE-joint-matrix-rank-spectrum-of-commuting-idempotents-in-rectangul--85aa4c5711c9
3. *Simultaneous idempotent spectra of split basic algebras and an inverse random-cluster invariant* (2026), publicly available research result, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-simultaneous-idempotent-spectra-of-split-basic-algebras-and-an-i--4fe52ac53574
4. J. R. Britnell and M. Wildon, *On types and classes of commuting matrices over finite fields*, Journal of the London Mathematical Society 83 (2011), 470–492, DOI: 10.1112/jlms/jdq088. This paper addresses square-matrix similarity-class commutation, rather than the present rectangular sandwich setting.
