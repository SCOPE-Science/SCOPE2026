# Sharp phase-dependent tracking speed for a moving thermal–oxygen refuge

## Finding
Consider the idealized, periodically moving admissible-depth interval
\[
I(t)=[L(t),U(t)],\qquad
L(t)=z_0+A\sin(\omega t),\quad
U(t)=z_0+h+A\sin(\omega t+\phi).
\]
For every amplitude \(A>0\), angular frequency \(\omega>0\), vertical offset \(z_0\in\mathbb R\), available mean interval width \(h\geq0\), and phase lag \(0\leq\phi\leq\pi\), seek an absolutely continuous, \(2\pi/\omega\)-periodic depth path \(z\) such that \(z(t)\in I(t)\) at every time and \(|z'(t)|\leq v\) almost everywhere. The **minimum required vertical speed** is as follows.

Write \(\alpha=\phi/2\) and \(h_0=2A\sin\alpha\). If \(h<h_0\), no admissible path exists at any finite speed. If \(h\geq2A\), a constant admissible path exists and \(v_{\min}=0\). For \(h_0\leq h<2A\), there is exactly one \(x\in[\alpha,\pi/2)\) solving
\[
h=2A\left[\sin x-(x-\alpha)\cos x\right],
\]
and the optimal bound is
\[
\boxed{v_{\min}=\omega A\cos x.}
\]
In particular the feasibility threshold \(h_0\) and the positive tracking speed are **different** tests: instantaneous availability of a suitable depth does not imply that a speed-limited occupant can remain suitable for the whole cycle.

For fixed \(0<\phi<\pi\), as \(\varepsilon=h-h_0\downarrow0\),
\[
\omega A\cos(\phi/2)-v_{\min}
=\omega\sqrt{A\sin(\phi/2)}\,\varepsilon^{1/2}+O(\varepsilon).
\]
For synchronized boundaries \(\phi=0\), instead,
\[
\omega A-v_{\min}
=\frac{\omega A}{2}\left(\frac{3h}{2A}\right)^{2/3}+o(h^{2/3})
\quad(h\downarrow0).
\]
Thus nonzero lag changes the speed-relief critical exponent from \(2/3\) to \(1/2\). For fixed \(\phi<\pi\), as \(h\uparrow2A\), \(v_{\min}\sim \omega(2A-h)/(\pi-\phi)\).

## Assumptions and scope
The depth is a scalar with no additional obstacles. The functions \(L\) and \(U\) represent, for example, a temperature-imposed lower depth boundary and an oxygen-imposed upper boundary, both assumed sinusoidal with identical amplitude and period and a fixed phase difference. These bounds are **assumed**, not fitted from field observations. Vertical motion is allowed in either direction with one symmetric instantaneous speed cap, no acceleration or energetic constraint, and no prescribed starting depth except periodicity. A physical water column may be included if it contains the whole interval at all times; for example, take \(z_0\geq A\) and water-column height at least \(z_0+h+A\). The claim does not extend automatically to unequal amplitudes, non-sinusoidal profiles, or inaccessible intermediate depths.

## Proof
1. Rescale to angular time \(\theta=\omega t\), let \(c=v/\omega\), and equip the phase circle with its geodesic distance \(d(\theta,\eta)\in[0,\pi]\). An absolutely continuous periodic depth trajectory whose speed is at most \(v\) corresponds exactly to a \(c\)-Lipschitz selection of \([L(\theta),U(\theta)]\). Instantaneous nonemptiness is equivalent to \(h\geq2A\sin\alpha\), since \(\max_\theta[L(\theta)-U(\theta)]=2A\sin\alpha-h\).
2. An admissible \(c\)-Lipschitz selection must satisfy \(L(\theta)-U(\eta)\leq c\,d(\theta,\eta)\) for every ordered pair of phases. Conversely, if all these inequalities hold, the explicit periodic function
\[
Z_c(\eta)=\sup_{\theta}\bigl[L(\theta)-c\,d(\theta,\eta)\bigr]
\]
is \(c\)-Lipschitz, is at least \(L(\eta)\), and is at most \(U(\eta)\). This proves sufficiency including at the sharp bound; no compactness or approximate-selection step is omitted.
3. For two phases at circle distance \(d\in[0,\pi]\), optimize over the common phase and both possible orientations. The maximum of \(L(\theta)-U(\eta)\) is
\[
2A\sin(\alpha+d/2)-h.
\]
Indeed the two orientations have extremal differences \(2A\sin((d+\phi)/2)\) and \(2A|\sin((d-\phi)/2)|\); the former dominates for \(d,\phi\in[0,\pi]\). Therefore, whenever \(h\geq h_0\),
\[
\frac{v_{\min}}{\omega}=
\max\left\{0,\sup_{0<d\leq\pi}
\frac{2A\sin(\alpha+d/2)-h}{d}\right\}.
\]
The endpoint \(d=0\) is understood as a one-sided limit. For \(h=h_0\) that limit is \(A\cos\alpha\); for \(h>h_0\) the quotient tends to negative infinity.
4. If \(h\geq2A\), the displayed numerator is nonpositive everywhere, and a constant depth between \(\max L=z_0+A\) and \(\min U=z_0+h-A\) is admissible. For \(h_0\leq h<2A\), put \(x=\alpha+d/2\) and
\[
G(x)=2A\bigl[\sin x-(x-\alpha)\cos x\bigr].
\]
The derivative of the quotient in step 3 has the sign of \(h-G(x)\). On \([\alpha,\alpha+\pi/2]\), \(G'(x)=2A(x-\alpha)\sin x\geq0\) and is strictly positive away from \(\alpha\). Moreover \(G(\alpha)=h_0\), \(G(\pi/2)=2A\), and \(\pi/2\) belongs to this interval. Thus the unique root in \([\alpha,\pi/2)\) gives the global quotient maximum, with the boundary interpretation when \(h=h_0\). Evaluating the quotient there using \(h=G(x)\) yields \(A\cos x\). This also verifies no larger value occurs at the circle antipode.
5. For \(0<\alpha<\pi/2\), expand \(G(\alpha+\delta)-G(\alpha)=A\sin\alpha\,\delta^2+O(\delta^3)\) and \(A[\cos\alpha-\cos(\alpha+\delta)]=A\sin\alpha\,\delta+O(\delta^2)\). For \(\alpha=0\), expand \(G(x)=(2A/3)x^3+O(x^5)\) and \(A(1-\cos x)=(A/2)x^2+O(x^4)\). Both asserted critical exponents and leading coefficients follow. At \(h\uparrow2A\), the derivative \(G'(\pi/2)=A(\pi-\phi)\) gives \(v_{\min}\sim\omega(2A-h)/(\pi-\phi)\). The case \(\phi=\pi\) has \(h_0=2A\), hence only the zero-speed feasible branch.

## Verification
The proof is exact for every real parameter in the stated domain. The included standalone `verification.py` numerically compares the root formula with independent one-dimensional optimization and tests the pairwise Lipschitz compatibility inequality and the two asymptotic regimes across deterministic parameter examples. Computation is supplementary and is not used to infer the universally quantified theorem. As a reproducible example, \(A=1\) metre, \(\phi=\pi/3\), \(h=1.5\) metres and period 24 hours give \(h_0=1\) metre, \(x\approx1.2921023255\) and \(v_{\min}\approx0.07202108385\) metres/hour.

## Relationship to prior work
Moravek et al. (2024) studied the time-dependent thermal value of off-channel refuges, including the necessity of adequate dissolved oxygen. Barrett, Gregory and Armstrong (2024) documented vertical temperature–oxygen restrictions in floodplain thermal refuges. Mejia et al. (2023) reviewed biological mobility and phase-lagged thermal refuges. These sources motivate the ecological constraints but do not, in the material inspected, supply a speed-minimal sinusoidal interval-selection classification. General Lipschitz-selection theory (Shvartsman 2020 and earlier work) supplies a much broader mathematical context and motivates treating interval tracking as a selection problem. The exact phase-lag root, the sharp feasibility boundary and the switch in critical exponents are the specific calculated invariants here, not a claim of inventing interval selections or their general existence criteria. A 2026 empirical depth-choice study by Barrett et al. examines asynchronous temperature and hypoxia but its accessible abstract does not establish the stated speed-constrained formula. See REVIEW.md for the explicitly bounded priority assessment.

## Limitations
This is a deterministic stylized geometric-viability theorem. It does not infer actual swimming speed capabilities, metabolic costs, ecological survival, oxygen physiology, or real thermal-depth trajectories. Free initial depth and full-cycle periodicity are essential; a fixed initial location, acceleration limits, spatial obstructions, vertical current, or different amplitudes require a new analysis. The publicly accessible abstract of one particularly relevant 2024 study and that of a recent 2026 study were not substitutes for full text; their uninspected portions remain a literature-priority risk. The numerical checks are not a substitute for the analytical proof.

## References
1. Moravek, J. A., Soto, T., Brashares, J. S., and Ruhí, A. (2024). *Restored off-channel pond habitats create thermal regime diversity and refuges within a Mediterranean-climate watershed.* Restoration Ecology. First published 2024-02-08. https://doi.org/10.1111/rec.14110
2. Barrett, H., Gregory, S., and Armstrong, J. (2024). *Evidence of a temperature–oxygen squeeze within floodplain thermal refuge habitats.* Freshwater Biology 69, 1118–1130. First published 2024-06-22. https://doi.org/10.1111/fwb.14294
3. Mejia, F. H. et al. (2023). *Closing the gap between science and management of cold-water refuges in rivers and streams.* Global Change Biology 29, 5482–5508. https://doi.org/10.1111/gcb.16844
4. Shvartsman, P. (2020). *The Core of a 2-Dimensional Set-Valued Mapping. Existence Criteria and Efficient Algorithms for Lipschitz Selections of Low Dimensional Set-Valued Mappings.* arXiv:2010.04540. https://arxiv.org/abs/2010.04540
5. Barrett, H., Ruprecht, J., Levi, T., Ebersole, J., and Armstrong, J. (2026). *Asynchronous timing of hypoxia and thermal stress induces diel vertical movement.* Limnology and Oceanography. https://doi.org/10.1002/lno.70536
