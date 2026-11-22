# Exact saturation law for heterogeneous electric-vehicle charging equilibrium

## Finding

Consider the two-charging-station, continuum-player, zero-noise pure Nash equilibrium specified below. Write \(\lambda\) for the total EV arrival rate (vehicles per hour), \(h_i\) for the monetary waiting cost at station \(i\), and \(U_i,V_i\) for the normalized first and second energy-demand moments among users assigned to that station. For each \(\lambda<24\) sufficiently close to \(24\), this equilibrium exists uniquely. As \(\lambda\uparrow24\), its limiting station-0 EV population fraction is **\(13/24\)**, although both stations receive precisely one-half of the total energy workload in the limit. If \(\varepsilon=600-25\lambda\) is the aggregate unused charging power and \(\delta_i=300-\lambda U_i\) is the unused power at station \(i\), then

\[
\frac{\delta_0}{\varepsilon}\longrightarrow\frac{23}{48},\qquad
\frac{\delta_1}{\varepsilon}\longrightarrow\frac{25}{48},\qquad
\varepsilon h_0,\ \varepsilon h_1\longrightarrow 1000.
\]

In particular, each waiting cost satisfies \(h_i\sim40/(24-\lambda)\) euros, the *finite* difference of two diverging waiting costs obeys \(h_0-h_1\to-5\) euros, and more sharply

\[
h_0-h_1=-5-\frac5{192}(24-\lambda)+O((24-\lambda)^2).
\]

For \(\lambda\ge24\), there is no allocation with finite waiting costs at both stations. The coefficient \(1000\) is independent of the station-specific second-moment split although that split determines the individual unused-capacity fractions.

## Assumptions and scope

The player characteristic \((y,e)\) is uniformly distributed on \([0,10]\times[0,50]\), with location \(y\) in kilometres and energy demand \(e\) in kilowatt-hours. Charging stations \(0\) and \(1\) are at \(y=3\) and \(y=7\), respectively; their energy prices are \(r_0=1/2\) and \(r_1=7/20\) euros per kilowatt-hour, transport costs are \((3/2)|y-z_i|\) euros, and each station has two charging points delivering \(150\) kW each. Waiting-time valuation is \(\omega=30\) euros per hour. Choices minimize

\[
c_i(y,e)+h_i,\qquad c_i(y,e)=r_ie+\frac32|y-z_i|.
\]

Exactly the source's **approximate** \(M/G/2\) waiting-cost function is used, not a claim about exact stationary queueing delays:

\[
U_i=\int e\,a_i\,d\mu,\quad V_i=\int e^2\,a_i\,d\mu,\quad
h_i=\frac{30\lambda^2U_iV_i}{300(300^2-\lambda^2U_i^2)}
\quad\text{when }\lambda U_i<300,
\]

and the cost is infinite otherwise. Players are nonatomic, so an individual unilateral change does not alter the aggregate queue costs. There is no choice noise. The statement is an analytic limit within this specified static queue-approximation game, not a stochastic queue heavy-traffic limit or a finite-EV prediction.

## Proof

**1. Scalar equilibrium and feasibility.** Put \(\tau=h_0-h_1\) and
\(\Delta(y,e)=c_1(y,e)-c_0(y,e)=z(y)-3e/20\), where
\(z(y)=\frac32(|y-7|-|y-3|)\) equals \(6\) on \([0,3]\), \(15-3y\) on \((3,7)\), and \(-6\) on \([7,10]\). Station 0 is selected if and only if \(\Delta\ge\tau\), with ties having zero population mass. The variable \(z\) has atoms of mass \(3/10\) at each of \(\pm6\) and continuous density \(1/30\) on \((-6,6)\). Thus for \(-6<t<-3/2\), all \(t+3e/20\), \(0\le e\le50\), belong to \((-6,6)\), where
\(\Pr\{z\ge v\}=1/2-v/30\). Exact integration against the uniform energy law gives the station-0 mass and moments

\[
m_0(t)=\frac38-\frac{t}{30},\quad
U_0(t)=\frac{25}{3}-\frac{5t}{6},\quad
V_0(t)=\frac{3125}{12}-\frac{250t}{9}.
\]

The totals are \(U_0+U_1=25\) and \(V_0+V_1=2500/3\). At equilibrium the scalar equation is \(h_0(t,\lambda)-h_1(t,\lambda)=t\). For \(\lambda\) sufficiently close to \(24\) from below, the capacity-feasible interval of thresholds is nonempty and lies in \((-6,-3/2)\), because it is characterized by \(25-300/\lambda<U_0(t)<300/\lambda\). At the lower endpoint station 0 saturates, so the left side minus \(t\) tends to \(+\infty\); at the upper endpoint station 1 saturates, so it tends to \(-\infty\). Since increasing \(t\) lowers both \(U_0,V_0\) and raises both \(U_1,V_1\), and each \(h_i\) is strictly increasing in its two positive moments, this difference is strictly decreasing. There is exactly one feasible root, and it is the pure Nash equilibrium.

