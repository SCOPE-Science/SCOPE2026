# Sharp two-input edge-variation amplification by uncentered maximal averaging on the six-cycle

## Finding
For the unweighted cycle \(C_6\), write \(V=\mathbb Z/6\mathbb Z\). For a nonnegative signal \(f:V\to\mathbb R\), let \(\widetilde Mf(i)\) be the maximum of the arithmetic averages of \(f\) over all graph-distance balls \(B(c,r)\) containing \(i\), for any center \(c\in V\) and radius \(r\ge0\). Define
\[\operatorname{TV}(h)=\sum_{i=0}^{5}|h_i-h_{i+1}|.\]
Then the following two-input modulus is **exact** and **attained**:
\[\boxed{\sup_{\substack{f,g\ge0\\\operatorname{TV}(f-g)>0}}\frac{\operatorname{TV}(\widetilde Mf-\widetilde Mg)}{\operatorname{TV}(f-g)}=\frac{19}{10}.}\]
This exceeds the sharp value \(7/5\) found by an analogous calculation on the five-cycle. The six-cycle is the smallest cycle with diameter three, so the change introduces a genuine additional class of proper graph-distance balls.

## Assumptions and scope
The graph is finite, simple, unweighted and precisely \(C_6\). Balls are closed sets for the graph's shortest-path metric. Averaging is with uniform counting measure; the operator is **uncentered**, meaning the evaluation vertex need only belong to the ball, not be its center. Both inputs are nonnegative. Their difference may have arbitrary signs. Indices are modulo six.

## Proof
Every vertex belongs to exactly ten distinct balls, of cardinalities \(1,3,5,6\). For each vertex \(i\), enumerate centers \(c=0,\ldots,5\) and radii \(r=0,1,2,3\); retain each distinct ball containing \(i\) in order of first appearance. Its averaging row is \(a_{i,j}\), where \(j=0,\ldots,9\). Define a branch selection \(s=(s_0,\ldots,s_5)\) and the row-stochastic matrix \(A_s\) with row \(i\) equal to \(a_{i,s_i}\).

**Reduction to feasible branches.** For nonnegative inputs \(\widetilde M_i\) is the maximum of ten linear forms. Its differentiability regions with unique row choices are open polyhedral cones. Those regions are dense after discarding finitely many tie hyperplanes. Along any segment joining two nonnegative inputs, the output increment is an integral of branch matrices applied to the input difference. Because total variation is convex and homogeneous, its global two-input Lipschitz modulus does not exceed the largest \(\operatorname{TV}\)-operator norm among feasible strict branches. Conversely, any strict feasible branch is realized at a nonnegative baseline by adding a sufficiently large constant; a sufficiently small cut-indicator perturbation realizes the corresponding branch norm. The two quantities therefore agree.

**Reduction to cuts.** Each row sum of \(A_s\) is one. For any real vector \(h\), subtract its minimum, then use the finite discrete coarea representation as a positive integral of nontrivial vertex-set indicators. Subadditivity of total variation gives
\[\|A_s\|_{\operatorname{TV}\to\operatorname{TV}}=\max_{\varnothing\ne S\subsetneq V}\frac{\operatorname{TV}(A_s\mathbf 1_S)}{|\partial S|}.\]
There are exactly \(62\) nontrivial labeled cuts to check for every feasible strict branch.

**Exact exhaustive certificate.** Multiply each averaging coefficient by \(30\); all entries are integers because the ball sizes divide \(30\). Translation of the baseline by a constant does not change the maximizing rows, so normalize its first coordinate to zero. For a partial branch selector \(s\), collect the five-coordinate integer row differences \(D_{i,j}=30(a_{i,s_i}-a_{i,j})\), omitting the first coordinate and the chosen row. The selector is strictly realizable precisely when a real vector \(x\in\mathbb R^5\) satisfies \(D_{i,j}\cdot x>0\) for all these differences.

