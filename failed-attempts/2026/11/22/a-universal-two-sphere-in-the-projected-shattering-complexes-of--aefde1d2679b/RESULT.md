# A universal two-sphere in the projected shattering complexes of double-star colourings

## Finding

For every two integers \(a,b\ge1\), the vertex-projected VC-shattering complex of proper three-colourings of the double-star tree \(D_{a,b}\) has exactly four facets, an explicit face polynomial, and a homotopy type independent of \(a,b\):
\[
|\mathcal P(D_{a,b})|\simeq S^2.
\]
The projected complex is pure only for \(a=b=1\), although its homology remains that of a single two-sphere at every order. Its facet dimensions can differ by an arbitrarily large amount. These statements concern the complex of **vertex supports admitting at least one fixed colour target assignment**, not the larger full Boolean-query complex.

More precisely, with \(u,v\) the hubs and nonempty disjoint leaf sets \(A,B\), the facets are
\[
A\cup B\cup\{u\},\quad A\cup B\cup\{v\},\quad A\cup\{u,v\},\quad B\cup\{u,v\}.
\]
The face enumerator, counting each vertex support once (including the empty support), is
\[
F_{a,b}(z)=(1+2z)(1+z)^{a+b}+z^2\big((1+z)^a+(1+z)^b-1\big).
\]
Consequently the ordinary VC dimension on vertex-colour queries is \(a+b+1\), because every shattered query support has at most one query per vertex and a largest projected support has that cardinality.

## Assumptions and scope

The underlying graph \(D_{a,b}\) has vertex set \(A\sqcup B\sqcup\{u,v\}\) and edges \(uv\), \(u x\) for \(x\in A\), and \(v y\) for \(y\in B\). Here \(a=|A|\ge1\) and \(b=|B|\ge1\). Proper colourings are maps \(f:V(D_{a,b})\to\{1,2,3\}\) such that adjacent vertices receive different colours; the three colours are named and need not all occur.

For a vertex \(x\) and colour \(c\), the Boolean query is \(h_f(x,c)={\bf1}[f(x)=c]\). A finite query support \(Q\subseteq V(D_{a,b})\times\{1,2,3\}\) is *shattered* if for each labelling \(\epsilon:Q\to\{0,1\}\), some proper \(f\) realizes all those answers. No shattered query support contains two different queries at the same vertex: the all-positive labelling of both is impossible.

The **vertex-projected shattering complex** \(\mathcal P(D_{a,b})\) consists of those vertex sets \(S\subseteq V(D_{a,b})\) for which *there exists one target-colour function* \(c:S\to\{1,2,3\}\) such that the query set \(\{(x,c(x)):x\in S\}\) is shattered. Target colours are fixed once for all binary answer patterns. Downward closure is immediate. This projection is essential; the face polynomial does not count different target-colour choices separately.

## Proof

**1. The universal four-path obstruction.** Suppose four consecutive path vertices are queried with respective fixed targets \(c_1,c_2,c_3,c_4\). The all-positive answer forces consecutive target colours to differ. If the targets on any consecutive triple are three different colours, the answer \((1,0,1)\) on that triple is impossible: the middle vertex, adjacent to two differently coloured fixed endpoints, must take its own forbidden target. Therefore the four targets must alternate \((p,q,p,q)\), with \(p\ne q\). But the answer \((1,0,0,1)\) forces both middle vertices to take the third colour, contradicting their adjacency. Thus no shattered vertex set contains all four vertices of any path of length three.

In a double star, every four-vertex path is of the form \(x-u-v-y\), with \(x\in A\) and \(y\in B\). Hence the necessary condition is precisely that \(S\) does not simultaneously contain \(u,v\), a vertex of \(A\), and a vertex of \(B\).

**2. Sufficiency via fixed target assignments.** Let \(S\) satisfy this condition. In every case, unqueried leaves can be coloured arbitrarily differently from their adjacent hub. A leaf with target colour \(1\), whose hub has colour \(2\) or \(3\), can always realize either answer: choose colour \(1\) for a positive answer and the other non-hub colour for a negative answer. Thus the leaf labels are independent after choosing hub colours in \(\{2,3\}\).

If neither hub is queried, assign target colour \(1\) to all queried leaves and fix hub colours \((f(u),f(v))=(2,3)\) for every answer pattern. If exactly \(u\) is queried, assign all queried leaves target \(1\) and give \(u\) target \(2\). On a positive hub answer use \((f(u),f(v))=(2,3)\); on a negative hub answer use \((3,2)\). The case of only \(v\) queried is symmetric.

If both hubs are queried, the necessary condition says all queried leaves lie on one side. After interchanging hubs if needed, take that side to be \(A\); give all queried leaves target \(1\), hub \(u\) target \(2\), and hub \(v\) target \(1\). For hub-answer pairs \((1,1),(1,0),(0,1),(0,0)\), respectively use
\[
(f(u),f(v))=(2,1),(2,3),(3,1),(3,2).
\]
Every pair is proper, the leaf-bearing hub is always non-\(1\), and both labels of every queried leaf remain possible independently. The same construction covers the case when no leaves are queried. Thus every vertex set avoiding a four-vertex path has a single target choice that realizes every Boolean pattern. Combining with step 1 proves the exact characterization.

