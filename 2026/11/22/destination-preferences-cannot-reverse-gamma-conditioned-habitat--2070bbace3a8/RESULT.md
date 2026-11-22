# Destination preferences cannot reverse gamma-conditioned habitat circulation, but observation time can reverse it twice

## Finding
For every cycle of \(n\ge3\) habitats with positive destination-only selection weights and arbitrary positive Gamma densities for the clockwise and counterclockwise route times, the orientation of the unique stationary cycle current of the row-normalized time-conditioned movement matrix is **completely independent of all habitat-selection weights**. As a function of the conditioning duration \(t>0\), this current either vanishes identically or changes sign at most twice, irrespective of \(n\). The bound of two is attained for every \(n\ge3\), even when the clockwise and counterclockwise route times have *the same mean at every habitat*.

Specifically, define \(A,B,C\) below. For every positive \(t\),
\[
\operatorname{sgn}J(t)=\operatorname{sgn}\bigl(C+A\log t-Bt\bigr).
\]
If \(AB>0\), put \(t_*=A/B\) and \(F_*=C+A(\log(A/B)-1)\). There are **exactly two distinct current-direction reversals** if and only if \(AF_*>0\), an isolated zero without reversal if \(F_*=0\), and no zero otherwise. The two reversal times are
\[
t_{-}=-\frac AB W_0\!\left(-\frac BA e^{-C/A}\right),\qquad
 t_{+}=-\frac AB W_{-1}\!\left(-\frac BA e^{-C/A}\right),
\]
where \(W_0,W_{-1}\) are the real Lambert-\(W\) branches, ordered \(t_-<t_+\). A zero-current matrix obeys detailed balance; in the two-reversal regime it is reversible exactly at the two isolated zero-current durations and irreversible at all other positive durations.

## Assumptions and scope
Let \(n\ge3\) be an integer, with habitats labelled modulo \(n\), and let \(q_i>0\) be arbitrary **destination-only** selection weights. For each starting habitat \(i\) and directed neighboring destination, choose arbitrary positive Gamma shape and rate parameters \(\alpha_i^\pm>0\), \(\beta_i^\pm>0\). At conditioning duration \(t>0\), put
\[
f_i^\pm(t)=\frac{(\beta_i^\pm)^{\alpha_i^\pm}}{\Gamma(\alpha_i^\pm)}t^{\alpha_i^\pm-1}e^{-\beta_i^\pm t},
\qquad
p_i^\pm(t)=\frac{q_{i\pm1}f_i^\pm(t)}{q_{i+1}f_i^+(t)+q_{i-1}f_i^-(t)}.
\]
The transition matrix \(P(t)\) has \(P_{i,i+1}(t)=p_i^+(t)\) and \(P_{i,i-1}(t)=p_i^-(t)\), with all other entries zero. The two destinations differ because \(n\ge3\). At every fixed \(t\), \(P(t)\) is irreducible and has a unique positive stationary distribution \(\pi(t)\); periodicity for even \(n\) does not affect uniqueness. Define its clockwise stationary edge flux
\[
J(t)=\pi_i(t)p_i^+(t)-\pi_{i+1}(t)p_{i+1}^-(t),
\]
which does not depend on \(i\). The time-conditioned family \(P(t)\) is **not assumed to form a Markov semigroup**; its stationary currents are separate model summaries for alternative observation durations, not physical currents of one underlying fixed continuous-time process.

All rates are expressed in one chosen time unit. Define dimensionless cycle coefficients by
\[
A=\sum_{i=0}^{n-1}(\alpha_i^+-\alpha_i^-),\quad B=\sum_{i=0}^{n-1}(\beta_i^+-\beta_i^-),
\]
\[
C=\sum_{i=0}^{n-1}\left[\alpha_i^+\log\beta_i^+-\alpha_i^-\log\beta_i^-
-\log\Gamma(\alpha_i^+)+\log\Gamma(\alpha_i^-)\right].
\]
The combination \(C+A\log t-Bt\) is unchanged by a consistent change of time units, though its individual coefficients transform.

