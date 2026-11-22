# Four optimal power-domination types and a sharp locality penalty on the Folkman graph

## Finding

The twenty-vertex Folkman graph has power-domination number \(4\). It has exactly \(560\) minimum four-vertex power-dominating sets, divided into four explicit symmetry classes of sizes \(80,120,240,120\). Each class has a simple description in the five-label incidence construction below.

Let \(\mathcal J\) be the graph on these \(560\) sets in which one selected vertex can be replaced by any unselected vertex, provided the resulting set is again a minimum power-dominating set. Let \(\mathcal S\) permit that replacement only if the departing and incoming vertices are adjacent in the Folkman graph. Both \(\mathcal J\) and \(\mathcal S\) are connected. Their properties are:

| Invariant | \(\mathcal J\) | \(\mathcal S\) |
|---|---:|---:|
| Vertices | 560 | 560 |
| Edges | 4,680 | 1,920 |
| Radius | 4 | 7 |
| Diameter | 4 | 8 |
| Degree distribution | \(80t^{15}+120t^{16}+240t^{17}+120t^{18}\) | \(240t^4+240t^8+80t^{12}\) |

The \(80\) members of the first symmetry class are precisely the centers of \(\mathcal S\), whereas every vertex of \(\mathcal J\) has eccentricity \(4\). For unordered pairs \(\{A,B\}\) of distinct minimum sets, the *locality penalty* \(d_{\mathcal S}(A,B)-d_{\mathcal J}(A,B)\) has distribution

| Penalty | 0 | 1 | 2 | 3 | 4 |
|---|---:|---:|---:|---:|---:|
| Unordered pairs | 38,400 | 65,940 | 41,400 | 9,460 | 1,320 |

Thus the sharp additional cost of preserving minimum power domination while relocating a sensor only along network edges is \(4\) moves. Among the \(1,320\) extremal pairs, \(780\) have jump/slide distances \((2,6)\) and \(540\) have distances \((4,8)\).

## Assumptions and scope

This is a statement about one precisely specified, unweighted, undirected, labelled graph and optimum-preserving moves. Start with the complete graph on five labels \(\{0,1,2,3,4\}\). Replace each label \(i\) by two vertices \(u_i^0,u_i^1\), and each unordered edge \(\{i,j\}\) by one vertex \(e_{ij}\). Join \(e_{ij}\) to all four vertices \(u_i^0,u_i^1,u_j^0,u_j^1\), with no other edges. This is the standard Folkman graph, a four-regular, twenty-vertex, forty-edge, edge-transitive but not vertex-transitive graph.

For a sensor set \(A\), initially mark all vertices in \(A\cup N(A)\). Repeatedly mark an unmarked vertex when it is the sole unmarked neighbor of some already marked vertex, until the marked set stops changing. A *power-dominating set* marks every vertex. A move must preserve both the set cardinality \(4\) and the power-domination property. Distances count individual legal moves; configurations are unordered four-element subsets with no token identities. All comparisons concern pairs of distinct configurations.

## Proof

First classify the candidates. For a selected edge vertex \(e_{ij}\), call \(i,j\) its *underlying endpoints*. If a label \(i\) contributes a vertex \(u_i^b\), exactly one of its two copies is selected unless otherwise specified. The four possible types of minimum power-dominating sets are:

1. **Single edge:** select \(e_{ij}\) and one copy at each of the three labels outside \(\{i,j\}\). Count \(\binom52 2^3=80\).
2. **Two-edge wedge:** select two edge vertices whose underlying edges share one endpoint, and one copy at each of the other two labels. Count \(5\binom42 2^2=120\).
3. **Two-edge matching:** select two edge vertices whose underlying edges are disjoint; also select one copy at the unique label outside their four endpoints and one copy at any one of those four endpoints. Count \(15\cdot4\cdot2^2=240\).
4. **Three-edge path:** select the three edge vertices of an underlying four-label path of length three, and one copy at the fifth, unused label. Count \(5\cdot(4!/2)\cdot2=120\).

These types are disjoint. Completeness and minimality can be established by a short *exhaustive finite proof*, rather than an appeal to sampled instances. The graph is represented by integers \(0,\ldots,19\): integers \(2i+b\) encode \(u_i^b\), and integers \(10,\ldots,19\) encode the ten lexicographically ordered edge vertices \(e_{ij}\). `verify_bitmask.py` constructs each neighborhood as a twenty-bit integer and implements the observation operator exactly. It checks every subset of sizes \(0,1,2,3,4\), which comprise respectively \(1,20,190,1140,4845\) subsets. None of sizes below four power dominates, and exactly \(560\) of size four do. It independently partitions these subsets into orbits under the two generators of \(S_5\) (a transposition and a five-cycle) together with one twin-copy interchange, whose conjugates generate all five copy interchanges. There are respectively \(1,2,6,16,40\) orbits in sizes \(0\) through \(4\); the only four successful orbits at size four have sizes \(80,120,240,120\) and representatives \(\{4,6,8,10\}\), \(\{6,8,10,11\}\), \(\{0,8,12,14\}\), \(\{8,10,12,14\}\). The resulting orbit descriptions are exactly the four classes above. This establishes necessity and sufficiency by examining all cases, not merely symmetry prototypes assumed to be exhaustive.

