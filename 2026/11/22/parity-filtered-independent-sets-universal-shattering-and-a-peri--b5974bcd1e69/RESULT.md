# Parity-filtered independent sets: universal shattering and a period-four online gap

## Finding
Let \(G=(V,E)\) be a nonempty finite simple graph. Write \(\mathcal I_p(G)\), for \(p\in\{0,1\}\), for the family of all independent vertex sets of cardinality congruent to \(p\pmod2\), queried by membership of individual vertices. For a vertex support \(S\subseteq V\), the following is an exact characterization of VC shattering:

1. \(S\) must be independent.
2. If \(|S|\not\equiv p\pmod2\), some vertex outside \(S\) must be nonadjacent to every vertex of \(S\).
3. If \(|S|\equiv p\pmod2\), then for every \(v\in S\), some vertex outside \(S\) must be nonadjacent to every vertex of \(S\setminus\{v\}\). For \(S=\varnothing\), this condition is vacuous.

Consequently, with \(\alpha=\alpha(G)\),
\[
\alpha-1\leq\operatorname{VCdim}(\mathcal I_p(G))\leq\alpha.
\]
The upper value occurs if and only if \(\alpha\equiv p\pmod2\) and a maximum independent set \(I\) exists such that every \(v\in I\) has an *external private neighbor*: a vertex \(t\in V\setminus I\) satisfying \(N(t)\cap I=\{v\}\).

For the path \(P_n\) with \(n\geq1\) labeled vertices and its two parity classes, the VC dimensions are, for \(n\geq3\),
\[
\operatorname{VCdim}(\mathcal I_p(P_n))=
\left\lfloor\frac{n-1}{2}\right\rfloor
+\mathbf1_{\{(n,p)=(4,0)\}}.
\]
At \(n=1\), both VC dimensions are zero; at \(n=2\), they are zero for \(p=0\) and one for \(p=1\). The exact Littlestone (complete adaptive binary-tree) dimensions are, for every \(n\geq1\),
\[
\operatorname{Ldim}(\mathcal I_p(P_n))=
\begin{cases}
\lfloor n/2\rfloor,& n\text{ even and }p\equiv n/2\pmod2,\\
\lfloor(n-1)/2\rfloor,&\text{otherwise}.
\end{cases}
\]
Thus for every even \(n\geq6\) exactly one of the two parity classes has a strict adaptive excess of one. The advantageous parity alternates with \(n\pmod4\); for odd \(n\), static and adaptive dimensions coincide in both classes.

## Assumptions and scope
All graphs are finite, simple, undirected, with at least one vertex. An independent set has no adjacent pair of selected vertices; the empty independent set is included in \(\mathcal I_0(G)\), not \(\mathcal I_1(G)\). The trace of a hypothesis \(H\) on \(S\) is \(H\cap S\). A support is shattered if all \(2^{|S|}\) traces occur. A complete Littlestone tree of depth \(d\) has a vertex-membership query at each internal node, with a distinct consistent hypothesis at each of its \(2^d\) leaves; queries may adapt to prior answers but cannot repeat on a feasible root-to-leaf path. The dimensions of a one-hypothesis family are zero. \(P_n\) has vertex set \(\{1,\ldots,n\}\) and edges between consecutive integers. Parity \(p=0\) means even independent-set cardinality and \(p=1\) means odd cardinality.

## Proof
**1. A one-vertex parity correction principle.** Let \(S\) be independent, and prescribe the positive trace \(Y\subseteq S\). If \(|Y|\equiv p\pmod2\), then \(Y\) itself is an allowed hypothesis, with precisely that trace. If its parity is wrong, every allowed realization must select at least one vertex \(t\notin S\), and since the realization is independent, \(t\) is nonadjacent to all of \(Y\). Conversely, whenever such \(t\) exists, \(Y\cup\{t\}\) is an allowed hypothesis with the desired trace. This proves the necessary and sufficient correction test for each \(Y\). If \(|S|\not\equiv p\), the largest wrong-parity set is \(Y=S\); a witness for it works for every smaller wrong-parity trace. If \(|S|\equiv p\), every wrong-parity \(Y\) is a proper subset, so choosing \(v\in S\setminus Y\) reduces the test to the maximal wrong-parity sets \(S\setminus\{v\}\). Adjacent supports cannot be shattered because the labeling positive on both endpoints of an edge is impossible. These observations prove the general support criterion, including the empty-support convention.

