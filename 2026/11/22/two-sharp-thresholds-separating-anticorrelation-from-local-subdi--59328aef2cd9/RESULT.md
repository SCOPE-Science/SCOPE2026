# Two sharp thresholds separating anticorrelation from local subdiffusion in hierarchical Ornstein–Uhlenbeck transport

## Finding

The stationary two-noise hierarchical Ornstein–Uhlenbeck (OU) tracer has **two distinct sharp transport thresholds**. A negative velocity autocorrelation appears strictly before the mean-squared displacement (MSD) acquires any genuinely subdiffusive *instantaneous logarithmic slope*. In the intervening open parameter region, both a sign-changing velocity autocorrelation and an overshooting finite-time diffusivity coexist with a logarithmic MSD slope strictly greater than one **at every finite positive observation time**.

Precisely, set \(q=\gamma_2/\gamma_1\in(0,1)\) and \(d=D_1/D_2>0\). For the stationary model specified below, define \(C(t)=\mathbb E[V_0V_t]\), \(M(t)=\mathbb E[X_t^2]\), the running diffusivity \(J(t)=M'(t)/2\), and the local exponent \(\nu(t)=tM'(t)/M(t)\) for \(t>0\). The complete classification is:

1. If \(0<d\le 1-q^2\), then \(C(t)>0\), \(J(t)\) increases strictly toward \(D_2\), and \(\nu(t)>1\) for every \(t>0\).
2. If \(1-q^2<d\le1+q\), then \(C(t)\) changes sign **exactly once**, from positive to negative, and \(J(t)\) has exactly one maximum, strictly greater than \(D_2\); nevertheless \(\nu(t)>1\) for every finite \(t>0\).
3. If \(d>1+q\), the same unique autocorrelation sign reversal and running-diffusivity maximum occur, but \(\nu(t)=1\) has exactly **one** solution \(t_*>0\). It lies strictly after the autocorrelation crossing. The local MSD exponent satisfies \(\nu(t)>1\) before \(t_*\) and \(0<\nu(t)<1\) afterwards, approaching one from below.

At the sharp second boundary \(d=1+q\), the logarithmic slope remains above one at every finite time, but its approach to one accelerates from the generic reciprocal-time law to the exponential law
\[
\nu(t)-1\sim\frac{q}{1-q}e^{-\gamma_2t}\qquad(t\to\infty).
\]
For \(d\ne1+q\), the exact leading law is
\[
\nu(t)-1\sim\frac{1-d/(1+q)}{\gamma_2t}\qquad(t\to\infty).
\]
The strict separation of the two thresholds has width \(q(1+q)>0\) in the diffusivity-ratio variable \(d\), and persists for every finite scale separation \(0<q<1\).

## Assumptions and scope

Let \(\gamma_1>\gamma_2>0\) and \(D_1,D_2>0\). Let \(W_1,W_2\) be independent standard Brownian motions. The *unique stationary* solution \((U_1,U_2)\) of the linear stochastic system satisfies
\[
\begin{aligned}
 dU_1(t)&=-\gamma_1U_1(t)\,dt+\sqrt{2D_1}\,dW_1(t),\\
 dU_2(t)&=(-\gamma_1U_1(t)-\gamma_2U_2(t))\,dt+\sqrt{2D_2}\,dW_2(t).
\end{aligned}
\]
Its velocity observable and displacement over a stationary window of duration \(t\) are
\[
V_t=\gamma_1U_1(t)+\gamma_2U_2(t),\qquad X_t=\int_0^tV_s\,ds.
\]
Expectations refer to the stationary law of the internal coordinates. Thus \(M(0)=0\) and \(M(t)>0\) for \(t>0\). "Subdiffusive local slope" means the **pointwise derivative criterion** \(\nu(t)<1\), not a finite-window regression exponent or global asymptotic anomalous diffusion. The motion is asymptotically Fickian with \(M(t)\sim2D_2t\) for every admissible parameter tuple. No claim is made for reversed or coincident relaxation rates, nonstationary internal initialization, or non-Gaussian forcing.

## Proof

