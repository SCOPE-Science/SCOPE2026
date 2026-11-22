# Rank-three witnesses and the nine six-vertex forbidden shapes for triangle-free graphs

## Finding

Let \(\mathcal T\) be the hereditary class of finite simple undirected triangle-free graphs, with induced embeddings, and let \(\operatorname{rk}_{\mathcal T}(X)\) be the one-point-extension rank of a finite or countable triangle-free graph \(X\) relative to this class. There are three equivalent conditions:

1. \(\operatorname{rk}_{\mathcal T}(X)\ge3\).
2. Some **nonadjacent** vertices \(u,v\) have all four possible adjacency traces among vertices outside \(\{u,v\}\):
   \[
   \{N_X(w)\cap\{u,v\}:w\in X\setminus\{u,v\}\}
     =\{\varnothing,\{u\},\{v\},\{u,v\}\}.
   \]
3. \(X\) contains, as an induced subgraph, one of precisely **nine** nonisomorphic triangle-free graphs on six vertices described by the census table below.

Thus the graphs of rank less than three form, *within triangle-free graphs*, a hereditary class with a finite forbidden induced-subgraph basis of nine six-vertex graphs. The minimum order for rank at least three is **six**. The minimum number of edges at every order \(n\ge6\) is **four**, uniquely attained up to isomorphism by \(P_5\sqcup(n-5)K_1\). On the labelled vertex set \(\{0,\ldots,5\}\), exactly **2292** of the **5789** triangle-free graphs have rank at least three, belonging to **nine** graph isomorphism classes. Grouped by edge count \(4,5,6,7\), the respective labelled counts are \(360,792,780,360\) and the respective unlabelled counts are \(1,3,3,2\); no other edge counts occur.

For context, the lower finite-rank cuts are exact as well: \(\operatorname{rk}_{\mathcal T}(X)\ge1\) precisely when \(X\) is nonempty, and \(\operatorname{rk}_{\mathcal T}(X)\ge2\) precisely when \(X\) has at least three vertices and at least one edge. No conclusion about rank four or higher is asserted.

## Assumptions and scope

All graphs are loopless and simple; embeddings are induced, so edges and nonedges are both preserved. The empty finite graph is included in the hereditary class. A **prime extension** of a finite marked induced graph adds one new vertex while staying triangle-free. For a finite marked induced subgraph \(F\subseteq X\), let \(\operatorname{rk}_{X}(F)\ge0\) always, and define \(\operatorname{rk}_{X}(F)\ge r+1\) when every admissible prime extension of \(F\) has a realization in \(X\) of rank at least \(r\). The host rank is \(\operatorname{rk}_{X}(\varnothing)\). Only the finite thresholds \(r\in\{0,1,2,3\}\) are needed; the usual ordinal continuation gives the same comparisons for finite or countable hosts.

If \(p,q\) are distinct, put
\[
T_X(p,q)=\{(\mathbf 1_{pw\in E(X)},\mathbf 1_{qw\in E(X)}): w\in X\setminus\{p,q\}\}.
\]
For a nonedge pair all four signatures \(00,10,01,11\) are admissible. For an edge pair, only \(00,10,01\) are admissible: \(11\) would create a triangle. In this context a rank-one marked pair has *all its admissible signatures* represented, with distinct exterior vertices whenever the signatures are different.

## Proof

**1. Three-round reduction.** Unroll the definition. The empty marking has one admissible singleton extension, hence \(\operatorname{rk}_{X}(\varnothing)\ge3\) iff some vertex \(u\) satisfies \(\operatorname{rk}_{X}(\{u\})\ge2\). For a singleton, the two admissible extension signatures are an edge and a nonedge. For a pair \(\{p,q\}\), rank at least one means that every admissible one-vertex extension signature is realized in the host. Consequently, rank at least three requires a vertex \(u\) with an adjacent partner whose three allowed signatures are realized and a nonadjacent partner whose four allowed signatures are realized. In particular, (1) implies (2).

