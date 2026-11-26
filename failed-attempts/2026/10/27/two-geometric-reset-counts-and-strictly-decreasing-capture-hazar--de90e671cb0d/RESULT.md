# Two-geometric reset counts and strictly decreasing capture hazards at a fluctuating target

## Finding
Consider a Brownian searcher on the half-line with an independently fluctuating absorbing/reflecting target at the origin. The searcher is returned to a fixed point by a Poisson clock, but resetting does **not** restart the target's internal state. If the target initially has its equilibrium internal distribution, the number \(N\) of resets strictly before absorption is an **exact positive mixture of two distinct geometric distributions**. Its conditional probability of capture in the next attempt, given that the previous attempts all failed, decreases strictly with the number of failures. Moreover, with \(m=\mathbb E N\),
\[
\operatorname{Var}(N)-m(1+m)
=\frac{2p t(f_1-f_0)}{(1-t)^2\bar f}>0.
\]
All quantities on the right are explicitly defined below. Thus the resetting count is strictly more dispersed than a geometric random variable with the same mean. This statement holds for all strictly positive model parameters, not just in a limiting regime.

## Assumptions and scope
Fix \(D,r,\alpha,\beta,x_r>0\). Between resets the particle follows \(dX_t=\sqrt{2D}\,dB_t\) on \([0,\infty)\). An autonomous independent two-state continuous-time chain \(G_t\in\{0,1\}\) jumps from closed state \(0\) to open state \(1\) at rate \(\alpha\), and from \(1\) to \(0\) at rate \(\beta\). The origin reflects the particle while \(G_t=0\) and absorbs it when \(G_t=1\); absorption also occurs immediately if the gate opens while the particle is at the origin. An independent Poisson clock of rate \(r\) resets only the *position* to \(x_r\), leaving \(G_t\) unchanged. Initially \(X_0=x_r\), while \(G_0\) has stationary probabilities \(\pi=(p,1-p)\), where \(p=\beta/(\alpha+\beta)\). Let \(N\in\{0,1,2,\ldots\}\) count the resets strictly before the first absorption.

Define
\[
 t=\frac{r}{r+\alpha+\beta},\quad k=\sqrt{r/D},\quad
 h=\sqrt{1+(\alpha+\beta)/r},\quad
 f_0=\frac{\alpha(h e^{-kx_r}-e^{-khx_r})}{\beta+\alpha h},\quad
 f_1=\frac{\alpha h e^{-kx_r}+\beta e^{-khx_r}}{\beta+\alpha h},\quad
 \bar f=p f_0+(1-p) f_1.
\]
The scalar \(t\) is a dimensionless relaxation ratio, not physical time; \(f_i\) is the probability of absorption before the first prospective reset for initial target state \(i\). In particular \(0<f_0<f_1<1\).

Let
\[
 P=\begin{pmatrix}p+t(1-p)&(1-p)(1-t)\\p(1-t)&1-p+tp\end{pmatrix},\qquad
 K=(I-f e_1^{\mathsf T})P,\quad f=(f_0,f_1)^{\mathsf T},\quad e_1=(0,1)^{\mathsf T}.
\]
Here \(K_{ij}\) is the probability that one Poisson reset occurs before absorption and that the target is in state \(j\) at that reset, conditioned on state \(i\) at the beginning of that attempt. Let \(1>\lambda_1>\lambda_2>0\) denote its two eigenvalues and \(s=1-\bar f\). Then
\[
 \lambda_2<s<\lambda_1,\quad
 w_1=\frac{s-\lambda_2}{\lambda_1-\lambda_2},\quad
 w_2=\frac{\lambda_1-s}{\lambda_1-\lambda_2},\quad
 w_1,w_2>0,\quad w_1+w_2=1.
\]
For every integer \(n\ge0\), the precise distribution and its tail are
\[
 \mathbb P(N=n)=\sum_{j=1}^2w_j(1-\lambda_j)\lambda_j^n,\qquad
 \mathbb P(N\ge n)=\sum_{j=1}^2w_j\lambda_j^n.
\]
The exact mean is
\[
 m=\frac{1-t+t f_1-\bar f}{(1-t)\bar f}.
\]
Define the per-attempt capture hazard \(H_n=\mathbb P(N=n\mid N\ge n)\). For every \(n\ge0\), \(H_{n+1}<H_n\) and \(H_n\downarrow1-\lambda_1\).

## Proof
**1. One-attempt kernel.** Put \(Q=\left(\begin{smallmatrix}-\alpha&\alpha\\\beta&-\beta\end{smallmatrix}\right)\). For a trial that stops at either the next position reset or at target absorption, the matrix \(K(x)\) of probabilities of surviving to the next reset with a specified target state solves the backward resolvent problem
\[
 D K''(x)+QK(x)-rK(x)=-rI\quad(x>0),\qquad
 K_{1j}(0)=0,\quad K_{0j}'(0)=0,
\]
with a bounded solution at infinity. The matrix \(P=r(rI-Q)^{-1}\) solves the constant part. The two independent decaying homogeneous modes are \((1,1)^{\mathsf T}e^{-kx}\) and \((\alpha,-\beta)^{\mathsf T}e^{-khx}\). Enforcing the absorbing and reflecting conditions gives the unique bounded solution \(K(x)=(I-f(x)e_1^{\mathsf T})P\), with exactly the displayed formulas for \(f_0(x),f_1(x)\). At \(x=x_r\) this is the stated matrix \(K\). Directly, \(f_1-f_0=(\alpha+\beta)e^{-khx_r}/(\beta+\alpha h)>0\), while \(f_1<1\) because \(x_r>0\), and \(f_0>0\) because \(h>1\) and \(e^{-kx_r}>e^{-khx_r}\). All entries of \(K\) are positive because each two-state target transition has strictly positive probability before a surviving reset.

