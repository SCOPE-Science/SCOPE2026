# Exact higher nilpotent commuting-tuple counts in the rank-one Witt algebra

## Finding

Let \(p\ge5\) be prime, let \(q=p^f\) with \(f\ge1\), and let \(m\ge3\). Put \(A=\mathbb F_q[t]/(t^p)\), \(W=\operatorname{Der}_{\mathbb F_q}(A)=A\partial\), where \(\partial(t)=1\), and \(\mathcal N=\{D\in W:D^p=0\}\). Let \(C_m(p,q)\) count ordered tuples \((D_1,\ldots,D_m)\in\mathcal N^m\) for which \([D_i,D_j]=0\) for all \(i,j\). Define \(h=(p-1)/2\). Then

\[
\boxed{C_m(p,q)=q^{p-2}(q^m-1)+q^{mh}+\sum_{k=2}^{h}q^{p-2k}(q^{mk}-q^{m(k-1)})}.
\]

The same stratification proves that the affine variety of ordered, pairwise commuting \(m\)-tuples of restricted-nilpotent elements in the rank-one Witt algebra over an algebraically closed field of characteristic \(p\) has dimension exactly \(mh+1\) for \(m\ge3\). This differs from the previously established dimension \(p\) for the two-tuple commuting variety. The theorem concerns higher tuples; the \(m=2\) specialization is a compatibility check, not claimed to be a new two-tuple result.

For instance, for \(p=q=5\) the respective higher-tuple counts are \(C_3(5,5)=108625\) and \(C_4(5,5)=2418625\); the familiar two-tuple specialization is \(C_2(5,5)=6625\).

## Assumptions and scope

All Lie brackets and derivation powers are taken in characteristic \(p\). For nonzero \(f\in A\), write \(\nu(f)\) for the least degree of a nonzero coefficient, and let \(\nu(0)=p\). Thus every derivation is uniquely \(D=f\partial\), with bracket \([f\partial,g\partial]=(fg'-gf')\partial\). The restricted map on derivations is ordinary \(p\)-fold composition. The finite-field count is for each prime-power field in characteristic \(p\), and the dimension statement concerns the affine reduced algebraic variety over an algebraically closed field of that characteristic. Every tuple is ordered and zero entries are permitted. No assumption is made that its nonzero entries are linearly independent.

## Proof

**1. The restricted-nilpotent locus.** If \(\nu(f)=1\), then \(f\partial\) acts as multiplication by a nonzero scalar on the one-dimensional quotient \((t)/(t^2)\), so it is not nilpotent. If \(\nu(f)\ge2\), the derivation strictly raises the degree filtration and hence is nilpotent, with \((f\partial)^p=0\) on the \(p\)-dimensional algebra.

