# Two sharp thresholds and an inverse timing law for an idealized wet-to-dry wildfire hazard proxy

## Finding
For an idealized antecedent-moisture perturbation, the competing trajectories of transient fuel stock and fuel dryness can generate a local hazard peak, a trough, and a delayed rebound even though both component variables are individually monotone. There are two different sharp thresholds: the first creates the peak–trough pair; the second causes the early peak to overtake the final baseline. At a specific two-to-one rate ratio the two turning times recover the characteristic drying time and fuel surplus without fitting the entire trajectory.

## Assumptions and scope
Fix \(B,A,k,h>0\). On elapsed time \(t\in[0,\infty)\), the idealized additional fuel anomaly is \(A e^{-kt}\), the background fuel stock is \(B\), and a dimensionless dryness factor recovering from zero is \(1-e^{-ht}\). Their product is the *index*, not a calibrated probability,
\[
H(t)=(B+A e^{-kt})(1-e^{-ht}).
\]
Define \(r=k/h\) and \(a=A/B\). The model deliberately holds all other ignition drivers fixed; no causality is inferred from observational fire records. The plateau is \(\lim_{t\to\infty} H(t)=B\) and the initial value is \(H(0)=0\). The first-public motivating source date is 2024-01-19. Primary classification: MSC2020 86A08 (climate science and climate modeling).

**Complete phase classification.** If \(0<r<1\), exactly one finite critical point exists and it is a strict global maximum, with value greater than \(B\). If \(r=1\), the function is strictly increasing with no positive finite critical point for \(0<a\le1\), whereas for \(a>1\) it has one strict global maximum above \(B\). If \(r>1\), put
\[
a_c=\left(\frac{r+1}{r-1}\right)^{r-1},\qquad
 a_g=\frac{r^r}{(r-1)^{r-1}}.
\]
These satisfy \(1<a_c<a_g\). For \(0<a<a_c\), \(H\) strictly increases with no finite stationary point; at \(a=a_c\) it strictly increases but has one non-extremal horizontal tangent; for \(a>a_c\), it has **exactly two** finite stationary times, an earlier strict local maximum followed by a strict local minimum. The early local maximum exceeds, equals, or falls short of \(B\) as \(a\) is greater than, equal to, or less than \(a_g\), respectively. For \(a<a_g\), the global supremum is \(B\) and is not reached at finite time; at \(a=a_g\) a finite maximum attains \(B\); for \(a>a_g\) the finite early local maximum is the unique global maximum.

**Turning-time inverse at rate ratio two.** For \(k=2h\), a peak and a subsequent trough exist exactly when \(a>3\). If their exact times are \(0<t_1<t_2\), then \(h\) is uniquely recovered from
\[
e^{-h t_1}+e^{-h t_2}=\frac23,
\]
and the other parameters are \(k=2h\), \(a=e^{h(t_1+t_2)}/3\). If the absolute plateau \(B\) is known, \(A=aB\). If not, any one nonzero indexed hazard measurement at a known finite positive time recovers \(B\) after \(h,a\) are identified. Thus the turning-time pair gives an exact inverse; the sum identity is independently testable if a drying rate is also measured.

