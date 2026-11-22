# Finite-time extinction with a sharp exploding-moment phase in Bernoulli-interpolated Nesterov acceleration

## Finding

Fix \(L>0\), \(p\in(0,1)\), and \(\beta\in(0,1)\). A scalar Nesterov iteration using unbiased, interpolating component gradients reaches the exact minimizer **in finite time almost surely**, yet its expected squared error may **grow exponentially**. For any nonzero deterministic initialization \(x_{-1}=x_0\), the sharp trichotomy is

\[
\begin{array}{ll}
\mathbb E x_n^2\longrightarrow 0\ \text{exponentially}, & (1-p)\beta(1+2\beta)<1,\\
\mathbb E x_n^2\longrightarrow C\in(0,\infty), & (1-p)\beta(1+2\beta)=1,\\
\mathbb E x_n^2\longrightarrow\infty\ \text{exponentially}, & (1-p)\beta(1+2\beta)>1.
\end{array}
\]

The critical/unstable regimes occur precisely when \(\beta>1/2\) and \(p\le 1-1/[\beta(1+2\beta)]\). For instance, \(\beta=3/4\) gives the exact critical sampling probability \(p=7/15\). Thus \(p=1/4\) is mean-square explosive despite exact pathwise termination, whereas \(p=1/2\) is mean-square convergent. The result also gives an exact generating function and a sharp exponential equivalent, not just a stability inequality.

## Assumptions and scope

The population objective is the strongly convex quadratic \(f(x)=pLx^2/2\). Draw independently \(B_k\sim\operatorname{Bernoulli}(p)\), and use the oracle gradient \(g_k=LB_k y_k\). It obeys \(\mathbb E[g_k\mid y_k]=\nabla f(y_k)\), with each component function minimized at zero. The zero-curvature component is convex but not strongly convex. Set the step to \(1/L\), and use the **lookahead Nesterov** recursion, for all integers \(k\ge0\),

\[
y_k=x_k+\beta(x_k-x_{k-1}),\qquad
x_{k+1}=y_k-\frac1L g_k=(1-B_k)y_k,
\qquad x_{-1}=x_0\ne0.
\]

All expectations refer to the independent Bernoulli sequence, and all claims concern exact arithmetic. Write \(q=1-p\). For \(g=0,1,2,\ldots\), define
\[
c_g=\beta\frac{1-\beta^g}{1-\beta},\qquad c_0=0.
\]

## Proof

**1. Exact absorption and its waiting time.** Every missed gradient leaves the initial pair \((x_k,x_{k-1})=(x_0,x_0)\) unchanged until the first active gradient. An active gradient sets the new iterate to zero. If the preceding state just after an active gradient is \((0,a)\) with \(a\ne0\), exactly \(g\) subsequent misses make the pair \((-c_ga,-c_{g-1}a)\) for \(g\ge1\), as follows by induction from \(x_{k+1}=(1+\beta)x_k-\beta x_{k-1}\). Since \(\beta\in(0,1)\), every \(c_g>0\) for \(g\ge1\). Thus a successful gradient after \(g\ge1\) misses resets to \((0,-c_ga)\) but does not annihilate the entire state. A second success with no intervening misses does annihilate it. Consequently, *the first two consecutive active Bernoulli gradients are exactly the first time of permanent absorption*. Such a pair occurs almost surely. Conditioning on the previous draw gives the standard two-success waiting-time expectation \(\mathbb E T=(1+p)/p^2\) updates.

**2. Renewal weights.** Regard each nonabsorbing success as a reset of the first coordinate to zero; its predecessor has nonzero amplitude \(a\). The number \(g\) of misses before the next success has probability \(p q^g\). The next predecessor amplitude is \(-c_ga\). Thus squared predecessor mass passed between successes across a gap of length \(m=g+1\) has kernel

\[
k_m=pq^{m-1}c_{m-1}^2\quad(m\ge2),\qquad k_0=k_1=0.
\]

Let \(K(z)=\sum_{m\ge2} k_m z^m\). Summing three geometric series gives, for \(|z|<1/q\),
\[
K(z)=p z\sum_{g\ge1}q^g c_g^2z^g
=\frac{p\beta^2qz^2(1+\beta qz)}{(1-qz)(1-\beta qz)(1-\beta^2qz)}.
\]

Starting immediately after a reset with predecessor amplitude one, let \(u_n\) denote expected squared predecessor mass carried by a nonabsorbed reset at relative time \(n\). The renewal relation is \(u_0=1\) and \(u_n=\sum_{m=2}^n k_m u_{n-m}\), so \(\sum_{n\ge0}u_nz^n=[1-K(z)]^{-1}\). The current squared iterate at relative time \(n\), after \(g\) trailing missed gradients, is \(c_g^2\) times its predecessor squared mass at the latest reset. Its generating function is
\[
\frac{\sum_{g\ge0}q^gc_g^2z^g}{1-K(z)}=\frac{K(z)}{pz[1-K(z)]}.
\]

From \(x_{-1}=x_0\), the first active gradient occurs after \(t-1\) misses with probability \(p q^{t-1}\), while paths with no success have \(x_n=x_0\). Summing the geometric first-success distribution therefore yields the exact identity
\[
\boxed{\displaystyle
H(z):=\sum_{n\ge0}\frac{\mathbb E x_n^2}{x_0^2}z^n
=\frac{1}{(1-qz)[1-K(z)]}.}
\]

