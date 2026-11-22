# Two sharp shelterbelt separation thresholds and increasing optimal leeward gaps

## Finding

Consider a finite one-directional field protected by three identical, zero-width windbreak rows. In the exponential wind-recovery model specified below, the unique placement maximizing integrated wind-speed reduction undergoes **two exact separation transitions** as field length increases. Initially all three rows coincide at the upwind edge; then only the last row moves downstream; finally all three rows have distinct positions. In every non-clustered optimum, consecutive downwind gaps (including the unprotected terminal interval) are strictly increasing.

Precisely, let attenuation \(a\in(0,1)\), recovery rate \(k>0\), field length \(L>0\), \(E=e^{-kL}\), and \(E_1=a(2-a)\). There is a unique \(E_2\in(0,E_1)\) satisfying
\[
\sqrt{\frac{E_2}{a(2-a)}}+\frac{1-a}{a}E_2=1.
\]
The uniquely optimal placement \(0=z_1\le z_2\le z_3\le L\), with \(x=e^{-kz_2}\) and \(y=e^{-kz_3}\), is classified as follows.

1. For \(E\ge E_1\), \(x=y=1\), so all three rows coincide at the upwind edge.
2. For \(E_2\le E<E_1\), \(x=1\) and \(y=\sqrt{E/E_1}\), so the first two rows coincide and the third lies strictly within the field. At \(E=E_2\), these formulas remain unique and mark the onset of further separation.
3. For \(0<E<E_2\), the unique maximizer satisfies \(E<y<x<1\), with
\[
 x=\sqrt{y+\frac{1-a}{a}E},\qquad
 E=a y^2\left(1-a+\frac1x\right).
\]
The scalar equation has exactly one solution \(y\in(E,1)\) in this regime.

When \(E<E_1\), put \(g_1=kz_2\), \(g_2=k(z_3-z_2)\), and \(g_3=k(L-z_3)\). Then \(0\le g_1<g_2<g_3\). Equality in the first inequality occurs only when the first two rows coincide. The transition field lengths are \(kL=\log(1/E_1)\) and \(kL=\log(1/E_2)\).

For \(a=1/2\), the two thresholds are exactly \(E_1=3/4\) and \(E_2=1/3\). At \(E=1/9\), the uniquely optimal placement is \((x,y)=(2/3,1/3)\); it has dimensionless integrated deficit \(17/18\), compared with \(7/9\) for three co-located rows, a relative improvement of \(3/14\).

## Assumptions and scope

