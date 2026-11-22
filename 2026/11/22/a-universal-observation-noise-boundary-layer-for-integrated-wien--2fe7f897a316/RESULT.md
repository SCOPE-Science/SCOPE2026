# A universal observation-noise boundary layer for integrated Wiener trajectories

## Finding
Fix any integer \(p\ge0\). Let \(W\) be standard Brownian motion on \([0,1]\), set \(X_0(s)=W(s)\), and for \(p\ge1\) define
\[
X_p(s)=\frac1{(p-1)!}\int_0^s(s-u)^{p-1}W(u)\,du.
\]
Choose one time \(t\in[0,1]\) at which to observe \(Y_t=W(t)+\varepsilon\), where \(\varepsilon\) is independent centered Gaussian noise of variance \(\eta>0\). Minimize the integrated conditional variance
\[
R_p(t;\eta)=\int_0^1\operatorname{Var}(X_p(s)\mid Y_t)\,ds.
\]
For **every** \(p\ge0\) and **every** \(\eta>0\), there is exactly one minimizing time \(t_{p,\eta}\), it lies strictly between \(0\) and \(1\), and it increases strictly with \(\eta\). In particular, placing a noisy derivative/base-process measurement at the endpoint is never optimal at finite positive noise. As \(\eta\to\infty\), write \(a_p=[2(2p+3)]^{-1/(p+1)}\). Then
\[
1-t_{p,\eta}=a_p\eta^{-1/(p+1)}+O_p(\eta^{-2/(p+1)}),
\]
and the exactly optimized improvement in integrated risk over the terminal-time sensor is
\[
R_p(1;\eta)-R_p(t_{p,\eta};\eta)
=\frac{p+1}{p+2}\frac{a_p}{[(p+1)!]^2(2p+3)}\eta^{-2-1/(p+1)}
+o_p(\eta^{-2-1/(p+1)}).
\]
The boundary-layer exponent therefore depends on the number of integrations and is \(1/(p+1)\), rather than a fixed universal exponent.

## Assumptions and scope
Brownian motion has \(W(0)=0\), covariance \(\min(u,v)\), and unit diffusion variance. Observation noise is independent of the entire process and has exactly variance \(\eta\). Placement is over the closed interval \([0,1]\); the objective integrates posterior variance over the entire interval, rather than endpoint error. The result concerns one observation of the *base process* \(W(t)\), not an observation of \(X_p(t)\); these are different experimental designs. For each fixed integer order, constants in \(O_p\) may depend on that order; no joint large-order uniformity is asserted. No discrete grid, sensor-switching cost, or multiple observations are involved.

