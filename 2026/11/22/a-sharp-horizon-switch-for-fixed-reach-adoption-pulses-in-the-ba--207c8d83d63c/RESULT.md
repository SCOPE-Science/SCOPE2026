# A sharp horizon switch for fixed-reach adoption pulses in the Bass diffusion model

## Finding

Consider the deterministic Bass innovation–imitation equation with strictly positive innovation and imitation rates, a fixed initial adopter fraction, and one instantaneous campaign. If a campaign directly converts a **fixed absolute fraction of the total market** (capped by the remaining nonadopters), its globally optimal delivery time is always **the beginning or the end** of the observation horizon, except for a precisely identified terminal saturation plateau. More surprisingly, a unique sharp horizon can switch the strictly optimal campaign from the beginning to the end. If instead the campaign converts a **fixed proportion of the then-remaining nonadopters**, the beginning is always uniquely optimal.

Here is the complete absolute-reach classification. Define
\[
\Lambda=p+q,\qquad y=\frac{p+qx_0}{1-x_0},\qquad
H_* =\frac{q^2[\Lambda-a(q+y)]}{y[aq(q+y)+\Lambda y]},\qquad
H_c=\frac{\Lambda/a-q}{y}.
\]
The quantities are positive and \(H_c>\max\{1,H_*\}\). Write \(H=e^{\Lambda T}\), where \(T>0\) is the observation horizon. If \(H<H_c\), the unique optimal campaign time is \(t=0\) when \(1<H<H_*\), the only optimal times are \(0,T\) when \(H=H_*>1\), and the unique optimum is \(t=T\) when \(H>H_*\) (including every case with \(H_*\le1\)). When \(H\ge H_c\), the optimal times are exactly
\[
\left[\frac{\log H_c}{\Lambda},\ T\right],
\]
all of which attain complete market saturation. The nontrivial early-to-late switch exists if and only if
\[
q-p-2qx_0>qa.
\]
In that case the switch time is \(T_*=(\log H_*)/\Lambda\), strictly smaller than the saturation time \(T_c=(\log H_c)/\Lambda\). There is never a strictly optimal interior, nonsaturating campaign time.

For the exact example \(p=1/10\), \(q=1\), \(x_0=0\), \(a=1/10\), the switch occurs at \(H_*=45\) and saturation first becomes possible at \(H_c=100\); at the switch both endpoint campaigns yield final adoption \(9/10\). This distinguishes a genuine endpoint tie from the later saturation plateau.

## Assumptions and scope

Let \(p,q,T>0\), \(0\le x_0<1\), and \(0<a<1-x_0\). In the absence of a campaign, adopter fraction \(x(t)\) evolves according to
\[
\dot x=f(x)=(p+qx)(1-x),\qquad x(0)=x_0.
\]
Adoption is irreversible, the market potential is normalized to one, the environment is homogeneous, and \(p,q\) are constant over the horizon. Let \(\Phi_t(x)\) denote the Bass flow. An **absolute-reach** campaign implemented at time \(t\in[0,T]\) makes the instantaneous state jump
\[
J_a(x)=\min\{1,x+a\}.
\]
The terminal payoff to maximize is \(X_a(t)=\Phi_{T-t}(J_a(\Phi_t(x_0)))\). Campaign timing is a continuous choice and the campaign jump is instantaneous; there are no financial costs, endogenous rate effects, or constraints other than the one nominal market-fraction reach \(a\). If too few nonadopters remain, a nominal campaign can convert fewer than \(a\), modeled by the cap. A **proportional-reach** campaign with \(0<\theta<1\) instead uses \(J_\theta(x)=x+\theta(1-x)\) and has terminal payoff \(X_\theta(t)=\Phi_{T-t}(J_\theta(\Phi_t(x_0)))\). These are different resources: one is an absolute fraction of the total market, the other a fraction of the remaining nonadopter pool. They are not assumed cost-equivalent.

The mathematical conclusions concern deterministic terminal adoption under those exact idealizations. They do not assert real marketing campaign effects, sales, profitability, or social welfare.

## Proof

