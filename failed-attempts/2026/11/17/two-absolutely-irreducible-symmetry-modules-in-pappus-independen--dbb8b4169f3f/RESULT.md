# Two absolutely irreducible symmetry modules in Pappus independence homology

## Finding

Let \(P\) be the eighteen-vertex Pappus graph, with the Hamiltonian-cycle labeling \(0,\ldots,17\) and LCF offsets \([5,7,-7,7,-7,-5]^3\). Let \(K=\operatorname{Ind}(P)\), and let \(G=\operatorname{Aut}(P)\), acting simplicially on \(K\). Let \(Z=G^{(3)}\), where \(G^{(1)}=[G,G]\) and \(G^{(j+1)}=[G^{(j)},G^{(j)}]\).

The full automorphism group has order \(216\), and its derived-series orders are \(216,54,27,3,1\). Thus \(Z\) is a characteristic subgroup of order three. The only nonzero reduced rational homology is \(\widetilde H_4(K;\mathbb Q)\), of dimension ten. This representation has the **canonical decomposition**
\[
\widetilde H_4(K;\mathbb Q)
  =\widetilde H_4(K;\mathbb Q)^Z\oplus
  \ker(1+z+z^2),\qquad
\dim_{\mathbb Q}=4+6,
\]
where \(z\) is either generator of \(Z\). **Both summands are absolutely irreducible \(\mathbb Q[G]\)-modules.**

The complete character \(\chi(g)=\operatorname{tr}(g\mid\widetilde H_4(K;\mathbb Q))\) on all thirteen conjugacy classes, in the class order and with the explicit representatives given in `character_classes.tsv`, is
\[
(10,2,-2,-1,1,0,2,0,-1,-2,1,-1,1).
\]
In particular, \(\chi(z)=1\) for either nonidentity \(z\in Z\). The character has no full-group invariant vectors; the same holds on restricting to the index-two subgroup \(G^+\) preserving the two parts of the bipartite graph. Consequently the **ordinary topological quotients** \(|K|/G\) and \(|K|/G^+\) are both rationally acyclic:
\[
\widetilde H_*(|K|/G;\mathbb Q)
=\widetilde H_*(|K|/G^+;\mathbb Q)=0.
\]
No homotopy-equivalence or integral-acyclicity assertion is made for these quotients.

## Assumptions and scope

The graph has vertex set \(\{0,1,\ldots,17\}\), its edges consist of the eighteen cycle edges together with the nine chords from the stated LCF presentation, and all vertices have degree three. The explicit twenty-seven edges are hard-coded in `verify_pappus_full.py`; the verifier does not appeal to a graph database. A simplex of \(K\) is a nonempty subset of vertices containing no graph edge. Oriented simplicial chains use vertices in increasing order. All representation and quotient-homology claims are over \(\mathbb Q\); only the auxiliary comparison homology is computed over \(\mathbb F_2\).

## Proof

**Homology concentration.** Complete enumeration gives the face vector, in dimensions zero through eight,
\[
(18,126,438,801,756,348,90,18,2),
\]
so the reduced Euler characteristic is \(10\). Exhaustive binary elimination on all simplicial boundaries gives the ranks, in degrees one through eight,
\[
(17,109,329,472,274,74,16,2).
\]
Accordingly the ordinary mod-two Betti vector is \((1,0,0,0,10,0,0,0,0)\). By universal coefficients, every rational Betti number is no larger than its mod-two counterpart. Thus rational reduced homology can occur only in degree four and have rank at most ten. The reduced Euler characteristic forces that rank to equal ten. This argument is about rational homology; it does not assert integral torsion-freeness.

**The complete symmetry character.** An adjacency-preserving backtracking enumeration produces exactly \(216\) permutations of the eighteen vertices. For an automorphism \(g\), its trace on oriented simplicial chains is the signed count of those independent sets fixed setwise by \(g\); the sign on an invariant \(d\)-simplex is the parity of the induced permutation of its \(d+1\) vertices. Since all positive-degree rational homology other than \(H_4\) vanishes and \(K\) is connected, the simplicial Lefschetz identity yields
\[
\chi(g)=-1+\sum_{\varnothing\ne\sigma\in K}
 (-1)^{|\sigma|-1}\operatorname{sgn}(g\mid\sigma)
 \mathbf 1_{g\sigma=\sigma}.
\]
A separate calculation recovers this same value by summing over unions of entire vertex cycles of \(g\), with a term \((-1)^{t+1}\) for every nonempty independent union of \(t\) cycles, and subtracting one. Both formulas agree on all \(216\) group elements. Conjugation partitions \(G\) into thirteen classes; their exact values and representatives are given in the attached TSV.

