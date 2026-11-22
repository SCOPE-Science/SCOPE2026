# A Moore–sphere wedge from the first singular Singer action on an order-four projective-plane matroid

## Finding

Let \(V=\mathbb Z/21\), and let \(D=\{0,1,4,14,16\}\subset V\). Define the lines of a projective plane \(P\) to be the 21 translates \(i+D\), with \(i\in V\). Let \(K\) be the simplicial complex with a face at every single point, every pair of points and every noncollinear triple of points of \(P\). The cyclic Singer group \(C_{21}=V\) acts by translation. The **ordinary geometric quotient** has the integral homotopy equivalence

\[|K|/C_{21}\simeq M(\mathbb Z/7\mathbb Z,1)\vee\bigvee^{44}S^2,\]

where \(M(\mathbb Z/7\mathbb Z,1)\) is the Moore complex obtained by attaching a disk to a circle by the degree-seven map. Consequently \(\pi_1\cong H_1\cong\mathbb Z/7\mathbb Z\) and \(H_2\cong\mathbb Z^{44}\). The full homotopy decomposition, not these homology groups in isolation, is the claim.

## Assumptions and scope

All spaces are ordinary geometric realizations of finite complexes with the compact CW topology. The line set is defined **exactly** by the stated difference set, and the group acts by addition modulo 21. This is the cyclic projective plane of order four: the ordered differences of distinct members of \(D\) exhaust the 20 nonzero residues once each, so every two points lie on exactly one five-point line. The matroid has rank three and contains precisely all noncollinear triples as facets. No assertion is made for other finite-field orders or other collineation subgroups.

The action is not free on the realization: the subgroup of order three fixes the barycenter of each triangle in the orbit of \(\{0,7,14\}\). The quotient here must **not** be replaced by a free/Borel quotient. The central difference between this and the smaller field orders is this exceptional stabilizer orbit.

## Proof

**1. Exact geometry and orbit cells.** The Singer translations act regularly on 21 vertices. Since the group has odd order, no nonidentity element stabilizes an unordered pair of distinct vertices, so there are 10 edge orbits. The number of independent triangles is

\[\binom{21}{3}-21\binom53=1330-210=1120.\]

Any nontrivial stabilizer of a three-point face acts as a three-cycle, and therefore is the unique subgroup of order three. Its seven three-element point-orbits are exactly the translates of \(\{0,7,14\}\). Each is noncollinear: none is contained in a translate of \(D\), as directly checked by the difference-set definition. They constitute one exceptional triangle orbit, of size seven. The remaining 1113 triangles form 53 free orbits of size 21. Hence the quotient has a CW structure with precisely **one vertex, ten oriented one-cells and 54 two-cells**. An orbit of a triangle with trivial stabilizer gives the usual disk; the exceptional triangle modulo its rotation by three is still a disk, with boundary mapping once (rather than three times) over its edge orbit.

**2. Attaching words.** Label the oriented quotient edge orbits \(e_1,\ldots,e_{10}\), with an ordered edge \((x,y)\) mapping to \(e_d\) if \(d\equiv y-x\pmod{21}\) and \(1\le d\le10\), or to the inverse of \(e_{21-d}\) otherwise. For every nonexceptional triangle orbit choose its lexicographically least translated ascending triple \((a,b,c)\). Its attaching word is the freely reduced word for \((a,b)(b,c)(c,a)\) under that edge map. For the exceptional orbit the attaching word is \(e_7\), because the rotation of its boundary circle identifies three edges in cyclic orientation.

These rules uniquely determine an integer-word presentation of the actual CW quotient, with no assumption about the fundamental group. The supplied standalone program enumerates all orbit representatives and verifies every word from these rules.

**3. Nine homotopy-preserving cancellations.** An attaching word containing a one-cell generator exactly once allows that generator and two-cell to be eliminated together: solve the relation for that generator, substitute in all other attaching maps, and remove the free one/two-cell pair. This is the standard cellular elementary elimination, valid at the homotopy level and not merely a presentation-level calculation. The reproducible sequence is

