# Sharp hub-allocation staircase and a nonvanishing refinement gap for stochastic trace probing on stars

## Finding

Let the unit-edge star have a hub and \(m\) leaves, where \(m\ge2\). Let \(\mu>0\), \(G_\mu=(\mu I+L)^{-1}\), and let \(2\le k\le m+1\) be an integer. Among **all** partitions of the \(m+1\) vertices into exactly \(k\) nonempty classes, use one independent class-supported Rademacher quadratic form per class to estimate \(\operatorname{tr}G_\mu\). There is no requirement that the classes properly color the graph.

Define \(q=k-1\), \(R=(1+\mu)^2\), and, for \(t\ge q\), write \(t=qa+b\), \(0\le b<q\), and put
\[
 B_q(t)=(q-b)\binom a2+b\binom{a+1}2.
\]
For integer \(0\le h\le m-q\), define
\[
 F_{m,k,\mu}(h)=\binom h2+Rh+B_q(m-h).
\]
Then the exact minimum variance is
\[
 \boxed{\mathcal V_k(m,\mu)=\frac{4}{\mu^2(1+\mu)^2(\mu+m+1)^2}\min_{0\le h\le m-k+1}F_{m,k,\mu}(h).}
\]
**Every** minimizer, and no other partition, is obtained by choosing one minimizing \(h\), grouping the hub with precisely \(h\) arbitrarily chosen leaves, and partitioning the other \(m-h\) leaves into \(q\) nonempty classes whose sizes differ by at most one. All minimizing \(h\) are described by the strictly increasing finite differences
\[
 F(h+1)-F(h)=h+R-\left\lfloor\frac{m-h-1}{k-1}\right\rfloor
 \quad(0\le h<m-k+1).
\]
There is one minimizing \(h\), except that exactly two consecutive values minimize at an equality. In particular, a singleton hub class is optimal if and only if
\[
 \boxed{(1+\mu)^2\ge\left\lfloor\frac{m-1}{k-1}\right\rfloor.}
\]
This is the sharp finite-size hub-isolation threshold; as screening increases, the optimal number of leaves sharing the hub descends through an explicit staircase. The number of unlabeled minimizing partitions is exactly
\[
 \sum_{h\in H_*}\binom mh\frac{(m-h)!}{(a_h!)^{q-b_h}((a_h+1)!)^{b_h}(q-b_h)!b_h!},
\]
where \(H_*\) is the minimizer set, \(m-h=qa_h+b_h\), and \(0\le b_h<q\).

A second conclusion quantifies the cost of preserving earlier work in a restricted nested-class scheme. Fix an integer \(k\ge2\) and a real \(\mu>0\), then let \(m\to\infty\). Start from **any** optimal \(k\)-class partition and form \(k+1\) classes by splitting precisely one of its classes, retaining all other classes unchanged. Denote the minimum variance among all such one-split refinements by \(\mathcal V_{k\to k+1}^{\mathrm{split}}(m,\mu)\). Uniformly over the choice of an optimal parent partition,
\[
 \boxed{\lim_{m\to\infty}\frac{\mathcal V_{k\to k+1}^{\mathrm{split}}(m,\mu)}{\mathcal V_{k+1}(m,\mu)}=1+\frac{k-1}{2k^2}>1.}
\]
For the first refinement, this is the sharp asymptotic ratio \(9/8\). Thus even an optimally chosen single-class subdivision incurs a nonvanishing variance penalty against redesigning all \(k+1\) classes.

## Assumptions and scope

The graph is precisely the unweighted star \(K_{1,m}\) with its **combinatorial**, unnormalized Laplacian; all vertex screening values equal \(\mu>0\). Each class receives one independently signed, zero-outside-class Rademacher vector, independently across classes, and one exact quadratic form. Variance means ordinary variance of the sum of these \(k\) quadratic forms (not sample-mean variance, and not deterministic Hadamard trace error). The classification covers all nonempty, potentially improper, nonuniform class partitions. The asymptotic claim holds with \(k\) and \(\mu\) fixed as the leaf count grows; it does not assert uniformity when either varies with \(m\).

## Proof

**Exact resolvent and variance.** Order the hub first. Block inversion of
\[
 \mu I+L=\begin{pmatrix}\mu+m&-\mathbf1^\mathsf T\\-\mathbf1&(\mu+1)I_m\end{pmatrix}
\]
gives, for distinct leaves \(i,j\),
\[
 G_{0i}=\frac1{\mu(\mu+m+1)},\qquad
 G_{ij}=\frac1{\mu(\mu+1)(\mu+m+1)}=:a.
\]
The first value is \((1+\mu)a\). For a real symmetric matrix and independent class-supported Rademacher vectors, diagonal terms are deterministic and off-diagonal sign products give
\[
 \operatorname{Var}\!\left(\sum_C z_C^\mathsf TG_\mu z_C\right)
 =4\sum_C\sum_{i<j\in C}(G_\mu)_{ij}^2.
\]
For a class containing the hub plus \(h\) leaves and other leaf-only classes with respective sizes \(r_1,\ldots,r_q\), division by \(4a^2\) gives exactly \(\binom h2+Rh+\sum_{j=1}^q\binom{r_j}2\).

