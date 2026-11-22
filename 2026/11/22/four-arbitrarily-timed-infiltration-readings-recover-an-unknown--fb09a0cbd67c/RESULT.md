# Four arbitrarily timed infiltration readings recover an unknown Philip clock and gauge origin

## Finding

Let four distinct observation times satisfy \(t_1<t_2<t_3<t_4\). The exact, shifted two-term Philip cumulative-infiltration model is
\[
Y(t)=B+S\sqrt{t-\tau}+K(t-\tau),\qquad t>\tau,
\]
with unknown clock origin \(\tau<t_1\), sorptivity coefficient \(S>0\), linear infiltration coefficient \(K>0\), and additive gauge offset \(B\in\mathbb R\). Every four exact values \(y_i=Y(t_i)\) uniquely determine all four parameters. Any three or fewer exact observations have an uncountable positive-parameter family of solutions through every interior model point; thus four readings are sharp.

Moreover, the theorem gives an *if and only if* admissibility test for arbitrary four measured ordinates, not merely an inverse for data assumed to follow the model. Define the second divided difference
\[
D_{ijk}=\frac{(y_k-y_j)/(t_k-t_j)-(y_j-y_i)/(t_j-t_i)}{t_k-t_i}.
\]
Suppose \(D_{123}<0\) and \(D_{234}<0\), and write \(\mathcal R=D_{123}/D_{234}\). Let
\[
\mathcal R_* = \frac{(\sqrt{t_3-t_1}+\sqrt{t_4-t_1})(\sqrt{t_2-t_1}+\sqrt{t_4-t_1})}{\sqrt{(t_2-t_1)(t_3-t_1)}}.
\]
First require \(1<\mathcal R<\mathcal R_*\). There is then exactly one \(\tau<t_1\) solving
\[
\mathcal R=\frac{(r_3+r_4)(r_2+r_4)}{(r_1+r_2)(r_1+r_3)},\qquad r_i=\sqrt{t_i-\tau}.
\]
Set
\[
S=-D_{123}(r_1+r_2)(r_2+r_3)(r_1+r_3),
\]
\[
K=\frac{y_2-y_1}{t_2-t_1}-\frac{S}{r_1+r_2},\qquad
B=y_1-Sr_1-K(t_1-\tau).
\]
The observations arise from the stated positive-parameter model **if and only if** the two negative-divided-difference conditions, the open ratio interval, and the reconstructed inequality \(K>0\) all hold. If the apparatus additionally imposes \(B\ge0\), add precisely that reconstructed inequality; no hidden condition is needed.

The shape ratio has the sharp remote-onset asymptotic
\[
\mathcal R(\tau)=1+\frac{t_4-t_1}{2(-\tau)}+O(\tau^{-2})\quad(\tau\to-\infty),
\]
when the observation times are held fixed. Thus exact identifiability does not imply good recovery of a far-remote clock origin under noisy data.

## Assumptions and scope

This is a finite, deterministic, noise-free *structural identifiability* statement, for four arbitrary, known, strictly increasing observation times. The origin \(\tau\) precedes all readings; the two positive rate coefficients are independent and there is a freely unknown additive calibration offset. In a soil interpretation the linear coefficient is a calibrated multiple of saturated conductivity, not necessarily the conductivity itself. The two-term Philip expansion is a short-time constitutive approximation, not an exact Richards-equation law for real soils at all times. The theorem does not infer the unspecified conversion factor, nor unknown additional higher-order Philip terms. All square roots are principal positive roots.

## Proof

**Exact curvature identity.** For \(r_i=\sqrt{t_i-\tau}\), the first divided difference of \(\sqrt{t-\tau}\) between two times is \(1/(r_i+r_j)\). Taking one more divided difference yields the exact identity
\[
[t_i,t_j,t_k]\sqrt{t-\tau}=-\frac{1}{(r_i+r_j)(r_j+r_k)(r_i+r_k)}.
\]
The affine term and the constant vanish under second divided differences. Consequently \(D_{ijk}\) equals \(-S\) times the displayed positive reciprocal product; in particular both required values are strictly negative. Their ratio cancels the common \(r_2+r_3\) term and yields the asserted equation for \(\mathcal R\).

**Strictly monotone onset invariant.** Denote the right side of the ratio equation by \(H(\tau)\). Differentiation of the identity \(r_i'=-(2r_i)^{-1}\) and \((\log(r_i+r_j))'=-1/(2r_ir_j)\) gives
\[
\frac{d}{d\tau}\log H(\tau)=\frac12\left(\frac1{r_1}-\frac1{r_4}\right)\left(\frac1{r_2}+\frac1{r_3}\right)>0.
\]
The strict inequality follows from \(t_1<t_4\), so \(r_1<r_4\). Also \(\lim_{\tau\to-\infty}H(\tau)=1\) and \(\lim_{\tau\uparrow t_1}H(\tau)=\mathcal R_*\), both endpoint values excluded. The intermediate value theorem and strict monotonicity prove the unique root and the exact open admissibility range.

