# A sphere survives the full dihedral quotient of the seven-point matching complex

## Finding

Let \(\mathcal M_7\) be the matching complex of the complete graph on the vertex set \(\mathbb Z/7\mathbb Z\). Its nonempty simplices are matchings of sizes one, two, and three. The fourteen-element dihedral group \(D_7\) acts through all permutations \(x\mapsto \pm x+t\) of this vertex set. For the **ordinary topological orbit space** \(Y=|\mathcal M_7|/D_7\),

\[
Y\simeq S^2.
\]

Indeed, a canonical orbit-cell subdivision undergoes twenty-seven explicit elementary collapses onto a closed surface of Euler characteristic two. Consequently, \(Y\) is simply connected and has integral homology \(H_0\cong H_2\cong\mathbb Z\), with all other groups zero.

## Assumptions and scope

The graph is the loopless complete graph on exactly seven labels, not the seven-cycle graph. Each edge \(\{a,b\}\) is a vertex of the matching complex; a collection of such edges is a simplex precisely when its endpoints are pairwise disjoint. The action of \(D_7\), including all reflections, is by simultaneous label permutations. The claim is a homotopy equivalence of ordinary geometric quotients, not a homotopy-orbit or Borel-space statement. No higher-label or different-subgroup classification is claimed.

## Proof

**The orbit cell structure.** A graph edge is represented by its increasing pair of labels, and a matching by a lexicographically sorted tuple of such edges. There are respectively \(21,105,105\) nonempty matching faces of cardinalities one, two, and three. The barycentric subdivision consists of *strict chains* of nonempty faces, giving \(231,840,630\) cells of dimensions zero, one, two. Every group element preserves face cardinality, hence fixes every vertex of any chain simplex it stabilizes: the action has no simplex inversions after subdivision. Therefore the orbit chains, with their induced boundary incidences, form a valid finite \(\Delta\)-complex for the ordinary quotient.

Use the lexicographically minimal image under all fourteen affine permutations as the canonical representative of each chain. All seven reflections are conjugate, and each fixes \(19,24,6\) original chains in dimensions zero, one, two. No nonidentity sevenfold rotation fixes a chain: any nonempty matching face has fewer than seven graph edges, whereas a nontrivial rotation has seven-element orbits on individual graph edges. Burnside's formula gives the quotient cell counts

\[
\bigl((231+7\cdot19)/14,\ (840+7\cdot24)/14,\ (630+7\cdot6)/14\bigr)=(26,72,48).
\]

**Explicit elementary collapses.** Index orbit cells lexicographically from zero, separately in each dimension. Repeatedly remove the smallest-index edge incident to exactly one surviving triangle, with that triangle; once no such pair remains, repeatedly remove the smallest-index vertex incident to exactly one surviving edge, with that edge. Every pair is a valid elementary collapse, since the paired lower cell is then a free face of the upper cell. Using the notation \((d,i,j)\) for the lower cell \(i\) and upper cell \(j\), with \(d=2\) for a triangle–edge pair and \(d=1\) for an edge–vertex pair, the exact ordered certificate is:

```text
(2,3,2) (2,9,7) (2,15,0) (2,0,1)
(2,1,13) (2,2,5) (2,19,24) (2,21,45)
(2,40,27) (2,45,17) (2,31,26) (2,39,25)
(2,34,19) (2,46,40) (2,58,35) (2,59,36)
(2,56,34) (2,57,38)
(1,1,16) (1,2,26) (1,3,38) (1,9,69)
(1,16,50) (1,20,49) (1,18,64)
(1,23,68) (1,24,71)
```

**The surviving surface.** The remaining complex has exactly \(17\) vertices, \(45\) edges and \(30\) triangles. It is connected; every edge lies in precisely two distinct surviving triangles. Each vertex link is a connected 2-regular *multigraph*, hence a circle. The distribution of link lengths is three of length two, six of length four, five of length six, and three of length ten. Parallel edges in a two-edge link are retained as distinct link edges. It follows that the remaining \(\Delta\)-complex is a connected closed surface. Its Euler characteristic is

\[
17-45+30=2.
\]

By the classification of connected closed surfaces, it is a two-sphere. Elementary collapses preserve homotopy type, proving the finding and all stated homotopy and integral homology consequences.

## Verification

Run `python3 verify_m7_dihedral.py` with a standard Python 3 interpreter; the script has no nonstandard package dependencies or external data. It constructs all matchings, strict chains, all fourteen group images and orbit incidences, checks the reflection fixed-chain counts, recomputes all twenty-seven ordered free pairs, and checks every incidence, surviving vertex link, connectivity, and Euler characteristic. The successful terminal marker is `M7_D7_QUOTIENT_COLLAPSES_TO_SPHERE_OK`. The certificate is a complete finite proof of the reduction, not a sample calculation or a rank-only homology test. A separate rational/integer chain calculation also gave ranks \(25\) and \(47\) for the first and second quotient boundaries and no torsion Smith factors, consistent with \(S^2\); the elementary-collapse proof does not depend on that ancillary computation.

## Relationship to prior work

Bouc's classical analysis computes topological properties of the unquotiented matching complex, including its seven-label fundamental group. Jonsson's later exact-sequence work recovers the order-three first-homology class, while Mondal–Mukherjee–Saha compute the integral homology \(H_1(\mathcal M_7;\mathbb Z)\cong\mathbb Z/3\mathbb Z\), \(H_2(\mathcal M_7;\mathbb Z)\cong\mathbb Z^{20}\). The published sevenfold *rotation*-quotient computation describes a different orbit space with order-twenty-one fundamental group and two free second-homology generators. This does not imply the full-dihedral answer: the additional reflection has nontrivial stabilizers and its induced action on the cyclic quotient's cells must be checked. The new closed-surface collapse is the essential input here.

## Limitations

The result concerns precisely seven labels and the full label-dihedral group. The residual novelty risk is a mathematically equivalent unindexed computation or a stronger equivariant result not located in the inspected literature; the full text of the closest published rotation-only record could not be retrieved during this comparison. No independent mathematical audit has been performed. The proof identifies homotopy type, not a homeomorphism of the original orbit space to a sphere: the twenty-seven collapses are generally nontrivial.

## References

1. S. Bouc, *Homologie de certains ensembles de 2-sous-groupes des groupes symétriques*, Journal of Algebra 150 (1992), 158–186, §2.2.3. DOI: https://doi.org/10.1016/S0021-8693(05)80054-7 ; author-hosted complete text: https://www.lamfa.u-picardie.fr/bouc/article-jofa.pdf
2. J. Jonsson, *Exact Sequences for the Homology of the Matching Complex*, arXiv:1203.5641 (first arXiv posting 2012-03-26), §4.1. https://arxiv.org/abs/1203.5641
3. A. Mondal, S. Mukherjee, K. Saha, *Topology of matching complexes of complete graphs via discrete Morse theory*, Discrete Mathematics & Theoretical Computer Science 26:3 (2024), Theorem 1.3 and §4.2.3. https://dmtcs.episciences.org/14584/pdf
4. *The sevenfold rotation quotient of the seven-point matching complex has cyclic fundamental group of order twenty-one*, published mathematical result. https://github.com/published-finding corpus/2026/tree/main/2026/11/17/SCOPE-the-sevenfold-rotation-quotient-of-the-seven-point-matching-comp--a542e17c25df
