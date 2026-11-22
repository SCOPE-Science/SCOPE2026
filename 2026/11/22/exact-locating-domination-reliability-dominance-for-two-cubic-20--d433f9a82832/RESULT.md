# Exact locating-domination reliability dominance for two cubic 20-vertex graphs

## Finding
Let \(D\) be the Desargues graph, and let \(P\) be the graph of the regular dodecahedron. For a graph \(G\) and \(0\le k\le20\), write \(a_k(G)\) for the number of labelled vertex subsets of cardinality \(k\) that are ordinary locating-dominating sets. Their complete cardinality polynomials \(L_G(z)=\sum_{k=0}^{20}a_k(G)z^k\) satisfy
\[
\boxed{L_P(z)-L_D(z)=220z^7+2460z^8+6660z^9+7228z^{10}+3880z^{11}+1050z^{12}+120z^{13}.}
\]
All seven coefficients on the right are strictly positive. At every fixed detector budget \(7\le k\le13\), therefore, a uniformly selected \(k\)-vertex detector set is strictly more likely to locate every unselected vertex in \(P\) than in \(D\). For \(0\le k\le6\) and \(14\le k\le20\), the two graphs have exactly equal numbers of successful sets.

For independent vertex-detector deployment with common inclusion probability \(p\), let \(R_G(p)\) denote the probability that the selected detectors locate and dominate all unselected vertices. Then
\[
R_P(p)-R_D(p)=\sum_{k=7}^{13}\delta_k p^k(1-p)^{20-k}>0\quad(0<p<1),
\]
where \((\delta_7,\delta_8,\ldots,\delta_{13})=(220,2460,6660,7228,3880,1050,120)\). Equality holds at \(p=0\) and \(p=1\). The total numbers of locating-dominating vertex subsets are respectively \(384459\) for \(P\) and \(362841\) for \(D\).

## Assumptions and scope
All graphs are finite, undirected, and simple. An ordinary locating-dominating set \(S\subseteq V(G)\) is defined by requiring the open-neighborhood signatures \(N_G(x)\cap S\), for every \(x\in V(G)\setminus S\), to be nonempty and pairwise distinct. There is no signature-separation requirement for vertices belonging to \(S\); this is not the stronger identifying-code condition.

The Desargues graph is represented as a bipartite graph on \(L_e,R_e\) for the ten two-subsets \(e\subseteq\{0,1,2,3,4\}\), with \(L_eR_f\) an edge if and only if \(e\cap f=\varnothing\). This is the twenty-vertex bipartite Kneser graph \(H(5,2)\), equivalently \(GP(10,3)\). The dodecahedral graph \(P=GP(10,2)\) has vertices \(u_i,v_i\) for \(i\) modulo ten and undirected edges \(u_iu_{i+1}\), \(u_iv_i\), and \(v_iv_{i+2}\). Both graphs are cubic on twenty vertices. Every vertex subset is counted once, without quotienting by graph automorphisms.

The complete coefficient lists for degrees \(0\) through \(20\), in increasing order, are
\[
\begin{aligned}
(a_0(D),\ldots,a_{20}(D))={}&(0,0,0,0,0,0,0,0,1475,15100,49826,83840,88890,66020,36330,15184,4825,1140,190,20,1),\\
(a_0(P),\ldots,a_{20}(P))={}&(0,0,0,0,0,0,0,220,3935,21760,57054,87720,89940,66140,36330,15184,4825,1140,190,20,1).
\end{aligned}
\]

## Proof
**Exact decision predicate.** Give the vertices of either graph fixed labels from \(0\) through \(19\). For a twenty-bit mask \(s\), let \(S\) be its selected vertices and let \(b_x\) be the mask of the open neighborhood \(N_G(x)\). Define \(t_x=s\mathbin{\&}b_x\). By the definition of ordinary locating domination, \(S\) is valid if and only if the list \((t_x:x\notin S)\) has no zero entry and no repeated entry. No approximations or additional assumptions enter this equivalence.

