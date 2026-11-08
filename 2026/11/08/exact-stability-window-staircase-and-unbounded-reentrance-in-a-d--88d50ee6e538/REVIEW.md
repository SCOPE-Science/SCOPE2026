# Scientific review — exact delay-stability staircase

## Correctness — PASS

The theorem assumes a positive coexistence equilibrium and \(0<\alpha<\beta\), \(\gamma>0\), and states precisely which delays are spectrally stable. The equilibrium reduction and characteristic polynomial match the exact model in Alawfi (2026). The imaginary-root quartic has the two claimed positive roots, but the sine equation distinguishes their phases: the lower frequency requires \(2\pi-\theta\), rather than \(\theta\). The strict transverse-crossing formula follows by explicit differentiation. The characteristic-root modulus bound prevents an uncounted right-half-plane crossing from infinity, so the count is exhaustive. The integer staircase and the positive-parameter family follow by algebra. The standalone checker verifies coefficient reductions and both frequency branches, and its independent contour root counts sample alternating stable and unstable intervals. Possible coincident crossings are excluded from stable intervals. The proof does not assert global attraction, nonlinear Hopf criticality, or periodic-orbit stability.

## Originality — PASS within inspected evidence

Alawfi (2026), https://doi.org/10.1038/s41598-026-74386-7, supplies the exact model, coexistence equilibrium, linearized characteristic equation, and imaginary-frequency quartic, and examines finitely many stability transitions by numerical continuation. Its inspected model, Hopf, numerical, discussion and conclusion sections do not state the complete all-delay unstable-pair counting formula, the exact integer formula for the number of reentrant stable windows, or the unbounded count and sharp small-growth-rate asymptotic in the exhibited positive parameter family.

Peng and Jiang (2025), https://doi.org/10.3390/modelling6030084, establish multiple stability switches for a hunting-cooperation model with a different quasipolynomial; their indexed theorem and conclusion concern a different ecological mechanism. The fully read publicly available result “Exact reentrant coexistence stability with delayed predator self-regulation” establishes one reentrant window for predator delayed self-limitation, rather than an exact all-delay staircase and unbounded-window family for delayed prey regulation. Freedman and Rao (1986), https://doi.org/10.1137/0146037, and standard geometric delay-switch criteria provide relevant general methods, but the inspected material does not give the present concrete realization or formula.

Residual priority risks: full text of some older general delay criteria and the Peng–Jiang article was not available through the inspected channels, so an unlocated stronger theorem with the same characteristic equation could dominate part of the claim. Novelty is a best-evidence assessment, not independent priority certification.

## Mathematical value — PASS

The sharp count and complete stability set classify delay-triggered recovery across all delay values, whereas a few numerical Hopf points do not distinguish a finite number of transient recovery windows from an arbitrarily large number. The concrete all-positive family shows every prescribed finite number of reentries can be realized biologically; the exact threshold for \(m\) windows and the asymptotic \(r^{-1/2}\) law quantify the mechanism. These are nontrivial parametric and spectral classifications, rather than a small numerical correction or a generic consequence of one Hopf criterion.

Self-review: passed. Independent audit: not yet performed.
