# A sharp one-slide detour law for optimal power domination on the seventeen-vertex Paley graph

## Finding

Let \(G=P_{17}\) be the Paley graph on \(\mathbb Z/17\mathbb Z\), with \(u\sim v\) exactly when \(u-v\) is a nonzero quadratic residue modulo \(17\). Under the standard power-domination rule, \(\gamma_P(G)=2\), and the **68 minimum power-dominating sets are exactly the unordered nonadjacent vertex pairs**.

Let \(R_J\) join two such minimum sets when one selected vertex is replaced by any unselected vertex, and let \(R_S\) impose the additional requirement that the removed and inserted vertices are adjacent in \(G\). With \(L(H)\) denoting the line graph and \(\Gamma(H)\) the Gallai graph, there are natural isomorphisms

\[
R_J\cong L(\overline G)\cong L(G),\qquad R_S\cong\Gamma(\overline G)\cong\Gamma(G).
\]

Both are connected and of diameter \(3\), though \(R_J\) has \(476\) edges and \(R_S\) has only \(272\). From every minimum placement, their respective distance-sphere sizes (at distances \(0,1,2,3\)) are

\[
(1,14,50,3)\quad\text{and}\quad(1,8,32,27).
\]

For **every** two optimal placements \(A,B\), the local-slide distance satisfies

\[
d_{R_J}(A,B)\le d_{R_S}(A,B)\le d_{R_J}(A,B)+1.
\]

The upper inequality is sharp for exactly \(1020\) of the \(\binom{68}{2}=2278\) unordered pairs of distinct optimal placements; the remaining \(1258\) pairs have equal distances.

## Assumptions and scope

Everything concerns this one explicitly labeled finite graph. The quadratic residues are

\[
Q=\{1,2,4,8,9,13,15,16\}\pmod{17}.
\]

For a nonempty vertex set \(S\), initially observe its closed neighborhood \(N[S]\). At each subsequent synchronous round, any observed vertex with exactly one unobserved neighbor causes that neighbor to become observed. A set is power dominating precisely when repeated rounds observe all seventeen vertices. A token jump exchanges one selected and one unselected vertex; a token slide is a jump along an edge of the original graph. Every intermediate state must be minimum power dominating. No assertion is made about other Paley graph orders, other observation models, or placement budgets above the optimum.

## Proof

**1. Exhaustive reduction of minimum placements to two pair types.** The translations \(x\mapsto x+b\) and multiplications \(x\mapsto rx\) with \(r\in Q\) are graph automorphisms. They act transitively on vertices, on adjacent unordered pairs, and on nonadjacent unordered pairs. It therefore suffices to inspect the singleton \(\{0\}\), the adjacent pair \(\{0,1\}\), and the nonadjacent pair \(\{0,3\}\).

From \(\{0\}\) the initial observed vertices are \(\{0,1,2,4,8,9,13,15,16\}\). Each observed vertex has either zero or four unobserved neighbors. Thus a single sensor cannot propagate.

For \(\{0,1\}\) the initially unobserved vertices are \(\{6,7,11,12\}\). Every observed vertex has either zero, two, or three neighbors in that set, so no forcing step is possible. For \(\{0,3\}\) the initial unobserved vertices are \(\{6,10,14\}\). Observed vertices \(4,9,13\) respectively have exactly one unobserved neighbor \(6,10,14\); one synchronous propagation round therefore observes all vertices. As all pairs fall into those two orbits, the claimed minimum-set classification follows. Exactly half of the \(\binom{17}{2}=136\) pairs are nonedges, hence there are \(68\) minimum placements.

**2. Graph-operator interpretation.** An optimal placement \(\{u,v\}\) is precisely an edge of \(H=\overline G\). Two placements admit a jump exactly if their corresponding edges of \(H\) share an endpoint. Thus \(R_J=L(H)\). If the exchanged endpoints are adjacent in \(G\), they are nonadjacent in \(H\), so the two incident edges of \(H\) do not span a triangle: that is exactly adjacency in \(\Gamma(H)\). Hence \(R_S=\Gamma(H)\). Multiplication by a nonresidue modulo \(17\), such as \(3\), maps \(H\) isomorphically onto \(G\), giving the other two isomorphisms. The graph \(H\) has degree \(8\) and adjacent-pair common-neighbor count \(3\). Consequently its line graph is \(14\)-regular and its Gallai graph is \(2(8-3-1)=8\)-regular. (Gallai regularity in this generality is prior work.) Therefore their respective edge counts are \(68\cdot14/2=476\) and \(68\cdot8/2=272\).

