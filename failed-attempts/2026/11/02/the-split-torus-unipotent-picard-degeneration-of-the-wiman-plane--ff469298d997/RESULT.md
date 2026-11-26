# The split torus–unipotent Picard degeneration of the Wiman plane sextic in characteristic three

## Finding
Let \(k=\mathbb F_3\) and let \(C\subset\mathbb P^2_k\) be the projective plane curve cut out by the reduction modulo \(3\) of Wiman's classical sextic equation
\[
F=X^6+Y^6+Z^6+(X^2+Y^2+Z^2)(X^4+Y^4+Z^4)-12X^2Y^2Z^2.
\]
Then \(C\) is a reduced curve with exactly five geometrically irreducible components: the smooth conic \(Q=X^2+Y^2+Z^2=0\) and the four lines \(L_1=X+Y+Z=0\), \(L_2=X+Y-Z=0\), \(L_3=X-Y+Z=0\), and \(L_4=-X+Y+Z=0\). Each line is tangent to \(Q\) at a distinct \(\mathbb F_3\)-point. The six pairwise intersections of the lines are distinct split ordinary nodes, disjoint from the conic; the four conic-line contacts are split tacnodes (analytic type \(A_3\)). There are no other singularities. The five-vertex dual graph is \(K_5\), with the four conic-line edges having intersection multiplicity two and the other six edges multiplicity one.

The connected degree-zero Picard group of this **specified reduced plane model**, as a smooth commutative \(\mathbb F_3\)-group scheme, is
\[
\operatorname{Pic}^0_{C/k}\cong\mathbb G_m^6\times\mathbb G_a^4.
\]
Consequently, for every integer \(m\geq1\), with \(q=3^m\),
\[
\#C(\mathbb F_q)=5q-5,\qquad
Z(C/\mathbb F_3,T)=\frac{(1-T)^5}{(1-3T)^5},\qquad
\#\operatorname{Pic}^0_{C/k}(\mathbb F_q)=(q-1)^6q^4.
\]
In particular the four ordinary double points of the characteristic-zero model specialize to the four tacnodes of this particular integral plane equation, while six new ordinary nodes appear.

## Assumptions and scope
All equations are homogeneous in \([X:Y:Z]\), and all assertions about irreducibility and singularities are geometric after base change to \(\overline{\mathbb F}_3\). The polynomial defines a flat degree-six Cartier divisor over the prime-local integer base because its homogeneous coefficients are primitive; the conclusion concerns the plane-model special fiber, **not** an asserted stable or regular model of the smooth genus-six normalization. Here \(\operatorname{Pic}^0\) means the identity component of the Picard scheme of this reduced connected projective curve. The zeta function counts points of the **reduced** scheme; its normalization is the disjoint union of five rational curves.

## Proof
**1. Factorization.** In characteristic \(3\), the freshman's dream gives \(X^6+Y^6+Z^6=(X^2+Y^2+Z^2)^3\), and the last term of \(F\) disappears. Direct expansion in \(\mathbb F_3[X,Y,Z]\) yields the *polynomial identity*
\[
F=Q L_1L_2L_3L_4.
\]
The linear forms are pairwise nonproportional; \(Q\) is nonsingular because its three partial derivatives are \(2X,2Y,2Z\), which cannot vanish simultaneously at a projective point. Thus the five components are reduced, distinct, smooth, and defined over \(k\).

**2. Intersections and local analytic types.** Write \(r_i=(a_i,b_i,c_i)\) for the coefficient vector of \(L_i\). Each has coordinates in \(\{1,-1\}\) and satisfies \(Q(r_i)=3=0\). The tangent line to \(Q\) at \([r_i]\) is exactly \(L_i=0\), so Bezout's theorem gives intersection multiplicity two at \([r_i]\), with no other intersections of \(Q\) and \(L_i\). These four points are distinct and none lies on another \(L_j\). Every pair of different lines intersects in one \(k\)-rational point with one coordinate zero and the other two nonzero; there are exactly six different such points. None lies on \(Q\), since \(Q=2\ne0\) at any such point after scaling. Therefore these six points are transverse ordinary nodes and there is no triple intersection. At a conic-line contact the conic is smooth with order-two tangency, so the completed local equation over \(\overline k\) is analytically equivalent to \(v(v-u^2)=0\), a split \(A_3\) tacnode. All singularities are these ten intersections. The four points \([1:1:1]\), \([1:1:-1]\), \([1:-1:1]\), and \([-1:1:1]\) are exactly the four classical nodes of the generic plane model, and here become the four contacts.

