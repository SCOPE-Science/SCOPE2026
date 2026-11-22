# Exact one-point-extension ranks of countable matchings and their finite census

## Finding

Let \(\mathcal M\) be the hereditary class of finite simple graphs of maximum degree at most one, with induced embeddings, and let \(\operatorname{rk}_X(F)\) be the one-point-extension rank relative to \(\mathcal M\). For every countable \(X\in\sigma\mathcal M\) and finite marked induced subgraph \(F\subseteq X\), write \(c_X(F)\) for the number of edges of \(X\) with both endpoints outside \(F\), and \(d_X(F)\) for the number of isolated vertices of \(X\) outside \(F\). Counts may be infinite. Then the exact relative rank is

\[
\operatorname{rk}_X(F)=
\begin{cases}
0,&F\text{ contains a vertex isolated in }X,\\
\infty,&F\text{ contains no such vertex and }c_X(F)=\infty,\\
c_X(F)+\mathbf1_{\{d_X(F)>0\}},&\text{otherwise}.
\end{cases}
\]

In particular, if \(p\) is the number of edge components and \(d\) the number of isolated vertices of \(X\), the unmarked rank is \(\infty\) exactly when \(p=\infty\); otherwise it is \(p+\mathbf1_{\{d>0\}}\). Thus the countable rank spectrum of \(\mathcal M\) is exactly \(\mathbb N_0\cup\{\infty\}\). In this natural Fraïssé class, no rank between \(\omega\) and \(\infty\) occurs, so the class does not have the Rank Property.

For finite labelled hosts, if \(a_{n,r}\) is the number of matching graphs on \(n\) named vertices with rank \(r\), then

\[
\sum_{n,r\ge0}a_{n,r}\frac{x^n}{n!}z^r=
\left(1+z(e^x-1)\right)e^{z x^2/2}.
\]

For every integer \(r\ge1\), the unique unlabelled smallest host of rank \(r\) is \((r-1)K_2\sqcup K_1\), of order \(2r-1\); its number of distinct labellings is \((2r-1)!/(2^{r-1}(r-1)!)\). The maximum rank on \(n\ge1\) vertices is \(\lfloor(n+1)/2\rfloor\).

## Assumptions and scope

Graphs are simple, undirected and loopless; the empty graph is allowed. The signature contains just adjacency, and all embeddings are induced. The ambient extension class is **only** finite graphs with maximum degree at most one; the rank is not the rank obtained by allowing all finite graphs as prime extensions. For every finite \(F\subseteq X\), \(\operatorname{rk}_X(F)\ge0\), and for each ordinal \(\alpha\), \(\operatorname{rk}_X(F)\ge\alpha+1\) precisely when every isomorphism type of one-new-vertex extension of \(F\) in \(\mathcal M\) has a realization in \(X\) over the fixed marked vertices with rank at least \(\alpha\). Limit ranks follow the usual intersection of preceding stages. The empty structure defines \(\operatorname{rk}(X)=\operatorname{rk}_X(\varnothing)\).

A marked vertex is *bad* if it is isolated in the full host \(X\), irrespective of the adjacency seen inside \(F\). Every other vertex of \(F\) is either already paired to its mate inside \(F\), or has its unique mate outside \(F\). The quantity \(c_X(F)\) counts only whole unmarked edges, not dangling mates of marked vertices; these are excluded from fresh-vertex realizations by their adjacency to \(F\).

## Proof

**Extension dichotomy.** Given an arbitrary induced finite marked matching \(F\), a permitted new vertex has either no neighbours in \(F\) (the *fresh* type), or is adjacent to precisely one vertex of \(F\) that currently has degree zero inside \(F\) (the *mate* type for that vertex). No other one-point extension belongs to \(\mathcal M\).

If \(F\) contains a bad vertex, the mate extension for that vertex has no realization in \(X\): the bad vertex has no neighbour anywhere in \(X\). Hence \(\operatorname{rk}_X(F)=0\), even when infinitely many free edges remain elsewhere.

Suppose now that \(F\) contains no bad vertex. Every mate extension is realizable by choosing the unique previously unused mate, and this does not change \(c_X(F)\) or \(d_X(F)\). A fresh extension is realizable only by choosing an endpoint of a wholly unused edge, or an isolated unused vertex. Choosing an edge endpoint decreases \(c_X(F)\) by one and creates a newly marked vertex with an available mate; choosing an isolated vertex creates a bad marked vertex and therefore gives rank zero. If there are no whole unused edges and no unused isolated vertices, the fresh extension has no realization and the rank is zero.

**Lower bound for finite resources.** Assume \(c=c_X(F)<\infty\) and put \(r=c+\mathbf1_{\{d_X(F)>0\}}\). We prove by induction on \(t\in\mathbb N_0\), uniformly over all such marked positions, that every position without bad vertices and with \(r\ge t\) has rank at least \(t\). The case \(t=0\) is immediate. For \(t\ge1\), all mate types can be realized without changing \(c,d\), leaving resource at least \(t-1\). For a fresh extension, if \(c>0\), choose an endpoint of a wholly unused edge; the new resource is exactly \(r-1\ge t-1\). If \(c=0\), then \(r\ge t\ge1\) implies \(d>0\) and \(t=1\); an unused isolated vertex realizes the fresh type with the required successor rank at least zero. Thus every extension has a realization of rank at least \(t-1\), establishing the induction.

