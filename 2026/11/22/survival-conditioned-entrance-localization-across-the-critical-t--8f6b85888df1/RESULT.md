# Survival-conditioned entrance localization across the critical tail boundary

## Finding
Consider the continuous-time nearest-neighbor random walk \((X_t)_{t\ge0}\) on \(\{0,1,2,\ldots\}\), absorbed at \(0\), with upward transition rate \(b\) and downward transition rate \(a\), where \(a>b>0\). Let \(T\) be its absorption time, and set
\[
\rho=\sqrt{b/a}\in(0,1),\qquad d=2\sqrt{ab},\qquad \lambda=a+b-d.
\]
For a fixed \(\beta>0\), draw the initial position \(X_0=I\) from
\[
\Pr(I=i)=C_\beta\rho^i i^{-\beta},\qquad
C_\beta=\left(\sum_{k\ge1}\rho^k k^{-\beta}\right)^{-1},\qquad i\ge1.
\]
Write \(J_t=X_t\) on the survival event \(\{T>t\}\). The conditional *entrance* location exhibits three regimes, while the conditional *terminal* location has the same limit in all regimes. Jointly with the terminal location, the respective limits are **independent**:

1. If \(0<\beta<2\), then
\[
\left(\frac{I}{\sqrt{t}},J_t\right)\ \bigg|\ \{T>t\}
\quad\Longrightarrow\quad (Y_\beta,J),
\qquad \Pr(J=j)=(1-\rho)^2j\rho^{j-1}.
\]
Here \(J\) is independent of \(Y_\beta\), whose density on \((0,\infty)\) is
\[
 f_\beta(y)=\frac{y^{1-\beta}e^{-y^2/(2d)}}{2^{-\beta/2}d^{1-\beta/2}\Gamma(1-\beta/2)}.
\]
Equivalently, \(Y_\beta^2/(2d)\) has a gamma law of shape \(1-\beta/2\) and rate \(1\).

2. At the exact boundary \(\beta=2\),
\[
\left(\frac{2\log I}{\log t},J_t\right)\ \bigg|\ \{T>t\}
\quad\Longrightarrow\quad (U,J),\qquad U\sim\operatorname{Uniform}[0,1],
\]
with \(U\) and \(J\) independent. In particular, the survivor's entrance state occupies **every logarithmic scale from constant to diffusive** with asymptotically equal weight; no deterministic power of \(t\) captures its entrance location.

3. If \(\beta>2\), the entrance stays at finite lattice distance:
\[
(I,J_t)\ \big|\ \{T>t\}\quad\Longrightarrow\quad (I_\infty,J),
\qquad\Pr(I_\infty=i)=\frac{i^{1-\beta}}{\zeta(\beta-1)},
\]
again with independent components. Convergence is in total variation on the discrete product space in this third regime.

The first two joint limits are weak convergence in \([0,\infty)\times\mathbb N\) and \([0,\infty)\times\mathbb N\), respectively (where \(\mathbb N\) has the discrete topology). In each regime the limiting terminal law \(J\) is the minimal quasi-stationary law. This theorem concerns the joint *initial/terminal* law, not a path-space limit.

## Assumptions and scope
All parameters \(a>b>0\) and \(\beta>0\) are fixed as \(t\to\infty\). The conditioning event \(\{T>t\}\) has positive probability. Rates, the initial distribution, the gamma parametrization and the topology of convergence are as above. No time-dependent \(\beta\), moving rates, or unbounded terminal-state observables are claimed. The statement covers the entire family \(m_i\propto\rho^i i^{-\beta}\), not arbitrary distributions with the same ratio asymptotics.

