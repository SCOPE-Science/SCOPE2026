# Affine subgroup quotients of the two-particle complete-five-graph surface

## Finding
Let \(K_5\) be the complete simple graph with vertex set \(\mathbb F_5\), with each edge realized as a closed unit interval, and let \(X=\operatorname{UConf}_2(|K_5|)\) be the space of two distinct, unordered points on the geometric graph. The affine group
\[
F=\operatorname{AGL}(1,\mathbb F_5)=\{x\mapsto ax+b:a\in\mathbb F_5^\times,\ b\in\mathbb F_5\}\cong C_5\rtimes C_4
\]
acts by vertex relabeling. Every subgroup of \(F\) is conjugate to exactly one of the following six groups. Its **compact cubical orbit space** \(D/H\) has the stated homeomorphism type, while the ordinary continuous orbit space \(X/H\) is **homotopy equivalent** to that surface:

| Subgroup \(H\) | Order | Homeomorphism type of \(D/H\) (homotopy type of \(X/H\)) |
|---|---:|---|
| Trivial | 1 | Closed nonorientable surface of genus \(7\) |
| \(C_2=\langle x\mapsto- x\rangle\) | 2 | Once-punctured Klein bottle |
| \(C_4=\langle x\mapsto2x\rangle\) | 4 | Möbius band |
| \(C_5=\langle x\mapsto x+1\rangle\) | 5 | Closed nonorientable surface of genus \(3\) |
| \(D_5=\langle x\mapsto x+1,\ x\mapsto-x\rangle\) | 10 | Closed disk |
| \(F\) | 20 | Closed disk |

In particular, the compact cyclic fivefold quotient \(D/C_5\) is a closed nonorientable genus-three surface, with \(H_1(X/C_5;\mathbb Z)\cong\mathbb Z^2\oplus\mathbb Z/2\). The compact order-two quotient \(D/C_2\) is a once-punctured Klein bottle, and \(H_1(X/C_2;\mathbb Z)\cong\mathbb Z^2\) is torsion-free. These cases have the same first rational Betti number but different integral topology.

## Assumptions and scope
The graph is the one-dimensional geometric realization, not a planar drawing or the complete-graph clique complex. Particles are indistinguishable and cannot collide. All orbit spaces are ordinary quotients by actual vertex permutations, not homotopy or Borel quotients. Let \(D\subset X\) be the compact unordered Abrams cubical complex: its cells are unordered pairs of closed, disjoint graph cells, with one cell factor per particle. It has \((10,30,15)\) cubical cells in dimensions \(0,1,2\), respectively. Every \(H\le F\) preserves \(D\). The standard equivariant two-particle deformation onto \(D\) is described below, so the theorem applies to the continuous configuration space as stated, not merely to its cubical approximation.

## Proof
**1. Complete subgroup list.** The translation subgroup \(T=\{x\mapsto x+b\}\cong C_5\) is normal in \(F\), and \(F/T\cong C_4\). A subgroup containing \(T\) is the preimage of one of the three subgroups of \(C_4\), producing \(C_5,D_5,F\). If \(H\cap T=1\), projection embeds \(H\) into \(C_4\), so \(H\) is cyclic of order \(1,2\), or \(4\). A nonidentity affine map \(x\mapsto ax+b\) with \(a\ne1\) has the unique fixed point \(b/(1-a)\); translating that point to zero conjugates it to a multiplication map. Hence \(H\) is conjugate to one of \(1,C_2,C_4\). These six choices are inequivalent by order. The standalone verifier also enumerates all \(14\) subgroups and confirms their six conjugacy classes.

**2. Equivariant comparison with continuous configurations.** The equivariant two-particle retraction used in published work on complete-graph configuration quotients can also be written directly. For a same-edge pair with coordinates \(0\le s<t\le1\), move it at time \(u\in[0,1]\) to \(\{(1-u)s,(1-u)t+u\}\). For particles on incident edges meeting at a vertex, at nonnegative distances \(s,t\) from that vertex, move them to
\[
\big((1-u)+u/\max(s,t)\big)(s,t).
\]
Use the second formula also when one particle is at the common vertex, and fix configurations whose closed supporting cells are disjoint. The formulas agree when one particle reaches an endpoint; they are invariant under reversal of edge coordinates and under graph automorphisms. The excluded simultaneous collision \(s=t=0\) is never needed. They remain collision-free, fix \(D\) pointwise, and reach \(D\) at time one. Thus \(X/H\) strongly deformation retracts onto \(D/H\) for every subgroup \(H\le F\). This retraction yields the stated homotopy equivalences for continuous configuration quotients. It does **not** assert a homeomorphism of a noncompact continuous quotient with a compact cubical quotient. 

**3. Orbit triangulations.** Barycentrically triangulate every square of \(D\). A triangle is a strict flag \(v<e<q\) of cubical cells. Group elements preserve cubical dimension, so every simplex has distinct rank types and the quotient is the finite \(\Delta\)-complex of flag orbits, allowing parallel edges. Each cubical vertex is an unordered pair of distinct graph vertices; each cubical edge consists of a vertex and a nonincident graph edge; each square is a pair of disjoint graph edges. A cubical support \(a\) is a face of support \(b\) exactly when its two particle supports can be matched so that each is equal to, or an endpoint of, the corresponding support of \(b\). Thus all flag inclusions and permutation actions are fully explicit.

