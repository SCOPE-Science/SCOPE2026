# Minimum total resolving sets of triangular graphs are long-cycle packings

## Finding
For every integer \(n\ge6\), the total metric dimension of the triangular graph \(J(n,2)=L(K_n)\) is
\[
\operatorname{dim}_t(J(n,2))=n-1.
\]
All its minimum total resolving sets correspond exactly to the edge sets of a spanning graph on \([n]\) consisting of **one isolated vertex and a disjoint union of simple cycles of lengths at least five** on the remaining vertices. This is an if-and-only-if classification.

The number \(b_n\) of such sets, with all \(n\) ground vertices labelled, is
\[
b_n=n!\,[z^{n-1}]\exp\!\left(\sum_{\ell\ge5}\frac{z^\ell}{2\ell}\right).
\]
For example \(b_6=72\), \(b_7=420\), \(b_8=2880\), \(b_9=22680\), \(b_{10}=201600\), and \(b_{11}=2195424\). The first minimum bases with multiple cycle components appear at \(n=11\): there are \(199584\) bases made of an isolated vertex and two five-cycles, as well as \(1995840\) bases made of an isolated vertex and one ten-cycle.

## Assumptions and scope
All graphs are finite, simple, undirected and unweighted. The triangular graph \(J(n,2)\) has one vertex for each two-element subset of \([n]=\{1,\ldots,n\}\), adjacent precisely when the corresponding subsets intersect. For any two *different* vertices \(A,B\), distance is \(2-|A\cap B|\), while \(d(A,A)=0\).

A subset \(S\subseteq V(J(n,2))\) is **totally resolving** if, for every two different vertices \(A,B\), there exists \(W\in S\setminus\{A,B\}\) satisfying \(d(W,A)\ne d(W,B)\). The minimization defining \(\operatorname{dim}_t\) is over such subsets. Associate to \(S\) a ground graph \(H=([n],S)\), treating two-element subsets as edges. The claim concerns ordinary labelled sets of landmarks, not landmark orders, graph-isomorphism classes or ordinary resolving sets for which self-witnesses are permitted.

## Proof
**Exact witness criterion.** We first prove that a ground graph \(H\) corresponds to a total resolving set if and only if both of the following hold:

(A) For any three pairwise distinct labels \(a,b,c\), at least one edge of \(H\) joins exactly one of \(b,c\) to a label outside \(\{a,b,c\}\).

(B) For any four distinct labels forming a set \(X\subseteq[n]\), at least one edge of \(H\) crosses the cut \((X,[n]\setminus X)\).

For an intersecting pair \(A=\{a,b\}\), \(B=\{a,c\}\), a third pair \(W\ne A,B\) distinguishes them precisely when one of \(b,c\), but neither \(a\) nor the other of \(b,c\), belongs to \(W\). Such a \(W\) is exactly an edge from one of \(b,c\) to outside \(\{a,b,c\}\), proving (A). For a disjoint pair \(A,B\), let \(X=A\cup B\). A third pair \(W\) distinguishes \(A,B\) exactly when it contains one label of \(X\) and one outside it: pairs internal to \(X\) that are not \(A,B\) meet each of them once; pairs disjoint from \(X\) meet neither; and \(A,B\) themselves are forbidden. This proves (B), independent of the pairing of \(X\).

**Lower bound.** Criterion (A) prohibits two isolated ground vertices: choose them as \(b,c\). It also prohibits every nontrivial tree component. Indeed, a component comprising a single edge fails (A) with both ends as \(b,c\), choosing any third \(a\). In a tree of order at least three, either some leaf \(b\) is attached to a degree-two vertex \(c\) (take \(a\) as the other neighbor of \(c\)), or two leaves \(b,c\) share their neighbor \(a\). To see this dichotomy, if every leaf has a neighbor of degree at least three, the number of leaves of a nontrivial tree exceeds the number of degree-at-least-three vertices, so two leaves share one neighbor. In either case every neighbor of \(b\) or \(c\) lies in \(\{a,b,c\}\), contradicting (A).

Consequently, every component other than a possible unique isolated vertex contains a cycle, and has at least as many edges as vertices. Thus \(|S|=|E(H)|\ge n-1\); without an isolate, the stronger bound \(|S|\ge n\) holds.

