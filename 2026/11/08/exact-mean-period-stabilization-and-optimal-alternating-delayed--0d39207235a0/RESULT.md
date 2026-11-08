# Exact mean-period stabilization and optimal alternating delayed-sample control

## Finding

For the one-sample-lag zero-order-hold feedback loop defined below, positive alternating sampling intervals admit an exact global stability classification and a unique fastest asymptotic period-two schedule at every normalized mean \(1\le m<3/2\). With dimensionless interval lengths \(a,b>0\), mean \(m=(a+b)/2\), and product \(p=ab\), the closed loop is exponentially stable precisely when

\[
p<1,\qquad p>2m-2.
\]

Thus every positive pair is stable when \(m<1\); at \(m=1\), every unequal pair is stable while the equal pair is not; for \(1<m<3/2\), exactly the pairs with \(2m-2<ab<1\) are stable; and for \(m\ge3/2\), no positive alternating pair is stable. In particular, allowing exactly alternating intervals raises the supremal stable mean from \(1\) (constant sampling) to \(3/2\), a fifty-percent increase, with neither boundary mean attained by a stable schedule at its corresponding supremum.

For each fixed \(1\le m<3/2\), the unique optimal unordered pair of positive dimensionless intervals, when minimizing the spectral radius of the two-interval update, is

\[
\{a_*,b_*\}=\left\{m+\frac{\sqrt{4m-1}}2,\;m-\frac{\sqrt{4m-1}}2\right\}.
\]

The optimal two-update spectral radius is exactly

\[
\rho_* =m-\frac12<1.
\]

At this optimum, the two Floquet multipliers coalesce into the negative, algebraically double eigenvalue \(-\rho_*\), and the two-update matrix has a nontrivial Jordan block. This is an optimal **asymptotic Floquet spectral factor**; a uniform finite-epoch norm bound with exactly \(\rho_*^j\) and no polynomial prefactor is not asserted.

## Assumptions and scope

Fix a gain \(\kappa>0\) and a scalar integrator plant \(\dot x(t)=u(t)\). Let sampling instants satisfy \(t_{k+1}>t_k\), with \(\kappa(t_{2j+1}-t_{2j})=a\) and \(\kappa(t_{2j+2}-t_{2j+1})=b\) for all nonnegative integers \(j\). The controller holds the **previous** sample, not the sample just acquired:

\[
u(t)=-\kappa x(t_{k-1}),\qquad t_k\le t<t_{k+1}.
\]

The initial previous sample \(x(t_{-1})\) and current sample \(x(t_0)\) may be arbitrary real numbers; the numerical stability assertion is for all such initial pairs. The delay is one sampling index, not a fixed physical time duration. The controller uses no measurement noise, saturation, uncertainty, actuator dynamics, or interpolation; the two intervals repeat exactly. Exponential stability means decay of every trajectory at the sampling instants and, because the interval lengths are bounded, also between sampling instants.

## Proof

**1. Exact sampled dynamics.** Integrating the held input across the \(k\)-th interval and defining \(x_k=x(t_k)\) gives

\[
x_{k+1}=x_k-h_k x_{k-1},\qquad h_{2j}=a,\quad h_{2j+1}=b.
\]

The augmented state \(v_k=(x_k,x_{k-1})^{\mathsf T}\) evolves by \(v_{k+1}=M(h_k)v_k\), where

\[
M(h)=\begin{pmatrix}1&-h\\1&0\end{pmatrix}.
\]

The two-interval transition from each even sample to the next is

\[
F=M(b)M(a)=\begin{pmatrix}1-b&-a\\1&-a\end{pmatrix},\qquad
\operatorname{tr}F=1-a-b=1-2m,\quad \det F=ab=p.
\]

Its characteristic polynomial is

\[
P(\lambda)=\lambda^2-(1-2m)\lambda+p.
\]

Both eigenvalues have modulus below one if and only if the periodic recurrence is exponentially stable. Indeed \(F^j\to0\) at an exponential rate exactly under that spectral condition, and the odd-index states are images under the fixed matrix \(M(a)\). Interpolation between samples is affine and introduces no separate instability.

**2. Sharp stability criterion.** For the real quadratic \(\lambda^2-T\lambda+p\) with \(p>0\), the degree-two strict Jury conditions are \(p<1\), \(1-T+p>0\), and \(1+T+p>0\). Substituting \(T=1-2m\) yields

\[
p<1,\qquad 2m+p>0,\qquad 2-2m+p>0.
\]

The middle condition is automatic. Therefore stability is equivalent to \(2m-2<p<1\). For fixed \(m>0\), every positive pair with sum \(2m\) has \(0<p\le m^2\), and each \(p\) in this interval is attained by a pair of positive roots of \(z^2-2mz+p=0\). It follows at once that every pair is stable for \(m<1\); for \(m=1\), stability fails precisely at \(a=b=1\); for \(1<m<3/2\), precisely the stated product interval works; and at \(m\ge3/2\), the required inequalities \(p>2m-2\ge1\) and \(p<1\) contradict one another.

**3. Unique optimal spectral rate.** For any pair with fixed mean, the eigenvalues \(\lambda_1,\lambda_2\) obey \(\lambda_1+\lambda_2=1-2m\). Consequently

