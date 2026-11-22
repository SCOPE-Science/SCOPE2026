# Universal single-crossing and delayed exposure reversals for two-zone ventilation sensing

## Finding

For two communicating, well-mixed indoor compartments with independent constant emissions and losses, the difference between their pollutant concentrations either retains its sign throughout the response or changes sign **exactly once**. The same dichotomy holds for every repeated time integral of that difference: a sign change exists exactly when the source-rate difference and the opposite steady-state loss-weighted source difference have opposing signs. The existence of the change does not depend on interzone exchange rates. When one exists, taking additional time integrals strictly delays it, to an unbounded sequence of observation horizons. For symmetric exchange, stronger mixing strictly advances the *instantaneous* reversal but never brings it before an explicit positive limiting time.

More precisely, use the notation and assumptions below. For each integer \(j\ge0\), either \(D_j\) has constant nonzero sign on \((0,\infty)\), or \(D_j\) crosses zero strictly once on \((0,\infty)\), with the latter occurring exactly when \(qh<0\). If \(q=h=0\), all differences vanish. With \(qh<0\), write the unique zeros as \(t_j\). They obey

\[
0<t_0<t_1<t_2<\cdots,\qquad \lim_{j\to\infty}t_j=\infty.
\]

If in addition \(u=v=k>0\), then \(t_0(k)\) decreases strictly with \(k\), and its sharp high-mixing limit is

\[
\lim_{k\to\infty}t_0(k)=\frac{2}{a+b}\log\left(1+\frac{a+b}{2}\left|\frac{q}{h}\right|\right).
\]

## Assumptions and scope

The variables \(x_1(t),x_2(t)\) are **excess** pollutant concentrations relative to a constant outdoor baseline. Initial excesses are zero. For real constants \(a,b,u,v>0\) and \(S_1,S_2\ge0\), concentrations solve the autonomous two-zone mass-balance model

\[
\dot x_1=S_1-(a+u)x_1+ux_2,\qquad
\dot x_2=S_2+vx_1-(b+v)x_2,\qquad x_1(0)=x_2(0)=0.
\]

The coefficients \(a,b\) denote compartment-specific removal other than exchange, while \(u,v\) are positive volume-normalized interzone transfers; for a conservative exchange flow \(Q>0\) between unequal positive volumes \(V_1,V_2\), one can put \(u=Q/V_1\) and \(v=Q/V_2\). The source terms are emissions divided by the respective volumes. Let \(q=S_1-S_2\) and \(h=bS_1-aS_2\). Define \(d=x_1-x_2\), \(D_0=d\), and \(D_j(t)=\int_0^t D_{j-1}(s)\,ds\) for every integer \(j\ge1\). Equivalently, \(D_j(t)=\int_0^t(t-s)^{j-1}d(s)/(j-1)!\,ds\). For positive volumes, the bias \(x_1-(V_1x_1+V_2x_2)/(V_1+V_2)=V_2d/(V_1+V_2)\), so the sign and all integration crossing times are identical to those of \(d\).

## Proof

**1. Two-mode exact transfer function.** Let \(s\) be the Laplace variable. Solving the two linear constant-source equations yields

\[
\widehat d(s)=\frac{qs+h}{s\{s^2+(a+b+u+v)s+ab+av+bu\}}.
\]

The positive relaxation rates \(r_-<r_+\) solve \((s+r_-)(s+r_+)=s^2+(a+b+u+v)s+ab+av+bu\), explicitly

\[
r_{\pm}=\frac{a+b+u+v\pm\sqrt{(a+u-b-v)^2+4uv}}{2}.
\]

Their positivity follows from positive trace and determinant of the decay matrix; their strict separation follows from \(uv>0\). Put \(B(t)=[e^{-r_-t}-e^{-r_+t}]/(r_+-r_-)\) and \(F_j=I^j B\) for all \(j\ge0\). Inverting the transfer function gives the **exact identity**

\[
D_j(t)=qF_j(t)+hF_{j+1}(t).
\]

