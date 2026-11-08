# All-order first-passage moment thresholds and orientation memory in a logarithmic run-and-tumble trap

## Finding

For the velocity-jump model defined below, all positive integer first-passage moments have a sharp ladder of finiteness transitions. Write \(\beta=2\gamma/v^2\) and
\[
C_0=1,\qquad C_n=\frac{1}{2^n\prod_{j=1}^{n}(1-(2j-1)/\beta)}.
\]
For every integer \(n\ge1\), every \(x>a\), and either initial orientation,
\[
\mathbb E_{x,\pm}T^n<\infty\quad\Longleftrightarrow\quad \beta>2n-1.
\]
In that regime,
\[
\mathbb E_{x,\pm}T^n\sim C_n x^{2n},\qquad
\mathbb E_{x,+}T^n-\mathbb E_{x,-}T^n
\sim \frac{2nC_{n-1}}{v(\beta-2n+1)}x^{2n-1}
\quad(x\to\infty).
\]
The novel contribution is the complete hierarchy, particularly orders \(n\ge3\), and the orientation-sensitive leading difference. The order-one mean and the order-two threshold/leading moment were previously known, as credited below. For example, the third moment is finite exactly when \(\gamma>5v^2/2\), and then \(\mathbb E_{x,\pm}T^3\sim x^6/[8(1-D)(1-3D)(1-5D)]\), where \(D=v^2/(2\gamma)\).

## Assumptions and scope

Fix \(0<v<1\) and \(\gamma>0\). On the half-line \((0,\infty)\), let \(X_t\) obey the piecewise deterministic equation \(\dot X_t=-1/(1+X_t)+v\sigma_t\), with the sign process \(\sigma_t\in\{-1,+1\}\) changing sign at independent exponential waiting times of rate \(\gamma\), without thermal Brownian noise. Absorb upon first reaching \(0\). Put \(a=v^{-1}-1>0\), start at any \(x>a\), and define \(T=T_{x,\pm}=\inf\{t\ge0:X_t=0\}\) conditional on the starting orientation. The normalization of generator, flips, the potential \(V(x)=\log(1+x)\), and the turning point are physical; in particular \(\gamma\) is the sign-*flip* rate. Moment existence means a finite real expectation, not only a formal solution of a differential equation. The all-order assertion holds for every fixed positive integer \(n\); no uniformity as \(n\to\infty\) is claimed.

## Proof

