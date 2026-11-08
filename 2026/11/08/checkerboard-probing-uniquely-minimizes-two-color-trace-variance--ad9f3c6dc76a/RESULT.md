# Checkerboard probing uniquely minimizes two-color trace variance on screened cycles

## Finding

For every even integer \(n\ge4\) and every \(\mu>0\), let \(P\) be the cyclic shift on \(n\) coordinates, set
\[
 A_\mu=(\mu+2)I-P-P^{\mathsf T},\qquad G=A_\mu^{-1},
\]
and choose any partition of the coordinate set into two nonempty colors. Draw independent fair signs \(\xi_i\in\{-1,1\}\), restrict the same sign vector to each color, and sum the two quadratic forms \(\xi^{\mathsf T}D_c G D_c\xi\). Among **every** two-color partition, not merely proper distance-one colorings, the alternating checkerboard partition uniquely minimizes variance, up to exchanging color names.

Define \(r\in(0,1)\) by \(r+r^{-1}=\mu+2\), and
\[
 c=\frac{r}{(1-r^2)(1-r^n)},\qquad m=\frac n2.
\]
The exact minimum variance is
\[
 \boxed{V_{\rm cb}=4nc^2\left[\frac{r^4(1-r^{2n-4})}{1-r^4}+(m-1)r^n\right].}
\]
At the same cost of two quadratic forms, two independent full-vector Hutchinson probes averaged together have variance
\[
 V_{\rm ind2}=n\sum_{d=1}^{n-1}c^2(r^d+r^{n-d})^2.
\]
For every finite even \(n\ge4\) and every positive \(\mu\), \(0<V_{\rm cb}<V_{\rm ind2}\). Moreover, at fixed \(r\in(0,1)\) as even \(n\to\infty\),
\[
 \frac{V_{\rm cb}}{V_{\rm ind2}}\longrightarrow\frac{2r^2}{1+r^2}.
\]
At fixed \(n\), the ratio approaches \((n-2)/(n-1)\) as \(\mu\downarrow0\), and zero as \(\mu\to\infty\). These are comparisons of **statistical variance under exact applications of** \(G\), not of floating-point or iterative linear-solve error.

## Assumptions and scope

The screening \(\mu\) is strictly positive; the directed shift \(P\) is used only to define the undirected cycle \(P+P^{\mathsf T}\). The dimension \(n\) is even and at least four. One sign is sampled independently for each coordinate, with exactly one probing quadratic form for each of two disjoint color classes. Both classes are required nonempty. The two-probe benchmark uses independent full-dimensional Rademacher sign vectors and their arithmetic average; both methods need exactly two products/solves with \(A_\mu\), in exact arithmetic. No optimality is claimed over all possible two-query algorithms or over partitions into three or more colors.

## Proof

**1. Cyclic Green kernel.** The characteristic equation for the homogeneous screened second-difference recurrence is \(r+r^{-1}=\mu+2\). Its positive decaying root satisfies \(0<r<1\). Periodizing the infinite-line Green function yields
\[
 G_{ij}=g_d,\qquad g_d=c(r^d+r^{n-d}),\qquad d=(j-i)\bmod n.
\]
Indeed, the entries satisfy \((\mu+2)g_d-g_{d-1}-g_{d+1}=0\) for \(d\not\equiv0\pmod n\), and that expression equals one at \(d=0\). All entries are strictly positive.

**2. Variance as a binary quadratic energy.** Encode the partition by \(s_i\in\{-1,1\}\). Since the diagonal of every Rademacher quadratic form is deterministic and products \(\xi_i\xi_j\), \(i<j\), are pairwise orthogonal centered random variables, its total variance is exactly
\[
 V(s)=4\sum_{0\le i<j<n\, :\,s_i=s_j}G_{ij}^2
 =2\sum_{i<j}G_{ij}^2(1+s_i s_j).
\]
Let \(K=G\circ G\) be the entrywise square. Up to a term independent of \(s\), \(V(s)\) equals \(s^{\mathsf T}Ks\). Every such binary sign vector has squared Euclidean norm \(n\).

**3. The unique minimum eigenfrequency.** Write \(\theta_j=2\pi j/n\). Because \(K\) is circulant, its discrete Fourier eigenvalues, obtained by summing the two geometric sequences in \(g_d^2=c^2(r^{2d}+r^{2n-2d}+2r^n)\), are
\[
 \lambda_j=c^2\left[\frac{(1-r^{2n})(1-r^4)}{1-2r^2\cos\theta_j+r^4}+2nr^n\mathbf 1_{\{j=0\}}\right].
\]
The denominator is strictly largest when \(\cos\theta_j=-1\). For even \(n\), this occurs only at \(j=n/2\); the extra strictly positive term at \(j=0\) cannot create another minimum. Therefore \(\lambda_{n/2}\) is the unique smallest eigenvalue, and its real eigenvector is \((1,-1,1,-1,\ldots)\). The Rayleigh inequality gives
\[
 s^{\mathsf T}Ks\ge n\lambda_{n/2},
\]
with equality if and only if the sign vector lies on that one-dimensional eigenspace. The only binary vectors on it are the checkerboard signing and its negative. This proves global two-color optimality and uniqueness.

