# Strong odd coloring profiles of partially deleted complete bipartite graphs
## Finding
Let \(2\le m\le n\) and \(1\le t<m\) be integers. From the complete bipartite graph \(K_{m,n}\), whose parts are
\[
A=\{a_1,\ldots,a_m\},\qquad B=\{b_1,\ldots,b_n\},
\]
delete the edges \(a_ib_i\) for \(1\le i\le t\), and call the resulting graph \(H_{m,n,t}\). Set \(u=m-t\) and \(v=n-t\); both are positive.

A coloring of \(H_{m,n,t}\) is strong odd if and only if it has all of the following structure:

1. Every vertex incident with a deleted matching edge forms a singleton *within its own bipartition side*.
2. The remaining \(u\) vertices of \(A\), and the remaining \(v\) vertices of \(B\), each split into arbitrary monochromatic blocks of odd cardinality.
3. The only colors reused across the two sides occur on an arbitrary chosen subset of the \(t\) corresponding deleted matched pairs \(\{a_i,b_i\}\); otherwise different blocks receive distinct colors.

Let \(S_{\mathrm{odd}}(w,r)\) be the number of set partitions of a labeled \(w\)-element set into exactly \(r\) nonempty blocks of odd cardinality, and let \((q)_k\) be the falling factorial, equal to zero when \(k>q\) for nonnegative integers \(q\). The number of strong odd vertex colorings using colors drawn from a specified palette of \(q\) colors, allowing colors to remain unused, is the polynomial
\[
P_{m,n,t}^{\mathrm{so}}(q)
=\sum_{r=1}^{u}\sum_{s=1}^{v}
S_{\mathrm{odd}}(u,r)S_{\mathrm{odd}}(v,s)
\sum_{j=0}^{t}\binom{t}{j}(q)_{2t-j+r+s}.
\tag{1}
\]

In particular, with \(\varepsilon_w=1\) for even \(w\), and \(\varepsilon_w=0\) for odd \(w\),
\[
\chi_{\mathrm{so}}(H_{m,n,t})=t+2+\varepsilon_u+\varepsilon_v.
\tag{2}
\]
Every minimum coloring shares the colors on *all* \(t\) deleted matching pairs. On each unmatched side it has one odd-sized color block if the side has odd size, or exactly two odd-sized blocks otherwise. Thus the number of minimum colorings up to relabeling of colors is
\[
M_{m,n,t}
=S_{\mathrm{odd}}(u,1+\varepsilon_u)
 S_{\mathrm{odd}}(v,1+\varepsilon_v),
\tag{3}
\]
and the number of named minimum colorings using a palette of exactly \(\chi_{\mathrm{so}}(H_{m,n,t})\) colors is \(\chi_{\mathrm{so}}(H_{m,n,t})!\,M_{m,n,t}\). Explicitly, for \(w\ge1\),
\[
S_{\mathrm{odd}}(w,1+\varepsilon_w)=
\begin{cases}
1,&w\text{ odd},\\
2^{w-2},&w\text{ even}.
\end{cases}
\tag{4}
\]

There is a sharp one-edge consequence. For even \(n\ge2\), the crown graph \(\operatorname{Cr}_n=K_{n,n}-\{a_ib_i:1\le i\le n\}\) has \(\chi_{\mathrm{so}}(\operatorname{Cr}_n)=2\), whereas restoring the single edge \(a_nb_n\) gives \(H_{n,n,n-1}\) and
\[
\chi_{\mathrm{so}}(H_{n,n,n-1})=n+1.
\tag{5}
\]
Thus inserting one edge can increase the strong odd chromatic number by the unbounded amount \(n-1\).

## Assumptions and scope
All graphs are finite, simple, and undirected. A strong odd coloring \(c:V(G)\to\{1,\ldots,q\}\) is a proper vertex coloring with the following additional property: for every vertex \(x\) and every color \(d\), the number of neighbors of \(x\) colored \(d\) is either zero or odd. The count \(P_{m,n,t}^{\mathrm{so}}(q)\) includes colorings that use fewer than \(q\) colors. The symbol \(\chi_{\mathrm{so}}\) denotes the least number of colors in such a coloring.