## Proof
**1. Exact positive heat-kernel representation.** The killed transition kernel is the classical Bessel formula (see [1]):
\[
 p_{ij}(t)=e^{-(a+b)t}\rho^{j-i}\big[I_{i-j}(dt)-I_{i+j}(dt)\big],\qquad i,j\ge1.
\]
Define \(H_t(k)=e^{-dt}I_{|k|}(dt)\) and \(B_t(i,j)=H_t(i-j)-H_t(i+j)\ge0\). Thus the *joint, unnormalized* mass is exactly
\[
\Pr(I=i,X_t=j,T>t)=C_\beta e^{-\lambda t}\rho^j i^{-\beta}B_t(i,j).\tag{1}
\]
This is the central normalization: both powers of \(\rho\) depending on \(i\) cancel.

**2. Three elementary uniform kernel estimates.** For \(i,j\ge1\), the reflection formula is
\[
B_t(i,j)=\frac2\pi\int_0^\pi e^{-dt(1-\cos v)}\sin(iv)\sin(jv)\,dv.\tag{2}
\]
Let \(A_d=2/(\sqrt{2\pi}d^{3/2})\). Changing variables \(v=u/\sqrt t\) in (2), using Gaussian domination, and evaluating \(\int_0^\infty ue^{-du^2/2}\sin(yu)\,du\), gives, for any fixed \(0<\varepsilon<R<\infty\) and \(L<\infty\), uniformly over \(\varepsilon\sqrt t\le i\le R\sqrt t\), \(1\le j\le L\log t\),
\[
\frac{t B_t(i,j)}{j}-A_d\frac{i}{\sqrt t}e^{-i^2/(2dt)}\longrightarrow0.\tag{3}
\]
The same integral, factoring \(\sin(iv)/(iv)\) and \(\sin(jv)/(jv)\), yields for any fixed \(0<\delta<1/2\), uniformly over \(1\le i\le t^{1/2-\delta}\) and \(1\le j\le L\log t\),
\[
\frac{t^{3/2}B_t(i,j)}{ij}\longrightarrow A_d.\tag{4}
\]
Indeed \(|\sin(kv)|\le k\sin v\le kv\) on \([0,\pi]\), so after rescaling the integrands are bounded by an integrable multiple of \(u^2e^{-c_0u^2}\) for small \(v\); the complementary arc is exponentially suppressed. The same inequality also gives the **global** estimate
\[
0\le B_t(i,j)\le C_d ij t^{-3/2},\qquad t\ge1.\tag{5}
\]
For large \(i\), use \(I_{k-1}(z)-I_{k+1}(z)=2kI_k(z)/z\). When \(i\ge2j\), telescoping the \(j\) terms and using monotonicity of \(I_k(z)\) in nonnegative integer \(k\) gives
\[
 B_t(i,j)\le \frac{2j(i+j)}{dt}H_t(i-j+1).
\]
The exponential tilt in the Fourier integral for \(H_t\) gives, for fixed \(d>0\),
\[
 H_t(k)\le C_d t^{-1/2}\exp[-c_d\min(k^2/t,k)]\qquad(k\ge0,t\ge1).
\]
For completeness, introduce a tilt \(h=\min\{k/(2dt),1\}\) in the Fourier coefficient of \(\exp(dt\cos v)\). Taking absolute values leaves a Gaussian angular integral of order \((dt\cosh h)^{-1/2}\) times \(\exp[-hk+dt(\cosh h-1)]\), bounded above by the displayed two-scale exponential; the range of bounded \(t\) is absorbed into constants. Therefore for \(i\ge2j\),
\[
 B_t(i,j)\le C_d ji t^{-3/2}\exp[-c_d\min(i^2/t,i)].\tag{6}
\]
All constants here depend only on \(d\) (and, if necessary, a lower bound on \(t\)), not on \(i,j,t\). These estimates are consequences of the explicit heat kernel, not assumptions.

