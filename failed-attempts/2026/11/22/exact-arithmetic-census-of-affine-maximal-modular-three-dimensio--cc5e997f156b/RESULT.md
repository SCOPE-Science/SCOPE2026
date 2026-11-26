# Exact arithmetic census of affine maximal modular three-dimensional queen placements

## Finding

Let \(n\ge2\) be an integer. On the toroidal three-dimensional board \((\mathbb Z/n\mathbb Z)^3\), two distinct queens attack when their displacement is a scalar multiple of a nonzero vector in \(\{-1,0,1\}^3\). A placement is **affine** when it is a coset of a subgroup of \((\mathbb Z/n\mathbb Z)^3\). A placement of \(n^2\) queens is maximal in cardinality, since each line parallel to the third coordinate axis contains at most one queen.

**Theorem.** Every affine nonattacking placement of the maximum cardinality \(n^2\) is uniquely of the form
\[
Q_{a,b,c}=\{(x,y,ax+by+c):x,y\in\mathbb Z/n\mathbb Z\},
\]
with \(a,b,c\in\mathbb Z/n\mathbb Z\), and it is nonattacking if and only if
\[
\gcd(n,v-t)=1\quad\text{for every }v\in\{a,b,a+b,a-b\}\text{ and }t\in\{-1,0,1\}.
\]
In particular, if \(A(n)\) is the number of **distinct sets of occupied board cells** of this kind, then
\[
\boxed{A(n)=\begin{cases}
0,&\text{if some prime }p\mid n\text{ has }p<11,\\[2pt]
n^3\displaystyle\prod_{p\mid n}\left(1-\frac5p\right)\left(1-\frac7p\right),&\text{otherwise}.
\end{cases}}
\]
The product runs over distinct prime divisors. Equivalently, for every prime \(p\ge11\) and positive exponent \(e\), there are exactly \(p^{2(e-1)}(p-5)(p-7)\) eligible ordered slopes \((a,b)\) modulo \(p^e\); the independent offset \(c\) contributes a factor of \(n\). Thus \(A(11)=264\), \(A(13)=624\), and \(A(121)=351384\).

## Assumptions and scope

All additions, scalar multiplications and congruences are modulo the integer \(n\). A direction is any nonzero vector from \(\{-1,0,1\}^3\), with opposite directions regarded as the same line family. In the definition of attack, the scalar may be any residue class, but must produce a nonzero displacement. "Affine" always means a translate of a subgroup, not an arbitrary combinatorial placement. Queens are indistinguishable; the counted objects are **occupied subsets**, not their ordered listings or equivalence classes under board automorphisms. These assumptions are essential: neither nonaffine placements nor arrangements modulo translations/rotations are counted here.

## Proof

**1. Normalization and completeness of the graph form.** If \(Q\) is a nonattacking placement with \(n^2\) queens, each of the \(n^2\) vertical lines contains exactly one queen. The coordinate projection \(\pi(x,y,z)=(x,y)\) is therefore bijective on \(Q\). If \(Q=h+H\) is affine, then \(H\) is a subgroup of order \(n^2\), and the restriction \(\pi|_H\) is an isomorphism of additive groups: injectivity follows from the vertical-line condition, and the finite groups have the same order. Thus the third coordinate of \(H\) is an additive homomorphism \((\mathbb Z/n\mathbb Z)^2\to\mathbb Z/n\mathbb Z\), necessarily \((x,y)\mapsto ax+by\) for unique \(a,b\). Translation contributes the unique constant \(c\). Distinct triples \((a,b,c)\) yield distinct occupied subsets.

**2. Exact attack criterion.** A displacement between two cells of \(Q_{a,b,c}\) has the form \((u,v,au+bv)\). If it equals a nonzero scalar multiple of a queen direction with horizontal entries \((d_1,d_2)\ne(0,0)\) and vertical entry \(d_3\), then for some nonzero residue \(j\),
\[
j(ad_1+bd_2-d_3)=0\pmod n.
\]
Conversely, any such annihilating \(j\) creates an attacking pair of cells, since one horizontal direction entry is a unit \(\pm1\) and the displacement is nonzero. An element of \(\mathbb Z/n\mathbb Z\) has no nonzero annihilator precisely when it is a unit. Up to a common sign, the possible horizontal linear forms are \(a,b,a+b,a-b\), and \(d_3\) takes the three values \(-1,0,1\). Purely vertical directions cannot join distinct graph cells. This proves the stated twelve unit conditions.