## Proof
Set \(z=e^{-ht}\in(0,1]\). Then \(H(t)/B=f(z)=(1+a z^r)(1-z)\), and direct differentiation yields
\[
\frac{H'(t)}{Bh z}=1-a g_r(z),\qquad
g_r(z)=z^{r-1}[r-(r+1)z],
\]
\[
g_r'(z)=r z^{r-2}[(r-1)-(r+1)z].
\]
Because \(z\) strictly decreases from one toward zero, every positive root of \(a g_r(z)=1\) produces exactly one finite stationary time.

If \(0<r<1\), \(g_r\) strictly decreases on \((0,1]\) from positive infinity to \(-1\), so the equation has exactly one root; \(H'\) changes from positive to negative as time increases. Since \(H(t)-B=Bz[a z^{r-1}(1-z)-1]\) is positive for sufficiently small \(z\), that maximum exceeds \(B\). If \(r=1\), \(g_1(z)=1-2z\), whose range for \(z>0\) is strictly less than one. A root exists exactly when \(a>1\), with the same maximum conclusion.

For \(r>1\), \(g_r\) is positive precisely on \((0,r/(r+1))\); it rises to a *unique* maximum at \(z_*=(r-1)/(r+1)\) and then decreases. Its maximum is
\[
g_r(z_*)=\left(\frac{r-1}{r+1}\right)^{r-1}=\frac1{a_c}.
\]
The equation \(a g_r(z)=1\) therefore has zero, one tangent, or two positive roots according as \(a<a_c\), \(a=a_c\), or \(a>a_c\). For two roots \(0<z_-<z_*<z_+<r/(r+1)\), the corresponding chronological order is \(t_+=-\log z_+/h<t_-=-\log z_-/h\). The sign pattern of \(H'\) is positive, negative, positive. At equality the derivative is nonnegative and vanishes at one isolated point, so \(H\) still strictly increases.

To determine the global optimum, the exact inequality
\[
H(t)>B\quad\Longleftrightarrow\quad a z^{r-1}(1-z)>1
\]
holds for finite positive time. On \((0,1)\), the latter factor has its unique maximum at \(z_g=(r-1)/r\), equal to \((r-1)^{r-1}/r^r=1/a_g\). Thus early overshoot occurs precisely at \(a>a_g\), with equality only at \(a=a_g\). Since \(z_g>z_*\) and \(g_r(z_g)<g_r(z_*)\), the threshold \(a_g=1/g_r(z_g)\) is strictly greater than \(a_c\). This proves the complete global ordering including all boundaries.

For \(r=2\), the stationary equation is \(3a z^2-2a z+1=0\). Its roots, the exponentials of the two turning times, have sum \(2/3\) and product \(1/(3a)\). The function \(h\mapsto e^{-ht_1}+e^{-ht_2}\) is continuous and strictly decreasing from two to zero for any fixed \(0<t_1<t_2\); hence it crosses \(2/3\) exactly once. The product identity then yields the stated unique \(a\). The strict inequality \(a>3\) follows because distinct positive roots of sum \(2/3\) have product strictly less than \(1/9\).

## Verification
In exact arithmetic choose \(r=2\), \(a=25/3\), and \(h=B=1\). The stationary phases are \(z_+=3/5\) and \(z_-=1/15\), so the strict local maximum occurs at \(t_1=\log(5/3)\) and the strict local minimum at \(t_2=\log(15)\). Their values are exactly
\[
H(t_1)=\frac85,\qquad H(t_2)=\frac{392}{405},\qquad \lim_{t\to\infty}H(t)=1.
\]
Thus the apparent early fire-risk surge is greater than the late baseline, the intervening trough is below it, and the terminal rebound is real. The same exact extremal phases satisfy \(3/5+1/15=2/3\) and recover \(a=(25/3)\) by the inverse timing law. At the second threshold \(a=4\) the exact phases are \(1/2\) and \(1/6\), and the early maximum is exactly the late plateau. At the first threshold \(a=3\) the two stationary phases merge to \(z=1/3\) without an actual local extremum.

Run `python checker.py` from the directory containing the included standalone checker. It performs supplementary numerical checks over broadly varying positive rates and exact-witness assertions; the calculus proof above, not finite testing, proves the universal statements.

## Relationship to prior work
The motivating observational study [1] identifies wetter antecedent conditions promoting later fuel growth followed by drought and wildfire, but does not define this two-exponential product, prove its exact phase diagram, or recover decay rates from turning-time pairs. The fuel-moisture model study [2] compares empirical moisture models, some exponential in atmospheric variables, but does not analyze a multiplied transient fuel-stock/drying-trajectory index or its sharp double turning threshold. The global fuel-model paper [3] dynamically tracks fuel and moisture; its full text contains forward dynamical modelling and observational validation, not the present toy-proxy classification.

Elementary root counting and elementary one-variable maximization are standard methods and are not independently claimed as new. The asserted narrower mathematical contribution is their complete implication for this explicitly specified wet-to-dry fuel-and-dryness index, including its two inequivalent thresholds and two-turning-time inverse. A historical priority gap remains possible in hydrological or fire-danger papers that use an equivalent three-exponential response formula without these terms.

## Limitations
The model is a deliberately simplified deterministic *proxy*, not an empirical wildfire ignition probability or a calibrated fuel-moisture law. It assumes one fuel surplus decays exponentially and dryness recovers monotonically to one; it omits precipitation recurrence, feedback on biomass, seasonality, atmospheric instability, ignition sources, suppression and stochastic error. The inverse relation uses exact turning times and the imposed \(k=2h\); no statistical stability guarantee is claimed. The supplied source dates establish the motivating literature window, not historical priority of all possible algebraic equivalents. No independent validation of the theorem has been performed.

## References
1. Alizadeh, M. R., Adamowski, J., and Entekhabi, D. (2024). *Land and Atmosphere Precursors to Fuel Loading, Wildfire Ignition and Post-Fire Recovery*. Geophysical Research Letters 51, e2023GL105324. First online 2024-01-19. https://doi.org/10.1029/2023GL105324
2. Sharples, J. J., and colleagues (2024). *Evaluation and comparison of simple empirical models for dead fuel moisture content*. International Journal of Wildland Fire 33(6). First online 2024-06-13. https://doi.org/10.1071/WF23120
3. McNorton, J. R., and Di Giuseppe, F. (2024). *A global fuel characteristic model and dataset for wildfire prediction*. Biogeosciences 21, 279–300. Open discussion began 2023-09-13. https://doi.org/10.5194/bg-21-279-2024
