# Maximal commutative subalgebras and exceptional equidimensional commuting varieties of rectangular-band algebras

## Finding
Let \(m,n\geq2\), let \(k\) be any field, and let \(A_{m,n}(k)\) be the \(mn\)-dimensional semigroup algebra with basis \(e_{ij}\) and multiplication
\[
e_{ij}e_{h\ell}=e_{i\ell}\qquad(1\leq i,h\leq m,\quad1\leq j,\ell\leq n).
\]
It is not assumed to have an identity. For a coefficient matrix \(X=(x_{ij})\), put \(r(X)_i=\sum_jx_{ij}\), \(c(X)_j=\sum_ix_{ij}\), and \(\epsilon(X)=\sum_{ij}x_{ij}\). Define
\[
W=\{X:r(X)=0,\ c(X)=0\},\quad
U=\{X:r(X)=0\},\quad V=\{X:c(X)=0\}.
\]
The two subalgebras \(U,V\) have zero multiplication. Set \(w=(m-1)(n-1)\) and \(d=m+n-1\).

**Classification of maximal commutative subalgebras.** The algebra \(W\) is the two-sided annihilator and center of \(A_{m,n}\). Every inclusion-maximal commutative \(k\)-subalgebra is precisely one of \(U\), \(V\), or \(\pi^{-1}(L)\), where \(\pi(X)=(r(X),c(X))\), and \(L\) ranges over one-dimensional subspaces of
\[
H=\{(r,c)\in k^m\oplus k^n:\mathbf1^Tr=\mathbf1^Tc\}
\]
whose two projections are both nonzero. All these subalgebras are distinct and self-centralizing. Their respective dimensions are \(w+n-1\), \(w+m-1\), and \(w+1\). In particular, the largest possible dimension is
\[
\boxed{mn-\min(m,n)}.
\]
Together with \(\dim_k A_{m,n}=mn\), the maximum commutative-subalgebra dimension recovers the unordered pair \(\{m,n\}\).

Over \(\mathbb F_q\), the exact number of inclusion-maximal commutative subalgebras is
\[
\boxed{2+\frac{q^{m+n-1}-q^{m-1}-q^{n-1}+1}{q-1}}.
\]

**All-arity commuting varieties.** For each integer \(t\geq2\), the reduced affine variety of ordered pairwise-commuting \(t\)-tuples in \(A_{m,n}\), over every algebraic closure of \(k\), is the union of the three closed loci
\[
\mathcal D_t=\{(X_a):\operatorname{rank}[\pi(X_1)\ \cdots\ \pi(X_t)]\leq1\},
\quad U^t,\quad V^t.
\]
The determinantal locus \(\mathcal D_t\) is geometrically irreducible of dimension \(wt+d+t-1\). The two coordinate-linear loci have dimensions \(t(w+n-1)\) and \(t(w+m-1)\), respectively. The *geometrically irreducible components* are \(\mathcal D_t\), together with \(U^t\) if \(n\geq3\), and \(V^t\) if \(m\geq3\). Hence the number of components is
\[
\boxed{1+\mathbf1_{n\geq3}+\mathbf1_{m\geq3}}.
\]
The variety is geometrically equidimensional exactly in the following cases (up to interchange of \(m,n\)):
\[
\boxed{m=n=2\text{ with any }t\geq2;\quad
(m,n,t)=(2,3,3),(2,4,2),(3,3,4),(4,4,3).}
\]
There is no assertion here that the unreduced commutator equation *scheme* is reduced.

For every finite field \(\mathbb F_q\) and every integer \(t\geq1\), the exact number of ordered commuting \(t\)-tuples is
\[
\boxed{q^{wt}\left[q^{t(n-1)}+q^{t(m-1)}-1+
\frac{q^{m+n-1}-q^{m-1}-q^{n-1}+1}{q-1}(q^t-1)\right].}
\]
Even though distinct elements of the underlying rectangular band never commute, its linearized algebra therefore contains two large zero-product commutative subalgebras and an entire projective family of further maximal commutative subalgebras.

## Assumptions and scope
Here \(A_{m,n}\) means the *ordinary nonunital semigroup algebra* of the rectangular band \(\{1,\ldots,m\}\times\{1,\ldots,n\}\). Its multiplication is not ordinary matrix multiplication. All sums are in \(k\), including positive characteristic. A commutative subalgebra is a \(k\)-linear associative subalgebra in which all pairs commute; it need not contain an identity. The commuting variety is defined set-theoretically by the polynomial commutator equations and then given its reduced algebraic-variety structure. Geometric irreducibility is assessed after extension to an algebraic closure. Finite-field formulas hold for all prime powers, not just prime fields.