**1. Flow coordinates and campaign map.** Set \(\Lambda=p+q\) and \(Y(x)=(p+qx)/(1-x)\) for \(0\le x<1\). Direct differentiation using the Bass equation gives \(dY/dt=\Lambda Y\), while the inverse is \(X(Y)=(Y-p)/(Y+q)\). Consequently
\[
\Phi_t(x)=\frac{Y(x)e^{\Lambda t}-p}{Y(x)e^{\Lambda t}+q}.
\]
For an unsaturated absolute pulse, applying \(x\mapsto x+a\) to the transformed coordinate is the fractional-linear map
\[
P_a(Y)=\frac{(\Lambda+aq)Y+aq^2}{\Lambda-a(Y+q)}.
\]
Its denominator is positive exactly when the immediate postpulse state is strictly below one. Along the unperturbed trajectory it decreases in time and first reaches zero when \(e^{\Lambda t}=H_c=(\Lambda/a-q)/y\), where \(y=Y(x_0)\). The assumption \(a<1-x_0\) gives \(H_c>1\). The original equation approaches one without reaching it in finite time. Thus \(X_a(t)=1\) if and only if \(e^{\Lambda t}\ge H_c\), and if \(H=e^{\Lambda T}\ge H_c\) the complete set of optima is \([\log(H_c)/\Lambda,T]\), proving the plateau statement.

**2. No interior nonsaturating maximizer.** For every time when the jump is unsaturated, differentiate the terminal payoff along the unperturbed trajectory and use the derivative of a flow with respect to its initial state. The flow variational identity yields
\[
X_a'(t)=\partial_x\Phi_{T-t}(x_t+a)\,[f(x_t)-f(x_t+a)],
\qquad x_t=\Phi_t(x_0).
\]
The first factor is strictly positive. Expanding the quadratic field gives
\[
f(x)-f(x+a)=a[p-q+2qx+qa].
\]
Since \(x_t\) strictly increases with \(t\), this last factor is strictly increasing across the entire nonsaturating interval and can change sign only from negative to positive. Thus \(X_a\) either increases, or decreases, or decreases and then increases; any nonsaturating stationary point is a **strict minimum**, never a maximum. If \(H<H_c\), every feasible pulse is unsaturated, so every global optimum belongs to \(\{0,T\}\).

**3. Exact comparison of the two endpoint impulses.** Put \(H=e^{\Lambda T}\) and suppose \(1<H<H_c\). The transformed terminal adopter coordinates for an early and a late absolute pulse are \(HP_a(y)\) and \(P_a(Hy)\), respectively. Direct subtraction gives
\[
HP_a(y)-P_a(Hy)=
\frac{-a(H-1)\{Hy[aq(q+y)+\Lambda y]-q^2[\Lambda-a(q+y)]\}}
{[\Lambda-a(q+y)][\Lambda-a(Hy+q)]}.
\]
Both denominator factors are strictly positive, as is \(a(H-1)\). Because the inverse \(X(Y)\) is strictly increasing, the sign of the early-minus-late terminal payoff is therefore the sign of \(H_*-H\), with \(H_*\) as in the finding. The comparison is strict off equality; at \(H=H_*\) the endpoints tie, and the no-interior-maximizer argument makes them the only optimizers. This proves the complete nonsaturated phase diagram.

**4. Existence and location of the switch.** Algebra using \(y=(p+qx_0)/(1-x_0)\) shows that \(H_*>1\) if and only if \(q-p-2qx_0>qa\). Direct simplification shows
\[
H_c-H_* = \frac{\Lambda^2}{a[aq(q+y)+\Lambda y]}>0.
\]
Therefore a genuine switch time, if it exists, is positive and strictly precedes the first possible saturation time. At \(H=H_c\), only the late endpoint is saturated; the plateau then grows continuously backward in calendar time with larger horizons. These strict inequalities settle every boundary case under the stated assumptions.

**5. Proportional reach always favors the beginning.** For \(J_\theta(x)=x+\theta(1-x)\), where \(0<\theta<1\), the same flow-variation calculation gives
\[
X_\theta'(t)=\partial_x\Phi_{T-t}(J_\theta(x_t))\,[J_\theta'(x_t)f(x_t)-f(J_\theta(x_t))].
\]
The bracket is exactly
\[
-(1-\theta)\theta q(1-x_t)^2<0.
\]
The remaining derivative is positive; hence \(X_\theta\) decreases strictly on the full interval \([0,T]\). This establishes the unique proportional-reach optimum \(t=0\). No part of the proof requires sampled numerical trajectories or external optimization software.

## Verification

Run the included standalone Python 3 standard-library checker using `python3 verify.py`. It executes exact rational arithmetic on the transformed Bass flow, checks a strict exact switch witness with \(H_*=45\), \(H_c=100\), both endpoint values \(9/10\), and checks projective subtraction identities. It then exercises \(12{,}000\) seeded rational parameter scenarios with five scheduled times, including exact switch and saturation boundaries, plus both absolute- and proportional-reach inequalities. The checker prints `VERIFY_OK` and the number of assertions if all pass. The full continuous-parameter theorem follows from the algebraic and variational proof above; sampling alone cannot establish it.

