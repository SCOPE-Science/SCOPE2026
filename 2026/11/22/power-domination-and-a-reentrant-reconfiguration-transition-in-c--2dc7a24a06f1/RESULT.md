# Power domination and a reentrant reconfiguration transition in clique-bouquet prisms

## Finding

Let \(k\geq2\) and \(r_1,\ldots,r_k\geq2\) be integers. Form the clique bouquet \(H=K_1\vee\bigl(K_{r_1}\sqcup\cdots\sqcup K_{r_k}\bigr)\) and its Cartesian prism \(G=H\square K_2\). Write \(R=\sum_{i=1}^k r_i\). The two copies of the common bouquet vertex are *hubs*, and the \(2r_i\) vertices over the \(i\)-th clique constitute its *doubled petal*.

**Exact configuration criterion.** A set \(S\subseteq V(G)\) is power dominating if and only if (a) \(S\) contains at least one hub, or (b) \(S\) contains no hub and intersects every doubled petal.

Consequently the cardinality polynomial of all power-dominating sets, and that of inclusion-minimal such sets, are respectively

\[
\mathcal P_G(z)=(2z+z^2)(1+z)^{2R}+\prod_{i=1}^k\bigl((1+z)^{2r_i}-1\bigr),
\qquad
\mathcal M_G(z)=2z+\left(\prod_{i=1}^k2r_i\right)z^k.
\]

In particular, the minimum power-domination number is \(1\), attained by exactly two hub singletons, whereas the upper power-domination number (the maximum size of an inclusion-minimal set) is \(k\). The inclusion-minimal spectrum is exactly \(\{1,k\}\).

For an integer budget \(b\geq1\), let \(\mathcal T_b(G)\) be the graph whose vertices are the power-dominating sets of size at most \(b\), with two sets adjacent when one is obtained from the other by adding or removing one vertex. Its complete connected-component count is

\[
c_G(b)=\begin{cases}
2,&b=1,\\
1,&2\leq b<k,\\
1+\prod_{i=1}^k(2r_i),&b=k,\\
1,&b\geq k+1.
\end{cases}
\]

These graphs \(G\) are two-vertex-connected. Thus when \(k\geq3\), connectivity first appears at budget \(2\), disappears at budget \(k\) with exponentially many isolated configurations for fixed petal sizes, and returns at budget \(k+1\). The same construction supplies arbitrarily long gaps in inclusion-minimal power-domination cardinalities on two-vertex-connected graphs.

## Assumptions and scope

Graphs are finite, simple and undirected. All \(k\) peripheral cliques are nonempty with sizes at least \(2\); distinct petals have no edges between them in \(H\). In the Cartesian prism, each vertex is joined to its counterpart in the other layer, and there are no other cross-layer edges. The underlying vertices are labelled; the polynomials count vertex subsets without quotienting by graph symmetries.

Power domination means first observing the closed neighborhood \(N[S]\), then repeatedly permitting an observed vertex with exactly one unobserved neighbor to observe that neighbor. The order of legal forces is immaterial to eventual success. An inclusion-minimal power-dominating set has no successful proper subset. A token-addition/removal move changes the selection by exactly one vertex and keeps its cardinality at most \(b\) at every intermediate step; empty states and unsuccessful states are not vertices of \(\mathcal T_b(G)\).

## Proof

**1. One selected hub suffices.** Suppose one hub, say the hub in layer zero, belongs to \(S\). After closed-neighborhood observation, all peripheral vertices of that layer and the opposite hub are observed. Every such observed peripheral vertex has all its own-layer clique neighbors and its hub observed; its only possibly unobserved neighbor is the matched peripheral vertex in layer one. Therefore each missing counterpart is a legal force. Eventually all vertices are observed, regardless of any other selections.

**2. One selected vertex in every doubled petal suffices.** Assume \(S\) avoids both hubs but meets every doubled petal. Fix a petal and let one selected vertex be in layer zero, after exchanging layer labels locally if necessary. After closed-neighborhood observation, its layer-zero clique and its matched layer-one vertex are observed, as is the layer-zero hub. Every observed vertex in this clique can now force its layer-one counterpart when that counterpart is unobserved: its own-layer clique and hub neighbors are already observed. Thus every layer-one vertex in this petal becomes observed. Once the entire layer-one clique is observed, any of its vertices can force the layer-one hub if that hub is still unobserved, because all its other neighbors are observed. Repeating independently for each petal observes all peripherals and both hubs. Additional initially selected vertices can only help.

**3. An unhit petal cannot be entered without a selected hub.** Suppose neither hub is selected and some doubled petal \(i\) contains no selected vertex. Initially it is wholly unobserved: its vertices are adjacent only to the corresponding hub and vertices within that petal. If this petal ever acquired its first observed vertex after the initial step, the forcing vertex would have to be one of the two hubs. But each hub has at least \(r_i\geq2\) still-unobserved neighbors in that petal, so neither can perform that force. This contradiction proves the criterion.