**2. Universal two-value rank dichotomy.** Fix a maximum independent set \(I\) of size \(\alpha\), choose \(v\in I\), and let \(S=I\setminus\{v\}\). Every \(Y\subseteq S\) has the right parity already or can be corrected by adding \(v\), which is outside \(S\) and nonadjacent to every element of \(S\). Hence \(S\) is shattered, giving \(\operatorname{VCdim}\geq\alpha-1\). No larger support than \(\alpha\) is independent, giving the upper bound. A support of size \(\alpha\) is necessarily a maximum independent set \(I\). Its all-positive trace forces \(\alpha\equiv p\pmod2\); in this case the support criterion requires, for every \(v\in I\), an outside vertex \(t\) nonadjacent to \(I\setminus\{v\}\). As \(I\) is maximal, each outside vertex has at least one neighbor in \(I\); thus the condition is exactly \(N(t)\cap I=\{v\}\). This proves the stated if-and-only-if criterion for the upper value.

**3. Path VC dimensions.** For \(P_{2k+1}\), the unique independent set of maximum size \(k+1\) is \(\{1,3,\ldots,2k+1\}\). When \(k\geq1\), each outside even vertex has two neighbors in this maximum set, so no member has an external private neighbor. Therefore both parities have VC dimension \(k\). For \(P_{2k}\), if a maximum independent set \(I\) of size \(k\) has an external private neighbor for each member, these \(k\) witnesses must be distinct. Since the complement also has exactly \(k\) vertices, every outside vertex must be a private neighbor and no pattern \(101\) may occur in the incidence word of \(I\). Its \(k\) selected vertices must therefore be separated by at least two zero positions, requiring length at least \(3k-2\). For \(k\geq3\), \(3k-2>2k\), a contradiction. At \(k=1\) the odd class on \(P_2\) shatters one vertex; at \(k=2\), the even class on \(P_4\) shatters \(\{1,4\}\), using the hypotheses \(\varnothing,\{1,3\},\{2,4\},\{1,4\}\). The one-vertex cases have one concept each. Together with Step 2 this establishes all claimed VC cases.

**4. General adaptive upper bounds.** In any complete depth-\(d\) shattered tree, the all-positive path uses \(d\) distinct queried vertices. Its consistent concept is independent and contains them, so \(d\leq\alpha(G)\). If the parity of \(\alpha(G)\) differs from \(p\), depth \(\alpha(G)\) is impossible. For odd \(n=2k+1\geq3\), a putative depth-\(k+1\) tree must follow the unique maximum independent set \(I=\{1,3,\ldots,2k+1\}\) on its all-positive path. If its parity matches \(p\), consider the leaf obtained by changing only the last answer to zero. Its positive set is \(I\setminus\{v\}\), of the wrong parity, and the last vertex \(v\) is forbidden. It would require an outside vertex nonadjacent to \(I\setminus\{v\}\), impossible because every outside vertex neighbors two distinct members of \(I\). Thus for both parities on odd paths the online dimension is at most \(k\). For even \(n=2k\), the bound is \(k\) for parity \(p\equiv k\) and at most \(k-1\) otherwise.

**5. Matching the adaptive bounds by endpoint recursion.** Write \(E_n\) and \(O_n\) for the respective even and odd independent-set online dimensions. Direct inspection of \(n=1,2\) gives \((E_1,O_1)=(0,0)\) and \((E_2,O_2)=(0,1)\). For \(n\geq3\), query endpoint vertex \(1\). Its zero branch is the same parity class on \(P_{n-1}\). Its one branch fixes vertex \(2\) negative and leaves the opposite parity class on \(P_{n-2}\). Both branches are nonempty; consequently
\[
E_n\geq1+\min\{E_{n-1},O_{n-2}\},\qquad
O_n\geq1+\min\{O_{n-1},E_{n-2}\}.
\]
Induction modulo four on these inequalities, with the two initial pairs, gives
\[
(E_{4a},O_{4a})=(2a,2a-1)\ (a\geq1),\quad
(E_{4a+1},O_{4a+1})=(2a,2a),
\]
\[
(E_{4a+2},O_{4a+2})=(2a,2a+1),\quad
(E_{4a+3},O_{4a+3})=(2a+1,2a+1),
\]
where \(a\geq0\) in the last three expressions. The upper bounds from Step 4 agree exactly with every entry. Therefore all adaptive formulas, including the period-four gap, hold for every path length, not merely for the enumerated examples.