**4. Exact variance.** For the alternating signing, two distinct sites have equal color precisely at even cyclic displacement, so
\[
 V_{\rm cb}=2n\sum_{\substack{2\le d\le n-2\\d\ \mathrm{even}}}g_d^2.
\]
Summing the geometric powers gives \(\sum_{d\ \mathrm{even},\,2\le d\le n-2}g_d^2=2c^2[r^4(1-r^{2n-4})/(1-r^4)+(m-1)r^n]\), which proves the displayed expression. A single full-vector Hutchinson probe has variance \(2n\sum_{d=1}^{n-1}g_d^2\), so averaging two independent probes yields \(V_{\rm ind2}\) as stated.

**5. Strict equal-cost improvement.** The difference of these variances is
\[
 V_{\rm ind2}-V_{\rm cb}
 =n\left(\sum_{d\ \mathrm{odd}}g_d^2-
    \sum_{\substack{d\ \mathrm{even}\\1\le d\le n-1}}g_d^2\right)
 =n(g_0^2-\lambda_{n/2}).
\]
The explicit Green and Fourier formulas give
\[
 g_0^2-\lambda_{n/2}
 =2c^2\left[r^n(1+r^n)+\frac{r^2(1-r^{2n})}{1+r^2}\right]>0.
\]
The minimum variance is positive for \(n\ge4\) because sites distance two apart have strictly positive Green entries. Finally the stated limits follow by finite sums as \(r\uparrow1\) (all \(g_d\) are asymptotically equal), by leading powers as \(r\downarrow0\), and by geometric-series convergence at fixed \(r\in(0,1)\) as \(n\to\infty\). Since \(\mu=(1-r)^2/r\), these are exactly the claimed screening regimes.

## Verification

`checker.py` is a standalone Python standard-library exact-rational checker. It directly verifies the cyclic inverse recurrence, minimum-variance closed form, strict equal-cost comparison, and every binary partition for \(n\in\{4,6,8,10,12\}\) and \(r\in\{1/5,1/2,4/5\}\). Reproducing its run with `python checker.py` produces the saved `checker_output.txt`. It reported 33,861 successful exact-rational assertions. The finite tests are illustrative; all-dimensional claims above follow from the analytic Fourier proof. For example, \(n=8\), \(r=1/2\) (equivalently \(\mu=1/2\)) gives the exact variance ratio \(V_{\rm cb}/V_{\rm ind2}=2568/5909\).

## Relationship to prior work

Frommer, Rinelli and Schweitzer [1], especially Section 3.2 and Theorem 3.3, give the general stochastic-probing variance as a sum of within-color squared off-diagonal matrix-function entries. Their result implies the starting variance identity here, but does not establish which of **all** two-color partitions minimizes it for a screened cycle, the unique Fourier-optimal signing, or the exact strict two-probe comparison. Switzer and collaborators [2] and Stathopoulos, Laeuchli and Orginos [4] describe distance-based and hierarchical lattice probing, including periodic lattices and randomized color vectors; their optimality discussion concerns coloring distance/number or reuse, not the global variance-minimizing partition for the fully dense screened inverse. Frommer, Schimmel and Schweitzer [3] derive decay-based probing error bounds and graph-color constructions, not this exact finite-cycle covariance minimum. The present contribution is **not** the known general Rademacher variance identity or the known checkerboard distance-one coloring; it is the proof that the checkerboard remains uniquely optimal against every competing two-color partition for every positive screen, plus exact residual and equal-cost statistics.

## Limitations

This result assumes homogeneous nearest-neighbor weights, a periodic even cycle, strictly positive screening, independent Rademacher coordinate signs, exact linear solves, and exactly one probe per color. Inhomogeneous edges, odd cycles, correlated probes, more colors, and iterative solve noise are not covered. Existing general spectral and graph-coloring principles may yield alternative proofs; a remote equivalently specialized result outside the inspected sources cannot be ruled out. The theorem is an analytic benchmark and makes no universal efficiency claim for all trace-estimation algorithms.

## References

[1] A. Frommer, M. Rinelli and M. Schweitzer, *Analysis of stochastic probing methods for estimating the trace of functions of sparse symmetric matrices*, arXiv:2308.07722, first public August 15, 2023. https://arxiv.org/abs/2308.07722

[2] H. Switzer, A. Stathopoulos, E. Romero, J. Laeuchli and K. Orginos, *Probing for the Trace Estimation of a Permuted Matrix Inverse Corresponding to a Lattice Displacement*, arXiv:2106.01275, first public June 2, 2021. https://arxiv.org/abs/2106.01275

[3] A. Frommer, C. Schimmel and M. Schweitzer, *Analysis of probing techniques for sparse approximation and trace estimation of decaying matrix functions*, arXiv:2009.01589, first public September 3, 2020. https://arxiv.org/abs/2009.01589

[4] A. Stathopoulos, J. Laeuchli and K. Orginos, *Hierarchical probing for estimating the trace of the matrix inverse on toroidal lattices*, arXiv:1302.4018, first public February 17, 2013. https://arxiv.org/abs/1302.4018
