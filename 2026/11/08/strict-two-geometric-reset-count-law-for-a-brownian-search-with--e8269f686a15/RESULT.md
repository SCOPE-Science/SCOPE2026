# Strict two-geometric reset-count law for a Brownian search with an independently switching gate

## Finding

For a Brownian searcher on the positive half-line with positional Poisson resetting and a stochastically switching absorbing/reflecting endpoint, the count \(N\) of resets before absorption has an exact **strictly positive mixture of two distinct geometric distributions**, provided that the gate continues evolving through positional resets and starts in its stationary distribution. This is not a single geometric distribution.

Let \(D,r,a,\alpha,\beta>0\). The Brownian diffusivity is \(D\), each positional reset returns the particle to \(a\), the reset intensity is \(r\), and the gate switches closed-to-open at rate \(\alpha\) and open-to-closed at rate \(\beta\). Define

\[
 c=\alpha+\beta,\quad p=\frac{\alpha}{c},\quad q=\frac{\beta}{c},\quad z=\frac{r}{r+c},\quad A=z^{-1/2},
\]
\[
 u=e^{-a\sqrt{r/D}},\qquad v=e^{-a\sqrt{(r+c)/D}},\qquad B=q+pA.
\]

The probability of absorption before the first reset, conditional on the initial gate being closed or open, respectively, is

\[
 h_0=\frac{p(Au-v)}B,\qquad h_1=\frac{pAu+qv}B.
\]

Set

\[
 U=\begin{pmatrix}q+pz&p(1-z)\\q(1-z)&p+qz\end{pmatrix},\qquad
 h=\begin{pmatrix}h_0\\h_1\end{pmatrix},\qquad
 K=U-h\begin{pmatrix}U_{10}&U_{11}\end{pmatrix},
\]

where the gate states are indexed \(0\) (closed) and \(1\) (open). The rows of \(K\) give the joint probabilities of surviving one reset-clock interval and having the indicated gate state at that reset. Put

\[
 s=1-\frac{pAu}{B},\quad T=1+z-\frac{pAu+qzv}{B},\quad \Delta=z(1-h_1),\quad
 \lambda_\pm=\frac{T\pm\sqrt{T^2-4\Delta}}{2},
\]
\[
 w_+=\frac{s-\lambda_-}{\lambda_+-\lambda_-},\qquad
 w_-=\frac{\lambda_+-s}{\lambda_+-\lambda_-}.
\]

For every choice of the strictly positive model parameters,

\[
 0<\lambda_-<s<\lambda_+<1,\qquad w_+>0,\quad w_->0,\quad w_++w_-=1.
\]

**The exact probability mass function**, for every integer \(n\ge0\), is

\[
 \boxed{\Pr(N=n)=w_+(1-\lambda_+)\lambda_+^n+w_-(1-\lambda_-)\lambda_-^n.}
\]

In particular, the tail \(\Pr(N\ge n)=w_+\lambda_+^n+w_-\lambda_-^n\) is strictly log-convex, so the conditional probability of absorption at the next cycle, given \(n\) completed resets, decreases strictly with \(n\). With \(m_\pm=\lambda_\pm/(1-\lambda_\pm)\) and \(m=w_+m_++w_-m_-\),

\[
 \boxed{\operatorname{Var}(N)=m(1+m)+2w_+w_-(m_+-m_-)^2>m(1+m).}
\]

Thus the reset count is strictly more dispersed than a geometric variable with the same mean.

## Assumptions and scope

A particle follows reflected Brownian motion with generator \(D\partial_{xx}\) in \((0,\infty)\). At the left endpoint, the particle is reflected whenever an independent two-state gate is closed and is absorbed upon contact whenever that gate is open. Each positional reset is instantaneous, follows an independent exponential clock of rate \(r\), returns only the particle's position to \(a\), and does **not** reinitialize the gate. Initially the position is \(a\) and the gate has its stationary law \((q,p)\). Reset counts do not include the final absorption event, and the Brownian path, gate, and reset clock are initially independent. All five dimensional parameters \(D,r,a,\alpha,\beta\) are strictly positive. Zero-rate and deterministic-gate limits are excluded from the strict-mixture statement.

## Proof