## Proof
**1. Conservation and current sign on any cycle.** At fixed \(t>0\), stationarity and the nearest-neighbor structure imply \(J_i=J_{i-1}\) at all sites, so \(J\) is common to every oriented edge. Write \(p_i=p_i^+\), \(r_i=p_i^-=1-p_i\). Rearrange edge balance into the exact recurrence
\[
\pi_{i+1}=\frac{p_i}{r_{i+1}}\pi_i-\frac{J}{r_{i+1}}.
\]
Iterating once around the ring gives \(\pi_i=R\pi_i-JD_i\), where
\[
R=\prod_{j=0}^{n-1}\frac{p_j}{r_j}>0
\]
and \(D_i>0\) is a sum of positive reciprocal-transition products. Thus
\[
J=\frac{\pi_i(R-1)}{D_i},\qquad
\operatorname{sgn}J=\operatorname{sgn}(R-1)=\operatorname{sgn}(\log R).
\]
This proves the oriented-current criterion directly, including equality and all strictly positive boundaries; it does not rely on aperiodic convergence. When \(J=0\), edge-by-edge detailed balance holds, so \(P(t)\) is reversible; the converse is immediate.

**2. Cancellation of all destination preferences.** Row normalization cancels separately in each quotient:
\[
\frac{p_i^+(t)}{p_i^-(t)}=\frac{q_{i+1}}{q_{i-1}}\frac{f_i^+(t)}{f_i^-(t)}.
\]
On the full cycle the destination factors telescope by permutation,
\[
\prod_i\frac{q_{i+1}}{q_{i-1}}=1.
\]
Therefore \(R(t)=\prod_i f_i^+(t)/f_i^-(t)\), and neither its sign nor any time at which it equals one depends on any \(q_i\). The stationary probabilities and *magnitude* of \(J\) generally do depend on these weights; only its direction and zero set are invariant.

**3. Gamma likelihoods and exhaustive root count.** Substituting the positive Gamma densities into \(\log R\) gives exactly
\[
F(t)=\log R(t)=C+A\log t-Bt,\qquad F'(t)=A/t-B.
\]
If \(AB>0\), the only critical point is \(t_*=A/B\), a strict maximum for \(A>0\) or minimum for \(A<0\); the function has the same unbounded sign at both ends. This proves the two/tangent/zero classification using the sign of \(AF_*\). Solving \(F(t)=0\) by rewriting \(t e^{-(B/A)t}=e^{-C/A}\) gives the two real Lambert-\(W\) branches when strict double reversal holds. If \(AB<0\), \(F\) is strictly monotone and tends to opposite infinities, so it has exactly one simple positive zero. If \(B=0,A\ne0\), its sole zero is \(e^{-C/A}\). If \(A=0,B\ne0\), it has one positive zero exactly when \(C/B>0\), namely \(C/B\). If \(A=B=0\), it is identically zero precisely when \(C=0\), otherwise has a fixed nonzero sign. These cases exhaust the domain. In particular, if all routes share a common Gamma *rate*, then \(B=0\) and two reversals are impossible.

**4. Attainment with matched directional means and no selection imbalance.** For every \(n\ge3\), choose \(q_i=1\) everywhere, all clockwise route times distributed as Gamma(shape \(2\), rate \(2\)), and all counterclockwise times distributed as Gamma(shape \(1\), rate \(1\)). Every route has mean one, in either direction, but the clockwise-to-counterclockwise density ratio is \(4te^{-t}\). The transition matrix is homogeneous and has uniform stationary law, so
\[
J(t)=\frac{4te^{-t}-1}{n(4te^{-t}+1)}.
\]
The function \(4te^{-t}\) rises from zero to \(4/e>1\) at \(t=1\), then falls to zero. Hence there are exactly two distinct finite positive roots
\[
t_-=-W_0(-1/4)=0.357402956181389\ldots,\quad
t_+=-W_{-1}(-1/4)=2.153292364110349\ldots.
\]
The current is counterclockwise before \(t_-\), clockwise between the roots, and counterclockwise afterward. This attains the universal two-reversal bound for every permissible ring size despite identical directional means. Any positive destination weights preserve both roots and the direction sequence by Step 2.

