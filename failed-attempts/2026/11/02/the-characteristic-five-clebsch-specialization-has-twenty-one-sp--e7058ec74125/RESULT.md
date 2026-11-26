# The characteristic-five Clebsch specialization has twenty-one split lines and an exceptional six-point action

## Finding
Let \(k=\mathbb F_5\) and let \(X\subset\mathbb P^4_k\) be the integral cubic surface
\[
\sum_{i=0}^4 X_i=\sum_{i=0}^4 X_i^3=0.
\]
Then \(X\) has precisely one geometric singularity, the ordinary double point \(P=[1:1:1:1:1]\). Its minimal resolution is the blowup of \(\mathbb P^2_k\) in six distinct \(k\)-rational points lying on a smooth \(k\)-conic; the strict transform of that conic is the unique exceptional \((-2)\)-curve. Exactly twenty-one geometric lines lie on \(X\), and **all twenty-one are defined over \(\mathbb F_5\)**. Fifteen are the coordinate-pairing lines, and the remaining six pass through \(P\).

The action of \(S_5\) on the six lines through \(P\) is its faithful six-point action on the six Sylow-five subgroups. Via the exceptional conic, it realizes the classical isomorphism \(S_5\simeq\operatorname{PGL}_2(\mathbb F_5)\). For every \(n\ge1\),
\[
\#X(\mathbb F_{5^n})=5^{2n}+6\cdot5^n+1,
\qquad
Z(X/\mathbb F_5,T)=\frac{1}{(1-T)(1-5T)^6(1-25T)}.
\]
This is a statement about the **singular integral-model specialization**; it does not posit a smooth Clebsch cubic in characteristic five. The existence of the characteristic-five singular point and the abstract six-point action are previously known; the specific split resolution, full arithmetic line descent, and zeta formula are the assessed contribution.

## Assumptions and scope
All schemes and point counts use the indicated coefficientwise model over \(\mathbb F_5\). Geometric statements hold after extension to \(\overline{\mathbb F}_5\). A 'line' means a geometrically reduced projective line contained in the cubic surface. The zeta function is the Hasse–Weil zeta function of the singular projective variety, not of its smooth resolution. The group \(S_5\) acts by permuting the five homogeneous coordinates.

## Proof
**1. Singularities.** A singular point on the hyperplane \(\sum X_i=0\) requires the gradients of the hyperplane and of \(\sum X_i^3\) to be dependent. Because \(3\neq0\), all squares \(X_i^2\) must agree. Over an algebraic closure, any nonzero such point has \(X_i=\pm a\). The number of plus signs minus the number of minus signs is one of \(\pm1,\pm3,\pm5\). The hyperplane condition in characteristic five forces all five signs to be equal. This gives only \(P\). (The common-square-zero case has no projective point.)

Set \(X_i=\lambda+u_i\) with \(u_4=0\), so the hyperplane condition becomes \(u_0+u_1+u_2+u_3=0\). Put
\[
Q=\sum_{i=0}^3u_i^2,\qquad R=\sum_{i=0}^3u_i^3.
\]
The exact homogeneous cubic equation becomes \(3\lambda Q+R=0\). The quadratic form \(Q\) is nondegenerate on the three-dimensional vector space \(\sum u_i=0\): the orthogonal complement of this hyperplane for the standard dot product is spanned by \((1,1,1,1)\), which does not belong to the hyperplane in characteristic five. Thus \(P=[\lambda:u]=[1:0:0:0]\) is an ordinary quadratic node (type \(A_1\)), with smooth projectivized tangent conic \(\{Q=0\}\subset\mathbb P^2\). As \(Q\) is irreducible and does not divide \(R\), the equation \(3\lambda Q+R\) is irreducible; the surface is integral and normal.

**2. Six rational base points and their symmetry.** Projection from \(P\) is the rational map \([\lambda:u]\mapsto[u]\) with inverse
\[
[u_0:u_1:u_2:u_3]\longmapsto[-R(u):3Q(u)u_0:3Q(u)u_1:3Q(u)u_2:3Q(u)u_3].
\]
Its base scheme is \(\{Q=R=0\}\) in \(\mathbb P^2\). Writing \(u_0=a,u_1=b,u_2=c,u_3=-a-b-c\) gives the polynomial identity
\[
R=-3(a+b)(b+c)(c+a).
\]
The smooth conic \(Q=0\) meets these three distinct lines in six distinct rational points, namely the six projective classes of \((a,b,c,u_3)\) obtained from permutations of \((1,2,3,4)\) with sum zero, modulo common affine rescaling. Equivalently, represent directions by five-tuples whose entries are \(0,1,2,3,4\) in some order, modulo \(u\sim a u+b(1,1,1,1,1)\) with \(a\in\mathbb F_5^\times\) and \(b\in\mathbb F_5\). Each point has a stabilizer of order \(5\cdot4=20\), the affine group \(\operatorname{AGL}_1(\mathbb F_5)\), and hence the six points are one \(S_5\)-orbit. In particular, the intersection is transverse and all six base points are geometrically reduced.

Blowing up the six simple base points resolves the inverse projection, giving a smooth surface \(Y=\operatorname{Bl}_{\{b_1,\ldots,b_6\}}\mathbb P^2\to X\). The strict transform \(E\) of \(Q=0\) has self-intersection \(4-6=-2\) and is contracted to \(P\); no other curve is contracted. (Indeed the cubic inverse map is the anticanonical linear system on \(Y\), and the only curve of anticanonical degree zero is this conic.) This is the minimal resolution of the sole \(A_1\) point.