**3. The finite-field arrangement.** For a prime \(p\), nonadmissibility modulo \(p\) is the union of twelve affine lines in \(\mathbb F_p^2\):
\[
a=t,\qquad b=t,\qquad a+b=t,\qquad a-b=t,\qquad t\in\{-1,0,1\}.
\]
Over the rationals, every intersection among nonparallel lines is one of 21 points. Exactly five are on four lines, four are on three lines, and twelve are on two lines. Explicitly, the five fourfold points are \((0,0),(\pm1,0),(0,\pm1)\); the four threefold points are \((\pm1,\pm1)\); the twelve double points are the four sign choices each of \((2,1)\), \((1,2)\), and \((1/2,1/2)\). There are no further intersections. All determinants of pairs of distinct line normals are \(\pm1\) or \(\pm2\). For \(p\ge7\), the 21 points remain distinct after reduction (nonzero coordinate differences have numerator of absolute value at most five after clearing denominators), and no extra line incidence appears (nonzero evaluations after clearing denominators have absolute numerator less than seven). Hence the multiplicities remain unchanged over every \(\mathbb F_p\) with \(p\ge7\).

There are initially \(12p\) incidences with the forbidden lines, while a point incident with \(m\) lines has been counted \(m\) times instead of once. Therefore the number of forbidden points equals
\[
12p-5(4-1)-4(3-1)-12(2-1)=12p-35.
\]
The number of admissible slopes is consequently \(p^2-12p+35=(p-5)(p-7)\) for \(p\ge7\), giving zero at \(p=7\). For \(p\in\{2,3\}\), no individual slope \(a\) can avoid the residues \(0,\pm1\). For \(p=5\), each of \(a,b\) must belong to \(\{2,3\}\), in which case either \(a-b=0\) or \(a+b=0\); hence there are no admissible slopes. Thus the prime-field count is zero for each \(p<11\) and is \((p-5)(p-7)\) for \(p\ge11\).

**4. Prime powers and composite moduli.** The twelve expressions in Step 2 are units modulo \(p^e\) exactly when their reductions modulo \(p\) are nonzero. Each admissible pair modulo \(p\) has exactly \(p^{2(e-1)}\) ordered lifts modulo \(p^e\). The Chinese remainder theorem bijects eligible pairs modulo a general \(n\) with products of eligible pairs modulo its prime-power factors. Multiplying these counts and then multiplying by the \(n\) choices of \(c\) yields
\[
A(n)=n\prod_{p^e\parallel n}p^{2(e-1)}(p-5)(p-7)
=n^3\prod_{p\mid n}\left(1-\frac5p\right)\left(1-\frac7p\right)
\]
when every \(p\ge11\), and zero otherwise. This proves the theorem for every \(n\ge2\). \(\square\)

## Verification

The standalone Python 3 script `verify_affine_queens.py` independently enumerates all 13 unoriented queen-line directions, directly checks the complete \(n^2\)-cell placements for every slope at \(n=2,3,5,7,11,13\), and compares these checks against the unit criterion. It separately enumerates twelve rational lines and verifies their intersection multiplicity profile \((5,4,12)\) at respective degrees \((4,3,2)\), with correction 35. For \(n\in\{2,3,5,7,11,13,17,19,25,49,121,143\}\), it compares exhaustive slope-unit counts with the product formula. It finishes with `VERIFY_OK`. These finite checks corroborate, but cannot replace, the unrestricted four-step proof.

## Relationship to prior work

Halberstam, Lee and Schildkraut (2026), arXiv:2611.14754v1, prove that the maximum cardinality \(n^2\) is attainable for the three-dimensional modular queen problem exactly when all prime divisors exceed eight. Their Section 2 gives the established affine existence construction, originally due in three dimensions to Klarner (1980), and Section 4 asks about counting *all* maximum arrangements. Neither the maximum-size bound nor the existence criterion nor that construction is claimed as new here. The present assertion is the exact number and characterization of **all affine maximum arrangements**, a natural subclass of that broader open enumeration question. Williams (2024; 2026 revision), arXiv:2404.18237, provides related existence bounds and near-maximal constructions but not this affine-subclass count. This distinction concerns implications of the actual statements; an unsuccessful literature search by itself cannot prove historical novelty.

## Limitations

This theorem does not enumerate nonaffine maximum placements; its formula is **not** asserted to equal the number of all maximum queen arrangements. It does not classify symmetry orbits or handle the non-toroidal board. The incidence analysis is a proof over every residue modulus, not an inference from the finite verification cases. Historical priority is provisional: equivalent counting formulas could exist under the terminology of linear queen placements, modular hyperplanes, or finite-field line arrangements. Independent mathematical review is not provided here.

## References

- Zachary Halberstam, Mitchell Lee, Carl Schildkraut, *Modular n-queens in higher dimensions*, arXiv:2611.14754v1 (public 2026-11-10), https://arxiv.org/abs/2611.14754.
- Kada Williams, *Torus Queen Independence*, arXiv:2404.18237v1 (public 2024-04-28; revision v4 2026-11-09), https://arxiv.org/abs/2404.18237.
- D. A. Klarner, 1980 affine construction, as cited and explained in Halberstam–Lee–Schildkraut, Section 2; the precise original work is not independently inspected here.
