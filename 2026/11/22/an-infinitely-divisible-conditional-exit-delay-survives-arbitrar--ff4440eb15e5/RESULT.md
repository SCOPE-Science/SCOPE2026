# An infinitely divisible conditional-exit delay survives arbitrary reset-return overhead

## Finding and assumptions

Brownian exploration with generator \(D\partial_x^2\), \(D>0\), starts at \(a\) in \((0,L)\), where \(0<a<L/2\) and \(b=L-a\). Each attempt has a rate-\(r>0\) exponential interruption clock independent of its Brownian exploration. Absorption at 0 or \(L\) during exploration immediately terminates the process. If the clock rings first, a nonnegative, almost surely finite return follows, with absorption inactive and the next exploration clock not yet running. Each exploration and its clock are freshly sampled from their fixed laws independently of the **entire history** preceding its start; explorations always start at \(a\). Return durations may depend on the aborted attempt and previous history, and need not be identically distributed or independent of each other. In particular, this includes the usual i.i.d. regenerative return cycles. No future exploration or clock can be used to choose earlier return durations.

Let \(T_0,T_L\) denote total completion times, including all returns, conditional on the eventual side. There is a strictly positive, nondegenerate, infinitely divisible random variable \(\Delta_r\) such that
\[
 T_L\stackrel d=T_0+\Delta_r,
 \qquad T_0\ \text{and}\ \Delta_r\ \text{independent on the coupling space}.
\]
This does not compare the two times pathwise on a common search trajectory. The full delay law is unaffected by the return mechanism just described, and has Laplace transform
\[
 M_r(s)=\frac{\sinh(a\sqrt{(r+s)/D})}{\sinh(b\sqrt{(r+s)/D})}
         \frac{\sinh(b\sqrt{r/D})}{\sinh(a\sqrt{r/D})},\qquad s\ge0.
\]
Write \(\lambda_{\ell,n}=r+D\pi^2n^2/\ell^2\). The sum \(\sum_{n\ge1} B_nE_n\) has law \(\Delta_r\) and converges almost surely, where the \(B_n\) are Bernoulli with probabilities \(1-\lambda_{b,n}/\lambda_{a,n}\), the \(E_n\) are exponential of rates \(\lambda_{b,n}\), and all those variables are independent. The drift-free Lévy measure and positive-integer cumulants are
\[
 \nu_r(dt)=\frac1t\sum_{n\ge1}(e^{-\lambda_{b,n}t}-e^{-\lambda_{a,n}t})\,dt,
 \qquad \kappa_k(\Delta_r)=(k-1)!\sum_{n\ge1}
    (\lambda_{b,n}^{-k}-\lambda_{a,n}^{-k})>0.
\]
When the conditional completion-time means are finite their difference equals \(\mathbb E\Delta_r\), which is strictly completely monotone in \(r>0\) and has the limits
\[
 \mathbb E\Delta_r\longrightarrow (b^2-a^2)/(6D)\quad(r\downarrow0),
 \qquad \mathbb E\Delta_r\sim (b-a)/(2\sqrt{Dr})\quad(r\to\infty).
\]
For \(a=b\) the two conditional laws are equal and the delay is zero. For \(a>b\), exchange the target labels.

## Proof

**One exploration.** Let \(\tau\) and \(J\) be the exit time and side of an uninterrupted Brownian attempt, and \(\sigma\) its independent interruption clock. For \(k_s=\sqrt{(r+s)/D}\), the Dirichlet equations \(Du''=(r+s)u\) with boundary values 1 at the selected target and 0 at the other give
\[
 f_0(s)=\mathbb E_a[e^{-s\tau};\,\tau<\sigma,J=0]=\frac{\sinh(bk_s)}{\sinh(Lk_s)},\qquad
 f_L(s)=\mathbb E_a[e^{-s\tau};\,\tau<\sigma,J=L]=\frac{\sinh(ak_s)}{\sinh(Lk_s)}.
\]
Write \(p=f_0(0)+f_L(0)>0\) for the probability of success of a fresh attempt.

**The failed prefix is common to both conditional laws.** Let \(N\) be the index of the first successful attempt; fresh exploration gives \(\Pr(N>m)=(1-p)^m\). On this event let \(S_m\) be the elapsed time through the first \(m\) failures and their completed returns, including \(S_0=0\). The event and its history are known before attempt \(m+1\). Conditioning on that history gives the joint transform of total time and side \(j\):
\[
 H_j(s)=f_j(s)\,C(s),\qquad
 C(s)=\sum_{m\ge0}\mathbb E[e^{-s S_m};N>m],\qquad C(0)=1/p.
\]
The series is bounded by \(1/p\); it is not assumed geometric for \(s>0\). In fact \(p C(s)\) is the transform of \(S_{N-1}\), the time through the complete failed prefix. The same factorization with any bounded measurable function of the stopped prefix in place of \(e^{-sS_m}\), and any bounded test of the next successful exploration in place of its Laplace weight, proves that the stopped prefix and the successful exploration (including the side) are independent. With genuinely i.i.d. failed-cycle laws, \(C(s)=(1-B(s))^{-1}\), where \(B(s)=\mathbb E[e^{-s(\sigma+R)};\sigma<\tau]\) for one attempt with return time \(R\).

