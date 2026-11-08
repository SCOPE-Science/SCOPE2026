# Variance-optimal spoke conductance in random wheel spanning trees

## Finding

Let \(W_{n+1}=K_1\vee C_n\) be the wheel with \(n\ge3\) rim vertices. Give every rim edge conductance \(1\) and every spoke conductance \(t>0\). Choose a spanning tree with probability proportional to the product of its edge conductances, and let \(S_n(t)\) denote its number of spokes (the unweighted degree of the hub). Set \(\rho=2-\sqrt3\).

**Theorem (asymptotically unique optimal spoke conductance).** For all sufficiently large integers \(n\), \(V_n(t)=\operatorname{Var}(S_n(t))\) has exactly one global maximizer \(t_n>0\). It satisfies \(t_n>2\) and
\[
\lim_{n\to\infty}\frac{t_n-2}{n^2\rho^n}=12,\qquad
\max_{t>0}V_n(t)=\frac{n}{3\sqrt3}-\frac23n^2\rho^n(1+o(1)).
\]

This theorem does not assert global uniqueness for the finitely many wheel sizes outside the eventual range; it specifies no numerical cutoff for that range. Its exact finite-size identities, used in the proof, hold for every \(n\ge3\):
\[
V_n(t)=\sum_{j=1}^{n-1}\frac{t\lambda_j}{(t+\lambda_j)^2},\qquad
\lambda_j=2-2\cos\!\left(\frac{2\pi j}{n}\right).
\]

## Assumptions and scope

All graphs are simple and undirected. The rim is the cycle \(C_n\); the hub is joined to each rim vertex. The conductance parameter controls the *sampling weight* of a tree, while the random variable counts spokes without conductance weighting. Thus the two notions of weight are not conflated. All limits take integer \(n\to\infty\) with the rim conductance fixed at one and the spoke conductance optimized separately for each \(n\). No claims about arbitrary non-wheel networks or nonuniform spoke weights are made.

## Proof

**1. Determinantal partition polynomial.** Delete the hub row and column from the weighted Laplacian. The remaining principal minor is \(L(C_n)+tI\). By the matrix-tree theorem, the spanning-tree partition polynomial by spoke count is
\[
Z_n(t)=\det(L(C_n)+tI)=\prod_{j=0}^{n-1}(t+\lambda_j).
\]
The cycle eigenvalues are the \(\lambda_j\) above, including \(\lambda_0=0\). Thus \(\mathbb E[z^{S_n(t)}]=Z_n(tz)/Z_n(t)\). Factoring the positive linear terms shows that \(S_n(t)\) is equal in law to \(1\) plus independent Bernoulli variables with success probabilities \(t/(t+\lambda_j)\) for \(1\le j<n\), and proves the stated variance formula. Equivalently, with \(T_n\) the ordinary Chebyshev polynomial, \(Z_n(t)=2(T_n(1+t/2)-1)\).

