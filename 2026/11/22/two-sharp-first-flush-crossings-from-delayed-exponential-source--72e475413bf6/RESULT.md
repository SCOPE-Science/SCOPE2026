# Two sharp first-flush crossings from delayed exponential source mixing

## Finding

A stormwater event can have a **positive early mass-over-volume surplus, a negative middle surplus, and a positive late surplus**, even though each of two contributing pollutant sources has strictly declining exponential mass release after it becomes active. In the two-source delayed model below, the exact necessary and sufficient condition for this pattern, equivalently for exactly two interior crossings of the cumulative mass–volume bisector, is

\[
L(a,d)<w<\min\{U_0(a),U_1(a,d)\}.
\]

The open interval exists for every positive wash-off rate and every strictly interior delay. The competing upper boundaries exchange dominance at one exact delay, and the window shrinks **linearly** for small delay but **quadratically** as the second source activates just before the end. For this specified model there are never more than two interior crossings.

## Assumptions and scope

Normalize the total runoff volume and exported pollutant mass each to one. Let \(v\in[0,1]\) be cumulative runoff-volume fraction; assume \(a>0\), a fixed activation delay \(d\in(0,1)\), and the delayed source's fraction \(w\in(0,1)\) of event-total pollutant mass. The two source-specific wash-off densities, normalized separately to integrate to one, are

\[
f_1(v)=\frac{ae^{-av}}{1-e^{-a}}\quad(0\le v\le1),
\]
\[
f_2(v)=\begin{cases}0,&0\le v\le d,\\ \frac{ae^{-a(v-d)}}{1-e^{-a(1-d)}},&d<v\le1.\end{cases}
\]

The value of the density at \(d\) is immaterial; its cumulative distribution is continuous. Define \(F_1(v)=(1-e^{-av})/(1-e^{-a})\), and \(F_2(v)=0\) for \(v\le d\), while \(F_2(v)=(1-e^{-a(v-d)})/(1-e^{-a(1-d)})\) for \(v>d\). The event-level mass–volume curve is \(F(v)=(1-w)F_1(v)+wF_2(v)\). Positive \(F(v)-v\) means proportionally more pollutant mass than runoff volume has been discharged by that fraction, and is not a statement that the concentration is necessarily increasing at that instant.

Define the exact quantities

\[
L=1-\frac{d(1-e^{-a})}{1-e^{-ad}},\qquad
U_0=1-\frac{1-e^{-a}}{a},
\]
\[
c=\frac{a}{e^a-1},\quad z=\frac{a}{e^{a(1-d)}-1},\quad
U_1=\frac{1-c}{z-c}.
\]

The denominator of \(U_1\) is positive because \(0<d<1\); \(0<L<\min\{U_0,U_1\}\). Here \(U_1\) may exceed one, which does not affect the condition since \(U_0<1\).

## Proof

Put \(H(v)=F(v)-v\). On each open interval \((0,d)\) and \((d,1)\), the function \(H\) is twice continuously differentiable and strictly concave, because its second derivative is the derivative of a strictly positive decreasing sum of exponentials. It is continuous at \(d\), with \(H(0)=H(1)=0\). A strictly concave function on an interval whose value vanishes at one endpoint has at most one additional zero inside that interval: its secant slopes from that endpoint decrease strictly.

At the delay, \(H(d)=(1-w)F_1(d)-d\), so \(H(d)<0\) if and only if \(w>L\). If \(H(d)\ge0\), strict concavity together with both endpoint values rules out any pair of interior zeros. If \(H(d)<0\), strict concavity on \([0,d]\) gives exactly one zero in \((0,d)\) if and only if \(H'(0+)>0\), equivalently \(w<U_0\); otherwise the function is strictly negative on \((0,d]\). On \([d,1]\), exactly one zero in \((d,1)\) exists if and only if \(H'(1-)<0\), equivalently \(w<U_1\). Thus the claimed three strict inequalities are jointly necessary and sufficient, and the two roots are unique within their respective intervals. At every boundary equality the relevant crossing is lost, so the inequalities are sharp. At admissible weights the signs follow the continuous concave shape: positive near zero, negative around \(d\), positive near one.

It remains to prove that the interval is nonempty for every \(a,d\). Set \(w=L\), for which \(H(0)=H(d)=H(1)=0\). Strict concavity on \([0,d]\) then implies \(H'(0+)>0\), so \(L<U_0\). Strict concavity on \([d,1]\) implies \(H'(1-)<0\), so \(L<U_1\). Also \(L>0\) because \(F_1(d)>d\), a consequence of the strictly decreasing normalized early-source density. Consequently there are admissible \(w\) immediately above \(L\).

For fixed \(a\), \(U_0\) is constant and \(U_1\) strictly decreases as \(d\) increases, since \(z=a/(e^{a(1-d)}-1)\) increases strictly from \(c\) to infinity. Therefore \(U_1\) decreases from infinity to zero and crosses \(U_0\) exactly once. With

