# Universal rare-delivery staircase for quadrature of square-integrable Lévy paths

## Finding
Let \(n\ge1\) be fixed. Consider \(n\) predetermined exact point observations of a square-integrable Lévy path on \([0,1]\), each independently delivered with probability \(p\in(0,1]\). The target is its time integral, estimated by its conditional expectation using the successfully delivered observations. For every such process having positive variance rate \(v\), the normalized mean-square risk and all optimal sampling times are **independent of the process's jump distribution and drift**.

There is one unique globally optimal ordered design for each \(p>0\). At perfect delivery its nodes are \(t_i=2i/(2n+1)\). As delivery becomes rare, the optimal nodes obey the *universal staircase*
\[
 t_i^*(p)=\frac23+\frac{2i-n-1}{9}p+o_n(p),\qquad i=1,\ldots,n.
\]
Its exact sharp third-order advantage over putting all observations at \(2/3\) is
\[
 \frac{R_p(2/3,\ldots,2/3)-\min R_p}{v}
 =\frac{n(n^2-1)}{486}p^3+o_n(p^3).
\]
Equivalently,
\[
 \frac{\min R_p}{v}=\frac13-\frac8{27}\bigl[1-(1-p)^n\bigr]
 -\frac{n(n^2-1)}{486}p^3+o_n(p^3).
\]
For \(n=1\), the unique optimal time is \(2/3\) for all \(p>0\). For \(n\ge2\), all optimal nodes are distinct for sufficiently small positive \(p\), with adjacent spacings \(2p/9+o_n(p)\).

## Assumptions and scope
The process \(X=(X_t)_{0\le t\le1}\) is a real-valued Lévy process with \(X_0=0\), finite second moment, known drift \(b=\mathbb E X_1\), and positive variance rate \(v=\operatorname{Var}(X_1)>0\). Its paths are integrable over the interval almost surely and in mean square. The target is \(J=\int_0^1X_s\,ds\). A nonadaptive design chooses ordered times \(0\le t_1\le\cdots\le t_n\le1\), including potentially repeated times and endpoints. Delivery indicators are independent Bernoulli variables with common success probability \(p\), independent of the entire process, and their outcomes are revealed. Each delivered value \(X_{t_i}\) is exact; the estimator may be any square-integrable function of delivered values and indicators, so the posterior conditional expectation is optimal under squared loss.

For a subset \(S=\{i_1<\cdots<i_k\}\) of delivered indices, put \(u_0=0\) and \(u_j=t_{i_j}\) for \(1\le j\le k\). Define
\[
 F_S(t)=\frac1{12}\sum_{j=1}^k(u_j-u_{j-1})^3+\frac13(1-u_k)^3,
 \qquad F_{\varnothing}=\frac13.
\]
The finite-dimensional risk for every \(p\in(0,1]\) is exactly
\[
 \frac{R_p(t)}v=\sum_{S\subseteq\{1,\ldots,n\}}p^{|S|}(1-p)^{n-|S|}F_S(t).
\]
The formula is a complete explicit finite polynomial optimization objective, valid for any number of proposed observation times and all permitted coincidence patterns.

## Proof
**Conditional linear bridges and distribution universality.** For independent stationary integrable increments, dividing a time interval into \(m\) equal pieces makes those increments exchangeable. Conditional on their total, each piece therefore has conditional expectation one \(m\)-th of that total. Summing pieces, passing from rational partitions by \(L^2\) continuity, and restoring the known drift proves that between two observed endpoints \(a<b\),
\[
 \mathbb E[X_s\mid X_a,X_b]
 =X_a+\frac{s-a}{b-a}(X_b-X_a),\qquad a\le s\le b.
\]
Disjoint Lévy increments ensure conditioning on additional measurements outside the segment does not alter this bridge mean. After the last observation at \(u\), the conditional mean is \(X_u+b(s-u)\). The conditional mean of \(J\) is thus the integral of these piecewise-linear and terminal drift extrapolants.

