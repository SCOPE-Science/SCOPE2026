# A single unitary orbit of degree-three points outside the generators of a Hermitian surface

## Finding
Let \(q\ge 2\) be any prime power, \(F=\mathbb F_{q^2}\), \(K=\mathbb F_{q^6}\), and
\[
X:\quad x_0^{q+1}+x_1^{q+1}+x_2^{q+1}+x_3^{q+1}=0\ \subset \mathbf P^3_F.
\]
Let \(D\) be the *reduced* union of **all** \((q^3+1)(q+1)\) geometric lines on \(X\), and \(U=X\setminus D\). The full generator configuration is defined over \(F\).

**Theorem.** There are no points on \(U\) of extension degree at most two over \(F\). The nonempty set \(U(K)\) is a single orbit of \(\operatorname{PGU}(4,q)\), and every stabilizer is **cyclic of order \(q^3+1\)**. In particular,
\[
\#U(K)=q^6(q^2-1)(q^4-1)
       =(q^6-q^2)(q^6-q^4).
\]
Thus the first closed points of \(U\) have degree three, in number \(q^6(q^2-1)(q^4-1)/3\).

Each such geometric degree-three point has a unique \(F\)-rational plane through it, namely the span of its three Frobenius conjugates; that plane is a non-tangent section of \(X\). The number of these planes is \(q^3(q-1)(q^2+1)\); each has exactly \(q^3(q+1)(q^2-1)\) points in \(U(K)\). Consequently these planes partition \(U(K)\) into explicit smooth Hermitian-curve fibers.

As an arithmetic corollary, for every integer \(n\ge 1\), with \(Q=q^{2n}\),
\[
\#U(\mathbb F_{q^{2n}})=(Q-q^2)(Q-q^4), \qquad
Z(U/F,T)=\frac{(1-q^2 T)^{q^2+q^4}}{(1-q^4T)(1-T)^{q^6}}.
\]
The orbit and cyclic-stabilizer statement is the principal structural assertion; the extension-count corollary is obtained from classical Hermitian point and line data.

## Assumptions and scope
All points are geometric/projective points of the smooth Hermitian surface over the specified finite extensions. A generator means a projective line wholly contained in \(X\); there are no other geometric lines. The finite unitary group acts through its standard \(F\)-linear projective action. In the stabilizer calculation, \(\operatorname{PGU}(4,q)\) denotes the projective image of \(\operatorname U(4,q)\), which equals the projective similitude group because Hermitian similitude factors are norms. Extension degree is taken over \(F\), not over \(\mathbb F_q\).

## Proof
**1. Why generators account for all points through degree two.** For a projective \(F\)-rational line \(L\), the Hermitian equation restricts to a binary Hermitian form of rank zero, one or two. In rank zero, \(L\) is a generator. Otherwise its geometric zero set consists respectively of one or \(q+1\) points, all defined over \(F\): diagonalize the binary Hermitian form over \(F\), and solve the resulting norm equation. Every \(F\)-rational point of \(X\) lies on \(q+1\) generators. If \(P\in X(\mathbb F_{q^4})\setminus X(F)\), the line joining \(P\) and its \(q^2\)-Frobenius conjugate is \(F\)-rational (the span descends under the order-two Galois action). Since it contains a point not in \(X(F)\), it must be a generator. This proves \(U(F)=U(\mathbb F_{q^4})=\varnothing\).

**2. A canonical plane for degree-three points.** Let \(P=[v]\in U(K)\), let \(\sigma(a)=a^{q^2}\), and put \(v_i=\sigma^i(v)\) for \(0\le i\le2\). Their \(K\)-linear span is stable under \(\sigma\) and hence descends to an \(F\)-subspace. If it had dimension at most two, its projectivization would be an \(F\)-line contained in \(X\) or meeting \(X\) only at \(F\)-points, a contradiction. Therefore the three \(v_i\) are independent and span a unique \(F\)-rational projective plane \(H_P\).

Write \(h(a,b)=\sum_{j=0}^3 a_j^q b_j\), considered as a \(q\)-semilinear form on \(K^4\). Since \(P\in X(K)\), the cyclic pairings
\[
h(v_0,v_1)=h(v_1,v_2)=h(v_2,v_0)=0.
\]
The remaining pairings are \(h(v_1,v_0)=c\), \(h(v_2,v_1)=c^{q^2}\), and \(h(v_0,v_2)=c^{q^4}\), with \(c=\sum_jv_j^{q^3+1}\in\mathbb F_{q^3}\). If \(c=0\), their three-dimensional span is totally isotropic for the nondegenerate \(q\)-semilinear form, which is impossible: its orthogonal complement has dimension one. Hence \(c\ne0\). The Gram determinant is nonzero, so the descended plane is nondegenerate for the ordinary Hermitian form over \(F\), and \(H_P\cap X\) is a smooth Hermitian plane curve.

**3. Transitivity.** The norm map \(K^\times\to\mathbb F_{q^3}^\times\), \(a\mapsto a^{q^3+1}\), is onto. Rescale \(v\) so that \(c=1\). For two normalized points \([v],[w]\in U(K)\), the unique \(K\)-linear transformation sending each \(v_i\) to \(w_i\) commutes with the \(q^2\)-Frobenius descent data. It therefore defines an \(F\)-linear isometry between their nondegenerate three-dimensional Hermitian subspaces, because their full Gram matrices coincide. Extend it to an isometry of \(F^4\) by choosing an isometry of the one-dimensional orthogonal complements (all nondegenerate Hermitian lines over \(F\) are isometric). The induced element of \(\operatorname{PGU}(4,q)\) sends \([v]\) to \([w]\), proving transitivity.