**1. Success probabilities for a single clock interval.** Let \(E\) be an independent exponential time of rate \(r\), and \(\tau\) be absorption without positional resets. Define \(H_i(x)=\Pr_{x,i}(\tau<E)\). The backward equations are

\[
 D H_0''+\alpha(H_1-H_0)-rH_0=0,\qquad
 D H_1''+\beta(H_0-H_1)-rH_1=0,
\]

with \(H_0'(0)=0\), \(H_1(0)=1\), and decay as \(x\to\infty\). Diagonalizing the gate generator gives decaying eigenmodes \(e^{-x\sqrt{r/D}}(1,1)\) and \(e^{-x\sqrt{(r+c)/D}}(p,-q)\). The boundary conditions fix the coefficients \(pA/B\) and \(-1/B\), so

\[
 H_0(x)=\frac{pA}{B}e^{-x\sqrt{r/D}}-\frac pB e^{-x\sqrt{(r+c)/D}},\quad
 H_1(x)=\frac{pA}{B}e^{-x\sqrt{r/D}}+\frac qB e^{-x\sqrt{(r+c)/D}}.
\]

Evaluating at \(x=a\) yields \(h_0,h_1\). Since \(A>1\), \(0<v<u<1\), we have \(0<h_0<h_1<1\). Moreover \(h_1-h_0=v/B>0\).

**2. The surviving-cycle matrix.** For the independent gate alone, its transition matrix at the random clock time has resolvent \(U=r(rI-Q)^{-1}\), where \(Q\) is the two-state generator; direct evaluation gives the displayed \(U\). Extend the gate hypothetically beyond absorption, independently of the particle and clock. If absorption occurs before \(E\), the gate must be open at absorption, and by the exponential memoryless property and the strong Markov property its state at \(E\) has law \(U_{1j}\). Consequently the probability of reaching the clock before absorption with gate state \(j\) is exactly \(K_{ij}=U_{ij}-h_iU_{1j}\). Each \(K_{ij}\) is positive: there is positive probability of an early reset before any boundary encounter and of either gate end state. Its row sums equal \(1-h_i<1\). At each successful reset the particle restarts at \(a\) without changing the gate. Therefore, with initial row \(\pi=(q,p)\), for all integers \(n\ge0\),

\[
 \Pr(N=n)=\pi K^nh,\qquad \Pr(N\ge n)=\pi K^n\mathbf 1.
\]

In particular, since \(\min_i h_i>0\), \(N<\infty\) almost surely and has all finite moments.

**3. Positivity and separation of the two spectral components.** From the displayed entries and \(z=A^{-2}\), elementary multiplication yields

\[
 \operatorname{tr}K=T,\qquad \det K=\Delta=z(1-h_1)>0.
\]

The survival after a single reset-clock interval is \(s=\pi K\mathbf1=1-\pi h=1-pAu/B\). Direct substitution and cancellation yield the decisive strict identity

\[
 \boxed{\det(sI-K)=-\frac{pquv}{AB^2}<0.}
\]

It follows that the characteristic polynomial of \(K\) has two distinct real roots straddling \(s\). Since \(K\) has positive entries and positive determinant, both eigenvalues are positive. Since every row sum of \(K\) is strictly smaller than one, its spectral radius is smaller than one. Hence \(0<\lambda_-<s<\lambda_+<1\), and the displayed weights are both strictly positive and sum to one.

**4. Exact law and strict inequalities.** Cayley–Hamilton forces \(S_n=\pi K^n\mathbf 1\) to satisfy the second-order recurrence with characteristic roots \(\lambda_\pm\). The initial conditions \(S_0=1\) and \(S_1=s\) give

\[
 S_n=w_+\lambda_+^n+w_-\lambda_-^n\quad(n\ge0).
\]

Taking \(S_n-S_{n+1}\) proves the stated mass function. For all integers \(n\ge0\),

\[
 S_n S_{n+2}-S_{n+1}^2
 =w_+w_-(\lambda_+\lambda_-)^n(\lambda_+-\lambda_-)^2>0.
\]

Thus \(S_{n+1}/S_n\) is strictly increasing and the conditional absorption hazard \(1-S_{n+1}/S_n\) is strictly decreasing. The variance of a geometric law on \(\{0,1,\ldots\}\) with parameter \(1-\lambda\) is \(m_\lambda(1+m_\lambda)\), where \(m_\lambda=\lambda/(1-\lambda)\). The law of total variance for the strictly positive mixture gives the displayed strict excess \(2w_+w_-(m_+-m_-)^2\). This proves the complete claim.

## Verification

The standalone standard-library script `checker.py` evaluates all parameters, the surviving-cycle matrix, its two eigenvalues, its weights and two independently computed count probabilities: direct powers of \(K\) and the geometric-mixture formula. It also compares the mean count to the known average absorption time via \(\mathbb E[N]=r\mathbb E[\tau_{\mathrm{abs}}]\). Under the displayed definitions the established source formula for that mean is

\[
 \mathbb E[\tau_{\mathrm{abs}}]=\frac{u^{-1}-1}{r}+\frac{q}{p}\frac{u^{-1}}{rA}\left(1+\frac{r}{c}v\right).
\]

The identity follows independently from the compensator of the Poisson reset clock stopped at absorption. The checker uses 321 parameter configurations and performs 10,914 deterministic assertions; running `python3 checker.py` produced `PASS: 10914 deterministic diagnostics across 321 parameter configurations`. Separately, a finite-difference calculation of the two-state killed backward equations on a truncated half-line agreed with the analytical \(h_0,h_1\) at the illustrative parameters within \(6.3\times10^{-6}\). These finite checks support but do not prove the universal claim; the four proof steps above are its analytical justification.

For \(p=1/2\), \(r=c=D=a=1\), the two component parameters are approximately \(\lambda_-=0.419889527139634\) and \(\lambda_+=0.814260561219115\), with \(w_-=0.075460279704806\) and \(w_+=0.924539720295194\). The count mean is approximately \(4.1076957895\), its variance approximately \(22.8500542768\), versus approximately \(20.9808604888\) for a same-mean geometric law.

## Relationship to prior work

Mercado-Vásquez and Boyer (2021) analyze precisely the independently switching, non-reset gate on the positive half-line. They establish the survival-time transform and the first two time moments, including the mean used above; the joint event that a clock rings before gated absorption, its surviving gate state, and the exact positive two-geometric reset-count law and its strict hazard/dispersion properties are different observables and are not stated there. Their Appendix B explicitly contrasts this gate-persistent model with Bressloff (2020), where the gate itself is reinitialized at each positional reset; that latter renewal model has a single-geometric counting mechanism. Biswas and collaborators (2023) study optimal mean completion times in gated drift-diffusion, not this count law. Bressloff (2023) analyzes reset-count truncation for an absorbing-target diffusion without this independently persistent gate. General discrete phase-type theory predicts a rational generating function but does not by itself imply that the two spectral weights in this specific target system are both strictly positive or that its count hazard decreases strictly; the negative characteristic-polynomial identity establishes those stronger properties here.

## Limitations

The precise two-geometric positivity claim assumes stationary initial gate mixing, strict positivity of every physical parameter, one Brownian spatial coordinate, a target at a reflecting/absorbing endpoint, and gate-state persistence across positional resets. It is not asserted for arbitrary initial gate mixtures, a gate reinitialized on reset, drift, several gates, or arbitrary non-Poisson clocks. Its novelty assessment is a literature comparison, not a proof that no equivalent unindexed theorem exists. The checker is a finite diagnostic, not an infinite certification.

## References

- G. Mercado-Vásquez and D. Boyer, *Search of stochastically gated targets with diffusive particles under resetting*, arXiv:2107.02148 (first posted 2021-07-05), https://arxiv.org/abs/2107.02148.
- P. C. Bressloff, *Diffusive search for a stochastically-gated target with resetting*, arXiv:2009.02739 (first posted 2020-09-06), https://arxiv.org/abs/2009.02739.
- A. Biswas, A. Pal, D. Mondal and S. Ray, *Rate enhancement of gated drift-diffusion process by optimal resetting*, arXiv:2304.10605 (first posted 2023-04-20), https://arxiv.org/abs/2304.10605.
- P. C. Bressloff, *Truncated stochastically switching processes*, arXiv:2310.20502 (first posted 2023-10-31), https://arxiv.org/abs/2310.20502.
