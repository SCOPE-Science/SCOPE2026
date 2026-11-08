# Two-colour strong-majority edge colourings of cubic graphs and perfect codes

## Finding

Let \(G\) be any finite, simple, connected cubic graph. Its strong-majority edge colouring is a map \(c:E(G)\to\{\mathrm{red},\mathrm{blue}\}\) such that, for every edge, each named colour occurs on at most half of the other edges incident with either endpoint. Let \(p(G)\) be the number of subsets \(S\subseteq V(G)\) for which \(|N_G[v]\cap S|=1\) for every vertex \(v\). These are **efficient dominating sets**, equivalently perfect radius-one codes.

**Theorem.** There is a canonical bijection between the named two-colour strong-majority edge colourings of \(G\) and pairs \((S,\varepsilon)\), where \(S\) is an efficient dominating set and \(\varepsilon\in\{\mathrm{red},\mathrm{blue}\}\). The colouring associated with \((S,\varepsilon)\) assigns colour \(\varepsilon\) to precisely the edges meeting \(S\), and the other colour to all remaining edges. Consequently, if \(b_2(G)\) counts named two-colour strong-majority edge colourings, then

\[
b_2(G)=2p(G),\qquad
\operatorname{Maj}'(G)=2\quad\Longleftrightarrow\quad
\gamma(G)=\frac{|V(G)|}{4}.
\]

