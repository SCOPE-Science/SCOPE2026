# Exact distance-two shattering of finite-tree one-point types

## Finding
Let \(T=(V,E)\) be any finite simple tree and define the first-order formula
\[
\varphi(x;y):=x\ne y\ \land\ \exists z\,(E(x,z)\land E(z,y)).
\]
For \(v\in V\), its parameter trace on \(A\subseteq V\) is \(S_2(v)\cap A\), where \(S_2(v)=\{a\in V:d_T(v,a)=2\}\). A set \(A\) is shattered if all \(2^{|A|}\) traces appear.

For a vertex \(u\), call a neighbor \(a\in N_T(u)\) **outward-deep** when there are distinct vertices \(z,w\) forming a path \(u-a-z-w\). Write \(e_T(u)\) for the number of outward-deep neighbors of \(u\). The number of shattered three-element parameter sets is exactly
\[
\boxed{H_3(T)=\sum_{u\in V:\,\deg_T(u)\ge4}\binom{e_T(u)}3.}
\]
More precisely, a triple \(A\) is shattered if and only if it consists of three outward-deep neighbors of one vertex \(u\) with \(\deg_T(u)\ge4\). Every tree has no shattered set of size four or greater, and the largest possible VC dimension of the formula \(\varphi\) on the class of finite trees is exactly three. The smallest tree with a shattered triple has exactly eleven vertices.

These are exact-radius-two spheres, not closed radius-two balls or ordinary radius-one neighborhoods.

## Assumptions and scope
Graphs are finite, undirected, simple, connected and acyclic. Vertices used as witnesses for traces may lie inside the parameter set. Distances count graph edges and the defining formula explicitly excludes \(x=y\). For a forest, the same no-four-shattering result holds componentwise; a shattered nonempty set must lie in one component because its full trace has a witness.

The empty sum and binomial coefficients with upper argument below three are interpreted as zero. A vertex is outward-deep relative to \(u\) precisely if its component in \(T-u\) contains a path of two more edges beginning at that neighbor. No restrictions on maximum degree or tree order are imposed.

## Proof
**Unique-midpoint lemma.** If two tree vertices \(a,b\) have distance four, their only common distance-two center is the unique midpoint of the path from \(a\) to \(b\). Indeed any \(v\) with \(d(v,a)=d(v,b)=2\) lies on a length-four walk joining them; uniqueness of tree paths forces that walk to be the geodesic.

**Center of a shattered set.** Let \(A\) be shattered with \(|A|\ge3\), and choose \(v\) realizing the full trace \(A\). All elements of \(A\) have distance two from \(v\), so any two are at distance two or four. If some \(a,b\in A\) had distance four, the unique-midpoint lemma would force any witness of the trace \(\{a,b\}\) to equal \(v\), which also sees a third element, a contradiction. Hence all distinct pairs of elements of \(A\) are at distance two. In a tree, any three pairwise distance-two vertices have one common neighbor: if the two common neighbors along paths from \(a\) to \(b\) and from \(b\) to \(c\) differed, the path from \(a\) to \(c\) would have length four. The center extends uniquely to all of \(A\). Denote it by \(u\). Thus \(A\subseteq N_T(u)\).

**All possible traces on common neighbors.** Fix \(A\subseteq N_T(u)\) with \(|A|\ge3\). If \(x\in N_T(u)\setminus A\), then \(S_2(x)\cap A=A\). If \(x\in A\), then \(S_2(x)\cap A=A\setminus\{x\}\). If \(x=u\), its trace is empty. Any vertex \(x\notin N_T(u)\cup\{u\}\) has at most one element of \(A\) at distance two: the paths from different neighbors of \(u\) to \(x\) pass through \(u\), and only the branch containing \(x\) can yield distance two. In fact \(S_2(x)\cap A=\{a\}\) exactly when \(x\) is two edges farther from \(a\) within the component of \(T-u\) containing \(a\).

