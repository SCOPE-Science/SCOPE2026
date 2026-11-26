# Full symmetry character of the Möbius–Kantor noncover complex

## Finding
Let \(\mathcal H\) be the unique eight-point, eight-line Möbius–Kantor configuration and let \(K=\operatorname{NC}(\mathcal H)\) be its noncover complex. Write \(G=\operatorname{Aut}_{\mathrm{points}}(\mathcal H)\), meaning the group of permutations of its eight points preserving the set of eight lines. Then \(|G|=48\). Its unique nonidentity central involution partitions the points into four pairs, denoted \(\mathcal B\); the action on these pairs identifies \(G/\langle z\rangle\cong S_4\).

The new assertion is the complete rational equivariant homology classification
\[
\widetilde H_2(K;\mathbb Q)\cong_G\operatorname{Inf}_{S_4}^{G}(\operatorname{sgn}\otimes\mathbb Q[\mathcal B]),\qquad
\widetilde H_3(K;\mathbb Q)\cong_G\mathbf1.
\]
The remaining reduced rational homology groups vanish. Thus \(\widetilde H_2\) decomposes into the sign character and the sign-twist of the three-dimensional standard representation of \(S_4\). Its full invariant subspace is zero, while the degree-three invariant subspace has dimension one. This refines an existing nonequivariant homotopy calculation, not a new homotopy-type determination.

## Assumptions and scope
Use point labels \(0,1,\ldots,7\) and exactly these eight line triples:
\[
(0,1,4),(0,3,7),(0,5,6),(1,2,5),(1,6,7),(2,3,6),(2,4,7),(3,4,5).
\]
A subset of points is a face of \(K\) exactly when it is disjoint from at least one displayed triple. These triples are the line-neighborhoods of the two bipartition classes of the generalized Petersen graph \(GP(8,3)\). Every automorphism in \(G\) acts simplicially on \(K\). Only point-preserving incidence automorphisms are considered; exchanging points with lines is not an action on this fixed vertex set. Every representation is over \(\mathbb Q\), not an asserted integral module splitting.

## Proof
**Previously determined underlying topology.** The cited Möbius–Kantor independence-complex classification already constructs this exact eight-point noncover complex as the Alexander-dual incidence model, enumerates \(140\) nonempty faces, and proves \(K\simeq\bigvee^4 S^2\vee S^3\). In particular, reduced integral homology is free of ranks four in degree two and one in degree three, vanishing otherwise. The accompanying independent computation in `verify_mk.py` reconstructs all \(140\) faces with dimension counts \((8,28,56,40,8)\). It produces an explicit acyclic matching of \(67\) Hasse pairs, with critical masks \(1\) in dimension zero, \(14,22,82,164\) in dimension two, and \(204\) in dimension three. It exhaustively topologically sorts \(424\) oriented face incidences, then computes the single integral Morse boundary vector to be zero. Since the two-skeleton of the resulting simply connected CW complex is \(\bigvee^4S^2\), the vanishing attaching degree yields the stated background homotopy type, without using finite-field inference to prove an integral assertion.

**Automorphism and canonical pair quotient.** The verifier exhausts all \(8!=40320\) point permutations, retaining exactly \(48\) that preserve the eight line triples. It computes the center as identity and the involution \(z=(0\,2)(1\,3)(4\,6)(5\,7)\). Therefore \(\mathcal B=\{\{0,2\},\{1,3\},\{4,6\},\{5,7\}\}\). Its induced action on the four pairs has exactly \(24\) permutations; hence the quotient is \(S_4\) with kernel \(\{1,z\}\).

**Degree-three character.** Let \(C_j\) be the simplicial signed chain group oriented by increasing point labels. The verifier specifies an explicit integral three-cycle supported on \(19\) tetrahedra (the list is encoded by `zs` as coefficients relative to the sorted degree-three faces). It checks its signed integral boundary is zero. Over each of \(\mathbb F_3\) and \(\mathbb F_5\), exact row reduction constructs a linear functional on \(C_3\) annihilating all eight four-simplex boundaries and pairing to one with this cycle. It then evaluates the action of all \(48\) automorphisms on this cycle and obtains character value one for each, independently in both fields. Since integral degree-three homology has rank one and no torsion, every automorphism acts on it by either \(+1\) or \(-1\); the distinct reductions modulo three decide the integral sign. Thus the rational third-homology representation is trivial.

