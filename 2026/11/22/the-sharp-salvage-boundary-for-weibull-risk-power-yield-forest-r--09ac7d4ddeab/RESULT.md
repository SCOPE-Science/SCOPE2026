# The sharp salvage boundary for Weibull-risk power-yield forest rotations

## Finding
Consider indefinitely repeated forest rotations, each reset by the earlier of an elected harvest age \(T\in(0,\infty)\) or a destructive event of Weibull age \(F\), with survival \(\Pr(F>t)=\exp(-(t/\eta)^m)\), \(m,\eta>0\). Timber value at age \(t\) is \(v(t)=t^p\), \(p>1\). Planned harvest recovers all value, whereas an earlier event recovers fraction \(s\in[0,1]\). With zero discount, zero replanting delay/cost, and long-run mean harvested value per unit calendar time as the objective, the following complete statement holds.

For every \(0\le s<1\), there is exactly one globally optimal finite cutting age \(T_*(s)\). Set \(\delta=1-s\). It lies strictly between
\[
T_{\mathrm{peak}}=\eta\left(\frac{p(p-1)}{\delta m(p+m-1)}\right)^{1/m},\qquad
T_0=\eta\left(\frac{p}{\delta m}\right)^{1/m},
\]
and is the unique root in this bracket of the explicit scalar equation \(I(T)g_s(T)=N_s(T)\) defined below. The map \(s\mapsto T_*(s)\) is strictly increasing on \([0,1)\). When \(s=1\), the objective is strictly increasing with every finite \(T\): the unique optimum in the extended policy space is \(T=\infty\), meaning never electively harvest and recover the entire stand at its eventual destruction.

Write \(C_{p,m}=\Gamma(1+p/m)/\Gamma(1+1/m)\) and \(X_\delta=(p/(m\delta))^{1/m}\). The precise near-complete-salvage singularity is
\[
\frac{T_*(1-\delta)}{\eta}
=X_\delta-\frac{C_{p,m}}{mp}X_\delta^{2-p}
+o(X_\delta^{2-p})\qquad(\delta\downarrow0).
\]
In particular for quadratic juvenile value \(p=2\) and Rayleigh fire age \(m=2\),
\[
T_*(s)=\eta\left[(1-s)^{-1/2}-\frac1{2\sqrt\pi}+o(1)\right].
\]

## Assumptions and scope
A rotation starts immediately after every cutting or destructive event, with identically distributed fresh Weibull event ages and no costs or delays. The fire hazard depends only on stand age and equals \(h(t)=m t^{m-1}/\eta^m\); salvage is a fixed fraction of the pre-event power-value \(t^p\). The decision is a stationary deterministic age \(T\), not a state-contingent thinning or fire-prevention policy. The extended policy \(T=\infty\) has only destructive-event resets. These assumptions define an idealized *physical-yield* benchmark rather than an economically discounted Faustmann land-value calculation.

Define the cycle duration \(Y=\min(F,T)\). Its expected length, expected harvested value, and renewal yield are respectively
\[
I(T)=\mathbb EY=\int_0^T e^{-(t/\eta)^m}\,dt,
\]
\[
N_s(T)=T^p e^{-(T/\eta)^m}+s\int_0^T t^p h(t)e^{-(t/\eta)^m}\,dt,
\qquad R_s(T)=\frac{N_s(T)}{I(T)}.
\]
All means are finite, so the renewal-reward theorem applies. An exact computational representation uses the lower incomplete gamma \(\gamma\):
\[
I(T)=\frac{\eta}{m}\gamma\left(\frac1m,(T/\eta)^m\right),\qquad
N_s(T)=T^p e^{-(T/\eta)^m}+s\eta^p\gamma\left(1+\frac pm,(T/\eta)^m\right).
\]