**The characteristic subgroup and irreducibility.** Direct finite-group multiplication and exhaustive commutator closure give \(|G^{(1)}|=54\), \(|G^{(2)}|=27\), \(|G^{(3)}|=3\), \(|G^{(4)}|=1\). The two nonidentity elements of \(Z\) form a conjugacy class of size two and have trace \(1\). The rational idempotent \((1+z+z^2)/3\) consequently has trace and rank \((10+1+1)/3=4\), and its complementary projection has rank six. Since \(Z\) is characteristic, both ranges are \(G\)-stable. Exact class summation gives
\[
\frac{1}{|G|}\sum_{g\in G}\chi(g)^2
=\frac{432}{216}=2.
\]
For a characteristic-zero complex representation this is the sum of the **squares** of the multiplicities of its complex irreducible constituents. The two nonzero, disjoint, \(G\)-stable subspaces just constructed force at least two such constituents. Equality to two forces exactly one irreducible constituent in each. Because the two summands are defined over \(\mathbb Q\), they are absolutely irreducible rational modules of dimensions four and six.

**Quotient statement.** The exact character sums over \(G\) and over its bipartition-preserving subgroup \(G^+\), respectively, are both zero. Hence \(\widetilde H_4(K;\mathbb Q)^G=\widetilde H_4(K;\mathbb Q)^{G^+}=0\). After barycentric subdivision, each finite group acts without inversions, and the rational homology of the ordinary finite quotient is the invariant rational homology: taking invariants is exact because the group order is invertible in \(\mathbb Q\). All other reduced homology vanishes, proving the two rational-acyclicity assertions.

## Verification

Run `python3 verify_pappus_full.py` from the directory containing `character_classes.tsv`, using Python 3 and no third-party libraries. The attached `verification_output.txt` records a complete successful execution. The verifier reconstructs the graph independently from twenty-seven hard-coded edges; enumerates its 2,597 independent simplices and all 216 automorphisms; performs complete mod-two boundary elimination; verifies both signed Lefschetz trace methods; checks all conjugacy classes, group products, commutator subgroup orders, characteristic-subgroup projections, character norms, the previously known period-six subgroup restriction and both rational invariant dimensions. The table's complete text is rechecked against a new calculation.

## Relationship to prior work

The classic Pappus configuration and its graph, including its distance-transitive geometry, occur in Dejter's 2009 study (arXiv:0904.1096). Berghoff's 2020 paper develops a general spectral-sequence method for independence-complex homology, with explicit cycle and Petersen-graph examples rather than this complete symmetry representation. Tsukuda's 2017 theorem relating incidence-graph independence complexes to Alexander dual constructions is potentially applicable to the Pappus Levi graph, but does not provide the thirteen-class rational homology character or its characteristic-subgroup splitting.

The publicly available earlier Pappus independence-homology report *Order-three symmetry on Pappus independence homology* determines the cyclic restriction for \(r(i)=i+6\pmod{18}\): its character is \((10,-2,-2)\). That cyclic computation and the nonequivariant homotopy type are **prior results, not novelty claims here**. The automorphism \(r\) belongs to a distinct order-three conjugacy class from \(Z\), whose nontrivial elements have trace \(1\). The previously available restriction does not determine the thirteen full-group character values, the \(4+6\) absolutely irreducible canonical splitting, or vanishing of full-group invariants. General computational recipes likewise do not state those outputs. No covering explicit determination was found in the inspected literature or mathematical research index.

## Limitations

The conclusion concerns this single graph and rational representation theory. It does not classify the integral \(\mathbb Z[G]\)-module, the homotopy type or integral torsion of either quotient, nor representations for other incidence graphs. Full publication priority cannot be guaranteed against unindexed material. The science has not undergone independent mathematical validation.

## References

1. I. J. Dejter, *Pappus–Desargues digraph confrontation*, first arXiv submission April 7, 2009, arXiv:0904.1096, https://arxiv.org/abs/0904.1096.
2. M. Berghoff, *On the homology of independence complexes*, first arXiv submission August 14, 2020, arXiv:2008.06267, https://arxiv.org/html/2008.06267v2.
3. S. Tsukuda, *Independence complexes and incidence graphs*, Contributions to Discrete Mathematics 12 (2017), 28–46, https://doi.org/10.55016/ojs/cdm.v12i1.62277.
4. *Order-three symmetry on Pappus independence homology*, publicly available 2026 report, identifier ea65a5211f31, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-order-three-symmetry-on-pappus-independence-homology--ea65a5211f31.
