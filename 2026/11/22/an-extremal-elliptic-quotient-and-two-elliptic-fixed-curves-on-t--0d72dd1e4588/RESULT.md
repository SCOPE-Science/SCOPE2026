# An extremal elliptic quotient and two elliptic fixed curves on the BHK self-mirror K3

## Finding

Let \(V\) be the smooth complex quartic surface
\[
V=\{x^3y+xy^3+z^3w+zw^3=0\}\subset\mathbb P^3_{\mathbb C}.
\]
Let \(s([x:y:z:w])=[-x:-y:z:w]\) and let \(S\) be the minimal resolution of \(V/\langle s\rangle\). This is the self-mirror K3 surface denoted \(X_2\) in Barrett–Clayton–DeVries–Priddis [1]. Let \(\iota\) be the involution of \(S\) induced by interchanging \(x\) and \(y\). The following statements hold.

1. The K3 surface \(S\) is isomorphic to the relatively minimal elliptic surface over \(\mathbb P^1_t\) with generic Weierstrass equation
\[
Y^2=X^3+t^2(t^2+1)^2X.
\]
It has exactly four singular fibers, each of Kodaira type \(I_0^*\), over \(t=0,i,-i,\infty\).

2. In these coordinates \(\iota\) acts on the function field by
\[
(t,X,Y)\longmapsto(t^{-1},t^{-4}X,t^{-6}Y).
\]
The quotient \(S/\langle\iota\rangle\) is isomorphic to the relatively minimal rational elliptic surface with generic equation
\[
\eta^2=\xi^3+u^2\xi,\qquad u=t+t^{-1},
\]
and exactly two \(I_0^*\) fibers, over \(u=0,\infty\). Its Mordell–Weil group is \((\mathbb Z/2\mathbb Z)^2\), with affine nonzero points \((0,0),(iu,0),(-iu,0)\).

3. The fixed locus of \(\iota\) on \(S\) is the disjoint union of exactly two smooth elliptic curves: the fibers over \(t=1\) and \(t=-1\). Thus its Nikulin invariant-lattice triple is
\[
(r,a,\delta)=(10,8,0),\qquad H^2(S,\mathbb Z)^\iota\cong U\oplus E_8(-2).
\]
This is not the one-elliptic-curve type \((10,10,\delta)\).

## Assumptions and scope

The ground field is \(\mathbb C\), and the quartic, symplectic sign change, and nonsymplectic coordinate transposition are exactly as above. The result concerns the minimal resolution of the quotient by \(s\), not the original quartic's transposition quotient. The Weierstrass equations describe smooth relatively minimal surfaces after resolving their additive fibers. Write \(i^2=-1\). Kodaira types and Néron–Severi ranks are geometric, over \(\mathbb C\). The invariant lattice includes the bilinear intersection form, and \(U\) is the even hyperbolic plane.

## Proof

**Invariant-field derivation.** Work on the dense affine chart \(w=1\) with \(y\ne0\). Put \(t=x/y\), \(v=z\), \(q=y^2\), and \(f=t(t^2+1)\). The automorphism \(s\) fixes \(t,v,q\) and generates a quadratic extension of their field by \(y\). Its invariant field satisfies the single relation
\[
fq^2+v^3+v=0.
\]
Define \(X=fv\), \(Y=if^2q\). Substitution yields
\[
Y^2=-f^4q^2=f^3(v^3+v)=X^3+f^2X.
\]
Conversely, \(v=X/f\) and \(q=Y/(if^2)\), so this is an equality of function fields, not just a map to a different surface.