**3. Finite complete distance certificate and symmetry lift.** Identify the \(68\) vertices with all sorted pairs \((u,v)\), \(0\le u<v\le16\), satisfying \((u-v)\notin Q\). The standalone `root_spheres.json` records the exact distances to each of these pairs from \(\{0,3\}\), under both move rules. Each root table entry is generated independently from the explicit adjacency rule in `check_direct.py` (bitset propagation and all-source shortest paths) and `check_orbit.py` (modular-residue arithmetic, the two pair-orbit representatives, and operator-based adjacency). Both checkers compare their computed rooted distances against all \(68\) entries of the certificate.

Breadth-first search of the explicit finite graphs gives the root distance distributions \((1,14,50,3)\) and \((1,8,32,27)\). Moreover, among the \(68\) root distances, exactly \(38\), counting the root, agree, and exactly \(30\) have slide distance one greater than jump distance. The affine automorphisms act transitively on all nonedge pairs, and preserve both reconfiguration adjacency relations. Thus these root distributions and the pointwise excess histogram hold from **every** state, proving connectivity, both diameters, and the one-step detour bound for all ordered pairs. Removing the root from the zero-excess count, the number of unordered pairs with an extra move is \(68\cdot30/2=1020\); the equal-distance count is \(68\cdot37/2=1258\).

The scripts exhaust a fixed finite graph; there is no inference from a finite experiment to an unbounded family. The proof's only nontrivial computation is an exhaustive breadth-first search on \(68\) explicitly described states, with a fully decoded root certificate and two reconstructing checkers.

## Verification

Use Python 3 with the three standalone package files in the same directory. Run `python3 check_direct.py` and `python3 check_orbit.py`. Neither requires third-party packages, downloads, imported data, or hidden state. Both verify all \(68\) rooted-distance rows in `root_spheres.json` and all reported totals. The former independently enumerates every singleton, every pair, and all \(2278\) unordered placement-pair shortest paths; the latter derives pair feasibility from symmetry representatives and transports rooted graph distances through \(136\) explicit affine automorphisms. Both were run successfully from the packaged directory. `VERIFICATION.md` records their precise outputs.

## Relationship to prior work

Bjorkman et al., *Power domination reconfiguration*, arXiv:2201.01798v1 (January 5, 2022), introduce the general token-jumping and token-addition/removal framework and identify reconfiguration graphs for several other graph families. The relevant sections contain neither the Paley-17 minimum-pair classification nor the present token-slide metric. Palathingal, Lakshmanan and Markowsky, *The Gallai and anti-Gallai graphs of strongly regular graphs*, arXiv:2106.03745 (first posted June 7, 2021), give the Gallai graph definition and prove its regularity for edge-regular graphs, subsuming the \(8\)-regularity observation here. Their spectral/structural results do not yield the specific pair-monitoring correspondence, full distance profiles, or \(1020\)-pair exact locality excess. Brouwer's Paley-graph reference and the P17 distance-regular graph database supply the established strongly regular parameters and symmetry background, not the claimed power-domination metric.

The graph operator definitions, self-complementarity, and regularity are **not** claimed as new. The claim of new work is the identification of the minimum power-domination relocation graphs with those operators in this canonical graph and the exact distance/penalty classification.

## Limitations

The theorem concerns only \(P_{17}\) and a precisely specified observation process. It does not classify power domination in general Paley graphs or Gallai graphs of arbitrary strongly regular graphs. The verified distances are finite, independently reproducible enumerations; they are not an all-orders symbolic diameter theorem. Historical literature outside the inspected searchable sources could contain an equivalent result. Independent mathematical audit has not been performed.

## References

1. B. Bjorkman, C. Bozeman, D. Ferrero, M. Flagg, C. Grood, L. Hogben, B. Jacob and C. Reinhart, *Power domination reconfiguration*, arXiv:2201.01798v1, first posted 2022-01-05. https://arxiv.org/html/2201.01798v1
2. J. J. Palathingal, S. A. Lakshmanan and G. Markowsky, *The Gallai and anti-Gallai graphs of strongly regular graphs*, arXiv:2106.03745, first posted 2021-06-07. https://arxiv.org/abs/2106.03745
3. A. E. Brouwer, *Paley graphs*, reference page. https://aeb.win.tue.nl/graphs/Paley.html
4. *Paley graph P17*, DistanceRegular.org, reference page (updated 2017-02-04). https://www.math.mun.ca/distanceregular/graphs/paley17.html