The wind-speed fraction \(u(z)\) is relative to a constant unobstructed ambient speed. Immediately before the first row at \(z_1=0\), \(u(0^-)=1\). Each identical row has negligible width and causes \(u(z_i^+)=(1-a)u(z_i^-)\). Between rows \(u'(z)=k(1-u(z))\). At coincident row positions all jumps are applied consecutively. The row order is fixed by downstream distance and all three rows are retained. Position constraints are \(0=z_1\le z_2\le z_3\le L\); the first row is pinned at the field's upwind edge. No other controls, penalties, row widths, or aerodynamic interactions are included.

The objective is the *whole-field* integrated wind-speed reduction
\[
 S=k\int_0^L(1-u(z))\,dz,
\]
which is dimensionless. The dimensional integral is \(S/k\). The result is about the linear recovery-plus-multiplicative-jump surrogate, not a universal law for turbulent flows, tree growth, or optimum agricultural planting.

## Proof

**1. An exact objective.** Every row produces an instantaneous deficit increment equal to \(a\) times the incoming speed. A deficit created at position \(z\) subsequently contributes its increment times \(1-e^{-k(L-z)}\) to \(S\). Write \(x=e^{-kz_2}\), \(y=e^{-kz_3}\), so \(E\le y\le x\le1\). The incoming speed at row two is \(1-ax\); at row three it is \(1-ay-a(1-ax)y/x\). Summing the three discounted deficit increments gives
\[
S(x,y)=a(1-E)+a(1-ax)(1-E/x)+a[1-ay-a(1-ax)y/x](1-E/y).
\tag{1}
\]
These formulas include all coincidences and endpoints by continuity and by applying the sequential jump rule.

**2. Eliminate the second-row position.** Direct differentiation yields
\[
\frac{\partial S}{\partial x}=
\frac{a}{x^2}\left(E(1-a)+ay-ax^2\right),\qquad
\frac{\partial S}{\partial y}=a\left(\frac{E}{y^2}-a(1-a)-\frac{a}{x}\right).
\tag{2}
\]
For each fixed \(y\in[E,1]\), the first derivative changes from positive to negative exactly at \(\sqrt{y+E(1-a)/a}\). This candidate is strictly larger than \(y\) for \(y<1\). Thus the sole maximizing admissible \(x\) is
\[
X_E(y)=\min\left\{1,\sqrt{y+\frac{1-a}{a}E}\right\}.
\tag{3}
\]
The endpoint \(y=1\) also gives \(X_E(1)=1\).

**3. A strictly monotone reduced derivative.** Define
\[
F_E(y)=a y^2\left(1-a+\frac{1}{X_E(y)}\right).
\tag{4}
\]
On the branch \(X_E(y)=1\), this is \(a(2-a)y^2\). On the other branch, it is \(a(1-a)y^2+ay^2/\sqrt{y+E(1-a)/a}\). Both branches are strictly increasing: the last term has positive derivative because for \(c\ge0\),
\[
\frac{d}{dy}\frac{y^2}{\sqrt{y+c}}=
\frac{y(3y/2+2c)}{(y+c)^{3/2}}>0.
\]
The branches join continuously, so \(F_E\) is strictly increasing on \([E,1]\). Furthermore \(X_E(E)\ge\sqrt{E}\), whence
\[
\frac{F_E(E)}{E}\le aE(1-a)+a\sqrt E<a(2-a)<1,
\qquad F_E(1)=a(2-a)=E_1.
\]
By (2) and the envelope theorem (or direct one-sided differentiation at the branch join), the sign of the reduced derivative \(dS(X_E(y),y)/dy\) is the sign of \(E-F_E(y)\). Consequently, if \(E\ge E_1\), the reduced objective strictly increases to its unique maximum at \(y=1\). If \(E<E_1\), it strictly increases and then decreases, with the unique maximizing \(y\in(E,1)\) specified by \(F_E(y)=E\). Hence the global optimum is unique for every \(a\in(0,1)\) and \(E\in(0,1)\).

**4. The second transition.** On the branch \(X_E(y)=1\), the reduced critical equation has the unique root \(y=\sqrt{E/E_1}\). This branch is admissible precisely when
\[
\sqrt{\frac{E}{E_1}}+\frac{1-a}{a}E\ge1.
\]
The left side is strictly increasing from zero as \(E\) increases and exceeds one at \(E=E_1\). Therefore it crosses one exactly once at \(E=E_2\in(0,E_1)\). This proves all three regimes and their equality cases.

**5. Strictly increasing optimal gaps.** In the intermediate regime, \(g_1=0<g_2\). In the fully separated regime, equation (3) gives \(x^2=y+E(1-a)/a>y\), and thus \(g_1<g_2\). In either non-clustered regime, equation (4) at its maximizing root gives
\[
\frac{y^2}{Ex}=\frac{1}{a(1+(1-a)x)}>1,
\]
since \(a(1+(1-a)x)\le a(2-a)<1\). Thus \(y^2>Ex\), equivalently \(g_2<g_3\).

**6. Exact instance.** With \(a=1/2\), one has \(E_1=3/4\), while the defining equation for \(E_2\) is \(\sqrt{4E_2/3}+E_2=1\), solved uniquely in \((0,E_1)\) by \(E_2=1/3\). For \(E=1/9\), the strictly interior stationarity equations give \((x,y)=(2/3,1/3)\), and substitution into (1) yields \(S=17/18\). At \((x,y)=(1,1)\), (1) gives \(S=7/9\), so the ratio of their difference to \(7/9\) is \(3/14\).

## Verification

Run the standalone program with `python3 verify_windbreak.py` using the Python standard library. Its actual execution passed 83,416 deterministic checks. It independently computes the state-evolution integral and the discounted-impulse formula on 5,000 sampled placements, verifies the two rational thresholds and the rational optimization example, and compares each proposed global maximum with numerous randomly sampled and boundary placements across wide attenuation and field-length ranges. Exact rational checks use `fractions.Fraction`. The program's finite parameter sampling is not a proof of the universal classification; the global proof is given above. The scalar roots in the full-separation regime can be reproduced by bisection on strictly increasing \(F_E\).

## Relationship to prior work

Windbreak spacing and area of protection are classical applied problems. Woodruff and Zingg (1953) measured protection as a function of shelterbelt structure in a wind tunnel; Woodruff (1956) compared principal and supplemental shelterbelt spacings. Those works motivate field-integrated protection and multiple rows but use physical wind-tunnel measurements and different row arrangements, not the three-identical-jump exponential-recovery global optimizer with its two sharp length thresholds. Zhu, Jiang, and Matsuzaki (2002) relate optimal spacing to porosity, wind-reduction targets, and tree height. Its accessible abstract does not provide this exact theorem, but its full paper was not inspected and historical coverage cannot be excluded. Sun and collaborators (2022) analyze field and numerical spacing according to wind-damage thresholds; Wang and collaborators (2024) analyze single and double shelterbelts by large-eddy simulation. Their stated design objectives and flow fields differ from the surrogate and exact whole-field integral here. General exponential impulse and periodic runoff results optimize different state transitions or objectives; their conclusions do not directly imply both thresholds, full uniqueness, or the strict leeward-gap ordering proved here. This is a claim of a mathematically new classification relative to inspected sources, not a guarantee of historical priority.

## Limitations

The model assumes instantaneous uniform multiplicative wind attenuation, identical row effects, constant exponential downstream relaxation, no upstream influence, zero row width, and fixed first-row placement. Actual turbulence, porosity, orientation, topography, crop-height variability and boundary-layer recirculation can invalidate these assumptions. At short horizons the optimizer requires coincident rows; if field engineering requires strictly separated rows, some optima are only suprema approachable by small positive gaps, not feasible maxima. The strict increasing-gap rule is specific to this simplified integrated-protection objective and is not a universal planting recommendation. No field measurements or calibrated predictive errors are supplied. The relevant 2002 spacing paper was inspected at abstract and bibliographic level only; more general historical analytic solutions may exist. Independent external mathematical audit has not been performed.

## References

- N. P. Woodruff and A. W. Zingg, *Wind Tunnel Studies of Shelterbelt Models*, Journal of Forestry 51(3), 173–178 (March 1953), https://doi.org/10.1093/jof/51.3.173 ; lawful USDA reprint: https://infosys.ars.usda.gov/WindErosion/publications/Andrew_pdf/474.pdf .
- N. P. Woodruff, *The Spacing Interval for Supplemental Shelterbelts*, Journal of Forestry 54(2), 115–122 (February 1956), lawful USDA reprint: https://infosys.ars.usda.gov/WindErosion/publications/Andrew_pdf/524.pdf .
- J. Zhu, F. Jiang and T. Matsuzaki, *Spacing interval between principal tree windbreaks*, Journal of Forestry Research 13(2), 83–90 (2002), https://doi.org/10.1007/BF02857227 .
- Q. Sun and collaborators, *The optimal spacing interval between principal shelterbelts of the farm-shelter forest network*, Environmental Science and Pollution Research (2022), https://doi.org/10.1007/s11356-021-17272-1 .
- J. Wang and collaborators, *Windbreak Effectiveness of Single and Double-Arranged Shelterbelts: A Parametric Study Using Large Eddy Simulation*, Forests 15(10), 1760 (2024), https://doi.org/10.3390/f15101760 .
