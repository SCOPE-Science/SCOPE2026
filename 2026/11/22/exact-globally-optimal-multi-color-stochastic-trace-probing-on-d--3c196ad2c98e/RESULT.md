# Exact globally optimal multi-color stochastic trace probing on divisible screened cycles

## Finding

**Theorem (all-budget strict class optimum).** Let \(k\ge3\) and \(m\ge2\) be integers, put \(n=km\), and let \(L_n\) be the combinatorial Laplacian of the unweighted cycle on vertices \(\{0,1,\ldots,n-1\}\). For every \(\mu>0\), put \(G=(\mu I+L_n)^{-1}\). Partition the vertices into exactly \(k\) nonempty classes and, independently for each class, evaluate one Rademacher quadratic form with entries \(\pm1\) on that class and zero elsewhere. Their sum is an unbiased estimator of \(\operatorname{tr}G\).

Among **all** such partitions, including unbalanced and improper graph colorings, the **unique** variance-minimizing unlabeled partition is
\[
  \bigl\{\{r,r+k,\ldots,r+(m-1)k\}:0\le r<k\bigr\}.
\]
For named colors there are exactly \(k!\) optimal assignments. Define
\[
 \alpha=\operatorname{arcosh}(1+\mu/2),\qquad
 g_d=\frac{e^{-\alpha d}+e^{-\alpha(n-d)}}{2\sinh\alpha\,(1-e^{-\alpha n})},
 \qquad 0\le d<n.
\]
The exact minimum variance is
\[
 \boxed{V_{n,k}(\mu)=2n\sum_{j=1}^{m-1}g_{jk}^{\,2}.}
\]
The optimal partition does not change with \(\mu\). For fixed \(n,k\) as \(\mu\to\infty\),
\[
 V_{n,k}(\mu)=
 \begin{cases}
 4n\mu^{-2k-2}(1+O_{n,k}(\mu^{-1})),&m\ge3,\\
 8n\mu^{-2k-2}(1+O_{n,k}(\mu^{-1})),&m=2.
 \end{cases}
\]
For comparison, the variance of the mean of \(k\) independent *full-support* Rademacher trace probes at the same \(k\)-solve budget is asymptotic to \((4n/k)\mu^{-4}\). Accordingly, the optimized-to-full variance ratio is asymptotic to \(k\mu^{-2(k-1)}\) if \(m\ge3\), or \(2k\mu^{-2(k-1)}\) if \(m=2\).

## Assumptions and scope

Each of the \(k\) class-supported sign vectors has independent symmetric Bernoulli entries on its support; different vectors are independent, and each class has at least one vertex. The matrix and quadratic forms are real. The cycle is undirected with unit edge weights, and \(\mu\) is any finite strictly positive real number. This theorem concerns the variance of this specific unbiased estimator at fixed cost \(k\), not a minimax statement over all possible coupled probes, nonuniform weights, or other trace-estimation methods. The divisibility condition \(k\mid n\) and \(m\ge2\) are essential to this statement. The two-class special case belongs to separate prior work and is not included in the claimed new range.

## Proof

**1. Exact Green entries and variance.** Let \(Q=\mu I+L_n\). The positive parameter \(\alpha\) satisfies \(2\cosh\alpha=\mu+2\). The periodically summed exponential Green kernel
\[
  G_{ij}=g_{d},\quad d\equiv i-j\pmod n,
  \qquad g_d=\frac{e^{-\alpha d}+e^{-\alpha(n-d)}}{2\sinh\alpha(1-e^{-\alpha n})}
\]
solves \(Qg_{\cdot}=e_0\), by the second-order nearest-neighbor difference equation away from \(0\) and its unit jump at \(0\). Since \(\mu>0\), \(Q\) is invertible and the formula is exact.

Writing \(\mathcal C\) for a partition into \(k\) nonempty classes, independence and \(\mathbb E\epsilon_i\epsilon_j=\mathbf1_{i=j}\) show unbiasedness. Expanding each centered quadratic form into \(2\sum_{i<j\text{ in class}}G_{ij}\epsilon_i\epsilon_j\), all pair cross-covariances vanish unless their unordered index pairs agree. Hence
\[
 \operatorname{Var}(\widehat T_{\mathcal C})=4\sum_{C\in\mathcal C}\sum_{\{i,j\}\subset C}g_{|i-j|}^2.
\]

**2. A strict cyclic equispacing inequality.** For real \(0\le x\le n\) define \(H(x)=g_x^2\), with the displayed exponential formula interpreted at real \(x\). It is symmetric about \(n/2\) and strictly convex, since if \(b=[2\sinh\alpha(1-e^{-\alpha n})]^{-1}\), then
\[
 H''(x)=4\alpha^2 b^2\left(e^{-2\alpha x}+e^{-2\alpha(n-x)}\right)>0.
\]
Consider a class \(C\) of size \(s\ge2\), whose cyclically ordered vertices have successive positive integer gaps summing to \(n\). Let \(d_{i,j}\) be the clockwise distance from its \(i\)-th point to its \(j\)-th successor, for \(j=1,\ldots,s-1\), with indices modulo \(s\). The identity \(\sum_i d_{i,j}=jn\) holds. Each unordered pair appears twice in the sum across all \(i,j\) because \(H(n-x)=H(x)\). Strict Jensen gives
\[
  \sum_{\{u,v\}\subset C}g_{|u-v|}^2
   =\frac12\sum_{j=1}^{s-1}\sum_{i=1}^{s}H(d_{i,j})
   \ge \frac{s}{2}\sum_{j=1}^{s-1}H(jn/s)=:\Phi(s).
\]
Equality requires all successive gaps to equal \(n/s\), using \(j=1\). Conversely equally spaced points achieve equality.

