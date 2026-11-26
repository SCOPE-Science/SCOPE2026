# An Ornstein–Uhlenbeck critical window for a two-colour mixed urn

## Finding

**Theorem (logarithmic critical window).** Fix any real \(\tau\). For each integer \(N\) large enough that
\[
0<p_N=\frac13+\frac{2\tau}{3\log N}<1,
\]
run a *separate* two-colour urn for \(N\) draws. Start with two balls of each colour. At every draw, independently choose the Friedman rule with probability \(p_N\), adding one ball of the drawn colour and three of the opposite colour, or choose the Pólya rule with probability \(1-p_N\), adding four of the drawn colour. The drawn ball is returned. These probabilities are fixed *within each row* of \(N\) draws.

Write \(Y^{(N),i}_k\) for the number of balls of colour \(i\) after \(k\) draws, \(U^{(N)}_k=Y^{(N),1}_k-Y^{(N),2}_k\), and \(Z^{(N)}_k=Y^{(N),1}_k/[4(k+1)]\). Define the cadlag process
\[
X_N(t)=\frac{U^{(N)}_{\lfloor N^t\rfloor}}{\sqrt{\lfloor N^t\rfloor\log N}},\qquad 0\le t\le1.
\]
As \(N\to\infty\), in the Skorokhod \(J_1\) topology on \(D([0,1])\),
\[
X_N\Rightarrow X_\tau,\qquad X_\tau(t)=\sqrt{12}\,e^{-\tau t}\int_0^t e^{\tau s}\,dB_s,
\]
where \(B\) is standard Brownian motion. Equivalently, \(X_\tau\) is the unique zero-initial continuous solution of
\[
dX_\tau(t)=-\tau X_\tau(t)\,dt+\sqrt{12}\,dB_t.
\]
For \(0\le s,t\le1\), its covariance is
\[
\operatorname{Cov}(X_\tau(s),X_\tau(t))
=12e^{-\tau(s+t)}\int_0^{\min(s,t)}e^{2\tau u}\,du.
\]
In addition, the second moments converge, with the continuous extension \(F(0)=1\) of \(F(\tau)=(1-e^{-2\tau})/(2\tau)\):
\[
\lim_{N\to\infty}\frac{\mathbb E[(U^{(N)}_N)^2]}{N\log N}
=12F(\tau),\qquad
\lim_{N\to\infty}\frac{N}{\log N}\mathbb E[(Z^{(N)}_N-\tfrac12)^2]
=\frac3{16}F(\tau).
\]
In the exactly critical row \(\tau=0\), the finite-size identity is
\[
\mathbb E[(U^{(N)}_k)^2]=12(k+1)(H_{k+1}-1),
\qquad H_m=\sum_{j=1}^{m}\frac1j,\quad 0\le k\le N.
\]

## Assumptions and scope

The claim holds for each *fixed* \(\tau\in\mathbb R\), as \(N\to\infty\); it does not assert a bound uniform over unbounded \(\tau\) or a fixed-parameter central limit theorem outside the logarithmic critical window. Draws and replacement-rule choices are independent conditional on the past in the manner specified above; the two colours' initial masses are deterministic and equal to two. Every update adds four balls, so \(Y^{(N),1}_k+Y^{(N),2}_k=4(k+1)\). The laws for different values of \(N\) need not be coupled. The endpoint \(t=0\) refers to one draw, rather than the initial urn.

## Proof

**1. Exact one-step decomposition.** Suppress the row superscript \(N\) temporarily and let \(\mathcal F_j\) contain the first \(j\) draws and rule choices. For \(j\ge1\), let \(S_j\in\{-1,1\}\) be the sign of the colour drawn at step \(j\) and let \(R_j\in\{-2,4\}\) be the signed reinforcement factor, independent of that draw, with \(\Pr(R_j=-2)=p_N\). Then
\[
U_j=U_{j-1}+R_jS_j,\quad
\mathbb E[S_j\mid\mathcal F_{j-1}]=\frac{U_{j-1}}{4j},
\]
and the exact constants are
\[
\alpha_N=\frac{\mathbb ER_j}{4}=1-\frac{3p_N}{2}
=\frac12-\frac{\tau}{\log N},\qquad
v_N=\mathbb E R_j^2=16-12p_N=12-\frac{8\tau}{\log N}.
\]
Set
\[
\xi_{N,j}=R_jS_j-\frac{\alpha_N}{j}U_{j-1}.
\]
These are martingale differences with conditional second moments
\[
\mathbb E[\xi_{N,j}^2\mid\mathcal F_{j-1}]
=v_N-\alpha_N^2\frac{U_{j-1}^2}{j^2}.
\]
Since \(|U_{j-1}|\le4j\) and \(|R_j|\le4\), the \(\xi_{N,j}\) are bounded by a deterministic constant for all sufficiently large \(N\).

