# A sharp endpoint-to-interior transition in two-sign Ornstein–Uhlenbeck quadrature

Let \(X\) be a centered stationary Gaussian process with covariance \(K_\lambda(u,v)=e^{-\lambda|u-v|}\), \(\lambda>0\), on \([0,1]\). We estimate \(I=\int_0^1 X(u)\,du\) from two predetermined zero-threshold readings \(S_s=\operatorname{sgn} X(s)\), \(S_t=\operatorname{sgn} X(t)\), with \(0\le s\le t\le1\), under squared loss. The decoder may be any measurable function of the two bits. Coincident readings are permitted.

## Exact risk and optimal sites

For \(s<t\) let
\[
k_\lambda(u)=\frac{2-e^{-\lambda u}-e^{-\lambda(1-u)}}{\lambda},\qquad
c=\frac2\pi\arcsin(e^{-\lambda(t-s)}),\qquad
V_\lambda=\frac{2(\lambda-1+e^{-\lambda})}{\lambda^2}.
\]
The conditional-mean decoder and its risk are
\[
\widehat I_{s,t}=\sqrt{\frac2\pi}\,
\frac{(k_\lambda(s)-c k_\lambda(t))S_s+(k_\lambda(t)-c k_\lambda(s))S_t}{1-c^2},
\quad
R_\lambda(s,t)=V_\lambda-\frac2\pi\frac{k_\lambda(s)^2+k_\lambda(t)^2-2c k_\lambda(s)k_\lambda(t)}{1-c^2}.
\]
For coincident sites the decoder is \(\sqrt{2/\pi}\,k_\lambda(s)S_s\) and the risk is \(V_\lambda-(2/\pi)k_\lambda(s)^2\).

There is a unique optimal pair up to order. Define \(\lambda_c=0.0600892783080023\ldots\) by
\[
\frac{e^{-\lambda_c}}{\sqrt{1-e^{-2\lambda_c}}\,\bigl(\pi/2+\arcsin(e^{-\lambda_c})\bigr)}=1.
\]
For \(0<\lambda\le\lambda_c\) the optimum is \((0,1)\). For \(\lambda>\lambda_c\) it is \(((1-d_*)/2,(1+d_*)/2)\), where the unique \(d_*\in(0,1)\) satisfies
\[
\frac{e^{-\lambda/2}\sinh(\lambda d_*/2)}{1-e^{-\lambda/2}\cosh(\lambda d_*/2)}
=\frac{e^{-\lambda d_*}}{\sqrt{1-e^{-2\lambda d_*}}\,\bigl(\pi/2+\arcsin(e^{-\lambda d_*})\bigr)}.
\]
In the short-correlation regime,
\[
d_*(\lambda)=\frac13+\frac{2\log(4/\pi)}{3\lambda}+o(\lambda^{-1})\qquad(\lambda\to\infty).
\]

## Proof

**Decoder.** Integrating the kernel once and twice gives \(k_\lambda(u)=\operatorname{Cov}(I,X(u))\) and \(V_\lambda=\operatorname{Var}(I)\). Gaussian regression and the absolute first moment of a standard normal give \(\mathbb E[I S_u]=\sqrt{2/\pi}\, k_\lambda(u)\). The Gaussian arcsine identity gives \(\mathbb E[S_s S_t]=c\). For distinct sites all four sign patterns have positive probability, and simultaneous reversal of both signs reverses the conditional mean. The space of functions odd under this flip is spanned by \(S_s,S_t\). Inverting their covariance matrix, with ones on the diagonal and \(c\) off-diagonal, gives the decoder, and orthogonal projection gives its risk. Coincidence reduces to the one-sign projection.

