# Sharp five-point failure of edge-insertion monotonicity in triangle-free Henson pair-type proportions

## Finding
Let \(H_3\) be the countable universal homogeneous triangle-free graph. Fix the vertices of a finite triangle-free graph \(G\) as *individually named* parameters. Give equal weight to each complete type of an ordered pair \((x,y)\) of distinct elements outside the parameter set. Denote by \(p(G)\) the resulting fraction with \(E(x,y)\). An *admissible edge insertion* adds a missing edge between two named parameters and keeps the named graph triangle-free.

**Theorem.** Every admissible insertion strictly increases \(p\) when the parameter set has at most four vertices. At five vertices, strict decreases first occur. There are exactly two isomorphism classes of marked insertions that decrease \(p\):

1. \(K_{1,3}\sqcup K_1\to K_{1,4}\), joining the centre of the three-leaf star to the isolated point;
2. \(P_3\sqcup K_2\to T\), joining the middle vertex of the three-vertex path to an endpoint of the isolated edge, where \(T\) is the tree with degree multiset \(\{3,2,1,1,1\}\).

Among the 1,410 labelled admissible insertions on five vertices, precisely 80 decrease the fraction: 20 of the first marked class and 60 of the second. In both classes the old named graph is disconnected and the new one connected. A *connected* named graph first admits a decreasing insertion on six vertices. Decreasing examples exist at every larger order by adding isolated named parameters.

In the two five-point classes the exact data are:

| Old and new named graphs | \(I(G),D(G)\) before | \(I(G+e),D(G+e)\) after | \(p(G)\) before | \(p(G+e)\) after |
| --- | --- | --- | --- | --- |
| star plus isolate to larger star | \((18,129)\) | \((17,113)\) | \(43/151\) | \(113/402\) |
| path plus edge to fork tree | \((15,119)\) | \((14,103)\) | \(119/344\) | \(103/299\) |

The respective strictly positive decreases are \(223/60702\) and \(149/102856\). Fractions refer to *types*, not random sampled vertices in the infinite graph.

## Assumptions and scope
The language is the ordinary undirected loopless graph language; every parameter is named pointwise. The variables \(x,y\) are ordered and required to be distinct from one another and from all named parameters. Graphs are simple and triangle-free before and after insertion, so both bases occur in \(H_3\). The theorem concerns uniform counting of complete first-order types over those finite bases. It is not a statement about empirical edge density in \(H_3\) or arbitrary graphs containing triangles.

For a finite graph \(G\), let \(\mathcal I(G)\) be its independent vertex subsets (including the empty set), and put
\[
 I(G)=|\mathcal I(G)|,\qquad
 D(G)=|\{(A,B)\in\mathcal I(G)^2:A\cap B=\varnothing\}|.
\]

## Proof
**1. Type-to-independent-set correspondence.** By the finite extension property and homogeneity of \(H_3\) (Henson, Theorem 2.3), the possible named-neighbour sets of a new point are precisely the independent sets of \(G\), and each is one complete nonalgebraic one-type. When \(x,y\) are not adjacent, any two such named-neighbour sets are simultaneously realizable, giving \(I(G)^2\) distinct complete pair types. When \(x,y\) are adjacent, their two named-neighbour sets must also be disjoint; otherwise a named vertex would complete a forbidden triangle. Conversely disjoint independent sets produce a triangle-free finite extension, so they give exactly \(D(G)\) adjacent pair types. Thus
\[
 \boxed{p(G)=\frac{D(G)}{I(G)^2+D(G)}.}
\]
For two admissible bases \(G,G+e\), strict decrease of this fraction is therefore **equivalent** to the integer inequality
\[
 \boxed{D(G+e)I(G)^2<D(G)I(G+e)^2.}
\]
This integer test avoids floating-point comparison.

**2. Exact, complete classification through five vertices.** Label vertices \(0,\ldots,n-1\), list the \(\binom n2\) possible edges in lexicographic order, and loop over all \(2^{\binom n2}\) graph bit masks. For each triangle-free mask and every missing edge, retain the augmentation only when it is also triangle-free. Compute \(I\) by testing all \(2^n\) vertex subsets for independence. To compute \(D\), sum for each independent set \(A\) the number of independent subsets of \(V(G)\setminus A\). The accompanying complete standard-library program uses the subset-zeta recurrence for the latter counts, evaluates the boxed exact inequality, and canonicalizes each decreasing marked graph \((G,e)\) over all \(n!\) vertex permutations. This is a *finite exhaustive enumeration*, with no sampling or numerical tolerance.