**2. Martingale normalization and second-moment bound.** Define
\[
A_{N,0}=1,\qquad A_{N,k}=\prod_{j=1}^k\left(1+\frac{\alpha_N}{j}\right),\qquad
M_{N,k}=\sum_{j=1}^k\frac{\xi_{N,j}}{A_{N,j}}.
\]
The recursion \(U_j=(1+\alpha_N/j)U_{j-1}+\xi_{N,j}\), together with \(U_0=0\), gives \(U_k=A_{N,k}M_{N,k}\). For each fixed \(\tau\), \(\alpha_N\to1/2\), and the gamma-product identity yields, uniformly for sufficiently large \(N\) and \(k\ge1\),
\[
A_{N,k}=\frac{\Gamma(k+1+\alpha_N)}{\Gamma(k+1)\Gamma(1+\alpha_N)}
=\frac{k^{\alpha_N}}{\Gamma(1+\alpha_N)}\big(1+O_\tau(k^{-1})\big).
\]
Let \(m_{N,k}=\mathbb E U_k^2\). Conditional expansion, with \(\mathbb EU_k=0\), gives the *exact* scalar recurrence
\[
m_{N,0}=0,\qquad
m_{N,k}=\left(1+\frac{2\alpha_N}{k}\right)m_{N,k-1}+v_N.
\]
Writing its solution as a sum of products, and using \(k^{|2\tau|/\log N}\le e^{2|\tau|}\) for \(k\le N\), gives
\[
m_{N,k}\le C_\tau\,k(1+\log k),\qquad 1\le k\le N.
\]
The implied constant is independent of \(N,k\) for fixed \(\tau\).

**3. Martingale functional limit.** For \(0\le t\le1\), consider \(Q_N(t)=M_{N,\lfloor N^t\rfloor}/\sqrt{\log N}\). Its predictable quadratic variation has expectation-correction term bounded by
\[
\frac{C_\tau}{\log N}\sum_{j=1}^N
\frac{\mathbb E U_{j-1}^2}{j^2 A_{N,j}^2}
\le\frac{C_\tau}{\log N}\sum_{j=2}^{\infty}
\frac{1+\log j}{j^{1+\delta}}\longrightarrow0
\]
for some fixed \(\delta>0\), as all sufficiently large \(N\) have \(\alpha_N\ge\delta/2\). The positive correction is therefore negligible in probability, uniformly in \(t\). On the other hand, the uniform gamma-product expansion and a harmonic Riemann sum show that
\[
\sup_{0\le t\le1}\left|
\frac{v_N}{\log N}\sum_{j\le N^t}A_{N,j}^{-2}
-12\Gamma(3/2)^2\int_0^t e^{2\tau u}\,du\right|\longrightarrow0.
\]
Indeed, \(j^{-2\alpha_N}=j^{-1}\exp(2\tau\log j/\log N)\), and errors from replacing the gamma product by its asymptotic sum to \(O_\tau(1)\) before division by \(\log N\). Since \(A_{N,j}\ge1\) for sufficiently large \(N\), each jump of \(Q_N\) is bounded by \(C_\tau/\sqrt{\log N}\); the martingale Lindeberg condition follows. The martingale functional central limit theorem thus gives
\[
Q_N\Rightarrow\sqrt{12}\,\Gamma(3/2)
\int_0^{\cdot}e^{\tau s}\,dB_s
\quad\text{in }D([0,1]).
\]

**4. Recover the urn and control the left endpoint.** For any fixed \(\varepsilon>0\), uniformly over \(\varepsilon\le t\le1\),
\[
\frac{A_{N,\lfloor N^t\rfloor}}{\sqrt{\lfloor N^t\rfloor}}
\longrightarrow\frac{e^{-\tau t}}{\Gamma(3/2)}.
\]
Multiplication gives the claimed Ornstein–Uhlenbeck process on \([\varepsilon,1]\). For \(0\le t\le\varepsilon\), the prefactor is uniformly bounded by \(C_\tau\); Doob's \(L^2\) inequality and the same bracket sum give
\[
\mathbb E\sup_{0\le t\le\varepsilon}|X_N(t)|^2
\le C_\tau\frac{1}{\log N}
\sum_{j\le N^\varepsilon}A_{N,j}^{-2}
\le C_\tau\varepsilon+o(1).
\]
Letting \(\varepsilon\downarrow0\) establishes tightness and convergence at the left endpoint and completes the functional limit on \([0,1]\). Itô isometry gives the stated covariance function.

