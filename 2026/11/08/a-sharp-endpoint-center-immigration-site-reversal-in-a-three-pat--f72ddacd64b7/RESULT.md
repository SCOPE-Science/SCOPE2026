# A sharp endpoint–center immigration-site reversal in a three-patch chain

## Finding

Consider three habitat patches arranged as the path \(1-2-3\). Each occupied patch goes locally extinct at rate \(1\). For every occupied–empty neighboring pair, colonization occurs at rate \(c>0\), independently across directed contacts. Exactly one chosen patch additionally receives external immigrants at rate \(1\) whenever it is empty. Let \(\pi_E\) be the stationary law with external immigration at an endpoint (patch \(1\)), and let \(\pi_C\) be the stationary law with external immigration at the center (patch \(2\)).

There is a **unique** \(c_*>0\) at which stationary *full occupancy* changes its maximizing immigration site:

\[
\begin{cases}
\pi_C(\{1,2,3\})>\pi_E(\{1,2,3\}),&0<c<c_*,\\
\pi_C(\{1,2,3\})=\pi_E(\{1,2,3\}),&c=c_*,\\
\pi_C(\{1,2,3\})<\pi_E(\{1,2,3\}),&c>c_*.
\end{cases}
\]

Here \(c_*\) is the unique positive zero of

\[
S(c)=6c^6+28c^5+9c^4-334c^3-990c^2-1038c-360,
\]

and \(3.637677<c_*<3.637678\). **By contrast**, the center is strictly better for *regional occupancy* for every \(c>0\):

\[
\pi_C(\text{at least one occupied patch})>
\pi_E(\text{at least one occupied patch}).
\]

Reflection makes the two endpoints equivalent, so these statements classify **all** choices of one external-immigration gateway on this graph. This is the smallest connected path with inequivalent endpoint and interior immigration choices.

## Assumptions and scope

The state \(A\subseteq\{1,2,3\}\) records occupied patches. The process is a time-homogeneous continuous-time Markov chain with transitions

\[
A\longrightarrow A\setminus\{i\}\quad\text{at rate }1\quad(i\in A),
\]

and

\[
A\longrightarrow A\cup\{i\}\quad\text{at rate }
\mathbf1_{\{i=s\}}+c\,|A\cap N(i)|
\quad(i\notin A),
\]

where \(s\in\{1,2,3\}\) is the chosen external-immigration gateway, and \(N(i)\) denotes its neighbors in the path. All rate-one normalizations are assumptions, not conclusions for arbitrary unequal rates. The external source never disappears, but the designated patch itself is subject to ordinary local extinction. Continuous immigration acts even if other patches remain occupied. Colonization does not remove its donor population. For every \(c>0\), each of the eight occupancy configurations communicates with each other through positive-rate events, so each placement has a unique strictly positive stationary distribution.

## Proof

Index subsets by the three-bit integer \(0,\dots,7\). Form the row generator \(Q_s\) from the displayed transition rates and solve the eight linear equations \(\pi Q_s=0\), \(\sum_A\pi(A)=1\). Exact rational elimination, with no probabilistic or large-population approximation, gives the following compact formulas. Put

\[
D_E=4c^6+34c^5+150c^4+371c^3+548c^2+450c+144
\]

and

\[
D_C=2(c+1)(c^3+5c^2+15c+12).
\]

For the endpoint gateway,

\[
\pi_E(\varnothing)=\frac{16c^4+86c^3+194c^2+201c+72}{D_E},\qquad
\pi_E(\{1,2,3\})=\frac{c^2(4c^4+24c^3+60c^2+64c+21)}{D_E}.
\]

For the center gateway,

\[
\pi_C(\varnothing)=\frac{8c^2+19c+12}{D_C},\qquad
\pi_C(\{1,2,3\})=\frac{c^2(c+2)(2c+3)}{D_C}.
\]

All denominators are strictly positive for \(c>0\). Subtracting the two complete-occupancy probabilities gives the *exact identity*

\[
\pi_E(\{1,2,3\})-\pi_C(\{1,2,3\})=
\frac{c^2S(c)}{D_ED_C}.
\]

