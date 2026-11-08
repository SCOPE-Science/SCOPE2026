# Exact three-variable deletion resilience of rank-two Grassmann graphs

## Finding
For any prime power \(q\ge2\) and integer \(n\ge4\), let \(G=J_q(n,2)\) be the graph whose vertices are two-dimensional vector subspaces of \(\mathbb F_q^n\), two distinct vertices adjacent when their intersection has dimension one. Define \(\rho(G)\) to be the smallest number of vertices whose deletion produces a graph that is **not** equivalent, in counting-free first-order logic using at most three variable names and unrestricted quantifier depth, to the countable random graph \(\mathcal R\).

The exact deletion threshold is
\[
\rho(J_q(n,2))=\begin{cases}6,&(n,q)=(4,2),\\(q+1)^2,&\text{otherwise}.\end{cases}
\]
All the original graphs \(J_q(n,2)\) have the same three-variable theory as \(\mathcal R\). For every vertex set \(S\) with \(|S|<\rho(G)\), the induced graph \(G-S\) remains three-variable equivalent to \(\mathcal R\); for at least one set \(S\) of size exactly \(\rho(G)\), equivalence fails. More precisely, **every** minimum destructive deletion set has the following form. In the exceptional binary four-dimensional graph, choose two disjoint two-dimensional subspaces \(A,B\) and delete all *other* vertices adjacent to neither; there are exactly six. In all other cases, choose two such subspaces and delete all their common neighbors; there are exactly \((q+1)^2\). Conversely every deletion set of one of these types is minimum destructive. No uniqueness of the representing pair is claimed.

## Assumptions and scope
Write \([m]_q=(q^m-1)/(q-1)\) for the number of projective points of \(\mathbb F_q^m\). Graphs are finite, undirected, loopless, and interpreted solely in the adjacency-and-equality signature, without counting quantifiers. \(q\) ranges over all prime powers, not just primes. The dimension \(n\) ranges over all integers at least four. The deletion operation is induced vertex deletion; a destructive set need not be unique. The countable random graph is the unique countable graph with the finite extension property. A graph has the two-extension property (is \(2\)-existentially closed) when, for every two distinct vertices \(a,b\), all four patterns of adjacency/nonadjacency toward \(a,b\) have witnesses distinct from \(a,b\).

## Proof
**1. Pair parameters.** Let \(v=|V(G)|\), let \(d\) be its degree, and let \(\lambda\) and \(\mu\) be the common-neighbor counts of adjacent and nonadjacent distinct vertices. Direct vector-space counting gives
\[
v=\frac{(q^n-1)(q^{n-1}-1)}{(q^2-1)(q-1)},\quad d=q(q+1)[n-2]_q,\quad \lambda=[n-1]_q-2+q^2,\quad \mu=(q+1)^2.
\]
For the degree, a neighbor of a two-space \(A\) meets it in one of its \(q+1\) projective points; for each choice, the other point of the neighbor is a projective point in the quotient \(\mathbb F_q^n/L\) outside the unique point \(A/L\), yielding \(q[n-2]_q\) choices. For adjacent \(A,B\), put \(L=A\cap B\) and \(W=A+B\) (dimension three). Common neighboring two-spaces either contain \(L\), giving \([n-1]_q-2\) possibilities, or are contained in \(W\) and do not contain \(L\), giving \(q^2\). For nonadjacent \(A,B\), the subspaces are disjoint, and a common neighbor is uniquely the span of one projective point in \(A\) and one in \(B\), giving \((q+1)^2\). These exhaust the possibilities by dimension two.

**2. All six witness multiplicities.** Fix distinct vertices \(a,b\). Denote by \(N_{11}\), \(N_{10}=N_{01}\), and \(N_{00}\) the numbers of vertices outside \(\{a,b\}\) having the indicated adjacency bits. For adjacent \(a,b\), the three counts are respectively
\[
\lambda,\qquad d-1-\lambda=q^3[n-3]_q,\qquad v-2d+\lambda.
\]
For nonadjacent \(a,b\), they are respectively
\[
\mu,\qquad d-\mu,\qquad v-2-2d+\mu.
\]
The subtraction of the stationary vertices is essential: for an adjacent pair, each endpoint is counted in its opposite endpoint's neighborhood, whereas for a nonadjacent pair both endpoints belong to the uncorrected common-nonneighborhood. Thus all six formulas count actual permissible witnesses, not merely Boolean intersections of unguarded neighborhoods.

**3. The global least witness number.** The elementary comparison
\[
\lambda-\mu\ge0,
\qquad (d-\mu)-(d-1-\lambda)=\lambda+1-\mu>0,
\qquad (v-2d+\lambda)-(v-2-2d+\mu)=\lambda-\mu+2>0
\]
holds because \(\lambda\ge\mu\) when \(n\ge4,q\ge2\). Hence the minimum over all pair types and all adjacency patterns is
\[
\rho_0=\min\big\{(q+1)^2,\ q^3[n-3]_q,\ Z(n,q)\big\},\quad Z(n,q)=v-2-2d+(q+1)^2.
\]
For \(q\ge3\), \(q^3\ge(q+1)^2\), so the second candidate is strictly larger than the first. For \(q=2,n\ge5\), it is at least \(2^3[2]_2=24>9\); the one exception \((n,q)=(4,2)\) has second candidate eight.