**1. Exact covariance and positivity at zero lag.** The drift matrix of the internal system is lower triangular with strictly negative eigenvalues, so it admits a unique nondegenerate stationary Gaussian law. A Fourier transfer-function calculation for \(V\) gives the spectral density
\[
S_V(\omega)=\frac{2D_1\gamma_1^2\omega^2}{(\omega^2+\gamma_1^2)(\omega^2+\gamma_2^2)}+\frac{2D_2\gamma_2^2}{\omega^2+\gamma_2^2}.
\]
Partial fractions and inverse Fourier transformation yield, for \(t\ge0\),
\[
C(t)=Ae^{-\gamma_1t}+Be^{-\gamma_2t},\quad
A=\frac{D_1\gamma_1^3}{\gamma_1^2-\gamma_2^2}>0,\quad
B=\gamma_2\left(D_2-\frac{D_1\gamma_1^2}{\gamma_1^2-\gamma_2^2}\right).
\]
The independent source of the model's two-exponential covariance is Voulgarakis (2023), Eq. (15); the explicit formula and the entire MSD are prior results and are not claimed as new. In particular,
\[
C(0)=\frac{D_1\gamma_1^2}{\gamma_1+\gamma_2}+D_2\gamma_2>0,\quad
\int_0^\infty C(s)\,ds=\frac A{\gamma_1}+\frac B{\gamma_2}=D_2.
\]
The slow coefficient satisfies \(B\ge0\) if and only if \(d\le1-q^2\). In this case \(C(t)>0\) at every finite lag. Otherwise write
\[
C(t)=e^{-\gamma_2t}\bigl(B+Ae^{-(\gamma_1-\gamma_2)t}\bigr).
\]
The expression in parentheses decreases strictly from \(C(0)>0\) to \(B<0\), giving precisely one zero,
\[
t_C=\frac{1}{\gamma_1-\gamma_2}\log\!\left(\frac{d}{q(d-1+q^2)}\right)>0.
\]
The sign of \(C\) is positive before and negative after \(t_C\).

**2. Exact running diffusivity and its unique maximum.** Stationarity of \(V\) and Fubini's theorem give
\[
M(t)=2\int_0^t(t-s)C(s)\,ds
=2A\left(\frac{t}{\gamma_1}-\frac{1-e^{-\gamma_1t}}{\gamma_1^2}\right)
+2B\left(\frac{t}{\gamma_2}-\frac{1-e^{-\gamma_2t}}{\gamma_2^2}\right).
\]
It follows that \(M''(t)=2C(t)\), \(J(t)=\int_0^tC(s)\,ds\), and \(J(t)\to D_2\) as \(t\to\infty\). If \(C>0\), then \(J\) is strictly increasing. If \(C\) changes sign once at \(t_C\), then \(J\) increases before that time and decreases afterwards, with a unique strict global maximum. Since the integral of the negative tail is negative,
\[
J(t_C)-D_2=-\int_{t_C}^\infty C(s)\,ds
=(-B)e^{-\gamma_2t_C}\left(\frac1{\gamma_2}-\frac1{\gamma_1}\right)>0.
\]
In either case \(J(t)>0\) for every \(t>0\), which also proves \(\nu(t)>0\).

