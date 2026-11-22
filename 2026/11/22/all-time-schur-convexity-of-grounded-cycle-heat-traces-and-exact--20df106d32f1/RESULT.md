# All-time Schur-convexity of grounded cycle heat traces and exact optimal leader spacing

## Finding

Let \(C_n\) be the simple unweighted cycle on \(n\ge 3\) vertices. Choose any \(k\) distinct perfectly grounded leaders, \(1\le k\le n\), and let \(L_{FF}(S)\) be the follower principal submatrix of the original combinatorial Laplacian (no diagonal recomputation after grounding). For every \(t>0\) and every uniform screening \(\mu\ge0\), set
\[
H_{t,\mu}(S)=\operatorname{tr}\bigl(e^{-t(L_{FF}(S)+\mu I)}\bigr).
\]
Write the clockwise leader-to-leader spacings as positive integers \(g_1,\ldots,g_k\) with \(\sum_i g_i=n\). For **every** positive time, the objective is **strictly Schur-convex on integer gap vectors** under majorization: every balancing operation that replaces two gaps \((a,b)\), with \(a\ge b+2\), by \((a-1,b+1)\) strictly decreases the objective. Consequently, the global minimizers, simultaneously for all \(t>0\) and \(\mu\ge0\), are **exactly** the leader sets with gaps differing by at most one. The maximizers are exactly the sets of \(k\) consecutive leaders (with trivial equality when every feasible gap vector is already balanced).

Writing \(n=qk+r\), \(0\le r<k\), the unique optimal *gap multiset* has \(k-r\) gaps of size \(q\) and \(r\) gaps of size \(q+1\). There are exactly
\[
N_{\mathrm{opt}}=\frac nk\binom{k}{r}
\]
labelled optimal leader sets. Let \(h_0(t)=0\) and
\[
h_\ell(t)=\sum_{j=1}^{\ell}\exp\left[-t\left(2-2\cos\frac{\pi j}{\ell+1}\right)\right]\quad(\ell\ge1).
\]
The global minimum and maximum are, respectively,
\[
H^{\min}_{t,\mu}=e^{-\mu t}\big[(k-r)h_{q-1}(t)+r h_q(t)\big],
\qquad H^{\max}_{t,\mu}=e^{-\mu t}h_{n-k}(t).
\]

These same minimizers and maximizers apply to every positive inverse spectral moment \(\operatorname{tr}((L_{FF}+\mu I)^{-s})\), \(s>0\), and to every positive-time integral of the heat trace against a nonzero nonnegative integrable weight. In particular they optimize squared transient consensus error and integrated unit-white-noise covariance at **all** observation horizons without retuning the leaders.

## Assumptions and scope

The edge weights are one; the cycle is simple (\(n\ge3\)); leaders are distinct fixed vertices, and their removal does not alter remaining diagonal degrees. No leader-input gains or noisy leaders are included. Exactly \(k\) vertices are leaders. The empty follower matrix at \(k=n\) has trace zero. The order relation concerns the multiset of *cyclic gaps*, not a graph-spectrum eigenvalue majorization claim. Inverse powers require \(s>0\) and \(L_{FF}+\mu I\) positive definite, which holds for \(k\ge1\) and \(\mu\ge0\). At \(t=0\), all placements tie, so strictness is asserted only at positive time.

## Proof

**Block reduction.** The follower vertices in each gap form an induced path of \(g_i-1\) vertices. Because the principal Laplacian retains degree two on every follower, its block is \(D_\ell=2I_\ell-A_\ell\), where \(A_\ell\) is the adjacency matrix of a path on \(\ell\) vertices. Thus
\[
H_{t,\mu}(S)=e^{-\mu t}\sum_{i=1}^k h_{g_i-1}(t),\quad
h_\ell(t)=e^{-2t}\operatorname{tr}(e^{tA_\ell}).
\]
The eigenvalues of \(D_\ell\) are \(2-2\cos(\pi j/(\ell+1))\), \(1\le j\le\ell\), giving the claimed exact formula.

**Strict discrete convexity.** Expand the matrix exponential as a power series with nonnegative coefficients:
\[
h_\ell(t)=e^{-2t}\sum_{m\ge0}\frac{t^m}{m!}\operatorname{tr}(A_\ell^m).
\]
A rooted closed nearest-neighbour walk of length \(m\) on the integer line has a finite span \(w\), the number of sites from its least to its greatest visited vertex. Translate each such walk uniquely so that its least visited vertex is zero, and write \(c_{m,w}\) for the resulting nonnegative integer count. The number of translations placing the walk inside an \(\ell\)-vertex path is \((\ell-w+1)_+\). Hence
\[
\operatorname{tr}(A_\ell^m)=\sum_{w\ge1}c_{m,w}(\ell-w+1)_+.
\]
With \(h_0=0\), the central second difference \(\Delta^2 h_\ell=h_{\ell+1}-2h_\ell+h_{\ell-1}\), for every integer \(\ell\ge1\), therefore equals
\[
\Delta^2h_\ell(t)=e^{-2t}\sum_{m\ge0}\frac{t^m}{m!}c_{m,\ell+1}.
\]
There are at least two rooted length-\(2\ell\) walks of span \(\ell+1\): traverse \(\ell\) steps in one direction and retrace, or traverse in the opposite direction and retrace. Consequently, for every \(\ell\ge1\) and \(t>0\),
\[
\Delta^2h_\ell(t)\ge\frac{2e^{-2t}t^{2\ell}}{(2\ell)!}>0.
\]
This is a pointwise, infinite-family proof; a numerical sample is neither used nor sufficient.