The accompanying `c6_branch_certificates.json` provides a complete ten-way prefix tree. Every pruned prefix has a nonzero, coordinatewise nonnegative **rational** combination of its row-difference vectors equal to zero; this proves strict feasibility impossible. Each unpruned complete six-vertex selector has a **rational witness** satisfying all strict inequalities. `verify_c6.py` reconstructs every averaging row, checks every dual identity and strict witness using exact rationals, and computes every labeled cut ratio for every strictly realizable complete selector. It verifies \(1{,}739\) feasible complete selectors, \(13{,}400\) infeasible prefix certificates, and \(107{,}818\) exact feasible-selector/cut pairs. The largest ratio is exactly \(19/10\). No floating-point optimization or external solver is used by the verifier. The finite certificate together with the elementary reductions above proves the universal inequality for **all** admissible real input pairs on this graph; sampling is not substituted for completeness.

**Equality.** Take the following nonnegative integer inputs:
\[f=(50,352,360,302,365,346),\qquad g=(50,352,361,303,366,346).\]
Direct arithmetic gives
\[\widetilde Mg-\widetilde Mf=(1/2,0,1,3/5,1,0),\quad\operatorname{TV}(g-f)=2,\quad\operatorname{TV}(\widetilde Mg-\widetilde Mf)=19/5.\]
Therefore the upper bound is attained at ratio \(19/10\).

## Verification
In the directory containing both artifacts, execute `python3 verify_c6.py c6_branch_certificates.json`. It uses only the Python standard library. It verifies exactly \(15{,}139\) certificate terminal nodes (including \(1{,}739\) realizable complete selectors), all rational dual obstructions and strict primal witnesses, all \(107{,}818\) selector/cut ratios, and the displayed attaining signals. The certificate is the actual finite proof's exhaustive arithmetic component.

## Relationship to prior work
Soria and Tradacete (2014 preprint, published 2016) treat the centered finite-graph maximal operator and its \(\ell^p\) and weak-type estimates, rather than the uncentered six-cycle **two-input** total-variation coefficient. Madrid (2015 preprint) proves sharp discrete maximal-function variation inequalities on \(\mathbb Z^d\), particularly one-input derivative bounds; these do not yield the stated finite-cycle two-input modulus. González-Riquelme and Madrid (2020 preprints) give sharp one-input variation estimates for centered finite-graph maximal operators on selected graph families. These statements and the present exact two-input uncentered coefficient use different norms, graph classes, and quantifiers. General maximal-operator theory motivates the problem but does not settle this coefficient by implication.

## Limitations
The formula is proved for nonnegative real signals on the unweighted six-cycle, with averaging over all graph-distance balls containing the evaluation vertex. It is not asserted for the centered operator, signed-input absolute-value maximal operator, arbitrary cycle lengths, other graphs, or weighted balls. An earlier unindexed equivalent result cannot be excluded; independent assessment of bibliographic priority has not been performed. The finite certificate is checkable with the included standalone exact-arithmetic program, not a closed-form classification of all maximizing branch selectors.

## References
- J. Soria and P. Tradacete, *Best constants for the Hardy–Littlewood maximal operator on finite graphs*, arXiv:1410.6204v1 (22 October 2014), https://arxiv.org/abs/1410.6204.
- J. Madrid, *Sharp inequalities for the variation of the discrete maximal function*, arXiv:1512.04112v1 (13 December 2015), https://arxiv.org/abs/1512.04112; *Bull. Aust. Math. Soc.* 95 (2017), 94–107.
- C. González-Riquelme and J. Madrid, *Sharp inequalities for maximal operators on finite graphs*, arXiv:2005.03146v1 (6 May 2020), https://arxiv.org/abs/2005.03146.
- C. González-Riquelme and J. Madrid, *Sharp inequalities for maximal operators on finite graphs, II*, arXiv:2011.02630v1 (5 November 2020), https://arxiv.org/abs/2011.02630.