The theorem requires \(1\le t< m\le n\). Consequently both bipartition sides have at least one vertex *not* incident with a deleted matching edge. Neither the complete-bipartite endpoint \(t=0\) nor the full crown endpoint \(t=m=n\) is included in Formula (1); the latter is compared separately as a boundary graph.

The ordinary set-partition number \(S_{\mathrm{odd}}\) may be computed without any graph input by
\[
S_{\mathrm{odd}}(0,0)=1,\qquad
S_{\mathrm{odd}}(w,r)=\sum_{\substack{1\le k\le w\\k\text{ odd}}}\binom{w-1}{k-1}S_{\mathrm{odd}}(w-k,r-1)
\quad (w\ge1).
\]
Its exponential generating function for fixed \(r\) is \((\sinh z)^r/r!\).

## Proof
Write \(A_0=\{a_1,\ldots,a_t\}\) and \(B_0=\{b_1,\ldots,b_t\}\) for the vertices incident with deleted edges. Since \(t<n\), there is a vertex \(b_j\) with \(j>t\), adjacent to **every** vertex of \(A\). The strong odd condition at this vertex implies that each color used on \(A\) occurs on an odd number of vertices of \(A\). Symmetrically, because \(t<m\), each color used on \(B\) occurs on an odd number of vertices of \(B\).

Suppose a marked vertex \(a_i\), with \(i\le t\), has the same color as another vertex of \(A\). Its entire color class within \(A\) has odd size at least three. But \(b_i\) is adjacent to all vertices of \(A\) *except* \(a_i\), so it sees that color on a positive even number of neighbors, a contradiction. Thus every \(a_i\) with \(i\le t\) is singleton within \(A\). The symmetric argument makes every \(b_i\), \(i\le t\), singleton within \(B\). Every other side-internal color class consists entirely of unmatched vertices and has odd cardinality. This proves the first two structural conditions.

Properness forbids any color from appearing on both bipartition sides at adjacent vertices. The **only** nonedges between \(A\) and \(B\) are the \(t\) deleted matched pairs. Thus a color can occur on both sides only when it colors exactly \(a_i\) and \(b_i\) for one \(i\le t\). Since all marked vertices are singleton on their respective sides, any subset of the \(t\) pairs may be assigned shared colors, with all remaining color blocks receiving separate colors. This proves necessity of the third condition.

Conversely, every described assignment is proper, because its only shared cross-side colors are on nonadjacent matched pairs. At any unmatched vertex of \(B\), a given color appears in its neighborhood either zero times or precisely as often as it does in \(A\), namely an odd number of times. At a matched \(b_i\), each side-internal \(A\)-color class still contributes an odd multiplicity, except the singleton \(\{a_i\}\), which contributes zero; the parity condition therefore holds. The same argument with the parts exchanged proves the condition at every vertex of \(A\). Hence the three conditions are sufficient.

For fixed block counts \(r\) and \(s\) on the unmatched sides, there are \(S_{\mathrm{odd}}(u,r)S_{\mathrm{odd}}(v,s)\) ways to partition those labeled vertices. Choose \(j\) of the \(t\) matched pairs to share one color, in \(\binom tj\) ways. There are then \(2t-j+r+s\) distinct nonempty color classes. Assigning them distinct colors from a palette of \(q\) colors gives exactly \((q)_{2t-j+r+s}\) colorings. Summing proves (1), with no multiple counting because each coloring reconstructs its blocks and its set of shared pairs uniquely.

