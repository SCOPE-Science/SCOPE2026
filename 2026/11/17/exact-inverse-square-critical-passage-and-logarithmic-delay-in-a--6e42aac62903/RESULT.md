# Exact inverse-square critical passage and logarithmic delay in an adaptive oscillator pair

## Finding

In the symmetric two-oscillator adaptive Kuramoto reduction at the coalescence of the antipodal coupling and identical-frequency thresholds, approach to the synchronizing state is delayed by an exactly quantified nonhyperbolic bottleneck. Fix an adaptation timescale \(\epsilon>0\), a fixed initial coupling \(\kappa_0\in\mathbb R\), and a fixed capture threshold \(c\in(0,2)\). For a starting phase \(\varphi_0\in(0,\pi)\), put \(v_0=1+\cos\varphi_0\), with \(0<v_0<c\). Under

\[
\dot\varphi=-\kappa\sin\varphi,\qquad
\dot\kappa=\epsilon(1+\cos\varphi-\kappa),
\]

let \(T_c(v_0,\kappa_0)\) be the first time \(1+\cos\varphi(t)=c\). Then the hitting time is finite and, as \(v_0\downarrow0\) with \(\epsilon,\kappa_0,c\) fixed,

\[
\boxed{T_c(v_0,\kappa_0)
=\frac{\exp(-2\kappa_0/\epsilon)}{2v_0}
+\left(\frac14+\frac1\epsilon\right)\log\frac1{v_0}
+O_{\epsilon,\kappa_0,c}(1).}
\]

Equivalently, for initial angular distance \(\rho=\pi-\varphi_0\downarrow0\),

\[
T_c=\exp(-2\kappa_0/\epsilon)\rho^{-2}
+\left(\frac12+\frac2\epsilon\right)\log(1/\rho)+O_{\epsilon,\kappa_0,c}(1).
\]

For any \(\varphi_0\in(0,\pi)\) and finite initial coupling, the solution converges to synchronized phase \(\varphi(t)\to0\) and coupling \(\kappa(t)\to2\). Exactly antipodal initial phase \(\varphi_0=\pi\) is exceptional and remains antipodal for all time.

The leading delay depends exponentially on the initial coupling, whereas the second, logarithmic coefficient depends only on adaptation speed. In particular, a linearization alone does not determine the first passage clock.

## Assumptions and scope

The differential equations above are precisely the normalized symmetric two-oscillator subsystem with zero intrinsic-frequency mismatch, zero phase lag, and adaptation strength \(a=1\) of Jüttner–Martens, equations (15a,b) in the 2023 article. Their preprint was publicly available on 2022-09-21. The statement concerns real finite \(\kappa_0\), \(\epsilon>0\), phases in \((0,\pi)\), and fixed \(c\in(0,2)\). Neither \(c\) nor the model parameters vary with \(v_0\); the \(O(1)\) remainder is uniform for sufficiently small \(v_0\) only after these quantities have been fixed. The opposite angular side follows by reflection.

Define \(v=1+\cos\varphi\). The exact, nonsingular dynamics on the invariant strip \(0<v<2\) is

\[
\dot v=\kappa v(2-v),\qquad \dot\kappa=\epsilon(v-\kappa).
\]

## Proof

**1. Boundedness, eventual approach, and finite hitting time.** The logistic factor makes \((0,2)\) invariant, and the variation-of-constants formula

\[
\kappa(t)=e^{-\epsilon t}\kappa_0+\epsilon\int_0^t e^{-\epsilon(t-s)}v(s)\,ds
\]

shows that \(\kappa\) is bounded between appropriate constants depending only on \(\kappa_0\) and the interval \([0,2]\). In particular, \(\kappa(t)\ge -|\kappa_0|e^{-\epsilon t}\). The exact logit equation is

\[
\frac{d}{dt}\log\frac{v}{2-v}=2\kappa.
\]

