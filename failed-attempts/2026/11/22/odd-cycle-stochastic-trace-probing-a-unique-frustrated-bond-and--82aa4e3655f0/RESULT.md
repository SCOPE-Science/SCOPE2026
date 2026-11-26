# Odd-cycle stochastic trace probing: a unique frustrated bond and an exact variance penalty

## Finding

Let \(n=2m+1\ge5\) be odd and \(\mu>0\). For the unweighted cycle \(C_n\), define \(G_\mu=(\mu I+L(C_n))^{-1}\). Partition the vertices into exactly two nonempty classes, and estimate \(\operatorname{tr}G_\mu\) using one independent class-supported Rademacher quadratic probe in each class. **Among all such partitions, the variance minimizers are exactly the \(n\) unlabeled near-alternating partitions having a single monochromatic cycle edge.** This classification holds for every positive screening parameter, including arbitrarily weak screening, and gives all ties.

Write \(r\in(0,1)\) for the unique number satisfying \(r+r^{-1}=\mu+2\), set
\[
 c=\frac{r}{(1-r^2)(1-r^n)},\qquad g_d=c(r^d+r^{n-d}),\qquad 0\le d<n,
\]
and define \(N_d=d\) for odd \(d\), and \(N_d=n-d\) for even \(d\). Then the exact minimum variance over all two-class partitions is
\[
 \boxed{V_{\min}(n,\mu)=4c^2\sum_{d=1}^{m}N_d(r^d+r^{n-d})^2.}
\]
The \(n\) optimizers are precisely the rotations of the sign assignment \(s_i=(-1)^i\) for \(0\le i<n\), identifying a signing and its negative. All optimal class sizes are \(m\) and \(m+1\).

For fixed \(\mu>0\), put \(c_\infty=r/(1-r^2)\). Along odd orders \(n\to\infty\),
\[
 \boxed{V_{\min}(n,\mu)=\frac{4nc_\infty^2r^4}{1-r^4}+\frac{4c_\infty^2r^2}{(1+r^2)^2}+O_\mu(n^2r^n).}
\]
The second, strictly positive, order-one term is the parity-frustration correction relative to the leading infinite-volume checkerboard variance density; the leading density itself is not feasible on an odd cycle. Relative to the variance \(V_{\mathrm{ind2}}\) of the **average** of two independent full-support Rademacher probes using the same two linear solves,
\[
 \frac{V_{\min}}{V_{\mathrm{ind2}}}\longrightarrow\frac{2r^2}{1+r^2}\quad\text{as odd }n\to\infty,
\]
while at fixed odd \(n\), this ratio tends to \((n-1)/n\) as \(\mu\downarrow0\), and \(2/n\) as \(\mu\to\infty\).

## Assumptions and scope

The graph is the ordinary undirected unweighted cycle with odd order \(n\ge5\); the matrix \(\mu I+L\) uses the unnormalized combinatorial graph Laplacian and strictly positive shift \(\mu\). Two classes must be disjoint, nonempty and exhaustive. Independent fair coordinate signs are sampled within each class and the two resulting quadratic forms are **summed**, not averaged; this sum is the unbiased trace estimate. Class probes are independent of one another. No claim is made about three or more probes, non-Rademacher coupling, noise in approximate linear solves, or arbitrary two-query trace algorithms. All statements refer to exact arithmetic.

## Proof

**1. Exact cyclic resolvent and variance reduction.** The infinite-line screened recurrence has decaying root \(r\in(0,1)\) specified above. Periodization proves
\[
 (G_\mu)_{ij}=g_{(j-i)\bmod n},\qquad
 (\mu+2)g_d-g_{d-1}-g_{d+1}=\mathbf1_{\{d=0\}},
\]
where indices are cyclic. Thus all entries are positive, and the inverse relation holds exactly. Encode a partition by signs \(s_i\in\{-1,1\}\). Independence and orthogonality of distinct products of fair Rademacher variables imply
\[
 V(s)=4\sum_{0\le i<j<n\,:\,s_i=s_j}g_{(j-i)\bmod n}^{\,2}.
\]
Set \(w_d=g_d^2\), for undirected distances \(1\le d\le m\), and \(S=\sum_i s_i\). Minimizing variance is equivalent to minimizing the Ising energy
\[
 E(s)=\sum_{1\le i<j\le n}w_{d(i,j)}s_i s_j,
\]
since \(V(s)=2\sum_{i<j}w_{d(i,j)}+2E(s)\). All \(n\) cyclic nearest-neighbor pairs have distance one.