**Equality and construction.** If \(|S|=n-1\), there is exactly one isolated vertex, and every other component must be unicyclic. In fact all remaining vertices have degree at least two: if \(b\) were a leaf with sole neighbor \(a\) and \(c\) the isolated vertex, criterion (A) would fail for \(a,b,c\). Since the nontrivial components have as many edges as vertices, minimum degree two forces every vertex therein to have degree exactly two. Hence they are cycles.

A three-cycle is forbidden by (A), taking \(a,b,c\) to be its three vertices. A four-cycle is forbidden by (B), taking its entire vertex set as \(X\), for no selected edge exits this component. All remaining cycles therefore have lengths at least five.

Conversely, suppose \(H\) consists of one isolate and disjoint cycles of lengths at least five. In any triple \(a,b,c\), if (A) failed, the two cyclic vertices among \(b,c\), when present, would each have both neighbors inside the triple, which is impossible in cycles of length at least five; if one is the isolate, the other cyclic vertex would need two neighbors among the other two triple labels, of which the isolate is not a neighbor. Thus (A) holds. If (B) failed, the four-label subset \(X\) would be a union of whole connected components, impossible because the only component with fewer than five vertices is the unique singleton. Hence (B) holds. A single \((n-1)\)-cycle with one isolate exists for every \(n\ge6\), proving attainability and completeness.

**Enumeration.** A labelled undirected simple cycle on \(\ell\ge5\) fixed labels has \((\ell-1)!/2\) possibilities. The labelled exponential formula counts disjoint unions of these cycles by \(m!\,[z^m]\exp(\sum_{\ell\ge5}z^\ell/(2\ell))\). Selecting the isolated label gives the stated formula. To count the first disconnected cycle type, on ten nonisolated labels the number of unordered pairs of five-cycles is \(\binom{10}{5}(12)^2/2=18144\); multiplying by eleven possible isolates gives \(199584\). A ten-cycle on ten labels gives \(11\cdot9!/2=1995840\). No two cycles of length at least five fit on fewer than ten nonisolated vertices.

## Verification
The accompanying `verify.cpp` reconstructs distances in \(J(n,2)\), forms all third-party witness masks, and exhaustively enumerates every ground-edge subset up to the claimed minimum cardinality for \(n=6,7,8\), with smaller boundary cases \(n=4,5\). It separately tests the ground graph criteria (A),(B) against the direct witness definition on randomized edge subsets, without assuming the theorem. The `count.py` script computes independent integer recurrence coefficients through dimension sixteen, including the first two-cycle case. Commands: `g++ -std=c++17 -O3 verify.cpp -o verify && ./verify`; `python3 count.py`. These are finite checks and do not substitute for the general proof above.

## Relationship to prior work
The total resolving requirement is the third-party metric-resolvability notion treated by Javaid, Iftikhar and Salman (2012) under strong total resolvability and by Hedetniemi, Laskar and Mulder (2020) under total metric dimension. The latter establishes values for paths, cycles, grids, the three-cube, and the Petersen graph, but no value or structure theorem for triangular graphs. Existing Johnson-graph results on ordinary resolving numbers and earlier structural classifications of forts or total dominating sets use distinct predicates and do not imply this criterion. The precise distinction matters: a landmark is not permitted to distinguish a pair by being one of its endpoints.

## Limitations
The classification is for the triangular family \(J(n,2)\) with \(n\ge6\); it does not treat general \(J(n,k)\), the small parameter values, or all inclusion-minimal (nonminimum) total resolving sets. Computational experiments were exhaustive only for the stated finite sizes. The proof is self-contained but not independently validated, and an unindexed publication could contain an equivalent classification.

## References
1. S. T. Hedetniemi, R. C. Laskar, H. M. Mulder, *New resolvability parameters of graphs*, AKCE International Journal of Graphs and Combinatorics **17** (2020), 1028–1038, published online 2020-05-04, https://doi.org/10.1016/j.akcej.2019.12.021. Full text: https://repub.eur.nl/pub/126872/Repub_126872_O-A.pdf.
2. I. Javaid, F. Iftikhar, M. Salman, *Total Resolvability in Graphs*, Middle-East Journal of Scientific Research **11** (2012), 1649–1658, https://doi.org/10.5829/IDOSI.MEJSR.2012.11.12.1750.
3. K. Casel, A. Estrada-Moreno, H. Fernau, J. A. Rodríguez-Velázquez, *Weak Total Resolvability in Graphs*, Discussiones Mathematicae Graph Theory **36** (2016), 185–210, https://doi.org/10.7151/dmgt.1853.
