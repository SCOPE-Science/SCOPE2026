# Coupling-renormalized critical oscillations at an additive-Allee fold–flip equilibrium

## Finding

Consider the positive planar discrete system
\[
 x_{n+1}=x_n\exp(\alpha-x_n+\beta y_n),\qquad
 y_{n+1}=y_n\exp\!\left(1-y_n-\frac{M}{A+y_n}\right).
\]
For every \(0<A<1\), \(0<\beta<4/(1-A)\), choose the simultaneous fold–flip parameters
\[
 M=\frac{(1+A)^2}{4},\qquad
 \alpha=2-\frac{\beta(1-A)}2.
\]
Set
\[
 y_*=\frac{1-A}{2},\quad C=\frac{1+A}{1-A},\quad
 K=\beta C,\quad W_*=3(1+2K).
\]
The positive equilibrium \((2,y_*)\) has the two multipliers \(-1\) and \(+1\). There exists \(\epsilon(A,\beta)>0\) such that the following two **nonempty open sets** have exact, opposite-phase asymptotics. For either sign \(\sigma\in\{-1,+1\}\), let
\[
\begin{split}
 0&<y_0-y_*<\epsilon,\\
 \frac{W_*}{2}&<\frac{C}{y_0-y_*}
       \bigl(x_0-2-\beta(y_0-y_*)\bigr)^2<2W_*,\\
 \operatorname{sign}\bigl(x_0-2-\beta(y_0-y_*)\bigr)&=\sigma.
\end{split}
\]
Then \(x_n,y_n>0\) for all \(n\ge0\), \(y_n\downarrow y_*\), and
\[
 \boxed{\displaystyle
 \lim_{n\to\infty}n(y_n-y_*)=C,
 \qquad
 \lim_{n\to\infty}(-1)^n\sqrt n\,(x_n-2)
     =\sigma\sqrt{3(1+2\beta C)}.}
\]
In particular, \(n(x_n-2)^2\to3(1+2\beta C)\). This is an exact original-iteration clock; no parameter-dependent rescaling of discrete time is used. The oscillation prefactor differs strictly from the autonomous critical Ricker value \(\sqrt3\) whenever \(\beta>0\).

## Assumptions and scope

All initial conditions and parameters are real, with \(x_0,y_0>0\), \(0<A<1\), \(0<\beta<4/(1-A)\), and the displayed choices of \(\alpha,M\). The positive number \(\epsilon\) is an existence constant, not a numerical cutoff. Each wedge is open in the positive quadrant; neither is asserted to exhaust its basin. The negative-sign wedge has \(x_0>0\) when \(\epsilon\) is sufficiently small because both wedges shrink to \((2,y_*)\). At the equilibrium, the Jacobian is
\[
 DF(2,y_*)=\begin{pmatrix}-1&2\beta\\0&1\end{pmatrix}.
\]
The result concerns convergence from the \(y>y_*\) side of the fold, and excludes the precisely neutral equilibrium and any exceptional faster-converging orbits.

## Proof