**2. Strict circular convexity.** Write \(q=r^2\). For \(1\le d\le m\),
\[
 w_d=c^2(q^d+q^{n-d}+2r^n).
\]
The difference \(w_d-w_{d+1}\) is positive for \(d<m\), because \(q^d-q^{d+1}>q^{n-d-1}-q^{n-d}\) there. Its second difference at interior distances is
\[
 w_{d-1}-2w_d+w_{d+1}
 =c^2(1-q)^2(q^{d-1}+q^{n-d-1})>0.
\]
Extend symmetrically by \(w_{m+1}=w_m\). The final discrete second difference is \(a_m=w_{m-1}-w_m>0\), and the earlier ones \(a_k=w_{k-1}-2w_k+w_{k+1}>0\) for \(2\le k<m\). With \(a_k>0\), backward telescoping yields
\[
 w_d=w_m+\sum_{k=d+1}^{m}(k-d)a_k,\qquad 1\le d\le m.
\]
For \(m=2\), only the final difference is present; all formulas remain valid.

**3. Sliding-window lower bounds.** Define the integer window energy
\[
 W_k(s)=\sum_{i=0}^{n-1}\left(\sum_{a=0}^{k-1}s_{i+a\bmod n}\right)^2,\qquad 2\le k\le m.
\]
If \(k\) is odd, all window sums are odd integers, hence \(W_k\ge n\). If \(k\) is even, the window sums are even integers \(y_i\) satisfying \(y_i^2\ge2|y_i|\); because \(\sum_i y_i=kS\) and \(S\) is odd, \(W_k\ge2k|S|\ge2k\).

Expanding the square and counting ordered pairs in each window gives the exact identity
\[
 W_k=kn+2\sum_{d=1}^{k-1}(k-d)\sum_{i=0}^{n-1}s_i s_{i+d}.
\]
Since \(k\le m\), these cyclic offsets represent distinct undirected distance classes. The weight decomposition therefore yields
\[
 \boxed{E(s)=\frac{w_m}{2}(S^2-n)
 +\frac12\sum_{k=2}^{m}a_k[W_k(s)-kn].}
\]
This equality is exact for every binary signing. Since \(w_m>0\), \(a_k>0\), and the window lower bounds hold simultaneously, the right side is bounded below by taking \(S^2=1\), \(W_k=n\) for odd \(k\) and \(W_k=2k\) for even \(k\).

**4. Simultaneous attainment and strict uniqueness.** On an odd cycle, \(s_i=(-1)^i\), \(0\le i<n\), has exactly one equal-sign nearest-neighbor pair, across the closing edge. For this signing \(S=1\). Every odd-length window has sum \(\pm1\); every even-length window has sum zero or \(\pm2\), and the nonzero window sums all have the sign of \(S\). Hence it attains every lower bound in Step 3. Every energy minimizer must also attain the \(W_2\) bound because \(a_2>0\). But \(W_2=4\) times the number of monochromatic nearest-neighbor edges. Thus exactly one edge is monochromatic. The remaining cycle edges force alternation and uniquely determine the signs, up to the choice of that edge and a global sign flip. There are therefore exactly \(n\) distinct unlabeled optimum partitions, all nonempty and of sizes \((m,m+1)\).

