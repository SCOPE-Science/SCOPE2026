# Collapsibility of the full-symmetry quotient of the Petersen induced-forest complex

## Finding

Let \(P=\operatorname{KG}(5,2)\) be the Petersen graph with vertices the two-element subsets of \(\{0,1,2,3,4\}\), where two vertices are adjacent exactly when they are disjoint. Let
\[
\mathcal F(P)=\{A\subseteq V(P):P[A]\text{ is acyclic}\}
\]
be the induced-forest complex, and let \(G=\operatorname{Aut}(P)\cong\mathfrak S_5\) act on its ten vertices through the underlying five labels. The ordinary geometric orbit space admits a cellular collapse
\[
\boxed{|\mathcal F(P)|/G\searrow\{\mathrm{point}\}.}
\]
The quotient of the first barycentric subdivision is a regular cell complex with 15,255 cells. The explicit certificate gives 7,627 successive elementary free-face collapses, leaving one zero-cell. In particular the quotient is contractible, has trivial integral reduced homology and fundamental group, and has the simple-homotopy type of a point.

## Assumptions and scope

The graphs are finite and simple. A face is a vertex subset inducing an acyclic subgraph, not an edge subset of a graphic matroid. The empty set belongs to the abstract complex but does not index a geometric cell. The quotient uses all 120 graph automorphisms, not just a rotation subgroup. No freeness is assumed. This result concerns the ordinary quotient of this ten-vertex graph's forest complex, not a homotopy-orbit space or a general statement about vertex-transitive graphs.

## Proof

**1. The group and the face poset.** Identify the Petersen vertices with the ten lexicographically ordered pairs from the five labels. An independent set is a pairwise intersecting family of pairs. If such a family contains \(ab,ac\) and a pair not containing \(a\), that pair must be \(bc\); only these three pairs can meet all three. Thus every independent family with at least four members consists of pairs sharing one label. The five stars of size four are all the maximum independent sets. Any graph automorphism permutes the stars, and their pairwise intersections recover the graph vertices, so the action on the five stars is faithful. Conversely every label permutation preserves disjointness, giving \(\operatorname{Aut}(P)=\mathfrak S_5\).

Enumerating all 1,024 vertex subsets gives 785 nonempty forest faces. The counts by cardinality from one through seven are
\[
(10,45,120,210,240,140,20).
\]
The forest test uses both disjoint-set cycle detection and the identity \(|E(P[A])|=|A|-c(P[A])\), where \(c\) counts connected components. There are 23 orbits of nonempty faces.

**2. A regular orbit-cell structure.** A simplex of \(\mathrm{sd}\,\mathcal F(P)\) is a chain \(F_0\subsetneq\cdots\subsetneq F_d\) of nonempty forest faces. The ranks \(|F_i|\) are all different and are preserved by \(G\). Suppose two points of the same closed chain simplex lie in one orbit. Their positive barycentric coordinates must be carried to vertices at the same ranks. Within that simplex each rank occurs only once, so the support and all the barycentric coordinates agree. Thus the projection is injective on each closed simplex and, since the finite-group quotient is Hausdorff, embeds it. Images of open simplices are indexed by chain orbits, and the boundary of each image is the union of images of its proper faces. The finite quotient therefore has a regular cell structure with simplex-shaped cell closures. Omitting different chain entries gives different rank sets, so these boundary cells are never identified within one closure. Ordering each simplex by increasing rank gives boundary signs \((-1)^i\) for omitting position \(i\).

**3. Exact indexing and finite collapse.** Encode the ten graph vertices as bits in lexicographic pair order. Each nonempty face is an integer mask. For a chain \(C=(F_0,\ldots,F_d)\), put \(r=\min_{g\in G} gF_d\). The canonical representative is the lexicographically least transformed tuple among elements of \(G\) with \(gF_d=r\). Sort all distinct canonical chains by \((d+1,C)\) to give IDs from 0 to 15,254. The verifier reconstructs this indexing from the graph and group without reading the collapse pairs. Its orbit-cell counts in dimensions zero through six are
\[
(23,283,1535,3984,5230,3360,840).
\]

The file `collapse_pairs.txt` gives 7,627 pairs of cell IDs in deletion order. At each step both cells are present, and the smaller cell has exactly one remaining codimension-one coface, the paired larger cell. If it also had a coface at least two dimensions higher, then in the closure of that coface one could adjoin either of two different omitted ranks, giving two distinct remaining immediate cofaces. Thus the smaller cell is a free face, the larger cell is maximal, and their interiors can be removed by an elementary collapse of the current subcomplex. The verifier reconstructs all incidences, checks the integral identity \(\partial^2=0\), and validates each pair in the current complex. Under the specified indexing the one remaining zero-cell has **ID 21**. The resulting collapse is of the regular cellular model of the geometric quotient itself.

## Verification

With Python 3 and no external dependencies, put `verify.py` and `collapse_pairs.txt` in the same directory and run `python3 verify.py`. The program enumerates the face masks, cross-checks both forest tests, and reconstructs the full label action, flag orbits, and signed boundary operators. It checks \(\partial^2=0\) over the integers and replays the deletions, asserting that exactly one zero-cell is left. This is an exact finite certificate for the stated complex.

## Relationship to prior work

Grady, Knoll, Laskar and Lipman study the cycle-independent vertex-set condition [1]; Taylan's devoid-complex framework gives general graph-complex methods [2]. The exact-object result [3] identifies the unquotiented complex as a wedge of six 5-spheres and its rational fifth homology as a nontrivial irreducible \(\mathfrak S_5\)-module. This implies that the quotient is rationally acyclic: on the rank-ordered barycentric chains, taking group coinvariants gives the rational quotient cellular chains, and coinvariants are exact over \(\mathbb Q\) for a finite group. It does not supply integral contractibility or a collapse. The invariant simplicial collapses of [4] compare the unquotiented Petersen odd-cycle and forest complexes. The fixed-space classification [5] concerns subgroup fixed sets, not the full orbit space. The Petersen matching-complex quotient in [6] uses matchings of graph edges rather than induced forests on graph vertices.

## Limitations

The result is an exact, computer-assisted simple-homotopy statement for this graph alone. It is not an equivariant collapse of the original complex, which is not contractible. The comparisons are limited to the stated prior results and do not certify historical priority.

## References

1. A. Grady, F. Knoll, R. Laskar and D. J. Lipman, *Cycle Domination, Independence and Irredundance in graphs*, arXiv:1505.02268, https://arxiv.org/abs/1505.02268.
2. D. Taylan, *Matching trees for simplicial complexes and homotopy type of devoid complexes of graphs*, arXiv:1501.06754, https://arxiv.org/abs/1501.06754.
3. *Six fifth-dimensional spheres and irreducible symmetry in the Petersen induced-forest complex*, Resultary, `6b5572bd5bd2`, 25 October 2026.
4. *Ten symmetric simplicial collapses between Petersen odd-cycle and forest complexes*, Resultary, `531791bfccb6`, 25 October 2026.
5. *All nonidentity subgroup-fixed homotopy types of the Petersen induced-forest complex*, Resultary, `51d29ae59122`, 17 November 2026.
6. *Contractibility of the full-symmetry Petersen matching-complex quotient*, Resultary, `864a7b10c56a`, 17 November 2026.
7. R. Forman, *Morse theory for cell complexes*, Advances in Mathematics 134 (1998), 90–145.
