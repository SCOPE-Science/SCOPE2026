# Connected distance-two supports classify minimal forts in whiskered trees

## Finding

Let \(T\) be any finite nonempty tree and let \(W(T)=T\circ K_1\) denote its *whiskering*: each core vertex \(v\) receives one new pendant mate \(v'\). A nonempty set \(F\) is a *fort* if no vertex outside \(F\) has exactly one neighbor inside \(F\); it is *inclusion-minimal* if it contains no smaller nonempty fort.

For every nonempty \(A\subseteq V(T)\), put
\[
S(A)=A\cup\{v':v\in A\}\cup\{v':v\notin A,\ |N_T(v)\cap A|=1\}.
\]
Define the **two-step link graph** \(H_T(A)\) with vertex set \(A\) and an edge \(uw\) precisely when a vertex \(v\notin A\) has \(N_T(v)\cap A=\{u,w\}\).

**Theorem.** The inclusion-minimal forts of \(W(T)\) are exactly
\[
\{S(A):\varnothing\ne A\subseteq V(T),\ H_T(A)\text{ connected}\}.
\]
This is a bijective characterization: distinct core supports give distinct forts.

For the *comb* \(W(P_n)\), \(n\ge2\), label the core path \(0,1,\ldots,n-1\). Each minimal fort has selected core support precisely \(A_{a,b}=\{a,a+2,\ldots,b\}\), where \(0\le a\le b<n\) and \(b-a\) is even. Consequently the polynomial counting all inclusion-minimal forts by their number of vertices is
\[
\boxed{\displaystyle
M_n(z)=\sum_{\substack{0\le a\le b<n\b-a\equiv0\pmod2}}
 z^{b-a+2+\mathbf1_{\{a>0\}}+\mathbf1_{\{b<n-1\}}}.}
\]
In particular,
\[
M_n(1)=\left\lfloor\frac{(n+1)^2}{4}\right\rfloor,\qquad
\operatorname{supp}(M_n)=\{3,4,\ldots,n+1\}.
\]
Exactly two minimal forts have size \(3\), and exactly two have size \(n+1\) (coincidences are counted by their distinct supports). Despite this quadratic census, the total number of nonempty forts of the comb is at least \(2^n-1\).

## Assumptions and scope

All graphs are finite, simple and undirected, with ordinary (not skew or positive semidefinite) zero forcing. Connectivity of a one-vertex link graph is understood to hold. The general criterion applies to every tree, including the single-vertex tree; the comb enumerator and cardinality interval use \(n\ge2\).

## Proof

1. For any nonempty \(A\), the set \(S(A)\) is a fort. Every pendant vertex outside it has its unique core neighbor outside \(A\). Every core vertex outside \(A\) has either zero core neighbors in \(A\) and its mate outside \(S(A)\), exactly one such core neighbor and its mate inside \(S(A)\), or at least two such neighbors. Its number of neighbors in \(S(A)\) is therefore respectively \(0,2,\) or at least \(2\).

2. If \(F\) is an inclusion-minimal fort, its core support \(A=F\cap V(T)\) is nonempty: otherwise any pendant vertex of \(F\) gives an outside core vertex with exactly one neighbor in \(F\). For a core vertex inside \(A\), its mate must belong to \(F\), because an outside mate has degree one. For a core vertex outside \(A\), a mate in \(F\) is forbidden when there are no neighbors in \(A\), required when there is exactly one, and dispensable when there are at least two (deleting that mate still leaves a fort). Thus necessarily \(F=S(A)\).

3. A minimal fort on a tree cannot have any outside vertex with three or more neighbors in the fort: delete the fort vertices in one branch of the tree rooted at this outside vertex. At least two fort neighbors remain at the root, and every vertex in the deleted branch has no surviving fort neighbor across the cut; elsewhere the fort condition is unchanged. This constructs a smaller nonempty fort, a contradiction. Hence for minimal \(S(A)\), every vertex \(v\notin A\) has at most two core neighbors in \(A\).

4. Suppose \(H_T(A)\) is disconnected and all vertices outside \(A\) have at most two neighbors in \(A\). Choose a nonempty proper connected component \(B\subsetneq A\) of \(H_T(A)\). For a vertex \(v\notin A\) with exactly two neighbors in \(A\), either both of them belong to \(B\) or neither does, because they form an edge of \(H_T(A)\). Vertices with zero or one such neighbor require no new pendant mates when one passes from \(A\) to \(B\). Consequently \(S(B)\subsetneq S(A)\), and \(S(A)\) is not minimal.

5. Conversely, suppose \(H_T(A)\) is connected. Since \(T\) is bipartite, the two endpoints of each link-graph edge lie in the same bipartition class. Connectedness therefore forbids an edge of \(T\) within \(A\). Connectedness also forbids an outside vertex \(v\) having three or more neighbors in \(A\): those neighbors lie in distinct components of \(T-v\), and no link-graph path can connect them without using \(v\), which is not eligible to induce a link edge. Assume \(F'\subseteq S(A)\) is a nonempty fort with core support \(B\subseteq A\). As in step 2, \(B\ne\varnothing\), and \(F'\) must contain the forced pendant mates in \(S(B)\). At every vertex with two neighbors in \(A\), its pendant mate is absent from \(S(A)\); consequently \(B\) must contain both those neighbors or neither. Hence \(B\) is a union of components of connected \(H_T(A)\), and since nonempty, \(B=A\). Now every pendant mate present in \(S(A)\) is forced, so \(F'=S(A)\). This proves minimality and the characterization.

6. When \(T=P_n\), a connected link graph can only connect selected core vertices at distance two separated by unselected vertices. Such a connected support must be a consecutive arithmetic progression with step two, and every such progression has connected link graph. It has \((b-a)/2+1\) selected cores and their mates, plus the mate at \(a-1\) if \(a>0\) and the mate at \(b+1\) if \(b<n-1\). This gives the displayed polynomial. The numbers of possible intervals in the two parity classes (of sizes \(\lceil n/2\rceil\) and \(\lfloor n/2\rfloor\)) sum to \(\lfloor(n+1)^2/4\rfloor\). The maximal progression in each parity class has size \(n+1\) as a fort. The singleton progressions at the two core endpoints are exactly the two size-three forts, and varying interval length and whether an interval touches an endpoint realizes every intervening integer cardinality. Finally each nonempty core subset \(A\) supplies a distinct fort \(S(A)\), establishing at least \(2^n-1\) forts.

## Verification

The accompanying standalone Python program independently enumerates every fort by the defining neighbor condition, filters inclusion-minimal ones by full subset containment (not only one-vertex deletion), constructs the proposed link-graph family, and compares both sets. It checks all combs through eight core vertices and all unlabeled trees through six core vertices by explicit representative edge lists. It also verifies polynomial coefficients and boundary cases. Execute \(`python3 VERIFY.py`\) with Python 3.9 or later; no third-party packages are used. Finite computations are corroboration, not a substitute for the all-tree proof above.

## Relationship to prior work

Becker–Cameron–Hanely–Ong–Previte (originally public April 9, 2024) give foundational fort enumeration, including a four-comb illustration and formulas for paths, cycles, and spiders, but not this complete whiskered-tree link-graph bijection or the comb cardinality polynomial. Cameron–Li (first public December 14, 2025) prove a general cut characterization of minimal forts in trees; the theorem here makes the structural constraints explicit for all one-leaf coronas and then derives an all-order counting polynomial for combs. Abiad–Ghasemi Nezhad (first public September 10, 2026) provide a linear-time scalar-counting algorithm for arbitrary trees; the symbolic cardinality profile and quadratic/exponential obstruction contrast are not stated in its accessible abstract. A contemporary classification for cycle coronas concerns cyclic support rather than the tree-corona family. General-purpose algorithms may compute each individual specialization, but do not by themselves state the all-order formula.

## Limitations

The theorem concerns one-leaf coronas of trees and their inclusion-minimal ordinary forts, not arbitrary graphs or all zero-forcing sets. The general scalar-counting algorithm and earlier four-comb example mean that no claim is made to discovering the comb object or algorithmic decidability. The 2026 linear-time algorithm was accessible through its primary abstract, not its complete paper, so historical priority of the explicit specialization retains a residual literature risk. Independent validation has not been performed.

## References

- P. Becker, T. R. Cameron, D. Hanely, B. Ong, J. P. Previte, *On the Number of Minimal Forts of a Graph*, arXiv:2404.05963v1 (April 9, 2024). https://arxiv.org/abs/2404.05963
- T. R. Cameron, K. Li, *On the minimal forts of trees*, arXiv:2512.12874v1 (December 14, 2025). https://arxiv.org/abs/2512.12874
- A. Abiad, S. Ghasemi Nezhad, *Fort Abundance in Zero Forcing*, arXiv:2609.11754v1 (September 10, 2026). https://arxiv.org/abs/2609.11754