**2. Exact hyperbolic form.** Put \(\theta=\operatorname{arcosh}(1+t/2)\), \(q=\sqrt{t/(t+4)}\), and \(v(t)=2\sqrt t/(t+4)^{3/2}\). The polynomial identity gives \(Z_n(t)=2(\cosh(n\theta)-1)\). The mean and variance are the first two logarithmic derivatives \((t\partial_t)^k\log Z_n(t)\). Using \(t\theta'(t)=q\), differentiation yields
\[
\mathbb E[S_n(t)]=nq\coth(n\theta/2),
\quad
V_n(t)=nv(t)\coth(n\theta/2)-\frac{n^2q^2}{2}\operatorname{csch}^2(n\theta/2).
\]
These are exact, including at every finite \(n\ge3\). In particular, since \(\theta(2)=\log(2+\sqrt3)\), letting \(\delta_n=\rho^n\) and differentiating gives
\[
V_n'(2)=\frac{n^2\delta_n}{3(1-\delta_n)^3}
\left[\frac n{\sqrt3}(1+\delta_n)-(1-\delta_n)\right]>0
\quad(n\ge3).
\]
Every factor in the last expression is positive; the bracket is positive since \(n/\sqrt3>1\).

**3. Global localization of maximizers.** By uniform Riemann-sum convergence on every compact subinterval of \((0,\infty)\),
\[
\frac{V_n(t)}n\longrightarrow
\frac1{2\pi}\int_0^{2\pi}\frac{t(2-2\cos u)}{(t+2-2\cos u)^2}\,du
=v(t),
\]
with the first and second derivatives converging uniformly on these compact intervals. The integral identity follows either by differentiating the standard cycle resolvent integral \((2\pi)^{-1}\int_0^{2\pi}(t+2-2\cos u)^{-1}du=[t(t+4)]^{-1/2}\), or by the exact hyperbolic formula.

This convergence also localizes *global* maximizers: if \(t\ge M\), then \(V_n(t)/n\le (\sum_j\lambda_j)/(nt)=2/t\). If \(0<t\le\varepsilon\), for an arbitrary spectral cutoff \(\eta>0\), use \(t\lambda/(t+\lambda)^2\le 1/4\) on \(\lambda<\eta\) and at most \(t/\eta\) elsewhere. Hence
\[
\limsup_{n\to\infty}\sup_{0<t\le\varepsilon}\frac{V_n(t)}n
\le\frac14\limsup_{n\to\infty}\frac{\#\{j:\lambda_j<\eta\}}n+\frac\varepsilon\eta.
\]
The eigenvalue proportion is \(O(\sqrt\eta)\) as \(\eta\downarrow0\). Taking \(\varepsilon\downarrow0\), with \(\eta\) chosen first, bounds all possible small-parameter maxima away from the positive global limiting peak. The large-parameter bound does the same at infinity. Since \(v'(t)=2(2-t)/(\sqrt t(t+4)^{5/2})\), the function \(v\) has a unique global maximum at \(t=2\). Therefore every maximizing sequence of \(V_n\) tends to \(2\).

**4. Eventual uniqueness and displacement.** Direct differentiation yields
\[
v''(t)=\frac{4(t^2-4t-2)}{t^{3/2}(t+4)^{7/2}}.
\]
It is strictly negative throughout \([3/2,5/2]\). By the compact uniform second-derivative convergence established above, \(V_n''<0\) on that interval for all sufficiently large \(n\). By Step 3 all global maximizers lie within that interval for these \(n\); thus there is exactly one, and the exact formula for \(V_n'(2)>0\) places it strictly to the right of \(2\).

The derivative formula gives \(V_n'(2)\sim n^3\rho^n/(3\sqrt3)\). The mean-value theorem at the unique maximizer gives \(0=V_n'(2)+V_n''(\xi_n)(t_n-2)\) for some \(\xi_n\) between \(2\) and \(t_n\). Because \(\xi_n\to2\), \(V_n''(\xi_n)/n\to v''(2)=-1/(36\sqrt3)\). Therefore \((t_n-2)/(n^2\rho^n)\to12\), as claimed.

Finally the exact hyperbolic formula at \(t=2\) gives
\[
V_n(2)=\frac n{3\sqrt3}\frac{1+\delta_n}{1-\delta_n}-\frac{2n^2}{3}\frac{\delta_n}{(1-\delta_n)^2}
=\frac n{3\sqrt3}-\frac23n^2\rho^n(1+o(1)).
\]
The shift improves the value by only \(O(n^5\rho^{2n})\), by the first-derivative estimate, displacement bound, and compact second-derivative bound. This is \(o(n^2\rho^n)\), proving the asserted optimized variance expansion.

## Verification

The standalone `checker.py` reconstructs \(Z_n\) by the Chebyshev recurrence, independently counts all spanning trees of \(W_{n+1}\) by spoke number for \(3\le n\le8\), and compares exact first and second moments at rational values of \(t\). It also compares the spectral and polynomial variance expressions numerically for \(3\le n\le40\). All 188 checks passed in a clean execution. These finite checks support the finite algebra and do **not** constitute the proof of the infinite-size assertion, which is given in Steps 2–4.

Run: `python3 checker.py` from the directory containing this file and the checker. No nonstandard packages are required.

## Relationship to prior work

Fita Sanmartín, Schnörr and Hamprecht [1] derive general Gibbs-spanning-tree degree moment formulas. Their Example 4.1 explicitly gives the spectral variance for a universal hub, a result that **already implies Step 1's variance sum** on a wheel. Neither that formula nor the Chebyshev determinant is claimed as new. Rapoport [2] treats degree correlations and distributions in the unweighted UST setting, not the present optimization of a variable spoke conductance. The contribution here is the **eventual uniqueness of the global conductance maximizing hub-degree variance and the sharp exponential finite-size displacement and peak deficit**, which are not stated in these inspected treatments. Independently developed wheel-based geometric optimization problems optimize other functionals; coincidence of a limiting numerical parameter alone does not imply the present stochastic-variance asymptotics.

## Limitations

The exact finite-size variance and the Poisson-binomial factorization follow from known general determinantal theory. No explicit smallest wheel size for uniqueness is proved here; the claim only asserts uniqueness for sufficiently large \(n\). The asymptotic optimum concerns a single shared spoke conductance with all rim edges normalized to one. The literature checks establish a bounded best-knowledge novelty comparison, not a guarantee of global priority. An independent mathematical audit has not yet been performed.

## References

1. E. Fita Sanmartín, C. Schnörr and F. A. Hamprecht, *Expectation and Variance of the Degree of a Node in Random Spanning Trees*, arXiv:2409.13472, first public 2024-09-20; Theorem 4.1, Remark 4.2, Example 4.1.
2. A. Rapoport, *Correlations in uniform spanning trees: a fermionic approach*, arXiv:2312.14992, first public 2023-12-22; introduction and degree-law sections.