## Proof
**1. Exact conditional-risk reduction.** The covariance of \(X_p(s)\) with \(W(t)\), for any \(p\ge0\), is
\[
K_p(s,t)=\frac{s^{p+1}-(s-t)_+^{p+1}}{(p+1)!},\qquad (x)_+=\max(x,0).
\]
This follows for \(p=0\) from \(\min(s,t)=s-(s-t)_+\), and for \(p\ge1\) by integrating \(\min(u,t)\) against the displayed convolution kernel. The scalar Gaussian conditioning identity yields
\[
R_p(t;\eta)=V_p-\frac{I_p(t)}{t+\eta},\quad
V_p=\frac1{(p!)^2(2p+1)(2p+2)},\quad
I_p(t)=\int_0^1 K_p(s,t)^2\,ds.
\]
Both \(K_p\) and \(I_p\) are nonnegative; \(I_p(0)=0\), \(I_p'(t)>0\) for \(0<t<1\), and \(I_p(1)=1/([(p+1)!]^2(2p+3))\).

**2. One inflection point for every integration order.** Put \(z=1-t\) and \(y=t/z\). Differentiation under the integral, followed by the binomial theorem, gives
\[
I_p'(t)=\frac{2z^{2p+2}}{(p+1)!p!}P_p(y),\qquad
P_p(y)=\sum_{j=1}^{p+1}\frac{\binom{p+1}{j}}{2p+2-j}y^j.
\]
Consequently, the sign of \(I_p''(t)\) is the sign of
\[
S_p(y)=(1+y)P_p'(y)-(2p+2)P_p(y)
=\frac{p+1}{2p+1}-p\sum_{j=1}^{p}\frac{\binom{p+1}{j}}{2p+1-j}y^j-y^{p+1}.
\]
The formula also holds when \(p=0\), with the sum empty. For all \(y>0\), \(S_p\) is strictly decreasing, starts positive, and tends to \(-\infty\). Thus \(I_p\) is first strictly convex and then strictly concave, with exactly one inflection point \(\theta_p\in(0,1)\).

**3. Unique placement for all positive noise.** For \(0<t<1\), define
\[
H_p(t)=\frac{I_p(t)}{I_p'(t)}-t.
\]
Direct differentiation gives \(H_p'(t)=-I_p(t)I_p''(t)/[I_p'(t)]^2\). Since \(I_p(t)\sim t^2/[(p!)^2(2p+1)]\) as \(t\downarrow0\), one has \(H_p(t)\sim-t/2\). Therefore \(H_p\) decreases from \(0\) to a negative minimum at \(\theta_p\), then strictly increases to \(+\infty\) as \(t\uparrow1\). The derivative of the risk reduction \(I_p(t)/(t+\eta)\) has the sign of \(\eta-H_p(t)\). Hence there is exactly one positive solution \(H_p(t)=\eta\); the reduction increases before it and decreases after it. The endpoint \(t=0\) provides zero reduction; \(t=1\) is inferior to nearby interior times because \(I_p'(1)=0\). Thus this solution is the unique global minimizer of risk. Because it lies on the strictly increasing branch of \(H_p\), its location increases strictly with \(\eta\).

**4. High-noise scale and sharp regret.** Put \(z=1-t\). Expanding the exact squared covariance yields
\[
I_p(1)-I_p(1-z)
=\frac{1}{[(p+1)!]^2}\int_0^z
\left[2(1-z+u)^{p+1}u^{p+1}-u^{2p+2}\right]du
=\frac{2z^{p+2}}{(p+2)[(p+1)!]^2}+O_p(z^{p+3}).
\]
Thus \(I_p'(1-z)=2z^{p+1}/[(p+1)!]^2+O_p(z^{p+2})\). The first-order condition \((\eta+t)I_p'(t)=I_p(t)\) and \(t_{p,\eta}\uparrow1\) imply
\[
(1-t_{p,\eta})^{p+1}=\frac{1}{2(2p+3)\eta}\bigl(1+O_p(\eta^{-1/(p+1)})\bigr),
\]
which proves the stated location expansion. Finally substitute \(z=a_p\eta^{-1/(p+1)}+O_p(\eta^{-2/(p+1)})\) into
\[
\frac{I_p(1-z)}{\eta+1-z}-\frac{I_p(1)}{\eta+1}
=\frac{I_p(1)z}{\eta^2}-\frac{2z^{p+2}}{(p+2)[(p+1)!]^2\eta}
+o_p(\eta^{-2-1/(p+1)}).
\]
The identity \(2a_p^{p+1}=1/(2p+3)\) reduces the leading constant to the displayed risk-regret value. All estimates hold for each fixed integer \(p\).

## Verification
A standalone \(\texttt{verify.py}\) performs exact polynomial checks at integration orders \(0\) through \(8\) of the inflection-sign identity, endpoint covariance identities, and leading asymptotic coefficients; it also performs bounded scalar optimization at two high noise levels. Its successful run reported 99 exact and supplementary checks. Those finite checks are supplementary: the proof above establishes the identities for all integers \(p\ge0\) by the binomial theorem and the coefficient signs. Examples: for \(p=0\), \(1-t_{0,\eta}\sim1/(6\eta)\) with regret \(\sim1/(36\eta^3)\); for \(p=1\), \(1-t_{1,\eta}\sim(10\eta)^{-1/2}\) with regret \(\sim1/(30\sqrt{10}\eta^{5/2})\).

## Relationship to prior work
Schober, Duvenaud and Hennig (2014) use integrated-Wiener Gaussian-process priors and derivative-like evaluations in probabilistic numerical ODE solvers; their Runge–Kutta-matching theorems do not assert an optimal noisy one-point location or an all-order high-noise placement exponent. Ji and Müller (2016) establish a general integrated prediction-error criterion for optimally timed noisy *process-value* observations, but not the present joint base-process/iterated-integral observation model or its explicit classification. Mukherjee's earlier dissertation develops integrated path-error optimal designs for various directly sampled stochastic processes, including Brownian and Ornstein–Uhlenbeck processes; the catalog does not establish coverage of the present observation modality, and its full text was not available for comparison. The distinction between observing \(W(t)\) and observing \(X_p(t)\) matters: neither corresponding optimal-location theorem follows from the other by changing the integration order.

## Limitations
Only one observation with independent homoscedastic Gaussian noise is treated. The high-noise expansions are fixed-order, not uniform as \(p\to\infty\). The analysis does not establish optimality for sampled sensor grids, correlated errors, unknown prior scale, arbitrary fractional integration orders or general Gaussian processes. Literature coverage is bounded by accessible primary texts and research indexes; an equivalent historical formulation may exist. Independent mathematical validation has not been performed.

## References
- M. Schober, D. Duvenaud and P. Hennig, *Probabilistic ODE Solvers with Runge-Kutta Means* (2014), arXiv:1406.2582, https://arxiv.org/abs/1406.2582. Public first version: 2014-06-10.
- H. Ji and H.-G. Müller, *Optimal Designs for Longitudinal and Functional Data* (2016), arXiv:1604.05375, https://arxiv.org/abs/1604.05375. Public first version: 2016-04-18.
- B. Mukherjee, *Optimal designs for estimating the path of a stochastic process*, Purdue University dissertation, catalog https://docs.lib.purdue.edu/dissertations/AAI3043760/ (full text not obtained).
