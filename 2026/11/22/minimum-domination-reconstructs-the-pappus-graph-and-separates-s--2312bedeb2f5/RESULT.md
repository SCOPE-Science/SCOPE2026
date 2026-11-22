# Minimum domination reconstructs the Pappus graph and separates static from adaptive shattering

## Finding

Let \(G\) be the eighteen-vertex Pappus incidence graph, and let \(\mathcal D\) be the Boolean concept class of **all minimum-cardinality ordinary dominating vertex sets** of \(G\). The theorem gives a complete geometric description of \(\mathcal D\), its two-point concurrence design, and every shattered membership-query support:

1. \(\gamma(G)=5\) and \(\mathcal D\) consists of precisely eighteen distinct five-vertex sets, nine centered at points and nine centered at retained affine lines, specified below.
2. Each vertex belongs to five optimal sets. Two distinct vertices appear together in zero optimal sets if they are adjacent, in exactly one if they lie in the same bipartition shore, and in exactly two if they lie in opposite shores but are nonadjacent. Consequently, adjacency is recovered *exactly* by zero concurrence in the optimum-set incidence matrix.
3. A support of vertex-membership queries is shattered if and only if it is empty, is a singleton, or consists of two nonadjacent vertices. Thus the complete shattering polynomial is
   \[\Phi_G(z)=1+18z+126z^2.\]
   The shattering complex is homotopy equivalent to a wedge of \(109\) circles.
4. The static and online dimensions differ sharply:
   \[\operatorname{VCdim}(\mathcal D)=2,\qquad \operatorname{Ldim}(\mathcal D)=3.\]

## Assumptions and scope

Work over \(F=\mathbb F_3\), with all arithmetic modulo three. The nine point vertices are \(P=F^2\), and the nine line vertices are the three retained parallel classes
\[
V_a=\{(x,y):x=a\},\quad H_b=\{(x,y):y=b\},\quad D_c=\{(x,y):y-x=c\},
\]
where \(a,b,c\in F\). A point is adjacent to a line vertex exactly when it belongs to that line. This is the Levi graph of the affine plane of order three with its fourth direction removed, hence the Pappus graph. The removed lines are \(E_s=\{(x,y):x+y=s\}\), \(s\in F\); they are **not** vertices of \(G\).

A dominating set is a set \(S\subseteq V(G)\) for which every vertex lies in \(S\) or is adjacent to a vertex of \(S\). Only sets of the minimum possible cardinality are concepts. A coordinate query at \(v\in V(G)\) returns \(1\) exactly when \(v\in S\). A support \(T\) is shattered when every binary trace on \(T\) occurs among those concepts. Littlestone dimension is the greatest depth of a complete binary tree of adaptive coordinate queries consistent with the concepts on each branch.

For each retained line \(\ell\), write \(\mathcal L(\ell)\) for its three-line parallel class and set
\[
A_\ell=(P\cap\ell)\cup(\mathcal L(\ell)\setminus\{\ell\}).
\]
For each point \(p=(x_p,y_p)\), let \(E(p)=E_{x_p+y_p}\) be its removed-direction line, and set
\[
B_p=((E(p)\cap P)\setminus\{p\})\cup\{\ell\in L:p\in\ell\}.
\]
Both definitions are subsets of the graph's vertices: \(A_\ell\) has three points and two line vertices, and \(B_p\) has two points and three line vertices.

## Proof

**Optimal-set classification.** Every closed neighborhood in the cubic graph has size four, so four vertices cover at most sixteen of the eighteen vertices. Hence \(\gamma(G)\ge5\). Each \(A_\ell\) and \(B_p\) dominates all eighteen vertices, by the parallel-class incidence properties, hence \(\gamma(G)=5\).

Let \(S\) be any dominating five-set with \(t=|S\cap P|\) points and \(5-t\) line vertices. Covering all nine point vertices requires \(t+3(5-t)\ge9\), so \(t\le3\). Covering all nine line vertices requires \((5-t)+3t\ge9\), so \(t\ge2\). If \(t=3\), the two selected lines must cover six *different* unselected points; they must be parallel, and the three selected points are exactly their omitted third parallel line. Therefore \(S=A_\ell\) for that omitted line \(\ell\).

If \(t=2\), the two selected points and three selected line vertices must account for all nine line vertices with no duplicated point-line incidences in this coverage bound. Thus the two points share no retained line, i.e., they lie on a single removed-direction line \(E_s\). In each retained direction they meet distinct lines; the one remaining line of that direction passes through the third point \(p\in E_s\). Hence the three selected line vertices are exactly the three retained lines through \(p\), and the two selected points are \(E_s\setminus\{p\}\). Thus \(S=B_p\). All sets of these two constructions are distinct (their shore cardinalities differ), proving there are nine of each and eighteen total.

**Concurrence and reconstruction.** A point \(p\) lies in the three sets \(A_\ell\) with \(\ell\ni p\) and the two sets \(B_q\) with \(q\ne p\) on \(E(p)\). A retained line \(\ell\) lies in the two sets \(A_h\) with \(h\ne\ell\) parallel to \(\ell\) and the three sets \(B_p\) with \(p\in\ell\). So each graph vertex has frequency five.