\[
C(a)=c+\frac{1-c}{U_0},\qquad
d_*(a)=1-\frac{1}{a}\log\!\left(1+\frac{a}{C(a)}\right),
\]

we have \(0<d_*(a)<1\), and the active upper boundary is \(U_0\) below \(d_*\) and \(U_1\) above it. For \(d\downarrow0\), Taylor expansion of \(1-e^{-ad}\) shows \(L=U_0-(1-e^{-a})d/2+O_a(d^2)\), while \(U_1\to\infty\). Hence the width is \((1-e^{-a})d/2+O_a(d^2)\).

For \(d\uparrow1\), write \(\varepsilon=1-d\) and \(c=a/(e^a-1)\). Direct Taylor expansion gives

\[
L=(1-c)\varepsilon+\left(c-c^2-\frac{ac}{2}\right)\varepsilon^2+O_a(\varepsilon^3),
\]
\[
U_1=(1-c)\varepsilon+\left((1-c)\left(c+\frac a2\right)\right)\varepsilon^2+O_a(\varepsilon^3).
\]

Here \(U_1<U_0\) for small positive \(\varepsilon\), and subtraction yields \(U_1-L=(a/2)\varepsilon^2+O_a(\varepsilon^3)\). The leading coefficient is independent of \(c\). This finishes the proof.

## Verification

The standalone `check.py` uses only the Python standard library and independently evaluates all three threshold functions for eight wash-off rates, eight intermediate delays per rate, both roots via bisection, interval sign patterns, unique upper-bound switches, and both endpoint asymptotics. Running `python3 check.py` returned `PASS 894 assertions`. These numerical checks corroborate identities and boundary behavior; the all-parameter theorems are proved analytically above.

For an exact illustrative instance, set \(a=2\log 2\), \(d=1/2\), and \(w=1/3\). Then \(L=1/4\) and \(H(d)=-1/18\); both upper bounds are larger than \(1/3\). Bisection gives the unique interior crossings at approximately \(v=0.3125783675\) and \(v=0.6383174433\). Both event endpoints are also trivial zeros and are **not** counted as interior crossings.

## Relationship to prior work

Bertrand-Krajewski, Chebbo and Saget (1998) develop cumulative mass–volume \(M(V)\) curves, show their empirical variability, and discuss a single-exponent fit \(F(v)=v^b\). Alias and colleagues (2014) analyze pollutant wash-off by runoff sectors. Di Modugno and colleagues (2015) fit event-level stormwater-quality simulations and use the same cumulative mass–volume framework. Wang and colleagues (2014) report empirical first- and end-flush behavior. These establish the relevance of changing wash-off shape but do not establish the present **two-source exact two-crossing interval, unique upper-bound switch, or linear-versus-quadratic window collapse** in the inspected material. A single power \(v^b\) cannot change the sign of \(v^b-v\) twice on \((0,1)\); the delayed-source mixture can.

## Limitations

The model fixes the same exponential wash-off rate in both sources, a sharp delayed activation, a prescribed total-mass mixture weight, and a runoff-volume rather than clock-time coordinate. Real routing, infiltration, source depletion, sediment resuspension, and noisy flow measurements can alter the curves. The result does not imply that the two-crossing pattern is common in observed storms or that capture basins should be resized without site-specific measurements. The exact upper bound of two crossings relies on each within-segment wash-off density being strictly decreasing. Historical priority is provisional; a potentially close 2014 flushing study was not inspected in full.

## References

- Bertrand-Krajewski, J.-L., Chebbo, G., and Saget, A. (1998). *Distribution of pollutant mass vs volume in stormwater discharges and the first flush phenomenon*. Water Research 32, 2341–2356. https://doi.org/10.1016/S0043-1354(97)00420-X
- Alias, N., Liu, A., Egodawatta, P., and Goonetilleke, A. (2014). *Sectional analysis of the pollutant wash-off process based on runoff hydrograph*. Journal of Environmental Management 134, 63–69. https://doi.org/10.1016/j.jenvman.2013.12.034
- Di Modugno, M., et al. (2015). *Build-Up/Wash-Off Monitoring and Assessment for Sustainable Management of First Flush in an Urban Area*. Sustainability 7, 5050–5070. https://doi.org/10.3390/su7055050
- Wang, L. Z., et al. (2014). *Pollutant Flushing Characterizations of Stormwater Runoff and Their Correlation with Land Use in a Rapidly Urbanizing Watershed*. Journal of Environmental Informatics 23, 44–54. https://doi.org/10.3808/jei.201400256
- Al Mamun, A., Shams, S., and Nuruzzaman, M. (2020). *Review on uncertainty of the first-flush phenomenon in diffuse pollution control*. Applied Water Science 10, 53. https://doi.org/10.1007/s13201-019-1127-1
