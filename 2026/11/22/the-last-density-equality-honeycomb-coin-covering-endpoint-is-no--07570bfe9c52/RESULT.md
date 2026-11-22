# The last density-equality honeycomb coin-covering endpoint is non-coverable

## Finding
Let \(\omega=e^{2\pi i/3}\), \(H=\{a+b\omega:a,b\in\mathbb Z,\ a+b\not\equiv0\pmod3\}\), and \(H_d=dH\). Define a *covering* as a family of closed unit disks with pairwise disjoint interiors whose union contains \(H_d\). Then
\[
\boxed{H_{2/\sqrt{39}}\text{ admits no such covering}.}
\]
More precisely, if \(R=\sqrt{39}/2\), the centers of closed radius-\(R\) disks containing the maximum possible number of points of \(H\), namely 26, are exactly
\[
\Omega_{26}=\Lambda+\left\{\frac{\epsilon}{2}:\epsilon\in\{\pm1,\pm\omega,\pm\omega^2\}\right\},\qquad \Lambda=(1-\omega)\mathbb Z[\omega].
\]
Each such maximal disk contains an antipodal pair of points at separation \(\sqrt{39}\) in **each** of the two associate classes of Eisenstein integers of norm 39. As a consequence, the unresolved \(k=26\) right endpoint in Kittipassorn–Phetmak–Sriamorn's density-obstruction theorem is non-coverable.

## Assumptions and scope
All disks are Euclidean and closed; interiors of distinct unit disks must be disjoint. The point set and scale are defined exactly above. Write \(Q(a,b)=a^2-ab+b^2\) for the squared Euclidean norm of \(a+b\omega\). Only the stated honeycomb spacing is classified; no claim about nearby open intervals follows.

## Proof
**Finite maximum-disks lemma.** The translation lattice of \(H\) is \(\Lambda=\mathbb Z(1-\omega)+\mathbb Z(1+2\omega)\), with both displayed generators of norm 3 and their sum also of norm 3. Hence any center can be translated to the closed fundamental parallelogram \(F\), where its Euclidean norm is at most \(\sqrt3\). A site in its radius-\(R\) disk has norm at most \(R+\sqrt3<\sqrt{24}\). Thus every site that matters is in the explicit 54-element set
\[
S=\{a+b\omega:Q(a,b)\le23,\ a+b\not\equiv0\pmod3\}.
\]
If a disk with center in \(F\) contains at least 26 sites, choose any 26 sites \(T\) it contains. The nonempty intersection of the 26 closed equal-radius disks centered at \(T\) contains an intersection point \(z\) of two distinct boundary circles: a compact intersection of at least two distinct equal disks either is a singleton with at least two active constraints or has a boundary with at least two intersecting circular arcs. Such a \(z\) is a candidate in the finite computation below. If its disk contains a pair at distance \(2R\), any disk containing all of \(T\) has center exactly their midpoint \(z\). Therefore every 26-site center is itself a circle-intersection candidate if all candidates containing 26 sites include a diameter pair.

The standalone `certificate.py` proves precisely these finite facts **using integers only**. For each pair of distinct sites \(p,q\in S\) with \(Q(q-p)\le39\), it evaluates the one or two intersections of their radius-\(R\) circles. Put \(w=q-p\), \(y=t-p\), and \(v=Q(w)\). Define the integers
\[
A=2Q(y)-(2y_1w_1-y_1w_2-y_2w_1+2y_2w_2),\qquad B=y_1w_2-y_2w_1.
\]
For either sign \(\sigma\), a third site \(t\) is in the corresponding disk exactly when
\[
A+\sigma B\sqrt{\frac{3(39-v)}v}\le0.
\]
This inequality is decided by sign checks and comparisons of integer squares, including equality. Enumeration of **all 2,352** circle-intersection candidates from the 54 sites shows: none contains more than 26 sites; precisely 180 counted-with-multiplicity candidates contain 26; every one of these contains an antipodal diameter pair from **each** associate class of vectors of norm 39. Their centers form 30 distinct half-Eisenstein-lattice points before restricting to \(F\), and reduce to exactly six residue classes modulo \(\Lambda\), represented by \(\pm1/2,\pm\omega/2,\pm\omega^2/2\). Direct exact counting at \(1/2\), combined with the symmetries of \(H\), proves that these six classes really attain 26. The convex-intersection argument above proves that there are no other maximal centers and no 27-site disk.

