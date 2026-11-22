# Two nested Gumbel detection layers at the inverse first-passage admissibility boundary

## Finding

The central finding is an exact **finite-distance visibility law** for failure of inverse mean-first-passage design. Near two distinct admissibility thresholds, the physical mean-time slope of the unique forced potential is almost indistinguishable from the prescribed slope over immense distances, but the mismatch emerges with the **same universal Gumbel profile**. One transition occurs on a single-exponential distance scale; the other on a double-exponential scale. The shifted admissibility condition, general well-free ceiling and clipped far-field laws are supporting structural results established below for a one-dimensional reversible diffusion with spatially decreasing diffusivity.

More precisely, fix \(D_0,A,a,\delta>0\), \(b\in\mathbb R\), and define
\[
D(x)=D_0(1+x)^{-\delta},\qquad
\ell(x)=1+\log(1+x),\qquad
\tau(0)=0,\qquad
\tau'(x)=Aa(1+x)^{a-1}\ell(x)^b.
\]
The potential \(U_\tau\) defined below realizes \(\mathbb E_xH_0=\tau(x)\) for every \(x\ge0\) if and only if
\[
\boxed{a<2+\delta\quad\text{or}\quad a=2+\delta,\ b\le1.}
\]
If this fails, no potential within the specified diffusion convention realizes \(\tau\). Nonetheless the physical mean hitting time \(T_\tau(x)\) of the **formal inverse potential** is finite for every finite \(x\), and obeys the sharp limits
\[
\boxed{T_\tau(x)\sim\frac{x^{2+\delta}}{D_0(2+\delta)(a-2-\delta)}
\quad (a>2+\delta),}
\]
\[
\boxed{T_\tau(x)\sim\frac{x^{2+\delta}\log x}{D_0(2+\delta)(b-1)}
\quad(a=2+\delta,\ b>1).}
\]
The limits hold for every fixed allowed parameter tuple. In particular, \(A\) cancels from both leading coefficients and the off-critical coefficient is also independent of \(b\). There is also a **model-wide no-wells ceiling**: for this fixed diffusivity, any eventually well-free smooth potential with finite MFPT \(T(x)\) and a log-log growth exponent \(\lim_{x\to\infty}\log T(x)/\log x=\gamma\) must satisfy \(\gamma\le2+\delta\). The globally increasing critical example below attains equality, so the ceiling is sharp even beyond the power-logarithmic family.

**Sharp finite-distance detection of failure.** Define the relative slope deficit of the forced inverse landscape by
\[
\Delta(x)=1-\frac{T_\tau'(x)}{\tau'(x)}=\exp[-Q(x)]
\quad\text{when}\quad W_\infty<\infty.
\]
It increases strictly from a possibly extremely small initial value toward one with increasing distance. The two qualitatively distinct near-critical failure regimes have the *same* universal Gumbel-type transition profile, but occur on radically different distance scales.

First take \(b=0\) and \(a=a_c+\varepsilon\), \(\varepsilon>0\). Put \(\kappa_\varepsilon=1/[D_0 A(a_c+\varepsilon)]\). Then **exactly for every finite** \(x\ge0\),
\[
\Delta_\varepsilon(x)=\exp\!\left[-\frac{\kappa_\varepsilon}{\varepsilon}(1+x)^{-\varepsilon}\right].
\]
For any fixed \(s\in\mathbb R\) define the moving observation point by \(\varepsilon\log(1+x_\varepsilon(s))=\log(1/\varepsilon)+s\). On this scale,
\[
\lim_{\varepsilon\downarrow0}\Delta_\varepsilon(x_\varepsilon(s))
=\boxed{\exp[-\kappa_c e^{-s}]},\qquad
\kappa_c=\frac1{D_0Aa_c},
\]
locally uniformly in \(s\). Thus \(\log(1+x)\) must be of order \(\varepsilon^{-1}\log(1/\varepsilon)\) to expose the failure.

Second take \(a=a_c\), \(b=1+\eta\), \(\eta>0\). Exactly,
\[
\Delta_\eta(x)=\exp\!\left[-\frac{\kappa_c}{\eta}\ell(x)^{-\eta}\right].
\]
At the moving observation level \(\eta\log\ell(x_\eta(s))=\log(1/\eta)+s\), whenever this defines a nonnegative observation point (always true for sufficiently small \(\eta\) at fixed \(s\)), the same profile is obtained **without even a limiting error**:
\[
\boxed{\Delta_\eta(x_\eta(s))=\exp[-\kappa_c e^{-s}].}
\]
Here \(\log\log(1+x)\) must be of order \(\eta^{-1}\log(1/\eta)\), so the detection distance is *double exponential* rather than the (single) single-exponential scale in the first regime. For any fixed deficit level \(0<h<1\) the corresponding threshold distances are given exactly by the formulas in the proof. The critical admissible boundary itself has \(\Delta\equiv0\) at every distance.