Writing \(\Phi_j(s)=H_j(s)/H_j(0)\) for the conditional transforms, we obtain \(\Phi_L/\Phi_0=f_L(s)f_0(0)/(f_0(s)f_L(0))=M_r(s)\). In particular the numerator and denominator share the complete overhead factor, even when the return durations are dependent.

**Identification of the delay.** For independent Brownian motion started at \(a\) in \((0,b)\), let \(\theta_b,\theta_0\) be the first times at the indicated endpoints. Its Dirichlet transform \(\mathbb E_a[e^{-u\theta_b};\theta_b<\theta_0]=\sinh(a\sqrt{u/D})/\sinh(b\sqrt{u/D})\) at \(u=r+s\), divided by its value at \(u=r\), proves that \(M_r\) is the transform of \(\theta_b\) under the exponentially tilted success law. This is a probability law supported on strictly positive times. Uniqueness of the Laplace transform proves the asserted independent distributional coupling. Strict positivity gives a nontrivial stochastic ordering.

**Product, spectral series, and moments.** Euler's product \(\sinh z=z\prod_{n\ge1}(1+z^2/(\pi^2n^2))\) gives
\[
 M_r(s)=\prod_{n\ge1}\frac{1+s/\lambda_{a,n}}{1+s/\lambda_{b,n}}.
\]
Since \(a<b\), \(0<\lambda_{b,n}<\lambda_{a,n}\). Each factor is the transform of \(B_nE_n\), and the expected sum of these nonnegative variables is \(\sum_n(\lambda_{b,n}^{-1}-\lambda_{a,n}^{-1})<\infty\). This proves almost sure convergence, and independence and the product prove equality of laws. A single term has positive variance, so the law is nondegenerate. Taking logarithms gives the sum of negative integrals of \((1-e^{-st})(e^{-\lambda_{b,n}t}-e^{-\lambda_{a,n}t})/t\). By Tonelli, the integral of \(t\) against the summed Lévy measure is the same finite expectation series, which implies Lévy integrability both at zero and infinity. This yields infinite divisibility by the Lévy–Khintchine representation. The logarithmic product is analytic near zero (the summands are bounded by a constant times \(1/n^2\) there), and expansion gives the stated cumulants. Termwise differentiation in \(r\) gives strict complete monotonicity of the first cumulant. Dominated convergence at zero and \(\sum n^{-2}=\pi^2/6\) give the finite low-rate limit; the identity
\[
 \mathbb E\Delta_r=\frac{b\coth(b\sqrt{r/D})-a\coth(a\sqrt{r/D})}{2\sqrt{Dr}}
\]
gives the high-rate limit. The equality of laws needs no finite return moments.

## Relationship to prior work

Pal et al. give a common exit-current denominator and conditional normalization for instantaneous resetting (Eqs. (4)–(7)), from which the no-overhead conditional transform ratio follows with the interval Dirichlet transforms. Pal–Prasad give interval resetting formulas. The spectral law is classical in substance: at \(r=0\) the hyperbolic ratio is the ratio of Laplace transforms of two scaled Pitman–Yor \(S_1\) laws; their Euler-product representation gives the individual spectral factors, and \(r>0\) is exponential tilting. The contribution here is the exact conditional-time convolution and invariance under history-dependent return overhead with fresh exploration, not a new hyperbolic distribution or a new renewal formula for instantaneous resetting. Newton–Vega Coso study stochastic orders and reset responses; Chen–Tang–Li show invariance of splitting probabilities in a finite-time return model with absorption disabled during returns. Those comparisons concern different conclusions from the full conditional convolution with arbitrary past-dependent overhead. Bressloff studies multiple targets with finite returns and refractory periods; the full original was not inspected, so historical priority is not asserted without qualification.

## Verification and limits

The enclosed `verify.py` gives finite numerical consistency checks for the i.i.d. mixture examples, spectral product and moments; execute with Python 3's standard library. The proof above, not the finite checker, establishes the extension to history-dependent returns and the convergence, positivity and exact law. Arbitrary anticipation of future explorations, absorption during return, variable exploration/reset sites and general nonexponential interruption clocks are not covered. Heavy-tailed overhead can leave conditional completion-time moment differences undefined.

1. S. Pal et al., *Universal criterion for selective outcomes under stochastic resetting*, https://arxiv.org/abs/2502.09127.
2. A. Pal and V. V. Prasad, *First passage under stochastic resetting in an interval*, https://arxiv.org/abs/1812.03009.
3. J. Pitman and M. Yor, *Infinitely divisible laws associated with hyperbolic functions*, https://statistics.berkeley.edu/tech-reports/581.
4. T. Newton and J. A. Vega Coso, *Stochastic Orders of the Exit Pair and the Monotone Response to Resetting*, https://arxiv.org/abs/2611.01756.
5. H. Chen, C. Tang, and G. Li, *Finite-time stochastic resetting in bounded domains: competing targets, energetic cost, and optimal search strategies*, https://arxiv.org/abs/2611.23790.
6. P. C. Bressloff, *Search processes with stochastic resetting and multiple targets*, https://doi.org/10.1103/PhysRevE.102.022115.