**Obstruction to a disjoint covering.** The spatial density of \(H_d\) at \(d=2/\sqrt{39}\) is \(\rho=13/\sqrt3\), so \(2\sqrt3\rho=26\). Lemma 3.14 of Kittipassorn–Phetmak–Sriamorn (arXiv:2611.16894v1), whose hypotheses are now verified, says that any hypothetical disjoint-unit-disk covering admits a hexagonal-lattice covering by disks of the same radius, with exactly 26 honeycomb sites in each disk. Scale back by \(d\). Its center lattice is \(c_0+u\mathbb Z[\omega]\), where \(Q(u)=39\). All centers belong to \(\Omega_{26}\subset\tfrac12\mathbb Z[\omega]\), so \(2u\in\mathbb Z[\omega]\). If \(2u=a+b\omega\), then \(Q(a,b)=156\), which is even; the elementary congruence \(Q(a,b)\equiv a+b+ab\pmod2\) forces both \(a,b\) even. Thus \(u\in\mathbb Z[\omega]\). The norm-39 equation has twelve solutions, forming two unit-associate classes. Furthermore \(3\mid Q(u)\) implies \(u\in\Lambda\), so \(u\mathbb Z[\omega]\subset\Lambda\); the quotient of the two honeycomb cosets by this center lattice has exactly \(2\cdot39/3=26\) classes.

But the finite lemma proves that **every** 26-site disk at \(c_0\) contains two sites differing by a unit multiple of \(u\), hence two sites of the same residue class modulo \(u\mathbb Z[\omega]\). With only 26 sites in this disk, some other residue class is absent, and translating the disk through the center lattice never covers that class. Contradiction.

## Verification
Run `python3 certificate.py` with Python 3 and no external dependencies; it finishes with `PASS`. The program recomputes all 54 sites, 2,352 circle intersections, included-site sets, maximal-center residues, two norm-39 associate classes, and an independent direct count at a sample center. No floating arithmetic is used in the proof certificate. A separate Euclidean-coordinate cross-check of the circle-inclusion formula tested random circle-site triples and found agreement away from numerical roundoff on equality cases. The finite enumeration is exhaustive because every possible maximal disk reduces to a pairwise circle-intersection candidate as proved above.

## Relationship to prior work
Kittipassorn, Phetmak and Sriamorn, *Covering the Square Lattice and the Honeycomb with Non-Overlapping Unit Disks*, arXiv:2611.16894v1 (first public November 12, 2026), establish the density obstruction, exact critical 26-point occupancy, and hexagonal-packing rigidity; their Remark 5.1 explicitly leaves the endpoint \(2/\sqrt{39}\) open. The present result adds the complete six-class classification of maximal disk centers and closes that endpoint. It invokes, rather than claims, their density-rigidity lemma. Earlier constructions for other spacings and the triangular-lattice companion paper do not establish this endpoint.

## Limitations
The finite certificate concerns the exact critical spacing only and is not a general decision procedure for other honeycomb spacings. The proof uses a published, fully inspected, nontrivial rigidity lemma for critical-density covers. Historical priority and the finite checker would benefit from independent external review; no independent audit is claimed.

## References
1. T. Kittipassorn, N. Phetmak, K. Sriamorn, *Covering the Square Lattice and the Honeycomb with Non-Overlapping Unit Disks*, arXiv:2611.16894v1 (2026-11-12), Sections 2–5, especially Lemma 3.14 and Remark 5.1, https://arxiv.org/pdf/2611.16894.
2. T. Kittipassorn, N. Phetmak, K. Sriamorn, *Covering the Triangular Lattice with Non-Overlapping Unit Disks*, arXiv:2611.13535 (companion study mentioned in Reference 1).
