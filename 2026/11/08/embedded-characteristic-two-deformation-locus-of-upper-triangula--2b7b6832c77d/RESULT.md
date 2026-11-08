# Embedded characteristic-two deformation locus of upper-triangular algebra involutions

## Finding

Let \(k\) be any field and \(n\geq2\). Write \(T_n(k)\) for the upper-triangular \(n\times n\) matrix algebra and let \(a^\star=J a^{\mathsf T}J\), with \(J\) the anti-identity matrix. Define the **reversal-inner involution parameter scheme** \(\mathcal I_n\) over \(k\) to parameterize units \(g\in T_n\), modulo multiplication by central scalar units, for which \(a\mapsto g^{-1}a^\star g\) is an involution. More precisely, its functor assigns pairs \(([g],c)\) satisfying \(g^\star=cg\), \(c\in\mathbb G_m\); the scalar \(c\) is uniquely determined and obeys \(c^2=1\). Every \(k\)-linear algebra involution on \(T_n(k)\) comes from exactly one \(k\)-point of \(\mathcal I_n\).

**Theorem (embedded modular locus).** If \(\operatorname{char}k=2\) and \(n=2m\), then \(\mathcal I_{2m}\) has coordinate ring
\[
 k[u_1^{\pm1},\ldots,u_{m-1}^{\pm1},\,w_1,\ldots,w_{m^2},\,\epsilon]
 /(\epsilon^2,\epsilon w_{m^2-m+1},\ldots,\epsilon w_{m^2}),
\]
where the last \(m\) variables are the fixed anti-diagonal coefficients of the normalized triangular matrix. Its reduction is smooth and geometrically irreducible of dimension \(m^2+m-1\), but the whole scheme is nonreduced. The non-smooth locus is precisely the common zero locus of these \(m\) coefficients, of codimension \(m\) in the reduction. At every geometric point of this locus the tangent dimension is \(m^2+m\), one larger than the local dimension; outside it, the scheme is smooth. The extra first-order direction is obstructed at second order.

For \(\operatorname{char}k=2\) and \(n=2m+1\), \(\mathcal I_{2m+1}\) is smooth, geometrically irreducible, and isomorphic to \((\mathbb G_m)^m\times\mathbb A^{m(m+1)}\). If \(\operatorname{char}k\ne2\), the odd-dimensional scheme is unchanged; for \(n=2m\) the scheme is the disjoint union of two smooth pieces
\[
 (\mathbb G_m)^{m-1}\times\mathbb A^{m^2}
 \quad\sqcup\quad
 (\mathbb G_m)^{m-1}\times\mathbb A^{m(m-1)}.
\]

Consequently, the number of distinct \(k\)-linear algebra involutions on \(T_n(\mathbb F_q)\), when \(q\) is any prime power, is
\[
 \#\mathcal I_n(\mathbb F_q)=
 \begin{cases}
 q^{m(m+1)}(q-1)^m,&n=2m+1,\\
 q^{m^2}(q-1)^{m-1},&n=2m,\ q\text{ even},\\
 (q-1)^{m-1}\bigl(q^{m^2}+q^{m(m-1)}\bigr),&n=2m,\ q\text{ odd}.
 \end{cases}
\]
The geometric scheme statement refers to \(\mathcal I_n\) as defined, not to an unproved identification with every conceivable anti-automorphism functor on nonreduced base rings.

## Assumptions and scope

The base is an arbitrary field. The scheme \(\mathcal I_n\) is defined on all commutative \(k\)-algebras \(S\) using invertible upper-triangular matrices in \(T_n(S)\) and the displayed equations. Since the center of \(T_n(S)\) consists of scalars when \(n\ge2\), the quotient by scalar units is faithful for the induced involution maps. The symbol \(\star\) always means reversal of transpose, not the usual transpose. The finite-field count concerns distinct \(\mathbb F_q\)-linear anti-automorphisms of order two, not conjugacy classes and not involutions as *elements* of a triangular matrix group.

## Proof

**1. Inner-twist equation.** Since \(\star\) is an anti-involution, direct composition gives
\[
 (g^{-1}(g^{-1}a^\star g)^\star g)
 =g^{-1}g^\star a(g^\star)^{-1}g.
\]
The square is the identity on \(T_n(S)\) precisely when \(g^{-1}g^\star\) commutes with the whole triangular algebra. Matrix units show that its center is \(S\cdot I\), hence \(g^\star=cg\) for a unique scalar unit \(c\). Applying \(\star\) again gives \(g=c^2g\), so \(c^2=1\). Replacing \(g\) by a central unit does not change \(c\) or the induced map. Conversely the equation implies an involution.

**2. Exhaustion over fields.** An algebra anti-automorphism followed by \(\star\) is an automorphism of \(T_n(k)\). On the semisimple quotient \(k^n\), it must preserve the unique total order encoded by the nonzero spaces \(e_iT_ne_j\), so it fixes the primitive diagonal factors. By conjugating a complete compatible lift of the diagonal idempotents, one reduces the automorphism to one fixing all matrix units \(e_{ii}\). Such an automorphism scales each one-dimensional space \(ke_{ij}\) by \(a_i/a_j\) from the multiplicative identities \(e_{ij}e_{j\ell}=e_{i\ell}\); it is conjugation by a diagonal unit. Thus every field-valued anti-automorphism is a reversal-inner twist. Two twists agree exactly when their ratio is a central scalar, proving the claimed bijection.

