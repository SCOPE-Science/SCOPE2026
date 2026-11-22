# A sharp five-to-three-culture transition in frozen Axelrod states on bicliques

## Finding

Consider the finite Axelrod model with two features, each taking three values, on the labelled complete bipartite graph \(K_{a,b}\), where \(a,b\geq 1\). Let \(Z_{a,b}\) count its absorbing (frozen) configurations. Then, for every pair of positive integers \(a,b\),

\[
\boxed{Z_{a,b}=9(5^a+5^b)+18\cdot 2^{a+b}+6\cdot3^{a+b}-36(2^a+2^b)-18(3^a+3^b)+81.}
\]

There are precisely 42 inclusion-maximal oriented compatible pairs of culture palettes, of size types \((1,5),(5,1),(2,2),(3,3)\), with respective multiplicities \(9,9,18,6\). An explicit four-family decomposition of frozen states gives the formula.

There is also a sharp structural limit law. Suppose \(a\leq b\), both \(a,b\) tend to infinity, and \(a/b\to\alpha\in(0,1]\). Put \(\theta=\log_3(5/3)\). A uniformly chosen absorbing configuration uses exactly five distinct cultures with probability tending to one if \(\alpha<\theta\); it uses exactly three distinct cultures with probability tending to one if \(\alpha>\theta\). In the critical window \(a-\theta b\to t\in\mathbb R\), the number of distinct cultures converges in distribution to a variable supported on \(\{3,5\}\), with

\[
\Pr(5)=\frac{9}{9+6\cdot3^t},\qquad
\Pr(3)=\frac{6\cdot3^t}{9+6\cdot3^t}.
\]

**The probability law throughout this finding is uniform over the set of absorbing configurations, not the distribution induced by running the Axelrod dynamics from a random initial state.**

## Assumptions and scope

A *culture* is an ordered pair \(c=(i,j)\in C=[3]\times[3]\). A configuration assigns one culture to each labelled vertex of \(K_{a,b}\). In the standard two-feature Axelrod dynamics, an edge is inactive precisely when its endpoint cultures are equal or disagree in both coordinates [1, Section 2]. Thus a configuration is absorbing exactly when each cross-shore pair \(c,d\) satisfies

\[
R(c,d)\quad\Longleftrightarrow\quad
(c=d)\ \text{or}\ (c_1\ne d_1\ \text{and}\ c_2\ne d_2).
\]

Both shores are nonempty. No restriction is placed on distinct cultures within either shore. A *compatible palette pair* is a pair of nonempty sets \((S,T)\) of cultures for which every cross-pair lies in \(R\). It is maximal when neither palette can be enlarged. The source-graph vertices and all nine cultures are named, and the formula counts assignments, not equivalence classes under graph or culture automorphisms.

## Proof

**1. Common-neighbour geometry.** For a culture \(c\) define \(N(c)=\{d\in C:R(c,d)\}\). A direct coordinate check gives \(|N(c)|=5\) (the culture itself and the four cultures different in both coordinates). For two *distinct* cultures \(c,d\), there are exactly two cases:

- If they share one coordinate, \(N(c)\cap N(d)\) has two members, which share the other coordinate. Their common-neighbour palette is exactly \(\{c,d\}\).
- If they differ in both coordinates, \(N(c)\cap N(d)\) is the unique three-culture permutation triple \(Q\) containing both, where a permutation triple has the form \(\{(i,\pi(i)):i\in[3]\}\) for a permutation \(\pi\) of \([3]\). Every pair in \(Q\) is compatible and its common-neighbour palette is all of \(Q\).

These statements follow by considering the remaining third value in each coordinate. There are six permutation triples and eighteen unordered pairs of distinct cultures sharing one coordinate: nine within common first-coordinate rows and nine within common second-coordinate columns.

**2. Exhaustiveness of the palette decomposition.** Let \(S,T\) be the cultures actually used on the two shores. If one shore is monochromatic, the state belongs to the family \(M\) or \(N\) defined below. Otherwise both palettes contain distinct pairs. Pick two distinct cultures in \(S\). If they differ in both coordinates, \(T\) lies in their unique permutation triple \(Q\); since \(T\) has at least two distinct members, the common-neighbour rule forces \(S\subseteq Q\) as well. Hence the state belongs to family \(T_0\) below. If no pair of distinct cultures in \(S\) differs in both coordinates, the chosen two share one coordinate, and their common-neighbour palette has size two. As the opposite shore uses at least two cultures, it uses exactly those two. Applying the two-member common-neighbour rule in reverse forces \(S\) to be exactly its original pair. This is family \(R_0\). The two-pair family \(R_0\) cannot overlap the permutation-triple family \(T_0\), because a permutation triple has distinct values in each coordinate.

The cases prove that every frozen state is contained in one of the four families. They also classify the 42 *maximal* compatible palette pairs: the nine singleton-to-five pairs and their nine reversals; the eighteen coordinate-sharing-two-to-complementary-two pairs; and the six permutation-three-to-permutation-three pairs. None of these maximal pairs properly contains another.

**3. Count the four families without double counting.** Let \(M\) mean that the first shore is monochromatic and \(N\) that the second shore is monochromatic. Choosing its one culture and then assigning independently a compatible culture to every vertex on the opposite shore gives

\[
|M|=9\cdot5^b,\quad |N|=9\cdot5^a,\quad |M\cap N|=45.
\]

Let \(T_0\) be the set of configurations whose entire image lies in one permutation triple. Each of the six triples allows \(3^{a+b}\) assignments. Two distinct triples intersect in at most one culture, and each of the nine cultures belongs to exactly two triples. Therefore

