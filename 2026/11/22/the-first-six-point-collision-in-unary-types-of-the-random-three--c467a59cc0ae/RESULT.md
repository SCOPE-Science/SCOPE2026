# The first six-point collision in unary types of the random three-polyhedron

## Finding

Let \(\mathcal P_3\) denote the countable unordered Fraïssé limit of finite simplicial complexes with all faces of cardinality at most three (topological dimension at most two). Let \(A\) be an induced finite named subcomplex and \(G\) its one-skeleton. If \(e(G[S])\) denotes the number of edges induced on \(S\subseteq V(G)\), then the number \(T(A)\) of complete nonalgebraic one-variable types over \(A\) is

\[
T(A)=Z(G):=\sum_{S\subseteq V(G)}2^{e(G[S])}.
\]

In particular the old triangle set does not affect this count. To avoid the immediate ambiguity caused by varying triangles while keeping the same graph, associate to any simple graph \(G\) its canonical triangle-filled two-complex \(K(G)\), with one triangle for every three-clique and no faces of larger size. The scalar \(T(K(G))\) distinguishes the underlying graph up to isomorphism at orders one through five. At order six, its complete list of non-singleton fibres among the 156 unlabelled simple graphs comprises exactly **three two-element fibres**, at values \(256\), \(376\), and \(832\). In exactly one of these fibres both graphs are connected: the fibre at \(832\). Its graphs have degree multisets \((2,2,2,2,3,5)\) and \((1,2,3,3,3,4)\), so they are nonisomorphic.

The following six orbit representatives give all the exceptions. Vertex labels are \(0,1,\ldots,5\); a mask encodes the fifteen potential edges in lexicographic order \((0,1),(0,2),\ldots,(4,5)\).

| \(T(K(G))\) | Edge mask | Connected? | Sorted degrees |
|---|---:|---|---|
| \(256\) | 61 | yes | \((1,1,1,1,2,4)\) |
| \(256\) | 110 | no | \((0,1,2,2,2,3)\) |
| \(376\) | 123 | yes | \((1,1,1,2,3,4)\) |
| \(376\) | 685 | no | \((0,2,2,2,3,3)\) |
| \(832\) | 927 | yes | \((2,2,2,2,3,5)\) |
| \(832\) | 1751 | yes | \((1,2,3,3,3,4)\) |

For the two connected graphs in the last fibre, the induced-edge histograms (coefficients of \(\sum_{S\subseteq V}y^{e(G[S])}\)) are respectively

\[
16+16y+12y^2+6y^3+7y^4+2y^5+4y^6+y^8,
\]
\[
16+14y+15y^2+5y^3+7y^4+4y^5+y^6+y^7+y^8.
\]

These are different polynomials but both evaluate to \(832\) at \(y=2\).

## Assumptions and scope

The language has an irreflexive symmetric binary face relation, an irreflexive symmetric ternary face relation, and the simplicial closure rule that a triple face forces its three edge faces. No faces of size four or more are included. Named parameters form an arbitrary finite induced subcomplex; only complete nonalgebraic one-types (new points different from all parameters) are counted. Graph comparison ignores the irrelevant choices of old two-faces by using the canonical triangle-filled subcomplex \(K(G)\). Comparisons are among **unordered underlying graph isomorphism types**, not different parameter labellings or orderings.

## Proof

**Link count.** Fix a fresh vertex \(x\). Its edge neighbours among the parameters can be any subset \(S\) of the old vertex set. Once \(S\) is chosen, every potential new triangle is of the form \(\{x,a,b\}\) with \(a,b\in S\) and \(\{a,b\}\) an old edge. Conversely every subset of these \(e(G[S])\) triangles defines a valid one-point simplicial extension: all necessary edges are present and there is no further dimension-three constraint. Hence exactly \(2^{e(G[S])}\) extensions correspond to \(S\). By the one-point extension property of the Fraïssé limit, all are realized. Homogeneity in this finite relational language makes distinct finite diagrams exactly the distinct complete one-types over \(A\). Summing proves the displayed formula for arbitrary \(A\).

**Finite sharp cutoff.** On \(n\) labelled vertices, enumerate all \(2^{\binom n2}\) simple graphs as edge masks. For each mask, its full orbit under the \(n!\) vertex permutations is marked. The first unmarked mask represents a new isomorphism type, and every labelled graph is covered because the outer loop visits every mask. The attached standalone `verify.py` uses this exhaustive algorithm for each \(1\le n\le6\). For each orbit representative it enumerates all \(2^n\) vertex subsets and evaluates the exact integer sum from the link-count formula. Its output verifies orbit counts \(1,2,4,11,34,156\), connectivity counts \(1,1,2,6,21,112\), no collisions below six, and exactly three two-element fibres at six with values and representatives as tabulated. It also checks connectedness and degree multisets for the full six-point classification. Since no labelled graph is skipped and orbit equivalence is exactly graph isomorphism, this is a finite exhaustive proof of the cutoff and uniqueness claims.

**Nonisomorphism and the connected fibre.** The two connected representatives in the fibre \(832\) have different degree multisets, so they cannot be isomorphic. Each of the other two fibres has exactly one disconnected representative. No other collision fibre exists, proving the unique connected-connected collision. The explicit edge histograms of the connected pair independently show the common value \(832\).

## Verification

Run `python3 verify.py` with Python 3 and no third-party dependencies. It checks each graph mask, every vertex permutation orbit, all vertex subsets, six representative encodings and the claimed classification, terminating with `EXHAUSTIVE_COLLISION_CHECK_OK`. Direct, independent enumeration of the standard graph-atlas isomorphism representatives gave the same three fibres, but the proof and provided script do not depend on that atlas. The exhaustive portion ends at six vertices; the link-count identity is valid for every finite base.

## Relationship to prior work

Mijares and Padilla introduced the ordered and unordered random polyhedra and their fixed-dimensional variants; their work establishes the relevant Fraïssé setting, rather than this unary-type reconstruction threshold. The type sum is also the graph two-spin partition function at edge interaction weights \(\left(\begin{smallmatrix}1&1\\1&2\end{smallmatrix}\right)\) and unit vertex activity: the state \(1\) is membership in \(S\). Thus the scalar is an existing kind of partition-function evaluation, not a newly invented graph polynomial. Liao and Hou study a different induced-subgraph invariant, weighted by component count, and its distinguishing power; their results do not state the present fixed-evaluation six-vertex classification. The literature comparison supports a specific new minimal-collision claim, not an assertion that partition functions or graph orbit enumeration were unknown.

## Limitations

Only the scalar count is compared, not the complete one-type space, its graph of relations, or the full induced-edge polynomial. For bases with freely varying old triangle sets, equal type counts arise even when the one-skeleton is fixed; the graph-reconstruction question therefore explicitly uses the canonical triangle-filled bases. The exact collision classification is proved only through six vertices and says nothing about uniqueness at higher orders. Independent external mathematical validation and exhaustive historical-priority checking have not been performed; an older table of specialized two-spin evaluations might already contain these collisions.

## References

- J. G. Mijares and G. Padilla, *A Ramsey space of infinite polyhedra and the random polyhedron*, arXiv:1209.6421, initially public 2012-09-28, especially Sections 6–7 (fixed-dimensional limits and unordered reducts), https://arxiv.org/abs/1209.6421.
- Y. Liao and Y. Hou, *Note on the subgraph component polynomial*, arXiv:1311.6856, initially public 2013-11-27; Electronic Journal of Combinatorics 21 (2014), P3.27, https://arxiv.org/abs/1311.6856.