**3. Coordinates.** Let \(u=n(n+1)/2\) be the number of upper-triangular entries. Reversal partitions these positions into pairs and \(f=\lceil n/2\rceil\) fixed positions on the secondary diagonal. One may normalize \(g_{11}=1\) using the scalar quotient. For each of the \((u-f)/2\) two-element orbits retain one free variable; the reversed entry equals \(c\) times that variable. The \(f\) fixed entries \(z_i\) satisfy \((c-1)z_i=0\). Among the paired entries, all diagonal coordinates are units; an additional fixed diagonal entry is a unit precisely when \(n\) is odd.

If \(n=2m+1\), the central diagonal entry is invertible and fixed under reversal, forcing \(c=1\) even over rings with nilpotents. Counting independent variables after normalization gives \(m\) invertible variables and \(m(m+1)\) unrestricted affine variables. In particular the scheme is smooth in every characteristic.

For \(n=2m\), there are \(m^2\) paired-coordinate variables, with \(m\) diagonal units, and \(m\) fixed-coordinate variables. Normalizing one diagonal unit leaves \(m-1\) unit coordinates and \(m^2\) affine coordinates. If the characteristic is odd, \(c^2-1=(c-1)(c+1)\) splits into two disjoint reduced components: on \(c=1\) all fixed variables are free, and on \(c=-1\) they vanish. These are the two stated smooth varieties. In characteristic two, putting \(\epsilon=c-1\) gives \(\epsilon^2=0\) and \(\epsilon z_i=0\), precisely the coordinate ring of the theorem.

**4. Singular support and obstruction.** In characteristic two and even \(n\), reducing sets \(\epsilon=0\), leaving a smooth integral variety. If any \(z_i\) is invertible in a local ring, then \(\epsilon z_i=0\) forces \(\epsilon=0\), so the scheme is smooth there. At a point where every \(z_i=0\), the linearization of the equations \(\epsilon^2=\epsilon z_i=0\) imposes no linear constraint on \(d\epsilon\). This adds exactly one tangent direction, and the nonzero nilpotent \(\epsilon\) persists in its local ring. The locus has codimension \(m\) in the reduction. The dual-number path \(\epsilon=t\), \(z_i=0\) in \(k[t]/(t^2)\) cannot lift to \(k[t]/(t^3)\), since any lift of \(\epsilon\) with linear coefficient one has square \(t^2\ne0\). This proves the second-order obstruction.

**5. Counting.** The number of points of \((\mathbb G_m)^a\times\mathbb A^b\) over \(\mathbb F_q\) is \((q-1)^a q^b\). Nilpotents have no nonzero values over a field, so only the reduction contributes in characteristic two. Applying this to the coordinate varieties proves the three displayed cases.

## Verification

The standalone `check.py` enumerates all invertible upper-triangular matrices over the prime fields \(\mathbb F_2,\mathbb F_3,\mathbb F_5\) for seven dimension/field pairs, tests the original relation \(g^\star=cg\), identifies projective scalars, and then checks the involution square and the reversed product identity on every ordered pair of matrix-unit basis elements for every admitted projective representative. It checks the count against the formulas. `CHECKS.txt` contains actual replay output. The scheme equations and tangent-space proof are symbolic arguments valid over all fields; the finite checks are not offered as a proof of the arbitrary-dimensional result.

## Relationship to prior work

The classical classification of upper-triangular algebra involutions is due to Spiegel and Di Vincenzo–Koshlukov–La Scala; classification *up to equivalence* is not claimed here. The work on incidence algebras by Brusamarello–Fornaroli–Santulo and Fornaroli–Pezzott likewise addresses equivalence classes. The new question is the *unquotiented involution parameter scheme*, especially its embedded nonreduced locus, tangent excess, and obstruction in characteristic two. The 2022 Fornaroli–Pezzott preprint was read in its full HTML version; it assumes characteristic different from two and does not derive this scheme geometry. The 2023 work of Kulguskin–Tapkin treats involutions over commutative rings up to equivalence, and is a significant possible implication risk: its abstract was inspected, but its full text could not be obtained. The original 2006 full text was also not accessible. Therefore historical priority is provisional and the claims are not independently certified.

## Limitations

The scheme statement is for the explicitly defined reversal-inner parameter scheme. It does not classify conjugacy orbits or establish a functorial isomorphism to an independently defined full anti-automorphism scheme over arbitrary nonreduced rings. Older classifications may imply aspects of the coordinate description; this remains a priority risk until their full proofs are inspected. The finite-field formula counts individual maps, not equivalence classes. There is no independent mathematical review.

## References

1. E. Spiegel, *Involutions in incidence algebras*, Linear Algebra Appl. 405 (2005), 155–162, DOI:10.1016/j.laa.2005.03.003.
2. O. M. Di Vincenzo, P. Koshlukov and R. La Scala, *Involutions for upper triangular matrix algebras*, Adv. Appl. Math. 37 (2006), 541–568, DOI:10.1016/j.aam.2005.07.004. An institutional repository assigns 2006-01-01 as a bibliographic date, not necessarily the first public day.
3. E. Spiegel, *Upper-Triangular Embeddings of Incidence Algebras with Involution*, Comm. Algebra 36 (2008), 1675–1681, DOI:10.1080/00927870801937224, verified online public date 2008-06-21.
4. R. Brusamarello, É. Z. Fornaroli and E. A. Santulo Jr, *Classification of involutions on incidence algebras*, Comm. Algebra 39 (2011), 1941–1955, DOI:10.1080/00927872.2010.480958.
5. É. Z. Fornaroli and R. E. M. Pezzott, *Classification of involutions on finitary incidence algebras of non-connected posets*, arXiv:2209.09690v1 (2022-09-20), full HTML at https://arxiv.org/html/2209.09690v1.
6. I. A. Kulguskin and D. T. Tapkin, *Involutions in algebras of upper-triangular matrices*, Russian Math. 67 (2023), 8–25, DOI:10.3103/S1066369X2306004X.