For the relocation metric, map each of the \(560\) successful four-subsets to one graph vertex. Two distinct successful sets are adjacent in \(\mathcal J\) precisely when their intersection contains exactly three vertices. They are adjacent in \(\mathcal S\) precisely when, in addition, their unique differing vertices are joined by a Folkman-graph edge. These equivalences follow immediately from the definitions and account for every legal transition without omissions or duplications.

An exhaustive breadth-first search from *every* configuration in the two fully constructed reconfiguration graphs provides their connectedness, degree distributions, radii and diameters, and each unordered-pair distance histogram. The jump histogram for distances \(1,2,3,4\) is \((4680,22440,64960,64440)\). The slide histogram for distances \(1,\ldots,8\) is \((1920,9000,23760,50280,42240,24700,4080,540)\). Both sum to \(\binom{560}{2}=156520\), a coverage cross-check. Pairwise subtraction of the two complete all-pairs distance matrices gives the claimed penalty histogram and confirms its exact maximum of four. The eighty configurations of the single-edge type have slide eccentricity seven; all other four hundred eighty configurations have eccentricity eight. `verify_incidence.py` independently constructs vertices as named tuples and neighborhoods as sets, directly constructs all four proposed families, evaluates the power-domination condition anew, and checks the same complete all-pairs metrics without importing the first implementation. Both are complete finite certificates for the asserted fixed graph.

## Verification

Run both standalone, standard-library-only Python programs from the same directory as this document:

```sh
python3 verify_bitmask.py
python3 verify_incidence.py
```

Each program uses assertions that fail if any claimed enumeration or distance invariant is wrong; each prints a JSON scientific summary only after all checks complete. Both programs were executed against their actual packaged sources before acceptance, and both passed. There are no hidden input files or third-party dependencies. The observation operator uses monotone, simultaneous updates, so it terminates in at most twenty strict enlargement rounds. Each breadth-first search explores every reachable configuration, and the explicit assertion that all \(560\) configurations were reached proves connectedness and finiteness of all recorded distances.

## Relationship to prior work

Bjorkman et al., *Power domination reconfiguration*, arXiv:2201.01798 (first public 2022-01-05), introduces the relevant reconfiguration frameworks. Its Section 5 covers general results and specific families such as complete graphs, complete bipartite graphs, paths, cycles and wheels. Its vertex-cover-based threefold edge subdivision construction is different from the *doubled-vertex, singly subdivided* \(K_5\) defining the Folkman graph. The checked article does not imply this four-class census, connected slide metric or locality penalty. The 2022 survey of independent- and domination-set reconfiguration by Bousquet et al., arXiv:2204.10526, concerns different feasible-set predicates and gives general complexity context rather than this exact power-domination computation. The underlying Folkman graph construction itself is classical (1967), and no novelty is asserted for the graph or for the definition of power domination.

## Limitations

The claim is a complete finite theorem for the specific twenty-vertex Folkman graph only; it is not an assertion about arbitrary semisymmetric graphs or larger doubled subdivisions. The reproducible computation uses exhaustive enumeration and ordinary graph search; it is not an independent external mathematical audit. Searches of indexed literature and related records did not reveal a dominating pre-existing exact classification, but the possibility of an unindexed historical calculation cannot be eliminated by search alone.

## References

- B. Bjorkman, C. Bozeman, D. Ferrero, M. Flagg, C. Grood, L. Hogben, B. Jacob and C. Reinhart, *Power domination reconfiguration*, arXiv:2201.01798, initial submission 2022-01-05, https://arxiv.org/abs/2201.01798 ; later peer-reviewed version https://doi.org/10.1007/s44007-025-00187-5 .
- N. Bousquet, A. E. Mouawad, N. Nishimura and S. Siebertz, *A survey on the parameterized complexity of the independent set and (connected) dominating set reconfiguration problems*, arXiv:2204.10526, first public 2022-04-22, https://arxiv.org/abs/2204.10526 .
- *Folkman graph*, graph construction and classical bibliography, https://en.wikipedia.org/wiki/Folkman_graph (definition and historical context only).