**3. Strict convexity in the class size.** Define \(q=e^{-\alpha n}\), \(c=2\alpha n\), and \(B=[4\sinh^2\alpha(1-q)^2]^{-1}\). A geometric sum yields, for every positive integer \(s\),
\[
 \Phi(s)=B\left[(1-q^2)\frac{s}{1-e^{-c/s}}-s+q\,s(s-1)\right].
\]
This formula extends continuously to \(s=0\), with \(\Phi(0)=0\). Write \(h(x)=(1-e^{-x})^{-1}\) for \(x>0\). Then
\[
 h''(x)=\frac{e^{-x}(1+e^{-x})}{(1-e^{-x})^3}>0,
\]
and, by differentiation of the perspective, for every \(s>0\),
\[
 \Phi''(s)=B\left[(1-q^2)\frac{c^2}{s^3}h''(c/s)+2q\right]>0.
\]
Thus \(\Phi\) is strictly convex on \([0,\infty)\), including the endpoint by continuity.

**4. Global minimization and uniqueness.** If the class sizes are \(s_1,\ldots,s_k\ge1\), with \(\sum s_i=n=km\), Steps 1–3 imply
\[
 \operatorname{Var}(\widehat T_{\mathcal C})
 \ge4\sum_{i=1}^k\Phi(s_i)
 \ge4k\Phi(m).
\]
The second strict Jensen inequality is an equality only for \(s_i=m\) for every color. The first is then an equality only when each class has constant cyclic gap \(n/m=k\). Those are exactly the \(k\) residue classes modulo \(k\); they form one unlabeled partition. Evaluating its within-class pair sum gives \(4k\Phi(m)=2n\sum_{j=1}^{m-1}g_{jk}^2\). This proves every assertion on global optima and ties.

**5. Strong-screening benchmark.** The Neumann expansion \((\mu I+L_n)^{-1}=\mu^{-1}\sum_{r\ge0}(-\mu^{-1}L_n)^r\) is convergent for sufficiently large \(\mu\). For cyclic distance \(d<n/2\), the first nonzero offdiagonal term at that distance is \(\mu^{-d-1}\); at antipodal distance \(d=n/2\), there are exactly two shortest paths, giving \(2\mu^{-d-1}\). In the residue partition the nearest same-class distance is \(k\). If \(m\ge3\), there are \(n\) unordered same-class pairs at that distance; if \(m=2\), there are \(n/2\) antipodal same-class pairs. Substitution proves both displayed leading constants. For full-support probes, the \(n\) nearest-neighbor edges have squared Green entries \(\mu^{-4}(1+O_n(\mu^{-1}))\), giving the stated benchmark and ratio.

## Verification

The accompanying standalone Python program `check_cycle_probing.py` uses exact rational linear algebra to verify resolvent entries, the variance formula (including exhaustive Rademacher-sign averaging on a six-cycle), and every unlabeled partition for several finite \((n,k,\mu)\) instances. Across the eight partition-search instances the checker compares 1,358,283 partitions, always finding exactly the residue partition as the unlabeled optimum. Its numerical experiments are **not** the proof of the universal theorem; the strict convexity/Jensen argument above supplies that proof.

Run with `python3 check_cycle_probing.py` using only the Python standard library.

## Relationship to prior work

Stathopoulos, Laeuchli and Orginos (first publicly posted February 17, 2013) established hierarchical and graph-distance probing for sparse inverse traces on periodic lattices. Their construction motivates color-supported probing and its computational cost, but the checked source does not classify *globally variance-minimizing* partitions for a fixed arbitrary number of independent supported sign probes, all positive screening parameters, and arbitrary unbalanced/improper competitors. A related published two-color result classifies the checkerboard on even screened cycles, but does not state the present \(k\ge3\) theorem. Classical circle-polarization work optimizes a max–min continuous potential, not this sum of within-color pair energies with integer class-size constraints.

## Limitations

The theorem assumes one independent supported sign vector per nonempty color and an exactly divisible unit-edge cycle. It does not establish analogous optimality for nondivisible cycle orders, inhomogeneous weights or screenings, coupled probes, or different optimality objectives. The strictness is for each finite \(\mu>0\), not at excluded boundary \(\mu=0\) or the formal limit \(\mu=\infty\). Although relevant primary literature and mathematical search results were compared, equivalent results outside the inspected/indexed sources remain possible.

## References

1. A. Stathopoulos, J. Laeuchli, K. Orginos, *Hierarchical Probing for Estimating the Trace of the Matrix Inverse on Toroidal Lattices*, arXiv:1302.4018v1 (publicly posted February 17, 2013), https://arxiv.org/pdf/1302.4018 .
2. D. P. Hardin, A. P. Kendall, E. B. Saff, *Polarization Optimality of Equally Spaced Points on the Circle for Discrete Potentials*, arXiv:1208.5261, https://arxiv.org/pdf/1208.5261 .
3. *Checkerboard probing uniquely minimizes two-color trace variance on screened cycles*, mathematical-result record `2026/11/8/SCOPE-checkerboard-probing-uniquely-minimizes-two-color-trace-variance--ad9f3c6dc76a`, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-checkerboard-probing-uniquely-minimizes-two-color-trace-variance--ad9f3c6dc76a .
4. H. M. Switzer, A. Stathopoulos, E. Romero, J. Laeuchli, K. Orginos, *Probing for the Trace Estimation of a Permuted Matrix Inverse Corresponding to a Lattice Displacement*, SIAM, DOI:10.1137/21M1422495, https://doi.org/10.1137/21M1422495 (abstract inspected).