## Proof
Put \(S(t)=e^{-(t/\eta)^m}\) and \(\delta=1-s\). Differentiation of the boundary term and event integral gives
\[
N_s'(T)=S(T)\bigl(v'(T)-\delta h(T)v(T)\bigr)=S(T)g_s(T),
\]
where \(g_s(T)=T^{p-1}[p-\delta m(T/\eta)^m]\), while \(I'(T)=S(T)\). Therefore
\[
R_s'(T)=\frac{S(T)}{I(T)^2}H_s(T),\quad
H_s(T)=I(T)g_s(T)-N_s(T),\quad
H_s'(T)=I(T)g_s'(T).
\]
For \(\delta>0\),
\[
g_s'(T)=T^{p-2}\left[p(p-1)-\delta m(p+m-1)(T/\eta)^m\right].
\]
Thus \(H_s\) increases strictly on \((0,T_{\mathrm{peak}})\) and decreases strictly thereafter. Since \(I(T)\sim T\), \(N_s(T)\sim T^p\), and \(g_s(T)\sim pT^{p-1}\) at zero, \(H_s(T)\sim(p-1)T^p>0\). At \(T_0\), \(g_s(T_0)=0\) and \(H_s(T_0)=-N_s(T_0)<0\). The intermediate value theorem and strict post-peak decrease supply exactly one root, situated in the stated bracket. The derivative changes from positive to negative there, proving strict global maximization on all \(T>0\) and against \(T=\infty\) (as the yield is eventually decreasing). For \(s=1\), \(g_1(T)=pT^{p-1}\) is strictly increasing and \(H_1(T)=\int_0^T S(t)[g_1(T)-g_1(t)]dt>0\), so no finite age maximizes.

To compare salvage fractions at fixed \(T\), differentiate \(H_s\) with respect to \(s\):
\[
\partial_s H_s(T)=I(T)h(T)T^p-\int_0^T t^ph(t)S(t)dt
=\int_0^T S(t)[h(T)T^p-h(t)t^p]dt>0.
\]
The last strict inequality follows because \(h(t)t^p=(m/\eta^m)t^{p+m-1}\) is strictly increasing for \(p>1,m>0\). At the unique optimum \(\partial_T H_s=I g_s'<0\); implicit differentiation yields \(dT_*/ds>0\) for \(s<1\), including the right derivative at \(s=0\).

Finally, continuity and \(H_1(T)>0\) at each fixed finite \(T\) show \(T_*(1-\delta)\to\infty\). Dividing the stationarity equation by \(\eta^{p-1}\) and putting \(x=T_*/\eta\) gives \(x^{p-1}[p-\delta m x^m]=R_{1-\delta}(T_*)/\eta^{p-1}\). Because \(x\to\infty\), Weibull tails vanish and the renewal ratio tends to \(C_{p,m}\). Thus the bracket tends to zero and \(x/X_\delta\to1\). Substituting \(x=X_\delta(1-\epsilon_\delta)\) into the stationarity identity gives \(p[1-(1-\epsilon_\delta)^m]=C_{p,m}X_\delta^{1-p}(1+o(1))\), hence \(\epsilon_\delta=(C_{p,m}/(mp))X_\delta^{1-p}+o(X_\delta^{1-p})\). This is the claimed two-term asymptotic. At \(s=1\), the limiting yield is exactly \(\eta^{p-1}C_{p,m}\).

## Verification
The included `checker.py` independently evaluates the gamma-function formulas and numerical quadratures, brackets the scalar optimum, checks its superiority over nearby and distant rotation ages, and tests strict salvage comparative statics over 900 seeded, numerically conditioned parameter draws. Its ordinary numerical output is `checks_passed 10795`. In the example \(p=m=2\), \(\eta=20\) years, optimal ages at salvage fractions \(0,0.5,0.9,0.99\) are approximately \(16.62354,23.89225,57.37586,194.16134\) years. The infinite-parameter mathematical proof does not rely on finite sampling.

## Relationship to prior work
Catastrophe-sensitive forestry rotation, age-varying disaster probabilities and salvageable timber are established in the primary studies by Routledge (1980), Amacher, Malik and Haight (2005), Kuboyama and Oka (2000), and Loisel (public arXiv version 2013). They provide the modeling motivation and, in particular, substantially more realistic discounted land-value, thinning and population models. The result here addresses a different, precisely stated renewal-average criterion and proves the all-Weibull/all-superlinear-power uniqueness and near-perfect-salvage singularity, which were not identified in the inspected accessible full texts. The renewal-reward formula and running-average differentiation are classical tools, not claimed as new. Exact historical priority is provisional owing to inaccessible older full texts.

## Limitations
The theorem is conditional on convex, unbounded power-law value \(t^p\), especially unrealistic if extrapolated to very old stands. Thus the divergent rotation age as salvage approaches one is a mathematical boundary effect, not a prediction of actual tree growth. A bounded sigmoid age-yield curve, ecological maturity, price discounting, mortality other than fire, state-dependent salvage, finite replanting costs or optimized fire-prevention activities change the objective and may remove this phase boundary. No empirical wildfire or timber-management guidance follows. Numerical tests cannot replace the analytic proof.

## References
- R. D. Routledge, “The Effect of Potential Catastrophic Mortality and Other Unpredictable Events on Optimal Forest Rotation Policy,” *Forest Science* 26 (1980), 389–399. https://doi.org/10.1093/forestscience/26.3.389 (abstract and date checked; full text not obtained).
- H. Kuboyama and H. Oka, “Climate risks and age-related damage probabilities – effects on the economically optimal rotation length for forest stand management in Japan,” *Silva Fennica* 34 (2000), article 637. https://doi.org/10.14214/sf.637 (abstract and date checked).
- G. S. Amacher, A. S. Malik and R. G. Haight, “Not Getting Burned: The Importance of Fire Prevention in Forest Management,” *Land Economics* 81 (2005), 284–302. https://doi.org/10.3368/le.81.2.284 (full publicly accessible text inspected).
- P. Loisel, “Faustmann Rotation and population dynamics in the presence of a risk of destructive events,” arXiv:1302.3503, first posted 2013-02-13. https://arxiv.org/abs/1302.3503 (full text inspected).