For a segment of length \(d\), the variance of the centered increment integral is \(vd^3/3\), its covariance with the observed total increment is \(vd^2/2\), and the latter has variance \(vd\). Since the conditional expectation is precisely linear in that observed increment, the **expected** bridge residual variance is
\[
 v\left(\frac{d^3}{3}-\frac{(d^2/2)^2}{d}\right)=\frac{vd^3}{12}.
\]
The unsampled terminal tail has residual variance \(vd^3/3\). Conditional residuals on disjoint segments have zero cross covariance after averaging. Summing these terms and then averaging over the independent delivery indicators gives exactly the asserted \(F_S\) risk, for Brownian motion, Poisson counting paths, compound-Poisson processes, and every other process satisfying the assumptions.

**Existence and uniqueness.** Each \(F_S\) is convex over the ordered compact simplex: it is a positive sum of cubes of nonnegative affine gaps. For \(p>0\), the all-delivered event has positive weight \(p^n\). Its gap vector \((t_1,t_2-t_1,\ldots,t_n-t_{n-1},1-t_n)\) determines \(t\) injectively, and the cubic is strictly convex on the nonnegative half-line. Hence \(F_{\{1,\ldots,n\}}\), and consequently \(R_p\), are strictly convex. Compactness gives existence; strict convexity gives uniqueness among ordered designs, even allowing duplicate nodes.

**Perfect-delivery endpoint.** At \(p=1\), let the first \(n\) consecutive gaps be \(d_1,\ldots,d_n\) and the final unsampled tail be \(d_{n+1}\). We minimize \(\sum_{j=1}^nd_j^3/12+d_{n+1}^3/3\), subject to nonnegative gaps summing to one. The strictly convex stationary equations give \(d_1=\cdots=d_n=2d_{n+1}=2/(2n+1)\). Therefore \(t_i=2i/(2n+1)\), with normalized minimum \(1/[3(2n+1)^2]\).

