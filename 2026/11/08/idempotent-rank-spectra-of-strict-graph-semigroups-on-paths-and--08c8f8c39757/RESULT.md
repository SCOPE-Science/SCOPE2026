# Graph-power structure of strict idempotents on paths and cycles

## Finding

For a finite simple graph \(G\), let \(\operatorname{St}(G)\) consist of the partial transformations of its vertex set for which the inverse image of each vertex and of each edge is either empty or an edge. Let \(E_G(t)=\sum_{f\in\operatorname{St}(G),\,f^2=f}t^{|\operatorname{im}f|}\), and let \(I(H;t)\) be the independence polynomial of a graph \(H\). The graph of pairwise conflicts between oriented edges representing strict idempotents is the **third power of a path or cycle**:
\[
H(P_n)\cong P_{2n-2}^{\,3}\quad(n\ge1),\qquad
H(C_n)\cong C_{2n}^{\,3}\quad(n\ge3).
\]
Consequently \(E_{P_n}(t)=I(P_{2n-2}^{\,3};t)\) and \(E_{C_n}(t)=I(C_{2n}^{\,3};t)\). In particular the cycle rank polynomial is
\[
 E_{C_n}(t)=\sum_{k=0}^{\lfloor n/2\rfloor}\frac{2n}{2n-3k}\binom{2n-3k}{k}t^k.
\]
This includes the coefficient \(4\) at maximum rank for even \(n\), and \(n(n+1)/2\) at maximum rank for odd \(n\). For every graph of maximum degree at most two, \(E_G\) is the product of the component polynomials. If nonconstant, it has only strictly negative real roots and its coefficients form an ultra-log-concave sequence in the sense of normalization by \(\binom{\deg E_G}{k}\).

## Assumptions and scope

Graphs are finite, undirected and simple. An oriented edge denotes an edge with one selected endpoint. Two distinct oriented edges conflict if their underlying edges coincide or intersect, or if their selected endpoints are adjacent. The graph \(H(G)\) has these oriented edges as vertices and conflicts as edges. A graph cube joins distinct vertices at distance at most three in the original graph. Here \(P_n\) has \(n\) vertices and \(P_0\) denotes the empty graph. The empty partial map is included, and rank is the cardinality of the image. The root statement is not asserted for source graphs of higher degree. These are not the idempotents of the full Margolis–Rhodes monoid.

## Proof

**From strict idempotents to the conflict graph.** Nonempty point fibers are disjoint edges. No two image vertices can be adjacent, because the inverse image of an edge between them would have four vertices. A partial map is idempotent if and only if it fixes every point in its image. Thus each nonempty fiber must contain its image vertex, and conversely choosing one vertex per matching edge and requiring all chosen vertices to be independent gives a strict idempotent. This known characterization identifies the rank with the number of chosen oriented edges and gives \(E_G(t)=I(H(G);t)\).

**Conflict geometry.** In order along the path or around the cycle, write \(e_i=\{i,i+1\}\). Let \(L_i\) and \(R_i\) select \(i\) and \(i+1\), respectively, and list the oriented edges as \(L_1,R_1,L_2,R_2,\ldots\). The two orientations of any single edge conflict, as do all orientations of successive edges. These are separated by at most three positions in the list. For disjoint edges, a conflict arises only when the right endpoint of one and the left endpoint of the other are consecutive vertices; in the forward direction the pair must be \(R_i,L_{i+2}\), exactly three positions apart. Conversely every pair at distance at most three in the list is of one of these types. On the cycle indices are taken periodically and either direction of the list can witness distance at most three. In \(C_3\) all underlying edges intersect, so the six orientations give the complete graph, also \(C_6^3\). For the one-vertex path the list is empty. This proves both graph identifications.

**Coefficient formulas.** In the linear list of \(2n-2\) positions, an independent set is a selection with successive positions differing by at least four. For rank \(k\ge1\), subtracting \(3(i-1)\) from the \(i\)-th position bijects to ordinary \(k\)-subsets of a list of length \(2n-2-3(k-1)\). Thus the already known path rank polynomial has the positive coefficient form \([t^k]E_{P_n}(t)=\binom{2n-3k+1}{k}\) for \(0\le k\le\lfloor n/2\rfloor\); the empty choice gives \(k=0\). For reference, writing \(n=m+2k\) in this coefficient sum gives the known path series \(\sum_{n\ge0}E_{P_n}(t)x^n=\sum_{m\ge0}x^m/(1-tx^2)^{2m+2}=1/(1-x-2tx^2+t^2x^4)\).