**Degree-two character.** For each of the same \(48\) automorphisms \(g\), an exact signed simplicial Lefschetz sum over all \(140\) nonempty faces gives
\[
\widetilde L(g)=\sum_{\sigma\ne\varnothing}(-1)^{\dim\sigma}\operatorname{sgn}(g|_\sigma)-1,
\]
where only setwise fixed simplices contribute. Homology concentration and the degree-three result imply \(\chi_2(g)=\widetilde L(g)+1\). For every element, direct comparison gives
\[
\chi_2(g)=\operatorname{sgn}(\overline g)\,|\operatorname{Fix}_{\mathcal B}(\overline g)|,
\]
where \(\overline g\) is its permutation of the four pairs. Its values occur with multiplicities \(12,18,16,2\) for traces \(-2,0,1,4\), respectively. Rational representations of a finite group are determined by their ordinary characteristic-zero characters, giving the claimed isomorphism. The signed-trace formulas also give invariant multiplicities \(0\) and \(1\) in degrees two and three, respectively.

## Verification
Execute `python3 verify_mk.py`; no external Python packages are needed. The program verifies all eight line triples, the complete \(140\)-face set, all \(424\) face incidences, the \(67\)-pair discrete-Morse acyclicity, the exact integral Morse differential, all \(48\) automorphisms and their order-\(24\) action on the canonical four pairs, the independent modular degree-three quotient actions, and all degree-two signed Lefschetz identities. `verification_output.txt` records the reproduced output. The finite verification is exhaustive for the explicitly defined eight-point object; it does not establish any unspecific higher-order family theorem.

## Relationship to prior work
The published Möbius–Kantor independence-complex classification (listed in the references) already constructs precisely this noncover complex and establishes its integral nonequivariant homotopy type. The present finding does **not** claim the four two-spheres and one three-sphere as new. A second published same-graph result establishes a character only for the cyclic subgroup generated by simultaneous rotation of the sixteen-vertex incidence graph. Such a subgroup character does not determine the action of all \(48\) point-preserving incidence automorphisms; in particular, it does not determine the sign-twisted four-pair permutation character under the induced \(S_4\) quotient. Kim and Kim's noncover-complex paper introduces the general duality and classifies tight paths and tight cycles, not this full symmetry representation. Matsushita and Wakatsuki classify independence complexes of rectangular grid graphs, a different family.

## Limitations
The object is the canonical eight-point configuration only. The isomorphisms are rational representation statements; no integral-equivariant lattice decomposition or equivariant homotopy equivalence is asserted. Complete absence of equivalent unpublished or unindexed work cannot be established by indexed searches, and potentially relevant general symmetry literature may require further human scrutiny. The prior nonequivariant homotopy classification is acknowledged in full. Independent external audit has not been performed.

## References
1. T. Matsushita and S. Wakatsuki, *Independence complexes of \((n\times6)\)-grid graphs*, arXiv:2207.10363v1 (first publicly posted 2022-07-21), primary MSC2020 55P10; full article inspected.
2. J. Kim and M. Kim, *Domination numbers and noncover complexes of hypergraphs*, arXiv:2101.01850v1 (first publicly posted 2021-01-06), Sections 1 and 3; full article inspected.
3. S. Tsukuda, *Independence complexes and incidence graphs*, Contributions to Discrete Mathematics 12 (2017), 28–46, DOI:10.55016/ojs/cdm.v12i1.62277, Corollary 4.11.
4. *Integral homotopy type of the Möbius–Kantor independence complex*, publicly accessible 2026 research record, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-integral-homotopy-type-of-the-m-bius-kantor-independence-complex--b0d62cfde5f3; complete result statement and proof inspected.
5. *Cyclic symmetry on Möbius–Kantor independence homology*, publicly accessible 2026 research record, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-cyclic-symmetry-on-m-bius-kantor-independence-homology--1c198fd64c4e; complete result statement and proof inspected.
