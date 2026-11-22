# A sharp endpoint-to-interior transition in two-sign Ornstein–Uhlenbeck quadrature

## Finding

For a stationary centered unit-variance Ornstein–Uhlenbeck Gaussian process on the unit interval with covariance \(K_\lambda(u,v)=e^{-\lambda|u-v|}\), \(\lambda>0\), the best estimator of \(I=\int_0^1 X(u)\,du\) from the two zero-threshold sign observations \(S_s=\operatorname{sgn}X(s)\) and \(S_t=\operatorname{sgn}X(t)\) has an explicit mean-square risk for every \(0\le s\le t\le1\). Among all fixed site pairs, **the unique optimum (up to site order) is symmetric about the midpoint** and undergoes a sharp transition between endpoint and interior sensing:

\[
\lambda_c=0.0600892783080022953\ldots,
\qquad
\frac{e^{-\lambda_c}}{\sqrt{1-e^{-2\lambda_c}}\,[\pi/2+\arcsin(e^{-\lambda_c})]}=1.
\]

For \(0<\lambda\le\lambda_c\), the unique optimal pair is \((s,t)=(0,1)\). For \(\lambda>\lambda_c\), the unique optimal pair is \((s,t)=((1-d_*)/2,(1+d_*)/2)\), where \(d_*\in(0,1)\) is the unique solution of

\[
\frac{e^{-\lambda/2}\sinh(\lambda d/2)}{1-e^{-\lambda/2}\cosh(\lambda d/2)}
=
\frac{e^{-\lambda d}}{\sqrt{1-e^{-2\lambda d}}[\pi/2+\arcsin(e^{-\lambda d})]}.
\]

In the short-correlation limit \(\lambda\to\infty\),
\[
d_*(\lambda)=\frac13+\frac{2\log(4/\pi)}{3\lambda}+o(\lambda^{-1}),
\]
so the interior nodes converge to the trisection sites. The design transition is specific to fixed **sign-only**, zero-threshold readings; it does not claim optimality among arbitrary binary encoders or thresholds.

## Assumptions and scope

The process is centered, Gaussian, stationary, with known correlation rate \(\lambda>0\), known variance one, and no observation noise beyond the binary sign quantization. Exactly two predetermined observation times are selected in the closed interval, independently of the sample path. The decoder may be any measurable real-valued function of the two bits, and its loss is \(\mathbb E[(I-\widehat I)^2]\). Coincident sites and endpoints are allowed. Observation order has no effect. For all \(s<t\), define
\[
k_\lambda(u)=\frac{2-e^{-\lambda u}-e^{-\lambda(1-u)}}{\lambda},\qquad r=e^{-\lambda(t-s)},\qquad c=\frac2\pi\arcsin r.
\]
The prior variance is \(V_\lambda=2(\lambda-1+e^{-\lambda})/\lambda^2\). The optimal decoder and its risk are exactly
\[
\widehat I_{s,t}=\sqrt{\frac2\pi}\,
\frac{(k_\lambda(s)-c k_\lambda(t))S_s+(k_\lambda(t)-c k_\lambda(s))S_t}{1-c^2},
\]
\[
R_\lambda(s,t)=V_\lambda-\frac2\pi\,
\frac{k_\lambda(s)^2+k_\lambda(t)^2-2c k_\lambda(s)k_\lambda(t)}{1-c^2}.
\]
For coincident sites the single-bit limit is \(R_\lambda(s,s)=V_\lambda-(2/\pi)k_\lambda(s)^2\).

## Proof

