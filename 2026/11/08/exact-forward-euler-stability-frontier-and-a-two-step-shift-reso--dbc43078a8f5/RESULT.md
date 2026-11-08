# Exact forward-Euler stability frontier and a two-step shift resonance for exponential FSBP transport

## Finding
For positive-speed periodic linear transport, a two-node exponential function-space summation-by-parts (FSBP) spatial discretization with upwind interfaces has an **exact all-wavenumber forward-Euler CFL frontier**. The exponential shape parameter can turn the polynomial two-node scheme's zero grid-uniform forward-Euler stability window into a positive one. At its unique optimal shape parameter, the fully discrete method has a resonant **two-step exact one-cell shift**.

For \(\beta>0\), define the dimensionless time step \(\nu=a\Delta t/h\) and
\[
\nu_*(\beta)=\frac{2\tanh(\beta/2)}{\beta}\min\{1,\sinh^2(\beta/2)\}.
\]
All Fourier amplification eigenvalues have modulus at most one **if and only if** \(0\le\nu\le\nu_*(\beta)\). In the polynomial limit \(\beta=0\), no positive step is stable uniformly across all Fourier phases. The threshold rises to its unique maximum
\[
\beta_c=2\operatorname{arsinh}1,\qquad
\nu_*(\beta_c)=\frac{1}{\sqrt2\operatorname{arsinh}1}\approx0.8022781617,
\]
then decreases. At this parameter and step, writing \(U_j^n=(u_j^n,v_j^n)^T\) for the two nodal values on element \(j\),
\[
U_j^{n+2}=U_{j-1}^{n}\quad\text{for every periodic sequence of nodal data.}
\]

## Assumptions and scope
Take a ring of \(m\ge2\) cells of equal length \(h>0\), positive advection speed \(a>0\), local coordinate \(\xi\in[0,1]\), and the cellwise approximation space \(\mathcal F_\beta=\operatorname{span}\{1,e^{\beta\xi}\}\), with \(\beta>0\). Each cell has two endpoints. We use the unique nodal derivative exact on \(\mathcal F_\beta\), its positive diagonal SBP norm, the **symmetric consistent** physical linear-advection volume flux (equivalently the strong-form nodal derivative), and the usual upwind intercell numerical flux. Time integration is forward Euler with a constant step. In the limit \(\beta=0\), interpret \(\mathcal F_0=\operatorname{span}\{1,\xi\}\), not the collapsed exponential basis.

The uniform spectral stability criterion means that for **every** Fourier phase \(\theta\in[0,2\pi)\), both eigenvalues of the single-cell amplification symbol have modulus at most one. It is therefore sufficient simultaneously for every finite periodic cell count and necessary for stability uniformly in the cell count; a particular fixed small ring can admit additional steps. This is an exact-arithmetic modal statement, not a positivity, one-step energy contraction, or finite-precision guarantee.

## Proof
**FSBP derivative and norm.** Set
\[
c=\frac{\beta}{e^\beta-1},\qquad d=\frac{\beta e^\beta}{e^\beta-1},\qquad
D=\begin{pmatrix}-c&c\\-d&d\end{pmatrix},\qquad
P=\operatorname{diag}\!\left(\frac1{2c},\frac1{2d}\right).
\]
Both \(c,d\) are positive, and \(D\mathbf1=0\), \(D(e^{0},e^\beta)^T=\beta(e^{0},e^\beta)^T\), and \(PD+D^TP=\operatorname{diag}(-1,1)\). These identities establish exact differentiation, positivity of the norm, and the SBP boundary identity without approximation.

**Cell recurrence and Fourier polynomial.** With \(v_{j-1}\) the upwind exterior trace on the left face, the spatial method is
\[
\dot u_j=\frac ah\,c(-u_j-v_j+2v_{j-1}),\qquad
\dot v_j=\frac ah\,d(u_j-v_j).
\]
For \(z=e^{-i\theta}\) and \(\nu=a\Delta t/h\), the forward-Euler Fourier symbol is
\[
G(z)=I+\nu\begin{pmatrix}-c&c(-1+2z)\\d&-d\end{pmatrix}.
\]
Writing \(p=\nu(c+d)\), \(q=2\nu^2cd\), its characteristic polynomial is
\[
\mu^2-(2-p)\mu+1-p+q(1-z)=0.\tag{1}
\]

**Sharpness.** A complex-coefficient quadratic \(\mu^2-b\mu+k\) has both roots in the closed unit disk (by interior approximation and the degree-two Schur criterion) when \(|k|\le1\) and \(|b|\,|1-k|\le1-|k|^2\), with boundary cases treated by continuity. Set \(x=1-\cos\theta\in[0,2]\), \(b=2-p\), \(k=1-p+q(1-z)\). Direct expansion gives
\[
(1-|k|^2)^2-(2-p)^2|1-k|^2
=2qx(2-p)(p^2-pq-2q)+4q^2x^2(p-q-1)^2.\tag{2}
\]
If
\[
0\le p\le2,\qquad p^2-pq-2q\ge0,\tag{3}
\]
then \(q\le p^2/(p+2)\le p/2\). Consequently \(|k|\le1\): its squared modulus is affine in \(x\), its endpoint values are \((1-p)^2\) and \((1-p+2q)^2\), and both are at most one. Equation (2) then proves the remaining Schur inequality. This proves sufficiency, initially for strict inequalities and then by continuity.

