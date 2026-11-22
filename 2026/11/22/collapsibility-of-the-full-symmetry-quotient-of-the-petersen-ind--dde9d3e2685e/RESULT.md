# Collapsibility of the full-symmetry quotient of the Petersen induced-forest complex

## Finding
Let \(P=\operatorname{KG}(5,2)\) be the Petersen graph with vertices the two-element subsets of \(\{0,1,2,3,4\}\), where two vertices are adjacent exactly when they are disjoint. Let
\[
\mathcal F(P)=\{A\subseteq V(P):P[A]\text{ is acyclic}\}
\]
be the *induced-forest complex*, and let \(G=\operatorname{Aut}(P)\cong\mathfrak S_5\) act on its ten vertices through the underlying five labels. The ordinary geometric orbit space has a cellular collapse
\[
\boxed{|\mathcal F(P)|/G\searrow\{\mathrm{point}\}.}
\]
More explicitly, the first barycentric subdivision of \(\mathcal F(P)\), modulo \(G\), is a finite regular cell complex having 15,255 cells. The delivered explicit certificate verifies 7,627 successive elementary free-face collapses and leaves a single zero-cell. In particular the quotient is contractible, has trivial integral reduced homology and fundamental group, and has trivial simple-homotopy type.

## Assumptions and scope
All graphs are finite simple graphs. A face is a *vertex subset* inducing an acyclic subgraph, not an edge subset of a graphic matroid. The empty set belongs to the abstract complex but is not a geometric cell. The quotient identifies points under all 120 graph automorphisms, not just the fivefold rotation subgroup. No freeness of the action is assumed. The assertion concerns this ten-vertex graph and its ordinary topological quotient; it is not a general statement for all vertex-transitive graphs or for homotopy-orbit spaces.

## Proof
**1. The group and the face poset.** Identify the Petersen graph with the Kneser graph on the ten lexicographically ordered two-subsets of \(\{0,1,2,3,4\}\). Each of the five sets of four pair-vertices containing a given label is a maximum independent set, and these are all the independent four-sets. Any graph automorphism permutes these five stars; their pairwise intersections recover all ten graph vertices, so this action is faithful. Conversely every five-label permutation preserves disjointness, proving \(\operatorname{Aut}(P)=\mathfrak S_5\).

Enumerate all 1,024 subsets. A subset belongs to \(\mathcal F(P)\) precisely when its induced graph has no cycle; this is independently decided by a disjoint-set test and the equation \(|E(P[A])|=|A|-c(P[A])\), where \(c\) counts components. There are 785 nonempty faces, with counts by face cardinality one through seven
\[
(10,45,120,210,240,140,20),
\]
and 23 orbits of nonempty faces under \(\mathfrak S_5\).

**2. A regular orbit-cell structure.** The first barycentric subdivision \(\mathrm{sd}\,\mathcal F(P)\) is the order complex of the poset of its nonempty faces. A dimension-\(d\) simplex is a strict chain \(F_0\subsetneq\cdots\subsetneq F_d\) of forest faces. An element of \(G\) fixing such a chain setwise must fix each \(F_i\) individually, since the cardinalities are strictly increasing. Thus there are no inversions and the quotient of this barycentric subdivision has one regular cell for each orbit of chains. The codimension-one boundary faces are represented by omitting one chain element; different omissions have different sets of face cardinalities and hence are never identified within the same cell. Each attaching incidence consequently has degree \(\pm1\).

**3. Exact indexing and finite collapse.** Encode the ten graph vertices by bits in lexicographic pair order; each nonempty forest face is an integer mask. For a chain \(C=(F_0,\ldots,F_d)\), first put \(r=\min_{g\in G}gF_d\). Its canonical representative is the lexicographically least transformed integer tuple \((gF_0,\ldots,gF_d)\) among elements satisfying \(gF_d=r\). Sort all distinct canonical chains by \((d+1,C)\) to give cell IDs from 0 to 15,254. The program reconstructs this entire indexing from the graph and group without reading the certificate. The resulting orbit-cell counts in dimensions zero through six are
\[
(23,283,1535,3984,5230,3360,840).
\]