**1. Exact conditional estimator.** Direct integration of the exponential covariance kernel gives \(\operatorname{Cov}(I,X(u))=k_\lambda(u)\) and \(\operatorname{Var}(I)=V_\lambda\). Gaussian regression and the standard half-normal moment give \(\mathbb E[I S_u]=\sqrt{2/\pi}\,k_\lambda(u)\). The Gaussian sign arcsine identity gives \(\mathbb E[S_s S_t]=c\). Since simultaneously reversing both signs reverses the conditional expectation of the centered jointly Gaussian integral, \(\mathbb E[I\mid S_s,S_t]\) is odd under this flip; the real vector space of such functions on four sign combinations is spanned by \(S_s,S_t\). All four patterns have positive probability when \(s<t\). Solving the normal equations with sign covariance matrix \(\left(\begin{smallmatrix}1&c\\c&1\end{smallmatrix}\right)\) gives the displayed decoder. The orthogonal-projection variance identity proves the displayed exact risk for *every measurable decoder*.

**2. Every fixed separation has a strictly optimal center.** Fix \(d=t-s\in(0,1]\), put \(w=\lambda d/2\), \(b=e^{-\lambda/2}\), \(h=(s+t)/2-1/2\), \(z=\cosh(\lambda h)\), and \(c=(2/\pi)\arcsin(e^{-2w})\). Omitting the common positive \(2/\pi\) factor, the explained variance \(J\) is
\[
J=\frac8{\lambda^2}\left[\frac{(1-bz\cosh w)^2}{1+c}+\frac{b^2(z^2-1)\sinh^2w}{1-c}\right].
\]
Its derivative with respect to \(z\) has the sign of \(bz(\cosh 2w-c)-(1-c)\cosh w\). Feasibility gives \(bz\le e^{-w}\), and the exact identity
\[
(1-c)\cosh w-e^{-w}(\cosh 2w-c)=(e^{-2w}-c)\sinh w>0
\]
holds because \((2/\pi)\arcsin r<r\) for \(0<r<1\). Thus \(J\) strictly decreases as \(z\) increases. Its unique maximum at fixed positive \(d\) has \(h=0\), i.e. reflection-symmetric nodes. Coincident readings cannot be optimal, as the next step proves strict improvement for sufficiently small positive separation.

**3. Strict one-dimensional shape and sharp threshold.** At the symmetric pair the explained variance is
\[
G_\lambda(d)=\frac4\pi\frac{k_\lambda((1-d)/2)^2}{1+c(d)},\qquad c(d)=\frac2\pi\arcsin(e^{-\lambda d}),\qquad 0<d\le1.
\]
Its logarithmic derivative is \(\lambda(B_\lambda(d)-A_\lambda(d))\), where
\[
A_\lambda(d)=\frac{e^{-\lambda/2}\sinh(\lambda d/2)}{1-e^{-\lambda/2}\cosh(\lambda d/2)},\quad
B_\lambda(d)=\frac{e^{-\lambda d}}{\sqrt{1-e^{-2\lambda d}}\,[\pi/2+\arcsin(e^{-\lambda d})]}.
\]
The function \(A_\lambda\) strictly increases on \([0,1]\), with derivative proportional to \(\cosh(\lambda d/2)-e^{-\lambda/2}>0\), and \(A_\lambda(1)=1\). The function \(B_\lambda\) strictly decreases with \(d\): for \(r\in(0,1)\), differentiation of its logarithm in \(r\) gives
\[
\frac{1}{r(1-r^2)}-\frac{1}{\sqrt{1-r^2}(\pi/2+\arcsin r)}>0,
\]
since \(\pi/2+\arcsin r>r\sqrt{1-r^2}\). Also \(B_\lambda(d)\to+\infty\) as \(d\downarrow0\). Therefore either \(G_\lambda\) increases strictly through \(d=1\), or it increases to a single strict interior maximum and then decreases. The boundary comparison is \(B_\lambda(1)\mathrel{\gtreqless}1\). As \(\lambda\) increases, \(r=e^{-\lambda}\) decreases and the positive function of \(r\) defining \(B_\lambda(1)\) strictly increases with \(r\); the boundary comparison crosses once from above to below, at exactly \(\lambda_c\) specified in the finding. The derivative remains strictly positive for \(d<1\) at equality. This proves existence and uniqueness globally, including the endpoints and the repeated-site case.