**2. Spectral weights.** The stochastic target-only kernel \(P\) has determinant \(t\). Since \(K=(I-f e_1^{\mathsf T})P\),
\[
 \det K=t(1-f_1)>0,\qquad \det(I-K)=(1-t)\bar f>0.
\]
Because the entries of \(K\) are positive and each row sum is \(1-f_i<1\), its eigenvalues are real, distinct, strictly positive, and less than one. Computing the characteristic polynomial at the stationary one-step survival probability \(s=\pi K\mathbf 1=1-\bar f\) yields the strict identity
\[
 \det(sI-K)=-p t(f_1-f_0)\bar f<0.
\]
Hence \(\lambda_2<s<\lambda_1\), giving two strictly positive weights \(w_1,w_2\).

**3. Full count distribution.** At each reset the searcher restarts at \(x_r\) while the target state is preserved. The strong Markov property at reset times therefore gives \(\mathbb P(N\ge n)=\pi K^n\mathbf1\), including the \(n=0\) case. The sequence satisfies the order-two Cayley--Hamilton recurrence with characteristic roots \(\lambda_1,\lambda_2\), and its initial values are \(1\) and \(s\). Solving the recurrence yields the asserted two-geometric mixture and the exact finite mean. Because its tail is a positive sum of two distinct exponentials, the tail ratios \(\mathbb P(N\ge n+1)/\mathbb P(N\ge n)\) strictly increase toward \(\lambda_1\): equivalently the capture hazards strictly decrease.

**4. Strict extra dispersion.** A geometric count with parameter \(1-\lambda\), supported on \(\{0,1,\ldots\}\), has mean \(\lambda/(1-\lambda)\) and variance equal to its mean times one plus its mean. Variance decomposition across the two mixture components gives
\[
 \operatorname{Var}(N)-m(1+m)=2w_1w_2
 \left(\frac{\lambda_1}{1-\lambda_1}-\frac{\lambda_2}{1-\lambda_2}\right)^2.
\]
Substitution of \(w_1w_2=-\det(sI-K)/(\lambda_1-\lambda_2)^2\) and \((1-\lambda_1)(1-\lambda_2)=\det(I-K)=(1-t)\bar f\) yields exactly \(2pt(f_1-f_0)/((1-t)^2\bar f)>0\). This proves all claims.

## Verification
The standalone `verify.py` checks the resolvent formula against an independently discretized mixed-boundary backward problem for three parameter choices. Symbolic algebra checks the determinant, characteristic-polynomial, mean, and exact variance identities. Random positive-parameter suites independently evaluate the two eigenvalues, positive mixing weights, geometric tails, and dispersion coefficient. The checker reports 24,018 assertion groups. These computations are reproducibility checks; universal statements follow from the proof above.

## Relationship to prior work
Mercado-Vásquez and Boyer (arXiv:2107.02148, first public 2021-07-05) analyze **the same independent-gate protocol** and solve its survival-time and first-hitting-time boundary-value problems, including means and relative variances. Their time-Laplace transform is distinct from the reset-*count*-marked kernel computed here. Bressloff (arXiv:2009.02739, first public 2020-09-06) studies a different protocol in which the gate is reinitialized at resets, producing a renewal structure and ordinary geometric attempt counts. Bressloff (arXiv:2310.20502, first public 2023-10-31) studies the number of resets before capture at an **ungated** absorbing boundary using a finite reset budget. The present statement concerns nonrenewal attempt counts for an independently fluctuating target; it neither claims that finite-state phase-type distributions are novel nor that its time-to-capture statistics supersede these works.

## Limitations
The positivity of both mixing weights requires equilibrium initial gate probabilities, positive opening and closing rates, and a positive reset point. The conclusion need not hold for arbitrary prescribed initial gate states, for a target state that is forcibly reinitialized at every reset, or for more than two internal target states. Only the number of position-reset events is studied; no general formula for joint reset count and capture duration is claimed. The sharp identity is an exact mathematical consequence of the specified half-line model. The full scholarly-priority status of this particular observable remains subject to independent literature review, especially for abstract Markov-modulated phase-type results.

## References
1. G. Mercado-Vásquez and D. Boyer, *Search of stochastically gated targets with diffusive particles under resetting*, arXiv:2107.02148 (first version 2021-07-05); J. Phys. A 54 (2021), 444002.
2. P. C. Bressloff, *Diffusive search for a stochastically-gated target with resetting*, arXiv:2009.02739 (2020); J. Phys. A 53 (2020), 425001.
3. P. C. Bressloff, *Truncated stochastically switching processes*, arXiv:2310.20502 (2023); Phys. Rev. E 109 (2024), 024103.