**Balancing and the exact optimizer set.** If gaps \(a\ge b+2\), the corresponding follower lengths are \(A=a-1\ge B+2=b+1\). The objective reduction on balancing the gaps is
\[
h_A+h_B-h_{A-1}-h_{B+1}
=\sum_{\ell=B+1}^{A-1}\Delta^2h_\ell>0.
\]
More quantitatively, it is at least
\[
\frac{2e^{-2t}t^{2(B+1)}}{(2B+2)!},
\]
which is strictly positive. Repeated transfers terminate exactly at balanced positive gap vectors; every other gap vector admits a strictly improving transfer. Conversely, the extreme vector \((n-k+1,1,\ldots,1)\) majorizes all positive integer gap vectors of total \(n\), so the same strict convexity establishes the maximum and its equality cases. These gap vectors are realized by actual cyclic leader placements; no relaxation is involved. The factor \(e^{-\mu t}>0\) does not change any ranking.

For the count, choose a starting vertex in \(n\) ways and an ordered length-\(k\) gap word containing \(r\) large gaps in \(\binom{k}{r}\) ways. Every resulting labelled leader set has exactly \(k\) representations, one for each choice of its starting leader. Division by \(k\) gives the stated integer count.

**Transfer to inverse spectral moments and observation horizons.** The grounded matrix is positive definite. For every \(s>0\), spectral calculus gives
\[
\operatorname{tr}((L_{FF}+\mu I)^{-s})
=\frac1{\Gamma(s)}\int_0^\infty t^{s-1}H_{t,\mu}(S)\,dt.
\]
The integral converges and preserves all strict inequalities. Any nonzero nonnegative integrable time weight likewise preserves the simultaneous order. For example, the integrated covariance objective of the linear stochastic system with unit white-noise forcing is \(\int_0^T H_{2t,0}(S)\,dt\), with \(T>0\), hence has precisely the same optimizers.

## Verification

The self-contained `verify.py` reproduces: (a) exhaustive labelled-leader-set comparisons on cycles of sizes three through ten, at three positive times; (b) exact optimal-set multiplicities; (c) independent full-matrix eigenvalue traces versus the gap formula; (d) positive walk-count second differences using exact integer adjacency powers; and (e) the quantitative analytic convexity lower bound on a stable finite parameter grid. Run `python verify.py` with Python 3 and NumPy. This finite checking corroborates but does not replace the infinite proof above.

## Relationship to prior work

Clark, Alomair, Bushnell and Poovendran (2013) analyze transient leader selection and supermodular convergence-error bounds; their convergence-error metric is not the isotropic squared-propagator trace, and their full paper does not give the cycle-gap heat-trace theorem. Patterson, McGlohon and Dyagilev (2014) give polynomial-time algorithms for steady-state inverse-trace leader selection on weighted paths and rings. Their ring decomposition supplies closely related block structure, but their objective and theorem do not establish strict all-time ordering or all positive inverse orders. A previously established screened-cycle Nyström landmark theorem gives **exactly the same balanced sets and their multiplicity for the first inverse spectral moment**. Indeed, for \(Q=\mu I+L\) and \(K=Q^{-1}\), the Schur complement identity \(K-K_{:,S}K_{SS}^{-1}K_{S,:}=\operatorname{diag}(0_S,Q_{FF}^{-1})\) (after ordering leaders first) makes its trace-residual objective equal to \(\operatorname{tr}(Q_{FF}^{-1})\). Neither its optimizer count nor this first-inverse optimality is claimed as new; the added theorem is the **strict pointwise heat-trace majorization at every positive time**, its explicit path-walk convexity certificate, worst-case placement, and all other positive-order/horizon consequences. Continuous-domain Dirichlet heat-trace obstacle optimization addresses a different domain and geometric operation. Related results for directed attenuated rings, and heat traces on other graph families, neither assert nor imply the symmetric unit-cycle gap-order theorem. This literature comparison is not a proof of publication priority.

## Limitations

The conclusion is not asserted for weighted or directed cycles, nonuniform screening, finite-gain leaders, state-dependent noise, or arbitrary initial condition vectors. The strict heat-trace ordering is an isotropic/Frobenius-error result, not an entrywise or worst-case operator-norm ordering. The infinite theorem is proved exactly; independent expert audit and a comprehensive survey of every inaccessible or unindexed publication have not been performed. The stationary first-inverse balanced-spacing rule and its optimum multiplicity are already available through a screened-cycle Nyström trace-residual equivalence, and are not presented as novel standalone claims.

## References

1. A. Clark, B. Alomair, L. Bushnell and R. Poovendran, *Minimizing Convergence Error in Multi-Agent Systems via Leader Selection: A Supermodular Optimization Approach*, first arXiv version 2013-06-20. https://arxiv.org/abs/1306.4949
2. S. Patterson, N. McGlohon and K. Dyagilev, *Efficient, Optimal k-Leader Selection for Coherent, One-Dimensional Formations*, first arXiv version 2014-12-20. https://arxiv.org/abs/1412.6595
3. A. El Soufi and E. M. Harrell II, *On the Placement of an Obstacle so as to Optimize the Dirichlet Heat Trace*, first arXiv version 2014-02-17. https://arxiv.org/abs/1402.3900