**3. Facets and polynomial.** A subset belongs to the projected complex exactly when it omits at least one hub or has its selected leaves entirely on one side. This is the union of the four simplices on
\[
F_1=A\cup B\cup\{u\},\quad F_2=A\cup B\cup\{v\},\quad
F_3=A\cup\{u,v\},\quad F_4=B\cup\{u,v\}.
\]
These are pairwise incomparable because \(A,B\ne\varnothing\), hence are exactly the facets. Supports containing neither hub contribute \((1+z)^{a+b}\). Supports containing exactly one hub contribute \(2z(1+z)^{a+b}\). Supports containing both hubs select an arbitrary subset from \(A\) or from \(B\), with the empty leaf selection counted only once; they contribute \(z^2((1+z)^a+(1+z)^b-1)\). This proves the polynomial. The two largest facets have \(a+b+1\) vertices; thus the VC dimension is \(a+b+1\). The other facets have \(a+2\) and \(b+2\) vertices, so all four have equal cardinality exactly when \(a=b=1\).

**4. Integral homotopy type.** Cover the geometric realization by its four facet simplices \(\Delta^{F_1},\ldots,\Delta^{F_4}\). Every nonempty intersection is itself a simplex and therefore contractible. The intersection of any one, two or three *distinct* facets is nonempty: in particular, the four triple intersections are \(A,B,\{u\},\{v\}\) in the ordering \((123),(124),(134),(234)\), respectively. But the intersection of all four facets is empty because \(F_1\cap F_2=A\cup B\), whereas \(F_3\cap F_4=\{u,v\}\). The nerve is exactly the boundary of a tetrahedron. The simplicial nerve lemma yields \(|\mathcal P(D_{a,b})|\simeq|\partial\Delta^3|\simeq S^2\). In particular its only nonzero reduced integral homology is \(\widetilde H_2\cong\mathbb Z\). The facet size gap between \(F_1\) and \(F_3\) is \(b-1\), arbitrarily large as \(b\to\infty\).

## Verification

The standalone `verify_double_star.py` independently enumerates all proper three-colourings, all vertex subsets, every possible fixed target assignment, and all Boolean traces. It compares the resulting projected supports with the forbidden-four-path criterion and the coefficient formula for \((a,b)=(1,1),(1,2),(2,2),(2,3),(3,3)\). The standalone `check_facets.py` checks the four facets, all nonempty intersections and complete face membership for 25 parameter pairs with \(1\le a,b\le5\). Recorded standard outputs are included. These finite tests are not relied on to establish universal quantifiers: the preceding arguments provide all-order proofs.

## Relationship to prior work

The 2017 preprint *Structure Learning of H-colorings* studies statistical identification of an unknown underlying graph from random colourings, not shattering of a fixed known graph's vertex-colour queries. The 2022 paper *Tree Dimension and the Sauer–Shelah Dichotomy* develops general static/adaptive dimension bounds without determining this projected complex. An existing mathematical note, *The first branching obstruction to three-colouring shattering on trees*, proves the universal four-vertex-path obstruction and a seven-vertex exceptional spider, and exhaustively classifies trees **up to order seven**; the necessity argument is acknowledged as prior. Another note gives all-parameter colour-query dimensions for **paths**, not double stars. The 2021 article *Chordal graphs, higher independence and vertex decomposable complexes* studies supports whose induced components have at most a fixed number of vertices; this is not the same as avoiding induced four-vertex paths, since a queried double-star may contain an arbitrarily large induced star. The new contribution assessed here is the unrestricted double-star converse, precise facet/face formula and uniform two-sphere homotopy despite unbounded nonpurity, not the generic definition of shattering or nerve lemma.

## Limitations

This theorem is restricted to diameter-three double-star trees with both leaf sets nonempty, and exactly three **named** colours. It does not claim a criterion for arbitrary trees or for full query supports in \(V\times\{1,2,3\}\), nor any adaptive-dimension formula. Similar induced-path avoidance complexes may admit alternative descriptions, and full historical publication priority is not independently established. Numerical experiments are restricted to the parameters stated above; all-order claims follow from the explicit proof.

## References

1. A. Blanca, Z. Chen, D. Štefankovič and E. Vigoda, *Structure Learning of H-colorings*, arXiv:1708.05118, first public version 2017-08-17, https://arxiv.org/abs/1708.05118.
2. R. Walker, *Tree Dimension and the Sauer–Shelah Dichotomy*, arXiv:2203.12211, 2022, https://arxiv.org/abs/2203.12211.
3. F. Abdelmalek et al., *Chordal graphs, higher independence and vertex decomposable complexes*, arXiv:2106.10863, 2021, https://arxiv.org/abs/2106.10863.
4. *The first branching obstruction to three-colouring shattering on trees*, public mathematical note, 2026, https://github.com/published-finding corpus/2026/blob/main/2026/10/26/SCOPE-the-first-branching-obstruction-to-three-colouring-shattering-on--6dd09fced05e/RESULT.md.
5. *A sharp three-colour palette threshold for VC and online shattering of path colourings*, public mathematical note, 2026, https://github.com/published-finding corpus/2026/blob/main/2026/10/26/SCOPE-a-sharp-three-colour-palette-threshold-for-vc-and-online-shatter--5ed55547f077/RESULT.md.
