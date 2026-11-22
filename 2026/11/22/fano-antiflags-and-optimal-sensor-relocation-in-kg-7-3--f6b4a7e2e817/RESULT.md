# Fano antiflags and optimal sensor relocation in \(KG(7,3)\)

## Finding

Let \(G=KG(7,3)\) be the odd graph with 35 vertices indexed by three-element subsets of \(\{0,1,2,3,4,5,6\}\), with adjacency precisely when the triples are disjoint. Under standard power domination, \(\gamma_P(G)=4\). There are exactly **840** four-vertex minimum power-dominating sets, and they have the following unique description.

Choose a point \(c\), partition the other six points into three unordered pairs \(P_1,P_2,P_3\), and choose a transversal \(b=\{b_1,b_2,b_3\}\) containing exactly one point of each pair. Then
\[
S(c;P_1,P_2,P_3;b)
=\bigl\{\{c\}\cup P_1,\{c\}\cup P_2,\{c\}\cup P_3,b\bigr\}
\]
is minimum power dominating, and **these are all** minimum power-dominating sets. Equivalently, each is the set of the three lines through a point and one line not through that point in a *uniquely determined labelled Fano plane*. Thus the minimum sensor placements are in bijection with the nonincident point-line pairs (antiflags) in all 30 labelled Fano planes. The count is
\[
7\cdot15\cdot8=30\cdot7\cdot4=840.
\]

On these 840 configurations define \(J\) by a *token jump*: change one chosen graph vertex to any other while retaining a minimum power-dominating set. Define \(T\) by a *token slide*: make the same replacement but require the removed and inserted graph vertices to be adjacent in \(G\), i.e., disjoint as ground-set triples.

The graph \(J\) is connected, vertex-transitive, and 13-regular, with 5,460 edges, radius six, and diameter six. Every vertex has distance-profile polynomial
\[
1+13z+39z^2+87z^3+204z^4+320z^5+176z^6.
\]
The slide graph \(T\) is a perfect matching of **420 disjoint edges**. The unique slide from \(S(c;P_1,P_2,P_3;b)\) replaces the transversal \(b\) by the complementary transversal \((\{0,\ldots,6\}\setminus\{c\})\setminus b\), fixing the three pencil lines. No sequence of slides can move between two different slide pairs, whereas all 840 placements communicate under jumps within six moves.

## Assumptions and scope

The ground set is precisely seven labelled points; only the 35 distinct three-subsets are graph vertices. Power domination begins with \(S\cup N(S)\) observed. In each subsequent round, every observed vertex with exactly one unobserved neighbor may observe that neighbor; steps repeat to closure. Simultaneous or sequential application of legal propagation rules gives the same closure. Sensors occupy distinct graph vertices. Both reconfiguration graphs contain *only* minimum sets of cardinality four, never larger intermediate placements. A jump changes exactly one sensor vertex. A slide additionally requires that the changed three-subsets be disjoint.

No result is claimed for \(KG(n,r)\) outside the single graph \(KG(7,3)\), or for arbitrary dominating, zero-forcing, or feedback sets.

## Proof

**1. Symmetry-reduced exhaustive classification.** Any permutation of the seven underlying points is a graph automorphism, because disjointness of triples is preserved. The complete 35-vertex graph, its closed-neighborhood initialization, and the monotone forcing closure are explicit finite objects. Enumerate all \(\binom{35}{3}=6,545\) distinct triple placements and all \(\binom{35}{4}=52,360\) distinct quadruple placements, and partition each collection into orbits under the \(7!=5,040\) ground-point permutations. The supplied `verify_symmetry.py` builds the permutations and orbit images directly, without assuming a precomputed orbit list. It finds **10** orbits of three-sensor configurations and **38** orbits of four-sensor configurations, covering exactly the stated numbers of candidates. None of the ten three-set orbit representatives observes all 35 vertices. Exactly one of the 38 four-set orbit representatives succeeds, namely
\[
S_0=\{012,034,056,135\},
\]
where three-digit strings designate ground-set triples. Its initial observed set has 20 vertices; two successive propagation rounds add 9 and 6 previously unseen vertices, respectively, and therefore observe all 35 vertices. Every other four-set orbit representative has final closure strictly smaller than 35. The 48 representative checks, orbit sizes, initial observed counts, closure sizes, and rounds are recorded in `orbit_census.csv`. These comparisons are finite exhaustive proofs, not statistical sampling: for every candidate, the symmetry action maps it to a listed representative, and the observation closure is equivariant under graph automorphisms. Since no set of size three works, monotonicity of power domination also excludes sizes zero, one, and two.

