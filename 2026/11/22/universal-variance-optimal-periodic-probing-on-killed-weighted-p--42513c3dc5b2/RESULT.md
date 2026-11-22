# Universal variance-optimal periodic probing on killed weighted paths

## Finding

For **every** path length \(n\ge2\), **every** strictly positive set of path conductances and vertex killing rates, and **every** probe budget \(1\le k\le n\), the minimum-variance design using one independent class-supported Rademacher trace probe per class is the periodic partition
\[
C_r=\{i\in\{1,\ldots,n\}:i\equiv r\pmod{k}\},\qquad r=1,\ldots,k.
\]
This partition is the **unique** minimizer up to permuting color names. It minimizes the variance among *all* partitions into exactly \(k\) nonempty classes, without restricting competitors to proper or distance colorings. A strictly positive interval sum provides the exact excess variance of every competing design and a nonzero local certificate whenever a length-\(k\) window repeats a color.

## Assumptions and scope

Let \(P_n\) have ordered vertices \(1,\ldots,n\). Let \(c_i>0\) be the conductance on edge \((i,i+1)\) for \(1\le i<n\), and let \(q_i>0\) be an independent killing rate at vertex \(i\). Write
\[
A=\operatorname{diag}(q_1,\ldots,q_n)+L_c,
\qquad G=A^{-1}.
\]
The weighted Laplacian \(L_c\) has diagonal entries equal to incident conductance sums and adjacent entries \(-c_i\). Thus \(A\) is symmetric positive definite. The usual screened graph inverse \((\mu I+L_c)^{-1}\) is the special case \(q_i=\mu>0\). For a partition \(\mathcal C=(C_1,\ldots,C_k)\) into \(k\) nonempty sets, independently sample signs \(\epsilon_i\in\{-1,1\}\) on each class and put \(z_r(i)=\epsilon_i\) for \(i\in C_r\), zero otherwise. Use
\[
\widehat T_{\mathcal C}=\sum_{r=1}^k z_r^\top Gz_r.
\]
The signs are independent across all coordinates and classes. This estimator is unbiased for \(\operatorname{tr}G\) and its variance is
\[
V(\mathcal C)=2\sum_{r=1}^{k}\sum_{\substack{i,j\in C_r\\i\ne j}}G_{ij}^{2}.
\]
The count of probes is exactly \(k\), not \(k\) independent full-vector Hutchinson probes. No equal-weight, constant-killing, or large-length limit is assumed.

## Proof

**1. A strictly ordered Green factorization.** Define two sequences with unit boundary seeds: \(a_1=1\), \(b_n=1\). Taking \(c_0=c_n=0\) and omitting nonexistent boundary terms, define for \(1\le i<n\)
\[
a_{i+1}=a_i+\frac{q_i a_i+c_{i-1}(a_i-a_{i-1})}{c_i},
\]
and for \(n\ge i>1\)
\[
b_{i-1}=b_i+\frac{q_i b_i+c_i(b_i-b_{i+1})}{c_{i-1}}.
\]
Induction gives \(0<a_1<a_2<\cdots<a_n\) and \(b_1>b_2>\cdots>b_n>0\). Both satisfy \(Aa=0\) and \(Ab=0\) in the interior; the first sequence satisfies the left homogeneous endpoint equation and the second the right endpoint equation. The discrete Wronskian
\[
\omega=c_i(a_{i+1}b_i-a_i b_{i+1})>0
\]
is independent of \(i=1,\ldots,n-1\) by subtraction of the two interior equations. It follows by direct multiplication with \(A\), including both endpoints, that
\[
G_{ij}=\frac{a_{\min(i,j)}b_{\max(i,j)}}{\omega}.
\]
At a diagonal column \(j\), the jump from the left and right homogeneous solutions equals \(\omega/\omega=1\); all other rows vanish. Since \(A\) is invertible this identifies its inverse.

**2. An interval-rank-one decomposition with strictly positive coefficients.** Set \(u_i=a_i^2/\omega^2\), \(v_i=b_i^2\), and introduce \(u_0=0\), \(v_{n+1}=0\). The increments \(\Delta u_a=u_a-u_{a-1}\) and \(\Delta v_b=v_b-v_{b+1}\) are strictly positive, including the boundary increments. Therefore, for all \(1\le i,j\le n\),
\[
G_{ij}^2=u_{\min(i,j)}v_{\max(i,j)}
=\sum_{1\le a\le b\le n}\Delta u_a\Delta v_b\,{\bf1}_{[a,b]}(i){\bf1}_{[a,b]}(j).
\]
The second identity is a product of two telescoping sums: \(\sum_{a\le\min(i,j)}\Delta u_a=u_{\min(i,j)}\) and \(\sum_{b\ge\max(i,j)}\Delta v_b=v_{\max(i,j)}\). The restriction \(a\le b\) is automatic for every summand contributing to a pair \(i,j\).