**4. Cyclic stabilizer.** If a unitary transformation fixes \([v]\), then it sends \(v\mapsto t v\) for some \(t\in K^\times\) and consequently \(v_i\mapsto t^{q^{2i}}v_i\). Preservation of \(h(v_1,v_0)=1\) forces \(t^{q^3+1}=1\). Conversely, every such \(t\) defines a descended isometry of the span of the \(v_i\), and independently the orthogonal Hermitian line may be multiplied by any \(s\) with \(s^{q+1}=1\). On passing to the projective group the diagonal center of order \(q+1\) is removed, leaving
\[
(\mu_{q^3+1}\times\mu_{q+1})/\mu_{q+1}^{\mathrm{diag}}\cong\mu_{q^3+1},
\]
a cyclic group of exact order \(q^3+1\). The classical group order \(\#\operatorname{PGU}(4,q)=q^6(q^2-1)(q^3+1)(q^4-1)\) yields the asserted orbit cardinality.

**5. Planes and extension counts.** There are \(q^6+q^4+q^2+1\) \(F\)-planes in \(\mathbf P^3\). Precisely \((q^3+1)(q^2+1)\) are tangent planes, indexed by the \(F\)-points of \(X\), so exactly \(q^3(q-1)(q^2+1)\) have a smooth Hermitian curve section. Such a section has genus \(q(q-1)/2\), and its maximality gives \(q^3+1\) points over \(F\) and \(q^6+1+q^4(q-1)\) over \(K\). Every extra point lies off all generators, and its unique plane is the section plane. Their difference is \(q^3(q+1)(q^2-1)\), proving the partition and count independently.

For the last corollary, the number of \(F\)-points of \(X\) is \((q^3+1)(q^2+1)\), saturating the Weil bound for its middle cohomology of rank \(q^3-q^2+q+1\). Hence all degree-two Frobenius eigenvalues are \(q^2\) and \(\#X(\mathbb F_{q^{2n}})=Q^2+(q^3-q^2+q+1)Q+1\). Every generator is \(F\)-defined and the distinct generators intersect only at \(F\)-points. Counting these incidence intersections gives \(\#D(\mathbb F_{q^{2n}})=(q^3+1)(q+1)Q+1-q^6\). Subtraction gives \(\#U=(Q-q^2)(Q-q^4)\). The zeta product follows by the defining exponential series \(Z(U/F,T)=\exp(\sum_{n\ge1}\#U(\mathbb F_{q^{2n}})T^n/n)\).

## Verification
The standalone standard-library program `verify.py` constructs \(\mathbb F_{64}=\mathbb F_2[z]/(z^6+z+1)\), enumerates every projective point on the Hermitian cubic surface over \(\mathbb F_{64}\), calculates the rank of each triple of \(\mathbb F_4\)-Frobenius conjugates, and searches all \(85\) \(\mathbb F_4\)-planes. The check returns \(4545\) points, conjugate-rank profile \(45,1620,2880\), and exactly \(40\) non-tangent planes each carrying \(72\) of the rank-three points. These tests confirm the small-field incidence and descent arithmetic, not the general group-theoretic proof, which is given above.

Reproduce with `python3 verify.py` in a directory containing the standalone file, using Python's standard library only.

## Relationship to prior work
Brosowsky–Page–Ryan–Smith (2021, arXiv:2110.15908v1), Sections 3–4, establishes the generator and star-point configuration and unitary automorphism group of smooth Hermitian/extremal surfaces, including the counts used here. Homma–Kim (arXiv:1304.0302) characterizes Hermitian surfaces through the number of rational points. Montanucci–Zini (arXiv:1804.03398v1) analyzes Hermitian **curves** and unitary subgroups associated with Frobenius triangles, not the degree-three generator complement on a Hermitian **surface**. The established generator incidence, maximal point counts, and group order are not claimed as new; the contribution examined here is the single degree-three projective-unitary orbit with explicit cyclic stabilizer and canonical smooth-section partition.

## Limitations
This describes one distinguished smooth Hermitian surface and its intrinsic generator complement, not arbitrary smooth degree-\(q+1\) surfaces or their twists. The extension-count corollary follows from classical data, rather than being an independent novelty claim. Historical-priority risk remains for older finite-polar-geometry orbit classifications; the checked primary sources did not exhibit the precise degree-three surface orbit, but the literature search is not exhaustive. No independent mathematical audit has been performed.

## References
Brosowsky, A.; Page, J.; Ryan, T.; Smith, K. E., *Geometry of Smooth Extremal Surfaces*, arXiv:2110.15908v1 (first submitted 2021-10-29), https://arxiv.org/abs/2110.15908.

Montanucci, M.; Zini, G., *Quotients of the Hermitian curve from subgroups of PGU(3,q) without fixed points or triangles*, arXiv:1804.03398v1 (2018), https://arxiv.org/abs/1804.03398.

Homma, M.; Kim, S. J., *The characterization of Hermitian surfaces by the number of points*, arXiv:1304.0302, https://arxiv.org/abs/1304.0302.

Napolitano, V., *A new combinatorial characterization of (quasi)-Hermitian surfaces*, J. Geom. 114 (2023), article 19, doi:10.1007/s00022-023-00681-7.
