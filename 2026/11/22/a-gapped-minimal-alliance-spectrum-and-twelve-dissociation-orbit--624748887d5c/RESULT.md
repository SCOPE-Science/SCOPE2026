# A gapped minimal-alliance spectrum and twelve dissociation orbits of the Desargues graph

## Finding

Let \(G=H(5,2)\) be the Desargues graph, realized as the bipartite disjointness graph on two labeled copies of the two-subsets of a five-element set. Write \(\mathcal D(G)\) for its dissociation sets, meaning vertex subsets whose induced subgraph has maximum degree at most one, and \(\mathcal F(G)\) for their inclusion-maximal members. The exact face and facet polynomials are

\[
\begin{aligned}
D_G(z)={}&1+20z+190z^2+1080z^3+3985z^4+9784z^5\\
&+15910z^6+16600z^7+10390z^8+3460z^9\\
&+564z^{10}+60z^{11}+5z^{12},\\[3pt]
F_G(z)={}&65z^8+540z^9+234z^{10}+5z^{12}.
\end{aligned}
\]

The \(844\) inclusion-maximal dissociation sets form exactly twelve orbits under the natural action \(S_5\times C_2\), with orbit-size breakdown (grouping by size of the dissociation set):

| Cardinality | Orbit sizes | Number |
| --- | --- | ---: |
| \(8\) | \(5,60\) | \(65\) |
| \(9\) | \(60,120,120,240\) | \(540\) |
| \(10\) | \(2,12,40,60,120\) | \(234\) |
| \(12\) | \(5\) | \(5\) |

The five maximum dissociation sets are exactly those obtained, for each element \(a\) of the five-element ground set, by selecting both copies of every two-subset not containing \(a\). Every one of the sixty dissociation sets of size eleven has a **unique** extension to one of those five twelve-vertex sets.

For a cubic graph, a global offensive alliance is a set \(S\) such that every vertex outside \(S\) has at least two neighbors in \(S\). Its complement is a dissociation set. Consequently the complete enumerator of inclusion-minimal global offensive alliances on \(G\) is

\[
\boxed{M_G(z)=5z^8+234z^{10}+540z^{11}+65z^{12}.}
\]

Thus the minimum global offensive alliance has eight vertices, precisely five such labeled alliances exist, and there is **no inclusion-minimal nine-vertex alliance**, despite the existence of larger inclusion-minimal alliances of sizes ten, eleven and twelve. The result concerns inclusion-minimal alliances, not all successful alliances of these sizes.

## Assumptions and scope

Let \([5]=\{0,1,2,3,4\}\) and enumerate its ten two-subsets in lexicographic order:
\(01,02,03,04,12,13,14,23,24,34\). The twenty vertices are \((A,\varepsilon)\), where \(A\) is one of these subsets and \(\varepsilon\in\{0,1\}\). Distinct vertices \((A,\varepsilon)\), \((B,\delta)\) are adjacent if and only if \(\varepsilon\neq\delta\) and \(A\cap B=\varnothing\). The two shores have ten vertices each, and each vertex has exactly three neighbors; this specifies a labeled copy of the classical Desargues graph.

A subset \(D\subseteq V(G)\) is dissociated if \(\deg_{G[D]}(v)\leq1\) for all \(v\in D\). A dissociation set is inclusion-maximal if no strict superset is dissociated. The face polynomial \(D_G\) counts *all* dissociation sets, including the empty set; the facet polynomial \(F_G\) counts the inclusion-maximal sets. The natural group \(S_5\times C_2\) permutes ground labels and optionally switches the two shores; the orbit assertion refers to this explicitly defined group, not to an unverified automorphism classification.

A global offensive alliance \(S\) satisfies \(|N(v)\cap S|\geq2\) for each \(v\notin S\); for this three-regular graph that is the usual global offensive alliance condition, not the stronger strict-majority variant. The final alliance polynomial counts only inclusion-minimal such sets.

## Proof

**Complement correspondence.** For any \(S\subseteq V(G)\), let \(D=V(G)\setminus S\). Each \(v\in D\) has \(|N(v)\cap S|=3-|N(v)\cap D|\). Therefore \(S\) is a global offensive alliance if and only if every vertex of \(D\) has at most one neighbor in \(D\), which is exactly the dissociation condition. Because dissociation is hereditary under taking subsets, \(S\) is an inclusion-minimal alliance if and only if \(D\) is an inclusion-maximal dissociation set. Complementation changes cardinality \(k\) into \(20-k\), explaining \(M_G(z)=z^{20}F_G(z^{-1})\).

**Upper bound and extremal form.** For an arbitrary dissociation set \(D\) of size \(k\), the induced edge count satisfies \(2e(G[D])\leq k\). The number of crossing edges from \(D\) to its complement is \(3k-2e(G[D])\geq2k\); it is at most \(3(20-k)\). Hence \(k\leq12\). Equality forces \(G[D]\) to be a perfect matching and \(V(G)\setminus D\) to be independent. For each \(a\in[5]\), let \(D_a\) consist of both shore copies of the six pairs avoiding \(a\). Disjointness among those pairs is exactly complementation inside the remaining four-element set, so \(G[D_a]\) is six disjoint edges. The five \(D_a\) are dissociated and saturate the bound. Their complements \(S_a\) are two copies of the four pairs containing \(a\).

