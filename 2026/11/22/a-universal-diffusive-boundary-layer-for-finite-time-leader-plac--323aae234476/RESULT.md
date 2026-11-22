# A universal diffusive boundary layer for finite-time leader placement on paths

## Finding
For the unweighted path \(P_n\) on vertices \(0,\ldots,n-1\), \(n\ge3\), select exactly one perfectly grounded leader \(j\). Write \(L_{FF}(j)\) for the unnormalized combinatorial Laplacian after deleting the leader row and column, and minimize the finite-horizon heat trace
\[
H_n(t,j)=\operatorname{tr}\big(e^{-tL_{FF}(j)}\big),\qquad t>0.
\]
There is a universal constant \(\xi\) such that for **every** sequence of horizons \(t\to\infty\) and integers \(n=n(t)\) with \(n/\sqrt t\to\infty\), **every** minimizing leader \(j=j(t)\) satisfies
\[
\frac{\min\{j,n-1-j\}}{\sqrt t}\longrightarrow \xi,
\qquad 0.86518<\xi<0.86519.
\]
The constant is the **unique** positive zero of
\[
\sum_{k=1}^{\infty}(-1)^k(1-2k^2\xi^2)e^{-k^2\xi^2}=0,
\]
and numerically \(\xi=0.8651854893390056\ldots\). The coefficient refers to \(e^{-tL}\), not \(e^{-2tL}\).

For each fixed finite \(n\ge3\), the only minimizers for all sufficiently small positive \(t\) are the two endpoints; for all sufficiently large \(t\), the minimizing leaders are precisely the central vertex (odd \(n\)) or two central vertices (even \(n\)). Thus the diffusive boundary layer describes a genuine migration between different intervention regimes. The statement does **not** claim an exact finite-size sequence or count of intermediate transitions.

## Assumptions and scope
All path edges have conductance one, original endpoint degrees one, and internal degrees two. Grounding is perfect (the leader is removed, with diagonal follower degrees retained). All times and matrix exponentials use the same unit-rate continuous-time Laplacian. There is exactly one grounded leader. A minimizer exists because there are finitely many possible vertices. The asymptotic hypothesis \(n/\sqrt t\to\infty\) is essential: for \(t\) comparable to \(n^2\), endpoints are not a valid isolated-boundary limit.

## Proof
**1. Exact block spectrum.** The leader at \(j\) splits its followers into lengths \(j\) and \(n-1-j\). Each nonempty block is the tridiagonal matrix \(A_\ell\) with diagonal \((1,2,\ldots,2)\) and adjacent off-diagonals \(-1\), and the zero-length block contributes zero. The eigenvalues are exactly
\[
\lambda_{\ell,r}=2-2\cos\frac{(2r-1)\pi}{2\ell+1},\qquad 1\le r\le\ell.
\]
Define \(a_\ell(t)=\sum_{r=1}^\ell e^{-t\lambda_{\ell,r}}\) and \(a_0=0\). Consequently
\[
H_n(t,j)=a_j(t)+a_{n-1-j}(t).
\]
The characteristic recurrence \(p_0=1\), \(p_1=z-1\), \(p_\ell=(z-2)p_{\ell-1}-p_{\ell-2}\) verifies the normalization.

**2. The short- and long-horizon endpoints.** A matrix exponential expansion gives
\[
H_n(t,j)=(n-1)-t\big(2(n-1)-\deg_{P_n}(j)\big)+O_n(t^2).
\]
An endpoint has degree one and any other vertex degree two, so precisely the two endpoints win for all sufficiently small \(t>0\). At large \(t\), the smallest eigenvalue of \(L_{FF}(j)\) is \(2-2\cos(\pi/(2\ell+1))\), where \(\ell=\max\{j,n-1-j\}\). This is strictly decreasing in \(\ell\); hence central sites, and only central sites, eventually minimize the trace.

**3. Two uniform heat-trace limits.** Set
\[
c(t)=\frac1\pi\int_0^\pi e^{-t(2-2\cos\theta)}\,d\theta,
\qquad \sqrt t\,c(t)\to\frac1{2\sqrt\pi}.
\]
For \(\ell/\sqrt t\to x\) with \(0<x<\infty\), the exact eigenvalue formula and dominated convergence give
\[
a_\ell(t)\to h(x)=\sum_{r=0}^{\infty}\exp\!\left(-\frac{\pi^2(r+1/2)^2}{x^2}\right).
\]
If \(\ell/\sqrt t\to0\), then \(a_\ell(t)\to0\). If \(\ell/\sqrt t\to\infty\), the uniform midpoint quadrature estimate yields
\[
a_\ell(t)-\ell c(t)\to0.
\]
For completeness, the quadrature nodes are the midpoints of intervals of width \(\Delta=2\pi/(2\ell+1)\), with the last half interval omitted. For \(f_t(\theta)=e^{-t(2-2\cos\theta)}\), its derivative has total variation \(O(\sqrt t)\), so the midpoint remainder, after division by \(\Delta\), is \(O(\Delta\sqrt t)\); the final omitted half interval is \(O(e^{-3t})\). This gives \(a_\ell=(\ell+1/2)c(t)+O(\sqrt t/\ell)+O(e^{-3t})\), proving the claimed limit. The same estimates are uniform for \(\ell/\sqrt t\) bounded away from zero or diverging.