\[
|T_0|=6\cdot3^{a+b}-9.
\]

For the overlaps, choosing a monochromatic first-shore culture within a triple and assigning arbitrary cultures from that triple to the second shore gives, after correcting for the nine constant duplicate assignments,

\[
|M\cap T_0|=18\cdot3^b-9,\quad
|N\cap T_0|=18\cdot3^a-9,\quad
|M\cap N\cap T_0|=45.
\]

The last identity holds since every compatible pair of single cultures is contained in at least one permutation triple: a repeated culture lies in two, and two cultures differing in both coordinates determine one. Inclusion-exclusion now yields

\[
|M\cup N\cup T_0|
=9(5^a+5^b)+6\cdot3^{a+b}-18(3^a+3^b)+9.
\]

Finally, let \(R_0\) be the states using *both* cultures from one of the eighteen coordinate-sharing pairs on the first shore, and both cultures from its uniquely complementary pair on the second shore. Each pair-choice contributes \((2^a-2)(2^b-2)\) onto assignments. Different choices are disjoint, and \(R_0\) is disjoint from \(M\cup N\cup T_0\). Hence

\[
|R_0|=18(2^a-2)(2^b-2).
\]

Adding the two disjoint totals and expanding proves the boxed all-order formula. At the boundary \(a=1\) or \(b=1\), the corresponding onto factor vanishes and the formula reduces to the known tree count \(9\cdot5^{a+b-1}\) from [1, Proposition 5.7]. For example \(Z_{1,3}=1125\) and \(Z_{2,2}=693\), matching [1, Table 1].

**4. Asymptotic dominance and culture counts.** In the regime \(a\le b\to\infty\), \(a\to\infty\), the principal components are \(9\cdot5^b\) from \(M\) and \(6\cdot3^{a+b}\) from \(T_0\). The other terms in the exact expression are negligible relative to their sum: \(5^a=o(5^b)\) whenever \(a/b\le\theta+o(1)\), and even at \(a=b\), \(5^a=o(3^{a+b})\) because \(5<9\); similarly \(2^{a+b}\), \(3^a\), \(3^b\), \(2^a\) and \(2^b\) are negligible relative to the dominant term. More explicitly, if \(a/b\to\alpha<\theta\), then \(3^{a+b}/5^b=3^{a-\theta b}\to0\). If \(\alpha>\theta\), the ratio tends to infinity. If \(a-\theta b\to t\), the ratio tends to \(3^t\).

Conditional on \(M\), all five cultures of the chosen first-shore culture's compatible five-set occur on the opposite shore with probability at least \(1-5(4/5)^b\), under the uniform count. Conditional on a fixed permutation triple, all three cultures occur on both shores with probability at least \(1-3(2/3)^a-3(2/3)^b\). The intersections of these dominant families are lower order by the formulas above, and the complementary family \(R_0\) is lower order. These statements establish both pure phases and the exact limiting mixture in the critical window.

## Verification

The standalone standard-library verifier `verify.py` independently constructs the nine-culture compatibility matrix, enumerates all 511 nonempty culture supports, checks the 42 maximal compatible bipalettes, compares the surjection-expansion identity to the closed formula for 576 pairs with \(1\le a,b\le24\), directly counts all assignments for eight small labelled bicliques (including the six-vertex balanced case), and checks the four-family decomposition in five small cases. It prints `VERIFY_OK` on success. All-order correctness rests on the explicit common-neighbour and inclusion-exclusion proof above, not on finite experiments.

## Relationship to prior work

Boudourides [1] proves the general absorbing-state criterion for arbitrary graphs, the connected-partition/chromatic-polynomial identity, and the graph-homomorphism formulation with loops (Proposition 5.7). These general tools are prior work and are **not** claimed as new. The same paper tabulates some small graphs and evaluates trees and cycles but does not give the nine-culture biclique maximal-palette classification, the explicit two-parameter closed form, or the aspect-ratio phase law. The present result evaluates a natural first genuinely nonbinary case of the existing framework.

Galvin and Tetali [2] study general and weighted homomorphisms of bipartite source graphs into targets possibly containing loops, including asymptotic extremal bounds. Their general results do not state this exact nine-culture, unbalanced biclique count or its three-versus-five-culture limit law. Sason [3] derives exact and bounded homomorphism formulas for complete bipartite *sources* and bipartite *targets*. The target here is a looped nine-vertex graph with nontrivial triangles and is not bipartite, so its target-bipartite formulas do not directly cover this instance.

## Limitations

The theorem fixes \(F=2\) and \(q=3\), and applies to positive shore sizes. It counts labelled configurations, not orbits; no assertion is made for other trait counts, other feature numbers, or arbitrary host graphs. The transition describes a **uniformly sampled frozen state**, not the absorbing-state distribution reached by the stochastic Axelrod process; the latter depends on the initial distribution and transition dynamics. The historical-priority comparison is based on identified, accessible literature and indexed mathematical records, and cannot rule out older unindexed equivalent calculations. No independent mathematical audit has been performed.

## References

[1] Moses Boudourides, *Triadic and assortative structure of absorbing states in the Axelrod model*, arXiv:2611.18719v1, first posted 2026-11-08. https://arxiv.org/abs/2611.18719v1

[2] David Galvin and Prasad Tetali, *On weighted graph homomorphisms*, DIMACS Series in Discrete Mathematics and Theoretical Computer Science **64** (2004); preprint arXiv:1206.3160. https://arxiv.org/abs/1206.3160

[3] Igal Sason, *Counting Graph Homomorphisms in Bipartite Settings*, arXiv:2508.06977, first posted 2025-08-09. https://arxiv.org/abs/2508.06977