**2. Critical threshold and exact limiting shares.** Define \(\delta_i=300-\lambda U_i>0\) and \(\varepsilon=600-25\lambda\). Summing gives \(\delta_0+\delta_1=\varepsilon\). Thus \(\delta_i\to0\) as \(\lambda\uparrow24\), whence \(U_0\to25/2\). The formula for \(U_0(t)\) forces \(\tau\to-5\), at which

\[
m_0=\frac{13}{24},\quad m_1=\frac{11}{24},\quad
V_0=\frac{14375}{36},\quad V_1=\frac{15625}{36}.
\]

Hence the conditional mean demands tend to \(300/13\) and \(300/11\) kWh, respectively, despite equal total energy workloads.

**3. Slack splitting and universal waiting-cost coefficient.** As \(\lambda\uparrow24\), the exact queue formula implies

\[
h_i=\frac{30\lambda V_i}{2\cdot300\,\delta_i}(1+O(\delta_i)),
\]

uniformly for positive \(V_i\) close to their nonzero limits. Since \(h_0-h_1=\tau\to-5\), the leading singular terms must agree. If a subsequential fraction \(\delta_i/\varepsilon\) tended to zero, multiplication of the cost difference by \(\varepsilon\) would yield a contradiction, so both fractions stay positive. Writing their limits as \(q_i\), one obtains \(V_0^*/q_0=V_1^*/q_1\) and \(q_0+q_1=1\). Therefore

\[
q_0=\frac{V_0^*}{V_0^*+V_1^*}=\frac{23}{48},\qquad q_1=\frac{25}{48}.
\]

Substitution gives \(\varepsilon h_i\to30\cdot24(2500/3)/(2\cdot300)=1000\). Since \(\varepsilon=25(24-\lambda)\), this also gives \(h_i\sim40/(24-\lambda)\).

**4. First-order gap.** Put \(\eta=24-\lambda>0\) and write \(\tau=-5+s\eta\). The exactly linear moment formula yields

\[
\delta_0=\eta\left(\frac{25}{2}+\frac{5(24-\eta)}6s\right),\qquad
\delta_1=\eta\left(\frac{25}{2}-\frac{5(24-\eta)}6s\right).
\]

Multiplying the equilibrium equation by \(\eta\) removes the simple queue poles. The resulting equation is analytic near \(\eta=0\) and its limiting equation is
\[
\frac{V_0^*}{25/2+20s}=\frac{V_1^*}{25/2-20s}.
\]

It has the unique feasible root \(s=-5/192\), with strictly nonzero derivative in \(s\). The analytic implicit-function theorem yields \(s=-5/192+O(\eta)\), establishing the claimed \(O(\eta^2)\) remainder. Finally, at \(\lambda\ge24\), finite queue costs would require simultaneously \(\lambda U_0<300\) and \(\lambda U_1<300\), contradicting \(\lambda(U_0+U_1)=25\lambda\ge600\).

## Verification

The standalone `verify.py` checks the exact rational integrations and critical fractions, then solves the original untruncated cost-balance equation by bisection for three arrival rates approaching \(24\). It confirms convergence of the slack fractions, scaled costs and first-order cost-gap coefficient. These finite computations are consistency tests; the infinite-limit statements follow from the proof above.

## Relationship to prior work

Dupont, Petit and Séguret (arXiv:2610.18035v1), Section 4.3, define precisely this heterogeneous-demand, two-station queue-approximation game, prove equilibrium existence/uniqueness using their general results and numerically observe that the energy shares approach one-half, while the station attracting more EVs may consume less energy. The new claim supplies the exact saturation arrival rate, the previously unstated rational **EV-count shares**, second-moment-controlled slack split, common pole coefficient and first-order finite waiting-cost difference. General Wardrop results for heterogeneous delay sensitivities (Bodas, Ganesh and Manjunath, 2021) characterize sorting with a different service-workload assumption; Liu, Pantelidis, Tam and Chow (2021/2023) use a distinct \(M/D/C\) charging queue model. These works do not imply the four specific asymptotic constants under this source's heterogeneous-workload queue formula by direct specialization.

## Limitations

This is a critical-load asymptotic for the specific uniform location–energy distribution and fixed station costs, not a claim of universal empirical EV behaviour. The waiting time is the approximation used in the source, not an exact queue law; finite noise, time-varying demand, queue correlations, and overloaded operation are outside scope. The exact constants do not extend automatically to different pricing, location distributions or charger capacities. The first-order coefficient concerns the **cost difference**, not the individual order-one constants in the divergent costs. The conclusion is literature-bounded; independent assessment of historical priority is not performed.

## References

1. A. Dupont, Q. Petit and A. Séguret, *Non-Potential Congestion Games with a Continuum of Players*, arXiv:2610.18035v1, released 2026-10-13. https://arxiv.org/abs/2610.18035
2. T. Bodas, A. Ganesh and D. Manjunath, *Pigouvian Tolls and Welfare Optimality with Parallel Servers and Heterogeneous Customers*, 2021. https://doi.org/10.1007/s41745-021-00258-w
3. B. Liu, T. P. Pantelidis, S. Tam and J. Y. J. Chow, *An electric vehicle charging station access equilibrium model with M/D/C queueing*, arXiv:2102.05851 (2021). https://arxiv.org/abs/2102.05851
