# Sharp stabilization of symmetry quotients of ordered star-graph configuration spaces

## Finding

Let \(S_m\) denote a star with \(m\ge3\) equal-length arms, and let \(\operatorname{Conf}_p(S_m)\) be the space of \(p\ge4\) *labeled, pairwise distinct* particles. A subgroup \(H\le S_m\) acts by permuting arms, not particle labels. For \(g\in H\), write \(f(g)\) for its number of fixed arms, and put \(R_q(f)=\prod_{j=0}^{q-1}(f+j)\) for \(q\ge1\), including \(R_q(0)=0\).

**Theorem.** For every integer \(p\ge4\), \(m\ge3\), and every subgroup \(H\le S_m\), the geometric orbit space \(\operatorname{Conf}_p(S_m)/H\) has the homotopy type of a connected finite graph. More precisely, it is homotopy equivalent to a wedge of exactly
\[
\beta_p(H)=1-\frac{1}{|H|}\sum_{g\in H}\bigl(2p-1-(p-1)f(g)\bigr)R_{p-1}(f(g))
\]
circles. Consequently its fundamental group is free of rank \(\beta_p(H)\); its integral first homology is \(\mathbb Z^{\beta_p(H)}\), with no torsion; and every integral homology group above degree one vanishes. The expression is necessarily a nonnegative integer.

**Sharp stabilization.** For the full arm-permutation group, the orbit graphs themselves (not only their homotopy types) are combinatorially isomorphic for all \(m\ge p\). The bound is sharp in every particle number \(p\ge4\):
\[
\beta_p(S_p)-\beta_p(S_{p-1})=p-1.
\]
The stable circle ranks for \(p=4,5,6,7,8\) are, respectively, \(12,180,2220,27300,351960\). Here \(S_m\) denotes a permutation group in \(\beta_p(S_m)\), whereas \(S_m\) in \(\operatorname{Conf}_p(S_m)\) denotes the star; context distinguishes these conventional usages.

## Assumptions and scope

A star has one central vertex and \(m\) terminal edges, each identified with a unit interval. Coordinates in the ordered configuration space are distinct and are allowed anywhere on the graph, including vertices. Quotienting identifies configurations related by *graph automorphisms permuting the whole arms*, never configurations differing only by particle relabeling. Quotients are ordinary topological orbit spaces, not homotopy quotients or unordered-particle configurations. The bound \(p\ge4\) isolates the multiparticle extension beyond previously studied two-particle equivariant calculations; the same elementary proof works for \(p\ge2\). For the full-group stabilization assertion compare the orbit graphs at different numbers \(m\) of arms by forgetting unoccupied arm names.

## Proof

**1. Equivariant one-dimensional graph model.** Use the standard Lütgehetmann configuration-space cube model, described in detail for star graphs in Wawrykow's Section 3. Its vertices are configurations in which each particle is either at the central vertex or belongs to one of the totally ordered queues on the arms, with at most one particle at the central vertex; the particle nearest the center may move between an arm and the center along a model edge. On a star the resulting cube complex is a graph. Its deformation retraction from the continuous configuration space is natural under arm-permuting graph isomorphisms: the cells and coordinate straightening use only the central vertex, relative radial order on each arm, and the identical arm parametrizations, so relabeling arms commutes with the construction. Denote this \(H\)-invariant graph by \(K_{p,m}\). It is connected when \(m\ge3\), because a third arm can temporarily hold particles while labels are rearranged through the center. Hence \(\operatorname{Conf}_p(S_m)/H\simeq K_{p,m}/H\). This equivariance is essential: nonequivariant equivalence alone would not justify the assertion about quotients.

Here is a complete combinatorial description of \(K_{p,m}\), sufficient to reconstruct the quotient. An A-vertex is an \(m\)-tuple of possibly empty ordered lists whose disjoint union is the set of \(p\) labels; each list is read from center outward. A B-vertex consists of a distinguished label \(c\) at the center and such an \(m\)-tuple partitioning the other \(p-1\) labels. For each B-vertex and each chosen arm \(i\), there is exactly one edge to the A-vertex formed by prepending \(c\) to list \(i\). Distinct choices can give distinct quotient edges, even if their quotient endpoints agree: count edge *orbits*, not endpoint pairs. The arm group permutes tuple positions; it never exchanges A and B vertex types, so there are no edge inversions. Consequently \(K_{p,m}/H\) is an ordinary connected finite graph, with no orbifold or higher-dimensional cells. This already proves the qualitative homotopy and torsion statements.

**2. Exact fixed-cell counts.** An element \(g\) can fix an A-vertex only if every occupied arm is individually fixed; a moved arm must contain the empty list, since labels are distinct and not moved. Let \(f=f(g)\). Ordered lists of \(p\) distinguishable labels distributed among \(f\) specified arms are counted by \(p!\binom{f+p-1}{p}=R_p(f)\). Thus the number of A-vertices fixed by \(g\) is \(A_g=R_p(f)\). Choose the center label in \(p\) ways; the others then form \(f\) queues, so \(B_g=pR_{p-1}(f)\) B-vertices are fixed. An edge is fixed precisely when the B-data are fixed and its selected target arm is individually fixed; therefore \(E_g=fpR_{p-1}(f)\). In particular this holds also when \(f=0\), where all three fixed-cell counts vanish. The fixed-cell Euler count is
\[
 A_g+B_g-E_g=[f+p-1+p(1-f)]R_{p-1}(f)
              =[2p-1-(p-1)f]R_{p-1}(f).
\]
Burnside's orbit-counting identity applied separately to vertices and edges yields \(V_H-E_H=|H|^{-1}\sum_g(A_g+B_g-E_g)\). Since \(K_{p,m}/H\) is connected, its first Betti number is \(E_H-V_H+1\), proving the formula and integral conclusions. This argument derives the integer directly as a graph rank rather than assuming it from a character table.

