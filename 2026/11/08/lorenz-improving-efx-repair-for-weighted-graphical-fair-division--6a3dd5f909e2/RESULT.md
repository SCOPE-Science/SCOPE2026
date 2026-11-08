# Lorenz-improving EFX repair for weighted graphical fair division

## Finding

For **every** finite loopless undirected multigraph with positive edge weights shared equally by the two endpoints, every complete orientation of edge-goods admits an EFX orientation whose realized-utility vector is a Lorenz improvement of the original. No goods are discarded or assigned to zero-value recipients. Consequently, **requiring positive-good EFX has zero optimality cost for every symmetric Schur-convex objective on the realized utility vector**, including the peak utility, the sum of squared utilities, and any common convex separable cost. Dually, **maximizing any symmetric Schur-concave welfare objective**, such as \(\sum_i\log(1+L_i)\), also admits an EFX optimizer.

The result concerns *cofinality* of EFX allocations in the Lorenz preorder, not the existence of a single Lorenz-best allocation that dominates all other orientations. In particular, there may be incomparable Lorenz-optimal utility vectors.

## Assumptions and scope

Let \(G=(V,E)\) be a finite undirected **loopless multigraph**, with \(|V|=n\ge1\), permitting isolated vertices and parallel edges. Each distinct edge \(e=\{i,j\}\) is a good of weight \(w_e>0\), worth exactly \(w_e\) to agents \(i,j\), and zero to all other agents. Values of bundles are additive and weights may be arbitrary positive real numbers.

An *orientation* assigns each edge-good to exactly one of its endpoints. Let \(X_i\) be the bundle received by \(i\), and let \(L_i(X)=\sum_{e\in X_i}w_e\). Such orientations maximize the sum of agents' utilities, equal to \(W=\sum_{e\in E}w_e\).

The adopted **positive-good EFX** definition is
\[
  v_i(X_i)\ge v_i(X_j\setminus\{e\})
\]
for every ordered pair of distinct agents \(i,j\) and every \(e\in X_j\) with \(v_i(e)>0\). This is distinguished from the stronger zero-inclusive \(\mathrm{EFX}_0\) condition.

For vectors of the same total, \(b\) *Lorenz-dominates* \(a\) if for every \(1\le k\le n\) the sum of the \(k\) smallest coordinates of \(b\) is at least that of \(a\). Thus \(b\) is no more unequal than \(a\) in the majorization order.

## Proof

Fix any orientation \(X\) and write \(L_i=L_i(X)\). For distinct vertices \(i,j\), let \(S_{ij}\) be the total weight of those goods joining \(i,j\) that were assigned to \(j\); if there are any, let \(s_{ij}\) be the minimum weight among them. Since only the edges between \(i,j\) contribute to agent \(i\)'s valuation of \(X_j\), the positive-good EFX condition for this ordered pair is **exactly**
\[
 L_i\ge S_{ij}-s_{ij},
\]
provided the set is nonempty. When there is no such edge, the pair imposes no constraint.

If EFX fails, choose a violating pair \(i,j\), so that \(L_i<S_{ij}-s_{ij}\). Because agent \(j\) owns every edge counted by \(S_{ij}\), its load satisfies \(L_j\ge S_{ij}\). Hence, for the minimum-weight edge \(e\) of weight \(s=s_{ij}>0\),
\[
  L_j>L_i+s.
\]
Reassign precisely this edge from \(j\) to \(i\). The affected loads change from \((a,b)=(L_i,L_j)\) to \((a+s,b-s)\), where \(a<a+s<b\) and \(a<b-s<b\). The two new entries lie strictly between the old entries, their sum is unchanged, and every other load remains the same. This is a strict *balancing transfer* and so Lorenz-improves the complete vector, by the elementary two-coordinate majorization criterion. Directly,
\[
(a+s)^2+(b-s)^2-a^2-b^2=-2s(b-a-s)<0.
\]
There are finitely many orientations (\(2^{|E|}\)), so the strictly decreasing square-potential prohibits revisiting any state. Repeatedly transferring a smallest edge from a violating pair therefore terminates, and termination means the orientation satisfies EFX. Every transfer weakly improves all Lorenz cumulative sums; their transitivity proves the assertion for the final orientation.

A Schur-convex function is monotone under majorization in the direction of reduced inequality. Given any orientation minimizing such a function, the repair just constructed does not increase its objective, so some EFX orientation also attains its minimum. In particular \(\max_i L_i\) and \(\sum_i\varphi(L_i)\) for a **common** convex \(\varphi\) have no price from enforcing EFX; strict convexity of \(\varphi\) makes each violation-removing transfer strictly improve that separable cost. By the same majorization order, every symmetric Schur-concave welfare functional weakly increases under the repair, so a maximizer of any such functional can be repaired without diminishing its value. All orientations have total welfare \(W\), so the result also preserves welfare optimality.