**3. Dominant renewal pole and exact rate.** Every coefficient \(k_m\) for \(m\ge2\) is strictly positive. On the positive real interval \((0,1/q)\), \(K\) increases strictly from zero to infinity. Thus there is exactly one \(r\in(0,1/q)\) satisfying \(K(r)=1\), and \(K'(r)>0\). For \(|z|<r\), \(|K(z)|\le K(|z|)<1\); for \(|z|=r\), equality in the triangle inequality requires that the positive powers \(z^2,z^3,\ldots\) have the same phase, forcing \(z=r\). Hence \(r\) is the unique nearest singularity of the rational function \(H\), a simple pole. Coefficient extraction of this isolated pole yields
\[
\boxed{\displaystyle
\mathbb E x_n^2\sim
\frac{x_0^2}{(1-qr)rK'(r)}\,r^{-n}.}
\]

This is an asymptotic equivalent with a strictly positive prefactor, for every prescribed \(p,\beta\in(0,1)\). A finite-time enumeration is not used to infer this infinite-horizon statement.

**4. Sharp phase boundary.** Since \(K\) increases strictly, \(r>1\), \(r=1\), or \(r<1\) if and only if \(K(1)<1\), \(K(1)=1\), or \(K(1)>1\). With \(q=1-p\), exact simplification gives
\[
K(1)=\frac{\beta^2q(1+\beta q)}{(1-\beta q)(1-\beta^2q)},\qquad
K(1)-1=\frac{q\beta(1+2\beta)-1}{(1-\beta q)(1-\beta^2q)}.
\]

Both denominator factors are positive, proving the stated trichotomy. At equality the limit is explicitly \(x_0^2/[pK'(1)]>0\). For \(\beta\le1/2\), the expression \(q\beta(1+2\beta)\) is strictly below one; for \(\beta>1/2\), equality occurs at \(p=1-1/[\beta(1+2\beta)]\). All boundary assertions follow.

## Verification

The included standalone standard-library program `verify_nesterov.py` enumerates Bernoulli paths with **exact rational arithmetic** and independently computes coefficients of the renewal generating function for four success probabilities, four momentum parameters, and eleven horizons; it checks 227 exact equalities/inequalities in total. It tests the rational critical parameter and the sign of either side of the phase transition. Execute `python3 verify_nesterov.py` from the extracted package directory. Finite enumerations verify the algebraic reduction but do not replace the analytic pole argument.

## Relationship to prior work

Li and Wang (2026) prove deterministic linear convergence for constant momentum Nesterov acceleration across all \(\beta\in[0,1)\), under strong convexity, in their equation (1.1) and Theorem 4.15. The present random-curvature construction retains a strongly convex **population** objective and interpolation, but departs from the exact deterministic-gradient hypothesis. Assran and Rabbat (2020), especially Theorem 3, demonstrate finite-sum stochastic Nesterov divergence for specially constructed strongly convex components and sampling patterns. Their result concerns expectation of the iterate error, whereas ours gives pathwise **finite termination** together with exact second-moment divergence or a nonzero limit, calibrated by a scalar Bernoulli probability.

Sharma et al. (2026), Algorithm 1 and Theorem 1, derive a general second-moment spectral criterion for **outer buffer momentum** on stochastic pseudo-gradients. Their state update \(u_t=\beta u_{t-1}+P_t\), \(\theta_{t+1}=\theta_t-\alpha(\beta u_t+P_t)\) is not the Nesterov extrapolate-then-gradient recursion above: a single successful curvature draw in their scheme does not null the new extrapolate. Their general jump-linear methodology motivates moment analysis but does not directly imply the present two-success exact extinction or formula. The published published-finding corpus result *All-order moment thresholds despite finite-time extinction in dropout-averaged iterations* treats a **different positive two-lag average** \(Y_t=A_t(Y_{t-1}+Y_{t-2})/2\); it does not imply the phase boundary for the signed Nesterov no-gradient evolution \((1+\beta)x_k-\beta x_{k-1}\). Broad random-coefficient autoregressive methods may also yield related general statements; the novel claimed content is this exact optimizer-specific renewal law, critical sampling threshold, and sharp rate, not an assertion that the generic phenomenon of random-moment explosion was unknown.

## Limitations

This theorem is confined to a scalar population quadratic, independent Bernoulli zero-or-full curvature gradients, constant momentum strictly between zero and one, and step \(1/L\). The zero-curvature component is not individually strongly convex. Results do not extend by the given proof to arbitrary smooth objectives, nonzero additive gradient noise, dependent sampling, other stepsizes, or a different momentum implementation. The exact root and phase boundary are proved, but there has been no independent mathematical audit or exhaustive historical-priority certification.

## References

1. H. Li and X. Wang, *Linear Convergence of Nesterov's Acceleration for All Momentum Parameter* (2026), arXiv:2611.10205v1, first publicly submitted 2026-11-06, https://arxiv.org/abs/2611.10205.
2. M. Assran and M. Rabbat, *On the Convergence of Nesterov's Accelerated Gradient Method in Stochastic Settings*, Proceedings of Machine Learning Research 119 (2020), 410–420, https://proceedings.mlr.press/v119/assran20a.html.
3. N. Sharma, L. Gomezjurado Gonzalez, G. Talluri, S. Chandar, and H. Naganuma, *Understanding Stability of Outer Nesterov Momentum on Stochastic Pseudo-Gradients* (2026), arXiv:2610.22623v1, https://arxiv.org/abs/2610.22623.
4. *All-order moment thresholds despite finite-time extinction in dropout-averaged iterations* (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-all-order-moment-thresholds-despite-finite-time-extinction-in-dr--31c71a26296d.