**5. Moment asymptotics.** Solve the exact recurrence from step 2:
\[
m_{N,N}=v_N\sum_{j=1}^N
\prod_{\ell=j+1}^N\left(1+\frac{2\alpha_N}{\ell}\right).
\]
The gamma-product approximation, uniformly away from finitely many small indices, and the harmonic Riemann sum yield
\[
\frac{m_{N,N}}{N\log N}
\longrightarrow12\int_0^1e^{-2\tau(1-u)}\,du
=12F(\tau).
\]
The finitely many small indices contribute only \(O_\tau(N)\), negligible after dividing by \(N\log N\). Since \(Z_N-1/2=U_N/[8(N+1)]\), the proportion moment follows. At \(\tau=0\), \(2\alpha_N=1\) and \(v_N=12\), so the recurrence is \(m_{N,k}=(1+1/k)m_{N,k-1}+12\), which telescopes to the displayed exact harmonic identity.

## Verification

Run `python3 urn_window_verify.py` with a standard Python interpreter. The standalone script checks the exact finite-state transition distribution for several rational mixture probabilities, compares enumerated moments with the derived recurrence, verifies the critical harmonic identity and conditional drift, and performs supplementary deterministic critical-window variance diagnostics. In one replay, **2,917 exact assertions and 56 numerical diagnostics passed**. These finite checks do not constitute a proof of the infinite-dimensional functional limit, which is established in the preceding argument.

## Relationship to prior work

Shi, Yin and Miao study the fixed-mixture Pólya–Friedman urn and establish a fixed-parameter central limit theorem on the noncritical side of the spectral boundary; they do not present a row-dependent mixing probability approaching that boundary. Classical generalized-urn and stochastic-approximation results (Janson; Bai–Hu–Zhang; Zhang) explain the fixed-regime Gaussian and critical behavior. A previously established exactly-critical logarithmic-time Brownian limit corresponds to \(\tau=0\) here and is not claimed as new. The present assertion concerns the *entire triangular critical window* \(p_N=1/3+2\tau/(3\log N)\), with both signs of \(\tau\), a nontrivial Ornstein–Uhlenbeck covariance process, and the interpolating second-moment profile. Fixed-parameter theorems do not by themselves justify this triangular limit, since asymptotic parameters and sample size vary together. The literature comparisons were not an exhaustive historical-priority certification.

## Limitations

The result addresses only the symmetric balanced mixed urn specified above; no generalization to arbitrary replacement matrices, initial compositions, nonconstant within-row mixing, or an unbounded sequence of critical-window parameters is proved. No quantitative functional approximation rate is asserted. The second-moment conclusion is explicit; higher moments, moderate deviations, and pathwise strong approximation are not. General stochastic-approximation literature may indirectly yield similar limits under additional uniformity arguments; an older broad generalized-urn article was not obtainable in full, leaving historical-priority uncertainty. Independent mathematical audit has not been performed.

## References

1. J. Shi, Q. Yin and Y. Miao, *Central Limit Theorem for a Pólya-Friedman Mixed Urn Model*, arXiv:2605.26669v1 (first posted 26 May 2026), https://arxiv.org/html/2605.26669v1.
2. L.-X. Zhang, *Central Limit Theorems of a Recursive Stochastic Algorithm with Applications to Adaptive Designs*, arXiv:1602.05708 (2016), https://arxiv.org/abs/1602.05708.
3. Z. D. Bai, F. Hu and L.-X. Zhang, *Gaussian approximation theorems for urn models and their applications*, Annals of Applied Probability **12** (2002), 1149–1173, https://doi.org/10.1214/aoap/1037125857.
4. S. Janson, *Functional limit theorems for multitype branching processes and generalized Pólya urns*, Stochastic Processes and their Applications **110** (2004), 177–245, https://doi.org/10.1016/j.spa.2003.12.002.
5. R. Roy, M. Takei and H. Tanemura, *The elephant random walk in the triangular array setting*, arXiv:2403.02881 (2024), https://arxiv.org/abs/2403.02881 (a distinct form of triangular array, based on limited memory).