Reflect the path if necessary and take \(0\le j\le (n-1)/2\). Then \((n-1-j)/\sqrt t\to\infty\) under the stated assumption, uniformly over such \(j\). Subtracting the \(j\)-independent reference \((n-1)c(t)\) therefore gives
\[
H_n(t,j)-(n-1)c(t)=a_j(t)-jc(t)+o(1).
\]
If \(j/\sqrt t\to x\in(0,\infty)\), the right side tends to
\[
G(x)=h(x)-\frac{x}{2\sqrt\pi}.
\]
If the ratio tends to zero or infinity, the right side tends to zero. (The infinity case uses the midpoint estimate on both blocks.)

**4. The universal variational problem.** Jacobi's Gaussian Poisson-summation identity gives the absolutely convergent alternatives
\[
G(x)=\frac{x}{\sqrt\pi}\sum_{k=1}^{\infty}(-1)^k e^{-k^2x^2}
=\sum_{r=0}^{\infty}e^{-\pi^2(r+1/2)^2/x^2}-\frac{x}{2\sqrt\pi}.
\]
The function tends to zero at both ends of the positive line and \(G(1)<0\), so it has an interior global minimizer. Its derivative is
\[
G'(x)=\frac1{\sqrt\pi}\sum_{k=1}^{\infty}(-1)^k(1-2k^2x^2)e^{-k^2x^2}.
\]
We show it has exactly one zero. For \(0<x\le7/10\), differentiate the second representation. Each positive derivative summand \(2\pi^2(r+1/2)^2x^{-3}e^{-\pi^2(r+1/2)^2/x^2}\) increases up to \(x=7/10\), and their sum there is less than \(0.11<1/(2\sqrt\pi)\); therefore \(G'<0\) in this range. For \(x\ge1\), set \(b_k=(2k^2x^2-1)e^{-k^2x^2}\). The terms are positive, \(b_1>b_2\) because \((8x^2-1)(2x^2-1)^{-1}e^{-3x^2}\le7e^{-3}<1\), and \(b_k\) decreases in \(k\ge2\); thus \(G'=(b_1-b_2+b_3-b_4+\cdots)/\sqrt\pi>0\).

On \(7/10\le x\le1\), the reproducible, **exact-rational** interval certificate in `VERIFY.py` divides this range into 40 closed panels. For each, its Taylor enclosures for \(e^{-z}\) rigorously show that the first five terms of \(\sqrt\pi G''(x)\) sum to more than \(1.40\). The sum of all terms with \(k\ge6\) has absolute value less than \(0.001\) uniformly on that range, by the geometric majorant \(\sum_{k\ge6}(4k^4+6k^2)e^{-0.49k^2}\). Hence \(G''>0\) throughout the middle range. The same rational exponential bounds and an explicit tail below \(10^{-6}\) certify opposite signs of \(G'\) at \(0.86518\) and \(0.86519\). The single zero \(\xi\) is therefore the unique global minimizer of \(G\).

**5. Convergence of every minimizing placement.** Choosing a leader at \(j=\lfloor\xi\sqrt t\rfloor\) (or its reflection) gives centered objective tending to \(G(\xi)<0\). Any sequence of minimizing positions may be reflected to the left half. A subsequence with its scaled distance tending to zero or infinity would instead have centered cost tending to zero, contradicting this comparison. Every remaining convergent subsequence has finite positive limit \(x\), and optimality forces \(G(x)\le G(\xi)\), so uniqueness implies \(x=\xi\). This proves convergence for **all** minimizing choices.

## Verification
Run `python VERIFY.py` with the listed Python dependencies. It verifies the exact rational 40-panel curvature certificate, signed root bracket with rigorously bounded exponential tails, and twelve exact tridiagonal characteristic polynomials. It additionally prints numerical finite-path checks (only corroborative). No random sampling, floating-point root finder, or asymptotic regression is used to justify the theorem. The coefficient and horizon normalization are explicit in the first section.

## Relationship to prior work
Clark, Alomair, Bushnell and Poovendran (arXiv:1306.4949, first public 2013-06-20) study finite-time convergence-error upper bounds and leader-selection approximation, not the sum of all grounded heat eigenmodes or the present path limit. Patterson, McGlohon and Dyagilev (arXiv:1412.6595, 2014-12-20; arXiv:1604.07094, 2016-04-24) solve one-dimensional leader selection for stationary inverse-trace coherence and smallest-eigenvalue convergence rate, not finite-time heat-trace minimization. Both objectives have structural connections but neither implies the universal \(\sqrt t\) location law here. Closest related individual network findings involve different functionals, including screened-path Nyström selection and cycle heat traces; those claims do not entail a grounded path's finite-time boundary-layer constant.

## Limitations
This result treats one leader, unit edge rates, perfect grounding, the unnormalized Laplacian, and the regime \(\sqrt t=o(n)\). It does not classify all finite-time switches for individual finite paths, weighted paths, multiple leaders, or objectives with source-specific initial-condition covariance. Independent mathematical validation and exhaustive world-literature coverage have not been performed. The interval certificate concerns only the uniqueness of the continuum variational constant; the discrete-to-continuum passage is proved analytically.

## References
1. A. Clark, B. Alomair, L. Bushnell, R. Poovendran, *Minimizing Convergence Error in Multi-Agent Systems via Leader Selection: A Supermodular Optimization Approach*, arXiv:1306.4949, first public 2013-06-20. https://arxiv.org/abs/1306.4949
2. S. Patterson, N. McGlohon, K. Dyagilev, *Efficient, Optimal k-Leader Selection for Coherent, One-Dimensional Formations*, arXiv:1412.6595, first public 2014-12-20. https://arxiv.org/abs/1412.6595
3. S. Patterson, N. McGlohon, K. Dyagilev, *Optimal k-Leader Selection for Coherence and Convergence Rate in One-Dimensional Networks*, arXiv:1604.07094, first public 2016-04-24. https://arxiv.org/abs/1604.07094
