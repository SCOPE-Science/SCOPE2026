# Exact mutual-nearest-neighbor component law in symmetric random-link graphs

## Finding
For a complete graph with independent, identically distributed, atomless real-valued edge weights shared by the two endpoints, each vertex points toward its incident edge of minimum weight. Let \(X_n\) count weak components of the resulting directed nearest-neighbor network on \(n\ge2\) labelled vertices. Then for every specified matching \(M\) of \(k\) edges, with \(0\le k\le \lfloor n/2\rfloor\),
\[
\Pr(\text{every edge of }M\text{ is a mutual-nearest-neighbor pair})=
\prod_{j=1}^k\frac1{2n-2j-1}. \tag{1}
\]
In particular, the complete finite distribution is determined by
\[
\mathbb E[z^{X_n}]=\sum_{k=0}^{\lfloor n/2\rfloor}
\frac{n!}{2^k k!(n-2k)!\prod_{j=1}^k(2n-2j-1)}(z-1)^k. \tag{2}
\]
The first two moments and their ratio satisfy
\[
\mathbb E X_n=\frac{n(n-1)}{2(2n-3)},\qquad
\operatorname{Var}(X_n)=\frac{n(n-1)(n-2)(n-3)}{2(2n-5)(2n-3)^2}\quad(n\ge3), \tag{3}
\]
\[
\frac{\operatorname{Var}(X_n)}{\mathbb E X_n}=\frac{(n-2)(n-3)}{(2n-5)(2n-3)}\longrightarrow\frac14. \tag{4}
\]
The number of mutual-nearest-neighbor pairs is therefore universally underdispersed, despite positive correlation between two specified vertex-disjoint pair events. The mean (the one-pair case) and the extreme probability of all vertices forming mutual pairs were known; the contribution is the complete simultaneous-pair and component-count law, including its variance.

## Assumptions and scope
\(n\) is an arbitrary integer at least \(2\). All \(\binom n2\) edge weights are independent, with the same atomless distribution; the weight is undirected and identical for each endpoint. Ties have probability zero. The law depends only on the uniform edge ranking, not on the common continuous weight distribution. Components refer to the underlying undirected graph of the directed nearest-neighbor mapping. Empty products equal \(1\). Equations (1) and (2) hold also at \(n=2\); equation (3)'s displayed variance is stated for \(n\ge3\) and at \(n=2\), \(X_2=1\) deterministically.

## Proof
**Cycles and components.** Every vertex has exactly one outgoing arrow. If a directed cycle had length at least three, comparing the weights of the outgoing and incoming incident edges at successive cycle vertices would give a strict cyclic chain of inequalities, an impossibility. Hence all cycles have length two. In any finite functional digraph, each weak component has exactly one directed cycle; thus \(X_n\) is exactly the count of reciprocal nearest-neighbor edges.

**Simultaneous-pair probability.** Fix a matching \(M=\{e_1,\ldots,e_k\}\). By the probability-integral transformation, the edge weights may be taken to be independent uniform variables on \([0,1]\) without changing any event. Let \(x_i\) be the weight of the selected matching edge \(e_i\). Conditional on these weights, all other edges incident to either endpoint of \(e_i\) must be larger than \(x_i\). Each selected pair has \(2(n-2k)\) edges to vertices outside the matching. There are exactly four edges between each two distinct selected pairs, which all must exceed the greater of their two selected weights. Since the integrand is symmetric, restrict to \(0<x_1<\cdots<x_k<1\) and multiply by \(k!\). The event probability becomes
\[
 k!\int_{0<x_1<\cdots<x_k<1}\prod_{i=1}^k
 (1-x_i)^{2(n-2k)+4(i-1)}\,dx_1\cdots dx_k. \tag{5}
\]
Put \(t_i=-\log(1-x_i)\), with \(0<t_1<\cdots<t_k\), and \(u_l=t_l-t_{l-1}\) for \(t_0=0\). Then the exponent is \(-\sum_{l=1}^k u_l B_l\), with
\[
 B_l=\sum_{i=l}^k(2(n-2k)+4(i-1)+1)
 =(k-l+1)(2n-2(k-l+1)-1).
\]
The positive \(u_l\) integrate independently, giving
\[
 k!\prod_{l=1}^k B_l^{-1}
 = k!\prod_{j=1}^k[j(2n-2j-1)]^{-1}
 =\prod_{j=1}^k(2n-2j-1)^{-1},
\]
which proves (1). The case \(k=0\) is immediate.

