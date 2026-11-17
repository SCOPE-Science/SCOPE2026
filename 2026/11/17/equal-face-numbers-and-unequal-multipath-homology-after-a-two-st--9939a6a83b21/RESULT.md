# Equal face numbers and unequal multipath homology after a two-step tournament reversal

## Finding

For an integer \(n\ge 3\) and \(0\le a\le n-3\), let \(T_{n,a}\) be the tournament on \(\{0,\dots,n-1\}\) that orients every edge from the smaller index toward the larger, except that the edge between \(a\) and \(a+2\) is oriented \(a+2\to a\). Let \(X_{n,a}\) be its directed-linear-forest (multipath) simplicial complex: vertices are directed edges and faces are edge sets that form vertex-disjoint directed simple paths, allowing isolated vertices.

**Finite homological counterexample.** The five-dimensional complexes \(X_{7,0}\) and \(X_{7,1}\) have the same complete face vector, including the empty face,
\[
(f_{-1},f_0,f_1,f_2,f_3,f_4,f_5)=(1,21,142,370,351,93,3),
\]
but their reduced mod-two homology groups differ:
\[
\widetilde H_i(X_{7,0};\mathbb F_2)\cong
\begin{cases}\mathbb F_2^6&i=2,\\\mathbb F_2^{19}&i=3,\\0&\text{otherwise,}\end{cases}
\]
\[
\widetilde H_i(X_{7,1};\mathbb F_2)\cong
\begin{cases}\mathbb F_2^{13}&i=3,\\0&\text{otherwise.}\end{cases}
\]
In particular the complexes are **not homotopy equivalent**, even though both underlying tournaments arise from reversing one edge spanning two positions in a transitive tournament, and each tournament has exactly one directed cycle, a triangle. Among these two-step reversal families with \(3\le n\le6\), all permitted reversal positions yield identical face vectors and reduced mod-two Betti numbers. Hence seven vertices is the first size at which the reversal's position distinguishes mod-two homology within this family.

## Assumptions and scope

All graphs here are finite simple tournaments, with one oriented edge per unordered vertex pair. A face of \(X_{n,a}\) is a set of arcs with in-degree and out-degree at most one at every vertex and no directed cycle. The complex includes the empty face; \(f_{-1}=1\). All claimed homology computations use the field \(\mathbb F_2\) and reduced simplicial chains; the listed ranks do not by themselves specify integral homology or an integral homotopy decomposition.

## Proof

**(1) Unique cycle and an exact face-membership test.** Every arc of \(T_{n,a}\), apart from \(a+2\to a\), strictly increases the integer vertex label. Consequently every directed cycle must traverse the reversed arc, followed by an increasing path from \(a\) to \(a+2\). The only possible strictly increasing intermediate vertex is \(a+1\), so the unique directed cycle is the directed triangle \(a\to a+1\to a+2\to a\). Any subgraph with indegree and outdegree at most one is a disjoint union of directed paths and directed cycles. Thus its edge set is a face exactly when no two edges share a source, no two share a target, and the three edges of that triangle are not all chosen.

**(2) Exhaustive finite face enumeration.** Order the \(\binom72=21\) arcs by the lexicographic order of their unordered endpoints. For each cardinality from zero to six, enumerate every subset of arc indices and apply the exact path test above (the code also detects cycles directly by following successor maps). There can be no face of seven or more arcs on seven vertices, since a directed path forest with \(k\) edges uses at least \(k+1\) vertices. Both seven-vertex complexes have respectively \(1,21,142,370,351,93,3\) faces of cardinalities zero through six. A separate recursive face-extension enumeration reconstructs exactly the same sets of faces.