The smallest possible number of odd-sized blocks on a nonempty \(w\)-set is \(1\) if \(w\) is odd, and \(2\) if \(w\) is even; both minima are attainable. The minimum number of color classes is therefore attained with \(j=t\), \(r=1+\varepsilon_u\), and \(s=1+\varepsilon_v\), which yields (2) and the optimizer count (3). When \(w\) is even, each partition into two odd blocks arises by choosing an odd subset and identifying it with its complement. There are \(2^{w-1}\) odd subsets, so their unordered-pair count is \(2^{w-2}\). This establishes (4).

Finally, for even \(n\), color all vertices on one side of the full crown with one color and the other side with another. Each vertex has \(n-1\) neighbors, an odd number, so this is a strong odd 2-coloring, and an edge rules out one color. The single restored edge turns the graph into \(H_{n,n,n-1}\), for which \(u=v=1\) and (2) yields \((n-1)+2=n+1\). Equation (5) follows.

## Verification
The bundled standalone checker constructs the edge-deleted bipartite graphs and evaluates the definition at every vertex independently of the block proof. Restricted-growth strings enumerate each unordered partition of the vertex set into color classes exactly once. In 16 parameter triples with \(2\le m\le4\), \(m\le n\le5\), \(1\le t<m\) and \(m+n\le9\), it exhaustively inspects 87,448 set partitions and matches **every** coefficient of the predicted coloring-class profile, as well as the exact minimum and optimizer count. It also enumerates palette assignments for selected small cases and directly verifies 13,795 explicit minimum constructions for \(2\le m\le31\), \(m\le n\le50\). The even-crown one-edge construction is verified through \(n=50\).

Run `python verify.py` from the directory containing the included script. The recorded output is in `verify_output.txt`. Finite checks corroborate the proof but are not used to establish the arbitrary-parameter theorem.

## Relationship to prior work
Kwon and Park introduced strong odd coloring in their 22 January 2024 preprint; their focus is bounds for sparse graphs and planar subclasses. Caro, Petruševski, Škrekovski, and Tuza subsequently proved in Theorem 4.4 the exact **scalar** strong odd chromatic number of complete-by-complete *direct products*. In particular, the full crown graph is \(K_2\times K_n\), so its chromatic number is already covered by their theorem. Their proof also observes that a repeated color inside a row of a complete direct product is forbidden unless the row size is even.

The graphs in the present theorem are a different, **nonregular** graph-operation regime with a **partial**, nonempty matching deleted: \(t<m\). The existence of unmatched vertices forces odd global side-class sizes; combining this with the missing-edge neighborhoods makes every marked vertex a singleton. Neither the 2024 direct-product theorem nor its proof gives the all-colorings profile (1), the new exact value (2) on these irregular graphs, or the unbounded single-edge jump (5). The endpoint crown value is used only as a **known comparator**, not presented as a new discovery.

Targeted literature searches for the same invariant combined with partially deleted matchings, near-complete bipartite graphs, and matching-edge restoration did not locate an existing exact theorem for this family. Nearby literature on *odd* coloring or strong *edge* coloring employs different predicates and is not a coverage source for this result.

## Limitations
The parameter range excludes zero deleted edges and deletion of a matching covering an entire bipartition side. Those endpoints have different permissible color-class structures and require distinct enumerators; the full crown is used only for the one-edge comparison. The result does not enumerate strong odd colorings of arbitrary bipartite graphs or of arbitrary deleted subgraphs of complete bipartite graphs.

Literature searches may miss an unindexed or differently named treatment of these graphs. The exact formula is proved symbolically for all allowed integer parameters; restricted exhaustive checks are not substitutes for that proof.

## References
1. H. Kwon and B. Park, *Strong odd coloring of sparse graphs*, arXiv:2401.11653v1, publicly posted 22 January 2024, https://arxiv.org/abs/2401.11653.
2. Y. Caro, M. Petruševski, R. Škrekovski, and Z. Tuza, *On strong odd colorings of graphs*, arXiv:2410.02336v1, publicly posted 3 October 2024; later Discrete Mathematics 348 (2025), article 114601; https://arxiv.org/abs/2410.02336. In particular, Theorem 4.4.