**3. The global sign criterion for the local MSD exponent.** Define
\[
H(t)=tM'(t)-M(t)=2\int_0^t sC(s)\,ds.
\]
Since \(M(t)>0\), the sign of \(\nu(t)-1\) is precisely the sign of \(H(t)\). Moreover, \(H(0)=0\), \(H'(t)=2tC(t)\), and the exact signed first covariance moment is
\[
\lim_{t\to\infty}H(t)
=2\left(\frac A{\gamma_1^2}+\frac B{\gamma_2^2}\right)
=\frac{2D_2}{\gamma_2}\left(1-\frac{d}{1+q}\right).
\]
When \(C(t)>0\), \(H(t)>0\) for positive \(t\). When \(C\) changes sign, \(H\) strictly increases on \((0,t_C)\), reaches its unique maximum at \(t_C\), and strictly decreases on \((t_C,\infty)\). If its limit is nonnegative, its strictly decreasing tail cannot reach zero at any *finite* time: hence \(H(t)>0\) throughout. If its limit is negative, the intermediate value theorem and strict decrease yield exactly one zero \(t_*>t_C\), with the claimed signs on either side. The limiting-sign threshold is \(d=1+q\), strictly larger than the autocorrelation threshold \(1-q^2\). This proves every global sign and uniqueness assertion without extrapolating from numerical samples.

**4. Sharp terminal asymptotics.** As \(t\to\infty\), \(M(t)\sim2D_2t\). If \(d\ne1+q\), the nonzero limit of \(H\) in Step 3 yields \(\nu(t)-1\sim[1-d/(1+q)]/(\gamma_2t)\). At \(d=1+q\), this limit vanishes, but the negative slow mode remains: \(B=-D_2\gamma_2q/(1-q)<0\). Therefore
\[
H(t)=-2\int_t^\infty sC(s)\,ds
\sim\frac{2(-B)t}{\gamma_2}e^{-\gamma_2t}.
\]
Dividing by \(M(t)\sim2D_2t\) proves \(\nu(t)-1\sim[q/(1-q)]e^{-\gamma_2t}\). All asymptotics are for fixed admissible parameter values, with \(t\to\infty\).

## Verification

The standalone file `verify.py` independently reconstructs the stationary Gaussian covariance from the continuous Lyapunov equation and compares \(C(t)\) with the matrix-exponential covariance over five rate combinations and seven diffusivity-ratio regimes, including both boundaries. It also checks the Green–Kubo identity, the first covariance moment, the analytic relation \(H=tM'-M\), the derivative \(H'=2tC\), the unique-crossing bracket and running-diffusivity overshoot, and the cancellation-critical prefactor using high-precision arithmetic. Execute from the extracted package directory with `python verify.py`. The tests passed on a Python environment with NumPy, SciPy, SymPy, and mpmath. The proof, not the finite checks, establishes the conclusions for all positive parameters.

For an illustrative nontrivial gap, take \(\gamma_1=1\), \(\gamma_2=1/2\), and \(D_1=D_2=1\). Then \(q=1/2\), \(d=1\), and \(C\) crosses zero at \(t_C=2\log8\), yet \(\nu(t)>1\) for every \(t>0\). At \(D_1=1.8\), \(D_2=1\) with the same rates, the two crossings occur at approximately \(t_C=2.4643\) and \(t_*=6.7318\), illustrating that the local-slope transition is later.

## Relationship to prior work

Voulgarakis (2023) introduced the hierarchical Langevin/OU model and derived its full two-exponential velocity autocorrelation [Eq. (15)] and complete stationary-internal-initialization MSD [Eq. (16)]. Its text acknowledges that the autocorrelation may become negative and gives examples of transient subdiffusion; both formulas are prior work. Wang and Voulgarakis (2024), especially Sec. 3.2, analyze and illustrate ballistic-to-anomalous-to-Fickian profiles and describe the diffusivity ordering \(D_2<D_1\) as a qualitative criterion for transient subdiffusion. The new claim is **not** another covariance or MSD formula. It is the simultaneous sharp, all-parameter classification of (i) negative velocity memory, (ii) overshooting finite-window diffusivity, and (iii) an exact instantaneous logarithmic MSD slope below one; it also proves unique crossings and the exceptional exponential cancellation at \(d=1+q\). The source's qualitative finite-range fitted exponent is not automatically equivalent to the pointwise criterion used here. The distinction is measurable: \(D_2<D_1\) alone is insufficient for \(\nu(t)<1\) anywhere at finite rate separation; one needs \(D_1/D_2>1+\gamma_2/\gamma_1\).

The formulas in the two cited studies logically contain enough information to *derive* the classification, making the closeness of this result to known equations an important novelty limitation. The relevant primary-text inspections and research-index comparisons did not identify an explicit global sign theorem with these two distinct thresholds, but lack of an indexed match does not establish publication priority. All physical modeling, stationary OU covariance, and the general MSD representation are credited to the prior literature.

## Limitations

The process has Gaussian internal noise and stationary initial internal coordinates; the result is not about non-Gaussian transport distributions. It does not give a closed elementary formula for the unique \(t_*\), only its exact implicit characterization and proof of uniqueness. It does not analyze \(\gamma_1\le\gamma_2\), the multilevel case \(n\ge3\), observation-window fitted exponents, or finite-sample statistical performance. The local exponent tends to one in all cases; the post-transition \(\nu<1\) is a finite-time sign property, not an asymptotically subdiffusive power law. Exact prior covariance and MSD formulas are acknowledged, and wider equivalent treatments cannot be excluded without independent literature review.

## References

1. N. K. Voulgarakis, “Multilayered noise model for transport in complex environments,” *Physical Review E* **108**, 064105 (published 4 December 2023). https://doi.org/10.1103/PhysRevE.108.064105 . Lawful accepted manuscript: https://link.aps.org/accepted/10.1103/PhysRevE.108.064105 .
2. J. Wang and N. K. Voulgarakis, “Hierarchically Coupled Ornstein–Uhlenbeck Processes for Transient Anomalous Diffusion,” *Physics* **6** (2024), 645–658 (published 24 April 2024). https://doi.org/10.3390/physics6020042 . Full text: https://www.mdpi.com/2624-8174/6/2/42 .
