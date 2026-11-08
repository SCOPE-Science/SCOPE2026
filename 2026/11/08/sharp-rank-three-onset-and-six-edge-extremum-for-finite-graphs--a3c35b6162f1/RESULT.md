# Sharp rank-three onset and six-edge extremum for finite graphs

## Finding

Let \(\mathcal G\) be the Fraïssé class of all finite simple undirected graphs, with induced-subgraph embeddings. For a finite or countable graph \(X\), use the extension rank \(\operatorname{rk}(X)=\operatorname{rk}_{X}(\varnothing)\) defined below. Then:

1. **Sharp onset:** \(\operatorname{rk}(X)\ge 3\) requires at least seven vertices, and a seven-vertex graph with rank exactly three exists.
2. **Sharp edge extremum and classification:** For every integer \(n\ge7\), the minimum number of edges in an \(n\)-vertex graph of rank at least three is **six**. Up to isomorphism the unique minimizer is a six-vertex connected graph with edge set
   \[
   \{\{0,2\},\{0,3\},\{0,5\},\{1,2\},\{1,4\},\{2,3\}\}
   \]
   together with \(n-6\) isolated vertices. The number of labelled minimizers is exactly
   \[
   \frac{n!}{(n-6)!}.
   \]
   In particular, exactly \(5040\) labelled graphs on seven vertices and six edges have rank at least three; no graph on seven vertices with at most five edges does.
3. **Consequent forcing cutoff:** Let \(N(3)\) be the least positive integer \(N\) such that every finite or countable graph containing every \(N\)-vertex graph as an induced subgraph has rank at least three. Then
   \[
   \boxed{6\le N(3)\le7.}
   \]
   This statement does **not** decide whether \(N(3)\) equals six or seven.

The first two assertions concern the rank of an individual graph. The third concerns simultaneous containment of *all* graphs of a prescribed order; they are different invariants.

## Assumptions and scope

Graphs are simple, undirected, loopless, and have no additional predicates. An embedding preserves edges and nonedges. The rank is the ordinal-valued one-point-extension rank for \(\mathcal G\): for any finite induced \(F\subseteq X\), \(\operatorname{rk}_{X}(F)\ge0\); and \(\operatorname{rk}_{X}(F)\ge\alpha+1\) iff every abstract one-vertex extension of \(F\) has an induced realization \(F\cup\{x\}\subseteq X\) with \(\operatorname{rk}_{X}(F\cup\{x\})\ge\alpha\). Limit ordinals are treated by intersection, and \(\operatorname{rk}(X)=\operatorname{rk}_{X}(\varnothing)\).

For distinct vertices \(v,w\), define their **two-vertex extension profile** by
\[
P_X(v,w)=\{(\mathbf1_{vx\in E(X)},\mathbf1_{wx\in E(X)}):x\in X\setminus\{v,w\}\}.
\]
Call \(\{v,w\}\) *full* when \(P_X(v,w)=\{0,1\}^2\). The definition concerns **distinct** witnesses outside the pair; each profile has at least one witness, but witnesses need not be unique.

## Proof

### One-step rank test

For each pair \(v,w\), the four possible abstract one-point extensions specify adjacency bits to the two already named vertices. Therefore
\[
\operatorname{rk}_{X}(\{v,w\})\ge1\quad\Longleftrightarrow\quad P_X(v,w)=\{0,1\}^2.
\]
There are exactly two one-point extension types of a singleton: an adjacent new vertex and a nonadjacent new vertex. The empty graph has one one-vertex extension type. Unrolling the rank definition three times yields the exact criterion
\[
\boxed{\operatorname{rk}(X)\ge3\quad\Longleftrightarrow\quad
\exists v\,\exists a\,\exists b\;[v\sim a\wedge v\not\sim b\wedge
P_X(v,a)=P_X(v,b)=\{0,1\}^2].}
\]
Here all vertices displayed in an extension are distinct. This criterion applies to **every** finite or countable graph; it does not assume saturation or homogeneity.

### Minimum number of vertices

Fix a witnessing center \(v\), adjacent partner \(a\), and nonadjacent partner \(b\). Fullness of \((v,a)\) requires both profiles \((1,0)\) and \((1,1)\), produced by two different neighbors of \(v\) other than \(a\). Thus \(v\) has at least three neighbors. Fullness of \((v,b)\) requires profiles \((0,0)\) and \((0,1)\), produced by two different nonneighbors of \(v\) other than \(b\). Thus \(v\) has at least three nonneighbors. There are at least \(1+3+3=7\) vertices.

On vertices \(0,1,\ldots,6\), take exactly the six edges displayed in the finding. For \((v,a)=(0,2)\), vertices \(4,1,5,3\) realize the profiles \((0,0),(0,1),(1,0),(1,1)\), respectively. For \((v,b)=(0,1)\), vertices \(6,4,3,2\) realize those same profiles, respectively. Since \(0\sim2\) and \(0\not\sim1\), the criterion gives rank at least three. A separate exhaustive recursion implementing the rank definition (rather than the simplified pair-profile test) computes rank exactly three for this finite witness; the explicit recursion is given in `checker.py`. Exact rank three is **not** needed for the other conclusions.

### Minimum number of edges

Let \(A=N_X(v)\) and \(B=X\setminus(A\cup\{v\})\). The first pair \((v,a)\) forces \(|A|\ge3\), hence at least three edges incident with \(v\). Its \((1,1)\) witness forces an edge internal to \(A\), and its \((0,1)\) witness forces an edge between \(A\) and \(B\). The second pair \((v,b)\) has a \((0,1)\) witness and therefore forces an edge internal to \(B\). These four edge classes are disjoint, giving at least \(3+1+1+1=6\) edges.