\[\begin{aligned}
e_7&=1,&e_{10}&=e_3,&e_9&=e_2,\\
e_8&=e_1,&e_6&=e_1^{-1},&e_5&=e_2^{-1},\\
e_4&=e_3^{-1},&e_3&=e_1e_2,&e_2&=e_1^2.
\end{aligned}\]

After nine such cancellations, exactly one generator \(e_1\) and 45 two-cell attaching words remain. Their complete freely reduced census is 31 empty words and 14 words equal to \(e_1^7\) or \(e_1^{-7}\). This is checked by the supplied code from the **original 54 orbit faces**, not inferred from the Smith normal form or a numerical homology calculation.

**4. Exact homotopy splitting.** Attach one of the 14 degree-seven disks to the remaining circle, forming \(M(\mathbb Z/7\mathbb Z,1)\). Each of the other 13 degree-seven attaching loops is already nullhomotopic via this first disk. The 31 empty words are also nullhomotopic. Attaching a two-cell along a nullhomotopic loop adds a wedge two-sphere, giving \(13+31=44\) copies of \(S^2\). This proves the displayed equivalence, including the fundamental group and all integral homology consequences.

## Verification

Run `python3 singer_homotopy_certificate.py` from the directory holding the embedded file. It uses only Python standard-library modules. It verifies the difference-set incidence axiom for all 210 point pairs; the enumeration of 1120 independent triangles; the 54 orbit representatives and unique stabilizer-three orbit; all original attaching words; every one-occurrence generator elimination; and the terminal census of 31 trivial and 14 degree-seven words. The successful output ends `SINGER_Q4_HOMOTOPY_CERTIFICATE_OK`.

An independent script `singer_matroid_verifier.py` rebuilds the quotient integral boundary matrices for orders two, three and four, including the order-four stabilizer correction, and calculates integer Smith normal forms using SymPy. Its order-four output has one torsion invariant factor seven and free second-homology rank 44; these checks corroborate but do not replace the cellular homotopy proof. Its output ends `SINGER_PROJECTIVE_MATROID_QUOTIENT_CHECKS_OK`.

## Relationship to prior work

Singer groups are classical regular cyclic collineation groups of finite projective planes. Matroid independence complexes are classically shellable and hence have sphere-wedge homotopy types before quotienting. Earlier calculations at field orders two and three identified corresponding homotopy quotients, and an all-field-order computation determines the **fundamental group and integral homology** of the rank-three Singer quotients. The present statement does not reassert the latter as a new result. What it adds is the **integral homotopy type at the first singular order-four action**, including all two-cell attaching maps up to cellular homotopy. Knowing a cyclic fundamental group and free second homology alone does not determine this two-dimensional homotopy type or its second homotopy-group module.

The 2014 matroid-shellability and Singer-action sources inspected below do not provide this quotient-cell homotopy reduction. A targeted search of related mathematical records and primary literature did not identify a prior proof of the order-four Moore–sphere splitting. The absence of an indexed equivalent is not a proof of publication priority.

## Limitations

The statement is specific to the cyclic order-four projective plane with the explicitly specified difference set and to the ordinary Singer quotient; it does not classify Singer quotients for all prime powers or other subgroups. The proof is exact finite enumeration plus elementary CW-homotopy transformations, not an independent formal proof-assistant certification. The related general homology classification is prior coverage of the group invariants but not of the claimed homotopy decomposition. Literature-search incompleteness remains a novelty risk.

## References

1. K. Thas, *Hyperfield extensions, characteristic one and the Connes–Consani plane connection*, arXiv:1407.0607v1 (first public version 2014-07-02), https://arxiv.org/abs/1407.0607 . Classical Singer actions and finite-projective geometry are discussed.
2. F. Ardila, F. Castillo, J. A. Samper, *The topology of the external activity complex of a matroid*, arXiv:1410.3870v1 (first public version 2014-10-14), https://arxiv.org/abs/1410.3870 . Theorems 1.3 and 2.12 provide shellability of matroid independence complexes.
3. M. A. Armstrong, *On the fundamental group of an orbit space*, Proc. Cambridge Philos. Soc. **61** (1965), 639–646, https://doi.org/10.1017/S0305004100038974 . A complementary theorem for orbit-space fundamental groups, not needed in the explicit CW proof.
