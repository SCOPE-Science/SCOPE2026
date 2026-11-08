# Exact coexistence and tricritical scaling of optimal transport in a mobile-wall run-and-tumble slit

## Finding

The four-direction slit model of Pietrangeli, Ybert, Cottin-Bizonne and Detcheverry has a sharp, explicitly computable separation between **continuous** loss of a finite optimal run time and **discontinuous** coexistence with the infinite-run plateau. The source identified both scenarios and a sufficient condition for the continuous scenario; the result below classifies all physical parameters, proves unique global optimization and identifies a distinct tricritical divergence exponent and the finite-run metastability interval.

Write \(a=1-\alpha\), where \(\alpha\) is the mean turning-angle cosine, and measure run time in units of slit crossing time. Set \(t=\tau_r\), \(h=\eta\), \(w=\bar v^{\,2}\) and \(x=\tau\). For all \(0<a\le2\), \(t>0\), \(h>1\), \(w\ge0\), define the source's dimensionless effective diffusivity
\[
 F_w(x)=\frac{tx\bigl[x+t+hwx(x+at)\bigr]}
 {(x+t)(x+at)(hx+2)},\qquad x>0.
\]
The infinite-run plateau is \(F_w(\infty)=tw\). Put
\[
 \Delta=2a-(1-a)ht,\qquad w_\infty=\frac1{ht+2}.
\]

**Continuous regime (\(\Delta\ge0\)).** If \(0\le w<w_\infty\), \(F_w\) has exactly one critical point and exactly one finite global maximizer \(x_m(w)\). If \(w\ge w_\infty\), \(F_w\) is strictly increasing, and its supremum \(tw\) is not attained at finite \(x\). The maximizer diverges as \(w\uparrow w_\infty\), but with two different exponents:
\[
 x_m(w)\sim
 \begin{cases}
 \displaystyle\frac{2t\Delta}{(ht+2)^2(w_\infty-w)},&\Delta>0,\\[6pt]
 \displaystyle t(1-a)\sqrt{\frac{3a}{2(w_\infty-w)}},&\Delta=0.
 \end{cases}
\]
In the second case necessarily \(0<a<1\) and \(ht=2a/(1-a)\).

**Discontinuous regime (\(\Delta<0\)).** Necessarily \(0<a<1\). Set \(K=-\Delta>0\), and define
\[
 z=\frac{t\bigl(2a+\sqrt{2a(1-a)ht}\bigr)}K,\qquad
 H(x)=\frac{x(x+t)}{(x+at)((ht+2)x+2t)},\qquad
 w_c=H(z).
\]
There is a second, higher threshold \(w_s\): let \(q\) be the unique positive root of
\[
 -Kq^3+6atq^2+6at^2q+2a^2t^3=0,
\]
and put
\[
 W(x)=\frac{(hx^2-2at)(x+t)^2}
 {hx\bigl((ht+2)x+4t\bigr)(x+at)^2},\qquad w_s=W(q).
\]
Then \(w_\infty<w_c<w_s\). For \(0\le w<w_c\), there is a unique finite global maximizer. At \(w=w_c\), \(z\) is the unique finite global maximizer and ties exactly with the infinite-run plateau: \(F_{w_c}(z)=tw_c\). For \(w>w_c\), the supremum is \(tw\), unattained at finite run time. For \(w_c<w<w_s\), a strict finite local maximum survives below that plateau (a metastable optimizer), together with a strict local minimum. For \(w\ge w_s\), there is no finite local maximum; at equality \(w=w_s\) there is one stationary shoulder. Thus the order parameter \(1/x_m\) jumps at coexistence from \(1/z\) to zero. As \(K\downarrow0\) with \(a,t\) fixed and \(h\) adjusted accordingly, \(z\sim4at/K\), so the jump vanishes at the tricritical boundary.

For the source's discontinuous example \((a,h,t)=(1/2,2,10)\), these are distinct exact thresholds:
\[
 z=4.62475295574264\ldots,\quad
 \sqrt{w_c}=0.24025307335204\ldots,\quad
 q=8.21450706554566\ldots,\quad
 \sqrt{w_s}=0.25587018722371\ldots.
\]

## Assumptions and scope