**2. Combinatorial identification of the successful orbit.** The displayed representative is a central three-line pencil through \(0\), using the partition \(12|34|56\), plus the transversal \(135\). Permuting the seven labels yields precisely the sets in the claimed form. Conversely, the root \(c\) is the unique point occurring in three of the four selected triples; the three pair blocks are uniquely recoverable from the triples containing \(c\), and the remaining triple is their transversal. There are 7 choices of root, \((6-1)!!=15\) pair partitions, and \(2^3=8\) transversals, so these 840 distinct sets form exactly the single successful orbit. This also proves that all these sets work, not merely the representative.

To obtain the Fano-plane interpretation, write each pair \(P_i=\{b_i,d_i\}\) with the chosen transversal \(b=\{b_1,b_2,b_3\}\). The three further triples
\[
\{b_1,d_2,d_3\},\quad \{d_1,b_2,d_3\},\quad \{d_1,d_2,b_3\}
\]
together with \(b\) and the three pencil lines form the seven blocks of a Steiner \(2\)-\((7,3,1)\) design: every ground-set pair appears in exactly one block. This construction is forced once the pencil and \(b\) are fixed, because a line not through \(c\) must take one element from each pair and every two such lines meet exactly once. Hence the Fano plane extending the four selected lines is unique. There are 30 labelled Fano planes, each with 7 choices of a point and 4 choices of a line not through it, again giving 840.

**3. All legal one-sensor moves.** Fix a configuration with pencil lines \(A_1,A_2,A_3\) and transversal \(b\). Replacing \(b\) while retaining the three pencil lines leaves precisely the other seven transversals, since any successful configuration keeping all three pencil lines must use their unique shared root. Exactly one of those seven replacement transversals is disjoint from \(b\): its complementary transversal.

Now replace a pencil line, say \(A_3\). The three unchanged triples \(A_1,A_2,b\) meet pairwise at three distinct points \(c,b_1,b_2\). A new successful configuration must be another three-line pencil plus a transversal. If the new pencil root is \(c\), then the fourth line is forced to be the original \(A_3\), giving no change. If the root is \(b_1\) or \(b_2\), there is exactly one possible new line through that root whose other two points are the remaining unused points, and it yields a valid central pencil plus transversal. These are exactly two new configurations. Each replacement line shares a ground-set point with the removed \(A_3\), so neither move is a slide. The same argument works for \(A_1\) and \(A_2\). Thus every configuration has \(7+3\cdot2=13\) jump neighbors but exactly one slide neighbor. That one slide interchanges \(b\) with its complement, and is involutive, proving that \(T\) is 420 copies of \(K_2\).

**4. Exact jump distances.** The natural \(S_7\)-action is transitive on the 840 configurations, so the distance profile is the same at every configuration. The independently coded adjacency construction and breadth-first search in `verify_symmetry.py` visit all 840 configurations from \(S_0\), and report level sizes
\[
(1,13,39,87,204,320,176)
\]
for distances zero through six. These totals sum to 840, so \(J\) is connected and has eccentricity six at \(S_0\); vertex transitivity makes its radius and diameter both six. The separate `verify_full.py` constructs the entire jump graph without orbit reduction and independently checks all 840 breadth-first-search distance rows, including the unordered-pair distance counts
\[
(5460,16380,36540,85680,134400,73920)
\]
for distances one through six. They sum to \(\binom{840}{2}=352,380\), confirming exhaustiveness.

