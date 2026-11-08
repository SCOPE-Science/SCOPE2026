# Gaussian stationary fluctuations in rightmost-reset Ornstein–Uhlenbeck groups

## Finding

Fix an integer \(N\geq2\), a harmonic confinement coefficient \(k>0\), and a diffusivity \(D>0\). Between independent Poisson events of rate \(r>0\), \(N\) particles follow independent processes \(dX_i=-kX_i\,dt+\sqrt{2D}\,dW_i\) on the **whole real line**. At every event, all coordinates are instantaneously replaced by their rightmost coordinate. No absorbing boundary is imposed.

Let \(M_N=\max\{Z_1,\ldots,Z_N\}\) for independent standard normal \(Z_i\), and put \(\mu_N=\mathbb E M_N\) and \(\nu_N=\mathbb E M_N^2\). At the stationary reset epochs let \(R_r\) be the common post-reset coordinate. Set
\[
c_N=\frac{\mu_N}{k}\sqrt{\frac{\pi D}{2}},\qquad
V_N=\frac{D}{k}\left(\nu_N-\frac{\pi}{4}\mu_N^2\right)>0.
\]
Then, as \(r\to\infty\) with \(N,k,D\) fixed,
\[
R_r-c_N\sqrt r\ \Longrightarrow\ \mathcal N(0,V_N),\qquad
\operatorname{Var}(R_r)\longrightarrow V_N,
\qquad \mathbb E R_r-c_N\sqrt r\longrightarrow0.
\]
The same centered weak limit holds jointly for the \(N\) stationary particle coordinates observed at an ordinary time:
\[
(X_1-c_N\sqrt r,\ldots,X_N-c_N\sqrt r)
\ \Longrightarrow\ (G,\ldots,G),\qquad G\sim\mathcal N(0,V_N).
\]
Thus the leading group fluctuations are perfectly shared. For any fixed \(p\in(0,1)\), the \(p\)-quantile of the stationary reset location is \(c_N\sqrt r+\sqrt{V_N}\,\Phi^{-1}(p)+o(1)\), where \(\Phi\) is the standard-normal distribution function.

For \(N=2\) the formulas simplify exactly to
\[
c_2=\frac{\sqrt{D/2}}{k},\qquad V_2=\frac{3D}{4k}.
\]
The variance splits into a maximum-fluctuation part and a Poisson-clock part:
\[
V_N=\frac Dk\left[\operatorname{Var}(M_N)+\left(1-\frac\pi4\right)\mu_N^2\right].
\]
The second positive term is missed if the random duration of each excursion is replaced by its mean.

## Assumptions and scope

The particle number \(N\ge2\) is a **fixed finite integer**, not a simultaneous growing-particle limit. All reset event times form one exogenous homogeneous Poisson process, independent of all Brownian motions. At a reset, the largest current coordinate is selected, and **all** particles are relocated there. Harmonic drift acts about the fixed origin. The absence of absorption is essential: this is the stationary reference system associated with the extreme-value group-resetting protocol, not a theorem on first-passage times with killing.

The stationary reset-location law is the invariant distribution of the embedded reset-epoch chain; a stationary ordinary-time configuration is defined by a two-sided stationary Poisson construction. Normalization uses the Ornstein–Uhlenbeck noise convention \(\sqrt{2D}\), so the unreset equilibrium variance is \(D/k\).

The constants can be evaluated without a large-\(N\) Gumbel approximation:
\[
\mu_N=N\!\int_{-\infty}^{\infty} z\phi(z)\Phi(z)^{N-1}\,dz,
\quad \nu_N=N\!\int_{-\infty}^{\infty} z^2\phi(z)\Phi(z)^{N-1}\,dz,
\]
where \(\phi\) and \(\Phi\) are the standard-normal density and distribution function.

## Proof

**1. Exact embedded kernel and invariant law.** Let \(E_j\) be independent unit-rate exponential variables, and let \(M_j\) be independent copies of \(M_N\), also independent of the \(E_j\). The interval from one reset to the next is \(E_j/r\). Conditional on common initial coordinate \(x\), each Ornstein–Uhlenbeck endpoint equals \(e^{-kE_j/r}x+\sqrt{(D/k)(1-e^{-2kE_j/r})}\,Z_{j,i}\); the rightmost endpoint gives the **exact** random affine recurrence
\[
R_{j+1}=A_{j,r}R_j+B_{j,r},\quad
A_{j,r}=e^{-kE_j/r},\quad
B_{j,r}=\sqrt{\frac Dk(1-A_{j,r}^2)}\,M_j.
\]
Here \(0<A_{j,r}<1\), \(\mathbb E\log A_{j,r}=-k/r<0\), and \(\mathbb E\log^+|B_{j,r}|<\infty\). The backwards perpetuity \(\sum_{j\ge1}(\prod_{i<j}A_{i,r})B_{j,r}\) therefore converges almost surely, giving the unique stationary distribution, with finite moments of all orders needed below.