**1. Backward moment system.** Let \(m_n^\pm(x)=\mathbb E_{x,\pm}T^n\), \(u_n=(m_n^++m_n^-)/2\), \(d_n=(m_n^+-m_n^-)/2\), with \(u_0\equiv1\), \(d_0\equiv0\). In every region where the relevant moments are finite, the stopped-process Dynkin identity or truncated-time resolvent calculation yields
\[
(-s^{-1}\pm v)(m_n^\pm)' +\gamma(m_n^\mp-m_n^\pm)=-n m_{n-1}^\pm,\qquad s=1+x.
\]
Solving for the two derivatives (prime denotes \(d/dx=d/ds\)) gives
\[
\begin{aligned}
d_n'&=\frac{2\gamma s}{v^2s^2-1}d_n
-\frac{n(vu_{n-1}+s^{-1}d_{n-1})}{v^2-s^{-2}},\\
u_n'&=\frac{2\gamma v d_n-n v d_{n-1}-n s^{-1}u_{n-1}}{v^2-s^{-2}}.
\end{aligned}
\]
These identities can be justified first on bounded regions for finite expected moments, then extended by localization. Define \(w(s)=(v^2s^2-1)^{-\beta/2}\) on \(s>1/v\). Since \(w'/w=-2\gamma s/(v^2s^2-1)\),
\[
(wd_n)'=-\frac{n w(s)(vu_{n-1}+s^{-1}d_{n-1})}{v^2-s^{-2}}.
\tag{1}
\]

**2. Positivity, accessibility and an unavoidable scale.** The sign process can equivalently be constructed by resetting to an independently fair orientation at Poisson rate \(2\gamma\): the rate of actual sign changes is then \(\gamma\). Couple two trajectories with opposite starting signs using the same first reset and all subsequent orientations. Before coalescence, the initially positive trajectory remains above the negative trajectory by scalar ODE comparison; after coalescence both follow the same driving sign. Hence \(T_{x,+}\ge T_{x,-}\) under this coupling, and \(0\le d_n\le u_n\) whenever finite. The integrand in (1) is nonnegative on \(s>1/v\), because \(v>s^{-1}\). Starting from any \(x>a\), positive-probability stretches of a positive orientation, preceded by a flip if needed, allow the process to reach any larger level with either designated sign in a bounded time. Consequently, if an order-\(n\) moment is finite at one point/sign, it is finite at all larger points and both signs, by the strong Markov property and the comparison coupling.

For any integer \(j\ge0\) and sufficiently large \(y\),
\[
\mathbb E_{y,\pm}T^j\ge c_j y^{2j},
\tag{2}
\]
where \(c_0=1\). To verify this, stop when the position first reaches \(y/2\). Until then the inward deterministic force has magnitude at most \(2/y\). The integrated telegraph noise has martingale representation \(\int_0^t\sigma_s\,ds=(\sigma_0-\sigma_t+M_t)/(2\gamma)\), with \(\langle M\rangle_t=4\gamma t\). Doob's \(L^2\) inequality at \(t=\epsilon y^2\), for a sufficiently small fixed \(\epsilon>0\), makes the probability of moving by \(y/2\) before that time bounded away from one, uniformly in the initial sign and large \(y\). Thus \(\Pr(T\ge\epsilon y^2)\ge c>0\) and (2) follows.

**3. Sharp necessity.** Suppose an order-\(n\) moment is finite but \(\beta\le2n-1\). When \(n\ge2\) and \(\beta\le2n-3\), the lower-order induction already makes the \((n-1)\)st moment infinite. Otherwise \(u_{n-1}(x)\ge c s^{2n-2}\) by (2), while \(0\le d_{n-1}\le u_{n-1}\). Equation (1) implies \((wd_n)'\le-c's^{2n-2-\beta}\) for large \(s\), because \(w(s)\asymp s^{-\beta}\). Its integral from any fixed large \(s\) to infinity diverges if \(\beta\le2n-1\), contradicting \(wd_n\ge0\). The argument also works for \(n=1\), using \(u_0=1\). Hence no order-\(n\) moment can be finite in that regime, for either orientation and any \(x>a\).

**4. Sharp sufficiency.** Fix \(n\) with \(\beta>2n-1\). For each \(1\le j\le n\), define the positive large-position Lyapunov function
\[
V_j(s,\sigma)=s^{2j}+\frac{jv}{\gamma}\sigma s^{2j-1}.
\]
The exact velocity-jump generator \(\mathcal L=(v\sigma-s^{-1})\partial_s+\gamma(\mathsf{flip}-I)\) satisfies
\[
\mathcal LV_j=2j\left[\frac{(2j-1)v^2}{2\gamma}-1\right]s^{2j-2}
-\frac{jv(2j-1)}{\gamma}\sigma s^{2j-3}.
\tag{3}
\]
The leading term is strictly negative for every \(j\le n\). Choose a sufficiently large \(R\) so that \(V_j\asymp s^{2j}\) and \(\mathcal LV_j\le-c_j s^{2j-2}\) outside \([0,R]\). The stopped Dynkin formula gives \(\mathbb E_{x,\pm}\tau_R\le C s^2\), where \(\tau_R\) is the first entrance into \([0,R]\). Iterating the strong Markov identity
\[
\mathbb E\tau_R^j=j\,\mathbb E\int_0^{\tau_R}\mathbb E_{X_t,\sigma_t}\tau_R^{j-1}\,dt
\]
with (3) yields \(\mathbb E_{x,\pm}\tau_R^j\le C_j s^{2j}\) for all \(j\le n\). Within the compact interval \([0,R]\), a negative orientation persisting for a fixed long enough duration necessarily hits zero; if the initial sign is positive, a flip to negative in a fixed short window and an uninterrupted negative run has a common strictly positive probability. During each bounded trial the position remains in another fixed compact interval. On failure, return from that compact region to \([0,R]\) has uniformly finite moments through order \(n\) by the outside Lyapunov estimates. Geometrically many such uniformly bounded-in-moments trials establish \(\mathbb E_{x,\pm}T^j<\infty\) and \(u_j(s)=O(s^{2j})\) for every \(j\le n\). Localization and monotone convergence justify the moment equations used above.

**5. Exact large-launch coefficients.** Induct on \(n\). For finite moments, equation (1) makes \(wd_n\ge0\) nonincreasing and hence convergent at infinity to some \(\ell_n\ge0\). If \(\ell_n>0\), then \(d_n(s)\ge c s^\beta\); the second equation in Step 1, together with the lower-order moment bound, gives \(u_n'(s)\ge c' s^\beta\) for large \(s\). Its integral contradicts \(u_n=O(s^{2n})\), because \(\beta>2n-1\). Therefore \(\ell_n=0\) and
\[
d_n(s)=\frac{n}{w(s)}\int_s^\infty\frac{w(t)[v u_{n-1}(t)+t^{-1}d_{n-1}(t)]}{v^2-t^{-2}}\,dt.
\tag{4}
\]
The base \(u_0\equiv1\), \(d_0\equiv0\) initiates the induction. Assuming \(u_{n-1}(s)\sim C_{n-1}s^{2n-2}\) and \(d_{n-1}(s)=O(s^{2n-3})\), and using \(w(s)\sim v^{-\beta}s^{-\beta}\), the elementary power-tail integral in (4) yields
\[
d_n(s)\sim\frac{n C_{n-1}}{v[\beta-(2n-1)]}s^{2n-1}.
\]
The second derivative equation now implies \(u_n'(s)\sim (2\gamma/v)d_n(s)\). Integrating gives
\[
u_n(s)\sim \frac{\beta}{2[\beta-(2n-1)]}C_{n-1}s^{2n}=:C_ns^{2n}.
\]
Consequently \(C_n=1/[2^n\prod_{j=1}^n(1-(2j-1)/\beta)]\) and \(m_n^\pm=u_n\pm d_n\) have the asserted common leading coefficient and positive orientation difference \(2d_n\). Replacing \(s=1+x\) by \(x\) leaves these leading powers unchanged. This completes the induction for every fixed integer \(n\ge1\).

## Verification

A standalone Python diagnostic, `check_hierarchy.py`, symbolically checks 34 identities involving the exact generator, the two-moment backward system, and the coefficient recurrence, including orders through eight. It also solves a finite-domain two-orientation upwind difference scheme for \(v=1/2\), \(\gamma=1\), \(\beta=8\) and orders one to three. The exact predicted third-order leading coefficient is \(64/105\). The computed mean/leading-coefficient ratios at launch positions \(20,40,80\) are respectively \(1.50839,1.31091,1.21638\) for the third moment, consistent with slow finite-distance convergence; the orientation-gap ratios are \(1.43348,1.27794,1.19966\). These finite-domain numbers are diagnostic, **not** a proof of limiting or infinite-domain statements. The proof is Steps 1–5 above. Run `python check_hierarchy.py` with Python 3, SymPy, NumPy, and SciPy installed.

## Relationship to prior work

Guéneau, Majumdar and Schehr, arXiv:2409.16951v1 (first posted 2024-09-25), treat the same logarithmic run-and-tumble model, derive the mean first-passage time, and supply general recursive equations for higher moments (Section II.1 and Appendix B) without the complete higher-order finiteness phase diagram or the orientation-difference asymptotic. Their known first-moment threshold and coefficient are recovered here. An earlier mathematical result in the same model (“Sharp second-passage-moment threshold for a run-and-tumble particle in a logarithmic trap”, opaque result identifier `e8413b50-16ce-49db-b2a6-b85eb1f6a2df`) already proves the order-two threshold and leading \(x^4\) coefficient; those are not novel here. Radice, arXiv:2307.12699, derives first-passage functional distributions for an overdamped Brownian, rather than finite-speed telegraph, particle in a logarithmic potential. Its analogous passive-particle power tails do not directly establish the all-order active result or the initial-orientation coefficient. No claim of priority over every unindexed or alternative representation is made.

## Limitations

The theorem concerns the athermal, two-velocity Markov model with constant speed and constant flip rate, the specific logarithmic force, and starts strictly above the turning point. It provides no finite-time probability density, no uniform joint asymptotic in moment order and starting distance, no exact error bound for finite starting distance, and no confidence intervals for empirical measurements. The diffusion approximation may suggest threshold locations but does not by itself prove the finite-speed orientation-difference result. The all-order form follows a published recursion and is therefore exposed to the possibility of an equivalent previously derived but unindexed statement.

## References

1. M. Guéneau, S. N. Majumdar and G. Schehr, “Run-and-tumble particle in one-dimensional potentials: mean first-passage time and applications,” arXiv:2409.16951v1, 2024-09-25. https://arxiv.org/html/2409.16951v1 ; *Physical Review E* **111**, 014144 (2025).
2. M. Radice, “First-passage functionals of Brownian motion in logarithmic potentials and heterogeneous diffusion,” arXiv:2307.12699v2, https://arxiv.org/html/2307.12699v2 ; *Physical Review E* **108**, 044151 (2023).
3. “Sharp second-passage-moment threshold for a run-and-tumble particle in a logarithmic trap,” earlier result identifier `e8413b50-16ce-49db-b2a6-b85eb1f6a2df`, citing arXiv:2409.16951 (prior order-two threshold and coefficient).