**Centering at fixed positive gap.** Let \(d=t-s>0\), \(w=\lambda d/2\), \(b=e^{-\lambda/2}\), \(h=(s+t)/2-1/2\), and \(z=\cosh(\lambda h)\). The variance explained by the two readings, divided by \(2/\pi\), equals
\[
J(z)=\frac8{\lambda^2}\left[\frac{(1-bz\cosh w)^2}{1+c}+\frac{b^2(z^2-1)\sinh^2w}{1-c}\right].
\]
In fact the numerator quadratic of the risk splits along the sum and difference of the weights, with denominators \(2(1+c)\) and \(2(1-c)\). The sign of \(J'(z)\) is the sign of \(bz(\cosh 2w-c)-(1-c)\cosh w\). Feasibility gives \(|h|\le(1-d)/2\), hence \(bz\le e^{-w}\). Since \(\arcsin r\) lies strictly below the chord \(\pi r/2\) on \(0<r<1\), we have \(c<e^{-2w}\), and
\[
(1-c)\cosh w-e^{-w}(\cosh 2w-c)=(e^{-2w}-c)\sinh w>0.
\]
The derivative is strictly negative and \(z=1\) occurs only at \(h=0\). Thus centering is strictly optimal at each positive gap (at \(d=1\) it is the only feasible placement).

**The gap and transition.** The variance explained at the centered sites is
\[
G_\lambda(d)=\frac4\pi\frac{k_\lambda((1-d)/2)^2}{1+c(d)},\qquad c(d)=\frac2\pi\arcsin(e^{-\lambda d}).
\]
Its logarithmic derivative is \(\lambda(B_\lambda(d)-A_\lambda(d))\) for
\[
A_\lambda(d)=\frac{b\sinh(\lambda d/2)}{1-b\cosh(\lambda d/2)},\qquad
B_\lambda(d)=\frac{r_d}{\sqrt{1-r_d^2}\,\bigl(\pi/2+\arcsin r_d\bigr)},\qquad r_d=e^{-\lambda d}.
\]
Indeed, the contribution from the denominator of \(G_\lambda\) is \(-c'(d)/(1+c(d))=\lambda B_\lambda(d)\). The derivative of \(A_\lambda\) is strictly positive, with sign given by \(\cosh(\lambda d/2)-b>0\); \(A_\lambda(0)=0\) and \(A_\lambda(1)=1\). The logarithmic derivative of the positive function defining \(B_\lambda\) with respect to \(r_d\) is
\[
\frac1{r_d(1-r_d^2)}-\frac1{\sqrt{1-r_d^2}\,\bigl(\pi/2+\arcsin r_d\bigr)}>0,
\]
because \(\pi/2+\arcsin r_d> r_d\sqrt{1-r_d^2}\). Thus \(B_\lambda\) strictly decreases with \(d\) and diverges as \(d\downarrow0\). The continuous limit of \(G_\lambda(d)\) there is the explained variance of one midpoint sign, which is the best coincident reading because \(k_\lambda(u)\) is maximal at \(1/2\). This limit is strictly improved by taking a sufficiently small positive gap. The boundary comparison is \(B_\lambda(1)\) against \(1\): when \(B_\lambda(1)\ge1\), the score strictly increases for \(0<d<1\); otherwise it first increases and then decreases about its unique stationary point. As a function of \(\lambda\), \(B_\lambda(1)\) strictly decreases from infinity to zero. This proves the asserted transition and uniqueness, including equality.

**Short-correlation expansion.** Uniformly on closed subintervals of \((0,1)\),
\[
\frac{A_\lambda(d)}{B_\lambda(d)}=\frac{\pi}{4}e^{\lambda(3d-1)/2}(1+o(1)).
\]
For any fixed small \(\epsilon>0\), the ratio is eventually below one at \(1/3-\epsilon\) and above one at \(1/3+\epsilon\). Strict monotonicity brackets the root, so \(d_*\to1/3\). It then lies in a fixed closed interior subinterval, where the uniform estimate and taking logs give \(\lambda(3d_*-1)/2=\log(4/\pi)+o(1)\).

## Verification and scope

The accompanying `verify_ou_sign.py` uses the denominator product in its `g_func`, checks the centering identity and finite examples, and approximates the transition and stationary gap. Its dependencies are listed in `requirements.txt`. Examples of optimal locations are \((0,1)\) at \(\lambda=0.03\), approximately \((0.07323308783,0.92676691217)\) at \(\lambda=0.1\), and \((0.27432361208,0.72567638792)\) at \(\lambda=1\). The proof, not these checks, establishes the global quantifiers. The result is specific to fixed zero-threshold signs, with known covariance and no further noise; it does not optimize nonzero thresholds, arbitrary binary encodings, adaptive sites, or other functionals.

## Related work

Gaussian conditional-mean estimation and the one-bit arcsine formula are standard; see D. Fesl, M. Koller and W. Utschick, [*On the Mean Square Error Optimal Estimator in One-Bit Quantized Systems*](https://arxiv.org/abs/2212.04470). L. Pronzato and A. Zhigljavsky, [*Bayesian quadrature and energy minimization for space-filling design*](https://arxiv.org/abs/1808.10722), §2.2, treat full-value Gaussian-process quadrature; the [full-value OU comparison](https://github.com/Resultary/2026/blob/main/2026/11/8/SCOPE-exact-optimal-nodes-and-stratification-penalty-for-ornstein-uhle--971795799fba/RESULT.md) has strictly interior two-node optima for every positive correlation rate. P. Bania and J. Baranowski, [*Approximation of optimal filter for Ornstein–Uhlenbeck process with quantised discrete-time observation*](https://doi.org/10.1080/00207179.2017.1282627), address state filtering; A. Bhadane and A. B. Wagner, [*On One-Bit Quantization*](https://arxiv.org/abs/2202.05292), address a different encoder class. The contribution here is the global location theorem for this fixed observation rule, not the general Gaussian estimation identities. No exhaustive priority claim is made.