**Exhaustive coefficient evaluation.** The attached `checks/verify_cpp.cpp` constructs \(D\) directly from disjoint pairs in a five-element set, constructs \(P\) from its generalized Petersen edges, and loops over all \(2^{20}=1048576\) masks. It evaluates the predicate exactly for every mask and increments the coefficient for its cardinality. Separately, `checks/verify_python.py` constructs \(D\) from \(GP(10,3)\) and \(P\) from \(GP(10,2)\), loops over every cardinality and every combination of that cardinality, and evaluates the same mathematical condition with a separate set-based implementation. The Python program also verifies an explicit twenty-vertex isomorphism between the \(GP(10,3)\) and disjoint-two-subset models. All vertex subsets, including the empty and full sets, are tested. The two independently constructed enumerations give exactly the coefficient lists displayed above. These finite exhaustive computations prove the coefficients, because every eligible labelled subset occurs in the loops and each is tested by a necessary-and-sufficient predicate.

**Comparison.** Subtracting the two exact lists gives the displayed seven-term polynomial with zero coefficient in every other degree. For a uniformly chosen \(k\)-subset, the success probability is \(a_k(G)/\binom{20}{k}\), so the coefficient inequalities prove the fixed-budget assertion. In the independent-deployment model, each individual \(k\)-subset has probability \(p^k(1-p)^{20-k}\). Summing over all successful sets proves \(R_G(p)=\sum_k a_k(G)p^k(1-p)^{20-k}\). Each difference summand is positive for \(0<p<1\), establishing strict dominance. At either endpoint, the selection is deterministic; both models have the same success status, establishing equality.

## Verification
From the directory containing this report and `checks`, run `python3 checks/verify_python.py`. Independently compile `c++ -std=c++17 -O2 checks/verify_cpp.cpp -o verify_cpp` and run `./verify_cpp`. Neither verifier requires input files, extra packages, or web access. Both assert the full twenty-one-coefficient vectors and the nonnegative coefficientwise difference, and both finish with an explicit success marker. The Python program independently checks the Desargues model isomorphism using the permutation listed in its source. These finite checks are complete enumeration proofs for the two fixed graphs, not extrapolations from sampling. The mathematical predicate and the code realizing it are available for inspection.

## Relationship to prior work
Balbuena, Foucaud, and Hansberg (first posted 27 July 2014) study locating-dominating and identifying-code minimum sizes on graphs of girth at least five; their Lemma 4 explains the separation obstruction using vertices with exactly one code neighbor. Foucaud and Henning (first posted 9 December 2014) prove an upper bound of half the order for ordinary location domination in twin-free cubic graphs. Neither of these general size bounds implies a coefficient of a complete locating-domination polynomial for the two particular graphs here.

Previously available exact results give \(1475\) minimum locating-dominating eight-sets of \(D\), and \(220\) minimum locating-dominating seven-sets of \(P\), including detailed symmetry and reconfiguration results. Those minimum-only results agree with our first nonzero coefficients but do not enumerate successful larger detector sets, nor do they imply the strict reliability comparison for all deployment probabilities. The distinction between ordinary locating domination, identifying codes, and graph metric resolution is maintained throughout. Targeted searches for these full coefficient lists, equivalent probability statements, and relevant graph names did not identify a covering published formula. A search not finding a result is not a proof of priority.

## Limitations
The conclusion concerns exactly two fixed twenty-vertex graphs; no corresponding inequality is claimed for arbitrary cubic graphs, other generalized Petersen graphs, or any larger family. The exact coefficient lists rely on executable finite enumeration rather than a short noncomputational closed-form count. The mathematical condition, complete finite search space, and two standalone implementations are supplied, but an independent scholarly audit has not been performed. An unindexed or inaccessible historical enumeration or equivalently formulated reliability calculation could predate this result.

## References
1. C. Balbuena, F. Foucaud, A. Hansberg, *Locating-dominating sets and identifying codes in graphs of girth at least 5*, arXiv:1407.7263, initially posted 2014-07-27, https://arxiv.org/abs/1407.7263.
2. F. Foucaud, M. A. Henning, *Location-Domination and Matching in Cubic Graphs*, arXiv:1412.2865, initially posted 2014-12-09, https://arxiv.org/abs/1412.2865.
3. *All 1,475 minimum locating-dominating sets of the Desargues graph*, publicly accessible mathematical result, 2026-10-12, https://github.com/published-finding corpus/2026/tree/main/2026/10/12/SCOPE-all-1-475-minimum-locating-dominating-sets-of-the-desargues-grap--d4faf2202a7f.
4. *Location-dominating code reconfiguration on the dodecahedral graph: token jumps are already slides*, publicly accessible mathematical result, 2026-11-08, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-location-dominating-code-reconfiguration-on-the-dodecahedral-gra--c7294558cbe4.