For necessity, at \(z=1\), the roots of (1) are \(1\) and \(1-p\), requiring \(p\le2\). If \(p<2\) and \(p^2-pq-2q<0\), equation (2) is negative at sufficiently small positive \(x\), which violates the Schur necessary inequality. If \(p=2\) but \(p^2-pq-2q<0\), then \(q>1\) and at \(z=-1\) one has \(|k|=|-1+2q|>1\), again impossible. Hence (3) is necessary and sufficient. Inserting \(p,q\) shows
\[
\nu\le \min\left\{\frac2{c+d},\frac{(c-d)^2}{2cd(c+d)}\right\}.
\]
Since \(d-c=\beta\), \((c+d)=\beta\coth(\beta/2)\) and \(cd=\beta^2/(4\sinh^2(\beta/2))\), this is exactly the displayed \(\nu_*(\beta)\). The limit of its second branch is \(\beta^2/4+O(\beta^4)\), hence zero when \(\beta=0\). Necessity is for the **whole** continuum of Fourier phases; failure at sufficiently small phase gives a failing large enough ring.

**Maximizer and resonance.** The second branch divided by the first equals \(\sinh^2(\beta/2)\), so the crossover is uniquely at \(\beta_c=2\operatorname{arsinh}1\). The first (small-\(\beta\)) branch is strictly increasing: with \(u=\beta/2\), its logarithmic derivative has sign \(3\coth u-\tanh u-1/u>0\). The other branch \(2\tanh(\beta/2)/\beta\) is strictly decreasing. At the crossover and optimal step one has \(p=2\), \(q=1\). Thus (1) becomes \(\mu^2-z=0\), and by Cayley--Hamilton
\[
G(z)^2=zI.
\]
The Fourier multiplier \(z\) represents the backward one-cell shift on the periodic ring, proving \(U_j^{n+2}=U_{j-1}^n\) for **all data**, not merely selected modes. Every Fourier multiplier is unimodular at the resonant step; the two-step map has no numerical damping even though the underlying semidiscretization is energy-stable.

## Verification
Execute `python verify.py` in an environment with Python and NumPy. It verifies the SBP identities and exponential exactness; compares assembled periodic matrices with Fourier eigenvalues on six ring sizes and nine shape parameters; checks characteristic coefficients and stability at 170 phases per nonzero parameter; confirms endpoint violations; and directly checks the two-step shift identity on five ring sizes. The supplied run returned `VERIFY_OK` with 1938 counted checks. These finite tests support the algebraic derivations but do not prove the all-phase theorem or historical priority.

## Relationship to prior work
Haase, Winters and Glaubitz (arXiv:2610.30272v1, 2026) establish conservation, entropy stability and design-order properties for general-function-space SBP flux differencing, with exponential spaces and numerical high-order time integrators. Glaubitz, Nordström and Öffner (arXiv:2203.05479v2, 2023 revision of a 2022 preprint) develop the underlying FSBP exactness and positive-norm theory and study linear advection with SSP-RK(3,3). Gassner and Kopriva (2011) analyze dispersion/dissipation of standard polynomial DGSEM. These results provide the underlying spatial framework and classical Fourier methodology. The present statement isolates the sharp **forward-Euler** all-frequency frontier for the two-node exponential subspace and identifies an all-data two-step shift resonance. No equivalence or broader theorem was identified in the inspected sources and claim searches; the general Fourier/Schur methodology is classical, and unlocated earlier exponential-fitting stability analyses remain a priority uncertainty.

## Limitations
Only scalar positive-speed periodic transport, equal cells, the stated two-node exponential FSBP operator and upwind interfaces are covered. The theorem concerns per-phase spectral radius, not uniform one-step operator-norm contraction, accuracy at the resonant endpoint, nodal positivity, all Runge--Kutta integrators or numerical round-off. At the resonance, absence of damping does **not** imply that the scheme is a useful physical-time integrator. The dimensionless parameter \(\beta\) is relative to the cell: for a fixed physical exponential profile with rate \(\alpha\), it equals \(\alpha h\); the small-parameter stability limit must then be interpreted accordingly. Historical priority and independent mathematical validation remain unresolved.

## References
- H. M. Haase, A. R. Winters and J. Glaubitz, *Summation-by-parts operators for general function spaces: Flux differencing, entropy stability, and accuracy*, arXiv:2610.30272v1, first public October 21, 2026. https://arxiv.org/abs/2610.30272
- J. Glaubitz, J. Nordström and P. Öffner, *Summation-by-parts operators for general function spaces*, arXiv:2203.05479v2. https://arxiv.org/html/2203.05479v2
- G. Gassner and D. A. Kopriva, *A Comparison of the Dispersion and Dissipation Errors of Gauss and Gauss–Lobatto Discontinuous Galerkin Spectral Element Methods*, SIAM J. Sci. Comput. 33 (2011), 2560–2579. https://doi.org/10.1137/100807211