**Complete inverse and sufficiency.** The first curvature identity uniquely gives \(S\), the first secant slope uniquely gives \(K\), and the first ordinate uniquely gives \(B\). The reconstructed curve matches \(y_1,y_2\) by those last two definitions and matches \(D_{123},D_{234}\) by \(S\) and the shape ratio. The transformation from four ordinates to \((y_1,(y_2-y_1)/(t_2-t_1),D_{123},D_{234})\) is invertible: the first two quantities determine \(y_2\), \(D_{123}\) determines \(y_3\), and \(D_{234}\) then determines \(y_4\). Hence the reconstructed curve matches all four observations. Conversely every physical curve satisfies the exact ratio and coefficient inequalities. This proves global uniqueness, existence and the stated necessary-and-sufficient test.

**Sharp three-reading obstruction.** Fix any three times and any interior \((\tau,S,K,B)\) with \(S,K>0\). For each nearby \(\tau'\ne\tau\) satisfying \(\tau'<t_1\), define \(S'\) using \(D_{123}\) and the reciprocal product at \(\tau'\), then \(K'\) using the first secant and \(B'\) using the first ordinate. These are continuous in \(\tau'\) and equal \((S,K,B)\) at \(\tau\), so both positive coefficients persist for a nonempty interval of different \(\tau'\). All three ordinates remain unchanged by the same invertible-triangle argument. Fewer observations cannot distinguish parameters already indistinguishable with three.

**Remote-onset boundary.** For fixed \(t_i\), \(r_i=\sqrt{-\tau}\left(1+t_i/(2(-\tau))+O(\tau^{-2})\right)\). Substituting the four pair sums in the ratio, or expanding their logarithms, yields \(\log H=(t_4-t_1)/(2(-\tau))+O(\tau^{-2})\). Exponentiation proves the stated expansion. This is a structural conditioning warning, not a statistical variance formula.

## Verification

The standalone `check_philip.py` uses exact symbolic identities for the second divided difference and logarithmic derivative, 1,200 randomized nonuniform four-time positive-parameter inversions, 400 three-observation perturbation examples (two perturbations each), and a concave but infeasible shape-ratio example. It passed 11,203 assertions. These finite tests supplement the full analytic proof and do not claim exhaustive numerical certification.

For an illustrative exact model with \((t_1,t_2,t_3,t_4)=(1,2,3,4)\), \(\tau=0\), \(S=2\), \(K=1/3\), and \(B=1/2\), the measured ordinates are \((17/6,\,1/2+2\sqrt2+2/3,\,3/2+2\sqrt3,\,35/6)\). The one-dimensional inverse returns the original four parameters to floating-point tolerance. The endpoint ratio \(\mathcal R_*\) is approximately \(6.07811602252011\).

## Relationship to prior work

Philip's 1957 sorptivity model and later standard inference procedures assume the observation clock and cumulative-infiltration zero are calibrated. Zeleke and Si (2005) investigate uniqueness of *different*, falling-head model parameters in noisy data. Jaiswal et al. (2022) estimate the original zero-origin Philip coefficients and time-validity with full infiltration records; Vrugt et al. (2024) investigate model validity and structural mismatch. Neither inspected analysis gives the four-reading, double-offset inverse and exact range test here.

A public result entitled *Four equal-depth infiltration readings with unknown volume and clock origins* treats a **Green–Ampt** implicit law and inverse level-crossing times. Its mathematical assumptions and observable map are different: it cannot imply this Philip square-root divided-difference criterion by a parameter substitution. Generic Chebyshev/variation-diminishing methods could potentially furnish alternative arguments for global identifiability, but the present strict shape-ratio range and explicit physical-feasibility test are not established by a citation to those general principles alone.

## Limitations

Exact algebraic identifiability does not imply reliable estimation from noisy measurements. When the onset is much earlier than the first observation, \(\mathcal R\) approaches 1 and inversion becomes poorly conditioned. Parameter-uncertainty bounds and experimental optimum spacing are not proved. The added gauge offset is an observational calibration parameter, not a new physical mass input, and it must be handled consistently in applications. Higher-order infiltration terms, unsaturated multidimensional flow, uncertain sampling times, and endogenous boundary forcing are excluded. Priority relative to historical results not accessible in full, especially the 1957 article and general shifted-power inverse-model literature, remains provisional.

## References

- J. R. Philip (1957), *The theory of infiltration: 4. Sorptivity and algebraic infiltration equations*, *Soil Science* 84, 257–264. DOI: 10.1097/00010694-195709000-00010. Public issue date September 1957; no exact publication day established here.
- T. B. Zeleke and B. C. Si (2005), *Parameter estimation using the falling head infiltration model: Simulation and field experiment*, *Water Resources Research* 41. DOI: 10.1029/2004WR003407. First published 2005-02-23.
- P. Jaiswal et al. (2022), *Parasite inversion for determining the coefficients and time-validity of Philip's two-term infiltration equation*, *Vadose Zone Journal*. DOI: 10.1002/vzj2.20166.
- J. A. Vrugt et al. (2024), *The time validity of Philip's two-term infiltration equation: An elusive theoretical quantity?*, *Vadose Zone Journal*. DOI: 10.1002/vzj2.20309.
- *Four equal-depth infiltration readings with unknown volume and clock origins*, public mathematical research record, 2026-11-02, available at https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-four-equal-depth-infiltration-readings-with-unknown-volume-and-c--49ccbc1b6a86.
