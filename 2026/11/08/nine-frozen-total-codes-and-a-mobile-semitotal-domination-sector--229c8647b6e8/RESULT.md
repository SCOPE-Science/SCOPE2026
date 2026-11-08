# Nine frozen total codes and a mobile semitotal-domination sector of the Pappus graph

## Finding

Let \(P\) denote the eighteen-vertex cubic Pappus graph. A **semitotal dominating set** \(S\subseteq V(P)\) dominates every vertex by closed neighborhoods and has, for every \(s\in S\), another \(t\in S\) at graph distance at most two. A **token jump** replaces one selected vertex with any unselected vertex; a **token slide** makes such a replacement along an edge. Every intermediate configuration must remain a *minimum-cardinality* semitotal dominating set.

**Theorem.** The semitotal domination number of \(P\) is \(6\). There are exactly \(297\) minimum semitotal dominating sets. Precisely nine of them are total dominating sets, and those nine are isolated in both the token-jump and token-slide graphs. The other \(288\) configurations form one connected component in each reconfiguration graph. The jump graph has \(1026\) edges; its nontrivial component is self-centered of radius and diameter \(6\). The slide graph has \(432\) edges; its nontrivial component has radius \(8\) and diameter \(10\). Thus the component decompositions agree, while their shortest-path metrics do not.

The full automorphism group of \(P\) has order \(216\). Its action on the \(297\) minimum sets has five orbits, with the following orbit size, jump degree, and slide degree, respectively:

| Orbit size | Jump degree | Slide degree |
|---:|---:|---:|
| 9 | 0 | 0 |
| 18 | 6 | 6 |
| 54 | 8 | 8 |
| 108 | 6 | 2 |
| 108 | 8 | 1 |

On the \(288\)-state component, all jump eccentricities equal \(6\). The slide eccentricity distribution is \(126\) states of eccentricity \(8\), \(54\) of eccentricity \(9\), and \(108\) of eccentricity \(10\).

The nine frozen configurations admit a particularly transparent \(3\times 3\) construction from the Pappus incidence geometry, detailed below. Their immobility is also explained by a general rigidity lemma for efficient open dominating sets in cubic graphs of girth at least five.

## Assumptions and scope

All graphs are finite, simple and undirected; vertices and configurations are labeled, but configurations are *sets*, not ordered token placements. The theorem is an exact finite statement for the Pappus graph, not a uniform statement about every cubic graph.

For a self-contained incidence realization, take nine points labeled \(A,B,C,a,b,c,X,Y,Z\) and nine lines \(L_0,\ldots,L_8\) containing the following triples, respectively:

| Line | Incident points | Line | Incident points | Line | Incident points |
|---|---|---|---|---|---|
| \(L_0\) | \(ABC\) | \(L_1\) | \(abc\) | \(L_2\) | \(XYZ\) |
| \(L_3\) | \(AbX\) | \(L_4\) | \(aBX\) | \(L_5\) | \(AcY\) |
| \(L_6\) | \(aCY\) | \(L_7\) | \(BcZ\) | \(L_8\) | \(bCZ\) |

The graph \(P\) is the bipartite point-line incidence graph of these nine triples. It has \(18\) vertices, \(27\) edges, degree \(3\) and girth \(6\). An independent representation is the Hamiltonian LCF form \([5,7,-7,7,-7,-5]^3\), with labels \(0,\ldots,17\) and cycle edges plus the corresponding chords. The following list gives an explicit isomorphism from LCF indices \(0\) through \(17\) to incidence labels, in order:

`PA,L0,PC,L8,Pb,L3,PX,L4,PB,L7,PZ,L2,PY,L6,Pa,L1,Pc,L5`.

The **token-jump graph** has as vertices all six-vertex semitotal dominating sets, with an edge between distinct sets \(S,T\) exactly when \(|S\cap T|=5\). The **token-slide graph** retains only those edges where the removed vertex and the added vertex are adjacent in \(P\). All graph distances, radii and diameters reported for disconnected reconfiguration graphs refer explicitly to their unique nontrivial components.

## Proof