**5. Exact variance and asymptotics.** Fix the near-alternating signing. At cyclic distance \(d\in\{1,\ldots,m\}\), exactly \(d\) of the \(n\) unordered pairs have equal color if \(d\) is odd, and exactly \(n-d\) if \(d\) is even. Substitution into the Rademacher variance formula gives the displayed finite sum. Equivalently, \(N_d=n\mathbf1_{\{d\text{ even}\}}+(-1)^{d+1}d\). For fixed \(r<1\), replace the finite Green kernel by \(c_\infty r^d\), with total finite-size discrepancy \(O_r(n^2r^n)\), and extend the convergent sums:
\[
 \sum_{\substack{d\ge2\\d\text{ even}}}r^{2d}=\frac{r^4}{1-r^4},\qquad
 \sum_{d\ge1}(-1)^{d+1}d r^{2d}=\frac{r^2}{(1+r^2)^2}.
\]
This proves the order-one positive parity correction. A full-support Rademacher quadratic probe has variance \(4\sum_{i<j}g_{ij}^2\), so the average of two independent probes has
\[
 V_{\mathrm{ind2}}=2n\sum_{d=1}^m g_d^2.
\]
The infinite-volume ratio follows from the even-distance geometric sum and the full geometric sum. When \(r\uparrow1\), all off-diagonal Green entries become asymptotically equal, the optimum has \(m^2\) same-color pairs, and \(V_{\min}/V_{\mathrm{ind2}}\to(n-1)/n\). When \(r\downarrow0\), the single same-color nearest-neighbor pair dominates \(V_{\min}\), while all \(n\) nearest-neighbor pairs dominate \(V_{\mathrm{ind2}}\), giving ratio \(2/n\). Finally \(\mu=(1-r)^2/r\), matching the stated screening limits.

## Verification

Run `python checker.py` using Python 3's standard library. Its exact-arithmetic exhaustive checks cover all unlabeled nontrivial partitions of odd cycles of sizes \(5,7,9,11,13,15\), at \(r\in\{1/5,1/2,4/5\}\), comparing their variances with the closed formula and counting exact optimizers. It separately checks the inverse recurrence, window lower bounds, optimal window equalities, strict convex coefficients, and telescoping decomposition. The supplied `checker_output.txt` records **502,920 exact-rational assertions passed**. Those finite computations independently corroborate the proof; they do not establish the universal quantifiers in place of Steps 1–5.

## Relationship to prior work

Stathopoulos, Laeuchli and Orginos [1] introduced hierarchical probing based on graph-distance coloring for inverse-trace estimation on toroidal lattices. Their inspected lattice-coloring construction motivates the precise two-solve question, but its results do not give a global variance-optimal two-partition of odd screened cycles, optimizer counts or the parity correction. Frommer, Rinelli and Schweitzer [2] derive the general variance decomposition for stochastic graph-coloring probes; this supplies the objective identity, not the new minimizer comparison.

The exact published even-cycle checkerboard classification [3] is the closest directly comparable finite-cycle result. It assumes even graph order, where a proper alternating two-coloring exists and a Fourier eigenvector proves optimality. On odd graph order there is no alternating Fourier eigenvector with binary coordinates or proper two-coloring; the strict window-energy argument above fills a genuinely different discrete optimization case. A historical paper on maximum cuts of circulant graphs [4] may contain related stronger methods or special cases; its complete text was not accessible, so an implication comparison with every theorem there remains unresolved. The present report does not assert that a search proves historical uniqueness.

## Limitations

The optimization is for exactly two **independent class-supported** Rademacher probes, not an arbitrary estimator design. The rings are homogeneous, odd and at least five vertices. The additive order-one term is a precise asymptotic correction to the leading variance density, not a universal comparison against a physically realizable odd-order checkerboard partition. A directly equivalent general result in inaccessible circulant max-cut literature, or in unindexed long-range antiferromagnetic Ising theory, could precede the result.

## References

[1] A. Stathopoulos, J. Laeuchli and K. Orginos, *Hierarchical probing for estimating the trace of the matrix inverse on toroidal lattices*, arXiv:1302.4018, first public February 17, 2013. https://arxiv.org/abs/1302.4018

[2] A. Frommer, M. Rinelli and M. Schweitzer, *Analysis of stochastic probing methods for estimating the trace of functions of sparse symmetric matrices*, arXiv:2308.07722, first public August 15, 2023. https://arxiv.org/abs/2308.07722

[3] *Checkerboard probing uniquely minimizes two-color trace variance on screened cycles*, mathematical result published November 8, 2026. https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-checkerboard-probing-uniquely-minimizes-two-color-trace-variance--ad9f3c6dc76a

[4] S. Poljak and D. Turzík, *Max-cut in circulant graphs*, Discrete Mathematics **108** (1992), 379–392, https://doi.org/10.1016/0012-365X(92)90690-H (complete text unavailable for comparison).
