# Sharp horizon reversal in the order of two quality-differentiated ecological subsidies

## Finding

Let \(a,b,d,m>0\), let \(q_{\rm H}>q_{\rm L}\geq0\), and let the observation horizon satisfy \(H\geq d\). Two identical-mass subsidy pulses of size \(m\) arrive at times \(0\) and \(d\), but their qualities are \(q_{\rm H}\) and \(q_{\rm L}\). A subsidy pulse of quality \(q\) instantaneously adds \(m\) to an activity pool \(B\) and \(mq\) to a quality-memory pool \(Q\). Between pulses, \(\dot B=-aB\) and \(\dot Q=-bQ\), with zero initial pools. The bilinear cumulative trophic-response proxy is

\[
J(H)=\int_0^H B(t)Q(t)\,dt.
\]

Write \(J_{\rm HL}(H)\) for high-quality first and \(J_{\rm LH}(H)\) for low-quality first. Put

\[
c=a+b,\quad E=1-e^{-cd},\quad D=e^{-ad}-e^{-bd}.
\]

The exact order contrast is

\[
\boxed{J_{\rm HL}(H)-J_{\rm LH}(H)=\frac{m^2(q_{\rm H}-q_{\rm L})}{c}\left[(E+D)e^{-c(H-d)}-D\right].}
\]

**Complete and sharp ordering theorem.** If \(a\geq b\), high-quality first is strictly optimal between the two orders for every finite \(H\geq d\). If \(a<b\), there is exactly one crossover horizon

\[
\boxed{H_c=d+\frac{1}{a+b}\log\!\left(1+\frac{1-e^{-(a+b)d}}{e^{-ad}-e^{-bd}}\right)>d.}
\]

High-quality first is strictly optimal for \(d\leq H<H_c\); both orders tie at \(H=H_c\); low-quality first is strictly optimal for \(H>H_c\). The crossover is independent of the common pulse mass and both quality levels, provided their contrast is positive. Furthermore, for fixed \(0<a<b\),

\[
\lim_{d\downarrow0}H_c=\frac{1}{a+b}\log\!\frac{2b}{b-a}>0,
\qquad
\lim_{d\to\infty}\frac{H_c}{d}=1+\frac{a}{a+b}.
\]

The first limit is singular: the *response difference* vanishes with \(d\), but the location of the crossover approaches a positive constant. At \(a=b\), the two orders are strictly distinct for every finite horizon yet their response difference tends to zero as \(H\to\infty\).

## Assumptions and scope

The two pulse times and masses are prescribed, only the assignment of two quality labels is compared, and both memory states experience constant first-order losses. The response is a bilinear proxy for the interaction between a pulse-induced activity state and a nutritional-quality state, not a calibrated prediction of predator numbers, plant biomass, food-web recycling, or consumption. Pulses are instantaneous, no underlying nonzero background is included, no feedback changes the loss rates, and the two pulse inputs do not deplete each other. All comparisons are at fixed model parameters and finite \(H\geq d\). The theorem is not an optimal-control result over arbitrary pulse calendars.

## Proof

With the quality at time zero denoted \(q_0\) and the quality at time \(d\) denoted \(q_1\), the exact solution before the second pulse is

\[
B(t)=me^{-at},\qquad Q(t)=mq_0e^{-bt},\qquad0\le t<d.
\]

After that pulse, with \(s=t-d\),

\[
B(d+s)=m(1+e^{-ad})e^{-as},\quad Q(d+s)=m(q_1+q_0e^{-bd})e^{-bs},\qquad s\ge0.
\]

Direct integration on the two subintervals, including the boundary case \(H=d\), gives

\[
J(q_0,q_1;H)=\frac{m^2}{c}\left[q_0(1-e^{-cd})+(1+e^{-ad})(q_1+q_0e^{-bd})(1-e^{-c(H-d)})\right].
\]

Subtract \(J(q_{\rm L},q_{\rm H};H)\) from \(J(q_{\rm H},q_{\rm L};H)\). The result initially reads

\[
\frac{m^2(q_{\rm H}-q_{\rm L})}{c}\left[E-(1+e^{-ad})(1-e^{-bd})(1-e^{-c(H-d)})\right].
\]

Since \(E-(1+e^{-ad})(1-e^{-bd})=-D\), this is exactly the boxed contrast. Define \(z=e^{-c(H-d)}\). For every finite \(H\ge d\), \(0<z\le1\), and the bracket is the affine function \(\psi(z)=(E+D)z-D\), with \(\psi(1)=E>0\) and \(\psi(0)=-D\).

