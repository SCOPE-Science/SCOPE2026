# All-budget optimal Rademacher probing partitions on screened star graphs

## Finding
For each star graph \(K_{1,m}\) with \(m\ge 2\) leaves, screening shift \(\mu>0\), and integer probe budget \(3\le k\le m+1\), consider the unbiased trace estimator for \(B=(\mu I+L)^{-1}\) formed by one independent Rademacher quadratic-form probe on each of exactly \(k\) nonempty, disjoint vertex classes. **All globally variance-minimizing partitions** have the following form: the hub shares its class with \(h\) leaves, and the other \(m-h\) leaves are distributed as equally as possible among the other \(k-1\) nonempty classes. The only allowable values of \(h\) are the minimizers of one explicitly given strictly discrete-convex finite sequence.

Set \(r=k-1\), \(\alpha=(\mu+1)^2\), and for integers \(N\ge r\), write \(N=rq+t\) with \(0\le t<r\), and set
\[
g_r(N)=r\binom q2+tq,\qquad
F(h)=\alpha h+\binom h2+g_r(m-h),\quad 0\le h\le m-r.
\]
Then the exact global minimum variance is
\[
\boxed{V_{m,k}(\mu)=\frac{4}{\mu^2(\mu+1)^2(\mu+m+1)^2}\min_{0\le h\le m-r}F(h).}
\]
Each minimizing \(h\) gives precisely those optimal partitions described above, and no others, up to relabeling classes and permuting leaves. Their \(h\)-values form either a singleton or two consecutive integers, with all ties included. In particular, a *proper* coloring (hub alone, \(h=0\)) is optimal exactly when
\[
\boxed{(\mu+1)^2\ge\left\lfloor\frac{m-1}{k-1}\right\rfloor.}
\]
When the inequality is strict, the hub-alone choice is the unique optimal hub occupancy. At equality with \(k\le m\), both \(h=0\) and \(h=1\) optimize and no other hub occupancies do. When the inequality is reversed, every optimal partition is improper (one or more hub-leaf edges lies inside a class). The dependence on the probe budget is exact for all allowed integers, not an asymptotic statement.

For example, with nine leaves, three classes, and \(\mu=1/2\), the optimal class occupancies are hub-plus-one-leaf and two blocks of four leaves. Its variance is exactly \(7/64\), or \(10.9375\%\), lower than that of the best proper partition, using the same three probes.

## Assumptions and scope
The star has one central vertex \(0\), \(m\) distinct leaves \(1,\ldots,m\), and unit edge weights. The symmetric combinatorial Laplacian is \(L\). The matrix \(B=(\mu I+L)^{-1}\) is positive definite for \(\mu>0\). Fix an integer budget \(k\in\{3,\ldots,m+1\}\). A partition is exactly \(k\) nonempty vertex classes; properness is not required. For every class \(C\), a probe \(z_C\) has independent symmetric signs on \(C\) and zero elsewhere; all class probes are independent. The estimator is \(T=\sum_C z_C^{\mathsf T}Bz_C\). Every such partition uses exactly \(k\) quadratic forms. We optimize variance over *all* these partitions only, not over general correlated probes, variable weights, or variable cost.

## Proof
**1. Explicit off-diagonal resolvent.** With the hub ordered first, \(\mu I+L\) has hub diagonal \(\mu+m\), leaf diagonal \(\mu+1\), and hub-to-leaf entries \(-1\). Schur complementation of the leaf block yields a scalar Schur complement
\[
S=\mu+m-\frac m{\mu+1}=\frac{\mu(\mu+m+1)}{\mu+1}.
\]
Consequently, all hub-to-leaf entries of \(B\) equal
\[
a=\frac1{\mu(\mu+m+1)},
\]
and all off-diagonal distinct-leaf entries equal
\[
b=\frac1{\mu(\mu+1)(\mu+m+1)}.
\]
Thus \(a^2/b^2=(\mu+1)^2=\alpha>1\). These are exact identities for every \(m\ge2\) and \(\mu>0\).

**2. Variance as a partition energy.** For a real symmetric matrix, expansion of independent Rademacher fourth moments gives
\[
\operatorname{Var}(z_C^{\mathsf T}Bz_C)=4\sum_{i<j,\ i,j\in C} B_{ij}^2.
\]
Different classes' probes are independent, so their variances add. Let \(h\) be the number of leaves sharing the hub class and let \(s_1,\ldots,s_r\ge1\) be the remaining class sizes, with \(\sum s_i=m-h\). Substituting the two resolvent-entry values gives exactly
\[
\operatorname{Var}(T)=4b^2\left[\alpha h+\binom h2+\sum_{i=1}^r\binom{s_i}2\right],\quad 0\le h\le m-r.
\]
No possible partition is omitted: every feasible partition has exactly one such occupancy description, and each feasible integer occupancy is realized by a partition.