**(3) Exact boundary-matrix ranks.** Over \(\mathbb F_2\), the augmented simplicial boundary of a nonempty ordered face \([e_1,\dots,e_s]\) is the sum of its \(s\) codimension-one faces. Form the boundary matrices using the complete enumerated face lists. For cardinalities \(s=1,\dots,6\), the exact ranks of these boundaries are respectively
\[
(1,20,122,242,90,3)\quad\text{for }X_{7,0},
\]
\[
(1,20,122,248,90,3)\quad\text{for }X_{7,1}.
\]
The rank computation is exact binary Gaussian elimination. Independent calculations with column vectors and with transposed row vectors agree at every degree. Applying the identity \(\dim\widetilde H_{s-1}=c_s-r_s-r_{s+1}\), where \(c_s\) is the number of cardinality-\(s\) faces and \(r_s\) is the cardinality-\(s\) augmented boundary rank, gives all listed reduced Betti numbers. The code also checks each boundary-square identity by direct pairwise cancellation.

**(4) Small-size threshold.** For every admissible two-step reversal position and each \(3\le n\le6\), the same independent face enumeration and rank procedures give, respectively, the common face-count sequences \((1,3,3)\), \((1,6,9,3)\), \((1,10,27,21,3)\), and \((1,15,67,102,45,3)\); the nonzero reduced mod-two homology ranks are respectively \(\widetilde\beta_1=1\), \(\widetilde\beta_1=1\), none, and \(\widetilde\beta_2=7\). Thus seven is the first order in the stated family exhibiting a location-dependent homological invariant. Since homotopy equivalences preserve homology over every field, the seven-vertex examples are not homotopy equivalent. \(\square\)

## Verification

Run `python3 checks/verify.py` with Python 3 and no third-party dependencies. Its full recorded standard output is in `checks/verification_output.txt`. The program enumerates all faces by **two separate algorithms**, computes each binary boundary rank from both the rows and columns, verifies the chain identity, and checks all two-step reversal positions through six vertices. It prints the exact boundary ranks and concludes `NEAR_TRANSITIVE_TOURNAMENT_FVECTOR_HOMOLOGY_CHECK_PASS` only after all assertions succeed. This is a complete finite proof certificate for the stated seven-vertex face and mod-two rank assertions, not numerical sampling or an infinite-family extrapolation.

## Relationship to prior work

Deshpande and Sawant (first publicly submitted February 16, 2026) identify the directed-linear-forest complex with a conflict-hypergraph independence complex and study vertex decomposability and shellability under structural hypotheses. In particular their Section 5.2 contains a general face characterization; the characterization itself is **not** claimed here as new. Their inspected results do not give the position-sensitive, equal-face-vector homology comparison in the finding.

Caputi, Collari, Di Trani and Smith (2022 preprint; 2024 journal article) compute the Euler characteristic of transitive-tournament multipath complexes, establish their sphere-wedge property, and in Theorem 3.5 treat reversal of the **outermost** edge of a transitive tournament at the level of Euler characteristic. That outermost reversal is different from the two-step reversals above, and an Euler characteristic alone cannot distinguish these two complexes, which have the same face vector and different graded homology. The result is a finite homological counterexample, not a new general structure theorem for all tournaments.

## Limitations

The new computation concerns mod-two homology of the two explicitly given seven-vertex tournaments and a small-order comparison in one natural reversal family. It does not calculate integral torsion, integral homotopy types, or an infinite-order formula, and it makes no claim that the two complexes are the smallest possible equal-face-vector non-homotopy-equivalent multipath complexes among *all* digraphs. Standard bibliographic searches and inspected primary works do not rule out a differently worded or unindexed prior instance.

## References

1. P. Deshpande and R. Sawant, *Vertex decomposable complexes of directed forests, conflict graphs and chordality*, arXiv:2602.14936 (first submitted 2026-02-16), especially Sections 3 and 5.2. https://arxiv.org/abs/2602.14936
2. L. Caputi, C. Collari, S. Di Trani and J. P. Smith, *On the homotopy type of multipath complexes*, arXiv:2208.04656 (first submitted 2022-08-09); *Mathematika* **70** (2024), e12235, especially Theorems 3.4, 3.5 and 5.1. https://irep.ntu.ac.uk/id/eprint/50523/
