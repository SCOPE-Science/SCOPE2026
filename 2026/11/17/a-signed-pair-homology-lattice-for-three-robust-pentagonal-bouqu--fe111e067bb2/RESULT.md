# A signed pair-homology lattice for three-robust pentagonal bouquets

## Finding
For every integer \(m\ge1\), let \(F_m\) be the graph obtained by identifying one vertex in each of \(m\) unfilled five-cycles, with no other vertex identifications or edges. Write \(R_3(F_m)\) for its three-robust clique complex: the abstract simplicial complex whose faces are vertex sets containing no independent triple in \(F_m\). Then
\[
\boxed{\left|R_3(F_m)\right|\simeq\bigvee^{\binom m2}S^3.}
\]
Here a wedge with zero spheres is a point. In particular, for \(m\ge2\) its only nonzero reduced integral homology group is \(\widetilde H_3\cong\mathbb Z^{\binom m2}\); for \(m=1\) the complex is a simplex.

The assertion includes an **integral equivariant homology classification**. For \(m\ge2\), the complete graph automorphism group is \(C_2^m\rtimes\mathfrak S_m\): each \(C_2\) reflects a single pentagon while fixing the common vertex, and \(\mathfrak S_m\) permutes the petals. There is a primitive integral basis \(\{z_{ij}:1\le i<j\le m\}\) of \(\widetilde H_3\) for which a reflection in petal \(i\) multiplies \(z_{jk}\) by \(-1\) precisely when \(i\in\{j,k\}\), and a petal permutation sends \(z_{ij}\) to \(z_{\min(\sigma i,\sigma j),\max(\sigma i,\sigma j)}\) **without a swapping sign**. Thus this is the squarefree degree-two symmetric monomial lattice of the signed coordinate-permutation module, not its exterior-square lattice.

The subgroup \(\mathfrak S_m\) has a one-dimensional fixed rational third-homology subspace, whereas the full automorphism group and the reflection subgroup \(C_2^m\) each have zero fixed third homology. Hence the full geometric symmetry quotient has no positive-degree rational homology. These are statements about homology and the ordinary homotopy type, not an equivariant wedge decomposition.

## Assumptions and scope
All graphs are finite, simple, loopless, and undirected. Write the common vertex as \(o\), and the private vertices of petal \(i\) as \(a_i,b_i,c_i,d_i\). Its edges are exactly \(oa_i,a_ib_i,b_ic_i,c_id_i,d_io\); there are no cross-petal edges. The realization of a simplicial complex is its ordinary finite CW realization. The parameter \(m\) is any positive integer, with no upper cutoff. The group description assumes \(m\ge2\); at \(m=1\) the automorphism group is different but the complex is contractible.

## Proof
**1. Exhaustive support decomposition.** A face cannot contain private vertices from three distinct petals: any three such vertices form an independent triple. For each \(i\), let \(T_i\) denote the induced complex on the five vertices of petal \(i\). Since \(\alpha(C_5)=2\), \(T_i\) is the entire four-simplex on those vertices. Thus \(Q=\bigcup_{i=1}^mT_i\) is a simplicial cone with apex \(o\) and is contractible. For each pair \(i<j\), let \(K_{ij}\) be the induced subcomplex on those two complete petals (nine vertices). The support observation gives
\[
R_3(F_m)=Q\cup\bigcup_{1\le i<j\le m}K_{ij}.
\]
Any intersection of two distinct \(K_{ij}\) lies in \(Q\): if the pairs share a petal the intersection is the corresponding \(T_i\), otherwise it is the vertex \(o\). Also \(K_{ij}\cap Q=T_i\cup T_j\). As \(Q\) is a contractible CW subcomplex, the quotient map \(R_3(F_m)\to R_3(F_m)/Q\) is a homotopy equivalence. The quotient is exactly
\[
R_3(F_m)/Q\cong\bigvee_{i<j}K_{ij}/(T_i\cup T_j),
\]
with the wedge at the point representing \(Q\). Since \(T_i\cup T_j\) is itself a contractible CW subcomplex (two four-simplices meeting in \(o\)), each quotient \(K_{ij}/(T_i\cup T_j)\) is homotopy equivalent to \(K_{ij}\). Consequently the entire problem reduces to one nine-vertex two-petal complex and is not an extrapolation from finitely many cases.

**2. Complete finite discrete-Morse certificate for two petals.** Number the vertices of \(F_2\) as \(0=o\), \(1=a_1\), \(2=b_1\), \(3=c_1\), \(4=d_1\), \(5=a_2\), \(6=b_2\), \(7=c_2\), \(8=d_2\). Represent a face by the integer bitmask \(\sum_{v\in S}2^v\). Enumerate every nonempty subset and discard it precisely if it contains an independent triple. This produces exactly \(134\) faces, with face numbers in dimensions zero through four equal to \((9,36,56,31,2)\).

Apply the following fully specified matching on the nonempty face poset. For each pivot vertex in the fixed order
\[
(0,6,3,2,1,7,4,5,8),
\]
visit all nonempty faces in increasing bitmask order, and whenever both a still-unmatched face omitting the pivot and its one-vertex extension are still unmatched, match them and remove both from subsequent consideration. Exactly \(66\) disjoint pairs are obtained; the only unpaired faces are bitmasks \(1\), a vertex, and \(390\), a tetrahedral three-cell. Verify global acyclicity by orienting each unmatched Hasse incidence from the larger face to the smaller, reversing each matched incidence, and topologically sorting the resulting directed graph. All \(134\) faces are visited; the Hasse diagram has exactly \(374\) incidences. These integer counts and the DAG test are independently reproducible by the complete standalone `verify.py` program. Forman's acyclic matching theorem produces a CW complex with one zero-cell and one three-cell. Its three-cell attaches to the point and therefore the realization is \(S^3\). This supplies the missing unrestricted base theorem with an exhaustive, finite, **globally acyclic** certificate, not only Betti-number or Euler-character evidence.