**3. Combinatorial stabilization.** An orbit of an A-vertex under all arm permutations is uniquely specified by the *unlabeled multiset of nonempty ordered lists* of particle labels. There are at most \(p\) such lists. An orbit of a B-vertex is specified by the center label together with a multiset of at most \(p-1\) nonempty lists. An orbit of a model edge additionally marks the target arm/list, with the option that the target is empty. Once \(m\ge p\), every A-data type is realizable, and every B-data type has at least one empty arm available for the latter option. Thus the orbit vertex and edge sets, including their incidence relations and edge multiplicities, are literally independent of \(m\ge p\). This proves stabilization as graphs.

**4. Sharpness.** Put \(F_p(f)=[2p-1-(p-1)f]R_{p-1}(f)\). As a polynomial in \(f\), it has degree \(p\) with leading coefficient \(-(p-1)\). Expand in falling-factorial polynomials \((f)_{\underline j}=f(f-1)\cdots(f-j+1)\). The coefficient at degree \(p\) is again \(-(p-1)\). For a uniformly random permutation of \(m\) symbols, the mean of \((f)_{\underline j}\) is exactly \(1\) when \(j\le m\), because it counts injective lists of \(j\) fixed points and each ordered list is fixed with probability \(1/(m)_{\underline j}\); it is \(0\) when \(j>m\). Therefore the mean of \(F_p(f)\) on \(S_p\) differs from its mean on \(S_{p-1}\) by precisely \(-(p-1)\), while all lower falling-factorial terms agree. The Betti formula has a minus sign, hence \(\beta_p(S_p)-\beta_p(S_{p-1})=p-1\). In particular the stabilization threshold cannot be lowered.

## Verification

The accompanying standalone `verify.py` enumerates distinct-label queues and B-center states directly. For each tested subgroup it computes the actual orbit graph's numbers of vertex and edge orbits, retaining parallel edges, and checks \(E_H-V_H+1\) against the fixed-arm formula using exact integers. The 42 cases cover \(p\in\{2,3,4\}\), \(m\in\{3,4,5\}\), and feasible trivial, cyclic, dihedral, alternating and full symmetric groups. These finite experiments are corroboration; the proof above establishes every parameter in the stated range, including groups that were not enumerated. To replay: `python3 verify.py`. Its terminal output is in `verify_output.txt`; the last line is `ALL_VERIFY_OK cases=42`. Independently evaluating the exact permutation mean at \(m=p-1,p\) for \(p=4,\ldots,8\) gives pairs \((9,12),(176,180),(2215,2220),(27294,27300),(351953,351960)\), as predicted by sharpness.

## Relationship to prior work

Ramos and Yun, arXiv:2606.13813v1 (11 June 2026), Theorems 3.2--3.3, give stable arm-permutation *rational homology representations* for **two** ordered or unordered particles on stars. Wawrykow, arXiv:2401.13821v1, studies ordered-star homology for arbitrary particle counts and quotes Lütgehetmann's graph deformation model (Section 3) and Ghrist's nonequivariant free-rank formula. Thus neither the graph-spine construction itself, nor the nonequivariant rank, nor the two-particle case is claimed new. The asserted addition is the exact **topology of geometric arm-subgroup quotients for every \(p\ge4\)** and the sharp **graph-level** full-automorphism stabilization. It is not a consequence merely of knowing ranks of the unquotiented configuration spaces. Earlier work may have an equivalent orbit-graph formula under different terminology; the checked literature and mathematical-record comparisons did not locate one.

## Limitations

The theorem does not address particle-label exchange, mixed arm/particle group actions, non-star graphs, the more general graph braid-group action on cells, or integral equivariant homology module decompositions of the unquotiented space. The model requires at least three arms for connectedness; the displayed beta formula is not asserted for two-arm intervals. The conclusion is a homotopy classification, not an assertion that the topological quotient itself is a graph homeomorphically. Priority remains provisional pending exhaustive independent literature review.

## References

1. Eric Ramos and Claudia He Yun, *Computing stable homology representations of graph configuration spaces*, arXiv:2606.13813v1 (first public 11 June 2026), Theorems 3.2 and 3.3, Section 3.1.
2. Nicholas Wawrykow, *Homology generators and relations for the ordered configuration space of a star graph*, arXiv:2401.13821 (first public January 2024), Section 3 and Proposition 3.3.
3. D. Lütgehetmann, finite cubical graph-configuration model, cited as [Lüt14, Theorem 2.3] in Wawrykow, Section 3.
4. R. Ghrist, free fundamental-group rank of ordered star configurations, cited as [Ghr01, Proposition 4.1] in Wawrykow, Section 3.