**Balancing and discrete convexity.** At fixed \(h\), if any two leaf-only classes have sizes differing by at least two, moving one leaf from larger to smaller strictly decreases the pair count. Hence exactly the near-equal sizes attain the minimum \(B_q(m-h)\). One additional leaf added to the hub class changes its cost by \(h+R\), whereas removing a leaf from an optimally balanced \(q\)-class allocation lowers its cost by \(\lfloor(m-h-1)/q\rfloor\). This proves the displayed finite difference. Consecutive differences increase by at least one, so the first nonnegative difference (or the endpoint when none exists) characterizes the optimal \(h\), with a two-way tie only if a difference vanishes. At \(h=0\), that difference proves the exact isolation threshold. Multinomial counting of distinct balanced unlabeled leaf-only classes proves the optimizer count.

**Sharp nested-refinement asymptotics.** For fixed \(k\) and \(\mu\), the two-sided optimality inequalities implied by the finite differences give \(h=m/k+O_{k,\mu}(1)\). Therefore **every** class of **every** optimal \(k\)-class parent has \(m/k+O_{k,\mu}(1)\) vertices. For any class of size \(s=m/k+O(1)\), splitting it into two groups minimizes the leading quadratic pair count when the groups have sizes \(s/2+O(1)\), and achieves the lower bound \(s^2/4+O(m)\) for their total \(\binom{\cdot}{2}\) count. The extra hub–leaf squared-weight contribution, relative to leaf–leaf weight, is \((R-1)h=O_{k,\mu}(m)\). Consequently the best one-split normalized energy is
\[
 \frac{m^2}{2}\left(\frac{k-1}{k^2}+\frac1{2k^2}\right)+O_{k,\mu}(m),
\]
while an unrestricted optimal \(k+1\)-class design has energy \(m^2/[2(k+1)]+O_{k,\mu}(m)\). Multiplying by the common positive factor \(4a^2\), dividing, and passing to the limit yields \((k+1)(k-1/2)/k^2=1+(k-1)/(2k^2)\). Both the lower bound and the matching balanced split apply to every optimal parent, establishing the stated uniformity and sharpness.

## Verification

The standalone file `verify_star.py` uses exact rational arithmetic throughout its finite tests. It independently enumerates unlabeled set partitions in restricted-growth-string order for every \(2\le m\le8\), every \(2\le k\le m+1\), and four rational screenings; it compares the global minimum, every optimal hub occupancy, and the exact number of minimizing partitions with the theorem. A separate rational Gauss–Jordan inverse check verifies the stated star Green entries and the direct full-matrix variance. Additional exact rational tests include the sharp isolation boundary and one-split asymptotic scaling examples. Running `python verify_star.py` prints `PASS: 367 exact-rational comparisons / identities`.

A concrete nonnesting witness has \(m=12\), \(\mu=1/2\). Every two-class optimum has class sizes \((6,7)\), while every three-class optimum has class sizes \((3,5,5)\); hence no globally optimal three-class partition refines an optimal two-class partition. In normalized pair-cost units, the optimal costs are \(169/4\) (two classes), \(51/2\) (three classes), and \(117/4\) (best single split of an optimal two-class parent); the last-to-unrestricted ratio is exactly \(39/34\).

## Relationship to prior work

The earlier hierarchical-probing framework of Stathopoulos, Laeuchli, and Orginos constructs nested graph-distance colorings, particularly for periodic lattices, and motivates the computational interest in retaining earlier probes. It does not state a global fixed-budget variance optimum for unrestricted partitions on stars. Frommer, Rinelli, and Schweitzer give the general class-supported stochastic-probing variance identity, used here as context; that identity alone does not classify optimal star partitions, compute hub-screening transitions, or give the asymptotic one-split penalty. Published work on two-color complete-bipartite graph probing includes the star as a two-class special case, but does not imply the multi-class or cross-budget assertions here. The present theorem compares one-split **independent class-supported estimators**, not the full correlated Hadamard hierarchy, and must not be interpreted as a performance lower bound for every hierarchical probing algorithm.

## Limitations

This is a structured star-graph theorem, not a result for arbitrary trees or all graph colorings. It concerns independent supported-sign estimators with one probe per color, not shared-sign hierarchical probes, optimally unequal sample counts, Gaussian probes, or inexact solves. The finite enumeration is not used as an infinite proof. The fixed-screening asymptotic does not cover moving screening or probe budgets. Although relevant sources and indexed results were compared, publication priority remains conditional on unindexed literature, particularly an inaccessible full version of the 2020 hierarchical-probing extension; no independent mathematical audit or priority certification is claimed.

## References

1. A. Stathopoulos, J. Laeuchli, and K. Orginos, *Hierarchical probing for estimating the trace of the matrix inverse on toroidal lattices*, first arXiv version dated 17 February 2013, [arXiv:1302.4018](https://arxiv.org/abs/1302.4018), SIAM J. Sci. Comput. 35 (2013), S299–S322.
2. A. Frommer, M. Rinelli, and M. Schweitzer, *Analysis of stochastic probing methods for estimating the trace of functions of sparse symmetric matrices*, [arXiv:2308.07722](https://arxiv.org/abs/2308.07722), Math. Comp. 94 (2025), 801–823.
3. J. Laeuchli and A. Stathopoulos, *Extending hierarchical probing for computing the trace of matrix inverses*, [DOI:10.1137/18M1176427](https://doi.org/10.1137/18M1176427), SIAM J. Sci. Comput. 42 (2020), A1459–A1485 (abstract and bibliographic material inspected; full text not obtained).
4. *Sharp two-color stochastic-probing transition on complete bipartite resolvents*, [published research record](https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-sharp-two-color-stochastic-probing-transition-on-complete-bipart--1edc2b42b895) (two-color comparison only; full content inaccessible).