The complete results for \(n=1,2,3,4,5\), in the form (decreasing, equal, increasing) admissible labelled augmentations, are respectively
\[
 (0,0,0),\ (0,0,1),\ (0,0,9),\ (0,0,96),\ (80,0,1330).
\]
At \(n=5\), all 80 negative cases belong to two and only two canonical marked orbits, with multiplicities 20 and 60. The representatives with old edge sets and inserted edge are
\[
 \begin{aligned}
 &\{01,02,03\},\quad 04;\\
 &\{03,04,12\},\quad 01.
 \end{aligned}
\]
Here a two-digit symbol denotes an unordered edge between the labelled vertices. Their counted \((I,D)\) values and exact rational differences are those in the Finding table. Every one of those 80 old graphs is disconnected. The finite loop exhausts all possible admissible augmentations through five vertices, proving the minimality and uniqueness assertions without an inductive assumption on graph shape. The verification script independently re-counts both nonadjacent and adjacent extensions by directly testing every full finite triangle-free adjacency diagram for the two displayed witnesses.

**3. Connected sharpness at six vertices.** On vertices \(0,\ldots,5\), take the connected tree with edges
\[
 \{02,04,05,12,13\},
\]
and insert the missing edge \(03\). Both old and new graphs are triangle-free, and the exact independent-set and disjoint-pair counts are
\[
 (I,D)=(23,249)\quad\longrightarrow\quad(22,225).
\]
Direct extension-diagram enumeration agrees. Therefore
\[
 p(G)=\frac{249}{778}>\frac{225}{709}=p(G+03),
\]
with difference \(1491/551602\). No connected counterexample occurs with at most five vertices by Step 2, so six is the sharp connected threshold.

**4. Persistence at arbitrary order.** Adding one isolated named point multiplies the independent-set count by two and the disjoint-independent-pair count by three:
\[
 I(G\sqcup K_1)=2I(G),\qquad D(G\sqcup K_1)=3D(G).
\]
Hence the odds ratio \(D/I^2\) is multiplied by \(3/4\) on both sides of an insertion, preserving the strict ordering. Repeating gives a counterexample on every number of named vertices at least five. This concludes the proof.

## Verification
Run `python3 verification/verify.py` using only the Python standard library. Its `counts` routine enumerates every independent vertex subset and applies exact subset-zeta sums. Its `is_triangle_free` function checks all vertex triples. Its `canon` function minimizes the marked adjacency encoding over all relabellings. The calculation exhausts all labelled admissible augmentations through five vertices, verifying the exact sign table and two marked orbit multiplicities. For each of the two five-point witnesses and the connected six-point witness, `direct_diagrams` separately enumerates all labelled two-new-vertex adjacency patterns and checks forbidden triangles directly. The captured output is in `verification/output.txt`. These finite exhaustive calculations establish the bounded threshold; the all-order persistence follows from the explicit multiplicative identities in the proof.

## Relationship to prior work
Henson's original 1971 paper proves homogeneity and the forbidden-clique extension property. Conant's 2014 preprint gives the relevant graph-type realization framework and proves model-theoretic forking/dividing results, not the present edge-insertion classification. Both are used for the type correspondence, which is not claimed new. A published result on two-types over *maximal multipartite* parameter graphs in \(K_{r+1}\)-free Henson structures explicitly takes \(r\ge4\) and develops a different multipartite collision asymptotic; it neither covers arbitrary triangle-free bases of \(H_3\) nor compares one-edge augmentations. Existing independence-polynomial research studies absolute independent-set counts, whereas this theorem concerns the normalized two-type ratio involving disjoint pairs. A published five-site edge-insertion anomaly for *irreversible random greedy adsorption* uses different graphs and a distinct dynamical expectation; it does not imply this uniform type-counting statement. Searches of related published records did not reveal a covering five-point monotonicity threshold or its two marked classes. Independent priority checking is not claimed.

## Limitations
The exhaustive *classification* is only through five named vertices; the six-vertex result gives a connected witness, not a census of all six-vertex failures. The all-size extension uses isolated parameters, so it does not give connected witnesses at every larger order. Fractions are uniform over complete types, not spatial or probabilistic frequencies of generic graph vertices. Historical novelty has a residual risk from specialized independent-set partition-function literature, and independent mathematical audit has not been performed.

## References
- C. Ward Henson, *A family of countable homogeneous graphs*, *Pacific Journal of Mathematics* 38 (1971), 69–83, Section 2, Theorem 2.3. https://msp.org/pjm/1971/38-1/pjm-v38-n1-p09-p.pdf
- Gabriel Conant, *Forking and dividing in Henson graphs*, arXiv:1401.1570v1 (first posted 2014-01-08), Section 3. https://arxiv.org/html/1401.1570v1
- *A collision law for two-types over maximal multipartite parameter graphs in Henson structures*, published 2026-10-26. https://github.com/published-finding corpus/2026/blob/main/2026/10/26/SCOPE-a-collision-law-for-two-types-over-maximal-multipartite-paramete--8c8e5c9b100b/RESULT.md
- *Sharp five-site onset and a common kinetic crossover for hard-core monomer adsorption*, published 2026-11-08. https://github.com/published-finding corpus/2026/blob/main/2026/11/8/SCOPE-sharp-five-site-onset-and-a-common-kinetic-crossover-for-hard-co--09aa39c3a62a/RESULT.md
- Yufei Zhao, *The number of independent sets in a regular graph*, arXiv:0909.3354 (2009). https://arxiv.org/abs/0909.3354