The file `collapse_pairs.txt` gives 7,627 pairs of cell IDs, in deletion order. At each step the smaller cell has exactly one remaining codimension-one coface, which is the paired larger cell. A higher-dimensional remaining coface would produce at least two distinct immediate cofaces by adjoining two different omitted chain ranks; thus a unique remaining immediate coface implies there is no higher coface. Removing the pair preserves the subcomplex property, so each step is a genuine elementary CW collapse. The checker re-creates all orbit-cell incidence relations, verifies the full integral cellular boundary identity \(\partial^2=0\), and tests every pair against the *current* complex; it finishes with exactly one vertex (ID 2570). Hence these are elementary collapses of the actual geometric quotient and prove the displayed topological conclusion.

## Verification
With Python 3 and no external dependencies, put `verify.py` and `collapse_pairs.txt` in the same directory and execute `python3 verify.py`. The program enumerates all masks; cross-checks two independent forest tests; reconstructs the full 120-element symmetry action, canonical flag orbits, signed boundary operators and all 15,255 cells; verifies \(\partial^2=0\) over the integers; and independently replays each proposed deletion. It asserts that exactly one zero-cell remains. Neither a floating-point approximation nor a truncated search is used in the proof. The certificate is an exhaustive finite proof for the specified finite graph, not an assertion about a graph family.

## Relationship to prior work
Grady, Knoll, Laskar and Lipman introduced the cycle-independent vertex-set condition in 2015; Taylan's 2015 devoid-complex framework gives general graph-complex methods but does not classify this symmetry quotient. The previously published exact-object classification *Six fifth-dimensional spheres and irreducible symmetry in the Petersen induced-forest complex* gives \(\mathcal F(P)\simeq\bigvee^6 S^5\) and a rational irreducible \(\mathfrak S_5\)-module on its fifth homology, so the full quotient is rationally acyclic. That does not imply integral contractibility, and it supplies no sequence of collapses of the orbit space. The published *Ten symmetric simplicial collapses between Petersen odd-cycle and forest complexes* compares two unquotiented spaces by an invariant matching, but does not determine either full geometric quotient's integral simple-homotopy type. The published classification of subgroup **fixed spaces** also does not classify the group orbit space. These distinctions are between mathematical statements, not merely between their titles.

## Limitations
This is a computer-assisted, finitely exhaustive simple-homotopy statement for this specific graph. Correctness depends on the supplied explicit enumeration and certificate as checked by the included independent reconstruction program. It neither determines equivariant homotopy types nor implies that the original complex is contractible (it is not). The novelty comparison is to the literature and research records actually inspected; an unindexed equivalent claim remains possible.

## References
1. D. Taylan, *Matching trees for simplicial complexes and homotopy type of devoid complexes of graphs*, first arXiv public version 27 January 2015, https://arxiv.org/abs/1501.06754 .
2. A. Grady, F. Knoll, R. Laskar, D. J. Lipman, *Cycle Domination, Independence and Irredundance in graphs*, first arXiv public version 9 May 2015, https://arxiv.org/abs/1505.02268 .
3. *Six fifth-dimensional spheres and irreducible symmetry in the Petersen induced-forest complex*, public mathematical research record, 25 October 2026, https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-six-fifth-dimensional-spheres-and-irreducible-symmetry-in-the-pe--6b5572bd5bd2 .
4. *Ten symmetric simplicial collapses between Petersen odd-cycle and forest complexes*, public mathematical research record, 25 October 2026, https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-ten-symmetric-simplicial-collapses-between-petersen-odd-cycle-an--531791bfccb6 .
5. R. Forman, *Morse theory for cell complexes*, Advances in Mathematics 134 (1998), 90–145. The standard notion of elementary CW collapse is used directly.