## Proof
**1. The quotient by the annihilator.** Bilinearity of the basis multiplication gives
\[
XY=r(X)c(Y)^T,\qquad
[X,Y]=r(X)c(Y)^T-r(Y)c(X)^T.
\]
Here the right side is interpreted as a coefficient matrix of an element of \(A_{m,n}\). Its row sums are \(\epsilon(Y)r(X)-\epsilon(X)r(Y)\), and its column sums are \(\epsilon(X)c(Y)-\epsilon(Y)c(X)\). The map \(\pi:A_{m,n}\to H\) is a surjective linear map: for a prescribed pair \((r,c)\in H\), choose a coefficient matrix with entries \(x_{i,n}=r_i\) for \(i<m\), \(x_{m,j}=c_j\) for \(j<n\), and \(x_{m,n}=r_m-\sum_{j<n}c_j\), with all other entries zero. Consequently \(\ker\pi=W\) has dimension \(mn-(m+n-1)=w\). Every element of \(W\) annihilates the algebra on both sides. Conversely, if \(X\) commutes with every element, its commutators with all elements of \(U\) force \(r(X)=0\), and its commutators with all elements of \(V\) force \(c(X)=0\), since \(m,n\geq2\). Hence \(W\) is exactly the center as well.

**2. Centralizers of noncentral elements.** Let \(h=(r,c)\in H\), with both \(r\) and \(c\) nonzero. If another profile \(h'=(r',c')\) satisfies \(rc'^T=r'c^T\), equality of the two rank-one tensors implies \(h'=\lambda h\) for a unique \(\lambda\in k\), allowing \(\lambda=0\). Indeed, a nonzero coordinate of \(r\) first makes \(c'\) a scalar multiple of \(c\), then a nonzero coordinate of \(c\) forces the same scalar for \(r'\). Thus the centralizer of any lift of \(h\) is exactly \(\pi^{-1}(kh)\).

If \(h=(0,c)\) with \(c\ne0\), its centralizer consists exactly of the elements whose row profile vanishes, namely \(U\). Dually, the centralizer of a nonzero \((r,0)\) is \(V\). For a lift \(X\) of a mixed line, observe that \(\pi(X^2)=\epsilon(X)\pi(X)\). It follows that \(\pi^{-1}(kh)\) is closed under multiplication, since \(W\) annihilates all elements. Both \(U\) and \(V\) multiply identically to zero by the multiplication formula. Each is therefore a commutative subalgebra equal to its own centralizer.

Any maximal commutative subalgebra contains \(W\), since \(W\) is central. Its profiles form a linear subspace of pairwise-commuting points of \(H\). If the subspace contains a mixed vector, the entire subspace lies on its line, so maximality gives \(\pi^{-1}(kh)\). Otherwise every nonzero vector is pure of one of the forms \((r,0)\) or \((0,c)\). Both forms cannot coexist in a commuting subspace, since their nonzero outer product would prevent commutation. Thus maximality yields \(U\) or \(V\). This proves classification, distinctness, dimensions and the maximum \(w+\max(m-1,n-1)=mn-\min(m,n)\).

**3. Commuting-tuples decomposition.** Apply the same mixed-versus-pure argument to the profiles of an arbitrary ordered commuting \(t\)-tuple. Either a mixed profile exists and every profile is proportional to it, or all nonzero profiles are purely of row type, or all are purely of column type. Thus the set of commuting tuples is exactly \(\mathcal D_t\cup U^t\cup V^t\). A linear section of \(\pi\) gives an affine-space isomorphism of \(\mathcal D_t\) with \(W^t\) times the rank-at-most-one determinantal variety of \(d\)-by-\(t\) matrices. This is irreducible: it is the image closure of the polynomial parameterization \((a,b)\mapsto ab^T\) from \(\mathbb A^d\times\mathbb A^t\); its nonzero part has one-dimensional scaling fibers, so its dimension is \(d+t-1\). The pure loci are linear spaces of the stated dimensions.

The determinantal locus does not lie in either pure locus because it contains mixed lines. If \(n=2\), all profiles in \(U\) lie in a one-dimensional subspace of \(H\), so \(U^t\subseteq\mathcal D_t\). If \(n\geq3\), its profile space has dimension at least two and \(t\geq2\), hence \(U^t\not\subseteq\mathcal D_t\). The same argument with \(m\) handles \(V^t\). Neither pure locus contains the other. This proves the complete component list over every algebraic closure.

