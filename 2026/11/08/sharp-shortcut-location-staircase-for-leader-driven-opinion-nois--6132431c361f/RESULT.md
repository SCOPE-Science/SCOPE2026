# Sharp shortcut-location staircase for leader-driven opinion noise on a path

## Finding

Consider a chain with a fixed leader at vertex \(0\) and \(n\ge3\) noisy followers at vertices \(1,\ldots,n\), with unit-weight edges between successive vertices. Add exactly one previously absent leader-to-follower edge \((0,j)\), where \(2\le j\le n\), of conductance \(\omega>0\). Define \(\mathcal R_n(j,\omega)=\operatorname{tr}(L_{n,j,\omega}^{-1})\), where \(L_{n,j,\omega}\) is the follower-grounded weighted graph Laplacian. The total stationary opinion variance about the leader under independent unit white noise is \(\mathcal P_n(j,\omega)=\mathcal R_n(j,\omega)/2\).

The exact reduction in resistance sum is
\[
\Delta_n(j,\omega)=\frac{\omega}{1+\omega j}\left[nj^2-\frac23j^3+\frac12j^2+\frac16j\right].
\]
Put \(j_0=\lceil(6n-1)/8\rceil\). For every integer \(j_0\le j<n\), put
\[
\omega_{n,j}=\frac{6(n-j)(2j+1)}{j(j+1)(8j+1-6n)}.
\]
These strictly positive thresholds decrease strictly as \(j\) increases. For \(\omega>0\), the optimal added edge is determined by the signs of \(\omega-\omega_{n,j}\): the maximizer of \(\Delta_n(j,\omega)\) is unique except when \(\omega=\omega_{n,j}\), in which case exactly the adjacent locations \(j\) and \(j+1\) are optimal. The optimizer moves monotonically from \(n\), at sufficiently weak extra conductance, to \(j_0\), at sufficiently strong conductance. When \(n=3\), \(j_0=n\) and \(j=n\) is always the unique optimizer.

For any fixed \(\omega>0\), every optimal \(j_n\) satisfies
\[
\frac{j_n}{n}\longrightarrow\frac34,\qquad
\frac{\min_j\mathcal R_n(j,\omega)}{n(n+1)/2}\longrightarrow\frac14.
\]
Thus one well-placed added leader edge removes asymptotically \(75\%\) of the aggregate noise variance of the original leader-rooted path. If instead \(n\omega_n\to c\in(0,\infty)\), the normalized optimal location converges to the unique \(u_c\in(3/4,1)\) satisfying
\[
2(1-u_c)+cu_c\left(1-\frac43u_c\right)=0.
\]
This interpolates continuously between far-end placement as \(c\downarrow0\) and three-quarter placement as \(c\to\infty\).

## Assumptions and scope

The chain has vertex set \(\{0,1,\ldots,n\}\), with vertex \(0\) a fixed leader of opinion zero; all followers experience independent unit-intensity additive white noise and unit-weight symmetric nearest-neighbor DeGroot coupling. The new edge has positive conductance \(\omega\) and must connect the same leader to a follower not already directly adjacent, so \(j\in\{2,\ldots,n\}\). No other vertices, edges, weights, controls or noise intensities vary. All claims concern finite \(n\ge3\), arbitrary real \(\omega>0\), and the specified large-network limits; they do not address multiple added edges or other topologies.

The stochastic differential equation for follower opinion vector is \(dX=-L_{n,j,\omega}X\,dt+dB_t\) with standard independent Brownian entries. Positive definiteness of the grounded Laplacian yields the unique stationary covariance \(L_{n,j,\omega}^{-1}/2\). Consequently minimizing \(\mathcal R\) is equivalent to minimizing steady-state aggregate variance.

## Proof

**Exact Green matrix.** Let \(L_0\) be the follower-grounded Laplacian before adding the edge. It is tridiagonal, with diagonal \((2,\ldots,2,1)\) and \(-1\) on adjacent off-diagonals. Direct multiplication verifies that its inverse has entries \((L_0^{-1})_{ik}=\min(i,k)\), for \(1\le i,k\le n\). Therefore \(\operatorname{tr}(L_0^{-1})=\sum_{i=1}^n i=n(n+1)/2\).

**Edge gain.** If \(e_j\) denotes the \(j\)-th coordinate vector, then \(L_{n,j,\omega}=L_0+\omega e_je_j^{\mathsf T}\). Sherman–Morrison gives
\[
L_{n,j,\omega}^{-1}=L_0^{-1}-\frac{\omega(L_0^{-1}e_j)(L_0^{-1}e_j)^{\mathsf T}}{1+\omega (L_0^{-1})_{jj}}.
\]
Taking traces and using \((L_0^{-1})_{jj}=j\), the reduction is \(\omega S_n(j)/(1+\omega j)\), where
\[
S_n(j)=\sum_{i=1}^n\min(i,j)^2
=\frac{j(j+1)(2j+1)}6+(n-j)j^2.
\]
The asserted cubic follows by expansion.