**3. Integral symmetry signs.** The quotient decomposition of Step 1 is natural under permutation and reflection of petals. Thus the canonical direct-sum decomposition on integral third homology consists of primitive rank-one summands indexed by unordered petal pairs, with each summand acted on via the two-petal group. To determine its signs, use the simplicial Lefschetz formula on the same complete \(134\)-face base complex. For an automorphism \(g\), let the signed trace of a fixed simplex be the sign of the induced permutation of its ordered vertices. Its reduced Lefschetz number equals the sum of \((-1)^{\dim\sigma}\) times those signs over fixed nonempty simplices, minus one for the augmentation. Since the base complex is \(S^3\), its degree-three homology trace is the negative of that reduced Lefschetz number.

For the identity and for the interchange \((1,5)(2,6)(3,7)(4,8)\), the exact third-homology trace is \(+1\). For either independent petal reflection \((1,4)(2,3)\) or \((5,8)(6,7)\), it is \(-1\). These are exact signed all-simplex sums, recomputed in `verify.py`. Fix a primitive generator in one pair quotient and transport it to each ordered pair \(i<j\). Because the swap sign is positive, these transports are coherent under every petal permutation, giving the unsigned pair permutation rule. Because a single reflection has sign negative, the reflection rule is the product of the two involved petal signs. There is no mixing between the pair summands, as the quotient wedge splits them canonically on reduced homology.

**4. Invariants and geometric quotients.** The symmetric group acts transitively and without signs on the basis indexed by two-subsets, so its rational invariant rank is one. A vector fixed by every single-petal reflection has zero coefficient at every basis element (each basis element contains a petal that can be reflected), so the entire reflection subgroup has zero invariant subspace. For a finite group acting simplicially on a finite complex, rational homology of the geometric quotient equals the invariant rational homology of the original complex: pass through a sufficiently fine equivariant subdivision so the quotient has an admissible cellular structure, then average chains over the group. This gives the asserted acyclicity of the full quotient in positive rational degrees.

## Verification
Running `python3 verify.py` requires only Python 3 standard library. It independently constructs the graph from the listed five-cycle edges, enumerates all forbidden independent triples, tests every face, constructs the exact two-petal discrete-Morse matching, topologically sorts every Hasse incidence, and separately computes the signed simplex Lefschetz traces. It also independently enumerates face numbers for \(m=1,2,3,4\). Its recorded terminal output is `verification_output.txt`. In the base case it checks \(134\) nonempty simplices, \(66\) matching pairs, \(374\) Hasse incidences, and the two critical cells. Finite examples for larger \(m\) corroborate but do not prove the infinite statement; Steps 1 and 3 do so.

## Relationship to prior work
Filakovský's 2026 work introduced the robust-clique terminology and proved sphere-wedge homotopy results for bipartite square-sequence graphs, including rectangular grids. Its hypotheses do not encompass bouquets of **odd** pentagons. Kim and Lew had earlier studied the same bounded-independence complex \(I_3(G)\), obtaining collapsibility estimates rather than this exact family homotopy or integral group module.

The closest subsequent published research record proves a three-sphere wedge formula for arbitrary **connected bipartite** graphs and separately analyses bouquets of **four-cycles** at various thresholds. The present graphs are nonbipartite, their petals are unfilled odd cycles, and those results neither determine the two-pentagon base nor give its petal-reflection signs or signed pair module. A different indexed result on the **ordinary three-cut** complex of short-cycle-free graphs uses the connectedness of induced triples; the present complex forbids *independent* triples and is Alexander-dual to the **total** three-cut complex, so that theorem does not imply this claim. Another result on ordinary independence complexes of vertex-glued five-cycles uses a different forbidden-face size. Comparing actual definitions and implied statements, rather than matching the words 'bouquet' or 'three-cut', is essential here. An unindexed equivalent or general reduction is still a residual risk.

## Limitations
This result is confined to common-vertex bouquets of unfilled five-cycles and robustness parameter three. It does not classify other odd cycle lengths, arbitrary cactus graphs, higher robustness thresholds, or an equivariant wedge decomposition. The finite computations are exhaustive only for the stated nine-vertex base and selected larger face counts; the global theorem uses the explicit support decomposition. The homology-module identification is integral, but the quotient assertion is only rational. Independent mathematical review has not been performed.

## References
1. M. Filakovský, *The Topology of \(k\)-Robust Clique Complexes in Grid-like Graphs*, arXiv:2602.11365, first public 2026-02-11, Theorems 1–3 and §3; https://arxiv.org/html/2602.11365v4.
2. M. Kim and A. Lew, *Complexes of graphs with bounded independence number*, arXiv:1912.12605, first public 2019-12-29, especially Theorem 1.8; https://arxiv.org/pdf/1912.12605.
3. *A three-sphere wedge theorem for robust clique complexes of all connected bipartite graphs*, publicly indexed research record, 2026-10-11, especially its statement and hypotheses.
4. *All-threshold sphere wedges for bouquets of quadrilaterals*, publicly indexed research record, 2026-11-08, especially the assumptions and limitation to four-cycles.
5. *Three-cut complexes of graphs without short cycles: sphere wedges and symmetry characters*, publicly indexed research record, 2026-10-11, especially the definition of ordinary three-cut and its Alexander dual.