If \(a>b\), then \(D<0\), so both endpoint values of this affine function are positive; if \(a=b\), then \(D=0\) and \(\psi(z)=Ez>0\). Thus high quality first wins strictly at every finite horizon for \(a\ge b\). If \(a<b\), then \(D>0\) and \(E+D>0\), so \(\psi(z)\) increases strictly with \(z\), crosses zero exactly once in \((0,1)\) at \(z_c=D/(E+D)\), and the fact that \(z\) decreases strictly with \(H\) gives the asserted strict winner and tie. Solving \(z=z_c\) gives the stated \(H_c\). All inequalities are strict because \(m^2(q_{\rm H}-q_{\rm L})/c>0\).

For the first asymptotic, as \(d\downarrow0\), \(E/d\to a+b\) and \(D/d\to b-a\); substitution into the continuous logarithm gives the limit. For \(d\to\infty\), \(E\to1\) and \(D=e^{-ad}(1-e^{-(b-a)d})\), whence \(\log(1+E/D)=ad+o(d)\). For \(a=b\), the contrast simplifies to \(m^2(q_{\rm H}-q_{\rm L})E e^{-2a(H-d)}/(2a)\), proving strict finite-horizon preference and vanishing infinite-horizon difference. This completes the proof.

## Verification

The accompanying `verify.py` uses exact piecewise exponential integration independently of the simplified contrast, checks all three loss-rate regimes over random positive parameters, verifies the unique crossover, compares against independent midpoint quadrature and tests the singular small-gap asymptotic. Running `python3 verify.py` returned `ASSERTIONS_PASSED 22813`. All sampled floating-point comparisons are supplementary consistency checks; the proof is the preceding exact identity and sign argument.

For example, take \(a=1\), \(b=2\), \(d=m=1\), \(q_{\rm H}=0.8\), and \(q_{\rm L}=0.2\). Then \(H_c=1.54217445834548\ldots\). At \(H=1.2\), the high-first and low-first cumulative responses are respectively \(0.3168082144921804\) and \(0.2334948753937352\); at \(H=2\), they are \(0.3869500713438859\) and \(0.4216817013146826\). This is a true reversal of the entire integrated proxy, not merely a crossing of instantaneous rates.

## Relationship to prior work

Osakpolor et al. (2023) model quantity and fatty-acid quality as distinct coupled state variables in riparian trophic subsidies and study their ecological effects using numerical transient dynamics. Their published model is biologically richer and not equivalent to the bilinear two-memory proxy here; their analyzed claims do not give this two-order finite-horizon classification. Jentsch and White (2019) provide a general theory of pulse dynamics, while Yee and Juliano (2012; electronically available in 2011) experimentally study resource-pulse amount, type and frequency. Neither gives the present exact order contrast. Standard exponential impulse responses and bilinear/Volterra representations are mathematical background, not claimed innovations. The specific all-parameter inequality, universal crossover, and singular-gap limit are the present claims, subject to residual historical-priority risk because more general ordering theory might imply the identity without this ecological formulation.

## Limitations

The proxy neglects population dynamics, feedback, variable pulse mass, nonlinear functional responses, saturation, bioaccumulation, spatial transport, prior food supply, and stochastic quality. Different modelling assumptions may remove or multiply order switches. The theorem does not recommend a real pulse schedule or attribute these idealizations to any cited experiment. Numerical examples and randomized checks are not empirical validation. Historical priority has been checked against identified sources but not independently audited or exhaustively established.

## References

1. Osakpolor, S. E., Manfrin, A., Leroux, S. J., and Schäfer, R. B. (2023). *Cascading impacts of changes in subsidy quality on recipient ecosystem functioning.* Ecology 104, e4023. First online 2023-03-08. https://doi.org/10.1002/ecy.4023
2. Jentsch, A., and White, P. (2019). *A theory of pulse dynamics and disturbance in ecology.* Ecology 100, e02734. https://doi.org/10.1002/ecy.2734
3. Yee, D. A., and Juliano, S. A. (2012). *Concurrent effects of resource pulse amount, type, and frequency on community and population properties of consumers in detritus-based systems.* Oecologia 169, 511–522. Published electronically 2011-12-02. https://doi.org/10.1007/s00442-011-2209-4
4. *Kernel Identification of Non-Linear Systems with General Structure* (2020), Algorithms 13(12), 328, https://doi.org/10.3390/a13120328 (generic bilinear/Volterra context; covering comparison limited by access).