**1. Minimum cardinality.** Goddard, Henning and McPillan proved the general lower bound \(\gamma_{t2}(G)\ge 2|V(G)|/(2\Delta(G)+1)\) for semitotal domination [1, Lemma 3]. As \(P\) is cubic on eighteen vertices, \(\gamma_{t2}(P)\ge\lceil36/7\rceil=6\). The explicit six-vertex sets constructed next are total dominating and hence semitotal dominating. Therefore \(\gamma_{t2}(P)=6\) without relying on a failed finite search for five-element sets.

**2. Three-by-three grid of total dominating minima.** Define three point triples
\[
\mathcal P=\big\{\{A,a,Z\},\{B,b,Y\},\{C,c,X\}\big\}
\]
and three line triples
\[
\mathcal L=\big\{\{L_0,L_1,L_2\},\{L_3,L_6,L_7\},\{L_4,L_5,L_8\}\big\}.
\]
Each point triple has exactly one incident point on each of the nine lines; each line triple has exactly one incident line on each of the nine points. Consequently every union \(T\cup U\), with \(T\in\mathcal P\) and \(U\in\mathcal L\), has exactly one selected neighbor at every vertex. These are nine *efficient open dominating* sets, hence nine minimum semitotal dominating sets.

Conversely, any total dominating set of size six is efficient open dominating: the six open neighborhoods have \(6\cdot3=18\) positions counting multiplicity and must cover all eighteen vertices, so none can overlap. Splitting such a set across the bipartition gives a point triple whose incident line neighborhoods partition the lines, and a line triple whose incident point neighborhoods partition the points. Directly inspecting the nine displayed incidence triples, the only possible point triples are the three in \(\mathcal P\), and the only possible line triples are the three in \(\mathcal L\). Hence **these nine, and no others, are the minimum total dominating sets**.

**3. Rigidity of efficient open domination.** More generally, suppose \(G\) is cubic with girth at least five and \(S\) is an efficient open dominating set. Every \(s\in S\) has three neighbors dominated by \(s\) and by no other selected vertex. If \(s\) is removed, any replacement \(w\ne s\) must dominate all three formerly private neighbors. If \(w\) is one of those three neighbors, it cannot dominate the other two in a triangle-free graph. If \(w\) is not among them, it cannot be adjacent to two of them without making a four-cycle with \(s\). Thus no one-vertex replacement preserves even ordinary domination. In particular, the nine Pappus total dominating minima are isolated under both exchange rules.

**4. Exhaustive six-subset classification.** For each of the \(\binom{18}{6}=18564\) six-subsets \(S\), the following finite predicate is exact:
\[
\left(\bigcup_{s\in S}N[s]=V(P)\right)
\quad\land\quad
\bigl(\forall s\in S\;\exists t\in S\setminus\{s\}:d_P(s,t)\le2\bigr).
\]
Using either the LCF adjacency masks or the point-line incidence lists, exhaustive application of this predicate yields \(297\) qualifying subsets. The nine efficient open dominating sets are already characterized without this enumeration; the other \(288\) therefore fail total domination while satisfying semitotal domination.

**5. Exact exchange and metric certificates.** Form an edge for every unordered pair of qualifying six-subsets whose intersection has five vertices. This gives \(1026\) token-jump edges. Restricting to exchanges along an edge of \(P\) gives \(432\) token-slide edges. In both cases, breadth-first exploration from every unvisited state identifies exactly one component of size \(288\) and nine singletons; Step 3 identifies the singletons as the efficient open dominating sets. Independently, all-sources breadth-first search in the \(288\)-state component yields the eccentricities and sharp radius/diameter claimed in the theorem. All visited states, transitions and distances are exhaustively determined by the standalone verifiers described below; no random testing or extrapolation is involved.

**6. Symmetry-orbit certificate.** Under the incidence realization, every point-side-preserving automorphism permutes the nine points while preserving the family of nine incident triples. Exactly \(108\) of the \(9!\) point permutations satisfy this, and their action on lines is uniquely determined. An explicit point-line interchange produces another \(108\) automorphisms; thus the full automorphism group has order \(216\). Enumerating their action on all \(297\) qualifying subsets gives the five orbits and the orbitwise constant exchange degrees in the table. The complete group enumeration and the duality witness are implemented in `verify_symmetry.py`.

## Verification

The accompanying standalone Python 3 files are intended to be run from this directory, without third-party dependencies:

```sh
python3 verify_lcf.py
python3 verify_incidence.py
python3 verify_symmetry.py
```

The scripts each print `VERIFY_OK` only after their assertions pass. `verify_lcf.py` constructs the LCF graph and uses bitmask tests and explicit permitted replacements. `verify_incidence.py` independently constructs the nine-point/nine-line graph, checks an explicit isomorphism to the LCF graph, tests candidate subsets with sets and shortest-path distances, and constructs exchanges by comparing all unordered pairs of states. Both compute exact component decompositions and all-sources eccentricities. `verify_symmetry.py` computes the entire incidence automorphism group and its five orbits without specialized graph libraries. The three corresponding `.out` files retain the recorded successful outputs.

The verifiers establish a finite theorem on the stated graph. They do not certify any global first-discovery claim or any generalization to other cubic graphs.

## Relationship to prior work

Goddard, Henning and McPillan [1] introduced semitotal domination and proved the degree-based lower bound applied in Step 1; their paper treats general inequalities, extremal families and complexity rather than a Pappus six-set census or exchange networks. Henning and Marcon [2] gave a characterization of minimal semitotal dominating sets and related matching bounds; its available abstract gives no Pappus classification. Alikhani and Zaherifar [3] count semitotal dominating sets in selected paths, cycles, complete bipartite graphs, friendship graphs and other families; its inspected full text does not address the Pappus graph or its reconfiguration.

The Pappus graph has been studied in many other combinatorial settings, including domination, locating codes, identifying codes, matchings and edge-colourings. These use different admissible configurations and moves: a minimum ordinary dominating set, identifying code, matching or edge-colouring is not the same object as a minimum semitotal dominating set. Such results do not imply the present \(297\)-state census or sharp exchange metrics. The nine efficient total dominating sets may be obtainable by independent incidence enumeration; their cardinality alone is not the claimed novelty. The substantive result is the joint precise decomposition of the semitotal minimum sets and their two exchange graphs, including the structural identification of all frozen states.

Henning and Marcon [4] establish bounds for claw-free cubic graphs, but their hypothesis excludes the Pappus graph: each vertex of a cubic graph of girth six is the center of an induced three-leaf claw. Thus their upper bounds do not cover the present classification.

## Limitations

The theorem applies only to this specified eighteen-vertex graph and these two fixed-cardinality exchange rules. All radii and diameters concern the nontrivial component; the disconnected full graphs have no finite global diameter under the usual convention. This is a finite proof by complete enumeration plus explicit structural arguments, not an analytic classification for an infinite family. Independent external scholarly audit has not occurred. Priority comparisons cannot exclude unpublished computations or literature outside the inspected and indexed sources; the full text of [2] was unavailable for close comparison, though its abstract and bibliographic metadata were checked.

## References

1. W. Goddard, M. A. Henning and C. A. McPillan, *Semitotal Domination in Graphs*, Utilitas Mathematica **94** (2014), 67–81. Author-hosted complete text: https://people.computing.clemson.edu/~goddard/papers/SemiTDomUtilitas.pdf . Lemma 3 establishes \(\gamma_{t2}(G)\ge2n/(2\Delta+1)\).
2. M. A. Henning and A. J. Marcon, *On matching and semitotal domination in graphs*, Discrete Mathematics **324** (2014), 13–18. DOI: https://doi.org/10.1016/j.disc.2014.01.021 . Abstract and bibliographic metadata inspected; full text unavailable.
3. S. Alikhani and H. Zaherifar, *On the semitotal dominating sets of graphs*, arXiv:2107.01424 (first submitted 2021-07-03). Full accessible text: https://arxiv.org/html/2107.01424v1 .
4. M. A. Henning and A. J. Marcon, *Semitotal Domination in Claw-Free Cubic Graphs*, Annals of Combinatorics **20** (2016), 799–813. DOI: https://doi.org/10.1007/s00026-016-0331-z . Its claw-free hypothesis does not apply to the cubic girth-six Pappus graph.
5. *Pappus graph*, conventional LCF representation \([5,7,-7,7,-7,-5]^3\); the standalone graph-isomorphism certificate also specifies the incidence geometry and gives the full vertex map.