The quantity \(Z(n,q)\) counts vertices outside a fixed disjoint pair of two-spaces that are adjacent to neither. Holding that pair inside a fixed four-dimensional summand and enlarging the ambient space only adds potential witnesses; therefore \(Z(n,q)\) is nondecreasing in \(n\) for each \(q\). At \(n=4\), direct expansion gives
\[
Z(4,q)-(q+1)^2=(q+1)\big(q^2(q-2)-1\big).
\]
This is positive for all \(q\ge3\) and equals \(-3\) at \(q=2\). In the remaining case \(q=2,n=5\), the explicit parameters are \(v=155\), \(d=42\), \(\mu=9\), and \(Z(5,2)=78>9\). Thus \(\rho_0=6\) at \((n,q)=(4,2)\), and \(\rho_0=(q+1)^2\) otherwise. All other witness types have strictly greater multiplicity than the minimum, proving that the only minimizing patterns are the ones stated in the finding. In particular \(\rho_0>0\), so each original graph has the two-extension property.

**4. Logical interpretation and deletion sharpness.** The two-extension property implies equivalence with \(\mathcal R\) in ordinary \(\mathrm{FO}^{3}\): in the infinite three-pebble game, Duplicator preserves equality and adjacency, and when a pebble moves only two stationary vertices remain. The required response exists by the two-extension property; fewer stationary pebbles are covered by forgetting an arbitrary second vertex. This maintains a winning strategy through all finite rounds and hence at every finite quantifier rank. Conversely, the two-extension property is a conjunction of four three-variable first-order sentences, with all inequality guards explicitly expressible using those three names. Therefore failure of one pattern is witnessed by a three-variable sentence that holds in \(\mathcal R\).

Deleting fewer than \(\rho_0\) vertices leaves at least one witness for every two-vertex pattern on all surviving stationary pairs, proving universal resilience. Choose any disjoint two-spaces \(A,B\). At the exceptional parameters delete their six common nonneighbors *other than the two stationary vertices*; otherwise delete the \((q+1)^2\) common neighbors. In each case \(A,B\) survive and the corresponding pattern has no witness. Thus deletion of exactly \(\rho_0\) vertices can destroy the property. Finally, if \(|S|=\rho_0\) destroys it, some stationary pair loses one entire witness set. That set has at least \(\rho_0\) vertices and is disjoint from its stationary pair, so it must equal \(S\) and have precisely the unique minimizing pattern type established above. This completes the classification of all minimum destructive sets.

## Verification
The included standalone script `verify.py` reconstructs, over the actual prime fields of orders two and three, all two-dimensional subspaces in ambient dimensions \((n,q)=(4,2),(5,2),(4,3)\) using canonical reduced row echelon forms. It enumerates every unordered pair and counts every legal adjacency extension with bitsets, including the exclusions of the two stationary vertices, then checks all six symbolic parameter formulas, the sharp minimum, and all uniform degree and vertex-count formulas. It also checks the purely arithmetic formulas for five ambient dimensions and eight field-order values (40 parameter pairs, including nonprime prime powers where only the arithmetic formulas are checked). Reproduce with `python3 verify.py` in the directory containing the embedded files; compare the exact printed results with `verification_output.txt`. The script relies only on the Python standard library. The calculations check finite instances and identities, not the all-parameters theorem, which is established above.

## Relationship to prior work
Pankov (2011, arXiv:1109.5624) treats Grassmann graph embeddings and the star/top geometry underlying the common-neighbor count; it does not state three-variable logical equivalence or adversarial vertex-deletion thresholds. Bonato and Cameron (2001) introduced critical existentially closed graphs; a later treatment of Cayley criticality (2025, DOI:10.61091/ars164-02) studies a different graph family and a one-vertex criticality question, not exact fault tolerance of Grassmann graphs. Guo, Wang and Li (2011, arXiv:1105.1847) study metric dimension of doubled Grassmann graphs, a separation-of-distances invariant rather than adjacency extension multiplicity. Byrne, Byrne and Cioabă (2026, arXiv:2609.10330) discuss existential closure and VC dimension of strongly regular graphs; their cited general results do not supply the rank-two Grassmann deletion classification. The algebraic witness calculations here are elementary once the parameters are known, but the exact resilience phase transition and classification of every minimum destructive deletion set are separate, motivated statements. These comparisons do not constitute an exhaustive historical-priority determination.

## Limitations
The theorem only addresses rank-two Grassmann graphs, the pure adjacency signature, counting-free three-variable first-order logic, and induced vertex deletion. It does not classify higher-variable equivalence, larger-subspace Grassmann graphs, edge deletion, or the number of distinct minimum destructive sets. A general unpublished statement about fault tolerance of all strongly regular graphs could subsume the elementary parameter reduction. Independent mathematical audit has not been performed. Computation over prime fields does not computationally exhaust all prime-power fields.

## References
- Mark Pankov, *Embeddings of Grassmann graphs*, arXiv:1109.5624, first submitted 2011-09-26; https://arxiv.org/abs/1109.5624.
- Jun Guo, Kaishun Wang, Fenggao Li, *Metric dimension of some distance-regular graphs*, arXiv:1105.1847, first submitted 2011-05-10; https://arxiv.org/abs/1105.1847.
- Anthony Bonato and Kathie Cameron, *On an adjacency property of almost all graphs*, Discrete Mathematics 231 (2001), 103–119; DOI:10.1016/S0012-365X(00)00309-5.
- *Existentially closed critical Cayley graphs*, Ars Combinatoria 164 (2025), 19–32; DOI:10.61091/ars164-02.
- Isabel Byrne, John Byrne, Sebastian M. Cioabă, *The VC-dimension of strongly regular graphs*, arXiv:2609.10330, first posted 2026-09-09; https://arxiv.org/abs/2609.10330.
