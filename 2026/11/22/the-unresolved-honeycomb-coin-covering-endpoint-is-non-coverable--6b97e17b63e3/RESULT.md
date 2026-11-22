# The unresolved honeycomb coin-covering endpoint is non-coverable

## Finding

**Theorem.** Put \(\omega=\exp(2\pi i/3)\) and
\[
\mathcal H=\{a+b\omega:a,b\in\mathbb Z,\ a+b\not\equiv0\pmod3\}.
\]
At spacing \(d=2/\sqrt{39}\), the infinite point set \(d\mathcal H\) cannot be covered by closed unit disks with pairwise disjoint interiors. This resolves the outstanding borderline case \(e_{26}\) in Kittipassorn--Phetmak--Sriamorn [1]. In particular, the two immediately adjacent open intervals of density-forbidden spacings meet at a non-coverable endpoint.

The key finite geometric statement is more precise. In unscaled coordinates let \(r=\sqrt{39}/2\), and let \(\Lambda=(1-\omega)\mathbb Z[\omega]\), the translation lattice of \(\mathcal H\). The centers of disks of radius \(r\) containing 26 points of \(\mathcal H\) form exactly six \(\Lambda\)-cosets. In the fundamental parallelogram spanned by \(1-\omega\) and \(1+2\omega\), their representatives are
\[
\tfrac12,\quad\tfrac{1+\omega}{2},\quad
1-\tfrac{\omega}{2},\quad1+\tfrac{3\omega}{2},\quad
\tfrac{3+\omega}{2},\quad\tfrac{3+2\omega}{2}.
\]
Every such disk contains precisely 26 honeycomb points and exactly two antipodal pairs of boundary points, with the pairs' displacement vectors belonging to the two different six-element unit orbits of Eisenstein integers of norm 39.

## Assumptions and scope

The Eisenstein norm is \(N(a+b\omega)=a^2-ab+b^2\). Covering disks are closed, all have Euclidean radius 1 in the scaled plane, and distinct disks have center distance at least 2. No periodicity is assumed of a hypothetical covering. The statement addresses the specific infinite honeycomb \(d\mathcal H\), rather than a finite patch or the full triangular lattice.

The unscaled translation lattice \(\Lambda\) has covolume \(3\sqrt3/2\) and the unscaled disk radius is \(r=1/d=\sqrt{39}/2\). The maximum occupancy at this radius is 26, which can be obtained independently by the exact finite certificate below and agrees with Table 2 of [1]. The triangular packing reduction in Lemma 3.14 of [1] applies because \(\mathcal H\) is periodic and \(26=2\sqrt3\rho\) for the scaled point density \(\rho=4/(3\sqrt3d^2)\).

## Proof

**1. Exact classification of maximum-occupancy centers.** Choose the half-open fundamental parallelogram \(F=\{u(1-\omega)+v(1+2\omega):0\le u,v<1\}\). Every point of \(F\) has modulus at most \(\sqrt3\). Thus any honeycomb point in an \(r\)-disk centered in \(F\) has squared Eisenstein norm bounded by
\[
\left(\sqrt3+\frac{\sqrt{39}}2\right)^2
=\frac{51}{4}+\sqrt{117}<24.
\]
Consequently all relevant honeycomb points belong to the explicit finite set \(S=\{a+b\omega\in\mathcal H:N(a+b\omega)\le24\}\). Its integer coordinates have absolute values at most six.

For any finite set containing at least two points in a closed disk of fixed radius, the disk center can be moved while retaining all points until at least two distinct points lie on the boundary; the short compactness/active-constraint argument is Lemma 3.5 of [1]. For distinct \(p,q\in S\), with \(m=N(q-p)\le39\), all radius-\(r\) circles passing through both have centers
\[
c_{\pm}=\frac{p+q}{2}\pm\frac12
\sqrt{\frac{39-m}{3m}}\bigl((a-2b)+(2a-b)\omega\bigr),
\quad q-p=a+b\omega.
\]
For \(m=39\) the two expressions coincide. Retain only the centers in \(F\), and count points of \(S\) in the disk by exact comparisons, without floating-point tolerances. For \(z\in S\), put \(W=2z-p-q\) and \(\Delta=aW_b-bW_a\). The inclusion condition is precisely
\[
N(W)-m\mp3\Delta\sqrt{\frac{39-m}{3m}}\le0.
\]
Signs of these quadratic-radical expressions are decided by comparing integers after squaring only when the two summands have opposite signs. Both parallelogram-coordinate tests are of the same form. The complete integer/radical enumeration, implemented in `check_honeycomb.py`, returns 192 candidate pair-boundary centers (counting descriptions), each with occupancy at most 26. Exactly six distinct centers attain 26, and they are the six representatives displayed above.

This also classifies *all*, not just pair-boundary, 26-point centers: given any 26-point disk, move its center to a two-boundary-point center keeping its 26 points. One of the six classified centers results. Each of those six contains an antipodal pair at distance \(2r=\sqrt{39}\), whose midpoint is the **only** possible radius-\(r\) center containing both endpoints. Therefore the original center already equals the classified center. The same argument rules out occupancy greater than 26.

