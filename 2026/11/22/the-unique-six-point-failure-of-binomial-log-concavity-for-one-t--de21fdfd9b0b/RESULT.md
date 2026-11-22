# The unique six-point failure of binomial log-concavity for one-types in the four-clique-free homogeneous graph

## Finding
Let \(\mathcal H_4\) be the countable homogeneous universal graph omitting \(K_4\). For an individually named finite induced base graph \(G\subset\mathcal H_4\) with \(n\) vertices, let \(f_k(G)\) be the number of complete nonalgebraic one-point types over \(G\) having exactly \(k\) adjacencies to the base, where \(0\le k\le n\). Put
\[
 b_k(G)=\frac{f_k(G)}{\binom nk}\qquad(0\le k\le n).
\]
Then \(b_k(G)^2\ge b_{k-1}(G)b_{k+1}(G)\) for all \(1\le k<n\) whenever \(n\le5\). For \(n=6\), the inequality fails for exactly one isomorphism class of allowed bases: the pentagonal wheel \(W=K_1\vee C_5\). All six-point failures occur at \(k=4\), and there are precisely \(72\) labelled failing graphs on a fixed six-element vertex set. For the wheel,
\[
 \sum_{k=0}^6f_k(W)z^k=1+6z+15z^2+15z^3+5z^4+z^5,
\]
and the exact reversed inequality is
\[
 b_3(W)b_5(W)-b_4(W)^2=\frac1{72}>0.
\]
The adjective *binomial* always refers to normalization by the ambient parameter count \(n\), including trailing zero coefficients. No statement here uses normalization by the degree of the enumerating polynomial.

## Assumptions and scope
Graphs are finite simple undirected graphs. The graph \(\mathcal H_4\) is the Fraïssé limit of finite \(K_4\)-free graphs in the pure adjacency language. The base \(G\) is induced and its vertices are named individually. A nonalgebraic one-point type is required to specify a fresh vertex different from every named vertex. Homogeneity and quantifier elimination imply that these types are exactly the allowed adjacency/nonadjacency assignments to the named vertices. The integer \(n\) is the number of named base vertices, not the largest allowed neighborhood size. The wheel has one universal hub and a five-cycle rim; the hub and any two adjacent rim vertices form its five triangles.

## Proof
**Type-to-face bijection.** Each potential one-point type corresponds to a vertex subset \(S\subseteq V(G)\), declaring the new point adjacent exactly to \(S\). The expanded graph remains \(K_4\)-free if and only if \(G[S]\) is triangle-free: a new \(K_4\) must consist of the new vertex and an old triangle, and conversely every old triangle in \(S\) creates such a clique. By the extension and homogeneity properties of \(\mathcal H_4\), every admissible diagram is realized by a fresh vertex, and distinct \(S\)'s yield distinct complete types. Thus \(f_k\) is the number of size-\(k\) faces of the triangle-free vertex complex \(\mathrm{CF}_3(G)\).

**Exact finite classification.** A stand-alone, exhaustive labelled graph enumeration is supplied as `VERIFY.py`, with its actual recorded output in `VERIFY.out`. For each \(n=0,1,\dots,6\), it enumerates every one of the \(2^{\binom n2}\) possible edge masks, excludes exactly those containing a four-clique, lists every triple that is a triangle, and enumerates every one of the \(2^n\) vertex subsets to obtain the exact integer vector \((f_0,\ldots,f_n)\). It tests each binomial-log-concavity inequality by cross-multiplication using integer binomial coefficients. No sampled graphs or floating-point comparisons occur. The numbers of labelled \(K_4\)-free graphs at orders \(0,1,2,3,4,5,6\) are respectively \(1,1,2,8,63,958,27626\). The numbers violating at least one inequality are respectively \(0,0,0,0,0,0,72\). Every one of the 72 exceptions has sorted degree sequence \((3,3,3,3,3,5)\), coefficient vector \((1,6,15,15,5,1,0)\), and exactly the failing index \(k=4\).