As a compact cross-check, the fixed-flag counts in dimensions \(0,1,2\) are \((55,180,120)\) for the identity, \((0,0,0)\) for a nonidentity translation, \((7,4,0)\) for an affine involution, and \((1,0,0)\) for an affine element of order four. The full affine group contains respectively \(1,4,5,10\) elements of these four types. Burnside averaging yields, for example, the full-group orbit counts \((5,10,6)\), and the subgroup counts follow similarly. The code checks all fixed flags directly, rather than assuming these fixed-count profiles.

The orbit counts and surface invariants are:

| \(H\) | Flag vertices | Flag edges | Flag triangles | \(\chi\) | Boundary circles | Orientable? |
|---|---:|---:|---:|---:|---:|---|
| \(1\) | 55 | 180 | 120 | \(-5\) | 0 | No |
| \(C_2\) | 31 | 92 | 60 | \(-1\) | 1 | No |
| \(C_4\) | 16 | 46 | 30 | 0 | 1 | No |
| \(C_5\) | 11 | 36 | 24 | \(-1\) | 0 | No |
| \(D_5\) | 9 | 20 | 12 | 1 | 1 | Yes |
| \(F\) | 5 | 10 | 6 | 1 | 1 | Yes |

**4. Local surface verification and classification.** For every flag-edge orbit, count its incident flag-triangle orbits, with multiplicity. Every edge has one or two incident triangles; the respective numbers of boundary edges are \(0,4,2,0,4,2\) for the groups in table order. At every flag-vertex orbit, form its link whose vertices are the incident edge orbits and whose edges come from adjacent triangles. Every link is a single circle or a single interval, with no disconnected, branching, or isolated link. The boundary-edge graphs have respectively \(0,1,1,0,1,1\) connected components; each component is a circle. Hence all six quotients are connected compact surfaces of exactly the indicated number of boundary circles.

Orientability is decided without relying on rational Betti numbers: give each ordered full flag \(v<e<q\) its standard rank-order orientation and propagate choices of triangle signs across common interior edges, requiring cancellation of the induced edge signs. This integer sign system is solvable exactly for \(D_5\) and \(F\); it is inconsistent for \(1,C_2,C_4,C_5\). In every case, Euler characteristic equals the alternating flag count above. The classification theorem for connected compact surfaces then gives, uniquely, the six types in the finding. For a closed nonorientable genus-three surface the abelianized surface-group presentation gives \(H_1\cong\mathbb Z^2\oplus\mathbb Z/2\); a once-punctured Klein bottle has free fundamental group of rank two and hence \(H_1\cong\mathbb Z^2\). This proves the integral distinction.

All finite incidence, link, boundary, orientability, group-conjugacy, and Burnside computations cited here are reproduced by `verify.py` with no external libraries. This is an exhaustive check of all cells and all members of the finite group, not a numerical sample.

## Verification
Run `python3 verify.py` with Python 3 from the directory containing the attached file. Its deterministic standard output is recorded as `verification_output.txt` and ends in `VERIFY_OK`. It independently counts flag orbits by both explicit orbit enumeration and Burnside's fixed-flag formula, checks that the full affine group has \(14\) subgroups in the six indicated conjugacy classes, checks every quotient vertex link and boundary component, propagates orientation signs, and derives surface type by Euler characteristic. All counts use finite exact integer calculations. The verification file is an integral part of the claim-to-evidence package; the mathematical reduction and surface classification are described above.

## Relationship to prior work
Abrams and Ghrist (2000) established that the **ordered** deleted-product configuration complex of \(K_5\) is an orientable genus-six surface, and gave the discrete cell counts and a deformation-retraction criterion. This does not classify these ordinary **unordered subgroup** quotient surfaces. Barnett and Farber (2009) developed general two-particle graph-configuration topology, without this affine subgroup census. Published complete-graph results classify the full symmetric and alternating vertex-relabeling quotients, and a separate published calculation determines the ordered \(S_5\)-equivariant rational homology and its exchange involution. In particular, existing rational characters constrain Betti numbers of these subgroup quotients, but do not determine boundary components, orientability, or homeomorphism types. The full-symmetric/alternating quotients also do not determine the homotopy types of intermediate subgroups. These results are credited rather than claimed again.

## Limitations
The homeomorphism types are asserted for the **compact** cubical quotients \(D/H\). The corresponding noncompact continuous spaces \(X/H\) have the listed **homotopy types** through an equivariant strong deformation retraction, and are not claimed homeomorphic to compact surfaces. The result concerns exactly two particles on the standard geometric complete-five-vertex graph, and exactly the affine subgroups described above. It does not classify all subgroups of \(S_5\), higher particle numbers, or configuration spaces with collisions permitted. No external independent mathematical audit has been performed. Despite specific source comparisons, equivalent unindexed literature remains a publication-priority risk.

## References
1. A. Abrams and R. Ghrist, *Finding topology in a factory: configuration spaces*, arXiv:math/0009118, first public 2000-09-12, Sections 5–6, https://arxiv.org/abs/math/0009118.
2. K. Barnett and M. Farber, *Topology of Configuration Space of Two Particles on a Graph, I*, arXiv:0903.2180, first public 2009-03-12, https://arxiv.org/abs/0903.2180.
3. *Alternating-symmetry exceptions in two-point complete-graph configuration quotients*, published research record, https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-alternating-symmetry-exceptions-in-two-point-complete-graph-conf--10eeb4d433b5.
4. *The full vertex-permutation and particle-exchange homology of two configurations on the Kuratowski graph*, published research record, https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-the-full-vertex-permutation-and-particle-exchange-homology-of-tw--31c73297535e.