To describe the antipodal contacts explicitly, represent a listed center \(c\) by the integer pair \(2c=(A,B)\) in Eisenstein coordinates. For the six pairs \((A,B)=(1,0),(1,1),(2,-1),(2,3),(3,1),(3,2)\), the two diameter displacements can be taken, respectively, as
\[
\begin{array}{c|cc}
(A,B)&\text{first displacement}&\text{second displacement}\\\hline
(1,0)&(7,2)&(5,-2)\\
(1,1)&(7,5)&(5,7)\\
(2,-1)&(2,7)&(2,-5)\\
(2,3)&(2,7)&(2,-5)\\
(3,1)&(7,5)&(5,7)\\
(3,2)&(7,2)&(5,-2)
\end{array}
\]
Every vector in this table has norm 39. Multiplication by \(1+\omega\) rotates an Eisenstein vector through \(60^\circ\), and the twelve norm-39 vectors split into two six-element orbits. Each row supplies one vector from each orbit. The checker also verifies directly, for all six centers and all twelve orientations, that at least one pair of contained points is congruent modulo the corresponding norm-39 Eisenstein principal lattice.

**2. Consequence of equality in the packing density bound.** Suppose the asserted covering exists. By Lemma 3.14 of [1], there then exists a covering whose disk centers form a translate of a regular triangular lattice \(L'\) with minimum distance 2, and every disk contains exactly 26 honeycomb points. Divide coordinates by \(d\). The centers now form a triangular lattice \(L\) with minimum distance \(\sqrt{39}\), and each radius-\(r\) disk contains 26 points of \(\mathcal H\). Step 1 forces every center into the union of the six \(\Lambda\)-cosets, all of whose coordinates lie in \(\tfrac12\mathbb Z[\omega]\).

Let \(v\) be any shortest nonzero vector of \(L\). Because it is a difference of two permitted centers, \(2v\in\mathbb Z[\omega]\), with \(N(2v)=156\). If an Eisenstein integer has norm divisible by four, both its coordinates are even: checking the four residue pairs modulo two in \(a^2-ab+b^2\) gives norm 0 modulo 4 only for two even coordinates. Thus \(v\in\mathbb Z[\omega]\), \(N(v)=39\), and (since \(N(a+b\omega)\equiv(a+b)^2\pmod3\)) \(v\in\Lambda\). A triangular lattice generated by its shortest vector and its \(60^\circ\) rotation is \(L=v\mathbb Z[\omega]\), a sublattice of \(\Lambda\) with index 13. Consequently \(\mathcal H\) has exactly \(2\cdot13=26\) residue classes modulo \(L\).

Every disk centered at \(c+L\) is a translate by \(L\) of the one at \(c\). To cover \(\mathcal H\), the radius-\(r\) disk at \(c\) must therefore meet **all 26 distinct residue classes** of \(\mathcal H\) modulo \(L\). But Step 1 says this disk contains an antipodal pair whose displacement has the same norm-39 orientation orbit as \(v\), hence is a unit multiple of \(v\) and belongs to \(L\). These are two distinct points of the **same residue class**. With only 26 contained points, at least one of the 26 residue classes is missing, a contradiction. Thus the covering does not exist. \(\square\)

## Verification

Run `python3 check_honeycomb.py` using Python 3 and only the standard library. The script independently enumerates pair-circle intersections and uses exact integer comparisons of \(A+B\sqrt{U/V}\). It checks: 192 boundary-pair candidate descriptions in the chosen fundamental parallelogram; maximum occupancy 26; the six representatives; both antipodal contact orbits; all twelve possible shortest vectors; and direct modular collisions in each of the 72 center/orientation cases. The finite enumeration is exhaustive because of the proved norm bound, boundary-pair lemma, and unique-midpoint argument. The non-coverability deduction uses the analytic packing-reduction lemma from [1], not experimental extrapolation.

## Relationship to prior work

Kittipassorn, Phetmak and Sriamorn [1], Theorem B, Table 2 and Remark 5.1 determine the twelve forbidden honeycomb intervals and settle all but the endpoint \(e_{26}=2/\sqrt{39}\); they explicitly identify its coverability as open. Their Lemma 3.14 supplies the global density-equality reduction used above. The present contribution is the exact six-center classification, the forced antipodal congruences and the resulting negative resolution at this endpoint, not a reproof of [1]'s density theorem. The related triangular-lattice paper [2] settles a different point set and does not imply this honeycomb endpoint result. Earlier periodic motif constructions [3] cover ranges beginning at larger spacings but do not address this endpoint.

## Limitations

The theorem excludes exactly the specified spacing and yields no classification of coverings at neighboring spacings where the packing density bound is not attained. The proof relies on the published density-equality reduction of [1]. Its finite part uses a self-contained exact-arithmetic executable certificate; its 192 candidate descriptions are not to be interpreted as 192 distinct centers. No independent external validation or priority certification is claimed.

## References

[1] T. Kittipassorn, N. Phetmak, K. Sriamorn, *Covering the Square Lattice and the Honeycomb with Non-Overlapping Unit Disks*, arXiv:2611.16894v1 (first posted 12 November 2026), https://arxiv.org/html/2611.16894v1. In particular Section 3.1 (Lemma 3.5), Section 3.3 (Lemma 3.14), and Section 5 (Theorem B, Table 2, Remark 5.1).

[2] T. Kittipassorn, N. Phetmak, K. Sriamorn, *Covering the Triangular Lattice with Non-Overlapping Unit Disks*, arXiv:2611.13535v1 (first posted 10 November 2026), https://arxiv.org/html/2611.13535v1.

[3] N. Phetmak, G. Nuntasombat, J. Fakcharoenphol, *Covering Planar Lattices with Interior-Disjoint Unit Disks*, arXiv:2607.19764v2 (first posted 22 July 2026), https://arxiv.org/html/2607.19764v2.