If \(f(0)\ne0\), \(f\partial\) has one-dimensional kernel (the constants) and rank \(p-1\). It is nilpotent exactly when there is an element \(u\in A\) with \((f\partial)(u)=1\), equivalently \(u'=f^{-1}\). To see the necessity, nilpotency plus kernel dimension one gives a single length-\(p\) Jordan block whose kernel is the line of constants and lies in the image. For sufficiency, the derivative equation forces \(u'(0)=f(0)^{-1}\ne0\), so substitution \(t\mapsto u\) is an automorphism of the local truncated polynomial algebra; in coordinate \(u\), the derivation becomes \(\partial_u\) and is nilpotent. In characteristic \(p\), \(u'=f^{-1}\) is solvable exactly when the coefficient of \(t^{p-1}\) in \(f^{-1}\) is zero. Inversion permutes the units of \(A\), so there are precisely \((q-1)q^{p-2}\) restricted-nilpotent derivations with unit coefficient. These form \(q^{p-2}\) one-dimensional scalar directions.

**2. Unit directions.** For a unit \(f\), the relation \([f\partial,g\partial]=0\) is equivalent to \((g/f)'=0\). The derivative has kernel only the constants on \(A\), so the centralizer of \(f\partial\) is the line \(\mathbb F_q f\partial\). Hence a commuting tuple with at least one unit coefficient occupies one uniquely determined restricted-nilpotent scalar line, and there are \(q^m-1\) tuples on each such line that contain a nonzero entry. This contributes \(q^{p-2}(q^m-1)\).

**3. Low-order centralizers.** Fix an element \(D=f\partial\) with \(2\le k=\nu(f)\le h\), and write \(J_k=t^{p-k+1}A\partial\), of dimension \(k-1\). Directly from the bracket, all elements of \(J_k\) commute with \(D\), and \(J_k\) itself is abelian. Conversely, suppose \(g\partial\) commutes with \(D\). If the least nonzero degree \(\ell=\nu(g)\) is below \(p-k+1\), then the lowest bracket term has nonzero coefficient \((\ell-k)f_k g_\ell\), unless \(\ell=k\). Here the difference cannot vanish modulo \(p\), since its absolute value is less than \(p\). If \(\ell=k\), subtract \((g_k/f_k)f\) to increase the valuation, and repeat. Consequently every commuting coefficient \(g\) belongs to \(\mathbb F_q f+t^{p-k+1}A\); the converse has already been checked. Therefore

\[
Z_W(D)=\mathbb F_qD\oplus J_k,
\qquad \dim Z_W(D)=k,
\]

and this centralizer is abelian. It depends only on the one-dimensional quotient direction determined by \(f\) in \(t^kA/t^{p-k+1}A\), rather than on the particular nonzero multiple or its high-order tail.

**4. Count disjoint low-order strata.** Consider a tuple all of whose nonzero entries have coefficients divisible by \(t^2\), and whose smallest positive valuation is \(k\) with \(2\le k\le h\). Choosing any entry of valuation \(k\) determines the same unique abelian centralizer \(H=\mathbb F_qD\oplus J_k\) containing every entry of the tuple. Two distinct centralizers with this minimal valuation cannot yield the same tuple. Their possible directions are represented by polynomials beginning in degree \(k\), modulo \(t^{p-k+1}\), normalized to leading coefficient one; there are exactly \(q^{p-2k}\) such directions. Within each \(H\) there are \(q^{mk}\) ordered \(m\)-tuples, exactly \(q^{m(k-1)}\) of which lie entirely in \(J_k\) and therefore have strictly higher minimum valuation. Thus the exact stratum count is \(q^{p-2k}(q^{mk}-q^{m(k-1)})\).

**5. High-order stratum.** The subspace \(J=t^{h+1}A\partial\), of dimension \(h\), is abelian: the degree of every bracket term is at least \(2(h+1)-1=p\), so the bracket vanishes in \(A\). Its elements are all restricted-nilpotent. Its ordered \(m\)-tuple contribution is \(q^{mh}\). The unit directions, low-order strata, and high-order stratum are pairwise disjoint and exhaustive, proving the formula.

**6. Dimension.** The counting strata have algebraic parameterizations over an algebraic closure: unit-line tuples form an open subset of \(\mathbb A^{p-2}\times\mathbb A^m\), of dimension \(p-2+m\); the high-order tuples form \(\mathbb A^{mh}\); and each low-order \(k\)-stratum is parameterized by an affine direction space \(\mathbb A^{p-2k}\) and the complement of \(\mathbb A^{m(k-1)}\) inside \(\mathbb A^{mk}\), of dimension \(p-2k+mk\). The parameterizations are bijective on points and have explicit coefficientwise inverses on the strata, so these are their geometric dimensions. For \(m\ge3\), this last expression increases strictly with \(k\); at \(k=h\) it is \(mh+1\), which exceeds both \(mh\) and \(p-2+m\) because \(h\ge2\). The finite disjoint stratification therefore has total dimension \(mh+1\).

## Verification

A standalone dependency-free verifier (`verify_witt_commuting_tuples.py`) independently builds all derivation matrices and checks the restricted-nilpotent test by matrix powers. It counts commuting pairs and, using adjacency intersections rather than the closed formula, all commuting triples and quadruples. Exhaustive calculations passed at \((p,q)=(5,5)\), with additional boundary checks at \((3,3)\) and at the genuine extension field \((3,9)\). For \((5,5)\), the exhaustive counts for arities one through four were \(625,6625,108625,2418625\). The verification ends with `VERIFY_OK_WITT_ALL_ARITY_NILPOTENT_COMMUTING`. Finite checks corroborate but do not prove the arbitrary-prime-power and unbounded-arity theorem.

## Relationship to prior work

Evans and Fuchs study the restricted power operation in the Witt algebra, supplying classical background for the nilpotence condition. Yao and Chang (arXiv:1301.5667, Lemma 2.3, Lemma 3.3, Theorem 3.6) determine centralizers and irreducible components and dimension for the **two-element** nilpotent commuting variety in characteristic greater than three. The present proof explicitly uses and rederives the crucial centralizer pattern; neither that paper's theorem nor the cited restricted-power work gives a finite-field formula for ordered commuting tuples of arbitrary arity \(m\ge3\). The passage from two elements to arbitrary arity requires a non-overlapping count of shared low-valuation centralizers and a comparison of the dimensions of all such strata. In particular, the known two-tuple dimension \(p\) is not being represented as a new result.

## Limitations

The theorem is for the rank-one Witt algebra and primes \(p\ge5\), and counts pairwise commuting tuples in the restricted-nilpotent cone rather than arbitrary nilpotent matrices or commuting tuples in higher-rank Cartan-type algebras. It does not determine irreducible components, scheme singularities, or point counts over rings. An equivalent higher-tuple count under older terminology cannot be ruled out by finite bibliographic searching. Although small cases were exhaustively verified, the universal claim depends on the preceding proof.

## References

- T. Evans and D. Fuchs, *On the Restricted Lie Algebra Structure for the Witt Lie Algebra in Finite Characteristic*, arXiv:math/0111271v1, first posted 2001-11-27. https://arxiv.org/pdf/math/0111271
- Y.-F. Yao and H. Chang, *Nilpotent Commuting Varieties of the Witt Algebra*, arXiv:1301.5667v1, first posted 2013-01-23. https://arxiv.org/pdf/1301.5667
- A. Premet, *Regular Derivations of Truncated Polynomial Rings*, arXiv:1405.2426, first posted 2014-05-10. https://arxiv.org/pdf/1405.2426
