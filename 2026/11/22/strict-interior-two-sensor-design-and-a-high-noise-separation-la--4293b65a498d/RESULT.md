# Strict interior two-sensor design and a high-noise separation law for an Ornstein–Uhlenbeck path

## Finding
Let \(X\) be a centered stationary real Gaussian process on \([0,1]\) with known covariance \(k_\alpha(s,t)=\exp(-\alpha|s-t|)\), where \(\alpha>0\). At freely chosen times \(0\le x\le y\le1\), observe \(Y_1=X(x)+\varepsilon_1\) and \(Y_2=X(y)+\varepsilon_2\), with independent \(N(0,\eta)\) errors and \(\eta>0\). Minimize the integrated conditional variance \(R_\eta(x,y)=\int_0^1\operatorname{Var}(X(s)\mid Y_1,Y_2)\,ds\).

**Theorem.** Every global minimizer, for every \(\alpha,\eta>0\), is of the form \((x,y)=(1/2-d,1/2+d)\) with \(0<d<1/2\). In particular no repeated time and neither endpoint is globally optimal. For each fixed \(\alpha>0\), the global minimizer is unique up to permuting the two observations whenever \(\eta\) is sufficiently large. Writing its half-separation as \(d_{\alpha,\eta}\), one has
\[
d_{\alpha,\eta}=\frac{e^\alpha-1}{2\alpha\eta}+O_\alpha(\eta^{-2}),
\qquad
R_\eta(1/2,1/2)-\min_{x,y}R_\eta(x,y)
=\frac{(1-e^{-\alpha})^2}{\alpha e^{-\alpha}\eta^3}+O_\alpha(\eta^{-4}).
\]
The second identity compares the best collocated pair (both at the midpoint) with the unrestricted optimum. The implied constants and sufficiently-large-noise cutoff may depend on fixed \(\alpha\).

## Assumptions and scope
The latent mean and covariance are known. The variance of \(X(s)\) is normalized to one; observation noises are independent of the path and each other, with the same variance \(\eta\). Both observations are allowed to occur at the same time but remain independent measurements there. The criterion integrates **pointwise path posterior variance** against Lebesgue measure, not posterior variance of the path integral. The design interval is exactly \([0,1]\). No limit is taken jointly in \(\alpha\) and \(\eta\).

## Proof
**1. Exact integrated information.** Put \(b=1+\eta\), \(x=c-d\), \(y=c+d\), \(0\le d\le1/2\), \(d\le c\le1-d\), \(r=e^{-2\alpha d}\), \(T=e^{-\alpha}\), and \(C=\cosh(2\alpha(c-1/2))\). The observation covariance is \(\left(\begin{smallmatrix}b&r\\r&b\end{smallmatrix}\right)\); it is positive definite since \(b>1\). Define \(M_{ij}=\int_0^1k_\alpha(s,t_i)k_\alpha(s,t_j)\,ds\), where \((t_1,t_2)=(x,y)\). Integrating each exponential over the intervals cut by the observation locations gives
\[
M_{11}+M_{22}=\frac2\alpha\bigl(1-TC\cosh(2\alpha d)\bigr),
\qquad M_{12}=r\left(2d+\frac1\alpha\right)-\frac{T}{\alpha}C.
\]
By Gaussian conditioning, \(R_\eta(x,y)=1-\mathcal I(c,d)\), where
\[
\mathcal I(c,d)=\frac{b(M_{11}+M_{22})-2rM_{12}}{b^2-r^2}.
\]
For fixed \(d\), the coefficient multiplying \(C\) in its numerator is \(-2T[b\cosh(2\alpha d)-r]/\alpha<0\). Because \(C\ge1\) with equality only at \(c=1/2\), **every** optimal pair is centered, including at collision \(d=0\).

