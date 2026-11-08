# Seven components of rank-one associative Nijenhuis operators on Kronecker path algebras

## Finding
Let \(k\) be an arbitrary field and \(m\ge2\). The reduced variety of rank-at-most-one associative Nijenhuis operators on the \(m\)-arrow Kronecker path algebra has exactly **seven geometrically irreducible components**, of dimensions
\[
2m+1,\quad 2m+1,\quad 2m,\quad m+1,\quad m+1,\quad 1,\quad 1.
\]
The components are described explicitly below. Over every finite field \(\mathbb F_q\), their union has exactly
\[
1+\frac{q^m-1}{q-1}(2q^{m+1}-q^m-1)
+2q^m(q^{m+1}+q-2)+2(q-1)
\]
points, including the zero operator.

## Assumptions and scope
Fix a field \(k\) of arbitrary characteristic. Let
\[
A_m=ke\oplus kf\oplus V,\qquad\dim_k V=m\ge2,
\]
with multiplication determined by
\[
e^2=e,\qquad f^2=f,\qquad ev=v=vf\quad(v\in V),
\]
and all other products of these summands zero. Thus \(1=e+f\), \(V^2=0\), and the algebra is the path algebra of the acyclic quiver with two vertices and \(m\) parallel arrows. An *associative Nijenhuis operator* is a \(k\)-linear map \(P:A_m\to A_m\) satisfying, for all \(x,y\in A_m\),
\[
P(x)P(y)=P(P(x)y+xP(y)-P(xy)). \tag{1}
\]
The rank constraint is \(\operatorname{rank}_kP\le1\). We study the **reduced** algebraic variety underlying these equations inside the space of linear maps, and count actual linear maps over finite fields. Let \(e^*,f^*\in A_m^*\) extract the \(e\)- and \(f\)-coefficients, vanishing on \(V\). Put
\[
E=ke\oplus V,\quad F=kf\oplus V,\quad
H=\{\phi\in A_m^*: \phi(1)=0\}.
\]
Write \(a\otimes\phi\) for the rank-at-most-one map \(x\mapsto\phi(x)a\). All listed families include zero.

## Proof
**1. Exhaustive image-line classification.** If \(P=a\otimes\phi\) is nonzero with \(a\ne0\), \(\phi\ne0\), the right side of (1) lies in \(ka\), so the left side forces \(a^2\in ka\). Write \(a=se+tf+u\), \(u\in V\). Then
\[
a^2=s^2e+t^2f+(s+t)u.
\]
Solving \(a^2=\lambda a\) shows that the image line has precisely one of the four forms \(kv\) (\(0\ne v\in V\)), \(k(e+u)\), \(k(f+u)\) (\(u\in V\)), or \(k1\). Indeed, if both \(s,t\) are nonzero they must equal \(\lambda\), then the radical equation forces \(u=0\). If exactly one is nonzero, rescale it to one; if both vanish, \(a\in V\).

**2. Reduction of the Nijenhuis identity.** With \(a^2=\lambda a\), substitute \(P=a\otimes\phi\) into (1). Its scalar condition, necessary and sufficient for all \(x,y\), is
\[
\lambda\phi(x)\phi(y)=\phi(x)\phi(ay)
+\phi(y)\phi(xa)-\phi(a)\phi(xy). \tag{2}
\]
If \(a=v\in V\), write \(\phi=\alpha e^*+\beta f^*+\ell\), \(\ell\in V^*\). Since \(vy=f^*(y)v\) and \(xv=e^*(x)v\), direct substitution in (2) reduces it to
\[
\ell(v)(\alpha+\beta)=0. \tag{3}
\]
Thus either \(\phi(v)=0\) or \(\phi(1)=0\). For \(a=e\), evaluating (2) on the ordered pairs \((f,f)\) and \((v,f)\), and then checking all remaining basis pairs, gives exactly
\[
\beta(\alpha+\beta)=0,\qquad (\alpha+\beta)\ell=0. \tag{4}
\]
Consequently \(\phi(1)=0\) or \(\phi\in ke^*\). The symmetric calculation for \(a=f\) yields \(\phi(1)=0\) or \(\phi\in kf^*\). For \(a=e+u\) (or \(f+u\)), conjugation by the unit \(1-u\) sends \(e\) to \(e+u\) (or the analogous inverse conjugation sends \(f\) to \(f+u\)), preserves \(\phi(1)\), and fixes \(e^*,f^*\) under pullback. Therefore the same alternatives apply, with \(a\in E\) (or \(F\)). Finally for \(a=1\), equation (2) becomes
\[
\phi(x)\phi(y)=\phi(1)\phi(xy). \tag{5}
\]
For \(\phi\ne0\), necessarily \(\phi(1)\ne0\); then \(\phi/\phi(1)\) is a unital algebra character. Since all characters kill the radical \(V\) and take complementary idempotents \(e,f\) to zero and one, these characters are exactly \(e^*\) and \(f^*\). Thus the unit-image operators are precisely \(k(1\otimes e^*)\cup k(1\otimes f^*)\). Equations (2)–(5) also verify sufficiency for each listed family.