## Verification
Run `python3 CHECK.py` using only the Python standard library. It independently solves the stationary linear equations for 2,590 positive cyclic kernels (including heterogeneous destination-weight cases), checks edge-current conservation and its sign against the cycle-product formula, checks exact cancellation under arbitrary destination qualities, and independently locates the two witness roots. These finite calculations corroborate, but do not replace, the all-size and all-parameter proof above. The two displayed roots are decimal approximations, whereas the Lambert-\(W\) expressions are exact.

## Relationship to prior work
Valle et al. (2024) introduced time-explicit habitat selection by multiplying time-to-destination likelihoods by destination or path selection scores and row-normalizing to construct connectivity probabilities. They use Gamma travel-time models, principally with a common rate parameter. The present result specializes selection to destination-only scores on a cycle and allows the **route-specific Gamma rates** needed for a two-reversal regime; it is an analytic consequence for that explicit extension, not a theorem stated by Valle et al. Prima et al. (2024) showed empirically and through movement simulation that sampling frequency can bias estimated connectivity, but did not provide the cycle-current sign invariant or two-reversal bound. Michelot et al. (2019) use a continuous-time Langevin semigroup with habitat-based stationary distribution, a different model that should not be conflated with the time-conditioned kernels here.

Kolmogorov's cycle criterion and the elementary Gamma density ratio are classical precursors, so the cycle-product test and two density intersections **are not claimed as new**. Prior mathematical analyses of switching ratchets bound current reversals as a *physical switching rate* changes (e.g. two-mode reversible landscapes, where the bound depends on site count); another analysis studies reversible sampling of a fixed continuous-time biased ring. Neither has the present destination-weight cancellation and sharp observation-duration phase classification for Gamma-weighted, row-normalized habitat kernels. The specific combined all-size result and the equal-mean counterexample were not located in the inspected literature; this is a provisional originality assessment, not proof of historical priority.

## Limitations
This is a fully specified, idealized, **time-conditioned Markov kernel** on a finite cyclic landscape. The kernels for distinct observation durations need not arise as observations of one consistent physical process; the changing stationary-current sign must not be interpreted as observed reversal of any animal's true direction of travel. The invariance requires destination-only selection weights independent of origin and duration, two allowed nearest-neighbor destinations, and strictly positive Gamma likelihoods. It need not hold for origin/path-dependent selection, self-loops or shortcuts, non-Gamma travel-time families, or physical continuous-time generators. The route-specific Gamma rate variation needed for two reversals extends the common-rate time-model parametrization in the motivating study and has not been ecologically calibrated. These calculations neither establish statistical estimation stability nor prescribe wildlife corridor design. Broader Markov-cycle and special-function literature may include equivalent formulas; independent external review has not been performed.

## References
1. D. Valle et al., “Bridging the gap between movement data and connectivity analysis using the Time-Explicit Habitat Selection (TEHS) model”, *Movement Ecology* 12, 19 (first public 2024-03-01). https://doi.org/10.1186/s40462-024-00461-1
2. M.-C. Prima et al., “Combined effects of landscape fragmentation and sampling frequency of movement data on the assessment of landscape connectivity”, *Movement Ecology* 12, 63 (first public 2024-09-09). https://doi.org/10.1186/s40462-024-00492-8
3. T. Michelot et al., “The Langevin diffusion as a continuous-time model of animal movement and habitat selection”, *Methods in Ecology and Evolution* 10, 1894–1907 (first public 2019-08-02). https://doi.org/10.1111/2041-210X.13275
4. F. P. Kelly, *Reversibility and Stochastic Networks*, Wiley (1979), ch. 1: classical finite Markov-cycle reversibility.