Two points on a retained line co-occur only in its \(A_\ell\); two points on a removed-direction line co-occur only in \(B_p\) for its third point. Two retained line vertices meet in exactly one \(B_p\) when they have different directions, or in exactly one \(A_h\) when parallel. These cover all pairs on the same shore, giving concurrence one. An incident point-line pair cannot occur in any \(A_\ell\) or \(B_p\), since these sets are independent. For a nonincident point \(q\) and retained line \(\ell\), one co-occurrence is in \(A_h\), where \(h\) is the line through \(q\) parallel to \(\ell\), and one is in \(B_p\), where \(p=\ell\cap E(q)\). There are no others. Thus the zero-concurrence pairs are **precisely the 27 edges of \(G\)**. In particular \(G\) is recovered from \(\mathcal D\) without using the original edge list; a vertex permutation preserves the optimum-set family exactly when it is a graph automorphism.

**Shattering.** Every singleton is shattered, since it occurs in five of the eighteen concepts. For distinct vertices \(u,v\), write \(c(u,v)\) for their concurrence. The four trace multiplicities, in order \((11),(10),(01),(00)\), are
\[
 c(u,v),\quad5-c(u,v),\quad5-c(u,v),\quad8+c(u,v).
\]
They are all nonzero exactly when \(c(u,v)>0\), equivalently when \(u,v\) are nonadjacent. There are \(\binom{18}{2}-27=126\) such supports. For any triple, at least two vertices lie in the same shore. Only one concept can contain both; shattering the triple would require *two* concepts containing that pair, one with and one without the third vertex. Therefore no triple, and by hereditary shattering no larger support, is shattered. This proves the polynomial and VC dimension.

The resulting one-dimensional simplicial complex has 18 vertices, 126 edges and is connected because each shore forms a complete subgraph. Its integral first Betti number is \(126-18+1=109\); as any connected graph deformation-retracts to a wedge of circles, the asserted integral homotopy equivalence follows (no higher homology or torsion).

**Adaptive dimension.** Each coordinate is positive on exactly five concepts. A depth-four complete decision tree would require at least eight distinct concepts in the positive child of its first query, impossible. Thus \(\operatorname{Ldim}\le3\). For a depth-three witness, start by querying any point \(p\). On the positive branch (five concepts), query a *nonincident* retained line: concurrence two splits the five concepts into groups of sizes two and three. On the negative branch (thirteen concepts), query an *incident* line: concurrence zero splits them into groups of sizes five and eight. Each of the four resulting groups consists of at least two distinct Boolean hypotheses, hence has some coordinate that splits it both ways. Query that separating coordinate at depth three. All eight leaves are nonempty, giving \(\operatorname{Ldim}\ge3\) and equality.

## Verification

The standalone standard-library script `verify_python.py` constructs the incidence graph and geometric candidate sets, enumerates all dominating sets of cardinality at most five, tests all singleton, pair and triple traces, and produces an explicit adaptive depth-three witness. The independent C++17 program `verify_cpp.cpp` enumerates every one of the \(2^{18}-1=262143\) nonempty vertex subsets without using the proposed geometric classification, checks the 18 optima, computes every pair concurrence and repeats all supports of sizes up to three. Both pass with the outputs in `python_output.txt` and `cpp_output.txt`.

The human proof, not the finite checker, supplies the conceptual explanations and establishes the geometry-to-learning implications. A separate graph-library isomorphism check of the affine incidence model against the standard Pappus graph returned true; the two standalone verification programs do not require that library.

## Relationship to prior work

The Pappus configuration and its affine completion are classical. Stroppel's 2018 work develops the group-theoretic configuration, its completion and polarities; its eighteen polarities are *not* the eighteen five-vertex dominating sets classified here. Potočnik and Toledo (first arXiv posting 11 March 2020) study cubic vertex-transitive graphs and classify the Pappus graph in cyclic-cover terminology; they do not give its minimum-domination design or membership-shattering dimensions. Biswas and Das (2022) extend the Pappus graph and determine automorphism groups, not its optimum-domination shattering.

A separate published result reconstructs the Pappus graph from eighteen **minimum locating-dominating six-sets** using their intersections. The present statement concerns eighteen **ordinary minimum dominating five-sets**, zero concurrence of graph-vertex coordinates, and an exact VC/Littlestone separation; neither statement implies the other without additional analysis. Standard shattering and graph-incidence definitions are used without claiming novelty. No earlier statement examined in the cited primary works yields the specific optimum-set classification, concurrence table, or online gap.

## Limitations

This is an exact theorem for a single canonical eighteen-vertex graph, not an all-order theorem for generalized Pappus graphs. Historical uniqueness is not certified: unindexed results or inaccessible sources could overlap. The 2018 source has an October publication month but no verified calendar *day* in the inspected record; the precisely dated 2020 arXiv item supplies the date-only source anchor without claiming to be the earliest publication of Pappus geometry. This is a self-review; no independent audit has been performed.

## References

- M. J. Stroppel, *Generalizing the Pappus and Reye configurations*, Australasian Journal of Combinatorics 72 (2018), 249–272. https://ajc.maths.uq.edu.au/pdf/72/ajc_v72_p249.pdf
- P. Potočnik and M. Toledo, *Finite cubic graphs admitting a cyclic group of automorphisms with at most three orbits on vertices*, arXiv:2003.05186 (first posted 2020-03-11). https://arxiv.org/abs/2003.05186
- S. Biswas and A. Das, *A generalization of Pappus graph*, Electronic Journal of Graph Theory and Applications 10 (2022), 345–356. https://doi.org/10.5614/ejgta.2022.10.1.25
- E. W. Weisstein, *Pappus Graph*, MathWorld. https://mathworld.wolfram.com/PappusGraph.html
- J. Petr, J. Portier, and L. Versteegen, *On the number of minimum dominating sets and total dominating sets in forests*, Journal of Graph Theory 106 (2024), 976–993. https://doi.org/10.1002/jgt.23107
