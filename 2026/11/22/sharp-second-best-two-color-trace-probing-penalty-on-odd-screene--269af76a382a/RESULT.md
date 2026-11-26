# Sharp second-best two-color trace-probing penalty on odd screened cycles

## Finding

Let \(n=2m+1\ge5\), let \(\mu>0\), and let \(G=(\mu I+L(C_n))^{-1}\), where the vertices are indexed modulo \(n\). Partition the vertices into two nonempty color classes. Sum the two independent Rademacher quadratic forms, each supported on one class, to estimate \(\operatorname{tr}G\) in two solves. Let \(V(s)\) be the variance, with \(s\in\{-1,1\}^n\) denoting the color word. Define
\[
r+r^{-1}=\mu+2,\quad 0<r<1,\qquad
c=\frac1{(r^{-1}-r)(1-r^n)},\qquad f_d=c^2(r^d+r^{n-d})^2.
\]

**Sharp gap.** Among partitions that do not minimize the variance, the smallest variance is precisely \(V_{\min}+\Delta_n\), where
\[
\Delta_5=8(f_1-f_2)=8c^2r^2(1-r^2)(1-r^4),
\qquad
\Delta_n=8(f_1-2f_2+f_3)=8c^2(1-r^2)^2(r^2+r^{2n-6})\quad(n\ge7).
\]
Both expressions are strictly positive. An attaining nonoptimal word is obtained from \(s_j^*=(-1)^j\), for \(0\le j<n\), by flipping just \(s_2^*\) and \(s_3^*\).

The one-defect baseline is also established in [1]: a partition minimizes variance exactly when it has one monochromatic adjacent edge, and then
\[
V_{\min}=2\sum_{d=1}^m[n+(-1)^d(n-2d)]f_d.
\]
This comprises \(n\) partitions up to color exchange, or \(2n\) labeled spin words. The new quantitative claim is the exact first gap above that minimum, not the formula for the baseline or the one-defect classification.

## Assumptions and scope

The cycle is simple; any partition into two nonempty classes is permitted, including improper and unbalanced colorings. Within a class the signs are independent and symmetric at distinct sites, and the two probes are independent. The only design variable is the partition. No optimization is claimed over correlated probes, other solve counts or arbitrary trace estimators.

## Proof

**Green function and estimator.** Set \(g_d=c(r^d+r^{n-d})\) for \(0\le d\le n\). This sequence is periodic at the endpoints, symmetric under \(d\mapsto n-d\), and satisfies \((\mu+2)g_d-g_{d-1}-g_{d+1}=\mathbf 1_{d=0}\) with cyclic indices. Indeed, the characteristic identity gives the recurrence off zero, and at zero the left side equals \(c(r^{-1}-r)(1-r^n)=1\). Thus \(G_{ij}=g_{j-i\bmod n}\). The diagonal terms of each Rademacher quadratic form are deterministic, and its unordered off-diagonal products are pairwise uncorrelated. Consequently the estimator is unbiased and
\[
V(s)=4\sum_{i<j:\,s_i=s_j}G_{ij}^2
=2\sum_{d=1}^m f_d(n+C_d(s)),\qquad C_d(s)=\sum_{i=0}^{n-1}s_i s_{i+d}.
\]
Equivalently, the variance is a constant plus twice the antiferromagnetic pair energy \(\sum_{i<j} f_{d(i,j)}s_i s_j\) at cyclic distance \(d(i,j)\). The Ising gap in this energy normalization is \(\Delta_n/2\).

**Window decomposition.** Let \(S=\sum_i s_i\) and \(T_k(s)=\sum_i(\sum_{j=0}^{k-1}s_{i+j})^2\) for \(2\le k\le m\). Then \(\sum_{d=1}^m C_d=(S^2-n)/2\) and \(T_k=nk+2\sum_{d<k}(k-d)C_d\). Define
\[
a_m=\tfrac12(f_{m-1}-f_m),\qquad
a_k=\tfrac12(f_{k-1}-2f_k+f_{k+1})\quad(2\le k<m).
\]
These are positive: \(f_d=c^2(r^{2d}+r^{2n-2d}+2r^n)\) strictly decreases up to \(m\) and has strictly positive interior second differences. Telescoping gives \(f_d-f_m=2\sum_{k=d+1}^m (k-d)a_k\). Substitution yields
\[
V(s)-V(s^*)=f_m(S^2-1)+2\sum_{k=2}^m a_k[T_k(s)-T_k(s^*)].
\]
Each difference displayed is nonnegative. In fact \(S^2\ge1\) by parity; for odd \(k\) every window sum has square at least one, while for even \(k\) its sum \(u\) satisfies \(u^2\ge2|u|\), so \(T_k\ge2k|S|\ge2k\). The reference word saturates these bounds. For windows that cross its unique defect, the two alternating pieces each end at the defect with a plus sign. At odd length exactly one piece has odd length, contributing a window sum of one; at even length a sum of two occurs exactly when both pieces have odd length, in \(k/2\) windows. Windows avoiding the defect are strictly alternating. Thus the reference gives \(S^2=1\), \(T_k=n\) for odd \(k\) and \(2k\) for even \(k\). Its correlation is \((-1)^d(n-2d)\) since exactly \(d\) directed distance-\(d\) pairs wrap past the defect. This proves the minimum formula.

