# A sharp one-split refinement gap for stochastic trace probing on screened stars

## Finding

Let \(L\) be the combinatorial Laplacian of the unit-edge star \(K_{1,m}\). Fix \(\mu>0\) and an integer \(k\ge2\), and let \(m\to\infty\). For each partition \(P\) of the vertices into nonempty classes, estimate \(\operatorname{tr}G\), where \(G=(\mu I+L)^{-1}\), by summing one independent class-supported Rademacher quadratic form per class. Write \(\mathcal V_j(m,\mu)\) for the minimum variance over all partitions into \(j\) classes. No proper-coloring constraint is imposed.

For an optimal \(k\)-class partition \(P\), let \(\mathcal V^{\mathrm{split}}(P)\) be the minimum variance over partitions obtained by splitting one class of \(P\) into two nonempty classes and leaving all other classes unchanged. Then
\[
\frac{\mathcal V^{\mathrm{split}}(P)}{\mathcal V_{k+1}(m,\mu)}
=1+\frac{k-1}{2k^2}+O_{k,\mu}(m^{-1}),
\]
uniformly over optimal parents \(P\). In particular, the best such upgrade from two classes to three has limiting variance ratio \(9/8\) against globally redesigning the three classes.

## Proof

Write \(a=[\mu(1+\mu)(\mu+m+1)]^{-1}\). The hub-to-leaf off-diagonal entries of \(G\) equal \((1+\mu)a\), and the entries between distinct leaves equal \(a\). Indeed the leaf block of \(\mu I+L\) is \((1+\mu)I_m\) and its hub Schur complement is \(\mu+m-m/(1+\mu)=\mu(\mu+m+1)/(1+\mu)\). Block inversion gives the two entries.

Each supported quadratic form has deterministic diagonal contribution. Two distinct unordered pairs of vertices in its off-diagonal contribution give uncorrelated sign products: their product contains a sign with odd exponent and mean zero. This gives variance \(4\sum_C\sum_{i<j\in C}G_{ij}^2\) for the sum of forms. Divide by \(4a^2\) and set \(R=(1+\mu)^2\). For class sizes \(s_0,\dots,s_{j-1}\), where the hub lies in class 0, the normalized cost is
\[
E(P)=\sum_{i=0}^{j-1}\binom{s_i}{2}+(R-1)(s_0-1).
\]

In any optimal \(j\)-class partition the largest and smallest sizes differ by at most \(R\). If their sizes differed by more than \(R>1\), the larger class would contain a movable leaf and would remain nonempty after its removal. Moving that leaf from a class of size \(u\) to one of size \(v\) changes the binomial sum by \(-(u-1)+v\) and the hub correction by at most \(R-1\). Thus the move would strictly improve the objective. In particular, every optimal \(j\)-class size is \((m+1)/j+O_\mu(1)\), uniformly over optimizers.

For an optimal \((k+1)\)-class partition this proves \(E=m^2/[2(k+1)]+O_{k,\mu}(m)\). In a one-split refinement of any optimal \(k\)-class partition, the \(k-1\) unchanged classes contribute \((k-1)m^2/(2k^2)+O_{k,\mu}(m)\) to the binomial sum. The split class has size \(s=m/k+O_{k,\mu}(1)\). For any split into sizes \(u,s-u\), the sum of their binomial terms is at least \(s^2/4-s/2\), attained up to an additive \(1/4\) by dividing into sizes \(\lfloor s/2\rfloor,\lceil s/2\rceil\). These sizes can be obtained whether or not the class contains the hub. The extra hub term is nonnegative and at most \((R-1)m\), so any split has cost at least \((k-1/2)m^2/(2k^2)-C_{k,\mu}m\) for a constant independent of the parent; an equal-as-possible split achieves that leading cost with \(O_{k,\mu}(m)\) error. For large \(m\) all parent classes are splittable. The common positive variance factor \(4a^2\) cancels in the ratio. Dividing by the unrestricted cost gives the claim and its uniform error estimate.

## Example and reproducibility

For \(m=12\) and \(\mu=1/2\), evaluating the normalized cost over the class sizes and the hub class gives optimal costs \(169/4\) for two classes (hub with five leaves and a class of seven leaves) and \(51/2\) for three classes (hub with two leaves and two classes of five leaves). A single split of the two-class optimum costs at least \(117/4\), attained by splitting the hub class into the hub with one leaf and a four-leaf class. The best-refinement ratio in this example is \(39/34\).

The accompanying `verify_star.py` uses the Python 3 standard library and exact rational arithmetic. It checks the variance reduction and auxiliary finite partition formulas, the example, and bounded refinement ratios. It enumerates unrestricted partitions for \(2\le m\le8\), \(2\le j\le m+1\), at four rational screenings and also checks several larger finite refinements. These checks supplement rather than prove the uniform asymptotic.

## Relationship to prior work and limitations

The general supported-probe variance identity is established stochastic-probing theory [1]. The fixed-budget hub-occupancy classification is not the contribution here: the two-probe complete-bipartite result includes the star as a special case [2], and a separate screened-star result states the all-optima discrete-convex classification for \(k\ge3\) [3]. Only a coarse, elementary balancing bound on the sizes of the parent classes is needed in the proof above. The additional comparison is a sharp penalty for an optimal fixed-budget design when the next budget permits changing just one class by splitting it. The indexed fixed-budget statements do not give this cross-budget ratio.

Hierarchical probing [4,5] motivates retaining partition information as the probe budget grows. The comparison here only concerns the variance of the independent one-probe-per-class estimator under the specified partition operation; it is not a variance lower bound for correlated Hadamard probes, arbitrary hierarchical estimators, or adaptive changes to multiple classes. The asymptotic holds at fixed \(k,\mu\); it makes no claim for weighted stars, other graphs, or varying screening or budget.

## References

1. A. Frommer, M. Rinelli, and M. Schweitzer, *Analysis of stochastic probing methods for estimating the trace of functions of sparse symmetric matrices*, [arXiv:2308.07722](https://arxiv.org/abs/2308.07722).
2. *Sharp two-color stochastic-probing transition on complete bipartite resolvents*, [indexed result](https://github.com/Resultary/2026/tree/main/2026/11/8/SCOPE-sharp-two-color-stochastic-probing-transition-on-complete-bipart--1edc2b42b895).
3. *All-budget optimal Rademacher probing partitions on screened star graphs*, [indexed result](https://github.com/Resultary/2026/tree/main/2026/11/22/SCOPE-all-budget-optimal-rademacher-probing-partitions-on-screened-sta--276450ab2e3f).
4. A. Stathopoulos, J. Laeuchli, and K. Orginos, *Hierarchical probing for estimating the trace of the matrix inverse on toroidal lattices*, [arXiv:1302.4018](https://arxiv.org/abs/1302.4018).
5. J. Laeuchli and A. Stathopoulos, *Extending hierarchical probing for computing the trace of matrix inverses*, [DOI:10.1137/18M1176427](https://doi.org/10.1137/18M1176427).