## Verification

The supplied reproducible finite evidence consists of `verify_full.py`, `verify_symmetry.py`, `orbit_census.csv`, and `CERTIFICATE.json`. Both scripts require only Python 3 standard-library modules. From the directory containing these files, run `python3 verify_full.py` and `python3 verify_symmetry.py`. The first uses integer-bitset propagation, direct checks of every placement of size at most four, and all-pairs graph distances. The second uses Python sets and the entire seven-point permutation group to enumerate orbit representatives, checks closure under a separately written propagation implementation, reconstructs the fan configurations, and uses a root-distance search plus transitivity. The second script regenerates the included 48-orbit CSV. Both programs executed successfully with the stated counts.

In particular the orbit census verifies completeness of the finite domain; numerical shortest-path data are not being extrapolated to an infinite graph family. The structural pencil and local-move arguments above independently explain the 840-state classification, 13 jump neighbors, and exactly one slide per placement; the exact jump diameter and level distribution rely on the fully specified finite computation.

## Relationship to prior work

Bjorkman, Bozeman, Ferrero, Flagg, Grood, Hogben, Jacob, and Reinhart (arXiv:2201.01798, first publicly available 2022-01-05) define and study power-domination reconfiguration and its unrestricted token-jumping graph; Sections 4 and 5 establish general constructions and specific cases but do not supply this odd-graph classification. Curtis, Flagg, and Hogben (arXiv:2406.05509, first publicly available 2024-06-08) survey general TAR reconfiguration of vertex-set parameters rather than this sharp token-slide dichotomy. Cornet and Torres (arXiv:2308.15603, first publicly available 2023-08-29) establish that the *ordinary* domination number of \(KG(7,3)\) is seven and that the corresponding minimum dominating sets are Fano planes, as part of an analysis of tuple domination and 2-packings. That work motivates the present Fano-plane interpretation, but ordinary neighborhood domination is not power domination, and knowing the seven-line minimum dominating sets does not determine the four-sensor forcing closure, the 840 four-sensor optima, or either reconfiguration graph.

The known two-subset Kneser-graph power-domination results concern \(KG(n,2)\), not \(KG(7,3)\). The present result addresses the first odd graph beyond the Petersen graph and the operationally natural distinction between replacing and locally sliding optimum sensors.

## Limitations

This is an exact result for one finite graph. The complete four-subset classification and jump distance statistics depend on transparent exhaustive computations with a stated 35-vertex domain and 840-state configuration graph, rather than on an infinite-family symbolic characterization. The structural proofs explain the class, counts, and one-step moves; the exact jump-distance distribution is supported by two independently implemented finite searches. No extrapolation to larger odd graphs, arbitrary reconfiguration budgets, resilience to sensor failure, or independent external audit is claimed. Literature searching does not exclude unindexed or differently named prior results; a separate expert comparison remains useful before attribution of priority.

## References

1. B. Bjorkman, C. Bozeman, D. Ferrero, M. Flagg, C. Grood, L. Hogben, B. Jacob, C. Reinhart, *Power domination reconfiguration*, arXiv:2201.01798, first version 2022-01-05. https://arxiv.org/abs/2201.01798
2. M. G. Cornet, P. Torres, *k-tuple domination on Kneser graphs*, arXiv:2308.15603, first version 2023-08-29. https://arxiv.org/abs/2308.15603
3. B. Curtis, M. Flagg, L. Hogben, *TAR reconfiguration for vertex set parameters*, arXiv:2406.05509, first version 2024-06-08. https://arxiv.org/abs/2406.05509
4. B. Brešar, T. Kos, P. Torres, *Grundy domination and zero forcing in Kneser graphs*, Ars Mathematica Contemporanea 19 (2020), a related but distinct vertex-parameter study. https://doi.org/10.26493/1855-3974.1881.384
