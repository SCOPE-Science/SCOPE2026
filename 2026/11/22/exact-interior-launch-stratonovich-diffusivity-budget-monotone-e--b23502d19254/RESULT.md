# Strict launch-position gain and sharp endpoint laws for budgeted Stratonovich escape

## Finding

Consider a zero-drift one-dimensional Stratonovich diffusion on \([0,\ell]\), reflected at zero and killed at \(\ell\), launched at \(a\ell\) for \(0<a<1\). Fix the spatial mean diffusivity \(D_0>0\). If \(T_*(a)\) denotes the least mean absorption time at this budget, then the relative gain over homogeneous diffusion,
\[
\eta(a)=1-\frac{T_*(a)}{\ell^2(1-a^2)/(2D_0)},
\]
is strictly increasing on \((0,1)\), and
\[
\lim_{a\downarrow0}\frac{\eta(a)}{a^3}=\frac13,\qquad
\lim_{a\uparrow1}\frac{1-\eta(a)}{\sqrt{1-a}}=2.
\]
These laws quantify both the onset of the gain and the rate at which the optimal relative time tends to zero near the target.

## Assumptions and scope

Admit positive measurable \(D\) with \(\int_0^\ell D(x)\,dx=\ell D_0\) and \(\int_0^\ell D(x)^{-1/2}\,dx<\infty\). To specify transmission at jumps of \(D\), define the diffusion by the intrinsic coordinate \(s(x)=\int_0^x D(y)^{-1/2}dy\) and reflected, absorbed Brownian motion with generator \(\partial_s^2\). If only smooth positive profiles are admitted, the same statements hold for the infimum, which is not attained for an interior launch. A smooth transition between the two positive optimal levels, followed by normalization to the original budget, approximates the intrinsic integrals and therefore the minimum.

## Proof

Write \(b=1-a\) and \(z(y)=D(\ell y)/D_0\). The intrinsic-coordinate Poisson equation gives \(\mathbb E\tau=[s(\ell)^2-s(a\ell)^2]/2\). Thus the normalized objective is \(S_1S_2+S_2^2/2\), with \(S_1=\int_0^a z^{-1/2}\) and \(S_2=\int_a^1 z^{-1/2}\). For fixed interval means \(u,v\) with \(au+bv=1\), strict Jensen gives \(S_1\ge a/\sqrt u\), \(S_2\ge b/\sqrt v\), with equality only for each interval constant almost everywhere. The objective strictly increases in both positive arguments.

Set \(t=\sqrt{v/u}\). The reduced objective and its derivative are
\[
F(t)=(a+bt^2)\left(\frac{ab}{t}+\frac{b^2}{2t^2}\right),\qquad
F'(t)=\frac{ab}{t^3}(bt^3-at-b).
\]
The polynomial has one stationary point on \(t>0\), a minimum, and is negative at zero and one. Its unique positive zero is greater than one and yields the unique global minimizer. This is the one-dimensional Stratonovich specialization of the published stationarity equations; the reduction is included to make the gain proof self-contained. In particular, writing \(K=t^3+t-1\) gives \(a=(t^3-1)/K\), \(b=t/K\), \(u=(a+bt^2)^{-1}\), \(v=t^2u\), and \(F_*=(2t^3-1)^2/(2K^3)\).

The residual ratio is \(R(t)=1-\eta(a(t))=(2t^3-1)^2/[t(2t^3+t-2)K]\). Differentiating gives
\[
R'(t)=-\frac{(t-1)^2(2t^3-1)(2t^3+1)(2t^4+4t^3+3t^2+2t-2)}{t^2K^2(2t^3+t-2)^2}<0.
\]
The quartic is positive for \(t>1\), being increasing there and equal to nine at one. As \(a'(t)=(2t^3+1)/K^2>0\), the gain is strictly increasing in \(a\). At \(t\downarrow1\) use the exact identity
\[
1-R(t)=\frac{(t-1)^3(2t^4+2t^3+3t^2+t+1)}{t(2t^3+t-2)K}.
\]
This is asymptotic to \(9(t-1)^3\), while \(a\sim3(t-1)\). At \(t\to\infty\), \(R\sim2/t\) and \(b\sim t^{-2}\). These establish the two limits. As a consequence of the known optimality relation, the normalized target-side budget share is \(bv=t^3/(2t^3-1)\to1/2\), and \(u\to1/2\); this allocation is context for the gain law, not a separate priority claim.

## Relationship to prior work

Menon, dos Santos and Anteneodo, [arXiv:2311.00818](https://arxiv.org/abs/2311.00818), §2.1, Eqs. (10)–(14), gives the intrinsic-coordinate time for arbitrary profiles. Menon, [arXiv:2611.17470v1](https://arxiv.org/abs/2611.17470v1), Eq. (50)–(52) and Fig. 4(a), treats the same optimization with a broader variational framework. In dimension one with the Stratonovich parameter \(1/2\), the stationarity equation above the launch point uses the full intrinsic length divided by \(2D_{\rm out}^{3/2}\); below the launch point it uses the target-side intrinsic length divided by \(2D_{\rm in}^{3/2}\). Equating them gives \(b/t=(a+b/t)/t^3\), exactly the cubic used here. The paper's Fig. 5 uses numerically optimized profiles for the gain curve. The claim here is the strict all-launch gain theorem and its two sharp asymptotic laws, not the variational condition, the two-level design or its algebraic parameterization.

## Verification and limitations

The symbolic identities for the derivative and limits can be checked with the accompanying `check.py` (SymPy and SciPy). Its finite profile comparisons do not prove the optimization or endpoint laws; those follow from the analytic argument. The results do not cover different prescriptions, dimension, drift, pointwise caps, or boundary/launch conditions. Literature comparisons do not certify historical priority.
