# Twenty-seven frozen minimum restrained dominating sets in the Pappus graph

## Finding

The Pappus graph has ordinary domination number \(5\), with exactly 18 labelled minimum dominating sets, and restrained domination number \(6\), with exactly 207 labelled minimum restrained dominating sets. The full automorphism group has order 216 and acts on the restrained optima with orbit sizes \(9,18,18,54,108\).

In both optimum-preserving reconfiguration graphs (token jumping and token sliding), exactly 27 configurations are isolated and the other 180 form one connected component. **The isolated configurations are exactly those inducing three edges:** nine induce \(3K_2\), and eighteen induce \(K_{1,3}\sqcup2K_1\). These are distinct automorphism orbits. There are 432 jump edges and 324 slide edges. In the 180-vertex component the jump degrees are four (108 states) and six (72 states), and the slide degrees are two (108 states) and six (72 states). Every vertex in the main component has eccentricity six for jumps and eight for slides, giving both its radius and diameter.

The restrained domination polynomial, in which the coefficient of \(z^k\) counts labelled restrained dominating \(k\)-sets, is
\[
R_G(z)=207z^6+1242z^7+3429z^8+5040z^9+4671z^{10}+3294z^{11}+1809z^{12}+756z^{13}+297z^{14}+54z^{15}+27z^{16}+z^{18}.
\]
In particular size seventeen does not occur.

## Assumptions and scope

The point shore consists of \(p_{x,y}\), \(x,y\in\mathbb F_3\); the line shore consists of \(\ell_{d,a}\) for \(d=x,y,s\) and \(a\in\mathbb F_3\). A point is adjacent to the three lines for which \(a=x,y,x+y\), respectively. For indexing, points have labels \(3x+y\); lines have labels \(9+a,12+a,15+a\), respectively. The mask of a set \(S\) is \(\sum_{i\in S}2^i\).

A set \(S\) dominates if every vertex outside \(S\) has a neighbor in \(S\). It is restrained dominating if every such vertex also has a neighbor outside \(S\). A jump exchanges one selected and one unselected vertex; a slide additionally requires an edge between the two exchanged vertices. Each move preserves restrained domination and cardinality six. The graph and both move rules are fixed throughout.

## Proof

**Ordinary domination and the lower bound for restrained domination.** If a dominating set contains \(a\) points and \(b\) lines, then \(a+3b\ge9\) and \(3a+b\ge9\), so \(a+b\ge5\). For size five the shore counts are \((2,3)\) or \((3,2)\). In the first case the two selected points must have disjoint incident-line pencils to dominate six unselected lines. Their difference is \((t,t)\) with \(t\ne0\); the three selected lines are forced to be the missing line in each of the three selected directions. They pass through the third point on the omitted-direction line through the chosen pair. Their union contains exactly the seven unselected points, so this set dominates. The common unselected point has all its neighbors selected and thus witnesses non-restraint. The three lines of the omitted direction each give three unordered pairs of points, for nine sets. A shore-reversing graph automorphism gives the other nine and transfers the same non-restraint argument. A shore-reversing automorphism, in the given indexing, is the permutation with images \((9,12,15,16,11,14,13,17,10,0,8,4,1,6,5,2,3,7)\); substitution into the incidence rule verifies it.

**Finite enumeration and the full group.** For all labelled subsets \(S\), test that no outside vertex \(v\) has its whole neighborhood \(N(v)\) contained in \(S\) or its complement. This is exactly the restrained condition. The resulting cardinality counts are the displayed polynomial; its minimum exponent is six. For automorphisms, the connected bipartite graph has a unique bipartition up to exchange, so the images of the nine points must biject onto one of the two shores. Once those images are fixed, the images of the nine lines are forced if they exist: the image of each of its three-element point neighborhoods must be the neighborhood of a vertex on the opposite shore. These nine neighborhoods are distinct on either shore. Checking both shores and all \(9!\) image permutations therefore finds every automorphism. There are 108 preserving the shores and 108 exchanging them. The orbit computation gives the following census; the representative is the least mask in each orbit.

| Mask | Orbit size | Induced graph | Isolated for both move rules |
|---:|---:|:---|:---:|
| 3682 | 9 | \(3K_2\) | yes |
| 3591 | 18 | \(K_{1,3}\sqcup2K_1\) | yes |
| 38150 | 18 | \(6K_1\) | no |
| 5040 | 54 | \(6K_1\) | no |
| 6020 | 108 | \(K_2\sqcup4K_1\) | no |

For example, 3682 induces edges \(\{1,9\},\{5,10\},\{6,11\}\); 3591 selects \(\{0,1,2,9,10,11\}\) and induces edges \(\{0,9\},\{1,9\},\{2,9\}\). Induced graph type is constant on each orbit.

**Moves and distances.** For each pair of the 207 optima, test whether their intersection has five vertices; for a slide also test adjacency of the two vertices in their symmetric difference. These tests enumerate exactly all legal moves. Component traversal gives 27 singletons and one 180-state component for each rule. Comparing the actual sets of singletons to the optimum sets inducing three edges gives equality for both rules. Breadth-first distances from every state in the main component give the asserted eccentricities and the degree counts above.

## Reproduction

Run `python3 verify_induced_shapes.py` from the directory containing that file. The script independently constructs the graph, tests every labelled subset, checks full automorphism and orbit counts including the induced graph types, and reconstructs both optimum reconfiguration graphs and their eccentricities. The original `verify_affine.py` and `verify_cpp.cpp` use other enumeration orders and check the numerical censuses; neither by itself distinguished all induced graph types. The complete induced-degree signatures in the new checker distinguish all displayed types on six vertices.

## Relationship to prior work and limitations

The general bounds of Poghosyan–Zverovich (arXiv:0901.2862) and Brešar–Henning (arXiv:2403.17129) do not give the optimizer and reconfiguration classification; the latter gives at most seven. *Nine frozen total codes and a mobile semitotal-domination sector* (record `229c8647b6e8`, proof §§2–3) already classifies the nine efficient open dominating sets and proves that they cannot move even among ordinary dominating sets. These are exactly the nine restrained optima inducing \(3K_2\): such a set totally dominates, then cubicity and its cardinality force each vertex to have exactly one selected neighbor; conversely that condition gives both a matching on the set and restraint outside it. *Minimum domination reconstructs the Pappus graph and separates static from adaptive shattering* (record `2312bedeb2f5`, optimal-set classification) gives the ordinary five-sets explicitly. The raised claw configurations can also be recovered from that list: each five-set is independent with just one outside vertex having all three neighbors selected, so adjoining that vertex preserves domination, leaves no isolated vertex in the unselected subgraph, and creates a claw with two isolates. Conversely deleting the center of any restrained six-set of claw type yields an ordinary dominating five-set, because that center has no neighbors outside the six-set. The two matching and claw families do not determine the full restrained polynomial, the five-orbit census, or the two 180-state reconfiguration graphs.

This is an exact finite result for one graph, not a classification for cubic graphs. The full restrained census and reconfiguration are the focus, not priority for the ordinary domination number, the efficient open domination family, or the claw construction. No assertion of historical priority over inaccessible or unindexed work is made.