This is an exact analysis of the four-cardinal-direction stochastic slit model, **not** a proof for continuous-orientation swimmers or disordered porous media. Longitudinal diffusion is governed by the published formula above, with unit speed and unit slit width. Tumbles occur at dimensionless rate \(1/x\), wall escape at \(1/(hx)\), wall reorientation at the remaining rate, mean cosine \(\alpha=1-a\), and the rotational persistence time is \(t\). The assumptions \(0<a\le2\), \(h>1\), \(t>0\), and \(w\ge0\) make all denominators positive for \(x>0\). The degenerate perfectly persistent turn law \(a=0\), for which the small-run boundary changes character, is excluded explicitly. The reference model assumes Poisson switching and idealized wall motion. The optimizer is over all finite positive \(x\); \(x=\infty\) denotes a limiting protocol rather than an admissible finite run time.

## Proof

**1. A positive bulk–wall decomposition.** Direct cancellation gives
\[
 F_w(x)=\underbrace{\frac{tx}{(x+at)(hx+2)}}_{B(x)}
 +w\underbrace{\frac{htx^2}{(x+t)(hx+2)}}_{S(x)}.
\]
In particular \(F_w(0+)=0\) and \(F_w(\infty)=tw\). Differentiating the two summands exactly yields
\[
 B'(x)=\frac{t(2at-hx^2)}{(x+at)^2(hx+2)^2},\qquad
 S'(x)=\frac{htx((ht+2)x+4t)}{(x+t)^2(hx+2)^2}>0.
\]
Set \(x_0=\sqrt{2at/h}\). For \(x\le x_0\), the derivative is positive except possibly at the endpoint when \(w=0\). For \(x>x_0\), \(F'_w(x)\) has exactly the sign of \(w-W(x)\), with \(W\) defined above. Note \(W(x_0)=0\) and \(W(\infty)=w_\infty\).

**2. The stationary-point geometry.** An exact quotient-rule calculation gives
\[
 W'(x)=\frac{2t(x+t)(hx+2)Q(x)}
 {hx^2(x+at)^3((ht+2)x+4t)^2},
\]
where
\[
 Q(x)=\Delta x^3+6atx^2+6at^2x+2a^2t^3.
\]
If \(\Delta\ge0\), \(Q(x)>0\) for all \(x>0\); hence \(W\) rises strictly from zero at \(x_0\) to its limiting \(w_\infty\), always from below. Every \(w<w_\infty\) has exactly one solution \(W(x)=w\) for \(x\ge x_0\), which changes \(F'_w\) from positive to negative. When \(w\ge w_\infty\), \(F'_w>0\) throughout the positive half-line. This proves the global claims in the continuous regime, including \(w=0\).

If \(\Delta=-K<0\), the coefficients of \(Q\) have exactly one sign change in descending powers. By Descartes' rule, \(Q\) has at most one positive zero, and continuity gives exactly one because \(Q(0)>0\) while \(Q(x)\to-\infty\). Call it \(q\). Since \(W(x_0)=0\), \(W\) is negative immediately to the left of \(x_0\) and positive immediately to its right, the simple numerator zero there gives \(W'(x_0)>0\), hence \(q>x_0\). Thus \(W\) increases on \((x_0,q)\), decreases on \((q,\infty)\), and approaches \(w_\infty\) from above. Its unique maximum is \(w_s=W(q)>w_\infty\). For \(w\le w_\infty\) there is exactly one finite maximum. For \(w_\infty<w<w_s\), exactly two positive stationary points occur: a strict maximum before \(q\) and a strict minimum after \(q\). For \(w\ge w_s\), there is no finite local maximum; at \(w=w_s\) the derivative merely touches zero. These statements follow directly from the sign of \(w-W(x)\), without solving the source's quartic stationarity equation.