## Verification
Two separately written verifiers are included. `check_parity.py` enumerates both classes for every \(1\leq n\leq16\), independently computes exact online ranks using the full version-space recurrence, evaluates the graph-theoretic shattering criterion, and compares it against direct traces for \(n\leq12\). It additionally checks the universal shattering criterion against direct traces on all 1,099 labeled graphs with at most five vertices, for both parities. `check_parity.cpp` independently constructs the membership tables for both classes on \(1\leq n\leq12\), enumerates all candidate supports by raw traces rather than using the criterion, and computes complete-tree online ranks with a separate version-space recursion. Output files record each checked path order, parity and dimension. Compilation and execution: `python3 check_parity.py`; `g++ -O2 -std=c++17 check_parity.cpp -o parity_checker && ./parity_checker`. These exhaustive finite checks corroborate, but do not replace, Steps 1–5, which prove the infinite path family.

## Relationship to prior work
The first-public 2021 work of Kovačević and Vukobratović (arXiv:2105.04617) analyzes rate, entropy, weight and run constraints for binary runlength-limited sequences; an independent-set word on a path is a no-adjacent-ones instance. Its full-text main results do not compute static or adaptive dimensions of parity-unions of these words. Johnson's 2021 paper (arXiv:2101.06490; primary MSC 03C45) examines VC dimension of the *translate family of a single infinite binary string*, not the vertex-membership concept family of all finite run-constrained words. These different notions of VC are not being conflated.

The published fixed-cardinality independent-path theorem (`2026/11/8/SCOPE-fixed-cardinality-independent-path-concepts-sharp-vc-rank-and-ne--2374d80e80d6`) gives exact VC rank and online bounds for **one prescribed weight**; the present classes unite all independent weights of one parity. Neither the weight-by-weight VC ranks nor their online bounds imply the all-weight parity correction criterion or the period-four online formula, because shattering trees may use different weights at different leaves. The antihole geodesic-convexity theorem (`2026/11/2/SCOPE-parity-sharp-vc-and-littlestone-dimensions-of-antihole-geodesic--3c49984c9619`) handles all independent sets of a *cycle* plus the universal vertex set, with no weight-parity restriction. It establishes a different odd-cycle gap and does not cover the present path parity-filtered family. Both published findings were inspected through their full proof text.

## Limitations
The graph-wide theorem determines static shattering and VC dimension, not the Littlestone dimension on arbitrary graphs. The exact online classification is proved only for paths; no cyclic or higher-width graph extension is asserted. The full coefficientwise support polynomial is not given. The finite verifier tests only its stated bounded graph sizes, whereas the unbounded statements follow from the proof. The searched published records and inspected papers do not establish historical uniqueness; independently indexed work under coding-theory terminology might exist. No independent mathematical audit has been performed.

## References
1. Hunter R. Johnson, *Binary strings of finite VC dimension*, arXiv:2101.06490, first public 2021-01-16, https://arxiv.org/abs/2101.06490.
2. Mladen Kovačević and Dejan Vukobratović, *Asymptotic Behavior and Typicality Properties of Runlength-Limited Sequences*, arXiv:2105.04617, first public 2021-05-10, https://arxiv.org/abs/2105.04617.
3. *Fixed-cardinality independent path concepts: sharp VC rank and near-saturation online growth*, published research record, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-fixed-cardinality-independent-path-concepts-sharp-vc-rank-and-ne--2374d80e80d6.
4. *Parity-sharp VC and Littlestone dimensions of antihole geodesic convexity*, published research record, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-parity-sharp-vc-and-littlestone-dimensions-of-antihole-geodesic--3c49984c9619.