**2. Exact mean and centered variance.** Write \(z=r/(2k)\). Since \(U=e^{-2kE/r}\) has density \(z u^{z-1}\) on \((0,1)\), beta integration gives
\[
\begin{aligned}
a_1&=\mathbb E A=\frac r{r+k},&
a_2&=\mathbb E A^2=\frac r{r+2k},\\
b&=\mathbb E B=\mu_N\sqrt{\frac Dk}\,zB(z,3/2),&
q&=\mathbb E(AB)=\mu_N\sqrt{\frac Dk}\,zB(z+1/2,3/2),\\
\mathbb E B^2&=\frac Dk\nu_N(1-a_2).&&
\end{aligned}
\]
The beta function is \(B(a,b)=\Gamma(a)\Gamma(b)/\Gamma(a+b)\). Let \(m_r=\mathbb E R_r\) and \(v_r=\operatorname{Var}(R_r)\). Stationarity of the recurrence gives **finite-rate identities**
\[
m_r=\frac b{1-a_1}=\mu_N\sqrt{\frac Dk}\,zB(z,1/2),
\]
\[
v_r=\frac{\frac Dk\nu_N(1-a_2)-2m_r(b-q)+m_r^2(1-2a_1+a_2)}{1-a_2}.
\]
The centered recurrence is \(R_{j+1}-m_r=A_{j,r}(R_j-m_r)+\zeta_{j,r}\), where \(\zeta_{j,r}=B_{j,r}-(1-A_{j,r})m_r\) is mean zero. The variance identity follows by squaring and using the independence of the current innovation from the preceding stationary coordinate.

The gamma-ratio expansion \(\Gamma(z)/\Gamma(z+1/2)=z^{-1/2}[1+(8z)^{-1}+O(z^{-2})]\) yields
\[
m_r=c_N\sqrt r+O(r^{-1/2}).
\]
Let \(Y_{j,r}=\sqrt r\,\zeta_{j,r}\). For each fixed \(j\), as \(r\to\infty\),
\[
Y_{j,r}\ \longrightarrow\ H_j:=\sqrt{2DE_j}\,M_j-kc_NE_j
\quad\text{in }L^2,
\]
and the fourth moments of \(Y_{j,r}\) are uniformly bounded for \(r\) sufficiently large. Indeed \(r(1-e^{-kE/r})\le kE\), \(\sqrt{r(1-e^{-2kE/r})}\le\sqrt{2kE}\), and \(m_r/\sqrt r\) remains bounded. Using \(\mathbb E E=1\), \(\mathbb E E^{3/2}=3\sqrt\pi/4\), and \(\mathbb E E^2=2\), one obtains
\[
\mathbb E H_j=0,\qquad
\sigma_N^2:=\mathbb E H_j^2=2D\left(\nu_N-\frac\pi4\mu_N^2\right).
\]
This variance includes the correlation between each Gaussian maximum and the random excursion duration.

**3. Gaussian triangular-array limit.** With independent pairs \((A_{j,r},Y_{j,r})\), the stationary centered perpetuity has the representation
\[
R_r-m_r\ \stackrel d=\ \frac1{\sqrt r}\sum_{j\ge1}
\left(\prod_{i<j} A_{i,r}\right)Y_{j,r}.
\]
The summands are martingale differences in the increasing reset-index filtration: the preceding product is predictable and \(\mathbb EY_{j,r}=0\). For each fixed \(T>0\), the maximal law-of-large-numbers deviation \(\sup_{j\le rT}|r^{-1}\sum_{i<j}E_i-j/r|\to0\) in probability. Thus their predictable quadratic variation truncated at \(j\le rT\) converges to
\[
\frac1r\sum_{j\le rT}\left(\prod_{i<j}A_{i,r}^2\right)\mathbb EY_{j,r}^2
\ \longrightarrow\ \sigma_N^2\int_0^T e^{-2ks}\,ds.
\]
The bounded fourth moments yield the conditional Lindeberg condition (the sum of fourth moments of the scaled, predictable-weighted increments is \(O(1/r)\)). The martingale-array central limit theorem proves a centered normal limit for the truncated sum. Its omitted tail has second moment at most
\[
\frac{\mathbb EY_{1,r}^2}{r}
\frac{a_2^{\lfloor rT\rfloor}}{1-a_2}
\ \longrightarrow\ \frac{\sigma_N^2}{2k}e^{-2kT}.
\]
Taking \(T\to\infty\) gives \(R_r-m_r\Rightarrow\mathcal N(0,\sigma_N^2/(2k))\). Since \(m_r-c_N\sqrt r\to0\), this is the asserted law, with \(V_N=\sigma_N^2/(2k)\). The exact centered variance identity, or convergence of the displayed predictable quadratic variation, also gives \(v_r\to V_N\).