**3. Global coexistence envelope.** Subtracting the plateau and factoring, with a strictly positive prefactor, gives
\[
 F_w(x)-tw=
 \frac{t(x+at)((ht+2)x+2t)}{(x+t)(x+at)(hx+2)}\bigl(H(x)-w\bigr).
\]
Thus a finite protocol beats the infinite-run plateau if and only if \(w<\sup_{x>0}H(x)\). The derivative of the elementary envelope is
\[
 H'(x)=\frac{t\bigl(\Delta x^2+4atx+2at^2\bigr)}
 {(x+at)^2((ht+2)x+2t)^2}.
\]
When \(\Delta\ge0\), \(H\) increases strictly to \(w_\infty\), giving exactly the threshold already established by stationary-point geometry. When \(\Delta=-K<0\), its numerator has a unique positive zero \(z\), given by the stated quadratic formula. Hence \(H\) has a strict unique maximum at \(z\). From the identity
\[
 H(x)-w_\infty=
 \frac{t(Kx-2at)}{(x+at)(ht+2)((ht+2)x+2t)}
\]
we see \(w_c=H(z)>w_\infty\). At \(w=w_c\), \(F_w(x)\le tw_c\) with equality at exactly one finite \(x=z\). Because this is an interior strict maximum, \(F'_{w_c}(z)=0\), so \(W(z)=w_c\), and its strict negative second derivative puts \(z\) on the increasing branch of \(W\), before \(q\). Therefore \(w_c<w_s\). For \(w<w_c\), some finite point beats the plateau; the stationary geometry proves the finite global maximizer is unique. For \(w>w_c\), every finite point lies below the plateau; the stationary geometry gives the specified metastable interval. This exhausts all parameter and equality cases.

**4. Tricritical divergence.** Expansion of the exact rational function \(W\) for large \(x\) gives, when \(\Delta>0\),
\[
 W(x)=w_\infty-\frac{2t\Delta}{(ht+2)^2x}+O(x^{-2}).
\]
At \(\Delta=0\), the inverse-first-power term cancels exactly, and substitution of \(ht=2a/(1-a)\) gives
\[
 W(x)=w_\infty-\frac{3a(1-a)^2t^2}{2x^2}+O(x^{-3}).
\]
The equation \(W(x_m)=w\), uniqueness, and \(x_m\to\infty\) then imply the two sharp asymptotic equivalents in the Finding. For \(\Delta=-K<0\), the displayed exact formula for \(z\) gives \(z\sim4at/K\) as \(K\downarrow0\), completing the tricritical boundary description.

## Verification

The accompanying `CHECK.py` uses only the Python 3 standard library. Its sparse multivariate polynomial arithmetic verifies **exactly**, for arbitrary symbolic parameter values, the bulk–wall derivative identities, the factorization for \(H'\), the full quotient-rule identity for \(W'\), and equivalence of the two forms of the source diffusivity. It also performs deterministic double-precision checks of the source's discontinuous example, strict separation of coexistence and spinodal thresholds, local maximizing behavior, and both divergence exponents. Execute `python CHECK.py` from the directory containing the checker. Successful output is a `PASS` message. Numerical checks support, but do not establish, the universal classification; the proof above does.

## Relationship to prior work

The exact four-direction stochastic model, diffusivity formula (its Eq. (27)), two illustrative types of optimizer transition (Figs. 6–7), continuous transition speed under \(2(1-\alpha)-\alpha\eta\tau_r>0\) (its Appendix C), and the asymptotic run-time divergence within that strict regime are due to Pietrangeli, Ybert, Cottin-Bizonne and Detcheverry (2024). The present claim is **not** a new derivation of that diffusivity or the first observation that two transition types exist. The additional results are: a necessary-and-sufficient order criterion including the equality case; an exact algebraic coexistence speed in the discontinuous region; the separate strict spinodal/metastability window; uniqueness of the global optimizer in every phase; and a different inverse-square-root exponent on the tricritical boundary. The same authors' 2025 porous-media dispersal work uses a more general motility framework and discusses surface sliding, but does not state this particular complete phase geometry for the four-direction slit model. These comparisons are based on the indicated accessible full texts; broader unindexed optimization results could still encompass the formula-based classification.

## Limitations

The mathematics proves global properties of the displayed exact rational diffusivity under the specified parameter range; it does not independently rederive the stochastic model's continuum transport limit. It does not extend the phase boundaries to continuous-orientation motion, non-Poissonian tumbles, finite-width wall potential layers, variable wall velocities, or arbitrary porous geometry. The point \(x=\infty\) is only an unattained limit of finite protocols. Local stability refers to extrema of the diffusivity as a function of run time, not to dynamic stability of a particle trajectory. An independent scientific priority audit and independent validation have not been carried out.

## References

1. T. Pietrangeli, C. Ybert, C. Cottin-Bizonne, and F. Detcheverry, *Optimal run-and-tumble in slit-like confinement*, Physical Review Research **6**, 023028 (published online 2024-04-05), DOI: https://doi.org/10.1103/PhysRevResearch.6.023028; open full text https://arxiv.org/pdf/2404.07680 (arXiv posted 2024-04-11). Relevant portions: Eq. (27), Sec. IV.A.2, Appendix C.
2. T. Pietrangeli, R. Foffi, R. Stocker, C. Ybert, C. Cottin-Bizonne, and F. Detcheverry, *Universal law for the dispersal of motile microorganisms in porous media*, https://arxiv.org/abs/2503.03273 (first posted 2025-03-05). Relevant portions: multimodal motion and surface sliding; the geometry is different from the exact slit model treated above.
