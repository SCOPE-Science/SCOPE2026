# A tricritical amplitude-optimization law for two-temperature cardinal plant responses

## Finding

For the cardinal-temperature rate law of Yan and Hunt, complete global optimization of an equal-duration warm/cool temperature pair at a fixed mean has three qualitatively different regimes: a discontinuous switch to no fluctuation, an exceptional completely flat optimum, and a continuously vanishing interior optimum. The boundary between these behaviors is the exponent \(p=2\), equivalent to the cardinal ratio \(T_{\mathrm{opt}}/T_{\max}=2/3\).

Define \(f_p(x)=x^p(1-x)\) on \([0,1]\), with \(p>0\), and for \(m\in(0,1)\) let
\[
J_{p,m}(a)=\tfrac12\{f_p(m-a)+f_p(m+a)\},\qquad 0\le a\le d_m:=\min(m,1-m).
\]
All maximizers of \(J_{p,m}\) on its closed feasible interval are as follows.

1. **Concave case \(0<p\le1\):** the unique maximizer is \(a=0\), for every \(m\).
2. **Discontinuous case \(1<p<2\):** let
   \[
   c_p=\frac{2^{p-1}-1}{2^p-1}.
   \]
   If \(m<c_p\), the unique maximizer is \(a=m\); if \(m>c_p\), it is \(a=0\). At \(m=c_p\), exactly \(a=0\) and \(a=m\) maximize (no interior amplitude does). In particular the maximizing amplitude jumps from the full cold-endpoint span to zero.
3. **Degenerate case \(p=2\):** for \(m<1/3\), \(a=m\) is the unique maximizer; for \(m>1/3\), \(a=0\) is the unique maximizer. At \(m=1/3\), *every* amplitude \(a\in[0,1/3]\) maximizes.
4. **Continuous case \(p>2\):** put
   \[
   b_p=\frac{p}{2(p+1)},\qquad i_p=\frac{p-1}{p+1}.
   \]
   For \(m\le b_p\), \(a=m\) uniquely maximizes. For \(m\ge i_p\), \(a=0\) uniquely maximizes. For \(b_p<m<i_p\), the unique maximizer lies strictly inside \((0,d_m)\) and is \(a_*=m\tanh z_*\), where the positive number \(z_*\) is the unique solution of
   \[
   m=\frac{p}{p+1}\left(1+\frac{\tanh z_*}{\tanh((p-1)z_*)}\right)^{-1}.
   \]
   The optimum \(a_*\) decreases continuously to zero as \(m\uparrow i_p\), and obeys the sharp fixed-\(p\) onset
   \[
   a_*\sim\sqrt{\frac{3i_p}{p-2}(i_p-m)}\quad (m\uparrow i_p).
   \]

As an exact nondegenerate illustration, at \(p=3\), \(m=2/5\), the unique maximizing amplitude is \(a_*=\sqrt3/5\). Average normalized response increases from \(24/625\) under constant temperature to \(33/625\), a relative gain of exactly \(3/8\).

## Assumptions and scope

In the unshifted Yan–Hunt cardinal-temperature model, \(0<T_{\mathrm{opt}}<T_{\max}\), and the biological rate on the interval \([0,T_{\max}]\) is
\[
r(T)=R_{\max}\frac{T_{\max}-T}{T_{\max}-T_{\mathrm{opt}}}
\left(\frac{T}{T_{\mathrm{opt}}}\right)^{T_{\mathrm{opt}}/(T_{\max}-T_{\mathrm{opt}})}.
\]
With \(x=T/T_{\max}\) and \(p=T_{\mathrm{opt}}/(T_{\max}-T_{\mathrm{opt}})\), this is a *positive constant multiple* of \(f_p(x)=x^p(1-x)\). Positive multiplication does not change maximizing temperatures. The warm and cool temperatures \(m\pm a\) each persist for exactly half of a fixed observation period; their arithmetic mean is held at \(m\), and their values remain in \([0,1]\). Temporal adaptation, unequal day and night physiological rates, costs of heating, temperature-transition durations, and ecological feedback are excluded.

No broader claim is made about arbitrary temperature distributions, unequal exposure fractions, sinusoidal forcing, crops outside model calibration, or optimization of actual harvest yield. This is an instantaneous-rate averaging problem with a fixed daily thermal mean, not a dynamical crop-growth theorem.