**2. Exclude both separation boundaries for all positive noise.** Set \(t=2\alpha d\), so \(0\le t\le\alpha\), and retain \(r=e^{-t}\), \(T=e^{-\alpha}\). The centered information is
\[
\mathcal I_\eta(d)=\frac{2P(t)}{\alpha(b^2-r^2)},\qquad
P(t)=b(1-T\cosh t)-r^2(1+t)+Tr.
\]
Direct differentiation gives
\[
P'(t)=-bT\sinh t+r^2(1+2t)-Tr,
\quad
\frac{d\mathcal I_\eta}{dt}=
\frac{2H(t)}{\alpha(b^2-r^2)^2},
\quad H(t)=P'(t)(b^2-r^2)-2r^2P(t).
\]
At the collocated boundary, \(H(0)=(1-T)(b-1)^2>0\). Equivalently,
\[
\mathcal I_\eta'(0)=\frac{4(1-e^{-\alpha})}{(\eta+2)^2}>0,
\]
where the derivative is with respect to the half-separation \(d\). At the opposite boundary \(t=\alpha\), where observations are precisely at \(0\) and \(1\), a cancellation yields
\[
H(\alpha)=\frac b2\bigl[-(1-T^2)(b^2+T^2)+4\alpha T^2b\bigr]<0.
\]
Indeed \(b+T^2/b\ge1+T^2\), whereas \((1-T^2)(1+T^2)>4\alpha T^2\) follows from \(\sinh(2\alpha)>2\alpha\). Consequently \(\mathcal I_\eta'(1/2)<0\). Compactness gives an optimum, and the two strict inward derivatives exclude \(d=0\) and \(d=1/2\). Combined with the centering argument this proves the first, all-noise assertion.

**3. Uniqueness and location at high noise.** Write \(\epsilon=b^{-1}\). For \(0\le d\le1/2\), put \(F(d,\epsilon)=\mathcal I_\eta(d)/\epsilon\). Its explicit formula is
\[
F(d,\epsilon)=\frac2\alpha\,
\frac{1-T\cosh(2\alpha d)-\epsilon[r^2(1+2\alpha d)-Tr]}{1-\epsilon^2r^2}.
\]
It is smooth on a neighborhood of \([0,1/2]\times\{0\}\), and \(F(d,0)=2[1-T\cosh(2\alpha d)]/\alpha\). The derivative \(\partial_dF(d,0)=-4T\sinh(2\alpha d)\) is strictly negative for \(d>0\), while \(\partial_d^2F(0,0)=-8\alpha T<0\). For any sufficiently small fixed \(\delta>0\), uniform continuity makes \(\partial_dF<0\) on \([\delta,1/2]\) and \(\partial_d^2F<0\) on \([0,\delta]\), for all sufficiently small positive \(\epsilon\). The exact derivative at the collocated boundary is \(\partial_dF(0,\epsilon)=4(1-T)\epsilon/(1+\epsilon)^2>0\). Thus there is exactly one critical point and global maximizer \(d(\epsilon)\) for all sufficiently small positive \(\epsilon\). The implicit function theorem at \((0,0)\) yields
\[
d(\epsilon)=\frac{1-T}{2\alpha T}\,\epsilon+O_\alpha(\epsilon^2).
\]
Finally, Taylor's theorem around \(d=0\), using \(\partial_dF(0,\epsilon)=4(1-T)\epsilon+O(\epsilon^2)\) and \(\partial_d^2F(0,0)=-8\alpha T\), gives
\[
\mathcal I_\eta(d(\epsilon))-\mathcal I_\eta(0)
=\frac{(1-T)^2}{\alpha T}\epsilon^3+O_\alpha(\epsilon^4).
\]
Since \(\epsilon=(1+\eta)^{-1}\), the stated results follow. All steps apply to arbitrary fixed \(\alpha>0\) and all positive \(\eta\) where claimed.

## Verification
Run `python verify.py` with Python 3, `sympy` and `mpmath`. It checks the polynomial identities for both boundary derivatives, compares the closed information expression to independent numerical quadrature for four designs (including coincident observations), tests inward derivatives at nine parameter pairs, and checks leading high-noise constants at three correlation lengths. The script passes 42 checks. The symbolic identities and limiting argument in the proof, not numerical sampling or the script, establish the statements for the continuum of parameters.

## Relationship to prior work
Ji and Müller (2016, arXiv:1604.05375, Sections 1–2 and 8) derive the general integrated trajectory-recovery criterion with noisy Gaussian measurements; their formula (10) is the parent optimization objective, not the explicit stationary-exponential two-point optimizer or its separation/regret asymptotics. Baldi Antognini and Zagoraiou (2010) establish exact design results for exponential-covariance ordinary Kriging in computer experiments, in a different no-measurement-noise setting; their full article could not be checked here. Mukherjee (2001) establishes exact path-design conditions including Ornstein–Uhlenbeck processes using direct process observations; only the dissertation catalog abstract was accessible, so stronger coverage cannot be ruled out from the available text. Baran, Sikolya and Stehlík (2013) study prediction designs for two-dimensional Ornstein–Uhlenbeck sheets on monotonic sets. The separate literature on posterior **integral** variance for exponential kernels concerns a different functional of the covariance, and does not directly imply integrated **pointwise** posterior variance results. Similarities to previously studied nonstationary Brownian sensor problems concern the optimization framework, not the stationary kernel's midpoint rigidity or its stated constants.

## Limitations
Uniqueness of the optimal positive separation is proved only for sufficiently large \(\eta\); no uniqueness claim is made at arbitrary finite positive noise. The theorem does not address unknown mean/covariance parameters, correlated or unequal measurement errors, other kernels, or more than two observations. The uninspected full texts of a closely related 2010 Kriging paper and a 2001 stochastic-process path-design dissertation, and potentially unindexed exact results, are residual publication-priority risks. Self-review is not independent mathematical validation.

## References
- H. Ji and H.-G. Müller, *Optimal Designs for Longitudinal and Functional Data*, arXiv:1604.05375v1 (first posted 2016-04-18), https://arxiv.org/html/1604.05375v1.
- A. Baldi Antognini and M. Zagoraiou, *Exact optimal designs for computer experiments via Kriging metamodelling*, Journal of Statistical Planning and Inference 140 (2010), 2607–2617, https://doi.org/10.1016/j.jspi.2010.03.027.
- S. Baran, K. Sikolya and M. Stehlík, *On the optimal designs for the prediction of Ornstein–Uhlenbeck sheets*, Statistics & Probability Letters 83 (2013), 1580–1587, https://doi.org/10.1016/j.spl.2013.03.003.
- S. Baran and M. Stehlík, *Optimal designs for parameters of shifted Ornstein–Uhlenbeck sheets measured on monotonic sets*, arXiv:1312.0099 (first posted 2013-11-30), https://arxiv.org/abs/1312.0099.
- B. Mukherjee, *Optimal designs for estimating the path of a stochastic process*, Ph.D. dissertation, Purdue University (2001), https://docs.lib.purdue.edu/dissertations/AAI3043760/.