For the cyclic list of \(N=2n\) positions, first take \(k\ge1\) and distinguish a chosen position. There are \(N\) choices of its label. The successive clockwise gaps, including the last gap back to the distinguished position, each have length at least four, and their sum is \(N\). For \(k=1\) there is just the gap of length \(N\). Subtracting four from each gap gives \(\binom{N-3k-1}{k-1}\) ordered nonnegative compositions of \(N-4k\) into \(k\) parts when \(4k\le N\), and none otherwise. Dividing by \(k\) removes the distinguishing mark. This yields \(\frac Nk\binom{N-3k-1}{k-1}=\frac{N}{N-3k}\binom{N-3k}{k}\). It also yields the stated expression at \(k=0\) when the empty set is included separately. In the original cycle notation the coefficient when \(2k<n\) is equivalently \(\frac{n}{n-2k}\binom{2n-3k-1}{k}\); for \(2k=n\) the uniform expression gives \(4\).

**Components and roots.** The fibers of an idempotent map to their own endpoints, so choosing idempotents on different connected components is independent, and ranks add. Isolated vertices contribute \(1\), as does the empty graph. In a path or cycle cube the neighbors of any vertex are covered by the clique of up to three immediately preceding vertices and the clique of up to three immediately following vertices. The cliques may overlap in a short cycle, which does not affect the argument. The cubes and their disjoint unions are therefore claw-free. The Chudnovsky–Seymour theorem makes their independence polynomials real-rooted. All coefficients are nonnegative, with constant coefficient one, so no root is zero or positive. Newton's inequalities give log-concavity after division by the binomial coefficients of the degree, hence ultra-log-concavity and unimodality. When the polynomial is constant the root statement is vacuous.

## Verification

The accompanying `verify.py` and `verification_output.txt` record bounded checks of the coefficients from direct partial maps, oriented matchings and conflict-graph independent sets, as well as finite tests of claw-freeness. The recorded summary is `VERIFY_OK direct_partial_map_cases=8 oriented_matching_cases=22 conflict_polynomial_cases=14 clawfree_cases=44`. These checks do not verify the cube identification or real-rootedness for an unbounded family; the proof above establishes both. Examples are \(E_{P_6}=1+10t+21t^2+4t^3\) and \(E_{C_6}=1+12t+30t^2+4t^3\).

## Relationship to prior work and limitations

Margolis and Rhodes supply the matching and independent-image description of arbitrary strict maps (Lemma 3.3), count all strict maps by rank (Section 8), and construct selected strict idempotents on even and odd cycles for a different purpose (Definitions 11.1 and 11.3). The earlier *Idempotent enumeration in strict Margolis–Rhodes path semigroups* already gives the general selected-endpoint characterization and the very same path rank generating function, including its coefficients in an equivalent alternating-sum form. Those are antecedents, not originality claims here. The cyclic coefficient calculation is a circular spacing count, and the implication from claw-freeness is the general theorem of Chudnovsky and Seymour. The claim concerns the precise graph-cube representation of the strict-idempotent constraint and the resulting cycle rank and root conclusions for degree at most two, not originality of spacing formulas or of real-rootedness for claw-free independence polynomials. Historical priority for equivalent representations is not asserted.

## References

- S. Margolis and J. Rhodes, *The Margolis–Rhodes Monoid of a Graph*, [arXiv:2609.39370v2](https://arxiv.org/pdf/2609.39370v2), Lemma 3.3 and Sections 8 and 11.
- [*Idempotent enumeration in strict Margolis–Rhodes path semigroups*](https://github.com/Resultary/2026/blob/main/2026/10/13/SCOPE-idempotent-enumeration-in-strict-margolis-rhodes-path-semigroups--a32f66c49f5d/RESULT.md), Finding and Proof.
- M. Chudnovsky and P. Seymour, *The roots of the independence polynomial of a clawfree graph*, J. Combin. Theory Ser. B **97** (2007), 350–357, [DOI: 10.1016/j.jctb.2006.06.001](https://doi.org/10.1016/j.jctb.2006.06.001), Theorem 1.1.