**3. Seven closed geometrically irreducible components.** Collecting the cases gives the following seven closed subsets of \(\operatorname{End}_k(A_m)\):
\[
\begin{aligned}
\mathcal X_e&=\{a\otimes\phi:a\in E,\phi\in H\},&
\mathcal X_f&=\{a\otimes\phi:a\in F,\phi\in H\},\\
\mathcal Y&=\{v\otimes\phi:v\in V,\phi(v)=0\},&
\mathcal L_e&=\{a\otimes e^*:a\in E\},\\
\mathcal L_f&=\{a\otimes f^*:a\in F\},&
\mathcal U_e&=k(1\otimes e^*),\quad
\mathcal U_f=k(1\otimes f^*).
\end{aligned}
\]
The first two are rank-one determinantal cones for tensor products of vector spaces of respective dimensions \(m+1,m+1\), each irreducible of dimension \(2m+1\). The third is the cone over the projective incidence variety \(\{([v],[\phi])\in\mathbb P(V)\times\mathbb P(A_m^*):\phi(v)=0\}\), which is a projective \(m\)-space bundle over \(\mathbb P^{m-1}\); hence it is irreducible and has affine-cone dimension \(2m\). Equivalently, \(\mathcal Y\) is cut out inside rank-at-most-one maps with image in \(V\) by the closed condition \(\operatorname{tr}P=0\). The remaining four are linear spaces with dimensions \(m+1,m+1,1,1\). No one of the seven closed irreducible sets lies in the union of the other six: the generic image and functional conditions distinguish them (notably, \(\mathcal Y\) has radical image and generic \(\phi(1)\ne0\), while the two \(\mathcal X\)'s impose \(\phi(1)=0\); the \(\mathcal L\)'s impose a character functional; and the \(\mathcal U\)'s have image \(k1\)). Therefore these are exactly all geometrically irreducible components of the reduced variety, in all characteristics.

**4. Exact finite-field census.** Over \(\mathbb F_q\), there are \((q^m-1)/(q-1)\) radical image lines. For each \(kv\), condition (3) gives the union of two distinct functional hyperplanes \(\phi(v)=0\) and \(\phi(1)=0\), each of size \(q^{m+1}\), intersecting in size \(q^m\); excluding \(\phi=0\) gives \(2q^{m+1}-q^m-1\) maps on that image line. There are \(q^m\) image lines \(k(e+u)\) and another \(q^m\) of type \(k(f+u)\); each admits \(q^{m+1}-1\) nonzero functionals in \(H\) and \(q-1\) additional nonzero scalar multiples of the relevant character, hence \(q^{m+1}+q-2\) maps per line. Finally, the unit-image line contributes \(2(q-1)\) maps. These four image-line types are disjoint, so summation proves the displayed census. The zero map adds one.

## Verification
A standalone Python 3 checker reconstructs the multiplication table of \(A_m\) and verifies the *original* identity (1) on every ordered pair of basis vectors for every distinct rank-one linear map over \(\mathbb F_2\), \(\mathbb F_3\) and \(\mathbb F_4\) in the indicated test dimensions. It also compares membership in the seven explicit families and their predicted counts, not merely a substituted normal form. Results (all **nonzero** rank-one operators): \((m,q)=(2,2)\): \(99\) (radical/e/f/unit strata \(33/32/32/2\)); \((2,3)\): \(684\) (\(176/252/252/4\)); \((3,2)\): \(419\) (\(161/128/128/2\)); \((2,4)\): \(2673\) (\(555/1056/1056/6\)). The \(\mathbb F_4\) arithmetic is implemented as \(\mathbb F_2[X]/(X^2+X+1)\). The included source and recorded program output reproduce these tests. Finite checks do not constitute proof for all fields or dimensions; the algebraic argument above does.

## Relationship to prior work
Guo and Lei, *Nijenhuis algebras, NS algebras and N-dendriform algebras* (first submitted 5 October 2012), give the associative operator identity and develop free/universal Nijenhuis algebra constructions and operadic consequences, not an explicit Kronecker rank-one component census. Bartocci and Tacchella, *Poisson-Nijenhuis structures on quiver path algebras* (2016), investigate a different noncommutative Poisson-geometric notion of Nijenhuis recursion operator, not arbitrary linear associative Nijenhuis endomorphisms satisfying (1). Zou, Gao, Kang and Lü, *Nijenhuis operators on 2D pre-Lie algebras and 3D associative algebras* (first posted 23 August 2023), classify only 3-dimensional associative algebras over the complex numbers; the present family has dimension \(m+2\ge4\), and its geometric and finite-field conclusions do not follow from that classification. The earlier finite-Kronecker commutator-fiber enumeration addresses element centralizers/commuting pairs, not Nijenhuis maps. Search noncoverage is not a proof of historical priority; a more general unlocated theorem might subsume this result.

## Limitations
The results apply only to linear operators of rank at most one and the specified acyclic \(m\)-Kronecker path algebra, \(m\ge2\). They do not classify higher-rank Nijenhuis operators, automorphism orbits, or the nonreduced scheme structure. Publication priority and independent mathematical validation are not certified. The geometric conclusions refer to the reduced variety and remain valid after passage to an algebraic closure.

## References
1. L. Guo and P. Lei, *Nijenhuis algebras, NS algebras and N-dendriform algebras*, arXiv:1210.1821v1, publicly posted 2012-10-05, https://arxiv.org/html/1210.1821v1.
2. C. Bartocci and A. Tacchella, *Poisson-Nijenhuis structures on quiver path algebras*, arXiv:1604.02012v1 (2016), https://arxiv.org/abs/1604.02012.
3. X. Zou, X. Gao, C. Kang and J. Lü, *Nijenhuis operators on 2D pre-Lie algebras and 3D associative algebras*, arXiv:2308.12121v3 (2026; originally posted 2023-08-23), https://arxiv.org/html/2308.12121v3.