**4. Short-correlation asymptotic.** At the unique interior stationary point, the two sides of the stationarity equation are asymptotic to \(\tfrac12e^{-\lambda(1-d)/2}\) and \((2/\pi)e^{-\lambda d}\) whenever \(d\) stays bounded away from zero and one. Their comparison first forces \(d\to1/3\). Taking logarithms with that limit gives \(\lambda(3d-1)/2=\log(4/\pi)+o(1)\), yielding the expansion in the finding. This is an analytic asymptotic, not a fit to numerical root searches.

## Verification

Run `python verify_ou_sign.py` after installing the two dependencies listed in `requirements.txt`. The standalone script passed 4,967 assertions: exact symbolic simplification of the crucial centered-pair inequality, Gaussian orthant-sign moments, independent integrated-covariance numerical checks, thousands of asymmetric-placement comparisons, monotonicity/unique-root checks at thirteen correlation rates, and the short-correlation expansion. For illustration, \(\lambda=0.03\) gives optimal sites \((0,1)\); at \(\lambda=0.1\) they are approximately \((0.07323308783,0.92676691217)\); at \(\lambda=1\) they are approximately \((0.27432361208,0.72567638792)\). The infinite-domain and global-uniqueness claims are proved analytically above; a finite verification suite alone would not establish them.

## Relationship to prior work

Bania and Baranowski (2017) develop filtering of OU states from quantized discrete-time observations, including an approximate nonlinear filter, but do not establish this exact two-fixed-sign-bit *integral* risk and optimal location transition. Pronzato and Zhigljavsky (2018), Section 2.2 and Appendix B, present general **full-valued** Gaussian-process Bayesian quadrature, not optimized signs. Fesl, Koller and Utschick (2022), Sections III–IV and appendices, analyze one-bit Gaussian conditional means and pilot designs; the odd conditional-mean projection and arcsine identities are established background, not asserted as new here. Bhadane and Wagner (2022) study arbitrary one-bit quantization of Hilbert-space sources, with a different observation budget and encoder class. A published full-value OU quadrature specialization [5] proves strictly interior full-value two-node optima for every positive correlation rate. The endpoint optimum for small correlation rates in this two-sign theorem is therefore a genuine comparison of observation models, but the general Gaussian sign regression formulas themselves are not new.

## Limitations

Only two predetermined signs at exactly zero thresholds are permitted. There is no theorem here about optimally chosen nonzero thresholds, arbitrary two-bit encoders of paths, noisy bits, adaptive observation timing, unknown covariance parameters, or estimating an entire trajectory. The proof is specific to known stationary exponential covariance in one time dimension. Historical priority has not been independently confirmed, and an equivalent formulation in older quantized-filtering or optimal-design literature cannot be ruled out completely. The source comparison does not claim comprehensive exhaustiveness.

## References

1. P. Bania and J. Baranowski, *Approximation of optimal filter for Ornstein–Uhlenbeck process with quantised discrete-time observation*, International Journal of Control (accepted author version online 2017-01-20), DOI: 10.1080/00207179.2017.1282627; https://www.researchgate.net/publication/312672801_Approximation_of_optimal_filter_for_Ornstein-Uhlenbeck_process_with_quantised_discrete-time_observation.
2. L. Pronzato and A. Zhigljavsky, *Bayesian quadrature and energy minimization for space-filling design*, arXiv:1808.10722v1 (2018-08-31), https://arxiv.org/abs/1808.10722.
3. B. Fesl, M. Koller and W. Utschick, *On the Mean Square Error Optimal Estimator in One-Bit Quantized Systems*, arXiv:2212.04470 (first public 2022-12-08), https://arxiv.org/abs/2212.04470.
4. A. Bhadane and A. B. Wagner, *On One-Bit Quantization*, arXiv:2202.05292 (2022), https://arxiv.org/abs/2202.05292.
5. *Exact optimal nodes and stratification penalty for Ornstein–Uhlenbeck Bayesian quadrature*, published full-value comparison, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-exact-optimal-nodes-and-stratification-penalty-for-ornstein-uhle--971795799fba.