Conversely, suppose a nonedge pair \(u,v\) realizes the four signatures, witnessed by four distinct vertices \(a,b,c,d\), with
\[
N_X(a)\cap\{u,v\}=\{u\},\quad
N_X(b)\cap\{u,v\}=\{v\},\quad
N_X(c)\cap\{u,v\}=\{u,v\},\quad
N_X(d)\cap\{u,v\}=\varnothing.
\]
The marked nonedge pair \(\{u,v\}\) has rank at least one. The edge \(uc\) also has rank at least one: \(a\) gives the signature \(10\), \(v\) gives \(01\), and \(b\) gives \(00\), relative to the ordered pair \((u,c)\). Indeed, the edges \(ac\) and \(bc\) are forbidden by the triangle-free assumption (as \(u,a,c\) and \(v,b,c\) would be triangles). Thus the vertex \(u\) has both an adjacent and a nonadjacent rank-one partner. The defining recursion yields \(\operatorname{rk}_{X}(\varnothing)\ge3\), proving (2) implies (1) for arbitrary finite or countable \(X\).

**2. Six-point extraction, minimum order and sparsity.** In the preceding argument \(u,v,a,b,c,d\) are six distinct vertices. They induce a triangle-free rank-three witness, so rank at least three forces at least six vertices. They also force the four distinct edges \(ua,uc,vb,vc\). The six-vertex graph with exactly these edges is the five-vertex path \(a-u-c-v-b\) plus the isolated vertex \(d\), which realizes every required signature and has rank at least three. Every additional edge-free vertex may be added without destroying the witness, proving attainability at every \(n\ge6\) with four edges. If a host has exactly four edges, these forced four must be all its edges, so every other vertex is isolated and its isomorphism type is uniquely \(P_5\sqcup(n-5)K_1\). Its number of labelled realizations is \(n!/[2(n-5)!]\).

**3. Complete six-vertex shape reduction.** On exactly six vertices, every rank-three graph has \(u,v,a,b,c,d\) as above. The four mandatory edges are \(ua,uc,vb,vc\). Every additional edge is forbidden except the four optional edges
\[
 ab,\qquad ad,\qquad bd,\qquad cd.
\]
The simultaneous presence of \(ab,ad,bd\) creates a triangle; no other selection of these optional edges creates one. Hence the six-vertex rank-three graphs are exactly the relabellings of the **14** rooted templates obtained by choosing any subset of the four optional edges other than one containing all of \(ab,ad,bd\). Every such template contains the full nonedge profile and therefore has rank at least three. This proves (1) equivalent to (3), and proves the nine shapes form a *minimal* forbidden induced family, once their pairwise nonisomorphism and number are verified: all nine have the same six-vertex order, so no distinct member can properly contain another.

**4. Exact isomorphism and labelled census.** For a machine-readable canonical representation, label vertices \(0,\ldots,5\), order the \(15\) potential edges lexicographically as \((0,1),(0,2),\ldots,(4,5)\), and represent an edge set by the integer with bit \(i\) equal to one exactly when edge \(i\) is present. Taking every relabelling by the \(720\) elements of \(S_6\), the fourteen templates generate exactly nine orbits:

| Edges | Canonical bitmask | Orbit size (labelled) | Automorphisms |
| ---: | ---: | ---: | ---: |
| 4 | 106 | 360 | 2 |
| 5 | 659 | 360 | 2 |
| 5 | 684 | 72 | 10 |
| 5 | 692 | 360 | 2 |
| 6 | 700 | 360 | 2 |
| 6 | 922 | 360 | 2 |
| 6 | 1880 | 60 | 12 |
| 7 | 956 | 180 | 4 |
| 7 | 1884 | 180 | 4 |

Canonical means the least bitmask over all six-vertex relabellings. The orbit sizes add to \(2292\), the edge strata to \((360,792,780,360)\), and orbit–stabilizer holds in each row. The standalone `checker.py` enumerates the fourteen rooted templates and all \(720\) relabellings, and separately exhausts all \(2^{15}\) labelled simple six-vertex graphs using the defining rank recursion. Both sets coincide, with exactly nine orbits, which is an exhaustive *finite* certificate for the displayed census. The general all-size theorem follows from the preceding structural proof, not from the finite enumeration.