**3. Complete balancing of leaf-only classes.** If \(s_i\ge s_j+2\), transferring one leaf from class \(i\) to \(j\) lowers the bracket by exactly \(s_i-s_j-1>0\). Therefore every minimum for fixed \(h\) has leaf-only class sizes differing by at most one. Conversely all such balanced allocations give the same minimum \(g_r(m-h)\), since \(m-h=rq+t\) forces exactly \(t\) classes of size \(q+1\) and \(r-t\) of size \(q\). This proves the formula and the complete equality classification for fixed \(h\).

**4. Strict discrete convexity and hub occupancy.** The exact first difference for each \(0\le h<m-r\) is
\[
F(h+1)-F(h)=\alpha+h-\left\lfloor\frac{m-h-1}{r}\right\rfloor.
\]
The right-hand side increases strictly as \(h\) increases, because its linear part increases by one and the floor term cannot increase. Thus the minimizing \(h\)-set is either one integer or exactly two consecutive integers, and every optimum is classified by steps 2–3. The first difference is \(\alpha-\lfloor(m-1)/r\rfloor\). Therefore \(h=0\) is globally optimal exactly when it is nonnegative; if it vanishes and the difference exists, strict increase ensures precisely the tie \(h=0,1\). When \(k=m+1\), only \(h=0\) is feasible, and the same displayed criterion holds since its right side is zero. Reversing the inequality strictly forces \(h\ge1\) for every minimizer. This completes the claimed global classification, sharp transition, and all equality cases.

**5. Exact three-probe example.** Take \(m=9\), \(k=3\), and \(\mu=1/2\), hence \(r=2\), \(\alpha=9/4\). Directly from the finite function, \(F(0)=16\), \(F(1)=57/4\), and strict discrete convexity places the unique minimum at \(h=1\). The normalized ratio of optimal variance to the best proper variance is \((57/4)/16=57/64\), yielding a relative saving of \(7/64\). The hub class and other classes have the sizes asserted in the finding.

## Verification
The self-contained standard-library script `verify.py` carries out exact rational Gauss–Jordan inversion of screened star Laplacians, independently confirms the off-diagonal entry formulas, enumerates every unlabeled nonempty class partition of the tested small stars, compares its exact matrix-derived quadratic-form variance with the explicit integer formula, and verifies optimal hub counts and selected ties. Its completed run reports 35,280 rational partition comparisons for star leaf counts \(2\) through \(7\), all available class budgets \(k\ge3\), and seven positive rational screening shifts. These finite checks are *supplementary*: the arbitrary-size and arbitrary-positive-real-shift conclusions follow from the explicit Schur complement and discrete-convex proof. Run `python verify.py`; the recorded output is in `VERIFY_OUTPUT.txt`.

## Relationship to prior work
Frommer, Rinelli and Schweitzer (arXiv:2308.07722v1, Theorem 3.3 and Lemma 3.5) derive stochastic-probing variance formulas for a fixed partition; the standard sign fourth-moment identity used in step 2 is not novel. Their partition discussions concern graph-distance colorings and estimator variance with predetermined color classes. Hierarchical probing as developed by Stathopoulos, Laeuchli and Orginos (arXiv:1302.4018) similarly motivates graph-partition-based trace estimation without providing this all-budget star-graph optimum. A closest publicly available theorem, *Sharp two-color stochastic-probing transition on complete bipartite resolvents* (2026), optimizes **exactly two** classes for \(K_{p,q}\) and includes stars in its two-class specialization. It does not classify the different feasible set with every \(k\ge3\), the discrete-convex hub occupancies, or the budget-dependent properness boundaries established here. The comparison is by logical coverage, not just title matching.

## Limitations
The theorem concerns a deliberately structured graph and the specified independent class-restricted Rademacher probes. Its proof does not extend to arbitrary weighted graphs, correlated probes, optimally allocated repeats, general matrix functions, or runtime savings. The exact balancing argument uses leaf permutation symmetry; application to nonsymmetric graphs is not established. The result is a complete finite-dimensional classification, not a general stochastic-probing algorithm. A specialized historical weighted-partition result may imply the same formulas, so independent publication-priority verification is still required.

## References
1. A. Frommer, M. Rinelli and M. Schweitzer, *Analysis of stochastic probing methods for estimating the trace of functions of sparse symmetric matrices*, arXiv:2308.07722v1, publicly released 15 August 2023, Theorem 3.3, Lemma 3.5 and Section 3.2. https://arxiv.org/abs/2308.07722
2. E. Hallman and A. Troester, *A multilevel approach to stochastic trace estimation*, arXiv:2103.10516v1, 2021. https://arxiv.org/abs/2103.10516
3. A. Stathopoulos, J. Laeuchli and K. Orginos, *Hierarchical probing for estimating the trace of the matrix inverse on toroidal lattices*, arXiv:1302.4018, 2013. https://arxiv.org/abs/1302.4018
4. *Sharp two-color stochastic-probing transition on complete bipartite resolvents*, public research record (2026). https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-sharp-two-color-stochastic-probing-transition-on-complete-bipart--1edc2b42b895
