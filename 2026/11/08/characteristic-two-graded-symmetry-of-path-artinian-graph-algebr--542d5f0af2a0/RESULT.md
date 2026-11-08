# Characteristic-two graded symmetry of path Artinian graph algebras

## Finding
For every integer \(n\ge4\) and finite field \(k=\mathbb F_q\) of characteristic two, put
\[
A_n(k)=k[x_1,\ldots,x_n]/(x_1^2,\ldots,x_n^2,x_1x_2,\ldots,x_{n-1}x_n).
\]
Every graded \(k\)-algebra automorphism is uniquely a reflection \(x_i\mapsto x_{n+1-i}\), optionally followed by an automorphism of the following form, with \(a_1,\ldots,a_n\in k^\times\) and \(b_1,c_1,b_n,c_n\in k\):
\[
\begin{aligned}
x_1&\longmapsto a_1x_1+b_1x_2+c_1x_3,\\
x_i&\longmapsto a_ix_i\quad(2\le i\le n-1),\\
x_n&\longmapsto a_nx_n+b_nx_{n-1}+c_nx_{n-2}.
\end{aligned}
\]
Consequently the *graded* automorphism group has exactly
\[
\boxed{|\operatorname{Aut}_{\mathrm{gr},k}(A_n(k))|=2q^4(q-1)^n.}
\]
The two independent extra endpoint parameters \(c_1,c_n\) are a characteristic-two phenomenon. For comparison, the same direct argument gives \(2q^2(q-1)^n\) in odd characteristic, with both extra coefficients necessarily zero; that characteristic-zero-type portion is not asserted as a new classification.

## Assumptions and scope
Here \(n\ge4\); the graph is the path with edges \(\{i,i+1\}\). The ring is commutative, standard \(\mathbb N\)-graded, and finite dimensional because every generator squares to zero. All automorphisms are \(k\)-linear and preserve this grading. A graded automorphism is determined by its invertible linear map on the degree-one space \(V=\langle x_1,\ldots,x_n\rangle_k\). The theorem concerns this graded group, **not** the full group of arbitrary (potentially nonhomogeneous) algebra automorphisms.

## Proof
Write \(vw\) for multiplication of linear forms in \(A_n(k)\). The distinct monomials \(x_ix_j\) with \(|i-j|\ge2\) form a \(k\)-basis of the quadratic component. Thus for \(v=\sum_iv_ix_i\) and \(w=\sum_iw_ix_i\), the equality \(vw=0\) holds precisely when
\[
v_iw_j+v_jw_i=0\qquad\text{for all }|i-j|\ge2.
\]
For nonzero \(v\), write \(I=\{i:v_i\ne0\}\) and \(\operatorname{Ann}_V(v)=\{w\in V:vw=0\}\). We claim that whenever \(|I|\ge2\),
\[\dim_k\operatorname{Ann}_V(v)\le2.\]
Indeed, for \(j\notin I\) with \(w_j\ne0\), the displayed equations force \(j\) to be adjacent in the original path to *every* element of \(I\). If \(|I|\ge3\), no such \(j\) exists (a path vertex has at most two neighbors). If \(|I|=2\), there is at most one such \(j\), and it can exist only when the two supported vertices are nonadjacent to one another. On \(I\), put \(t_i=w_i/v_i\). Every pair of distinct supported vertices nonadjacent in the original path imposes \(t_j=-t_i\). The space of such \(t\) has dimension at most the number of components of the graph complementary to the induced path on \(I\). This complementary graph has at most two components: if it had three, picking one vertex from each would give a triangle in the original path. When \(|I|=2\) with the pair adjacent, it has two isolated components and there is no outside common neighbor; when the pair is nonadjacent, it has one component and at most one outside common neighbor. Thus the total dimension is always at most two, in any characteristic.