**3. The exact discrete variance gap.** Let \(N_r[a,b]=|C_r\cap[a,b]|\), let \(m=b-a+1\), and write \(m=ks+t\), with \(0\le t<k\). The elementary smoothing inequality \((x+1)^2+(y-1)^2<x^2+y^2\) whenever \(y\ge x+2\) proves that the smallest value of \(\sum_{r=1}^k N_r[a,b]^2\), over nonnegative integer counts summing to \(m\), is
\[
B_k(m)=(k-t)s^2+t(s+1)^2.
\]
Every length-\(m\) interval in the periodic residue partition has \(t\) color counts equal to \(s+1\) and the others equal to \(s\). Using the variance formula, the interval decomposition and cancellation of diagonal terms therefore gives for *every* partition
\[
\boxed{
V(\mathcal C)-V_*
=2\sum_{1\le a\le b\le n}\Delta u_a\Delta v_b
\left(\sum_{r=1}^k N_r[a,b]^2-B_k(b-a+1)\right)\ge0.
}
\]
The constant \(V_*\) is the variance of the periodic residue partition, so this identity is an explicit finite formula for both its optimal value and every excess variance. All summands are nonnegative.

**4. Exhaustive classification of equality and a strict local certificate.** For \(k=1\) only one partition exists. For \(k\ge2\), equality in the boxed identity forces all \(k\)-vertex windows to have exactly one vertex from each class, since their weights \(\Delta u_a\Delta v_{a+k-1}\) are strictly positive. Comparing consecutive windows shows the departing color equals the entering color: \(\operatorname{col}(i+k)=\operatorname{col}(i)\) for \(1\le i\le n-k\). Thus all colors are repeated in the periodic residue order, and there is precisely one unlabeled optimizer (exactly \(k!\) labeled optimizers). In fact, a length-\(k\) window with any color collision has count-square excess at least \(2\), yielding the explicit lower bound
\[
V(\mathcal C)-V_*\ge4\sum_{a=1}^{n-k+1}
\Delta u_a\Delta v_{a+k-1}
\,{\bf1}_{\{\text{some color repeats on }[a,a+k-1]\}}.
\]
Every nonperiodic partition has at least one offending window. This proves uniqueness and strictness for all finite lengths, budgets and positive parameters.

## Verification

A standalone Python 3 exact-arithmetic checker is supplied as `verify.py`. It uses `fractions.Fraction` to invert actual weighted tridiagonal matrices independently, reconstruct the discrete Wronskian, verify the interval decomposition entry by entry, and enumerate every unlabeled partition on each path of lengths \(2\) through \(7\) for three distinct rational conductance/killing patterns. It independently verifies nonnegative variance gaps, the equality characterization, exact excess-variance identity and quantitative window lower bound. Its recorded outcome is **14,337 exact assertions passed**. The finite enumeration is a regression check only; the all-length theorem is proved by the argument above.

## Relationship to prior work

Stathopoulos–Laeuchli–Orginos (2013) introduced graph-distance and hierarchical probing for inverse trace estimation. Frommer–Schimmel–Schweitzer (2020) explicitly give the periodic residue coloring for banded matrices as a *minimum-color distance-coloring*; that is a different optimization problem from minimum Rademacher variance over *every* fixed-budget partition, and their result does not incorporate arbitrary positive killing and edge weights. Frommer–Rinelli–Schweitzer (2023) analyze the stochastic-probing variance and error bounds but do not assert the complete universal global optimizer characterization above. The new step is the positive all-interval Green-kernel decomposition and the consequent exact variance-gap/uniqueness law. Existing exact results for even cycles and complete bipartite resolvents concern different graph families and do not directly imply this weighted open-path statement.

## Limitations

The result assumes a path, positive conductances and strictly positive killing at **every** vertex, and independent class-supported Rademacher signs with exactly one vector per class. It does not cover cycles, branching trees, general tridiagonal matrices with sign-indefinite off-diagonals, zero killing rates, Gaussian probes, correlated probes, or a fixed total of independent *full* Hutchinson probes. It establishes statistical variance optimality for exact matrix-vector products, not floating-point solve-time optimality. Publication priority beyond the inspected literature and indexed mathematical records is not independently certified.

## References

- A. Stathopoulos, J. Laeuchli, K. Orginos, *Hierarchical probing for estimating the trace of the matrix inverse on toroidal lattices* (first publicly available 17 February 2013), https://arxiv.org/abs/1302.4018, in particular Section 1 and the hierarchical coloring construction.
- A. Frommer, C. Schimmel, M. Schweitzer, *Analysis of probing techniques for sparse approximation and trace estimation of decaying matrix functions* (first public 3 September 2020), https://arxiv.org/abs/2009.01589, in particular Section 2.1 and equation (9).
- A. Frommer, M. Rinelli, M. Schweitzer, *Analysis of stochastic probing methods for estimating the trace of functions of sparse symmetric matrices* (first public 15 August 2023), https://arxiv.org/abs/2308.07722, in particular the definition of the stochastic method and its variance analysis.