## Relationship to prior work

Bass (1969) introduces the innovation–imitation differential equation and the direct-adoption interpretation; its inspected full text does not study optimization of a single fixed-reach instantaneous adopter-state jump. Fruchter and Van den Bulte (2011, DOI:10.1016/j.ijresmar.2011.03.005) analyze optimal continuous advertising-expenditure paths in the Generalized Bass Model with revenue and advertising costs; their inspected model, objective, and control channel differ materially from this one-impulse terminal-adoption problem. Lehmann and Esteban-Bravo (2006, DOI:10.1007/s11002-006-7942-9) analyze market seeding with two coupled adopter segments, three discrete periods, subsidy and price choices, and a discounted-profit objective. Their inspected full text fixes subsidy timing to the initial period (page 247) rather than globally optimizing a single fixed-size direct-adoption pulse across a continuous horizon. Delre, Jager, Bijmolt and Janssen (2007, DOI:10.1016/j.jbusres.2007.02.002) study timing and targeting in a heterogeneous agent-based simulation; the accessible abstract reports category-dependent timing, but no full-text negative-priority conclusion is drawn from that abstract alone.

Two further publicly indexed mathematical treatments consider, respectively, **sorting finitely many innovation/imitation rate regimes by a cross-product condition** in a finite stochastic Bass process, and **ordering two Bass-type flows with customer attrition** by comparing rational-flow compositions. Their examined statements concern concatenated *rate changes*, not a single instantaneous direct conversion of a fixed fraction of the whole market followed by an unchanged Bass flow; neither their assumptions nor their conclusions imply the horizon threshold and saturation classification here without additional derivation. Standard Riccati and linear-fractional methods themselves are established mathematical tools, not claimed novel. The specific phase diagram and the contrast between absolute-reach and proportional-reach impulses form the proposed contribution, conditional on incomplete historical-priority coverage.

## Limitations

The proof applies only to a homogeneous, noiseless, one-product Bass model with no customer exit, fixed innovation/imitation rates, one instantaneous jump, terminal-adoption objective, and no discount or intervention cost. It does not establish an empirically useful intervention protocol or prove any schedule optimal under equal monetary spend; the two pulse mechanisms consume different resources. Saturation depends on the explicit cap at one. More general hybrid impulse control theorems may subsume portions of the phase diagram; possible historical equivalents in uninspected advertising and optimization literature remain unresolved. Prior-work inspection does not certify uniqueness, and no independent mathematical audit has been performed.

## References

1. F. M. Bass, *A New Product Growth for Model Consumer Durables*, *Management Science* **15** (1969), 215–227. DOI:10.1287/mnsc.15.5.215. Full lawful text: https://pdodds.w3.uvm.edu/files/papers/others/1969/bass1969a.pdf. First verified public source date: 1969-01-01 (journal issue).
2. G. E. Fruchter and C. Van den Bulte, *Why the Generalized Bass Model Leads to Odd Optimal Advertising Policies*, *International Journal of Research in Marketing* **28** (2011), 218–230. DOI:10.1016/j.ijresmar.2011.03.005. Accessible author-distributed text: https://www.academia.edu/17669574/Why_the_Generalized_Bass_Model_leads_to_odd_optimal_advertising_policies.
3. D. R. Lehmann and M. Esteban-Bravo, *When Giving Some Away Makes Sense to Jump-Start the Diffusion Process*, *Marketing Letters* **17** (2006), 243–254. DOI:10.1007/s11002-006-7942-9. Full text: https://business.columbia.edu/sites/default/files-efs/pubfiles/2671/giving_away_some.pdf.
4. S. A. Delre, W. Jager, T. H. A. Bijmolt, and M. A. Janssen, *Targeting and Timing Promotional Activities: An Agent-Based Model for the Takeoff of New Products*, *Journal of Business Research* **60** (2007), 826–835. DOI:10.1016/j.jbusres.2007.02.002. Accessible abstract: https://research.rug.nl/en/publications/targeting-and-timing-promotional-activities-an-agent-based-model-/.
5. *A Complete Stochastic-Ordering Law for Phased Innovation and Imitation Campaigns* (2026), publicly indexed mathematical result, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-a-complete-stochastic-ordering-law-for-phased-innovation-and-imi--d4e238d7e82e.
6. *Two Preference Reversals Between Marketing Regimes with Customer Attrition* (2026), publicly indexed mathematical result, https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-two-preference-reversals-between-marketing-regimes-with-customer--010583627893.