The descending coefficients of \(S\) have signs \(+,+,+,-,-,-,-\), with exactly one sign change. Descartes' rule of signs implies **at most** one positive root; \(S(0)=-360<0\) and \(S(c)\to+\infty\) as \(c\to\infty\), so the intermediate-value theorem supplies exactly one. Exact rational evaluation gives \(S(3637677/1000000)<0<S(3637678/1000000)\). This proves the complete full-occupancy classification, including equality and uniqueness.

For regional occupancy, the difference between the endpoint and center **empty-state** probabilities is

\[
\pi_E(\varnothing)-\pi_C(\varnothing)
=\frac{cT(c)}{D_ED_C},
\]

where

\[
T(c)=16c^6+166c^5+808c^4+2111c^3+2980c^2+2112c+576.
\]

Every coefficient of \(T\) is positive, so the empty-state difference is strictly positive for \(c>0\). Taking complements proves strict superiority of center immigration for the event that at least one patch is occupied, at every positive colonization rate.

## Verification

The standalone `check.py` reconstructs both eight-state generators directly from the stated transition rules. It computes both stationary vectors exactly over \(\mathbb Q(c)\), verifies the stationary balance and normalization equations, and checks all four displayed stationary probabilities and both difference factorizations as exact rational identities. It also checks the positivity of the denominator and \(T\)-coefficients, the single coefficient-sign change of \(S\), and the rational root bracket. As an independently organized calculation, it computes stationary weights by principal minors of the negative row generator for seven positive rational colonization rates, comparing all eight weights for each source placement (112 exact comparisons). The analytical polynomial sign argument, not the sampled minors, proves all-parameter uniqueness. Run with `python check.py` and SymPy installed. No other artifacts are required.

For context at \(c=1\), the center full-occupancy probability is approximately \(0.11363636\), versus approximately \(0.10170488\) for an endpoint. At \(c=5\), the corresponding probabilities are approximately \(0.56256182\) and \(0.56474618\). Thus the optimization reversal is not an artefact of merely taking a formal asymptotic limit.

## Relationship to prior work

The source–sink and mainland–island metapopulation paradigm motivates one exogenous immigrant gateway linked to patches subject to extinction and rescue [1,2]. A finite-site contact process with spontaneous infection at a specified site is a well-established mathematical model. Foxall [3], especially §§1–4, establishes the general generator framework, irreducibility, and parameterwise monotonicity for this broader process; its §8 gives a star-network **approximation with positive spontaneous infection throughout**, not the exact gateway-location comparison on the three-site path. Economou, Gómez-Corral, and López-García [4] provide general finite-state SIS calculation methods. Those methods enable evaluation of instances but the inspected material does not state or imply the sharp sign-changing source-location inequality or its strict opposing regional-occupancy comparison. In particular, moving a sole positive immigrant rate from endpoint to center changes the source-rate vector in incomparable coordinates, so standard coordinatewise monotonicity gives no ordering.

## Limitations

The result is an exact, idealized three-patch stationary classification at **fixed equal immigration and extinction rates**. It is not a theorem for arbitrary network sizes, heterogeneous patch qualities, correlated catastrophes, finite-time occupancy, or field interventions. The all-occupied advantage is sometimes quantitatively small. Generic exact finite Markov-chain methods and older metapopulation literature mean independent historical-priority review is still warranted; bibliographic search is not proof of novelty. A potentially relevant 2015 SIS manuscript was accessible only in part during literature inspection; no claim is made that uninspected pages have been ruled out. This is a mathematical benchmark rather than a validated conservation recommendation.

## References

[1] Hanski, I., and Gyllenberg, M. (1993). *Two General Metapopulation Models and the Core-Satellite Species Hypothesis*. American Naturalist 142, 17–41. https://doi.org/10.1086/285527

[2] Freckleton, R. P., and Watkinson, A. R. (2002). *Large-scale spatial dynamics of plants: metapopulations, regional ensembles and patchy populations*. Journal of Ecology. https://doi.org/10.1046/j.1365-2745.2002.00692.x

[3] Foxall, E. (2014). *Convergence and Monotonicity for a Model of Spontaneous Infection and Transmission*. Advances in Applied Probability 46, 560–584. https://doi.org/10.1239/aap/1401369707

[4] Economou, A., Gómez-Corral, A., and López-García, M. (2015; online 2014). *A stochastic SIS epidemic model with heterogeneous contacts*. Physica A 421, 78–97. https://doi.org/10.1016/j.physa.2014.10.054