As a section of \(\mathcal O_{\mathbb P^1}(4)\), \(f=t(t^2+1)\) has four *simple* zeros \(0,i,-i,\infty\): in the reciprocal chart \(z=1/t\), its transformed coefficient is \(z^4f(1/z)=z(z^2+1)\). For the Weierstrass equation \(a_4=f^2,a_6=0\), the discriminant is \(\Delta=-64f^6\). At each zero, \(v(a_4)=2\), \(v(\Delta)=6\), and the equation is minimal. The characteristic-zero Tate–Kodaira classification gives exactly one \(I_0^*\) fiber at each such zero. In particular, the elliptic surface has holomorphic Euler characteristic \(24/12=2\), no multiple fibers, a section and trivial canonical class; it is a K3 surface. It is birational to the K3 surface \(S\); minimal smooth K3 surfaces are birationally isomorphic. This proves the first assertion.

**Induced transposition and invariant quotient.** In the invariant coordinates before the change to Weierstrass form, swapping \(x\) and \(y\) gives \(t\mapsto1/t\), \(v\mapsto v\), and \(q\mapsto t^2q\). Since \(f(1/t)=f(t)/t^4\), it follows that \(X\mapsto X/t^4\) and \(Y\mapsto Y/t^6\). Set
\[
u=t+t^{-1},\quad \xi=X/t^2,\quad\eta=Y/t^3.
\]
These are invariant, \(f/t^2=u\), and division of the Weierstrass equation by \(t^6\) gives
\[
\eta^2=\xi^3+u^2\xi.
\]
Moreover \(t\) solves the quadratic equation \(t^2-ut+1=0\). The invariant field is exactly \(\mathbb C(u,\xi,\eta)\), because the action is nontrivial on \(t\). The quadratic base change has discriminant \(u^2-4\), ramifying precisely over \(u=2,-2\).

For the quotient's Weierstrass surface over \(\mathbb P^1_u\), the coefficient \(a_4=u^2\) is a section of \(\mathcal O(4)\); near infinity, with \(z=1/u\), its local expression is \(z^4(1/z)^2=z^2\). Thus exactly at \(u=0,\infty\), the valuations are \(v(a_4)=2\), \(v(\Delta)=6\), giving two \(I_0^*\) fibers. The surface has \(\chi(\mathcal O)=12/12=1\), section, no multiple fibers and base \(\mathbb P^1\); it is a rational elliptic surface. It is the quotient itself rather than an arbitrary birational model: the double-cover base change \(t^2-ut+1=0\) is unramified above the two additive fibers and ramified only along the smooth fibers \(u=\pm2\). Accordingly the pullback of the relatively minimal smooth rational elliptic surface is already the smooth relatively minimal K3 surface above, with deck transformation \(\iota\); taking the quotient recovers the given smooth rational elliptic surface.

**All sections of the quotient.** After the substitution \(u=v^2\), put \(\xi=v^2 A\) and \(\eta=v^3B\). The generic fiber becomes the constant elliptic curve \(E:B^2=A^3+A\) over \(\mathbb C(v)\). Every \(\mathbb C(v)\)-rational point of this constant curve defines a rational map \(\mathbb P^1_v\dashrightarrow E\), extending to a morphism. Since there is no nonconstant map from \(\mathbb P^1\) to a genus-one curve, such a point is constant. Under \(v\mapsto-v\), descent requires \((A,B)=(A,-B)\); this is exactly \(E[2]\). Consequently the full quotient Mordell–Weil group (not only its torsion subgroup) consists of its four displayed two-torsion sections. Independently, the Shioda–Tate formula gives \(10-2-4-4=0\) for the free Mordell–Weil rank.

**Fixed locus and lattice.** The morphism \(S\to\mathbb P^1_t\) is \(\iota\)-equivariant for the involution \(t\mapsto1/t\) of the base. Any fixed point therefore lies over \(t=\pm1\). The two fibers are smooth, because \(f(1)=2\) and \(f(-1)=-2\) are nonzero. At either base point the displayed formulas act as the identity on \(X,Y\), so both fibers are fixed pointwise. This proves that their disjoint union is the whole fixed locus, without relying on a count of individual exceptional curves. Nikulin's classification of nonsymplectic involutions on complex K3 surfaces [2] says that the exceptional fixed-locus type of two disjoint elliptic curves occurs exactly for \((r,a,\delta)=(10,8,0)\). Its rank-ten even two-elementary invariant lattice is therefore isometric to \(U\oplus E_8(-2)\). Indeed, the latter has discriminant group \((\mathbb Z/2)^8\) and integral discriminant quadratic form; uniqueness follows from the classification. This proves the final assertion.