## Proof

**1. Derivative geometry.** For \(x\in(0,1)\),
\[
f_p'(x)=x^{p-1}[p-(p+1)x],\qquad
f_p''(x)=p x^{p-2}[(p-1)-(p+1)x].
\]
The objective is continuous on \([0,d_m]\), differentiable in its interior, and
\[
2\partial_a J_{p,m}(a)=f_p'(m+a)-f_p'(m-a).
\]
For \(p\le1\), the second derivative of \(f_p\) is negative throughout \((0,1)\); strict Jensen concavity gives a unique optimum at zero amplitude. For \(p>1\), its sole inflection is \(i_p=(p-1)/(p+1)\). Thus \(J\) initially increases with amplitude when \(m<i_p\), and initially decreases when \(m>i_p\). At the cold-endpoint boundary \(a=m\le1-m\), the one-sided derivative has the sign of \(f_p'(2m)\) because \(f_p'(0+)=0\), hence the sign of \(b_p-m\), with \(b_p=p/[2(p+1)]\). If \(m>1/2\), the feasible right endpoint is \(a=1-m\); there \(\partial_aJ<0\), since \(f_p'(1)=-1<f_p'(2m-1)\) for \(p>1\).

**2. One critical point at most.** At a strictly interior critical amplitude, write \(r=(m+a)/(m-a)>1\), or \(r=e^{2z}\) with \(z>0\). Rearrangement of \(f_p'(m+a)=f_p'(m-a)\) gives
\[
 m=\frac{p}{2(p+1)}\frac{(1+r)(r^{p-1}-1)}{r^p-1}
   =\frac{p}{p+1}\left(1+\frac{\tanh z}{\tanh((p-1)z)}\right)^{-1}=:M_p(z).
\]
The logarithmic derivative of \(H_p(z)=\tanh z/\tanh((p-1)z)\) is
\[
\frac{d}{dz}\log H_p(z)
=\frac{2}{\sinh(2z)}-\frac{2(p-1)}{\sinh(2(p-1)z)}.
\]
Since \(u\mapsto\sinh(u)/u\) is strictly increasing on \((0,\infty)\), \(H_p\) strictly increases for \(p>2\), strictly decreases for \(1<p<2\), and is identically one when \(p=2\). Its endpoint limits are \(1/(p-1)\) as \(z\downarrow0\) and one as \(z\to\infty\). Therefore \(M_p\) ranges strictly from \(i_p\) to \(b_p\), decreasing for \(p>2\) and increasing for \(1<p<2\); there is at most one interior positive stationary amplitude for any fixed pair \((p,m)\). The map \(a=m\tanh z\) is strictly increasing and bijects \(z>0\) with \(0<a<m\).

**3. The case \(1<p<2\).** Here \(i_p<b_p<1/2\). For \(m\in(i_p,b_p)\), zero amplitude is a strict local maximum and the cold-endpoint boundary is a strict one-sided local maximum. Since at most one stationary amplitude lies between, and it occurs, that point is a strict minimum. Outside this interval the derivative has a fixed sign and the appropriate endpoint is the unique maximizer. Comparing both endpoint values, whenever \(m\le1/2\), yields the exact identity
\[
 J_{p,m}(m)-J_{p,m}(0)
 =m^p\{(2^{p-1}-1)-(2^p-1)m\}.
\]
Its unique positive zero is \(c_p\), and the stationary-branch endpoint limits imply \(i_p<c_p<b_p\). The optimizer classification, including its exactly two maximizers at the switch, follows. When \(m>1/2\), the derivative is everywhere negative; the cold endpoint \(a=m\) is unavailable and \(a=0\) uniquely maximizes.

**4. The case \(p=2\).** Direct polynomial expansion gives
\[
J_{2,m}(a)=m^2(1-m)+(1-3m)a^2.
\]
This proves the entire three-way classification and the interval of maximizers at \(m=1/3\).