For a basis vector, the defining relations directly give
\[
\dim_k\operatorname{Ann}_V(x_i)=\begin{cases}2,&i=1,n,\\3,&2\le i\le n-1.\end{cases}
\]
The preceding bound therefore characterizes, among nonzero lines in \(V\), precisely the \(n-2\) interior coordinate lines as those having annihilator dimension three. Any graded automorphism preserves this dimension and hence permutes the interior coordinate lines. Because \(x_ix_{i+1}=0\) for consecutive interior indices and the image lines remain distinct, this permutation preserves adjacency in the path on \(2,\ldots,n-1\). It is thus identity or reversal. After composing with the obvious global reflection, write \(T(x_i)=a_ix_i\) for every \(2\le i\le n-1\), where \(a_i\ne0\).

The two remaining adjacent-product relations force
\[
T(x_1)\in\operatorname{Ann}_V(x_2)=\langle x_1,x_2,x_3\rangle,
\quad T(x_n)\in\operatorname{Ann}_V(x_{n-1})=\langle x_{n-2},x_{n-1},x_n\rangle.
\]
Invertibility forces the coefficients of \(x_1\) and \(x_n\) in these respective images to be nonzero. Conversely, every invertible linear map of the displayed form respects all consecutive-product relations. In characteristic two it respects the square relations automatically, because any linear form satisfies \(v^2=\sum_iv_i^2x_i^2=0\). It therefore induces a surjective graded endomorphism of a finite-dimensional algebra, hence an automorphism.

There are exactly \((q-1)^n\) choices of nonzero diagonal coefficients, \(q^4\) independent endpoint additions, and two disjoint choices of interior permutation. This proves the stated order and classification. For odd characteristic, squaring the two endpoint images gives respectively \(2a_1c_1x_1x_3\) and \(2a_nc_nx_{n-2}x_n\), so \(c_1=c_n=0\), establishing the comparison.

## Verification
The accompanying standalone `verify.py` enumerates degree-one column images using the actual quotient multiplication table and finite-field Gaussian elimination; it tests invertibility and every defining quadratic relation, without assuming the classification. The finite fields of sizes \(2\), \(3\), and \(4\) use separate arithmetic, with \(\mathbb F_4\) constructed using \(t^2+t+1\). The program verifies exact counts for \((n,q)=(4,2),(5,2),(6,2),(4,3),(5,3),(4,4)\), giving respectively \(32,32,32,288,576,41472\). Execute `python verify.py`; expected final line `VERIFY_OK`. The finite tests are corroboration; the all-\(n\), all-even-prime-power statement follows from the proof.

## Relationship to prior work
Nguyen and Tran [1] study the same path Artinian graph algebra through its weak Lefschetz property, under characteristic-zero hypotheses. Díaz, Liendo, Manzano-Flores and Regeta [2] establish a general description of automorphism groups of zero-dimensional monomial algebras in characteristic zero, including the role of homogeneous locally nilpotent derivations. Their general characteristic-zero theory is the closest structural antecedent; it does not determine the characteristic-two degree-one automorphism group in the present path family. The present claim isolates an explicit positive-characteristic jump in the graded group, rather than claiming the general theory or the odd-characteristic calculation as new.

## Limitations
The result is only about **graded** automorphisms, not arbitrary automorphisms of the local algebra. No scheme-theoretic smoothness assertion is made. Its proof is for paths on at least four labeled vertices; small paths can have different symmetry types. The finite-field enumerations do not constitute a complete computational proof for arbitrarily large \(n\) or \(q\). Exhaustive priority review of all graph-algebra automorphism literature has not been performed.

## References
[1] Hop D. Nguyen and Quang Hoa Tran, *The weak Lefschetz property of artinian algebras associated to paths and cycles*, arXiv:2310.14368, first public version October 22, 2023. https://arxiv.org/abs/2310.14368

[2] Roberto Díaz, Alvaro Liendo, Gonzalo Manzano-Flores and Andriy Regeta, *The Automorphism groups of zero-dimensional monomial algebras*, arXiv:2408.02197, first public version August 5, 2024. https://arxiv.org/abs/2408.02197

[3] Roberto Díaz, Giancarlo Lucchini Arteche and Gonzalo Manzano-Flores, *The structure of automorphism groups of zero-dimensional monomial algebras*, arXiv:2609.13741, first public version September 12, 2026. This later characteristic-zero work is contextual only, not the date-defining source. https://arxiv.org/abs/2609.13741