**3. Arithmetic genus and local Picard defects.** At an ordinary node the normalization quotient has length \(\delta=1\), and its local unit quotient is \(\mathbb G_m\). At a tacnode the completed local ring embeds into its two-branch normalization as
\[
\{(f(u),g(u))\in k[[u]]\oplus k[[u]]: f\equiv g\pmod{u^2}\}.
\]
The normalization quotient has length \(\delta=2\), and the unit quotient is \((k[u]/u^2)^\times\cong\mathbb G_m\times\mathbb G_a\): write each invertible jet uniquely as \(c(1+du)\). Consequently \(\sum\delta=6+2\cdot4=14\). With five rational components, the normalization exact sequence gives \(p_a(C)=14-5+1=10\), agreeing independently with the plane-sextic genus formula \((6-1)(6-2)/2=10\).

**4. Global Picard identity component.** The normalization is \(\coprod_{i=1}^5\mathbb P^1_k\) (the smooth conic is split since it has a rational point), so each component has trivial \(\operatorname{Pic}^0\). The exact sequence of units for the normalization therefore identifies \(\operatorname{Pic}^0(C)\) with the quotient of the product of the ten local unit quotients by the componentwise nonzero scalars modulo a simultaneous scalar. The local product is \(\mathbb G_m^{10}\times\mathbb G_a^4\); the four-dimensional split subtorus of component scalars acts on the multiplicative coordinates only. The incidence graph is connected and its character incidence matrix has rank \(5-1=4\) over \(\mathbb Z\) (a spanning tree has unimodular reduced incidence matrix), so the quotient torus is split of rank \(10-4=6\). Hence, as a group scheme over \(k\), \(\operatorname{Pic}^0(C)\cong\mathbb G_m^6\times\mathbb G_a^4\). Its dimension \(6+4=10\) independently matches \(p_a(C)\).

**5. Point counts and zeta function.** Each of the five components has exactly \(q+1\) rational points over every \(\mathbb F_q/\mathbb F_3\). Exactly ten distinct rational points are counted twice, one for each of six nodes and four tacnodes, with no triple intersection. Thus \(\#C(\mathbb F_q)=5(q+1)-10=5q-5\) for every \(q=3^m\). Taking the defining exponential series \(Z=\exp(\sum_{m\ge1}\#C(\mathbb F_{3^m})T^m/m)\) gives \((1-T)^5/(1-3T)^5\). Finally, the split Picard decomposition gives \((q-1)^6q^4\) rational points in its identity component.

## Verification
The standalone exact verifier `verify_wiman3.py` checks the polynomial factorization over \(\mathbb F_3\), all four conic tangencies, the six distinct transverse line-pair intersections, the graph and genus arithmetic, and exhaustive projective point counts over \(\mathbb F_3\), \(\mathbb F_9\), and \(\mathbb F_{27}\). Its final output is `VERIFY_OK`. The all-extension formula, local analytic classification, and Picard decomposition follow from the written proof, not from extrapolating finite computations.

## Relationship to prior work
Inoue and Kato's preprint supplies the classical plane equation and develops the Wiman–Edge geometry with the explicit standing assumption that the characteristic is not \(2\), \(3\), or \(5\). Giulietti, Kawakita, Lia, and Montanucci (2018), §2.1 and Remark 3.1, identify reducibility in characteristics \(2\) and \(3\), but the portions inspected do not state this factorization, the ten singularities, the split generalized-Picard group, or the all-extension point count. Dolgachev, Farb, and Looijenga (2018) describe the distinct characteristic-zero Wiman–Edge pencil degenerations, including a five-conic member with incidence graph \(K_5\); that different curve and setting do not imply the asserted characteristic-three scheme or Picard calculation. The complete characteristic-three picture above is an explicit special-fiber refinement of the published reducibility statement. A previously unindexed equivalent computation remains a priority risk.

## Limitations
No stable reduction, conductor of the smooth genus-six Jacobian, Néron model, or reduction of the full characteristic-zero automorphism group is claimed. The linear algebraic group computed is the Picard identity component of the reduced *plane-model* special fiber; it is not asserted to equal the special fiber of the Néron model of the genus-six Jacobian. The proof does not establish publication priority beyond the checked literature.

## References
1. N. Inoue and F. Kato, *On the geometry of Wiman's sextic*, Kyoto preprint (2005), https://www.math.kyoto-u.ac.jp/preprint/2005/2inoue.kato.pdf; J. Math. Kyoto Univ. 45 (2005), 743–757, DOI:10.1215/kjm/1250281655.
2. M. Giulietti, M. Kawakita, S. Lia, and M. Montanucci, *An \(\mathbb F_{p^2}\)-maximal Wiman's sextic and its automorphisms*, arXiv:1805.06317 (first posted 2018-05-15), https://arxiv.org/abs/1805.06317.
3. I. Dolgachev, B. Farb, and E. Looijenga, *Geometry of the Wiman–Edge pencil, I: algebro-geometric aspects*, Eur. J. Math. 4 (2018), 879–930, DOI:10.1007/s40879-018-0231-3.