**Exhaustive finite classification.** The remaining equality uniqueness, all lower-cardinality counts, and the twelve-orbit partition are established by a finite exhaustive certificate. Number vertices \(0\) through \(19\): positions \(0,\ldots,9\) are shore zero in the lexicographic pair order above; positions \(10,\ldots,19\) are shore one. A subset is represented by a twenty-bit integer \(s\). For each vertex \(i\), its neighborhood bitmask \(a_i\) is determined solely by the disjointness rule. The exact Boolean predicate is

\[
P(s)\ \Longleftrightarrow\ \forall i\text{ with }s_i=1:\ \operatorname{popcount}(s\mathbin{\&}a_i)\leq1.
\]

The independent direct enumerator `desargues_enum.cpp` tests \(P(s)\) for every integer \(0\leq s<2^{20}\), and declares a valid set inclusion-maximal if and only if \(P(s\cup\{i\})\) fails for every absent bit \(i\). This tests all and only valid sets; the one-vertex criterion is sufficient because validity is hereditary. Its histograms are exactly the displayed polynomials and sum to \(62\,049\) valid sets and \(844\) facets.

The second implementation `desargues_verify.py` uses a different inductive membership predicate: remove the least significant selected vertex \(u\) to obtain \(T\). The larger set is dissociated if and only if \(T\) is dissociated, \(u\) has at most one neighbor in \(T\), and, when there is exactly one such neighbor \(v\), that \(v\) was isolated in \(G[T]\). Induction on the binary mask gives the correct answer for every subset. The script then independently enumerates inclusion-maximal sets and all \(240\) vertex permutations induced by \(S_5\times C_2\). It computes the orbit of each unclassified facet, verifies that the orbit lies in the unclassified facet family, removes it, and repeats. The twelve representatives and orbit sizes are also listed in `ORBIT_REPS.tsv`; their orbit sizes sum to \(844\), so none is omitted. The check also verifies that the five twelve-vertex facets are exactly \(\{D_a:a\in[5]\}\).

**Missing facet size and unique completion.** The exact polynomial \(D_G\) shows that there are sixty dissociation sets of size eleven. Deleting any one of the twelve vertices of each \(D_a\) produces sixty valid eleven-sets, all distinct: for different omitted labels \(a\neq b\), the intersection \(D_a\cap D_b\) contains only the two shore copies of the three pairs avoiding both labels, hence six vertices. Therefore all eleven-sets arise by deleting one vertex from exactly one \(D_a\), establishing the unique-completion assertion and ruling out eleven-vertex facets. Under complementation this is exactly the absence of nine-vertex minimal global offensive alliances.

## Verification

Two complete, self-contained and independently structured computational implementations accompany the proof, along with a twelve-row orbit representative certificate. The C++17 checker directly tests all \(2^{20}=1\,048\,576\) masks. The Python checker uses an induction on masks rather than direct neighborhood re-testing and additionally reconstructs the symmetry orbits and unique-completion fact. The two programs were executed against their actual distributed source files and agreed on every coefficient and all facet counts. Reproduction commands and exact expected outputs appear in `VERIFICATION.md`. No probabilistic sampling or truncated search is used.

## Relationship to prior work

Rodríguez and Sigarreta's 2006 work defines global offensive alliances of cubic graphs and proves the general lower bound \(\gamma_o(G)\geq2|V(G)|/5\) (and the corresponding upper bound). The minimum value eight here is therefore an instance of their sharp lower bound once the five constructions are supplied; neither this general bound nor its equality condition implies the count \(844\), the detailed facet spectrum, the orbit decomposition or the unique eleven-to-twelve extension rule. Orlovich et al. study the complexity of maximum and minimum-maximal dissociation sets, without this Desargues classification. Tu, Xiao and Lang prove general cubic-graph upper bounds on the entire dissociation polynomial for a range of activities; this does not determine the exact graph-specific coefficients. The bipartite Kneser graph \(H(5,2)\) is not the ordinary two-subset Kneser graph \(KG(5,2)\); a classification in the latter graph does not transfer by identity to this bipartite double cover.

## Limitations

The classification is exact for the specified labeled twenty-vertex graph and the specified natural group action; no extension to arbitrary bipartite Kneser graphs, generalized Petersen graphs, or all cubic graphs is asserted. Exhaustive computation is legitimate here because the graph has a fixed finite vertex set and the algorithms test every subset, but the counts are computer-assisted rather than an independent hand classification of all twelve orbits. The literature comparison cannot establish absolute publication priority against unindexed or inaccessible historical computations.

## References

1. J. A. Rodríguez and J. M. Sigarreta, *Offensive alliances in cubic graphs*, arXiv:math/0610023, first public 2006-09-30. https://arxiv.org/abs/math/0610023
2. Y. Orlovich, A. Dolgui, G. Finke, V. Gordon and F. Werner, *The complexity of dissociation set problems in graphs*, Discrete Applied Mathematics 159 (2011), 1352–1366; earlier preprint dated 2010-02-07. https://doi.org/10.1016/j.dam.2011.04.023
3. J. Tu, J. Xiao and R. Lang, *Counting the number of dissociation sets in cubic graphs*, AIMS Mathematics 8 (2023), 10021–10032. https://doi.org/10.3934/math.2023507
4. E. W. Weisstein, *Desargues Graph*, MathWorld. https://mathworld.wolfram.com/DesarguesGraph.html