Integration gives a positive lower bound \(v(t)\ge m>0\) depending on the initial state, because the negative part of the logit growth has integral at most \(2|\kappa_0|/\epsilon\). Consequently \(\kappa'=\epsilon(v-\kappa)\ge\epsilon(m-\kappa)\); after a finite time \(\kappa(t)\ge m/2\). The logit then diverges to \(+\infty\), so \(v(t)\to2\) and \(\kappa(t)\to2\). For any threshold \(v_0<c<2\), a finite first hitting time \(T_c\) therefore exists. At such a first upward crossing, \(\kappa(T_c)\ge0\); its value is uniformly bounded in the limit \(v_0\downarrow0\).

**2. An exact reciprocal integrating factor.** Introduce

\[
H(v,\kappa)=\frac{\exp(-2\kappa/\epsilon)}{v}.
\]

A direct derivative using both differential equations, with no approximation, yields

\[
\frac{dH}{dt}=-(2-\kappa)e^{-2\kappa/\epsilon}.
\]

Since \(\kappa\) is uniformly bounded for \(0\le t\le T_c\), Taylor's theorem on that compact interval gives

\[
(2-\kappa)e^{-2\kappa/\epsilon}
=2-\left(1+\frac4\epsilon\right)\kappa+R(\kappa),\qquad
|R(\kappa)|\le C_{\epsilon,\kappa_0,c}\kappa^2.
\]

The Taylor bound remains valid for negative as well as positive \(\kappa\); the constant can be chosen independent of sufficiently small \(v_0\).

**3. Two exact time integrals.** Integrating the logit identity from \(v_0\) to \(c\) gives

\[
\int_0^{T_c}\kappa\,dt
=\frac12\log\frac{c(2-v_0)}{v_0(2-c)}
=\frac12\log(1/v_0)+O_c(1).
\]

The square-coupling balance

\[
\frac{d}{dt}\frac{\kappa^2}{2\epsilon}=v\kappa-\kappa^2
\]

and the exact identity \(v\kappa=\dot v/(2-v)\) provide

\[
\int_0^{T_c}\kappa^2\,dt
=\log\frac{2-v_0}{2-c}
+\frac{\kappa_0^2-\kappa(T_c)^2}{2\epsilon}
=O_{\epsilon,\kappa_0,c}(1).
\]

The last boundedness follows from \(0<v_0<c\), fixed \(c<2\), and the uniform coupling bound. In particular, the error in integrating the Taylor remainder is uniformly bounded as the passage time diverges; one must not treat a merely pointwise Taylor expansion as sufficient here.

**4. Passage asymptotics.** Integrating the exact \(H\) identity and invoking the preceding two integrals gives

\[
H(v_0,\kappa_0)-H(c,\kappa(T_c))
=2T_c-\left(1+\frac4\epsilon\right)\int_0^{T_c}\kappa\,dt+O(1).
\]

The first term on the left is \(e^{-2\kappa_0/\epsilon}/v_0\); the second is bounded because \(c\) is fixed and \(\kappa(T_c)\) is bounded. Solving for \(T_c\) yields

\[
T_c=\frac{e^{-2\kappa_0/\epsilon}}{2v_0}
+\frac{1+4/\epsilon}{4}\log(1/v_0)+O(1),
\]

as asserted. Lastly, \(v_0=1-\cos\rho=\rho^2/2+O(\rho^4)\), so \((2v_0)^{-1}=\rho^{-2}+O(1)\) and \(\log(1/v_0)=2\log(1/\rho)+O(1)\), proving the equivalent angular statement.

## Verification

The accompanying standalone `check.py` verifies the reciprocal integrating-factor identity, the logit derivative, and the squared-coupling balance symbolically using SymPy. It independently integrates the two-dimensional initial-value problem with high-precision adaptive ODE integration and event detection for three parameter combinations, including positive, zero, and negative initial coupling, and for five successively halved small initial displacements. It subtracts the two explicit asymptotic terms and checks that the remaining differences are small and consistent with a finite limiting remainder. This numerical diagnostic cannot replace the proof of the uniform remainder, which is given by the exact integral argument above. Run with `python check.py` (requires SymPy, NumPy, and SciPy).

## Relationship to prior work

The model and symmetric reduction are from B. Jüttner and E. A. Martens, *Complex dynamics in adaptive phase oscillator networks*, first circulated 2022-09-21 (arXiv:2209.10514), later *Chaos* 33 (2023), 053106. The open-access article, in particular its equations (13)–(15), Sec. III B stability/bifurcation analysis and Sec. V discussion, describes locking, bistability, and oscillatory bifurcations rather than a quantitative critical first-passage clock. This contribution is restricted to the identical-frequency, adaptation-strength-one degeneracy and derives the exact inverse-square and logarithmic coefficients from two time-integral identities. It does not claim invention of adaptive Kuramoto dynamics, phase locking, or generic parabolic slowing.

Earlier adaptive-coupling synchronization frameworks (Ha–Noh–Park 2016; Ha–Lee–Li–Park 2018) use alternative learning rules and provide sufficient asymptotic synchronization criteria or singular-perturbation limits, respectively; the accessible abstracts do not establish this exact finite-adaptation passage formula. Their full journal texts were not verified in the present comparison, so implicit equivalence remains a literature risk. Related indexed results on discrete two-clock sine maps and critical synchronization have different state updates and do not imply the stated adaptive continuous-time hitting-time law merely by sharing an inverse-power exponent.

## Limitations

The asymptotic statement holds at exactly \(a=1\), \(\omega=0\), and zero phase lag, for fixed \(\epsilon\), fixed initial coupling, and fixed positive capture threshold. It is not uniform under joint limits such as \(\epsilon\downarrow0\), \(c\downarrow0\), or \(\kappa_0\to\infty\). It does not classify time-varying adaptation, finite frequency mismatch, nonlinear synaptic constraints, or multi-oscillator networks. The \(O(1)\) constant is not given explicitly. Scientific originality is assessed against inspected literature, not independently certified or guaranteed against unindexed equivalents. No independent mathematical audit has been performed.

## References

1. B. Jüttner and E. A. Martens, *Complex dynamics in adaptive phase oscillator networks*, arXiv:2209.10514 (public 2022-09-21); *Chaos* **33** (2023), 053106, https://doi.org/10.1063/5.0133190.
2. S.-Y. Ha, S. E. Noh and J. Park, *Synchronization of Kuramoto Oscillators with Adaptive Couplings*, *SIAM Journal on Applied Dynamical Systems* **15** (2016), 162–194, https://doi.org/10.1137/15M101484X.
3. S.-Y. Ha, J. Lee, Z. Li and J. Park, *Emergent Dynamics of Kuramoto Oscillators with Adaptive Couplings: Conservation Law and Fast Learning*, *SIAM Journal on Applied Dynamical Systems* **17** (2018), 1560–1588, https://doi.org/10.1137/17M1124048.