**Rare-delivery localization.** Write \(t_0=2/3\) and \(f(t)=F_{\{i\}}(t)=t^3/12+(1-t)^3/3\). We have \(f'(t_0)=0\), \(f''(t_0)=1\), and \(f''(t)\ge1/2\) on \([0,1]\). The singleton-delivery component \(p(1-p)^{n-1}\sum_i f(t_i)\) therefore makes \(R_p/v\) strongly convex with modulus at least \(p(1-p)^{n-1}/2\). At the coincident design \(t_i=t_0\), its gradient comes only from events with two or more deliveries, so its norm is \(O_n(p^2)\). Strong convexity and comparison to the coincident design imply every optimal node satisfies \(t_i^*(p)=t_0+O_n(p)\).

Set \(t_i=t_0+p y_i\) with bounded ordered offsets \(y_1\le\cdots\le y_n\). The singleton events contribute \(p^3\sum_i y_i^2/2+O_n(p^4)\) to the risk difference from the coincident design. For two successful readings \(s\le t\) near \(t_0\),
\[
 F_{\{s,t\}}=\frac{s^3}{12}+\frac{(t-s)^3}{12}+\frac{(1-t)^3}{3},
 \qquad F_{\{s,t\}}-f(t_0)=-\frac{t-s}{9}+O((|s-t_0|+|t-t_0|)^2).
\]
Pair-delivery events therefore contribute \(-p^3\sum_{i<j}(y_j-y_i)/9+O_n(p^4)\); events with three or more deliveries contribute only \(O_n(p^4)\) after subtracting their coincident values. Uniformly for bounded ordered offsets,
\[
 \frac{R_p(t_0+p y)-R_p(t_0,\ldots,t_0)}{v p^3}
 =H_n(y)+O_n(p),\quad
 H_n(y)=\frac12\sum_{i=1}^n y_i^2-\frac19\sum_{i<j}(y_j-y_i).
\]
The coercive strictly convex quadratic \(H_n\) has its unique (strictly ordered for \(n\ge2\)) minimum at
\[
 y_i=\frac{2i-n-1}{9},\qquad
 H_n^{\min}=-\frac{n(n^2-1)}{486}.
\]
The \(O_n(p)\) localization ensures the true rescaled minimizers stay in a compact set; uniform convergence to \(H_n\) then proves their convergence to these offsets. Finally, at coincident \(t_0\), all nonempty delivered sets yield the same information, so
\[
 R_p(t_0,\ldots,t_0)/v=\frac13-\frac8{27}[1-(1-p)^n].
\]
Combining with the minimum of \(H_n\) proves the stated risk asymptotic and the exact leading diversification advantage. \(\square\)

## Verification
The included `check.py` uses only exact rational arithmetic from Python's standard library. It enumerates delivered subsets, independently computes the cubic-gap objective, checks the algebraic coefficient of \(p^3\) against \(n(n^2-1)/486\) for \(1\le n\le6\), tests distinct nonoptimal offsets against the full limit quadratic, and verifies the exact perfect-delivery optima and nearby rational perturbations. It also checks improvement over the coincident design at two small rational success probabilities. Executing `python check.py` produced the supplied `check_output.txt` with **102 passed exact-rational assertions**. These finitely many checks are supplementary: the proof above handles every fixed positive integer \(n\), every real \(p>0\), and every admissible Lévy law.

## Relationship to prior work
Research on remote Wiener sampling under random delay and unreliable transmissions [1–3] optimizes causal, real-time or long-time-average signal tracking and yields threshold/stopping policies. That problem is not finite-horizon retrospective estimation of a path integral from a fixed nonadaptive batch with independently missing exact values. Multipoint fractional-Brownian bridge interpolation [4] concerns fixed-path reconstruction and Hurst-parameter inference, not optimal Bernoulli-erasure quadrature across Lévy laws. The pinned Brownian-bridge integral problem has different boundary conditions: both terminal gaps have bridge coefficient \(1/12\), so its one-observation optimum is \(1/2\); here the free terminal gap has coefficient \(1/3\) and the center is \(2/3\). Thus a pinned-bridge result does not imply the free-terminal universal Lévy staircase or its \(1/486\) coefficient. Standard conditional Poisson arrival-time results [5] explain linear bridge means for one special process, but do not determine these all-budget optimal designs.

## Limitations
The result requires stationary independent increments, a known first moment, a finite nonzero variance, exact successful readings, and independent identically distributed erasures independent of the path. The asymptotic expansion holds for each fixed \(n\) as \(p\downarrow0\), not uniformly for \(n\) growing with \(p^{-1}\). It does not cover adaptively chosen times, path-dependent loss probabilities, noisy successful readings, dependent packets, or arbitrary non-Lévy processes. At \(p=0\), no design is identifiable as optimal because all observations fail. Algebraic exactness does not certify historical priority: non-indexed work on stochastic quadrature or sensor scheduling could contain an equivalent formulation. Independent mathematical and literature review has not been performed.

## References
1. Y. Sun, Y. Polyanskiy and E. Uysal-Biyikoglu, *Remote Estimation of the Wiener Process over a Channel with Random Delay*, arXiv:1701.06734, first public 2017-01-24. https://arxiv.org/abs/1701.06734
2. F. Peng, X. Chen and J. Gong, *Optimal sampling policy of multi-dimensional wiener processes with random delivery time*, first public online 2021-10-11, DOI:10.1049/cth2.12205. https://doi.org/10.1049/cth2.12205
3. J. Pan, Y. Sun and N. B. Shroff, *Sampling for Remote Estimation of the Wiener Process over an Unreliable Channel*, arXiv:2310.11037, first public 2023-10-17. https://arxiv.org/abs/2310.11037
4. J. Friedrich, S. Gallon, A. Pumir and R. Grauer, *Stochastic interpolation of sparsely sampled time series via multi-point fractional Brownian bridges*, arXiv:2005.07591, first public 2020-05-15. https://arxiv.org/abs/2005.07591
5. H. Gomez Marquez, A. Ramirez-Nafarrate and R. López-Bracho, *Estimation of the expected value of the arrival epochs given a bounded period of observation for the homogeneous and non-homogeneous Poisson processes*, first public online 2020-08-05, DOI:10.1080/00949655.2020.1800707. https://doi.org/10.1080/00949655.2020.1800707