**Distribution and variance.** In any outcome, the number of \(k\)-subsets of reciprocal pairs is \(\binom{X_n}k\). There are exactly \(n!/(2^k k!(n-2k)!)\) matchings of size \(k\), so linearity of expectation and (1) give
\[
 \mathbb E\binom{X_n}k=
 \frac{n!}{2^k k!(n-2k)!\prod_{j=1}^k(2n-2j-1)}. \tag{6}
\]
Expand \(z^{X_n}=(1+(z-1))^{X_n}\) and take expectations to obtain (2). In particular,
\[
 \mathbb E[X_n(X_n-1)]=\frac{n(n-1)(n-2)(n-3)}{4(2n-3)(2n-5)}
 \quad(n\ge4).
\]
For \(n=3\), the left side is zero, and the right side is zero. Subtracting the square of the mean from this factorial moment plus the mean gives (3). The Fano ratio (4) follows by division. In addition, for two disjoint specified candidate pair edges (\(n\ge4\)) their indicator covariance equals
\[
 \frac1{(2n-3)(2n-5)}-\frac1{(2n-3)^2}
 =\frac2{(2n-3)^2(2n-5)}>0,
\]
whereas overlapping candidate edges are mutually exclusive and have covariance \(-(2n-3)^{-2}\).

## Verification
The standalone script `VERIFY.py`, requiring only the Python standard library, independently enumerates all \(\binom n2\)! strict edge-rank orders for \(2\le n\le5\), computes the exact component-count histogram, and compares it with (2). It also checks the binomial moments, positive coefficients, normalization, variance and Fano factor by exact rational arithmetic for \(2\le n\le50\). The actual saved checker returned `VERIFY_OK 923 assertions`. The exhaustive finite checks do not establish an infinite theorem; equations (1)–(6) provide the proof for every \(n\ge2\).

## Relationship to prior work
The 2009 deterministic-tourist-walk/random-link analysis gives the marginal one-pair probability (and hence the mean in (3)) but does not state the joint matching probabilities or full component-count law in its inspected sections. Frieze and Pegden (first publicly posted May 4, 2021) analyze spanners of independently weighted complete graphs and motivate nearest-neighbor structures, not the present entire component distribution. In a November 23, 2023 MathOverflow question, Aldous explicitly computed the event that *all* vertices form disjoint mutual-nearest-neighbor pairs: for even \(n=2m\), (2) recovers his published expression
\[
 \Pr(X_{2m}=m)=\frac{(2m-1)!!(2m-3)!!}{(4m-3)!!}.
\]
That extreme event is therefore **not** claimed new. Neither that event nor the single-pair marginal implies the full family of joint moments (6) without an additional argument. This comparison does not establish universal historical priority.

## Limitations
The graph is complete, the edge weights independent and identically distributed, and each unordered pair uses one common weight. The conclusion does not extend without proof to directed independently weighted links, nonidentical edge laws, or geometric metric dependencies. No central limit theorem or higher-dimensional spatial model is proved. Prior literature on related random-link networks is extensive, so a previously unlocated equivalent full-distribution theorem remains possible. Independent external audit has not been carried out.

## References
1. D. Aldous, *Nearest neighbors on random complete graph*, MathOverflow, question and answer dated November 23, 2023. https://mathoverflow.net/questions/458980/nearest-neighbors-on-random-complete-graph
2. A. Frieze and W. Pegden, *Spanners in Randomly Weighted Graphs: Independent Edge Lengths*, preprint publicly posted May 4, 2021. https://arxiv.org/abs/2105.01718
3. R. M. S. González and collaborators, *Deterministic tourist walk* (random-link-model mutual-neighbor calculation), 2009. https://cbpfindex.cbpf.br/publication_pdfs/2009_rodrigo_jcis.2009_08_19_14_18_17.pdf