## Verification

The accompanying `CHECK.py` uses exact symbolic identities to replay the invariant-field transformation, the coordinate-swap action, the quadratic quotient relation, the four simple roots of the K3 coefficient as a degree-four section, the two simple roots of the rational surface coefficient as a degree-two section, the smooth fixed fibers, and the four rational two-torsion points. Run `python CHECK.py` with SymPy installed. The output `PASS` establishes these *finite algebraic identities*; the global conclusions (minimality, smooth-model identification, elliptic-section descent, fiber types, fixed-locus completeness and lattice identification) follow from the mathematical arguments above, not from finite testing.

A separate geometric cross-check uses the planes \(x=y\) and \(x=-y\) in \(V\). Their quartic intersections each have genus three, and restriction of \(s\) has four fixed points (the four simple roots of \(zw(z^2+w^2)\)), so their quotients are genus-one curves by Riemann–Hurwitz. Their strict transforms separate over the four common quotient nodes. This agrees with the two distinct elliptic fixed fibers found in the explicit Weierstrass model.

## Relationship to prior work

Barrett, Clayton, DeVries and Priddis [1], Sections 3.7.1 and 3.7.4, define the same quotient K3 and coordinate-transposition involution, and give its invariant rank as ten. They report a single elliptic fixed curve and \(a=10\), without determining \(\delta\). The explicit function-field model here shows instead that its fixed locus has two elliptic components and forces the exceptional Nikulin type \((10,8,0)\). This is a statement-level disagreement rather than a difference of nomenclature; the proof includes a separate plane-section cross-check. The general classification of Nikulin [2] and the rational-surface classification of Miranda–Persson [3] supply context but do not identify this particular BHK quotient and involution. General results about double-cover elliptic K3s in Garbagnati–Salgado [4] allow this geometry but do not give the specific coordinate formulas or transposition fixed-locus determination.

## Limitations

The theorem is over \(\mathbb C\); it does not address integral reductions or other involutions of the quartic. The rational elliptic surface of two \(I_0^*\) fibers is a classical type, so its *abstract* classification is not asserted to be new. Newness is the explicit equivariant identification of the named mirror K3, its named coordinate swap, and the resulting fixed-locus and lattice correction. Independently reviewed publication priority has not been established. No complete classification of all elliptic pencils on \(S\) is claimed.

## References

[1] A. Barrett, A. Clayton, B. DeVries, N. Priddis, *K3 surfaces and BHK Mirror symmetry: A counterexample*, arXiv:2611.15986v1, first public 2026-11-11, especially Sections 3.7.1 and 3.7.4. https://arxiv.org/html/2611.15986v1

[2] V. V. Nikulin, *Integral symmetric bilinear forms and some of their applications* and the classification of 2-elementary K3 involutions (1979); the explicit fixed-locus statement is reproduced in the survey *K3 Surfaces with non-symplectic automorphisms of prime order*, Section 3, Theorem 3.1. https://www.ms.u-tokyo.ac.jp/~kazushi/proceedings/K3-mirror.pdf

[3] R. Miranda and U. Persson, *On extremal rational elliptic surfaces*, Math. Z. 193 (1986), 537–558. See also T. Jarvis, W. Lang, J. Ricks, *Integral Models of Extremal Rational Elliptic Surfaces* (2012), https://doi.org/10.1080/00927872.2011.598593

[4] A. Garbagnati, C. Salgado, *Elliptic fibrations and involutions on K3 surfaces*, arXiv:2304.01383, 2023, especially Section 3.1 (type-two fibrations and quotient base change). https://arxiv.org/abs/2304.01383