The action of coordinate permutations descends to the plane of directions \(\{\sum_{i=0}^4u_i=0\}/\langle(1,1,1,1,1)\rangle\), preserving the tangent conic and its six rational base points. The stabilizer of one base point is the normalizer of its cyclic order-five subgroup, namely \(\operatorname{AGL}_1(\mathbb F_5)\). Consequently the action is conjugation on the six Sylow-five subgroups of \(S_5\), and is faithful (the only nontrivial proper normal subgroup is \(A_5\), which is not contained in a point stabilizer). Since every projective automorphism of the split smooth conic is in \(\operatorname{PGL}_2(\mathbb F_5)\), and both this group and \(S_5\) have order \(120\), this identifies the whole automorphism group of the conic with the six-point action. This last abstract group isomorphism is classical; its realization on the special fiber's exceptional conic is the geometry used here.

**3. All lines.** The six exceptional divisors of the plane blowup map to six distinct lines through \(P\). Fifteen further lines are explicitly given by
\[
L_{ij\mid kl}=\mathbb P\bigl(\operatorname{span}(e_i-e_j,e_k-e_l)\bigr),
\]
where \(\{i,j,k,l,m\}=\{0,1,2,3,4\}\), \(m\) is the zero coordinate and the remaining four indices are paired in one of three ways. All twenty-one are distinct and defined over \(\mathbb F_5\).

To prove geometric completeness without extrapolating finite enumeration, let \(L\) be a line not through \(P\). Its strict transform on \(Y\) is a smooth rational \((-1)\)-curve whose anticanonical degree is one. Write its class \(dH-\sum_{i=1}^6m_i E_i\), where \(d\ge1\) and \(m_i\ge0\). Adjunction and the anticanonical degree give
\[
\sum m_i=3d-1,\qquad\sum m_i^2=d^2+1.
\]
Cauchy–Schwarz implies \((3d-1)^2\le6(d^2+1)\), forcing \(d\le2\). For \(d=1\), exactly two multiplicities equal one, giving the fifteen lines through two base points. For \(d=2\), exactly five multiplicities equal one; the unique conic through any five of the six points is \(Q=0\), which passes through the sixth and hence cannot have the required irreducible strict-transform class. Therefore there are no further lines. Every line through the node comes from a solution of \(Q=R=0\), already the six identified above.

**4. Arithmetic and zeta.** Every blowup center is \(\mathbb F_5\)-rational, so for \(q=5^n\),
\[
\#Y(\mathbb F_q)=\#\mathbb P^2(\mathbb F_q)+6q=q^2+7q+1.
\]
The exceptional conic is split, with \(q+1\) points; contracting it replaces those points by the one rational point \(P\). Hence \(\#X(\mathbb F_q)=q^2+6q+1\). The displayed zeta function follows from its defining logarithmic generating series. The line-count and arithmetic claims follow for every extension.

## Verification
Run `python3 verify.py` using Python 3's standard library. The checker enumerates all \(156\) rational points of \(\mathbb P^3(\mathbb F_5)\), constructs the \(21\) rational lines on the cubic, verifies the six node-through lines and fifteen coordinate-pairing lines, enumerates the \(120\) distinct permutations induced by \(S_5\) on the six nodal lines, and counts \(56\) points over \(\mathbb F_5\) and \(776\) over \(\mathbb F_{25}\). Four rational points on any projective line suffice to certify vanishing of the degree-three restricted cubic over \(\mathbb F_5\). Its execution output is provided in `verify_output.txt`. The infinite-extension claims and geometric completeness are established by the preceding proof, not finite enumeration.

## Relationship to prior work
Clebsch and Klein introduced the symmetric cubic and its classical \(27\)-line/icosahedral geometry. Baez (2016) reviews its symmetric equations, six blown-up points, and the \(S_5\) action over characteristic zero. Trepalin (2015) describes the classical six-point \(A_5\)-equivariant blowup, including order-five subgroup stabilizers. Dolgachev and Duncan (2017, Section 12.1) specifically observe that the characteristic-five symmetric model is singular at \(P\) and exclude any smooth Clebsch cubic in characteristic five. The location of that singularity and the classical exceptional group isomorphism are therefore background, not originality claims. The exact resolution of the *specified singular arithmetic reduction* as a blowup of the six \(\mathbb F_5\) conic points, the exhaustive split \(21\)-line configuration, and its zeta function are the additional results assessed here.

## Limitations
This is a special arithmetic model, not a classification of every nodal cubic over finite fields. A known general \(A_1\)-surface line-count table alone gives the geometric number \(21\), but not that all lines descend to \(\mathbb F_5\) nor the six-point Galois action or the displayed zeta function. Sources searched did not identify an exact previously published statement of this joint arithmetic refinement; absence from searched material does not prove historical priority. No independent external validation has been performed.

## References
- A. Clebsch, *Ueber die Anwendung der quadratischen Substitution auf die Gleichungen 5ten Grades und die geometrische Theorie des ebenen Fünfseits*, Mathematische Annalen 4 (1871), 284–345, DOI: 10.1007/BF01442599. Historical complex-geometric background.
- F. Klein, *Ueber Flächen dritter Ordnung*, Mathematische Annalen 6 (1873), 551–581, DOI: 10.1007/BF01443196. Historical six-point icosahedral background.
- A. Trepalin, *Quotients of cubic surfaces*, arXiv:1506.05138v1 (16 June 2015), https://arxiv.org/abs/1506.05138. Characteristic-zero equivariant blowups.
- J. Baez, *Clebsch Surface*, AMS Visual Insight, 1 March 2016, https://blogs.ams.org/visualinsight/2016/03/01/clebsch-surface/.
- I. Dolgachev and A. Duncan, *Automorphisms of cubic surfaces in positive characteristic*, arXiv:1712.01167 (4 December 2017), Section 12.1, https://arxiv.org/abs/1712.01167. Known singular point and smooth-characteristic-five obstruction.