**3. Weighted mass asymptotics for \(0<\beta<2\).** Combining (3) with a Riemann sum over \(i/\sqrt t\) in \([\varepsilon,R]\), for \(1\le j\le L\log t\), yields
\[
 \frac{t^{(\beta+1)/2}}{j}\sum_{i\ge1}i^{-\beta}B_t(i,j)
 \longrightarrow A_d\int_0^\infty y^{1-\beta}e^{-y^2/(2d)}dy=:k_\beta.\tag{7}
\]
This convergence is uniform in the specified range of \(j\). The neglected range \(i<\varepsilon\sqrt t\) is bounded using (5), after scaling, by \(O(\varepsilon^{2-\beta})\); the range \(i>R\sqrt t\) is bounded via (6) by an integrable exponentially decaying tail. The integral is finite precisely for \(\beta<2\), with
\[
 k_\beta=\frac{2^{1-\beta/2}\Gamma(1-\beta/2)}{\sqrt{2\pi}\,d^{(\beta+1)/2}}.
\]
The identical Riemann-sum argument restricted to \(i/\sqrt t\in E\), for continuity sets \(E\subset(0,\infty)\), identifies the joint entrance density proportional to \(y^{1-\beta}e^{-y^2/(2d)}\), and the \(j\)-weight \(j\rho^j\) factors out.

**4. The logarithmic critical boundary.** For \(\beta=2\), (4) implies, uniformly for \(1\le j\le L\log t\) and every fixed \(\delta\in(0,1/2)\),
\[
 \sum_{1\le i\le t^{1/2-\delta}}i^{-2}B_t(i,j)
 =A_d j t^{-3/2}\big[(1/2-\delta)\log t+o(\log t)\big].\tag{8}
\]
On \(t^{1/2-\delta}<i\le\sqrt t\), (5) bounds the sum by \(O(\delta j t^{-3/2}\log t)\). On \(i>\sqrt t\), (6) gives \(O(jt^{-3/2})\) once \(j\le L\log t\). Letting \(\delta\downarrow0\) proves
\[
 \sum_{i\ge1}i^{-2}B_t(i,j)
 \sim\frac{A_d}{2}j t^{-3/2}\log t.\tag{9}
\]
For any \(u\in(0,1/2)\), (4) also gives
\[
\sum_{i\le t^u}i^{-2}B_t(i,j)
 \sim A_d u j t^{-3/2}\log t.\tag{10}
\]
Dividing (10) by (9) shows \(\Pr(2\log I/\log t\le v\mid X_t=j,T>t)\to v\) for \(v\in(0,1)\), uniformly over each fixed finite set of \(j\). The extremes \(v\le0\) and \(v\ge1\) follow from the same bounds.

**5. Endpoint tightness and asymptotic independence.** When \(\beta>0\), the convolution form (1) and \(i^{-\beta}\le1\) give
\[
 \Pr(X_t=j,T>t)\le C_\beta e^{-\lambda t}\rho^j\sum_{i\ge1}H_t(i-j)
 \le C_\beta e^{-\lambda t}\rho^j.\tag{11}
\]
Choose \(L\) so that \(\sum_{j>L\log t}\rho^j=o(t^{-3/2})\). Therefore the terminal tail is negligible even compared with the slowest of the three survival scales. For \(j\le L\log t\), (7) and (9) imply the unnormalized \(j\)-marginal has a uniform equivalent proportional to \(j\rho^j\). Summing it gives the common limiting distribution
\[
\Pr(J=j)=\frac{j\rho^j}{\sum_{k\ge1}k\rho^k}
 =(1-\rho)^2j\rho^{j-1}.\tag{12}
\]
The restricted sums in Steps 3 and 4 factor into a scale-dependent entrance integral and the same \(j\rho^j\) weight. Since (11) makes the terminal index tight, this factorization proves **joint weak convergence to the product law**, not merely separate marginal convergence.

**6. Finite entrance for \(\beta>2\).** From (2), for each fixed \(i,j\),
\[
 t^{3/2}B_t(i,j)\longrightarrow A_d ij.
\]
By (5), \(i^{-\beta}B_t(i,j)t^{3/2}\le C_d i^{1-\beta}j\), summable over \(i,j\) after multiplying by \(\rho^j\) exactly when \(\beta>2\). Dominated convergence directly in the two-dimensional counting measure proves convergence in \(\ell^1\) of the scaled joint mass to a multiple of \(i^{1-\beta}j\rho^j\). Renormalization gives the claimed independent laws of \(I_\infty\) and \(J\), with \(I_\infty\) normalized by \(\zeta(\beta-1)\).