\[
\rho(F)=\max(|\lambda_1|,|\lambda_2|)\ge\frac{|\lambda_1+\lambda_2|}{2}=m-\frac12
\]

for \(m\ge1\). Equality forces both eigenvalues to equal the same real number \(-(m-1/2)\): the triangle inequalities can be equal only when their phases are identical and their magnitudes equal. Hence \(p=\lambda_1\lambda_2=(2m-1)^2/4\). Conversely, solving \(a+b=2m\) and this product gives the displayed \(a_*,b_*\), both positive because \(4m-1<4m^2\) for \(m>1/2\) except at \(m=1/2\). The resulting characteristic polynomial is \((\lambda+m-1/2)^2\), attaining the lower bound. The product and sum uniquely determine the unordered pair. As the upper right entry of \(F\) is \(-a_*\ne0\), this repeated-eigenvalue matrix is not scalar, hence it has a nontrivial Jordan block. Its powers still decay exponentially whenever \(m-1/2<1\), that is, \(m<3/2\).

**4. Comparison with equal spacing and an exact example.** For \(a=b=m\), the single-interval matrix has polynomial \(\mu^2-\mu+m\). At every \(m\ge1\) the two eigenvalues are complex conjugates of modulus \(\sqrt m\), so the two-interval spectral factor is \(m\ge1\). At the mean \(m=5/4\), the optimal alternating intervals are \((a,b)=(9/4,1/4)\), with double Floquet multiplier \(-3/4\) and asymptotic factor \(3/4\), while equal spacing yields a two-interval factor \(5/4\). Thus one schedule is exponentially stable and the other unstable at identical average sampling frequency. This establishes the sharp crossover and the claimed optimum.

## Verification

The standalone script `verify.py` uses SymPy to reconstruct \(F\), its characteristic polynomial, both Jury factors, the optimal pair, repeated eigenvalue, and the rational example. It additionally compares the exact Jury inequalities with directly computed Floquet eigenvalue magnitudes over a rational parameter grid and samples the claimed spectral lower bound. Its recorded output is in `verify_output.txt`. Invoke `python verify.py` with SymPy 1.14.0 (see `requirements.txt`). The analytic proof, not finite grid checks, establishes all real-parameter assertions. Particular numeric experiments are neither necessary nor sufficient to prove uniqueness or the sharp mean limit.

## Relationship to prior work

García, Aguirre and Suárez (2008) study sampled-data feedback with a **fixed physical delay** that is an integer multiple of a constant sampling period, including a companion-matrix stability analysis. Their assumptions do not determine a period-two variable-index-delay controller, its exact average-period frontier, or its optimized Floquet rate.

Berberich, Wildhagen, Hertneck and Allgöwer (2020), Wildhagen and coauthors (2021), and Vallarella and Haimovich (2022) study general nonuniform sampled-data stability, mostly with the **current** sampled state in the control action and bounds that hold for all sufficiently small intervals or classes of schedules. Their inspected statements do not supply a necessary-and-sufficient, fixed-average, two-periodic law for the previous-sample integrator model.

Jin, Wang and Wang (2022) explicitly advocate mixing short stable and long unstable sampling intervals to enlarge admissible averages. Thus the *qualitative idea* of stabilization by mixed intervals is established prior art, not claimed here. The distinct contribution claimed is the exact two-step lagged-control Schur region, the sharp \(3/2\) mean limit, and the unique optimal two-interval schedule. Only bibliographic and abstract material was accessible for that source; a potentially relevant special example in its inaccessible full text remains a precedence risk.

## Limitations

The result is limited to a scalar integrator and a one-index-delayed proportional hold with exactly two repeating positive intervals. It does not give robust stability under arbitrary jitter, random packet losses, fixed physical-time delays, plant dynamics, noisy measurements, or control saturation. Exponential stability is not monotonic decay within each interval, and the optimal defective Floquet matrix can display transient growth. The algebra itself is elementary; the mathematical content claimed is the complete sharp parameter classification and uniquely optimal schedule for this motivated delayed-sensing design. Similar sharp formulas could exist in unindexed or inaccessible control literature; novelty is not independently certified.

## References

1. F. R. García, B. Aguirre, R. Suárez, *Stabilization of Linear Sampled-Data Systems by a Time-Delay Feedback Control*, Mathematical Problems in Engineering (2008), DOI: https://doi.org/10.1155/2008/270518.
2. J. Berberich, S. Wildhagen, M. Hertneck, F. Allgöwer, *Data-driven analysis and control of continuous-time systems under aperiodic sampling*, first public arXiv posting November 18, 2020, https://arxiv.org/abs/2011.09221.
3. S. Wildhagen, J. Berberich, M. Hirche, F. Allgöwer, *Improved stability conditions for systems under aperiodic sampling: model- and data-based analysis*, first public arXiv posting March 26, 2021, https://arxiv.org/abs/2103.14353.
4. A. J. Vallarella, H. Haimovich, *On the stability of nonlinear sampled-data systems and their continuous-time limits*, first public arXiv posting February 21, 2022, https://arxiv.org/abs/2202.10549.
5. C.-L. Jin, Q.-G. Wang, R. Wang, *Exponential stability of sampled-data control systems with enhanced average sampling interval*, published online May 3, 2022, https://doi.org/10.1080/00207179.2022.2069051.