**Exact second-best penalty.** Let \(b\) count monochromatic adjacent bonds. The number of sign changes around a ring is even, so \(b\) is odd and \(T_2=4b\). Positivity of \(a_2\) in the certificate proves that any minimizing word has just one defect; all those words are rotations or global flips of \(s^*\). A nonoptimal word has \(b\ge3\), which gives a variance excess of at least \(16a_2\).

Flip entries 2 and 3 of \(s^*\). This leaves \(S\) unchanged and creates two additional monochromatic bonds. For any \(3\le k\le m\), only two window sums can change: the one ending at site 2 and the one starting at site 3. All other windows contain both flips (which cancel in the sum) or neither. For odd \(k\) these two window sums are respectively \(1,-1\) before the flip and \(-1,1\) after it. For even \(k\) they are \(2,0\) before the flip and \(0,2\) after it. The left window wraps at the defect for \(k\ge4\); the right one does not wrap since \(k\le m\). Therefore \(T_k\) is preserved for \(k\ge3\) and the excess is exactly \(16a_2\). Using the endpoint coefficient for \(m=2\) and the interior coefficient otherwise gives the claimed formulas.

**Comparison at the same solve count.** Two averaged independent full-support Hutchinson probes have variance \(V_{H,2}=2n\sum_{d=1}^m f_d\). Thus
\[
\frac{V_{\min}}{V_{H,2}}=\frac{\sum_{d=1}^m[n+(-1)^d(n-2d)]f_d}{n\sum_{d=1}^m f_d}.
\]
As odd \(n\to\infty\) at fixed \(\mu\), for fixed \(d\) the numerator coefficient divided by \(n\) tends to two for even \(d\) and zero for odd \(d\). Since \(f_d\) is dominated by a constant times \(r^{2d}\) uniformly for \(d\le m\), the ratio tends to \(2\sum_{j\ge1}r^{4j}/\sum_{d\ge1}r^{2d}=2r^2/(1+r^2)\).

## Verification

The claim is proved by the analytic window decomposition and explicit witness. The unchanged `check.py` is an exact rational diagnostic for \(n=5,7,9,11,13\) and \(r=1/4,1/2,3/4\); it checks the variance, minimum and sharp gap, witness, windows and Green recurrence. The packaged finite check reports 15 parameter cases, 16,368 spin tests and 135 recurrence tests. These finite data do not replace the all-parameter proof.

## Relationship to prior work

The odd-cycle result [1] gives the same two-class variance baseline, the same one-defect optimality classification and an asymptotic parity-frustration correction. Its baseline is credited here; the present sharp finite gap compares the global optimum to the **best nonoptimal partition**, not to a different graph size or asymptotic benchmark. No ordering between same-date records is inferred. Kerimov [2] and the Hubbard criterion concern ground-state ordering in one-dimensional long-range antiferromagnets. Switzer et al. [3] give probing background, and the even-cycle checkerboard law [4] and complete-bipartite transition [5] concern other graph families. None of those comparisons is used to claim novelty for the Rademacher variance calculation or for the one-defect minimum.

## Limitations

The exact gap treats the stated odd simple cycles, uniform positive screening and independent class-supported probes. It is not a lower bound for arbitrary trace estimators. Equivalent first-excitation results in the weighted circulant-cut or Ising literature remain a priority risk.

## References

1. *Odd-cycle stochastic trace probing: a unique frustrated bond and the parity penalty*, https://github.com/Resultary/2026/blob/main/2026/11/22/SCOPE-odd-cycle-stochastic-trace-probing-a-unique-frustrated-bond-and--82aa4e3655f0/RESULT.md
2. A. Kerimov, *Ground state criteria in one-dimensional antiferromagnetic Ising model with long range interaction*, https://doi.org/10.1063/5.0001423
3. H. Switzer, A. Stathopoulos, E. Romero, J. Laeuchli and K. Orginos, *Probing for the Trace Estimation of a Permuted Matrix Inverse Corresponding to a Lattice Displacement*, https://arxiv.org/abs/2106.01275
4. *Checkerboard probing uniquely minimizes two-color trace variance on screened cycles*, https://github.com/Resultary/2026/tree/main/2026/11/8/SCOPE-checkerboard-probing-uniquely-minimizes-two-color-trace-variance--ad9f3c6dc76a
5. *Sharp two-color stochastic-probing transition on complete bipartite resolvents*, https://github.com/Resultary/2026/tree/main/2026/11/8/SCOPE-sharp-two-color-stochastic-probing-transition-on-complete-bipart--1edc2b42b895
