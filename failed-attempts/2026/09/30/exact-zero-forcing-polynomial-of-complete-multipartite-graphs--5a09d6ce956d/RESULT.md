# Exact zero forcing polynomial of complete multipartite graphs
## Finding
Let \(G=K_{n_1,\ldots,n_r}\) be a complete multipartite graph with \(r\ge2\), positive part sizes \(n_i\), and order
\[
N=\sum_{i=1}^r n_i.
\]
Let \(s\) be the number of singleton parts, and write
\[
C(G)=\sum_{1\le i<j\le r} n_i n_j-\binom{s}{2}.
\]
If every part is a singleton, so \(G=K_N\), then its zero forcing polynomial is
\[
\mathcal Z(G;x)=N x^{N-1}+x^N.
\]
Otherwise,
\[
\boxed{\mathcal Z(G;x)=C(G)x^{N-2}+N x^{N-1}+x^N.}
\]
Equivalently, when at least one part is non-singleton, the zero forcing sets are exactly the complements of: the empty set; one vertex; or two vertices in distinct parts with at least one of those two parts non-singleton. In particular,
\[
Z(G)=N-2
\]
and the number of minimum zero forcing sets is exactly \(C(G)\).

## Assumptions and scope
All graphs are finite, simple, and undirected. The graph is assumed connected, hence \(r\ge2\). A zero forcing process begins with a set \(B\subseteq V(G)\) of blue vertices and the remaining vertices white. A blue vertex with exactly one white neighbor may force that neighbor blue. The set \(B\) is zero forcing if repeated legal forces eventually make every vertex blue.

The zero forcing polynomial is
\[
\mathcal Z(G;x)=\sum_{k=1}^{N}z(G;k)x^k,
\]
where \(z(G;k)\) is the number of zero forcing sets of cardinality \(k\).

## Proof
Fix an initial blue set \(B\), and let \(W=V(G)\setminus B\) be its white complement.

Suppose first that \(|W|\ge3\). If a first force is possible from a blue vertex \(v\) in part \(V_i\), then the white neighbors of \(v\) are precisely \(W\setminus V_i\). Hence a force requires
\[
|W\setminus V_i|=1.
\]
After that unique white vertex outside \(V_i\) is forced, at least two white vertices remain, all in \(V_i\). A blue vertex in \(V_i\) is adjacent to none of them, while every blue vertex outside \(V_i\) is adjacent to all of them. No further force is possible. Thus no zero forcing set can have three or more initially white vertices.

Now suppose \(|W|=2\), say \(W=\{u,v\}\). If \(u\) and \(v\) lie in the same part, every blue vertex outside that part has two white neighbors and every blue vertex inside it has none, so the process is stuck.

Assume instead that \(u\in V_i\) and \(v\in V_j\) with \(i\ne j\). If \(n_i\ge2\), choose a blue vertex \(u'\in V_i\setminus\{u\}\). Its unique white neighbor is \(v\), so \(u'\) forces \(v\). The newly blue vertex \(v\) then has \(u\) as its unique white neighbor and forces it. The same argument applies if \(n_j\ge2\). Conversely, if \(n_i=n_j=1\), then neither of the two white singleton parts contains a blue vertex, while every blue vertex in any other part sees both white vertices. Hence no force is possible. Therefore a two-vertex white set is the complement of a zero forcing set exactly when its vertices lie in distinct parts and at least one of those parts is non-singleton.

If \(|W|=1\), the unique white vertex has a blue neighbor in a different nonempty part because \(r\ge2\), and that neighbor immediately forces it. If \(W=\varnothing\), the set is trivially zero forcing.

This proves the stated classification of all zero forcing sets. There is one zero forcing set with no white vertices and \(N\) choices with one white vertex. For two white vertices, there are
\[
\sum_{i<j}n_i n_j
\]
cross-part pairs in total. Exactly \(\binom{s}{2}\) of them use two singleton parts and therefore fail. Hence the coefficient of \(x^{N-2}\) is \(C(G)\). If every part is singleton, no two-white configuration succeeds and \(G=K_N\), giving only the last two terms. Otherwise at least one admissible two-white pair exists, so \(Z(G)=N-2\).

## Verification
A standalone exhaustive verifier enumerates every unordered complete-multipartite part-size type of orders \(2\) through \(8\) having at least two parts, then tests every initial blue subset by direct simulation of the zero forcing rule. It checks \(58\) graph types and confirms, coefficient by coefficient, the stated polynomial in every case. The replay also exercises complete graphs, stars, complete bipartite graphs, and multipartite graphs with several singleton and non-singleton parts.

## Relationship to prior work
Boyer, Brimkov, English, Ferrero, Keller, Kirsch, Phillips, and Reinhart introduced the zero forcing polynomial and derived formulas for several graph families in the first public version of arXiv:1801.08910 on 26 January 2018. Complete multipartite graphs have also appeared in later zero-forcing work at the level of the minimum zero forcing number and density of minimum zero forcing sets. The statement here is narrower and counting-oriented: it classifies every zero forcing set of an arbitrary complete multipartite graph and consequently gives its entire zero forcing polynomial in closed form.

Targeted searches for a complete-multipartite zero forcing polynomial, complete-bipartite specializations, and equivalent complement-of-two-vertices descriptions did not locate an equivalent formula. This is therefore a best-of-knowledge originality claim, not a proof that no differently indexed prior equivalent exists.

## Limitations
The theorem concerns standard zero forcing only. It does not assert corresponding formulas for positive-semidefinite, skew, signed, or \(q\)-zero forcing variants. The exhaustive computation is a finite consistency check and is not a formal proof. The literature search cannot exclude an unindexed or differently phrased earlier equivalent.

## References
1. K. Boyer, B. Brimkov, S. English, D. Ferrero, A. Keller, R. Kirsch, M. Phillips, and C. Reinhart, “The zero forcing polynomial of a graph,” arXiv:1801.08910; Discrete Applied Mathematics 258 (2019), 35–48, DOI:10.1016/j.dam.2018.11.033.
2. R. Davila, M. A. Henning, and R. Pepper, “Zero and total forcing dense graphs,” Discussiones Mathematicae Graph Theory 43 (2023), 619–634, DOI:10.7151/dmgt.2389.