**Uniqueness without an isomorphism oracle.** A simple six-vertex graph of degree sequence \((3,3,3,3,3,5)\) has one universal vertex and five remaining vertices of induced degree two. A two-regular simple graph on five vertices must be a single five-cycle, since every component of a simple two-regular graph is a cycle of length at least three. Hence every enumerated violating graph is isomorphic to \(K_1\vee C_5\). Conversely, there are \(6\) choices of the hub and \(5!/10=12\) distinct labelled cycles on the remaining five vertices, giving precisely \(72\) labelled wheels.

**Exact witness calculation.** A triangle-free subset of the wheel either omits the hub, giving an arbitrary rim subset and generating function \((1+z)^5\), or contains the hub, in which case its rim subset must be independent in \(C_5\), giving \(z(1+5z+5z^2)\). Therefore the displayed coefficient vector follows. At degrees \(3,4,5\), the binomially normalized values are respectively \(3/4,1/3,1/6\), and \((3/4)(1/6)-(1/3)^2=1/72\). This establishes the strict obstruction.

## Verification
Run `python3 VERIFY.py` in a standard Python 3 environment; no external Python package, network connection, database or separate source file is needed. The exact last line is `EXHAUSTIVE_K4_FREE_BINOMIAL_THRESHOLD_OK`. The checker independently enumerates the wheel's finite induced diagrams in a second routine using explicit edge membership and combinations. Its assertions confirm the six labelled-graph census totals, the uniqueness certificate, the failing index, the wheel polynomial and the rational gap.

## Relationship to prior work
The homogeneous \(K_n\)-free graphs and their quantifier-eliminating type descriptions are classical; Gabriel Conant's 2014 manuscript [1, Section 3] provides explicit background on realization of finite \(K_n\)-free diagrams. The triangle-free vertex complex \(\mathrm{CF}_3(G)\) is not a new construction; Ghosh and Selvaraja [2] define general \(t\)-clique-free complexes and analyze shellability, not this normalized rank-sequence threshold. The published Shrikhande complex calculation [3] concerns homotopy of a particular sixteen-vertex complex, not the small-base binomial log-concavity classification. Xie and Xu [4] study ultra-log-concavity of *dependence polynomials*, where forbidden patterns are graph edges; here admissible sets exclude triangular cliques of a \(K_4\)-free graph. Their results therefore do not imply this six-point threshold or its equality classification. The novelty claim is confined to the complete sharp threshold for the specified model-theoretic type enumerator and ambient normalization, not to the established concept of ultra-log-concavity or clique-free complexes.

## Limitations
The proof classifies every permitted base through six named vertices, not larger bases. It establishes a failure at six, not a statement that the normalized coefficients must fail for every larger base or every wheel. A mathematical equivalence under another name or an unindexed old table could predate this formulation; the literature comparison is not an independent priority certification. The type-frequency distribution is a uniform count over complete logical types, not a probability law on randomly chosen vertices of \(\mathcal H_4\). The unnormalized coefficient sequence for the wheel is log-concave; only the stronger binomially normalized inequality fails. Independent audit has not been performed.

## References
1. Gabriel Conant, *Forking and dividing in Henson graphs*, arXiv:1401.1570v1, first public version 2014-01-08, https://arxiv.org/html/1401.1570v1.
2. Rakesh Ghosh and S. Selvaraja, *Shellability in Clique-Free Complexes of Graphs*, arXiv:2602.09623v1, first public version 2026-02-10, https://arxiv.org/html/2602.09623v1.
3. *Nine six-spheres in the triangle-free vertex complex of the Shrikhande graph*, published mathematical research record, 2026-11-01, https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-nine-six-spheres-in-the-triangle-free-vertex-complex-of-the-shri--d41d15ef6445.
4. Yan-Ting Xie and Shou-Jun Xu, *Ultra log-concavity and real-rootedness of dependence polynomials*, arXiv:2408.09152v1, first public version 2024-08-17, https://arxiv.org/abs/2408.09152; version 2 inspected at https://arxiv.org/html/2408.09152v2.