**5. The case \(p>2\).** Now \(b_p<i_p\). For \(b_p<m<i_p\), the one-sided derivatives are positive near zero and negative at the feasible right boundary. Since the critical equation has exactly one solution, that interior stationary amplitude is the unique global maximizer. If \(m\le b_p\), the derivative stays positive until the feasible right endpoint; if \(m\ge i_p\), it stays negative from zero onward. Strict uniqueness at the threshold means follows by taking the stationary equation's endpoint limits; no separate optimizer arises at equality. As \(m\uparrow i_p\), \(z_*\downarrow0\), so \(a_*\downarrow0\). Taylor expansion near \((m,a)=(i_p,0)\) gives
\[
f_p''(m)=p(p+1)i_p^{p-2}(i_p-m)+O((i_p-m)^2),\quad
f_p^{(4)}(i_p)=-2p(p+1)(p-2)i_p^{p-3}.
\]
Using \(\partial_a J=f_p''(m)a+f_p^{(4)}(i_p)a^3/6+o((i_p-m)a+a^3)\) on the nonzero maximizing branch proves \(a_*^2\sim 3i_p(i_p-m)/(p-2)\).

**6. Exact example.** For \(p=3\) and \(m=2/5\),
\[
J_{3,2/5}(a)=\frac{24}{625}+\frac{6}{25}a^2-a^4
=\frac{33}{625}-\left(a^2-\frac3{25}\right)^2.
\]
The factorization proves unique optimality at \(a=\sqrt3/5\) on \([0,2/5]\) and exactly \(3/8\) relative gain over \(a=0\).

## Verification

The self-contained `checks/verify.py` uses the standard Python library and checks exact rational identities at the degenerate exponent, the exact quartic example and its gain, numerical boundaries, and a reproducible grid of admissible amplitude comparisons for twenty exponents and ninety-nine means. Running `python checks/verify.py` prints `PASS 244035 assertions`. The proof above, not the finite grid, establishes global and infinite-parameter correctness. The code is auxiliary and requires no third-party packages.

## Relationship to prior work

Yin, Kropff, McLaren and Visperas (1995) introduced the general beta-function temperature response \((T-T_b)^\alpha(T_c-T)^\beta\), including its inflection geometry, and compared predictions for varying day/night regimes. Their full original paper gives response and calibration formulas, not the fixed-mean, equal-duration global amplitude optimization and its three exponent-dependent regimes. Yan and Hunt (1999) simplified the model to the one-power family treated here and evaluated maize day/night-temperature experiments. Their full paper does not derive this global optimization classification. Denny (2019) explains how temporal variation changes mean thermal performance through Jensen averaging, but does not give this family's complete optimal-amplitude or discontinuity theorem.

The result does not rename the general beta response as a new function and does not claim the known Jensen principle as new. Its new mathematical content is the complete **constrained symmetric-pair optimizer classification**, the abrupt versus continuous transition at the quadratic exponent, and the unique interior-temperature law. General convexification or Jensen's inequality supplies useful background but neither alone implies the optimizing symmetric pair and all equality cases.

## Limitations

The result is exact only for one specified rate curve and two equal-duration temperatures with fixed arithmetic mean; real crops have acclimation, separate day/night responses, physical thermal bounds and thermal-transition costs. Particularly, the \(a=m\) optimum includes a zero-temperature boundary at which extrapolated model behavior may be biologically unreliable. The polynomial example is a benchmark, not a field-tested temperature prescription. Historical priority remains provisional against unindexed global optimization studies of beta-shaped thermal performance and general symmetric two-point moment problems; exact first-public day for the broader 1995 predecessor was not independently established. No independent scientific audit has been performed.

## References

- Yin, X., Kropff, M. J., McLaren, G., and Visperas, R. M. (1995). *A nonlinear model for crop development as a function of temperature*. Agricultural and Forest Meteorology 77, 1–16. https://doi.org/10.1016/0168-1923(95)02236-Q . Lawful institutional manuscript: https://edepot.wur.nl/215405 .
- Yan, W., and Hunt, L. A. (1999, published November 1). *An Equation for Modelling the Temperature Response of Plants using only the Cardinal Temperatures*. Annals of Botany 84, 607–614. https://doi.org/10.1006/anbo.1999.0955 . Full paper: https://www.ggebiplot.com/Yan-Hunt1999a.pdf .
- Denny, M. (2019). *Performance in a variable world: using Jensen's inequality to scale up from individuals to populations*. Conservation Physiology 7, coz053. https://doi.org/10.1093/conphys/coz053 . Full text: https://pmc.ncbi.nlm.nih.gov/articles/PMC6736373/ .