**Upper bound for finite resources.** Induct on the finite number \(c\) of unused whole edges, for all finite marked positions without bad vertices and all finite or countably infinite \(d\). If \(c=0\), the fresh type has no realization when \(d=0\), giving rank zero; if \(d>0\), all its realizations are marked isolated vertices of rank zero, giving rank at most one. Suppose \(c>0\) and let \(r=c+\mathbf1_{\{d>0\}}\). The adversary chooses the fresh type. Its realizations are only unused isolated vertices (rank zero) or endpoints of free edges. In the latter case the successor has \(c-1\) free edges, unchanged \(d\), and no bad vertex; by induction its rank is exactly \(r-1\). Consequently no realization of this fresh type has rank at least \(r\), so the present position fails the successor condition for rank \(r+1\). Combining with the lower bound gives rank exactly \(r\). The argument also handles the empty host and all nonnegative boundary values.

**Infinitely many free edges.** If \(c_X(F)=\infty\) and \(F\) contains no bad marked vertex, the responding player can answer every fresh extension by taking a vertex from a new free edge and every mate extension by taking the designated mate. At every finite stage infinitely many whole edges remain free and no marked isolated vertex has been introduced. This is a winning strategy in the infinite extension game, so the rank is \(\infty\). When the full host has infinitely many edges, this applies to the empty marked set. When the host has finitely many edges, the preceding finite-resource calculation applies to every finite marked set, ruling out nonfinite ordinal ranks.

**Rank spectrum and finite census.** The graph consisting of \(p\) disjoint edges and \(d\) isolated vertices has rank \(p+\mathbf1_{\{d>0\}}\) for finite \(p\). Every nonnegative integer therefore occurs, as does \(\infty\) for countably many disjoint edges; no other rank occurs. The class \(\mathcal M\) has the hereditary, joint-embedding and amalgamation properties: to amalgamate two matching extensions over a finite common induced submatching, identify the two optional mates attached to each shared currently unpaired vertex, and leave other components disjoint. Its countable homogeneous limit is the disjoint union of countably many edges. Accordingly the preceding spectrum proves failure of the Rank Property (realizing every countable ordinal), despite the existence of a Fraïssé limit.

A labelled matching with \(p\) edges and \(d\) isolated vertices on \(n=2p+d\) vertices has \(n!/(2^p p!d!)\) realizations. When \(d=0\), the rank is \(p\); when \(d\ge1\), the rank is \(p+1\). Their two disjoint exponential generating series are \(e^{zx^2/2}\) and \(z(e^x-1)e^{zx^2/2}\), yielding the asserted bivariate formula. The least host of rank \(r\ge1\) has \(r-1\) edges and one isolate, of size \(2r-1\), uniquely up to isomorphism; a host with no isolates requires \(r\) edges and \(2r\) vertices. The maximum rank at order \(n\) is therefore \(\lfloor(n+1)/2\rfloor\).

## Verification

The accompanying \(\texttt{check_matching_ranks.py}\) computes finite ranks directly from the game recursion, enumerating each permitted fresh or mate extension over every marked subset and maximizing over every actual realization in the fixed graph. It does **not** implement the closed formula inside the recursive rank computation. This independent finite procedure was compared with the theorem for all \(51{,}883\) marked positions in the canonical labelled matchings of orders at most \(12\). A separate exhaustive enumeration of all \(3{,}736\) labelled matching graphs of orders at most \(9\) compared their game ranks with the predicted exact rank distribution. Both comparisons passed; the command and summary are given in \(\texttt{VERIFICATION.md}\). This is finite corroboration only; the countable and unrestricted-size claims are proved by the preceding strategy and induction arguments.

## Relationship to prior work

López-Callejas and Navarro-Castillo (first public April 15, 2026) define and investigate the one-point-extension rank in Fraïssé classes, prove Rank Property results for free-amalgamation classes, tournaments, and linear orders, and compute linear-order ranks. Their unrestricted graph results apply to a different extension class; the present exact matching-class rank is not obtained by restricting their graph rank, because changing the allowed one-point extensions changes the game. Their broad results do not supply this matching-specific finite/countable classification or rank census. Kubiś and Shelah's evolution-system rank framework supplies the original general setting, not this exact matching computation.

Equivalence relations with classes of size at most two can encode the same host structures, but this is **not** the rank game on unrestricted equivalence relations: an unrestricted equivalence-class extension may add a third member, which is forbidden here. Similarly, a calculation for arbitrary equivalence relations does not imply the result by taking a special case without also changing the extension class.

## Limitations

Only degree-at-most-one undirected graphs, induced embeddings, and the precisely specified rank game are covered. The bivariate series enumerates finite labelled hosts, not isomorphism classes or the distribution of ranks of all graphs. The countable classification assumes countable hosts; no claim concerns uncountable host structures or ranks in the unrestricted graph age. Historical priority beyond the inspected primary texts and searchable mathematical records is provisional. No independent external mathematical audit is claimed.

## References

1. C. López-Callejas and J. Navarro-Castillo, *A rank function for Fraïssé classes and the rank property*, arXiv:2604.14461, first submitted 2026-04-15, https://arxiv.org/html/2604.14461 . Relevant material: Introduction and Sections 2, 4, and 6.
2. W. Kubiś and S. Shelah, *Evolution systems — an ordinal rank measuring universality*, manuscript dated 2024-08-19, https://users.math.cas.cz/kubis/pdfs/ranksEvasPS_ver2.pdf . General rank definitions and examples; the text inspection did not identify a matching-class formula.
