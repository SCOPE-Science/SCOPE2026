# A sharp antecedent-heat threshold and universal early-shading offset for one agrivoltaic window

## Finding

Consider a fixed-duration, possibly partial shade interval in a single-time-constant heat-balance model. A previously heated crop canopy need not benefit from placing this interval near the middle of an otherwise uniformly illuminated day: there is an exact initial-heat threshold above which shading should begin immediately. Below that threshold a unique interior start is best, strictly earlier than the midpoint of the available start-time interval. Stronger shade delays that interior start, whereas greater initial heat advances it. For a long day and fixed initial heat below the unshaded equilibrium, the optimal start is advanced from the available-window midpoint by a universal leading amount that does not depend on shade strength.

Write \(H>d>0\), \(0<\rho\le1\), and \(m\ge0\). For every start \(s\in[0,H-d]\), let \(x_s\) be the continuous solution of

\[
 x_s'(t)=1-\rho\,\mathbf 1_{[s,s+d]}(t)-x_s(t),\qquad x_s(0)=m,\qquad 0\le t\le H.
\]

The fixed-duty quadratic heat-exposure objective is \(Q(s)=\int_0^H x_s(t)^2\,dt\). Put

\[
 b=e^{-d},\quad C=e^{-(H-d)},\quad
 m_{\mathrm{crit}}=1-\frac{2C-\rho(1-b)C^2}{1+bC^2}.
\]

**Complete optimizer classification.** If \(m\ge m_{\mathrm{crit}}\), then \(s_*=0\) is the unique global minimizer. This includes every \(m\ge0\) when \(m_{\mathrm{crit}}\le0\). If \(0\le m<m_{\mathrm{crit}}\), the unique global minimizer is \(s_*=-\log q_*\), where \(q_*\) is the unique root in \((C,1)\) of

\[
 (m-1)q^3+\bigl(2C+b(m-1)C^2\bigr)q-\rho(1-b)C^2=0.
\]

Always \(0\le s_*<(H-d)/2\). Within the interior regime \(s_*\) is strictly decreasing in \(m\) and strictly increasing in \(\rho\), with \(H,d\) fixed. For fixed \(d>0\), fixed \(\rho\in(0,1]\), and fixed \(0\le m<1\), as \(H\to\infty\),

\[
 s_* = \frac{H-d}{2}-\frac12\log\frac{2}{1-m}
       + O\!\left(e^{-(H-d)/2}\right).
\]

In particular a cold initial canopy (\(m=0\)) has limiting advance \(\tfrac12\log2\) thermal time units, independent of \(d\) and \(\rho\).

## Assumptions and scope

All times above are dimensionless. From a physical relaxation rate \(\lambda>0\), physical day length \(T\), shade duration \(\delta\), and shade start \(t_0\), set \(H=\lambda T\), \(d=\lambda\delta\), and \(s=\lambda t_0\). The state \(x\) is excess thermal load normalized by the constant full-sun forcing equilibrium. During the single shading interval the forcing falls from \(1\) to \(1-\rho\), with unchanged relaxation rate. The initial state \(m\) may exceed the unshaded equilibrium. The interval is constrained to lie wholly in the day. The objective is cumulative squared thermal load, not temperature peak, harvest, or photon-derived carbon gain. Under a constant full-sun irradiance and a fixed \(\rho d\), the removed solar forcing is the same for every allowed placement; the result isolates the effect of thermal memory on timing.

## Proof

Fix the parameters and write \(q=e^{-s}\), \(r=e^{-(H-s-d)}=C/q\), and \(a=1+(m-1)q\). Elementary solution of the linear differential equation yields

\[
 x_s(t)=\begin{cases}
  1+(m-1)e^{-t},&0\le t<s,\\
  1-\rho+\bigl(\rho+(m-1)q\bigr)e^{-(t-s)},&s\le t<s+d,\\
  1-\bigl(\rho(1-b)-b(m-1)q\bigr)e^{-(t-s-d)},&s+d\le t\le H.
 \end{cases}
\]

Differentiating the three explicit squared-state integrals with respect to the shared moving start, including the interval endpoints, gives

\[
 Q'(s)=\frac{\rho(1-b)}{q^2}P(q),\qquad
 P(q)=(m-1)q^3+\bigl(2C+b(m-1)C^2\bigr)q-\rho(1-b)C^2.
\]

All prefactors outside \(P\) are positive. The endpoint signs simplify exactly to

\[
 P(C)=C^2\bigl[2-\rho(1-b)+(m-1)(1+b)C\bigr]>0,
 \quad
 P(1)=(1+bC^2)(m-m_{\mathrm{crit}}).
\]

Indeed, the bracket in \(P(C)\) is bounded below by \((1+b)(1-C)>0\), using \(m\ge0\) and \(\rho\le1\). Also \(m_{\mathrm{crit}}<1\), because \(2C-\rho(1-b)C^2>0\).

If \(m\ge1\), then

\[
 P(q)=(m-1)q(q^2+bC^2)+2Cq-\rho(1-b)C^2>0
\]