**5. Rank one and two.** Rank at least one means merely that a singleton extension of the empty marking can be realized. For rank at least two, a vertex needs both a neighbour and a nonneighbour. Such a vertex plainly forces an edge and at least three vertices. Conversely, if a triangle-free graph with at least three vertices has an edge \(uv\), any third vertex is nonadjacent to at least one of \(u,v\), otherwise it would form a triangle. That endpoint has both sorts of partner; this proves the claimed rank-two criterion.

## Verification

Execute `python3 checker.py` in an environment with Python 3.8 or later. No third-party packages or input files are needed. The program has three independent cross-checks: literal evaluation of rank one on every marked pair and rank two on every singleton, a separate nonedge-profile predicate, and labelled orbit expansion of the fourteen rooted templates. It examines all \(2^{15}=32768\) six-vertex simple graphs, including exactly \(5789\) triangle-free ones. It confirms that the recurrence, the profile characterization, and the template expansion identify the same \(2292\) labelled graphs, then computes the nine orbit sizes and automorphism counts. The results are recorded in `CENSUS.csv` and in standard output. The exhaustive check is finite; it does not purport to prove the assertion for arbitrary host order.

## Relationship to prior work

López-Callejas and Navarro-Castillo, *A rank function for Fraïssé classes and the rank property* (arXiv:2604.14461v1, first public April 15, 2026), supplies the one-point-extension rank definition and its basic properties. It treats unrestricted finite graphs and explicitly notes that clique-free ages fail its full-extension-property hypothesis; it does not provide the relative rank-three criterion or the present six-vertex census.

The published result *Sharp rank-three onset and six-edge extremum for finite graphs* concerns the **unrestricted graph age**, where an edge pair also has an admissible double-neighbour extension. Its minimum rank-three order is seven and its minimum support is six edges. Those results cannot be transferred to the triangle-free age: an edge pair in the latter has only three admissible types, and the four-edge \(P_5\sqcup K_1\) already has relative rank three although it has smaller unrestricted rank. The comparison explains rather than erases the change in the ambient class.

Bodirsky and Guzmán-Pro, *The Generic Circular Triangle-Free Graph* (2025), characterize a **proper subclass** avoiding \(K_3\), \(K_1\sqcup2K_2\), \(K_1\sqcup C_5\), and \(C_6\). Their embedding and circular-colouring statements neither characterize the rank relative to *all* triangle-free graphs nor yield the nine rank-boundary shapes here. In particular, the present nine-shape list contains both \(K_1\sqcup C_5\) and \(C_6\), explicitly excluded by their theorem.

## Limitations

This is a characterization of **rank at least three relative to the triangle-free age**, not of unrestricted graph rank or of quantifier rank of first-order sentences. It does not classify the ranks four and higher and does not imply the Rank Property for the Henson age. The nine-graph list and exact counts are fully finite and supported by reproducible enumeration, whereas their novelty relative to all historical literature cannot be certified by searches alone. The present review is not independent external validation.

## References

1. C. López-Callejas and J. Navarro-Castillo, *A rank function for Fraïssé classes and the rank property*, arXiv:2604.14461v1, 2026-04-15, https://arxiv.org/html/2604.14461v1 .
2. *Sharp rank-three onset and six-edge extremum for finite graphs*, published mathematical result, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-sharp-rank-three-onset-and-six-edge-extremum-for-finite-graphs--a3c35b6162f1 .
3. M. Bodirsky and S. Guzmán-Pro, *The Generic Circular Triangle-Free Graph*, *Journal of Graph Theory* 109 (2025), 426–445, https://doi.org/10.1002/jgt.23235 .
4. W. Kubiś and S. Shelah, *Evolution systems—an ordinal rank measuring universality* (2024), https://users.math.cas.cz/kubis/pdfs/ranksEvasPS_ver2.pdf .