This completes the proof. The argument yields the three entrance laws directly from the exact joint kernel; it does not infer entrance distributions from terminal marginals.

## Verification
The bundled standalone `checker.py` performs 3,622 exact-rational and numerical assertions. These test the Bessel reflection formula against the Taylor coefficients of a killed continuous-time random-walk generator, the telescoping Bessel recurrence, the normalized quasi-stationary weights, and special-case leading constants. It uses Python standard-library modules only and is run with `python checker.py`. The optional `numerical_check.py` uses NumPy and SciPy to compare conditional entrance probabilities at increasing finite times against all three predicted limits. Finite checks corroborate algebra and normalization but **do not prove asymptotic convergence**. The analytic proof above, including uniform estimates and tightness, bears that burden.

For the transparent parameter choice \(a=2\), \(b=1/2\), \(d=2\), \(\rho=1/2\), the case \(\beta=1\) has \(Y_1\stackrel d=|N(0,2)|\); the case \(\beta=2\) has the logarithmic-uniform entrance law; and for \(\beta=3\), \(\Pr(I_\infty=1)=6/\pi^2\). These are straightforward numerical test targets.

## Relationship to prior work
Pollett [1] proves quasi-stationary attraction for supercritical geometric tail ratios, including exact survival and terminal-state equivalents, and gives a finite moment criterion for minimal-QSD attraction. His Remark 4.2 discusses polynomial corrections at the critical tail ratio, without establishing a conditional law for the **initial state given eventual survival**. Earlier research on this absorbed walk also derives marginal critical-tail survival equivalents, but those do not determine the location of the initial state under survival conditioning. The new content here is a joint entrance/terminal localization theorem with three regimes and independence, including a critical log-uniform entrance law.

Van Doorn [2] establishes the classical QSD structure and fixed/finite-support quasi-limits, rather than a conditional entrance-distribution phase transition for these infinite-support initial laws. Lee and Ben-Ari [3] study analogous drifted-Brownian quasi-limits; their abstract indicates different continuous-state models and domains of attraction. That analogy is a genuine historical-priority risk, not a claim of complete noncoverage from abstract evidence. General positive-kernel ratio-limit and random-walk local limit technology can overlap with the proof mechanism; novelty is asserted only for the precise joint conditioned entrance law.

## Limitations
The theorem requires the exactly specified polynomially tilted critical-geometric initial distribution. It does not give a necessary-and-sufficient domain-of-attraction criterion, a universal law for arbitrary slowly varying factors, a full conditioned-path limit, quantitative error rates, or independent validation. The conditional entrance law for \(\beta=2\) concerns weak logarithmic scaling; it makes no claim of total variation convergence to a continuous law. Historical priority remains open for older drifted Brownian and general ratio-limit literature. Independent mathematical review has not been performed.

## References
1. Phil. Pollett, *Domains of attraction of quasi-stationary distributions for an absorbed random walk*, arXiv:2611.17791v1, first submitted 2026-11-13, https://arxiv.org/html/2611.17791v1 (Sections 2–4, especially Theorem 3.1 and Remark 4.2).
2. Erik A. van Doorn, *Quasi-stationary distributions and convergence to quasi-stationarity of birth–death processes*, Advances in Applied Probability 23 (1991), 683–700, DOI:10.1017/S0001867800023880, https://zhanghanjun.weebly.com/uploads/9/5/0/0/9500832/quasi-stationary_distributions_and_convergence_to_quasi-stationarity_of_birth-death_processes_.pdf .
3. SangJoon Lee and Iddo Ben-Ari, *Quasi-Limiting Behavior of Drifted Brownian Motion*, arXiv:2001.04523 (2020), https://arxiv.org/abs/2001.04523 .