If there are exactly six edges, then \(\deg(v)=3\), and there is exactly one edge in each of \(E(A)\), \(E(B)\), and \(E(A,B)\). Write the three neighbors of \(v\) as \(a,c,d\), with \(a\) the full adjacent partner. The profiles \((1,1)\), \((1,0)\) for \((v,a)\) force the unique edge of \(E(A)\) to be \(ac\), not \(ad\); the labels \(c,d\) may be interchanged. Let \(b\) be the full nonadjacent partner. The \((0,1)\) profile for \((v,b)\) forces the unique \(B\)-edge to be \(be\) for some \(e\in B\setminus\{b\}\). The \((0,1)\) profile for \((v,a)\) forces the unique cross edge to touch \(a\); the \((1,1)\) profile for \((v,b)\) forces that same cross edge to touch \(b\). Consequently the cross edge is \(ab\). Together with the three edges incident with \(v\), the six edges are exactly
\[
\{va,vc,vd,ac,be,ab\}.
\]
Their nonisolated vertices form one connected six-vertex graph. All other vertices are isolated. At least one isolate is needed to supply the \((0,0)\) profile for \((v,b)\), so \(n\ge7\); conversely one isolate suffices, and more isolates preserve the profile witnesses.

This connected component is asymmetric: its triangle has two degree-three vertices, of which only one supports a leaf and the other supports a path of length two. Every other vertex is then fixed. Hence the automorphism group of the full \(n\)-vertex minimizer is the symmetric group on its \(n-6\) isolates, and the number of labelled copies is \(n!/(n-6)!\).

### Universal forcing cutoff

The seven-vertex witness is one of the seven-vertex graph types. Any \(X\) containing **every** such graph contains an induced copy of the witness. Existing witnesses to the two full pairs remain witnesses in \(X\), so \(\operatorname{rk}(X)\ge3\). Therefore \(N(3)\le7\).

For the reverse bound, take a disjoint union \(Y\) of one representative of **each** five-vertex graph isomorphism type. It contains all five-vertex graph types. Suppose a vertex \(v\) in a five-vertex component \(C\) had full adjacent and full nonadjacent partners. A full adjacent partner forces at least three neighbors of \(v\), all in \(C\). A full nonadjacent partner cannot be outside \(C\): a cross-component pair has no common neighbor and lacks profile \((1,1)\). Thus it lies in \(C\), where its \((0,1)\) profile requires a *second* nonneighbor of \(v\) within \(C\). Then \(C\) would contain at least \(1+3+2=6\) vertices, contradiction. Thus \(\operatorname{rk}(Y)<3\), proving \(N(3)>5\). This proves \(6\le N(3)\le7\).

## Verification

Run `python checker.py` using Python 3 and no external dependencies. The checker independently unrolls all four adjacency profiles for every ordered pair. It exhausts all \(33867\) labelled graphs on at most six vertices; all seven-vertex graphs with at most six edges; and the orbit of the displayed extremal graph under all \(7!\) permutations. It finds zero rank-three cases with at most five edges, exactly \(5040\) with six edges, and equality of that entire set with the one permutation orbit. A separate recursive computation of the finite rank of the witness returns three. Finally, the checker tests all \(1024\) five-vertex labelled components with a disconnected outside vertex as a finite check of the lower-bound mechanism.

The finite census is exhaustive within its explicitly stated finite ranges. The proof, not extrapolation from the census, establishes the claims for arbitrary \(n\ge7\) and all finite or countable graphs in the cutoff statement.

## Relationship to prior work

López-Callejas and Navarro-Castillo, *A rank function for Fraïssé classes and the rank property* (arXiv:2604.14461, first posted April 15, 2026), introduced the exact finite-structure rank framework used here, proved general existence of finite graphs of any finite rank, and in Question 7.4 asked about a related graph forcing cutoff. They gave \(N(1)=1\), \(N(2)=2\), and \(4\le N(3)\le |H_3|\); their construction gives \(|H_3|=11\) for simple graphs. The bound \(6\le N(3)\le7\), the sharp six-edge threshold, and its uniqueness are additional quantitative statements rather than a rephrasing of the general construction.

Kubiś and Shelah's *Evolution systems—an ordinal rank measuring universality* (2024) develops the underlying one-point extension rank in a broader category-theoretic setting. The known enumeration of unlabeled graphs on at most seven vertices in Read–Wilson's *An Atlas of Graphs* does not itself tabulate this rank or imply the edge-extremal classification without an additional rank argument.

## Limitations

The exact value of \(N(3)\) remains undetermined between six and seven. The theorem does not claim a classification of all graphs with rank three, nor a seven-vertex induced witness inside *every* larger rank-three graph. It classifies **edge-minimal** cases only. The finite computation confirms the small cases but does not replace the general proof. Historical priority beyond the primary papers and databases searched is not independently established.

## References

1. C. López-Callejas and J. Navarro-Castillo, *A rank function for Fraïssé classes and the rank property*, arXiv:2604.14461v1, 2026-04-15; revised version v3 2026-06-02. https://arxiv.org/html/2604.14461
2. W. Kubiś and S. Shelah, *Evolution systems—an ordinal rank measuring universality*, 2024, https://users.math.cas.cz/kubis/pdfs/ranksEvasPS_ver2.pdf
3. R. C. Read and R. J. Wilson, *An Atlas of Graphs*, Oxford University Press, 1998; catalogue availability also described at https://r.igraph.org/reference/graph_from_atlas.html