All \(F_j(t)>0\) for \(t>0\). Also \(d'(0)=q\) and \(d(\infty)=h/(ab+av+bu)\), confirming that the sign condition compares early and equilibrium ordering, with no exchange terms in its numerator.

**2. Strictly decreasing ratio.** Let \(\delta=r_+-r_->0\). Since \(B(t)=e^{-r_-t}(1-e^{-\delta t})/\delta\),

\[
\frac{d^2}{dt^2}\log B(t)=-\frac{\delta^2e^{\delta t}}{(e^{\delta t}-1)^2}<0
\]

for \(t>0\). More generally, if \(f\) is positive and strictly log-concave on \((0,\infty)\), with \(f(0)=0\) and finite continuous initial extension, then \(G(t)=\int_0^t f(s)\,ds\) is strictly log-concave: writing \(\ell=\log f\),

\[
G(t)^2(\log G(t))''
=f'(t)G(t)-f(t)^2
=f(t)\int_0^t f(s)[\ell'(t)-\ell'(s)]\,ds<0.
\]

Apply this recursively to \(B,F_1,F_2,\ldots\). Therefore, for every \(j\ge0\), the ratio

\[
R_j(t)=\frac{F_j(t)}{F_{j+1}(t)}
=(\log F_{j+1}(t))'
\]

is strictly decreasing. The small-time asymptotics \(B(t)\sim t\) imply \(F_j(t)\sim t^{j+1}/(j+1)!\), hence \(R_j(t)\to\infty\) as \(t\downarrow0\). At infinity, \(F_0\to0\), \(F_1\to1/(r_-r_+)\), and \(F_j(t)\sim t^{j-1}/[(j-1)!r_-r_+]\) for \(j\ge1\), so \(R_j(t)\to0\). Consequently \(D_j=F_{j+1}(qR_j+h)\) has exactly one strict positive zero if \(qh<0\), and none if \(qh\ge0\) apart from the identically zero case \(q=h=0\). The crossing is from the sign of \(q\) to the sign of \(h\).

**3. Separation and divergence of crossing times.** Assume \(qh<0\). On \((0,t_j)\), the signal \(D_j\) has exactly the sign of \(q\). Therefore

\[
D_{j+1}(t_j)=\int_0^{t_j}D_j(s)\,ds
\]

has that same strict sign, and the unique zero of \(D_{j+1}\) occurs later, proving \(t_{j+1}>t_j\). For \(j\ge1\), the positive-kernel integral formulas give \(F_{j+1}(t)\le (t/j)F_j(t)\). At a zero, \(R_j(t_j)=|h/q|\), so \(t_j\ge j|q/h|\), showing \(t_j\to\infty\).

**4. Monotone symmetric mixing.** When \(u=v=k>0\), put \(\delta(k)=\sqrt{(a-b)^2+4k^2}\) and \(r_-(k)=[a+b+2k-\delta(k)]/2\). In the crossing regime \(a\ne b\) necessarily, so both \(r_-\) and \(\delta\) are strictly increasing in \(k\). For each \(0<s<t\),

\[
\frac{B_k(s)}{B_k(t)}=e^{r_-(k)(t-s)}\frac{1-e^{-\delta(k)s}}{1-e^{-\delta(k)t}}
\]

increases strictly in \(k\). Indeed the logarithmic derivative of the second factor with respect to \(\delta\) is \(s/(e^{\delta s}-1)-t/(e^{\delta t}-1)>0\). Thus \(R_0(t,k)=B_k(t)/\int_0^tB_k(s)\,ds\) strictly decreases with \(k\) at fixed \(t\). Since it also decreases strictly with \(t\), its unique crossing of \(|h/q|\) occurs at a strictly decreasing time \(t_0(k)\). Finally \(r_-(k)\to(a+b)/2=:r\) and \(\delta(k)\to\infty\), implying \(R_0(t,k)\to r/(e^{rt}-1)\) for each fixed \(t>0\). Monotonicity and uniqueness identify the stated limit. No claim is made about monotonicity of \(t_j(k)\) for \(j\ge1\).

## Verification

The included standalone `verify.py` checks the Laplace rational identity symbolically, and verifies the exact rational example \(a=4,b=1,u=v=2,S_1=2,S_2=1\). In that case

\[
d(t)=\frac{14e^{-2t}-9e^{-7t}-5}{35},\qquad D_1(t)=\frac{7(1-e^{-2t})-\frac97(1-e^{-7t})-5t}{35}.
\]

Its unique instantaneous crossing is \(t_0=0.485623294953729886\ldots\), the cumulative crossing is \(t_1=0.921651901306632447\ldots\), and the symmetric-high-exchange limiting instantaneous horizon is \((2/5)\log(9/4)=0.324372086486531506\ldots\). The verifier independently evaluates 150 matrix-exponential time observations, positive-kernel integrals through the first five crossing horizons and a sample of mixing coefficients. All numerical results are checks on an analytic theorem, not substitutes for infinite-dimensional quantifiers or strict global inequalities. Run `python verify.py` with SymPy and mpmath installed.

## Relationship to prior work

Rodda, Hughes and Craske's 2023 public preprint (arXiv:2306.03183v1, originally titled *Fast and slow response modes in the ventilation of a living computer laboratory*) motivates studying finite-dimensional indoor CO₂ transient dynamics through fast and slow relaxation modes. Its accessible later full text and the 2026 journal article model classroom–plenum exchange and occupancy forcing; those works establish the multizone foundation, not the stated two-source cross-horizon all-integral classification or its mixing monotonicity. Pei et al. (2019) document consequential spatial sensor bias, particularly in displacement ventilation; that empirical sensor-placement result is distinct from this universal linear-model time-order classification. Log-concavity and elementary positive-convolution techniques are classical mathematical ingredients and are not claimed as novel. A separate three-room source-versus-middle-purifier comparison concerns an impulse and treatment-location choices, not simultaneous constant-source sensor bias. These are implication-level comparisons, not novelty inferred from title mismatches.

## Limitations

The result assumes linear perfectly mixed zones, positive constant rates, constant *simultaneous* source terms starting from zero excess, and a fixed outdoor baseline. There is no occupant movement, variable ventilation or sensor delay, and no validation against measured spatial profiles. Two-compartment analytical transfer theory predates the cited motivating source. Priority of this precise specialization is provisional pending broader historical verification, especially older control-theory and multizone literature not fully inspected. Equal-exchange monotonicity is **only** asserted for \(u=v=k\); it is not asserted for independently changing \(u,v\). The model is an analytical benchmark, not a building-design rule or empirical estimate.

## References

1. Rodda, C., Hughes, G., and Craske, J. (2023). *Fast and slow response modes in the ventilation of a living computer laboratory*. arXiv:2306.03183v1, first submitted 5 June 2023. https://arxiv.org/abs/2306.03183 (subsequent revisions bear a changed title).
2. Rodda, C., Craske, J., and Hughes, G. O. (2026). *Mixing and ventilation in a living laboratory due to fast and slow response modes*. *Flow* 6, E9. https://doi.org/10.1017/flo.2026.10045
3. Pei, G., Rim, D., Schiavon, S., and Vannucci, M. (2019). *Effect of sensor position on the performance of CO2-based demand controlled ventilation*. *Energy and Buildings* 202, 109358. https://doi.org/10.1016/j.enbuild.2019.109358
