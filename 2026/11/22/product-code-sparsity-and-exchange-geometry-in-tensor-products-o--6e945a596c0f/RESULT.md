# Product-code sparsity and exchange geometry in tensor products of bicliques

## Finding

**Theorem.** Fix an integer \(r\geq2\). For each \(1\leq i\leq r\), let \(a_i,b_i\geq2\) be integers, let \(H_i=K_{a_i,b_i}\) have named shores \(A_i,B_i\), and let \(G=\bigotimes_{i=1}^r H_i\) be the simple-graph tensor (categorical/direct) product. Define
\[
B=\prod_{i=1}^r a_i b_i,\qquad s_i=a_i+b_i-2,\qquad N_\varepsilon=\prod_{i=1}^r\begin{cases}a_i,&\varepsilon_i=0,\\ b_i,&\varepsilon_i=1,\end{cases}
\]
for \(\varepsilon\in\{0,1\}^r\). A *total perfect code* is a subset \(C\subseteq V(G)\) for which every vertex has exactly one neighbor in \(C\). An *exchange* changes one selected vertex to one unselected vertex while retaining this property. A *factorwise product code* has the form \(\prod_{i=1}^r\{u_i,v_i\}\) with \(u_i\in A_i\), \(v_i\in B_i\).

1. Every total perfect code contains exactly one vertex of each of the \(2^r\) shore patterns \(\varepsilon\). It has cardinality \(2^r\), and the number of codes is exactly \(B^{2^{r-1}}\).
2. The one-vertex-exchange graph on **all** codes is the Cartesian product \(\square_{\varepsilon\in\{0,1\}^r}K_{N_\varepsilon}\). It is connected and regular of degree \(\prod_i(a_i+b_i)-2^r\), with diameter exactly \(2^r\).
3. Precisely \(B\) codes are factorwise products: their fraction among all codes is \(B^{1-2^{r-1}}\). For two such codes \(C,C'\), with factor choices \((u_i,v_i)\) and \((u'_i,v'_i)\), their exchange distance is
\[
d(C,C')=2^r-\prod_{i=1}^r\bigl(\mathbf1_{u_i=u'_i}+\mathbf1_{v_i=v'_i}\bigr).
\]
Consequently, the least positive distance between factorwise product codes is exactly \(2^{r-1}\). Their distance distribution from **every** fixed factorwise code is: one code at distance zero; \(e_{r-j}(s_1,\dots,s_r)\) codes at distance \(2^r-2^j\) for each \(0\le j\le r-1\); and \(B-\prod_i(a_i+b_i-1)\) codes at distance \(2^r\). Here \(e_t\) denotes the elementary symmetric polynomial of degree \(t\).
4. Every total perfect code can be transformed into a factorwise product code using at most \(2^r-2\) exchanges. This is the **exact covering radius** of the factorwise codes whenever \(a_i,b_i\ge2^{r-1}\) for all \(i\); in particular it is exactly two for every two-factor instance covered by the theorem.

For example, \(K_{2,2}\otimes K_{2,2}\) has \(256\) total perfect codes, of which \(16\) factor, and its exchange graph has \(256\) vertices, degree \(12\), and diameter \(4\). Its factorwise codes have covering radius two and distance multiplicities \(1,4,4,7\) at distances \(0,2,3,4\).

## Assumptions and scope

All graphs are finite, simple and labelled; the two shores of each complete bipartite factor are distinguished. The tensor product uses **simultaneous adjacency in every factor**, not the Cartesian graph product. Codes are vertex subsets, not ordered tuples; vertices are distinct when any coordinate differs. Exchanges are single removals and insertions with unchanged set size, and graph distance means shortest exchange-path length. Counts therefore refer to labelled subsets. The theorem does not claim a covering-radius equality for smaller shores when \(r\ge3\).

## Proof

**Components and enumeration.** Each product vertex has a unique shore pattern \(\varepsilon\in\{0,1\}^r\), determined by whether its \(i\)th coordinate is in \(A_i\) or \(B_i\). Two product vertices are adjacent if and only if their patterns are complementary, since every cross-shore pair is adjacent in each complete bipartite factor. Thus, for every complementary pair \(\{\varepsilon,\bar\varepsilon\}\), its induced component is the complete bipartite graph \(K_{N_\varepsilon,N_{\bar\varepsilon}}\), and the \(2^{r-1}\) components have no edges between them.

In a complete bipartite graph \(K_{p,q}\) with nonempty shores, if \(x\) vertices are selected from the first shore and \(y\) from the second, then every vertex of the first shore has exactly \(y\) selected neighbors and every vertex of the second has exactly \(x\). Therefore the total-perfect-code condition is **equivalent** to \(x=y=1\). Applied to every component, this proves that every code has one vertex per shore pattern and \(2^r\) vertices. Each component contributes \(N_\varepsilon N_{\bar\varepsilon}=\prod_i a_i b_i=B\) possibilities, independently. Hence the total count is \(B^{2^{r-1}}\).

**Exchange graph.** A permitted single-vertex replacement must change the selected choice **inside the same shore pattern**. Replacing across patterns would leave one pattern empty and another with two selected vertices, violating the proved characterization. Conversely, every within-pattern replacement preserves the condition. Independent choices at all \(2^r\) patterns give the stated Cartesian product of complete graphs. Its vertex degree is
\[
\sum_{\varepsilon}(N_\varepsilon-1)
=\prod_i(a_i+b_i)-2^r,
\]
by expanding the product. The distance between two codes is their number of differing pattern choices. As each \(N_\varepsilon\ge2\), all \(2^r\) choices can differ; connectivity and diameter \(2^r\) follow.

**Factorwise codes and their spectrum.** A factor code in \(K_{a_i,b_i}\) is exactly a cross-shore pair \(\{u_i,v_i\}\), by the same one-per-shore argument. Its product selects one vertex in each pattern, so there are exactly \(B\) distinct factorwise product codes (the factor choices can be recovered by coordinate projection). Two factorwise codes agree at a pattern precisely when every one of their \(r\) selected shore coordinates agrees. The number of agreeing patterns is therefore the product of the two-indicator sums in the theorem. Subtracting this number from \(2^r\) gives the distance formula. For each factor, two choices can have both shore vertices equal in one way, exactly one equal in \(s_i=a_i+b_i-2\) ways, and neither equal in \((a_i-1)(b_i-1)\) ways. Requiring exactly \(j\) factors with both equal and \(r-j\) with exactly one equal yields \(e_{r-j}(s_1,\ldots,s_r)\) choices at distance \(2^r-2^j\). If any factor has neither equal, the intersection is empty; subtracting the \(\prod_i(1+s_i)=\prod_i(a_i+b_i-1)\) nonzero-intersection cases from all \(B\) factorwise codes gives the distance-\(2^r\) multiplicity. Changing a single selected factor endpoint changes exactly \(2^{r-1}\) product vertices; every nonidentical pair changes at least that many.

**Covering radius.** Let \(C\) be arbitrary. Choose two complementary shore patterns \(\varepsilon,\bar\varepsilon\). Their two selected vertices specify one coordinate choice from **both shores of every factor**, hence determine a factorwise product code agreeing with \(C\) on these two patterns. The exchange distance is at most \(2^r-2\). To attain the bound when each shore size is at least \(2^{r-1}\), construct a code \(C_*\) whose chosen coordinate in each fixed shore of each factor varies injectively across the \(2^{r-1}\) patterns using that shore. This is possible under the size hypothesis, and the component characterization makes \(C_*\) valid. A factorwise product code cannot agree with \(C_*\) on two distinct noncomplementary patterns, because those patterns share at least one shore and the prescribed coordinates there differ. Thus it agrees on at most two patterns; the preceding argument guarantees two are attainable. Its distance from every factorwise code is at least \(2^r-2\), proving sharpness. When \(r=2\), the size hypothesis is exactly the standing \(a_i,b_i\ge2\).

## Verification

The attached `exhaustive_checker.cpp` builds the graph from simultaneous factor adjacency, tests **all** \(2^{16}\) vertex subsets of \(K_{2,2}\otimes K_{2,2}\) and **all** \(2^{20}\) subsets of \(K_{2,3}\otimes K_{2,2}\), checks every successful set, reconstructs the entire single-replacement graph, computes all-pairs shortest-path distances, verifies the product-code distance spectrum and the covering radius of two. Results: respectively \(256\) and \(576\) codes, \(16\) and \(24\) factorwise codes, degree \(12\) and \(16\), and diameter four in each case.

The separately written `independent_check.py` constructs the graphs by coordinate tuples and neighbor sets; enumerates all four-vertex candidates in those two cases; verifies the \(r=3\), \(K_{2,2}\) triple product's \(64\) factorwise codes and their distance spectrum \((1,6,12,8,37)\) at distances \((0,4,6,7,8)\); validates \(1000\) reproducibly sampled ambient codes; and confirms the sharp six-exchange covering-radius example for the threefold \(K_{4,4}\) tensor product. The programs corroborate finite instances and do not replace the all-parameter combinatorial proof.

Run in a standard environment with `g++ -O2 -std=c++17 exhaustive_checker.cpp -o exhaustive_checker && ./exhaustive_checker` and `python3 independent_check.py`.

## Relationship to prior work

Abay-Asmerom, Hammack and Taylor (2008) proved that a tensor product has a total perfect code exactly when every factor has one and observed explicitly that total-perfect-code counts cannot, in general, be deduced from just the counts in the factors. Their examples include product codes not arising as Cartesian products of factor codes. The present theorem supplies an exact all-parameter count for the natural biclique-factor family, together with a complete exchange graph, sharp factorwise distance spectrum, and covering-radius statement; it does not assert the earlier existence theorem as novel. Hammack (2006) studies connected components of direct products of bipartite graphs; here the complete-bipartite component structure follows directly from the specified factors. Related finite studies of total perfect codes on the four-cube concern a connected hypercube and are not covered by, nor do they imply, this theorem about tensor products of bicliques.

## Limitations

This theorem concerns tensor products **only of complete bipartite factors** with both shore sizes at least two. It does not classify codes on tensor products of arbitrary bipartite graphs. The exact covering radius for smaller shore sizes in three or more factors is not settled here. The historical-priority search cannot exclude an unindexed earlier equivalent formula or special-case enumeration. No independent scholarly audit has been performed.

## References

1. G. Abay-Asmerom, R. H. Hammack and D. T. Taylor, *Total Perfect Codes in Tensor Products of Graphs*, Ars Combinatoria **88** (2008), 129–134. Publisher full text: https://combinatorialpress.com/article/ars/Volume%20088/volume-88-paper-12.pdf (published 31 July 2008).
2. R. H. Hammack, *Isomorphic components of direct products of bipartite graphs*, Discussiones Mathematicae Graph Theory **26** (2006), 231–248. https://geodesic.mathdoc.fr/item/DMGT_2006_26_2_a5/.
