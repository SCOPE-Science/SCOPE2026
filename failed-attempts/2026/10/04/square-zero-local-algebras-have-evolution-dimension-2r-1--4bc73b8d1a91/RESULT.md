# Square-zero local algebras have evolution dimension \(2r+1\)
## Finding
Let \(\mathbb F\) be a field of characteristic different from \(2\), let \(V\) be an \(r\)-dimensional \(\mathbb F\)-vector space with \(r\ge 1\), and let
\[
A_r=\mathbb F\oplus V,\qquad (a,u)(b,v)=(ab,av+bu).
\]
Thus \(A_r\) is the unital square-zero local algebra with radical \(V\) and \(V^2=0\). Its squaring map has simultaneous Waring rank exactly
\[
\operatorname{wr}(H_{A_r})=2r+1.
\]
Consequently, in the sense of Costoya--Fernández Ouaridi--Viruel, the smallest dimension of an evolution algebra containing \(A_r\) as an ideal is
\[
\operatorname{edim}(A_r)=2r+1.
\]

## Assumptions and scope
The field is arbitrary except that \(2\) must be invertible. No algebraic-closure or field-cardinality hypothesis is used. The conclusion concerns the evolution dimension introduced for finite-dimensional commutative algebras and the simultaneous Waring rank of the vector-valued quadratic squaring map.

Choose a basis \(e_1,\ldots,e_r\) of \(V\), put \(e_0=1\), and let \(x_0,\ldots,x_r\) be the dual coordinates. Then
\[
H_{A_r}(x)=x_0^2e_0+2x_0\sum_{i=1}^r x_i e_i.
\]
The scalar coordinate space of this map is
\[
W=\operatorname{span}\{x_0^2,x_0x_1,\ldots,x_0x_r\}.
\]

## Proof
A vector-valued Waring decomposition
\[
H_{A_r}(x)=\sum_{j=1}^m \ell_j(x)^2v_j
\]
exists exactly when the coordinate space \(W\) is contained in the span
\[
S=\operatorname{span}\{\ell_1^2,\ldots,\ell_m^2\}.
\]
Hence it is enough to determine the least number of squares of linear forms whose span contains \(W\).

For the upper bound, use the \(2r+1\) squares
\[
x_0^2,\qquad (x_0+x_i)^2,\qquad (x_0-x_i)^2\quad(1\le i\le r).
\]
Since
\[
2x_0x_i=\frac{(x_0+x_i)^2-(x_0-x_i)^2}{2},
\]
they span every element of \(W\). Therefore
\[
\operatorname{wr}(H_{A_r})\le 2r+1.
\]

For the lower bound, write each linear form as
\[
\ell_j=a_jx_0+\beta_j,\qquad \beta_j\in V^*.
\]
Let
\[
\pi:\operatorname{Sym}^2(\mathbb F x_0\oplus V^*)\longrightarrow \operatorname{Sym}^2(V^*)
\]
be the projection obtained by setting \(x_0=0\). Because \(W\subseteq S\cap\ker\pi\),
\[
\dim S\ge \dim W+\dim \pi(S)=r+1+\dim\operatorname{span}\{\beta_j^2\}.
\]

The mixed \(x_0V^*\)-part of \(\ell_j^2\) is \(2a_jx_0\beta_j\). Since \(W\) contains \(x_0\gamma\) for every \(\gamma\in V^*\), comparison of mixed parts in representations of those elements by the \(\ell_j^2\) shows that the \(\beta_j\) span \(V^*\). Select \(r\) linearly independent members \(\beta_{j_1},\ldots,\beta_{j_r}\). After using them as part of a coordinate basis, their squares are distinct quadratic coordinate monomials, so
\[
\beta_{j_1}^2,\ldots,\beta_{j_r}^2
\]
are linearly independent in \(\operatorname{Sym}^2(V^*)\). Thus
\[
\dim\operatorname{span}\{\beta_j^2\}\ge r,
\]
and consequently
\[
m\ge\dim S\ge 2r+1.
\]
Together with the upper bound this proves
\[
\operatorname{wr}(H_{A_r})=2r+1.
\]

Costoya--Fernández Ouaridi--Viruel prove, over characteristic different from \(2\), that for a unital commutative algebra the evolution dimension equals the Waring rank of its squaring map. Applying that theorem gives
\[
\operatorname{edim}(A_r)=2r+1.
\]

## Verification
The upper bound is an explicit identity and uses only division by \(2\). The lower bound is a dimension argument in a symmetric square. Its two critical points are: the mixed terms force the \(\beta_j\) to span \(V^*\), and squares of \(r\) linearly independent linear forms are linearly independent after a change of coordinates. Neither step uses algebraic closure, genericity, or a finite computation.

For \(r=1\), the formula gives \(3\), agreeing with the dual-number decomposition exhibited in the recent evolution-envelope paper. The proof works uniformly for every finite \(r\ge1\).

## Relationship to prior work
Costoya, Fernández Ouaridi, and Viruel reduce the evolution-dimension problem for unital commutative algebras to the simultaneous Waring rank of the squaring map and explicitly treat truncated polynomial algebras; their dual-number example is the case \(r=1\). The argument above computes the rank for the different natural family \(\mathbb F\oplus V\) with \(V^2=0\) and arbitrary radical dimension.

Carlini and Ventura give exact simultaneous Waring-rank formulas for several collections of monomials. Their different-support theorem assumes that exponents on the support unique to one monomial are at least \(2\); their subsequent remark explicitly notes that the analogous upper-bound argument is not known when such an exponent is \(1\). The star collection underlying the present coordinate space contains the exponent-one monomials \(x_0x_i\), so those formulas do not imply the result.

A published record on the same square-zero local family computes all-degree Tor groups of the dual module. Its objects coincide with \(A_r=\mathbb F\oplus V\), but its statements concern derived homology rather than simultaneous Waring rank or evolution dimension and therefore do not cover the claim here.

## Limitations
No statement is made in characteristic \(2\), where the displayed polarization identities degenerate. The originality comparison was targeted rather than exhaustive: older algebraic-complexity or tensor-rank literature could contain an equivalent formula under different terminology. The proof itself is self-contained and does not depend on the absence of such a reference.

## References
1. Cristina Costoya, Amir Fernández Ouaridi, Antonio Viruel, *Commutative algebras are ideals of evolution algebras*, arXiv:2609.32784v1, 2026.
2. Enrico Carlini, Emanuele Ventura, *A note on the simultaneous Waring rank of monomials*, Illinois Journal of Mathematics 61 (2017), DOI 10.1215/ijm/1534924838; arXiv:1711.00089.