**4. Equidimensionality.** The component dimensions, after subtracting the common \(wt\), are \(m+n+t-2\), \(t(n-1)\) when \(n\geq3\), and \(t(m-1)\) when \(m\geq3\). If \(m=n=2\), only the first component exists. If \(m=2<n\), equality of the two existing dimensions is \(t(n-2)=n\), whose integer solutions for \(n\geq3,t\geq2\) are exactly \((n,t)=(3,3),(4,2)\). If \(m,n\geq3\), equality of the pure dimensions forces \(m=n=a\); equality with the determinantal dimension is then \(t(a-2)=2(a-1)\), whose solutions for \(a\geq3,t\geq2\) are exactly \((a,t)=(3,4),(4,3)\). This proves the complete exceptional list.

**5. Finite-field arithmetic.** The number of profiles in \(H(\mathbb F_q)\) is \(q^d\). There are \(q^{n-1}\) with zero row, \(q^{m-1}\) with zero column, and one with both zero, so exactly \(q^d-q^{n-1}-q^{m-1}+1\) mixed profiles. Scalar multiplication is free on their nonzero vectors, yielding the displayed number of mixed lines. For a commuting ordered \(t\)-tuple of profiles, the pure-row family has \(q^{t(m-1)}\) points and the pure-column family has \(q^{t(n-1)}\); they intersect only at the zero tuple. Every mixed line contributes \(q^t-1\) nonzero \(t\)-tuples, and these contributions are disjoint from one another and from the pure families. Every tuple of profiles has exactly \(q^{wt}\) lifts. Multiplication proves the asserted finite-field formula. The same count of mixed lines, plus the two pure subalgebras, gives the maximal-commutative-subalgebra count.

## Verification
The standalone standard-library program `verify.py` constructs literal coefficient matrices and multiplies each pair directly from the table \(e_{ij}e_{h\ell}=e_{i\ell}\). It separately computes row and column profiles and checks the correspondence. It independently enumerates commuting tuples through arity four in selected prime fields, checks the three-locus membership, and tests the exact point-count formula. Finally, it exhaustively enumerates *maximal cliques from direct multiplication*, proving agreement in the tested small cases with the predicted maximal commutative subalgebras and checking linear/multiplicative closure. Run `python3 verify.py` from the directory containing this report. The program is finite experimental corroboration, not the infinite proof above.

## Relationship to prior work
The decomposition of a rectangular band into left-zero and right-zero factors is classical. Choi, Gourdeau and White (2010 preprint) use rectangular-band algebras as building blocks in the study of cyclic and simplicial cohomology; they do not give the finite-field commuting-tuple decomposition. Nagy and Zubor (2015 preprint) analyze congruences and ideals of semigroup algebras of permutable rectangular bands, not the arbitrary-size commutative-subalgebra geometry. The article *Commuting graphs of Rees matrix semigroups* concerns commuting elements of the **semigroup**, rather than the linearized semigroup algebra; in a rectangular band, distinct semigroup basis elements do not commute. The present theorem instead characterizes all maximal commutative *linear subalgebras* and geometric components and counts tuples over arbitrary finite fields. A different nilpotent block-matrix commuting-variety model has analogous rank-one equations, but its multiplication is nilpotent and its parameter space has no common-augmentation constraint; that result does not directly imply this theorem.

## Limitations
This theorem does not describe the nilpotent or embedded structure of the unreduced commutator scheme, commuting tuples of arbitrary Rees matrix algebras, or the automorphism group of the algebra. It assumes both band-factor sizes are at least two and treats the semigroup algebra without an adjoined identity. The finite checks use selected small *prime* fields; the proof handles every field and every prime power. A covering older result phrased in terms of rank-one sandwich algebras could still exist, despite the comparisons made here; no exhaustive priority guarantee is asserted.

## References
1. Y. Choi, F. Gourdeau, M. C. White, *Simplicial cohomology of band semigroup algebras*, arXiv:1004.2301 (first submitted 14 April 2010), especially Sections 1–3.
2. A. Nagy and M. Zubor, *A Note on Semigroup Algebras of Permutable Semigroups*, arXiv:1511.08671 (first submitted 27 November 2015), especially Theorem 2 and Corollary 2.
3. *Commuting graphs of Rees matrix semigroups*, Semigroup Forum, DOI:10.1007/s00233-025-10597-0, especially Lemma 3.13 and Theorem 3.14 (semigroup-level comparison only).