**Characterization and cutoff.** For a triple \(A\subseteq N_T(u)\), the three two-element traces are witnessed by the marked vertices themselves and the empty trace by \(u\). The full trace exists precisely when \(u\) has an additional neighbor, that is, \(\deg_T(u)\ge4\). Each singleton \(\{a\}\) occurs precisely when \(a\) is outward-deep. These conditions are therefore necessary and sufficient. For \(|A|\ge4\), every available trace is empty, a singleton, all of \(A\), or \(A\) minus at most one element; in particular a two-element trace is impossible. No four points are shattered. Since shattered sets are downward closed, no larger set is shattered either.

**Enumeration.** Any shattered triple has a unique common neighbor \(u\). At a fixed \(u\) with at least four neighbors, every three-element subset of its \(e_T(u)\) outward-deep neighbors is shattered, and no other triple centered at \(u\) is shattered. Summation proves the displayed formula without overcounting.

**Eleven-vertex minimum and witness.** Three marked neighbors, their center \(u\), and an additional neighbor of \(u\) are five distinct vertices. For each of the three marked neighbors \(a\), an outward length-two path \(a-z_a-w_a\) requires two more vertices; the six vertices are pairwise distinct and lie in separate components of \(T-u\). Thus every tree with a shattered triple has at least \(5+6=11\) vertices. Equality is realized by the edge set
\[
\{\{0,1\},\{0,2\},\{0,3\},\{0,4\},\{1,5\},\{5,6\},\{2,7\},\{7,8\},\{3,9\},\{9,10\}\},
\]
where each pair denotes one undirected edge. Here \(A=\{1,2,3\}\), \(u=0\), the vertex \(4\) witnesses \(A\), the marked vertices witness the complementary pairs, vertices \(6,8,10\) witness the three singletons, and \(0\) witnesses the empty trace. This achieves VC dimension three and the minimum size.

## Verification
Run `python3 verify.py` with Python 3's standard library. It independently constructs the distance-two traces from adjacency lists and checks the shattering formula on all labelled trees with up to seven vertices (via Prüfer sequences), together with seeded randomized trees up to thirty-five vertices. It also checks the explicit eleven-vertex construction. The observed result is `VERIFY_OK 18889 trees; eleven-vertex witness and exact triple formula`. This finite verification corroborates the structural proof; it is not an infinite exhaustive enumeration or an independent audit.

## Relationship to prior work
Dreier, Mählmann and Toruńczyk (2026), Theorem 1.2, prove general polynomial bounds for first-order types over parameter sets on monadically dependent graph classes, with neighborhood/VC arguments in the introduction. That theorem does not specify the exact-shape shattering triples of the distance-two formula on trees or the sharp eleven-vertex witness threshold. Benediktsson, Macpherson and Adler (2022) determine the VC dimension of the *edge* formula on Hamming and Johnson graphs, rather than the distance-two formula on trees. Bousquet and Thomassé (2015) study closed balls of varying radius and distance VC dimension, distinct from fixed exact-radius-two spheres; the latter distinction is essential. These comparisons do not establish an exhaustive historical novelty claim.

## Limitations
The result does not classify all shattered pairs or give a complete VC-density polynomial in parameter-set size. The formula is for exact graph distance two in trees, not arbitrary graph classes, and does not extend automatically to distance-at-most-two balls, induced subgraphs of tree squares, or larger radii. An independently located earlier equivalent theorem may affect priority. Neither external proof certification nor independent historical-priority audit is asserted.

## References
- J. Dreier, N. Mählmann and S. Toruńczyk, *First-Order Model Checking on Monadically Dependent Graph Classes*, arXiv:2611.08143v1, first public 2026-11-05. https://arxiv.org/abs/2611.08143
- I. Adler, B. G. Benediktsson and D. Macpherson, *Vapnik–Chervonenkis dimension and density on Johnson and Hamming graphs*, Discrete Applied Mathematics 312 (2022), 29–44. https://doi.org/10.1016/j.dam.2021.09.017
- N. Bousquet and S. Thomassé, *VC-dimension and Erdős–Pósa property*, Discrete Mathematics 338 (2015), 2302–2317. https://doi.org/10.1016/j.disc.2015.05.026