**Unique optimum and all switches.** The discrete difference of these sums is
\[
S_n(j+1)-S_n(j)=(n-j)(2j+1).
\]
Putting the two gains over their positive common denominator \((1+\omega j)(1+\omega(j+1))\) shows that their difference has exactly the sign of
\[
A_{n,j}(\omega)=(n-j)(2j+1)+\frac{\omega j(j+1)}6(6n-8j-1).
\]
For every \(j<j_0\), both terms in \(A_{n,j}(\omega)\) are positive. For \(j\ge j_0\), the second coefficient is strictly negative (\(6n-1\) is odd and cannot be divisible by \(8\)), and \(A_{n,j}(\omega)=0\) exactly when \(\omega=\omega_{n,j}\). In this range, \((n-j)(2j+1)\) strictly decreases with \(j\), whereas \(j(j+1)(8j+1-6n)\) strictly increases. Thus the thresholds strictly decrease in \(j\). For any fixed \(\omega>0\), adjacent gain differences are initially positive, then negative, with at most one zero at their transition. This proves unique optimization except for the specified adjacent tie. The limiting choices as \(\omega\downarrow0\) or \(\omega\to\infty\) follow from the smallest and largest thresholds; when the threshold index set is empty, \(j_0=n\).

**Macroscopic optimization.** Write \(u=j/n\). Uniformly on the full feasible grid, if \(n\omega_n\to c\in(0,\infty)\), then
\[
\frac{\Delta_n(j,\omega_n)}{n^2}
\longrightarrow F_c(u)=\frac{c(u^2-2u^3/3)}{1+cu}
\]
in the sense that the supremum absolute error on the grid tends to zero. Its derivative has the sign of \(u[2(1-u)+cu(1-4u/3)]\). It is positive below \(3/4\); in \([3/4,1]\) the bracket is strictly decreasing, positive at \(3/4\), and negative at \(1\). Consequently \(F_c\) has exactly one maximizing point \(u_c\in(3/4,1)\), giving the asserted root equation. The identity \(c=2(1-u)/(u(4u/3-1))\) makes its continuous, strictly decreasing dependence on \(c\) and endpoint limits explicit.

For fixed \(\omega>0\), the thresholds \(\omega_{n,j}\) are \(O(1/n)\) uniformly whenever \(j/n\ge3/4+\varepsilon\), for any fixed \(\varepsilon>0\); hence the optimal \(j_n/n\) lies between \(j_0/n\to3/4\) and \(3/4+\varepsilon\) eventually. With \(j_n/n\to3/4\), dividing the exact reduction by \(n^2\) gives
\[
\frac{\Delta_n(j_n,\omega)}{n^2}\longrightarrow
\left(u-\frac23u^2\right)_{u=3/4}=\frac38.
\]
Since \(\operatorname{tr}(L_0^{-1})/n^2\to1/2\), the optimal residual-to-original ratio tends to \((1/2-3/8)/(1/2)=1/4\), completing the proof.

## Verification

The standalone `verify.py` uses exact rational arithmetic, independently inverts the tridiagonal and edge-augmented grounded Laplacians and checks the inverse entries and gain formula for path sizes \(3\) through \(17\). It checks the exact adjacent-difference identity and complete maximizing-position staircase for every path size \(3\) through \(150\), multiple rational edge weights and every rational threshold; all tests passed (60,096 checks). Large finite-size limit checks are illustrative, not the proof of any asymptotic statement. Run `python3 verify.py` from a directory containing the supplied script; no external libraries are required.

## Relationship to prior work

Xu and Zhang (arXiv:2308.07008v1, August 14, 2023) formulate noisy leader-follower polarization minimization as a grounded-Laplacian inverse-trace objective and give a general rank-one edge-gain expression and algorithms for multiple candidate edges. Their rank-one identity supplies the general framework here. The new contribution is the all-length *specific path* location classification, strict ordering and exact values of all weight-dependent switching thresholds, and the three-quarter position / one-quarter residual scaling. Those conclusions are not stated by the inspected source. Patterson, McGlohon and Dyagilev (arXiv:1412.6595) optimize *which vertices are designated as leaders* in path and cycle networks, rather than placing one finite-conductance edge to a pre-existing leader. Zhou, Sun, Li and Zhang (arXiv:2309.17019) maximize the *smallest grounded-Laplacian eigenvalue*, not the inverse trace. Pandey's 2026 grounded-path resistance preprint addresses a different degree-weighted aggregate, landmark selection and edge removal; only its public abstract and description were inspected, so equivalence risk is retained.

## Limitations

The statement is an exact theorem for a deliberately homogeneous rooted path and one positive-weight added leader edge. It need not extend to multiple leaders, multi-edge budgets, heterogeneously weighted paths or different objective functions. The finite example \(n=3\) has no weight-dependent switch. The asymptotic \(75\%\) reduction is relative to the original path's total stationary variance, not a guarantee about an arbitrary network. No exhaustive search of all historical and unindexed literature is possible; an unrecognized equivalent path result remains a priority risk.

## References

1. W. Xu and Z. Zhang, *Minimizing Polarization in Noisy Leader-Follower Opinion Dynamics*, arXiv:2308.07008v1, first public August 14, 2023. https://arxiv.org/html/2308.07008v1
2. S. Patterson, N. McGlohon and K. Dyagilev, *Efficient, Optimal \(k\)-Leader Selection for Coherent, One-Dimensional Formations*, arXiv:1412.6595, December 20, 2014. https://arxiv.org/abs/1412.6595
3. X. Zhou, H. Sun, W. Li and Z. Zhang, *Optimization on the smallest eigenvalue of grounded Laplacian matrix via edge addition*, arXiv:2309.17019, September 29, 2023. https://arxiv.org/abs/2309.17019
4. J. P. Pandey, *Exact Grounded Resistance Sums on Path Graphs: Closed Forms, Optimal Landmarks, Cycles, and Edge Sensitivity*, Zenodo:20328332, 2026. https://zenodo.org/records/20328332