**4. Count all successful sets.** Hub-containing sets have one of three nonempty hub selections, of weights \(2z+z^2\), and arbitrary choices from the \(2R\) peripheral vertices. Hub-free successful sets must choose a nonempty subset independently within every petal; their generating function is the stated product. The alternatives are disjoint.

**5. Determine minimal configurations.** A selected hub alone succeeds, so no larger hub-containing set is inclusion-minimal. A hub-free set is inclusion-minimal precisely when it contains exactly one vertex from each doubled petal: deleting one loses that petal, while deleting a hub is irrelevant because none is present. There are \(\prod_i2r_i\) such transversals. This proves \(\mathcal M_G\) and both extremal cardinalities.

**6. Determine reconfiguration components.** All hub-containing states with budget at least two lie in one component: delete all nonhub vertices while keeping a hub, and use the two-hub state to connect the two hub singletons. For budgets below \(k\), there are no hub-free successful states; hence the graph has two singleton components at budget one and a single hub-containing component for \(2\leq b<k\). At budget \(k\), every hub-free successful state is an exact one-per-petal transversal of size \(k\). Such a state cannot delete any selected vertex, and adding a hub would exceed the budget. It is therefore isolated, accounting for \(\prod_i2r_i\) additional components. At budget at least \(k+1\), each hub-free successful set can successively delete surplus peripheral vertices to reach a transversal, add one hub, then delete its remaining peripheral choices. Thus every state joins the hub-containing component.

**7. Two-vertex-connectivity.** The two hubs are adjacent. Deleting a peripheral vertex leaves every other peripheral connected to its corresponding hub. Deleting one hub leaves the other hub adjacent to all vertices in its own layer, with every surviving vertex of the opposite layer linked through its vertical matching edge. Hence deleting any single vertex leaves \(G\) connected. This also proves the claimed unbounded-gap and reentrant phenomena for the specified family.

## Verification

The standalone Python 3 file `verify_power.py` constructs each graph directly and exhaustively simulates closed-neighborhood observation and unique-white-neighbor propagation on every vertex subset. It compares each result with the proposed hub/petal criterion, checks every coefficient of both enumerators, and performs explicit breadth-first-search component enumeration of token-addition/removal states at budgets from \(1\) to \(k+2\). Tested petal-size vectors include \((2,2)\), \((2,3)\), \((2,2,2)\), \((2,2,3)\), and \((2,2,2,2)\), with graph orders from \(10\) to \(18\). The largest test checked every one of \(2^{18}=262144\) subsets and found \(247233\) successful sets; the component count at budget \(4\) was \(257\), as predicted. The program outputs `VERIFY_OK` on successful completion. Small finite checks corroborate, but do not replace, the all-parameter proof above.

## Relationship to prior work

Brimkov, Patel, Suriyanarayana and Teich (2018) define and analyze power-domination polynomials and give decomposition formulas for vertex identifications; this Cartesian prism does not arise by their vertex-identification construction, which does not determine the stated formula. Anderson, Kuenzel and Schuerger (2022) study bounds for Cartesian products under power domination, rather than complete placement and reconfiguration enumerators of these clique-bouquet prisms. General power-domination reconfiguration work and explicit nonmonotone budget transitions for crown graphs are prior art; neither general nonmonotonicity nor the definition of token-addition/removal is asserted to be new. The distinct contribution here is the exact all-subset criterion, the two complete polynomials, and the component formula for this specified infinite two-connected prism family.

## Limitations

The minimum clique size \(2\) is essential to the unhit-petal obstruction; the theorem does not assert the same criterion for singleton petals. The result concerns the ordinary observation-and-forcing model, without leaks, simultaneous forcing budgets or weighted sensors. The two-connected conclusion is vertex-connectivity, not a higher connectivity statement. Priority against inaccessible or unindexed material is not conclusively established. The result has not received independent mathematical audit.

## References

1. B. Brimkov, R. Patel, V. Suriyanarayana and A. Teich, *Power domination polynomials of graphs*, arXiv:1805.10984v1, submitted 2018-05-28. https://arxiv.org/abs/1805.10984
2. S. E. Anderson, K. Kuenzel and H. Schuerger, *Graphs which satisfy a Vizing-like bound for power domination of Cartesian products*, arXiv:2209.03930v1, submitted 2022-09-08. https://arxiv.org/abs/2209.03930
3. *Crown-graph power domination and nonmonotone reconfiguration thresholds*, mathematical research record, 2026. https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-crown-graph-power-domination-and-nonmonotone-reconfiguration-thr--6949b15f6548
4. *Sharp low-budget power domination on Cartesian clique paths*, mathematical research record, 2026. https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-sharp-low-budget-power-domination-on-cartesian-clique-paths--e7bac4253341
