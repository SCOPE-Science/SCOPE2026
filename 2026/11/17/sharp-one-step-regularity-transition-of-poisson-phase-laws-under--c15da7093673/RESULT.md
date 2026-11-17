# Sharp one-step regularity transition of Poisson phase laws under a sinusoidal circle kick

## Finding
Let \(P_a\) be the circular Poisson probability density with parameter \(a\in\mathbb C\), \(|a|<1\). For any \(s,\gamma,\omega\in\mathbb R\), consider the degree-one phase map
\[
T_{s,\gamma,\omega}(\theta)=\theta+\omega-s\sin(\theta+\gamma)\pmod{2\pi}
\]
and its pushed-forward probability measure \(\nu_s=(T_{s,\gamma,\omega})_\#(P_a(\theta)\,d\theta)\). The measure \(\nu_s\) always has a density \(q_s\), and exactly the following three regimes occur.

1. If \(|s|<1\), then \(q_s\) is strictly positive and real analytic, and it is a Poisson density **if and only if \(s=0\)**.
2. If \(|s|=1\), there is precisely one critical source angle \(c\pmod{2\pi}\) and its image \(y_c=T(c)\), at which
\[
q_s(y_c+v)=\frac{2P_a(c)}{6^{2/3}}|v|^{-2/3}\bigl(1+O(|v|^{1/3})\bigr),\qquad v\longrightarrow0.
\]
3. If \(|s|>1\), there are precisely two nondegenerate critical source angles per period. Each fold at \(c\) contributes, from the side where its two nearby inverse branches exist, a positive singularity
\[
\sqrt{\frac{2}{|T''(c)|}}P_a(c)|y-T(c)|^{-1/2}+O(1),\qquad |T''(c)|=\sqrt{s^2-1}.
\]
Other inverse branches contribute nonnegative terms; contributions of coincident critical images add.

Consequently the exact Lebesgue-integrability classification on the circle is
\[
\boxed{\begin{array}{ll}
|s|<1:&q_s\in L^\infty,\\
|s|=1:&q_s\in L^p\ \Longleftrightarrow\ 1\le p<3/2,\\
|s|>1:&q_s\in L^p\ \Longleftrightarrow\ 1\le p<2.
\end{array}}
\]
In particular, \(\nu_s\) belongs to the Poisson family **exactly for \(s=0\)**. These assertions hold for every interior parameter \(|a|<1\), including \(a=0\), and every choice of forcing and rotation phases.

For a single common-frequency fibre of the discrete Kuramoto–Sakaguchi update with a nonzero Poisson order parameter \(Z=a\), take \(s=K|a|>0\) and a suitable phase shift \(\gamma\). Thus a single positive-coupling step never preserves the exact Poisson family. Its conditional density is smooth for \(0<K|a|<1\), has the cubic-cusp exponent \(-2/3\) at \(K|a|=1\), and has quadratic-fold exponents \(-1/2\) for \(K|a|>1\).

## Assumptions and scope
Angles are elements of \(\mathbb R/(2\pi\mathbb Z)\); all densities are relative to angular Lebesgue measure \(d\theta\). For \(|a|<1\),
\[
P_a(\theta)=\frac{1-|a|^2}{2\pi|e^{i\theta}-a|^2}>0,\qquad
\int_0^{2\pi}P_a(\theta)\,d\theta=1.
\]
The kick parameters are fixed for the one-step pushforward and the order parameter is evaluated from the **pre-kick** distribution. In the self-consistent interpretation, common intrinsic phase increment and phase lag enter \(\omega\) and \(\gamma\); no frequency averaging is performed. At \(a=0\) the self-consistent kick amplitude vanishes, although the externally forced theorem also applies to \(a=0\) at nonzero \(s\). The singular asymptotics are for ordinary angular coordinates; they are invariant under additive rotation of \(y\).

The theorem addresses one iteration of the continuum density transfer operator, not a stationary invariant density or long-time bifurcation. It does not claim that a finite atomic oscillator ensemble develops an absolutely continuous density.

## Proof
**(i) Smooth branch.** A lift has derivative \(T'(\theta)=1-s\cos(\theta+\gamma)\). When \(|s|<1\), the derivative is uniformly positive, so \(T\) is an analytic orientation-preserving circle diffeomorphism. Its pushforward density is \(q_s(T(\theta))=P_a(\theta)/T'(\theta)\), proving positivity, boundedness and analyticity.

To decide Poisson-family closure without a perturbation expansion, let \(\Phi_a(z)=(z+a)/(1+\bar a z)\), an orientation-preserving boundary Möbius transformation that pushes normalized angular Lebesgue measure to \(P_a\,d\theta\). Suppose \(T_\#P_a=P_b\) for some \(|b|<1\). Then \(G=\Phi_b^{-1}\circ T\circ\Phi_a\) is an orientation-preserving circle homeomorphism preserving normalized angular Lebesgue measure. For any lifted interval, measure preservation and orientation imply that its image has the same angular length; hence \(G\) is a rigid rotation. It follows that \(T\) itself is a boundary Möbius transformation.

The angular derivative of any orientation-preserving boundary Möbius transformation has the form
\[
\frac{1-|c|^2}{|e^{i\theta}-c|^2}\quad (|c|<1),
\]
up to a rotation of its angular argument. If \(c\ne0\), its Fourier series contains a nonzero second harmonic, whereas \(T'(\theta)=1-s\cos(\theta+\gamma)\) has no second harmonic. Therefore \(c=0\), the Möbius transformation is a rotation and \(s=0\). Conversely \(s=0\) simply rotates \(P_a\) to \(P_{e^{i\omega}a}\). This establishes exact nonclosure for every nonzero subcritical kick.

**(ii) Critical cubic cusp.** At \(|s|=1\), the derivative vanishes at exactly one point \(c\pmod{2\pi}\), where \(s\cos(c+\gamma)=1\). It is nonnegative everywhere and positive except at \(c\), so \(T\) is a circle homeomorphism. At the critical point \(T''(c)=0\) and \(T'''(c)=1\). For a local source displacement \(u\) and target displacement \(v\), Taylor's formula gives
\[
v=\frac{u^3}{6}+O(u^5),\qquad T'(c+u)=\frac{u^2}{2}+O(u^4).
\]
The inverse satisfies \(|u|=(6|v|)^{1/3}(1+O(|v|^{2/3}))\). Since \(P_a(c+u)=P_a(c)+O(u)\), the positive Jacobian change of variables gives the stated sharp \(|v|^{-2/3}\) coefficient and relative remainder. The density is smooth away from this single image point and locally integrable at it.

**(iii) Supercritical folds.** For \(|s|>1\), the equation \(T'(c)=0\) is \(\cos(c+\gamma)=1/s\), with exactly two solutions modulo \(2\pi\). Their second derivatives are nonzero and have magnitude \(\sqrt{s^2-1}\). Near each one, writing \(u=\theta-c\),
\[
v=T(c+u)-T(c)=\tfrac12 T''(c)u^2+O(u^3).
\]
On the accessible side \(vT''(c)>0\), the two local inverse branches satisfy \(u_\pm=\pm\sqrt{2|v|/|T''(c)|}+O(v)\). The transfer-operator formula \(q_s(y)=\sum_{T(\theta)=y}P_a(\theta)/|T'(\theta)|\) yields their combined leading term \(P_a(c)\sqrt{2/|T''(c)|}|v|^{-1/2}\), with bounded remainder. There are finitely many inverse branches for fixed \(s\). At a coincident target critical value, divergent contributions add because \(P_a>0\). Elsewhere all branches are smooth. The transfer density exists almost everywhere and integrates to one, since the critical set is finite and the map is smooth and nonconstant on each monotonicity interval.

**(iv) Sharp integrability and closure.** A local positive density asymptotic to \(C|v|^{-\eta}\), with \(0<\eta<1\), belongs to \(L^p\) locally precisely when \(p\eta<1\); the equality case diverges logarithmically. Combining the analytic complement of the finite critical-value set with the strict positive coefficients above proves the three stated sharp ranges. Poisson densities are globally bounded for \(|a|<1\), so the singular cases cannot be Poisson. Together with part (i), the Poisson closure condition is exactly \(s=0\).

## Verification
The standalone standard-library script \(\texttt{verify.py}\) directly evaluates the original sine map, its first three derivatives, and the original Poisson density. It checks one-sided and two-sided critical coefficients numerically at four shrinking scales each, verifies the analytic critical-point identities for positive and negative amplitudes and three forcing phases, and prints reproducible results. A representative complex parameter is \(a=0.35+0.13i\). The computation is a consistency test; the analytical change-of-variables and Möbius arguments prove the universal statements.

Run from the directory containing this file using \(\texttt{python3 verify.py}\). Expected first line: \(\texttt{VERIFY_OK critical_cubic_cases=4 fold_cases=4 derivative_grid=351}\).

## Relationship to prior work
Gade and Gupta [1] derive the discrete-time Kuramoto–Sakaguchi continuum transfer equation and report a numerical breakdown of the Ott–Antonsen reduction. The **qualitative nonclosure** is known. The present statement gives a nonperturbative all-amplitude impossibility theorem together with the exact one-step density regularity and \(L^p\) phase diagram.

A published mathematical finding [2] already gives the complete leading weak-kick circular-cumulant sequence for this same additive sine update. The new statement does **not** claim the weak-kick quadratic coefficient: it treats every finite amplitude and the two distinct critical-density exponents. Gong, Tönjes and Pikovsky [3] establish exact Poisson-kernel preservation for their distinct **Möbius phase update**; that construction supplies the structural contrast underlying the Möbius argument here. Zhai, Xiao and Zheng [4] discuss the classical loss of invertibility of sine circle maps at unit normalized kick magnitude. The unit invertibility threshold, the generic fold/cusp exponents, and classical change-of-variables principles are not individually new; the claim is their complete sharp consequence for Poisson phase laws in the specified discrete update, including exact closure and integrability classification. These are statement-level comparisons rather than proof of exhaustive historical priority.

## Limitations
The 2026 motivating preprint was accessible at its verified public abstract but its full text could not be inspected; any theorem on one-step Poisson-density singularities in the unavailable sections remains a historical-priority risk. Broad mathematical theory of density folds and boundary Möbius maps may provide equivalent derivations. No claim is made about preservation under frequency integration, stationary densities, absolute continuity after arbitrary repeated noninvertible steps, finite-ensemble density limits, or universal bounds uniform as \(|a|\uparrow1\). The transition is a one-step regularity result; it does not establish a synchronization or desynchronization threshold for the long-time dynamics.

## References
[1] P. M. Gade and S. Gupta, *Discrete-time Kuramoto model with phase lag: Linear stability analysis and onset of synchronization*, arXiv:2609.22715v1, first posted 2026-09-19, https://arxiv.org/abs/2609.22715.

[2] *Universal quadratic circular-cumulant cascade under a discrete Kuramoto phase kick*, published mathematical record, 2026-11-08, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-universal-quadratic-circular-cumulant-cascade-under-a-discrete-k--df3799d60a95.

[3] C. C. Gong, R. Tönjes and A. Pikovsky, *Coupled Möbius maps as a tool to model Kuramoto phase synchronization*, Physical Review E 102 (2020), 022206, https://doi.org/10.1103/PhysRevE.102.022206; preprint arXiv:2001.07593.

[4] Y. Zhai, J. Xiao and Z. Zheng, *Synchronization–desynchronization transitions in networks of circle maps with sinusoidal coupling*, Chinese Physics B 32 (2023), 060505, https://doi.org/10.1088/1674-1056/acc062.