**4. Stationary ordinary-time particles.** At an ordinary stationary observation time the age \(F_r\) since the last reset has the exponential law of rate \(r\), independently of the last reset coordinate \(R_r\) and of the subsequent Brownian increments. Conditional on \(F_r\),
\[
X_i=e^{-kF_r}R_r+\sqrt{\frac Dk(1-e^{-2kF_r})}\,Z_i.
\]
As \(F_r=O_{\mathbb P}(r^{-1})\) and \(R_r=O_{\mathbb P}(\sqrt r)\), each \(X_i-R_r=O_{\mathbb P}(r^{-1/2})\). Joint Slutsky convergence gives the diagonal Gaussian law. Strict positivity of \(V_N\) follows from \(\operatorname{Var}(M_N)>0\) and \(1-\pi/4>0\). Convergence of fixed quantiles follows from continuity and strict monotonicity of the limiting Gaussian distribution.

## Verification

The file `verify_group_reset.py` checks exact Gaussian-maximum moments, positivity and beta-function identities at multiple reset rates, convergence of the exact mean and variance, and seeded direct simulation using the **exact interval transition**, not an Euler approximation. It passed 52 tests (\(N=2,3,5\) for quadrature/moment checks and \(N=2\) for simulation). With \(D=1.7\), \(k=0.9\), \(N=2\), and \(r=250\), the seeded simulation gave sample mean \(16.2272927\) versus exact \(16.2116725\), and sample variance \(1.3863857\) versus exact \(1.4162424\); the limiting variance is \(1.4166667\). These numerical tests are finite diagnostics only. The Gaussian limit is established by the analytical martingale argument.

## Relationship to prior work

Lee, Yang, Park and Lizana [1] formulate rightmost-particle group resetting, develop a renewal equation and calculate stationary mean and squared coefficient of variation using a large-group Gumbel approximation. In their notation the ordinary-time mean follows from our exact reset-epoch mean by multiplication with \(r/(r+k)\), followed by their large-\(N\) approximation. Their general renewal kernel is a starting point, not an already evaluated fixed-\(N\) high-frequency Gaussian law or its explicit Poisson-clock variance.

Lee, Yang and Lizana [2] study group first-passage distributions with an absorbing boundary; the present statement is restricted to their unabsorbed stationary reference dynamics. Galla [3] gives a diffusion approximation for frequent small **proportional** random resets; its displacement order and reset map differ from the rightmost-selection rule, whose typical jumps scale as \(r^{-1/2}\) rather than \(r^{-1}\). Majumdar, Sabhapandit and Schehr [4] study a single lattice walker resetting to its **historical** maximum, not a simultaneously reset finite Gaussian group in a harmonic trap. Biroli, Larralde, Majumdar and Schehr [5] study independent Brownian walkers simultaneously reset to a **fixed origin**. These comparisons distinguish the stated coefficient and diagonal central limit from prior spectral, extreme-value and generic resetting results.

## Limitations

Only fixed finite \(N\) and \(k,D>0\) are proved. No uniform growing-\(N\) limit, first-passage asymptotic, rare-event probability at a fixed boundary, quantitative convergence rate, non-Poisson clock extension or anharmonic trap is claimed. A Gaussian central limit does not determine the exponentially small stationary probability of reaching a fixed origin when the center grows as \(\sqrt r\). The proof uses standard martingale central limit theory; prior abstract probability results imply the limit when the specific embedded recursion and its variance are supplied. Publication-priority uncertainty remains about unindexed earlier analyses of precisely this high-frequency rightmost-reset model.

## References

[1] J. Lee, S.-G. Yang, H. J. Park and L. Lizana, *General Theory for Group Resetting with Application to Avoidance*, arXiv:2412.02524, version 3 (2026), https://arxiv.org/html/2412.02524v3.

[2] J. Lee, S.-G. Yang and L. Lizana, *Beyond average: heterogeneous first-passage dynamics in many-particle systems with resetting*, arXiv:2604.24406, first public 2026-04-27, https://arxiv.org/html/2604.24406v2.

[3] T. Galla, *A diffusion approximation for systems with frequent weak resetting*, arXiv:2602.21635v1 (2026), https://arxiv.org/html/2602.21635.

[4] S. N. Majumdar, S. Sabhapandit and G. Schehr, *Random walk with random resetting to the maximum*, arXiv:1509.04516 (2015), https://arxiv.org/abs/1509.04516.

[5] M. Biroli, H. Larralde, S. N. Majumdar and G. Schehr, *Extreme Statistics and Spacing Distribution in a Brownian Gas Correlated by Resetting*, arXiv:2211.00563 (2022), https://arxiv.org/abs/2211.00563.