for every \(C\le q\le1\); hence \(Q\) increases strictly. If \(0\le m<1\), then \(P''(q)=6(m-1)q<0\) for all \(q>0\), while \(P(0)<0\), \(P(C)>0\), and \(P(q)\to-\infty\) as \(q\to\infty\). Strict concavity and these signs give exactly two positive roots, one in \((0,C)\) and one in \((C,\infty)\). On the physical interval \(q\in[C,1]\), the upper root lies in \((C,1)\) exactly when \(m<m_{\mathrm{crit}}\). As \(s\) increases, \(q=e^{-s}\) decreases: the derivative of \(Q\) is then negative followed by positive, so the upper root is the unique global minimum. If \(m\ge m_{\mathrm{crit}}\), the derivative is positive for all strictly positive feasible starts, making \(s=0\) uniquely minimizing (also at equality).

At the available-window midpoint \(s=(H-d)/2\), \(q=\sqrt C\) and

\[
 P(\sqrt C)=C^{3/2}\left[m(1+bC)+(1-\sqrt C)(1+b\sqrt C)
 +(1-\rho)(1-b)\sqrt C\right]>0.
\]

Since the objective has only the classified minimum, that minimum always occurs strictly before the midpoint. For the interior root, \(P_q(q_*)<0\) because it is the larger positive root of a strictly concave cubic; furthermore \(P_m=q(q^2+bC^2)>0\) and \(P_\rho=-(1-b)C^2<0\). Implicit differentiation of \(P(q_*)=0\), followed by \(s_*=-\log q_*\), proves the stated strict monotonicities.

Finally, fix \(m<1\), \(d\), and \(\rho\), and let \(C\to0\). Then \(m_{\mathrm{crit}}\to1\), so the interior regime eventually applies. Substituting \(q=\sqrt C\,z\) into \(P(q)=0\), dividing by \(C^{3/2}\), and taking \(C\to0\) gives

\[
 (m-1)z^3+2z+O(\sqrt C)=0.
\]

The relevant positive simple root tends to \(\sqrt{2/(1-m)}\), with error \(O(\sqrt C)\) by the implicit-function theorem. Taking negative logarithms gives the expansion displayed in the finding.

## Verification

The standalone Python 3 program `verify.py` uses only the standard library. It evaluates the explicit solution, integrates its squared trajectory numerically, compares the exact derivative to centered finite differences, checks the cubic optimizer against finite grids over random parameter choices, tests monotonicities, and checks the large-horizon expansion. In the recorded run it completed 51,592 assertions; these tests supplement rather than replace the proof. A separate symbolic differentiation of the three integrated pieces also reduced the difference from the displayed derivative to zero.

For \(H=4\), \(d=1\), \(m=0\), and \(\rho=1\), the root gives \(s_*\approx1.1846878064\), \(Q(s_*)\approx1.2962948866\), versus \(Q(0)\approx1.5983347606\). The initial-load threshold is \(m_{\mathrm{crit}}\approx0.9020820231\).

## Relationship to prior work

Savalle-Gloire and colleagues (first online June 30, 2024) experimentally compared times of shade under mobile agrivoltaic panels, and discussed the trade-off between shade avoidance, heat, and carbon allocation. Uchanski and colleagues (2023) measured temperature moderation for opaque and semi-transparent agrivoltaic arrays. Weselek and colleagues (2021) evaluated crop yields and microclimates under fixed agrivoltaic installations. These establish the motivation, not the threshold theorem. Earlier greenhouse thermal-control literature (Bailey and Seginer, 1989) considers constrained temperature-integral and energy-cost strategies, not the fixed single window and cumulative squared-state criterion treated here. The calculation is also distinct from general PV orientation/irradiance optimization and unrestricted optimal control: it classifies a restricted, experimentally interpretable shade duty with one specific cost. No universal historical novelty is asserted.

## Limitations

The initial-state threshold is a theorem **only for the stated scalar linear relaxation and squared-load criterion**; it does not demonstrate improved crop yields. Real solar irradiance varies during the day, and partial shading can alter wind, humidity, photosynthesis, evapotranspiration, and heat transfer. Multiple shade windows, nonconstant relaxation, changing irradiance, nonlinear injury, an operating cost, or a maximum-temperature objective can produce different schedules. All asymptotics hold with fixed \(d\), fixed \(\rho>0\), and fixed \(m<1\). The degenerate cases \(\rho=0\), \(d=0\), and \(H=d\) are excluded; with zero shade effect all starts tie. No field calibration or independent external mathematical audit has been performed.

## References

1. Savalle-Gloire, N., Vercambre, G., Chopard, J., Blanchard-Gros, R., Catala, J., Fumey, D., and Gautier, H. (2024), *Transient shading in agrivoltaic greenhouses: its impact on growth, architecture, and dry matter accumulation and partition in tomato plants*. Journal of Horticultural Science and Biotechnology. First online 2024-06-30. https://doi.org/10.1080/14620316.2024.2371593
2. Uchanski, M., Hickey, T., Bousselot, J., and Barth, K. L. (2023), *Characterization of Agrivoltaic Crop Environment Conditions Using Opaque and Thin-Film Semi-Transparent Modules*. Energies 16, 3012. https://doi.org/10.3390/en16073012
3. Weselek, A., et al. (2021), *Agrivoltaic system impacts on microclimate and yield of different crops within an organic crop rotation in a temperate climate*. Agronomy for Sustainable Development 41, 59. https://doi.org/10.1007/s13593-021-00714-y
4. Bailey, B. J., and Seginer, I. (1989), *Optimum Control of Greenhouse Heating*. Acta Horticulturae 245. https://doi.org/10.17660/ActaHortic.1989.245.69
