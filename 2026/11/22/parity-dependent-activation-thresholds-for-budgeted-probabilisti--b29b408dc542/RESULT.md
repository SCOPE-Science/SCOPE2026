# Parity-dependent first activation thresholds for probabilistic firebreaks on a path

## Finding

There are \(n\ge2\) equal-value patches on a path. Edge \(i\), between patches \(i\) and \(i+1\), independently transmits fire with probability \(q_i=e^{-g_i}\). Choose the nonnegative investments \(g_i\) with sum \(B>0\) to minimize the expected number burned when one uniformly chosen patch ignites. There is a unique minimizer. Its first departure from protection concentrated at the center depends on parity:

- If \(n=2m\), \(m\ge2\), only edge \(m\) is protected, with investment \(B\), exactly for \(0<B\le \log(m/(m-1))\).
- If \(n=2m+1\), \(m\ge2\), only edges \(m,m+1\) are protected, with investment \(B/2\) each, exactly for \(0<B\le 2\log(m/(m-1))\).

At the threshold the stated center allocation remains uniquely optimal; above it the allocation is strictly suboptimal. At \(n=2\) the sole edge takes the whole budget, and at \(n=3\) the two edges split it equally for all \(B\). At matched \(m\) the odd threshold is twice the even one, with leading scales \(2/m\) and \(1/m\), respectively. The claim is the first threshold for the entire path family, not a separate four-site continuation result.

## Assumptions and scope

Edge transmission outcomes are independent of the choice of the initial patch. Exactly the vertices in its open-edge component burn. The exponential law is a dimensionless assumption. The path is undirected, and no other ignition or route is allowed. Costs are linear and identical for all edges. All optimality statements are global, on the closed budget simplex.

Equivalently, defining \(x_i=\sum_{k<i}g_k\), the mathematical problem is to minimize the sum of the pair potentials \(e^{-|x_j-x_i|}\) at ordered positions \(0=x_1\le\cdots\le x_n=B\); coincident positions are allowed. An active edge is a strict gap between consecutive positions.

## Proof

**Loss and uniqueness.** An ordered vertex pair belongs to the same component precisely when all intervening edges are transmitting. If \(L\) is the number burned, then
\[
\mathbb E L=1+\frac 2n F(g),\qquad
 F(g)=\sum_{1\le i<j\le n}e^{-\sum_{a=i}^{j-1}g_a}.
\]
The second directional derivative of \(F\) in direction \(v\) is the sum of the corresponding positive weights times \((\sum_{a=i}^{j-1}v_a)^2\). The terms \(j=i+1\) already sum to \(\sum_i e^{-g_i}v_i^2>0\) when \(v\ne0\). Compactness of the budget simplex and strict convexity give a unique minimizer, which is fixed by path reflection.

**Optimality certificate.** Write \(G_k=\partial F/\partial g_k\); it equals minus the sum of the weighted pairs crossing edge \(k\). At a candidate allocation the first-order certificate is that all active edges have the same \(G_k\) and every inactive edge has derivative at least that value. Necessity follows by moving infinitesimal investment from an active edge to a second edge. Sufficiency follows from the convex supporting-hyperplane inequality, since the inner product of the gradient with any feasible displacement is nonnegative. Strict convexity gives uniqueness, including at equality in an inactive-edge condition.

**Even path.** Put the budget on edge \(m\) and write \(q=e^{-B}\). The center derivative is \(-m^2q\). For \(1\le k<m\), there are \(k(m-k)\) pairs crossing \(k\) on the left and \(km\) crossing both \(k\) and the center. Thus
\[
G_k-G_m=(m-k)(mq-k).
\]
Right-side conditions follow by reflection. All inequalities hold precisely when \(mq\ge m-1\). If this fails, the nearest inactive edge gives a strictly improving direction.

**Odd path.** Put \(B/2\) on each central edge with \(q=e^{-B/2}\). For \(1\le k<m\), pairs crossing \(k\) have total weights \(k(m-k)\) within the left block, \(kq\) to the center vertex and \(kmq^2\) to the opposite block. The central derivatives, identical by reflection, are \(-m(q+mq^2)\). Consequently
\[
G_k-G_m=(m-k)(q+mq^2-k),\qquad
q+mq^2-(m-1)=(q+1)(mq-(m-1)).
\]
The sharp condition is again \(mq\ge m-1\); taking logarithms now yields the factor of two. Reflection excludes an unequal central-only split. If the condition fails the nearest inactive edge again gives improvement. For \(n=3\) symmetry and uniqueness already suffice, and \(n=2\) has a single decision variable. The expansion \(-\log(1-1/m)=1/m+O(m^{-2})\) gives the scales.

## Verification

The accompanying standard-library Python file `check_firebreak.py` checks the pair expectation against finite bond-outcome enumeration, the exact rational derivative identities and representative positive Hessian forms. Its four-site numerical checks illustrate the previously documented specialization below. None of these finite checks substitutes for the all-size convex certificate.

## Relationship to prior work

The four-site corridor result [1] gives a complete diagram at baseline permeability \(p\), including \(p=1\) here. At \(p=1\) its threshold is \(\log2\), and above it the optimizer is \((\log z,\log(z+1),\log z)\), where \(z>1\) solves \(z^3+z^2=e^B\). This is exactly the same four-site specialization (set \(z=e^x\) if the flanks are denoted by \(x\)). No separate originality is claimed for the four-site diagram; chronology is not inferred from the shared publication date.

Demange et al. [2] optimize a budgeted set of discrete firebreaks on a graph; their edge-removal decisions differ from the continuous attenuation here. The discrete two-cut cycle [3] optimizes separation under independent vertex ignitions. A connectivity investment problem [4] instead maximizes reliability with transmission \(1-e^{-g_i}\). Neither cycle geometry nor the reliability objective gives the all-path suppression thresholds above.

## Limitations

The result does not characterize later support changes for general \(n\). It is a mathematical model, not an empirical firebreak design rule. Heterogeneous patch values or ignition sources, fire jumping, and different attenuation laws may alter the thresholds. The prior-work comparison is bounded and does not certify priority.

## References

1. [*A sharp central-to-distributed fuel-break budget transition on a four-site forest corridor*](https://github.com/Resultary/2026/tree/main/2026/11/22/SCOPE-a-sharp-central-to-distributed-fuel-break-budget-transition-on-a--ea6f3ea0be9f), Finding and model.
2. M. Demange et al., *A graph theoretical approach to the firebreak locating problem*, [arXiv:2103.10115](https://arxiv.org/abs/2103.10115), §2.2.
3. [*Exact staircase of optimal two-firebreak gaps on a uniformly ignited cycle*](https://github.com/Resultary/2026/tree/main/2026/11/2/SCOPE-exact-staircase-of-optimal-two-firebreak-gaps-on-a-uniformly-ign--20549d04bba2).
4. [*Four habitats are the sharp onset of unequal reliability investment on a path*](https://github.com/Resultary/2026/tree/main/2026/11/22/SCOPE-four-habitats-are-the-sharp-onset-of-unequal-reliability-investm--dc53d6309137).
