# Zero-forcing polynomials of chain graphs with no singleton twin class
## Finding
Let \(G\) be a connected chain graph. Write its canonical open-neighborhood twin classes as \(A_1,\ldots,A_p\) and \(B_1,\ldots,B_p\), ordered so that every vertex of \(A_i\) has neighborhood \(B_1\cup\cdots\cup B_i\), equivalently every vertex of \(B_i\) has neighborhood \(A_i\cup\cdots\cup A_p\). Put \(\alpha_i=|A_i|\), \(\beta_i=|B_i|\), and \(N=\sum_i(\alpha_i+\beta_i)\), and assume \(\alpha_i,\beta_i\ge2\) for every \(i\). Then a set \(S\subseteq V(G)\) is zero forcing if and only if its complement contains at most one vertex from each twin class. Consequently \[\mathcal Z(G;x)=x^{N-2p}\prod_{i=1}^{p}(x+\alpha_i)(x+\beta_i),\] so \(Z(G)=N-2p\), the number of minimum zero forcing sets is \(\prod_i\alpha_i\beta_i\), and every zero of \(\mathcal Z(G;x)\) is real and nonpositive.

The characterization is exact: it describes every zero forcing set, not only the minimum ones. The factorization therefore gives every coefficient of the zero-forcing polynomial at once.

## Assumptions and scope
The graph is finite, simple, connected, bipartite, and a chain graph. Equivalently, the neighborhoods in either bipartition class are linearly ordered by inclusion. Collapse equal open neighborhoods into twin classes and index them so that
\[
N(a)=B_1\cup\cdots\cup B_i\quad\text{for }a\in A_i,
\]
and therefore
\[
N(b)=A_i\cup\cdots\cup A_p\quad\text{for }b\in B_i.
\]
The hypothesis is that every one of these \(2p\) twin classes has size at least two. This condition is structural rather than cosmetic: with singleton twin classes the simple complement criterion can fail, as already happens for the four-vertex path \(P_4\).

A zero forcing process starts from a blue set \(S\); a blue vertex with exactly one white neighbor forces that neighbor blue. The polynomial is
\[
\mathcal Z(G;x)=\sum_{S\text{ zero forcing}}x^{|S|}.
\]

## Proof
First prove necessity. Vertices in the same class \(A_i\), or in the same class \(B_i\), are false twins: they are nonadjacent and have identical open neighborhoods. Suppose two vertices \(u,v\) of one twin class are initially white. As long as both are white, every neighbor of \(u\) is also a neighbor of \(v\), so no blue vertex can have either one as its unique white neighbor. Thus neither \(u\) nor \(v\) can be the first of the pair to be forced. They remain white forever. Hence every zero forcing set leaves at most one white vertex in each twin class.

Conversely, suppose \(S\) leaves at most one white vertex in every class. Since every class has size at least two, each \(A_i\) and each \(B_i\) contains an initially blue vertex.

Force the \(B\)-classes in the order \(B_1,B_2,\ldots,B_p\). When class \(B_i\) is reached, all earlier \(B_j\) with \(j<i\) are already entirely blue. If \(B_i\) contains a white vertex, choose any initially blue vertex of \(A_i\). Its neighborhood is exactly \(B_1\cup\cdots\cup B_i\), so that white vertex is its unique white neighbor and is forced. After this pass all vertices of \(B\) are blue.

Now force the \(A\)-classes in reverse order \(A_p,A_{p-1},\ldots,A_1\). When class \(A_i\) is reached, all later classes \(A_j\) with \(j>i\) are already entirely blue. If \(A_i\) contains a white vertex, choose a blue vertex of \(B_i\). Its neighborhood is exactly \(A_i\cup\cdots\cup A_p\), so the remaining white vertex of \(A_i\) is its unique white neighbor and is forced. Hence every vertex becomes blue, proving sufficiency.

For a twin class of size \(c\), an admissible zero forcing set either contains all \(c\) vertices, contributing \(x^c\), or omits exactly one vertex, with \(c\) choices contributing \(c x^{c-1}\). The choices are independent across the \(2p\) classes, so
\[
\mathcal Z(G;x)=\prod_{i=1}^p\bigl(x^{\alpha_i}+\alpha_i x^{\alpha_i-1}\bigr)
\bigl(x^{\beta_i}+\beta_i x^{\beta_i-1}\bigr)
=x^{N-2p}\prod_{i=1}^p(x+\alpha_i)(x+\beta_i).
\]
The smallest exponent is \(N-2p\), attained by omitting one vertex from every class, which proves \(Z(G)=N-2p\) and gives \(\prod_i\alpha_i\beta_i\) minimum sets. The displayed factorization also gives the asserted real nonpositive zeros.

## Verification
The standalone checker `artifacts/verify_chain_zf_poly.py` constructs canonical chain graphs with \(p\le3\), all twin-class sizes in \(\{2,3,4\}\), and total order at most twelve. For each graph it exhaustively tests all vertex subsets by simulating the zero forcing rule and compares the resulting coefficient vector with the factored formula. It also checks the \(P_4\) singleton-class boundary where the hypothesis is absent. The executed package artifact reported:

`VERIFY_OK graphs=60 subsets=128016 max_order=12 boundary=P4`

This finite computation is a stress test of the statement and boundary conditions; the infinite theorem follows from the proof above.

## Relationship to prior work
The 2008 AIM Minimum Rank--Special Graphs Work Group paper introduced the standard zero forcing parameter. Ross's 2012 paper on difference graphs gives a canonical creation-sequence description of the same graph class also known as chain graphs, exposing the nested-neighborhood blocks used here. Boyer, Brimkov, English, Ferrero, Keller, Kirsch, Phillips, and Reinhart introduced the zero-forcing polynomial and derived closed forms for several graph families, including complete and complete multipartite graphs.

Targeted searches under the aliases chain graph, difference graph, Ferrers graph, nested-neighborhood bipartite graph, false twins, and zero-forcing polynomial did not locate the characterization or factorization above. The closest exact polynomial result located is the complete-multipartite formula. When \(p=1\), the present theorem is the complete bipartite specialization
\[
x^{\alpha_1+\beta_1-2}(x+\alpha_1)(x+\beta_1),
\]
which agrees with that known formula; the staircase case \(p>1\) is not implied by complete multipartite structure.

The chain-graph structural source and the zero-forcing-polynomial source supply the two established ingredients, while the accepted claim is the exact sufficiency of the twin-class complement condition and the resulting factorization for the no-singleton-twin subclass.

## Limitations
The theorem requires every canonical twin class to have at least two vertices. It does not claim a formula for arbitrary chain graphs with singleton classes, where additional interactions occur. The exhaustive checker reaches order twelve and is corroborative rather than a proof. Literature searching was targeted across the principal aliases, not logically exhaustive, and older difference/Ferrers literature remains a residual originality risk.

## References
1. AIM Minimum Rank--Special Graphs Work Group, “Zero forcing sets and the minimum rank of graphs,” *Linear Algebra and its Applications* 428 (2008), 1628--1648, DOI: 10.1016/j.laa.2007.10.009. Published 1 April 2008.
2. C. Ross, “Properties of Random Difference Graphs,” *Electronic Journal of Combinatorics* 19(4) (2012), P28, DOI: 10.37236/2354. Published 22 November 2012.
3. K. Boyer, B. Brimkov, S. English, D. Ferrero, A. Keller, R. Kirsch, M. Phillips, and C. Reinhart, “The zero forcing polynomial of a graph,” arXiv:1801.08910, first submitted 26 January 2018.