**1. The fold coordinate and its clock.** Define \(B=(1+A)/2=A+y_*\) and \(\delta_n=y_n-y_*\). The saddle-node relation gives the exact identity
\[
 1-y-\frac{M}{A+y}=-\frac{(y-y_*)^2}{A+y}.
\]
Hence, for small positive \(\delta\), the host recurrence is
\[
 \delta'= (y_*+\delta)\exp\left(-\frac{\delta^2}{B+\delta}\right)-y_*
          =\delta-\frac{\delta^2}{C}+O(\delta^3).
\]
For sufficiently small \(\delta>0\), \(0<\delta'<\delta\). Iteration decreases to zero (there is no other positive host fixed point at these parameters). Introduce the **exact** positive orbit clock \(t_n=C/\delta_n\). Taylor's formula gives
\[
 t_{n+1}=t_n+1+O(t_n^{-1}),
 \quad t_n\longrightarrow\infty,
 \quad \frac{t_n}{n}\longrightarrow1.
\]
The last limit follows by summing the one-step increment (or Cesàro averaging). The forcing \(p_n=\beta\delta_n\) therefore equals \(K/t_n\) exactly and satisfies
\[
 p_{n+1}-p_n=O(t_n^{-2}),\qquad
 p_{n+2}-2p_{n+1}+p_n=O(t_n^{-3}).
\]
These are consequences of the analytic scalar host map, not numerical approximations.

**2. Eliminate the even forcing.** In the transverse coordinate
\[
 v_n=x_n-2-p_n,
 \qquad h_p(v)=(2+p+v)e^{-v}-2-p,
\]
the full map is exactly
\[
 v_{n+1}=h_{p_n}(v_n)+p_n-p_{n+1}.
\]
For small \(p,v\), direct Taylor expansion (including the quartic cancellation in the two-step composition) gives
\[
 h_p(h_p(v))=v+2pv-\frac13v^3
 +O\bigl(p^2|v|+p|v|^3+|v|^5\bigr).
\]
Indeed, the linear coefficient is exactly \((1+p)^2\), the cubic coefficient at \(p=0\) is \(-1/3\), and the pure quadratic and quartic coefficients vanish at \(p=0\) with the quadratic coefficient having zero first derivative in \(p\). The exact two-step nonautonomous recurrence differs from this frozen-\(p\) composition by \(O(t_n^{-2}|v_n|+t_n^{-3})\): the two constant forcing differences cancel to leading order, and \(\partial_p h_p(v)=e^{-v}-1=O(v)\). Thus, uniformly on any fixed annulus
\[
 0<w_-\le t_nv_n^2\le w_+<\infty,
\]
we have
\[
 \boxed{v_{n+2}=v_n+\frac{2K}{t_n}v_n
                   -\frac13v_n^3+O(t_n^{-5/2}).}
\]
The constants in the error depend only on fixed parameter and annulus bounds. This is a Taylor estimate for the actual map, not an assumed normal form.

**3. An attracting positive amplitude.** Put \(w_n=t_nv_n^2\). Since \(t_{n+2}=t_n+2+O(t_n^{-1})\), squaring the preceding equation yields, uniformly in the same annulus,
\[
 \boxed{w_{n+2}=w_n+\frac{2}{3t_n}w_n(W_*-w_n)
                       +O(t_n^{-2}),\qquad W_*=3(1+2K).}
\]
Choose \(w_-=W_*/2\) and \(w_+=2W_*\). The leading drift is strictly inward at both endpoints. For all sufficiently large \(t_0\), the exact two-step map preserves \([w_-,w_+]\), including points close to the endpoints by the uniform Taylor bounds. It also preserves the sign of \(v_{2j}\): the two-step change is \(O(t_{2j}^{-3/2})\), whereas \(|v_{2j}|\ge\sqrt{w_-/t_{2j}}\). Thus both signed initial wedges are invariant in the required local asymptotic sense.

For \(E_j=(w_{2j}-W_*)^2\), the same recurrence and \(w_{2j}\ge w_-\) give, for some fixed \(D>0\),
\[
 E_{j+1}\le\left(1-\frac{4w_-}{3t_{2j}}\right)E_j
                         +\frac{D}{t_{2j}^2}.
\]
As \(t_{2j}/(2j)\to1\), the multiplicative deficits have divergent sum, and the additive errors are summable. Iteration of this inequality (or discrete Gronwall with any small positive tolerance) proves \(E_j\to0\), hence \(w_{2j}\to W_*\). This reconstructs the critical amplitude from the exact two-step dynamics rather than from finite numerics.

**4. Return to every time step.** The one-step identity gives \(v_{2j+1}/v_{2j}\to-1\). Therefore signs alternate, \(w_n\to W_*\) also along odd indices, and
\[
 (-1)^n\sqrt{t_n}\,v_n\to\sigma\sqrt{W_*}.
\]
Finally \(t_n/n\to1\) and \(p_n=K/t_n=O(n^{-1})\), so replacing \(v_n=x_n-2-p_n\) by \(x_n-2\) does not affect the square-root limit. The host limit follows from \(\delta_n=C/t_n\). This proves both asserted limits for each sign.

## Verification

The standalone `verify.py` checks the exact fold identity, the host quadratic coefficient, the one-step and two-step Taylor cancellations and the value \(-1/3\), using symbolic algebra. It also runs finite diagnostics in two admissible parameter chambers and both initial phases. Invoke `python verify.py` with Python and SymPy. The expected completion marker is `FOLD_FLIP_COUPLED_CLOCK_VERIFY_OK`. Numerical convergence is deliberately not used to establish the infinite-time theorem: the invariant-annulus and squared-amplitude inequalities above do so. The checker covers algebra and sample behavior; it is not an independent audit.

For example \(A=1/3\), \(\beta=1\), \(\alpha=5/3\), \(M=4/9\), the two exact constants are \(C=2\) and \(W_*=15\), so the period-alternating amplitude tends to \(\sqrt{15}\) in either wedge.

## Relationship to prior work

Chong, Kashyap, Chen and Chen (2023) define this exact map and study equilibria, codimension-one fold and flip bifurcations and stability. Their Section 5 explicitly leaves the simultaneous fold–flip configuration at the positive saddle-node equilibrium for future work. The fixed point and its two critical multipliers are not asserted here as new by themselves. The contribution is the **two simultaneous, original-iteration asymptotic laws on open sets**, especially the coupling-sensitive coefficient \(3(1+2\beta C)\).

General fold–flip analyses in other discrete predator–prey maps (for example Wang and coauthors, 2024, doi:10.3390/math12182872) are not an implication of the present asymptotic statement: they work with different map equations and characterize local bifurcation curves or normal forms rather than this coupled critical clock. Critical inverse-square-root relaxation for autonomous Ricker-type maps supplies a comparison principle, but it does not yield the extra \(2\beta C\) term without analyzing the nonautonomous host approach. Related mathematical literature may contain equivalent asymptotics not identified by the searches described in the review.

## Limitations

Only explicitly specified local, nonempty open initial wedges above the host fold are covered; no claim is made for every positive initial condition, for initial data below the host fold, for a global basin partition, for parameters away from the simultaneous fold–flip surface, or for exceptional faster-relaxing solutions. The coefficient describes a mathematical population map, not empirical ecological measurement. An independent mathematical audit has not been performed. No computational experiment is offered as a proof of the limit.

## References

1. Y. Chong, A. J. Kashyap, S. Chen, F. Chen, “Dynamics Analysis of a Discrete-Time Commensalism Model with Additive Allee for the Host Species,” *Axioms* 12 (2023), 1031, published 2023-11-02, https://doi.org/10.3390/axioms12111031.
2. “Some Bifurcations of Codimensions 1 and 2 in a Discrete Predator–Prey Model with Non-Linear Harvesting,” *Mathematics* 12 (2024), 2872, https://doi.org/10.3390/math12182872 (different model, methodological comparison).
3. X. He, Z. Zhu, J. Chen, F. Chen, “Dynamical analysis of a Lotka Volterra commensalism model with additive Allee effect,” *Open Mathematics* 20 (2022), 646–665, https://doi.org/10.1515/math-2022-0055 (continuous-time predecessor).