## Assumptions and scope

The state space is \([0,\infty)\), with absorption at zero and the nonexplosive natural endpoint at infinity. Distances are expressed in a fixed length unit. The stochastic dynamics use the reversible overdamped convention with backward generator
\[
\mathcal L_U f=D f''+(D'-DU')f'
=e^U\bigl(De^{-U}f'\bigr)',
\]
corresponding to the forward equation \(\partial_t p=\partial_x[D(\partial_xp+U'p)]\). The potential is measured in thermal-energy units; additive constants do not affect the process. This fixes the stochastic convention, which matters for nonconstant \(D\). We assume smooth coefficients on finite intervals and no extra resetting or boundary reactions.

Here \(H_0=\inf\{t\ge0:X_t=0\}\), \(T_\tau(x)=\mathbb E_xH_0\), and \(\tau\) is the *desired* mean-time profile, not automatically the actual one. Write \(a_c=2+\delta\) and set
\[
W(x)=\int_0^x\frac{dy}{D(y)\tau'(y)},\quad
W_\infty=\lim_{x\to\infty}W(x),\quad
U_\tau(x)=\log(D(x)\tau'(x))+W(x).
\]
These formulas give a smooth, finite potential on every compact interval. The same result includes all real \(b\), including negative values.

## Proof

**1. Forced inverse and the boundary-at-infinity correction.** Any actual differentiable finite mean hitting-time profile \(T\) satisfies \(\mathcal L_UT=-1\) with \(T(0)=0\). If it equals \(\tau\), then
\[
U'(x)=\frac{\tau''(x)}{\tau'(x)}+\frac{D'(x)}{D(x)}+\frac1{D(x)\tau'(x)},
\]
so \(U_\tau\) is the *only* possible potential, up to an additive constant. The apparent inverse is therefore not an arbitrary choice.

Set \(W'=1/(D\tau')\). The identity
\[
e^{-U_\tau}=\frac{e^{-W}}{D\tau'}=-\frac{d}{dx}e^{-W}
\]
shows that \(\int_x^\infty e^{-U_\tau(y)}dy=e^{-W(x)}-e^{-W_\infty}<\infty\). The scale derivative is \(s'(x)=e^{U_\tau(x)}/D(x)=\tau'(x)e^{W(x)}\). Because \(\tau(x)\to\infty\), its integral diverges at infinity, making that endpoint inaccessible. The standard minimal Green-function formula consequently gives the finite actual mean hitting time
\[
T_\tau(x)=\int_0^x\frac{e^{U_\tau(y)}}{D(y)}
\left(\int_y^\infty e^{-U_\tau(z)}dz\right)dy.
\]
Inserting the exact tail identity yields
\[
\boxed{T_\tau'(x)=\tau'(x)
\left[1-e^{W(x)-W_\infty}\right],}
\]
with \(e^{-\infty}=0\). It also proves \(T_\tau(x)\le\tau(x)\), with equality at every positive \(x\) exactly when \(W_\infty=\infty\). In the finite-\(W_\infty\) case the bracket is strictly between zero and one, and direct differentiation checks \(\mathcal L_{U_\tau}T_\tau=-1\). Thus there is no other potential realizing the forbidden profile.

**2. Sharp admissibility including the logarithmic line.** Directly from the definitions,
\[
W'(x)=\frac{(1+x)^{1+\delta-a}}{D_0Aa\,[1+\log(1+x)]^b}.
\]
With the change of variables \(u=1+\log(1+x)\), the integral at infinity behaves as a power integral if \(a\ne a_c\), and as \(\int_1^\infty u^{-b}du\) if \(a=a_c\). It diverges precisely for \(a<a_c\), or \(a=a_c,b\le1\). The preceding exact identity proves necessity and sufficiency, including the boundary \(b=1\).

**3. Sharp clipping outside the admissible region.** When \(W_\infty<\infty\), define
\[
Q(x)=W_\infty-W(x)=\int_x^\infty\frac{dy}{D(y)\tau'(y)}\downarrow0.
\]
The exact multiplier \(1-e^{-Q(x)}\sim Q(x)\). For \(a>a_c\), elementary tail integration (or the regular-variation integral theorem) gives
\[
Q(x)\sim\frac{(1+x)^{a_c-a}\ell(x)^{-b}}
{D_0Aa(a-a_c)}.
\]
Multiplication by \(\tau'(x)\) therefore yields
\[
T_\tau'(x)\sim\frac{x^{a_c-1}}{D_0(a-a_c)}.
\]
Integrating and using \(a_c>0\) gives the first boxed law.

At \(a=a_c,b>1\), the substitution \(u=\ell(y)\) gives the **exact** tail
\[
Q(x)=\frac{\ell(x)^{1-b}}{D_0Aa(b-1)}.
\]
Thus \(T_\tau'(x)\sim x^{a_c-1}\log x/[D_0(b-1)]\). Another integration gives the second boxed law. These computations supply the complete leading constants and show their independence from \(A\).

**4. A monotone, genuinely superquadratic realization.** At \(a=a_c,b=0\), the desired profile is exactly
\[
\tau(x)=A\big((1+x)^{a_c}-1\big),
\qquad
U_\tau(x)=\left(1+\frac1{D_0Aa_c}\right)\log(1+x)+C.
\]
The potential is strictly increasing on the whole half-line, yet \(\tau(x)\sim Ax^{2+\delta}\) with exponent greater than two. For \(2<a<a_c\) and \(b=0\), the explicit inverse
\[
U_\tau(x)=(a-1-\delta)\log(1+x)
+\frac{(1+x)^{a_c-a}-1}{D_0Aa(a_c-a)}+C
\]
is eventually strictly increasing, and exact admissibility holds. Consequently the constant-diffusivity necessity of distant wells is not stable under spatially decaying diffusivity.

**5. The general sharp no-wells ceiling.** Let \(U\) be any smooth potential with finite physical mean \(T(x)\) for all finite \(x\), and suppose \(U\) has no local minima beyond some \(X\). The finiteness of \(T\) forces \(\int_x^\infty e^{-U(y)}dy<\infty\); an eventually nonincreasing potential would violate this. Continuity of \(U'\) together with the absence of negative-to-positive crossings therefore forces \(U'\ge0\) eventually (the same elementary sign argument as in [1]). Hence the backward equation implies
\[
(DT')'=DU'T'-1\ge-1.
\]
Thus \(G(x)=D(x)T'(x)+x\) is nondecreasing beyond \(X\). Set \(J(x)=\int_X^x D(y)^{-1}dy\asymp x^{1+\delta}\). As \(D>0\), for \(x>X\),
\[
T(x)-T(X)=\int_X^x\frac{G(y)-y}{D(y)}dy
\le G(x)J(x),
\]
and therefore \(D(x)T'(x)\ge[T(x)-T(X)]/J(x)-x\). If \(T(x)=x^{\gamma+o(1)}\) for some \(\gamma>2+\delta\), choose \(0<\varepsilon<\gamma-2-\delta\); then for large \(x\),
\[
D(x)T'(x)\ge c x^{\gamma-\varepsilon-1-\delta},
\qquad
\int^\infty\frac{dx}{D(x)T'(x)}<\infty.
\]
This contradicts the necessary boundary-at-infinity condition: applying the forced-inverse identity to an actual \(T\) gives \(De^{-U}T'=e^{-W_T}\to0\), where \(W_T'=1/(DT')\) and the limit is zero because \(De^{-U}T'(x)=\int_x^\infty e^{-U(y)}dy\to0\). Thus \(\gamma\le 2+\delta\). The globally increasing example in step 4 has exponent \(2+\delta\), proving sharpness.

**6. Exact detection radii and singular transition profiles.** For an inadmissible prescription, the identity of step 1 gives \(\Delta(x)=\exp[-Q(x)]\). When \(a=a_c+\varepsilon,b=0\), the integral for \(Q\) is exact:
\[
Q_\varepsilon(x)=\frac{\kappa_\varepsilon}{\varepsilon}(1+x)^{-\varepsilon}.
\]
When \(a=a_c,b=1+\eta\), the logarithmic substitution is exact and gives
\[
Q_\eta(x)=\frac{\kappa_c}{\eta}\ell(x)^{-\eta}.
\]
Both are strictly decreasing. Fix a desired relative slope deficit \(h\in(0,1)\) and write \(q_h=-\log h>0\). For sufficiently small \(\varepsilon,\eta>0\), the unique point where \(\Delta=h\) is therefore exactly
\[
\boxed{1+x_\varepsilon(h)=\left(\frac{\kappa_\varepsilon}{\varepsilon q_h}\right)^{1/\varepsilon},}
\qquad
\boxed{1+\log(1+x_\eta(h))
=\left(\frac{\kappa_c}{\eta q_h}\right)^{1/\eta}.}
\]
Consequently
\[
\log(1+x_\varepsilon(h))
=\frac{\log(1/\varepsilon)+\log(\kappa_\varepsilon/q_h)}{\varepsilon},
\]
\[
\log\log(1+x_\eta(h))
=\frac{\log(1/\eta)+\log(\kappa_c/q_h)}{\eta}+o(1).
\]
Substituting the two rescaled distances into the exact \(Q\)'s proves the universal profile in the finding, with local uniformity in the first case by \(\kappa_\varepsilon\to\kappa_c\). For every fixed \(x\) the deficit goes to zero when the forbidden parameter approaches its admissible boundary, while for any fixed forbidden parameter it tends to one as \(x\to\infty\). Hence the limits provably do not commute. The detection thresholds refer to the **relative derivative**, not the total MFPT or to finite-precision experimental data.

## Verification

The accompanying standalone standard-library \(\texttt{CHECK.py}\) evaluates the forced potential derivative, exact boundary correction, generator equation, pure-power and marginal-logarithmic classes, clipping derivative coefficients, the two critical distance-rescaled profile identities, and a constant-diffusion control. It passed **1131 finite assertions** over several parameter values and positions. These checks do not constitute an infinite-domain proof; the proof above supplies the required quantifiers and tail estimates. Execute \(\texttt{python3 CHECK.py}\) beside this document to reproduce the checks.

## Relationship to prior work

Keidar, Reuveni and Sokolov [1], first public on 2 November 2026, prove the unique inverse potential, the constant-diffusivity condition \(\int^\infty dx/\tau'(x)=\infty\), a quadratic ceiling for eventually monotone landscapes, and the phenomenon of clipping when a forced cubic inverse violates the infinity boundary. Those general *constant-diffusivity* results are not claimed here. The present classification uses a **specified nonuniform diffusion law** and the reversible stochastic convention; it gives the shifted power-logarithmic admissibility boundary, a globally monotone superquadratic example, the full sharp forbidden-profile clipping constants, and, centrally, exact finite-distance critical detection layers with a common Gumbel profile and distinct single-exponential/double-exponential scales. The inverse ODE and its constant-diffusivity admissibility criterion are known; their variable-diffusivity forms can also be obtained by a Lamperti coordinate change. The new result assessed here is the explicit dual detection law, not the general inversion identity.

Menon [2], first public 12 November 2026, optimizes a diffusivity profile on a *bounded reflecting/absorbing shell* for a different objective; it does not solve inverse potential design on a half-line. Kim and Netz [3] derive forward path-time formulas for general heterogeneous diffusivity in finite reaction intervals, but do not state these inverse admissibility or sharp clipping classifications. The Green-function method here is standard and credited; the contribution is the precise combined phase classification and its physical interpretation. An equivalent reduction in the broader diffusion/regular-variation literature remains a publication-priority risk.

## Limitations

The exact laws assume a known deterministic \(D(x)=D_0(1+x)^{-\delta}\), \(\delta>0\), and the specified reversible stochastic convention. They do not hold verbatim for other stochastic prescriptions, higher-dimensional geometry, arbitrary variable diffusivity, finite reflecting domains, or noisy empirical inversion. The detection thresholds concern the relative starting-distance derivative of the mean hitting-time profile, not a total-time error or a statistical finite-sample detectability guarantee. The clipping formulas and sharp variable-diffusivity ceiling follow from known one-dimensional inverse/forward identities with additional exact calculations; their role here is to establish the detection-law setting rather than a separate independent novelty claim. The clipped laws are fixed-parameter asymptotics as \(x\to\infty\), not a uniform transition as \(a\to a_c\) or \(b\to1\). The general no-wells bound assumes existence of the log-log growth exponent and eventual absence of local minima, not arbitrary oscillatory profiles. The result is not a claim about first-passage-time distributions beyond their means. Literature searches cannot certify global priority; an implicit older equivalent remains possible.

## References

[1] T. D. Keidar, S. Reuveni, I. M. Sokolov, *The Inverse Mean First-Passage Time Problem*, arXiv:2611.03831v1 (2 November 2026). https://arxiv.org/html/2611.03831v1

[2] L. Menon, *Optimal heterogeneous diffusivity profiles for mean first-passage minimization*, arXiv:2611.17470v1 (12 November 2026). https://arxiv.org/html/2611.17470v1

[3] W. K. Kim, R. R. Netz, *The mean shape of transition and first-passage paths*, J. Chem. Phys. 143, 224108 (2015); arXiv:1509.00418. https://arxiv.org/abs/1509.00418

[4] S. Ray, *Space-dependent diffusion with stochastic resetting: A first-passage study*, arXiv:2010.14237 (27 October 2020). https://arxiv.org/abs/2010.14237