The endpoint-equality assumption is material. With two agents and two positive goods each valued at \(1\) by agent \(1\) and \(R>2\) by agent \(2\), all assignments to agent \(1\) give realized loads \((2,0)\), whose peak \(2\) is unconstrained-optimal. But assigning both goods to either agent fails EFX (the other agent still values a single remaining good after deletion); the only EFX orientations split the two goods and have peak \(R\). Thus the EFX-constrained peak/unconstrained peak ratio is \(R/2\), unbounded as \(R\to\infty\).

## Verification

The standalone exact-integer checker in `verify.py` tests the repair starting from **every** orientation for all edge-weighted multigraphs with \(n=2\) and at most six edges, \(n=3\) and at most five edges, and \(n=4\) and at most four edges, where edge weights are in \(\{1,2,3\}\) and parallel edges are permitted. In total it checks **9,401 multigraph instances and 159,039 orientations**, verifies EFX after repair and all Lorenz partial-sum inequalities, and checks equality of the global EFX and unrestricted minimum peak and minimum square-cost optima. It additionally checks 500 seeded instances with up to 11 edges and weights up to 18, the two-agent asymmetric example, and the explicit pair of incomparable Lorenz-optimal profiles. Run `python verify.py` (Python standard library only).

These finite checks are not an infinite proof. The universal assertion follows from the strict balancing-transfer argument, which applies to all finite multigraphs and positive real weights.

## Relationship to prior work

Afshinmehr, Ashuri, Mahmoudkhan, Mehlhorn and Shahrezaei, *EFX Allocations Exist on Multi-Graphs* (first posted June 17, 2026, arXiv:2606.18665), prove a much broader EFX **existence** theorem for cancelable multigraph valuations. Their main framework does not state this universal Lorenz-improving transfer from any given orientation or simultaneous preservation of arbitrary Schur-convex load objectives. This result is narrower in valuations but strengthens the **relationship between fairness and load optimality**.

Kaviani, Seddighin and Shahrezaei, *Almost Envy-free Allocation of Indivisible Goods: A Tale of Two Valuations* (first posted July 6, 2024, arXiv:2407.05139), established EFX **existence** for two-relevant-agent restricted-additive valuations; Section 8 treats the relevant domain, but not this arbitrary-start majorization guarantee. Their treatment also uses a stronger zero-inclusive deletion formulation, which this result does not claim.

Babaioff, Ezra and Feige, *Fair and Truthful Mechanisms for Dichotomous Valuations* (AAAI 2021, DOI 10.1609/aaai.v35i6.16647), construct **Lorenz-dominating** allocations for binary-marginal valuations. This strongly covers the uniform unit-weight special case, but does not cover arbitrary positive heterogeneous edge weights: the all-binary premise is essential. The present result does **not** claim to rediscover the binary case or to produce a universally Lorenz-dominating allocation in the weighted setting.

## Limitations

The result depends on identical positive values for the two endpoints of every edge, and on additive utilities. It provides a finite repair procedure, **not** a polynomial bound on its running time in the binary encoding of arbitrary real/rational weights; computing an initially optimal weighted makespan orientation may itself be hard. The EFX condition is only for goods positively valued by the observer, not the stronger \(\mathrm{EFX}_0\) convention. The result does not assert a single globally Lorenz-best orientation. For example, a three-vertex multigraph with weighted edges \((0,1,2),(0,1,3),(0,1,5),(0,2,4),(0,2,4)\) has incomparable undominated sorted-load vectors \((5,5,8)\) and \((4,7,7)\).

Existing related literature establishes more general EFX existence results; full originality depends on the non-implication of this specific weighted Lorenz-cofinality assertion. No independent scientific review has been performed.

## References

1. Afshinmehr, M., Ashuri, A., Mahmoudkhan, P., Mehlhorn, K., Shahrezaei, A. M., *EFX Allocations Exist on Multi-Graphs*, arXiv:2606.18665 (2026), https://arxiv.org/abs/2606.18665.
2. Kaviani, A., Seddighin, M., Shahrezaei, A., *Almost Envy-free Allocation of Indivisible Goods: A Tale of Two Valuations*, arXiv:2407.05139 (2024), https://arxiv.org/abs/2407.05139.
3. Babaioff, M., Ezra, T., Feige, U., *Fair and Truthful Mechanisms for Dichotomous Valuations*, AAAI 2021, DOI:10.1609/aaai.v35i6.16647, https://doi.org/10.1609/aaai.v35i6.16647.