Here \(\gamma(G)\) is ordinary domination number, and \(\operatorname{Maj}'(G)\) is the minimum number of colours in a strong-majority edge colouring. In particular, two-colour strong-majority edge colourability forces \(|V(G)|\equiv0\pmod4\), and the colourings can be enumerated by enumerating perfect codes.

As an explicit infinite-family consequence, the circular ladder \(C_m\square K_2\), for every integer \(m\ge3\), has eight named two-colour strong-majority edge colourings when \(4\mid m\) and none otherwise. This consequence is an illustration of the general theorem; the corresponding minimum-dominating-set configurations in prisms have independently been studied.

## Assumptions and scope

All graphs are finite, simple, undirected and connected, and every vertex has degree exactly three. An edge \(e=uv\) is adjacent to exactly four other edges: the two other edges at \(u\) and the two other edges at \(v\). The colours are **named**; swapping them produces a distinct colouring. Neither proper edge colouring nor balanced colour incidence at an individual vertex is assumed. A dominating set \(D\) meets every closed neighbourhood \(N_G[v]\); a perfect code \(S\) meets each such neighbourhood in exactly one vertex. The theorem does not claim a formula for \(p(G)\) on all cubic graphs.

## Proof

**1. Local edge equations.** Fix a named two-colour strong-majority edge colouring \(c\). Write \(r(v)\in\{0,1,2,3\}\) for the number of red edges incident with \(v\). The four edges adjacent to any fixed edge must contain exactly two red and two blue edges, because each colour can occur on at most two. If \(uv\) is red, its red adjacent-edge count is \(r(u)+r(v)-2\), so

\[
r(u)+r(v)=4\qquad\text{for red }uv.
\]

If \(uv\) is blue, the red adjacent-edge count is \(r(u)+r(v)\), so

\[
r(u)+r(v)=2\qquad\text{for blue }uv.
\]

Thus every red edge joins vertex types \((1,3)\), \((2,2)\), or \((3,1)\), and every blue edge joins types \((0,2)\), \((1,1)\), or \((2,0)\).

**2. Connectivity dichotomy.** Put \(A=\{v:r(v)\in\{0,2\}\}\) and \(B=\{v:r(v)\in\{1,3\}\}\). The exhaustive edge-type list shows that no edge joins \(A\) to \(B\). Because \(G\) is connected, exactly one of these sets equals \(V(G)\). If \(A=V(G)\), let \(S=\{v:r(v)=0\}\). Every vertex of \(S\) has three blue edges to vertices of type two; every type-two vertex has one blue edge, whose other endpoint must have type zero. No two vertices of \(S\) are adjacent. Hence \(S\) is an efficient dominating set and exactly the edges meeting \(S\) are blue. If \(B=V(G)\), use \(S=\{v:r(v)=3\}\). All its incident edges are red; every type-one vertex has exactly one red edge to \(S\). Again \(S\) is an efficient dominating set, and the edges meeting \(S\) are exactly the red ones.

This also shows that \(S\) is **uniquely recoverable** from \(c\): in the first case it is the type-zero class; in the second, the type-three class. The common colour of edges incident to its vertices determines \(\varepsilon\). There is therefore no double counting between the two cases or between different codes.

**3. Converse construction.** Let \(S\) be an efficient dominating set and choose a named colour \(\varepsilon\). Since each \(v\notin S\) has exactly one neighbour in \(S\), and \(S\) is independent, give colour \(\varepsilon\) to the edges incident to \(S\), and give the opposite colour to other edges. An edge meeting \(S\) has two other incident edges of colour \(\varepsilon\) at its code endpoint and two opposite-colour edges at its non-code endpoint. An edge not meeting \(S\) has, at each endpoint, exactly one other \(\varepsilon\)-coloured edge and one other opposite-colour edge. In both cases its four neighbouring edges split two-and-two. The construction meets the strong-majority condition and is inverse to Step 2, proving \(b_2(G)=2p(G)\).

**4. Domination number.** Every closed neighbourhood in a cubic graph has exactly four vertices. Thus every dominating set \(D\) obeys \(4|D|\ge|V(G)|\). Equality means the closed neighbourhoods of vertices of \(D\), whose union is all of \(V(G)\), have no overlap, so \(D\) is an efficient dominating set. Conversely, an efficient dominating set has cardinality \(|V(G)|/4\). Finally, one colour cannot be strong-majority on a cubic graph, since all four edges adjacent to each edge would have that colour. Hence \(\operatorname{Maj}'(G)=2\) precisely in the domination-equality case.

**5. Circular-ladder illustration.** Index the vertices of \(C_m\square K_2\) by \((i,t)\), where \(i\in\mathbb Z/m\mathbb Z\), \(t\in\{0,1\}\), \(m\ge3\). For a perfect code put \(a_i=\mathbf1_{(i,0)\in S}\), \(b_i=\mathbf1_{(i,1)\in S}\), and \(s_i=a_i+b_i\). Requiring exactly one code vertex in each closed neighbourhood gives

\[
a_{i-1}+a_i+a_{i+1}+b_i=1,\qquad
b_{i-1}+b_i+b_{i+1}+a_i=1.
\]

Adding yields \(s_{i-1}+2s_i+s_{i+1}=2\), so \(s_i\) cannot be two; it must alternate between zero and one. Thus \(m\) is even and precisely every other column contains one code vertex. At each empty column, the top and bottom equations force its two adjacent occupied columns to choose opposite rows. The row choices along the \(m/2\) occupied columns therefore alternate, which is possible precisely when \(4\mid m\). If \(4\mid m\), there are exactly two choices of column parity and two choices of initial row, hence four perfect codes, giving eight named colourings. Otherwise there are none.

## Verification

The accompanying standard-library-only program `verify.py` checks the original definitions without using the theorem as its admissibility predicate. One enumeration tests every named binary edge colouring and checks, for every edge, that exactly two of its four adjacent edges have each colour. A separate enumeration tests every candidate vertex set of size one quarter of the vertices against every closed neighbourhood. The script then constructs the predicted colourings from the codes and compares the two full sets, not only their cardinalities.

It tests complete and complete-bipartite examples, the Petersen graph, several circular and Möbius ladders, and deterministically generated connected cubic graphs through twelve vertices. It also independently enumerates perfect codes on circular ladders for \(3\le m\le12\). Run with `python3 verify.py`; no external Python packages are required. These are finite consistency checks, not a proof of the statement for arbitrary order.

## Relationship to prior work

Kalinowski, Kamyczura, Pilśniak and Woźniak introduced strong-majority edge colouring in 2026 [1]. Antoniuk, Prorok and Salia [2] and Pękała and Przybyło [3] developed general small-colour upper bounds, which neither require nor characterize exactly two colours on cubic graphs. The 2024 neighbourhood-balanced-colouring literature [4] concerns balanced vertex colourings; a two-colour strong-majority edge colouring of cubic \(G\) is exactly a neighbourhood-balanced vertex colouring of the four-regular line graph \(L(G)\). The cited paper does not state the cubic-line-graph perfect-code correspondence. Perfect codes in cubic vertex-transitive graphs were previously studied independently [5]. A separately indexed 2026 result gives the strong-majority index of complete graphs, including the \(K_4\) special case, which is covered here rather than claimed as a new special example. Existing prism domination enumerations also cover aspects of the illustration; no novelty is claimed for the prism domination count itself.

The claimed new content is the all-connected-cubic structural equivalence, its canonical two-to-one counting correspondence, and its exact domination-equality characterization. A historical-priority search is not a proof of originality.

## Limitations

Connectedness is essential to the stated canonical two-to-one count: for disconnected cubic graphs, the argument applies independently on each component and colour orientations can vary by component. The theorem does not compute the number of perfect codes on arbitrary cubic graphs, and it does not resolve strong-majority indices three or four for graphs without a perfect code. The related original and published sources were compared to the extent accessible; priority and complete bibliography coverage need independent checking. No external mathematical audit has been performed.

## References

1. R. Kalinowski, M. Kamyczura, M. Pilśniak, and M. Woźniak, *Strong majority colorings of graphs* (first submitted 2026-05-22), arXiv:2605.23828v1, https://arxiv.org/abs/2605.23828.
2. S. Antoniuk, M. Prorok, and N. Salia, *Strong Majority Edge-Coloring* (2026-06-30), arXiv:2607.00212v1, https://arxiv.org/abs/2607.00212.
3. P. Pękała and J. Przybyło, *On Strong Majority Edge Colourings with Few Colours* (2026-08-04), arXiv:2608.04122, https://arxiv.org/abs/2608.04122.
4. B. Freyberg and A. Marr, *Neighborhood Balanced Colorings of Graphs*, Graphs and Combinatorics **40**, 41 (2024), https://doi.org/10.1007/s00373-024-02766-9.
5. *Efficient domination in cubic vertex-transitive graphs*, European Journal of Combinatorics **33** (2012), 1755–1764, https://doi.org/10.1016/j.ejc.2012.04.007.
6. *Exact Dominion of the Prism Graph: Enumeration by Congruence Class via Cyclic Words* (2026), https://doi.org/10.1155/ijmm/1411005.
