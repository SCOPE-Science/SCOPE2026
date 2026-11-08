# Scientific assessment

**Claim assessed:** The gas-independent, matched-flux two-phase stationary classification and the unique \(p\)-dependent optimal resetting ratio for positive increasing dense fluxes, specialized to \(F_\ell(\rho)=c\rho^p\), \(0<p\le1\).

## Correctness — PASS

The stationary directional equations imply \(S'=-r\rho\) and \(R'=-(r+\alpha)\sigma\). Their conserved quadratic first integral vanishes from far-field decay and transmission at the interface. The outward sign forces \(\sigma=q\rho\) everywhere off the source, yielding the exact decreasing-flux equation \(F'(\rho)\rho'=-\Gamma\rho\). Strict monotonicity and unbounded dense flux give a unique center and width whenever \(\Gamma M/2>F_*\); \(F_g'(0)>0\) yields a gas tail extending to infinity. The mass-jump and source constraints are verified explicitly. The power-law width is an elementary but nontrivial exact function of the physical control ratio, with a unique derivative zero and sharp global endpoint limits. A standalone checker passed 570 deterministic scalar conditions on independent flux families and parameters; finite tests supplement the proof.

## Originality — PASS, qualified

The closest source is Grange, arXiv:2610.26149, inspected in full through HTML sections 2–5 and appendices, including its pre-existing general flux first integral. It treats a specific dilute flux and constant-speed dense phase, where the normalized optimum is \(e\). This finding changes the dense constitutive law, proves a general gas-independent inverse-flux classification, and gives the new exponent-dependent exact optimum \(p^{p/(p-1)}\) for \(0<p<1\). Two accessible earlier findings motivated by the same paper address (i) stochastic concentration and Wasserstein distances between gas and dense branches of the **original linear-core model** and (ii) the pure-gas log-density-score law. Neither implies a variable-core exponent optimum. Semantic searches of indexed mathematical findings, primary literature searches, and related literature abstracts did not expose the same theorem. Search failure alone is not a novelty proof; the general first integral in the primary source leaves a meaningful risk of an unindexed deduction.

## Value — PASS

Holding the phase-interface flux constant while changing the gaseous transport law is a natural test of whether the dilute bath controls the condensation geometry. The proof identifies a full functional invariance, not a single fitted numerical coincidence. Allowing dense-phase slowdown produces a genuine continuum of sharp design laws: at a square-root core flux the optimal normalized reset scale is \(2\) rather than the previously known \(e\), and the exponent determines the optimum monotonically. These quantities are structural and directly interpretable in the model; neither generic correctness nor computation alone is the justification of value.

## Closest literature, limitations and risks

- P. Grange (2026), arXiv:2610.26149, sections 2–5, appendices A and B: full relevant HTML examined. General invariant and linear-core \(e\) optimum acknowledged; the nonlinear dense-core family is not treated there.
- A. G. Thompson et al. (2011), *Lattice models of nonequilibrium bacterial dynamics*: abstract and bibliographic record examined. Density-dependent propulsion and lattice hydrodynamics, but no identified local-reset droplet optimum.
- A. Pelizzola, M. Pretti and M. Zamparo (2021), *Simple exclusion processes with local resetting*: abstract and bibliographic record examined. A distinct exclusion-lattice local-reset phase diagram rather than the present two-velocity continuum classification.
- The claim is for a specified symmetric, monotone, single-core stationary configuration. It does not prove dynamic stability, microscopic universality, unique global steady-state selection or arbitrary coexistence rules. The core generalization follows from known stationary equations but requires new constitutive integration and a sharp optimization. An unindexed equivalent result is a remaining originality risk.

Self-review: passed. Independent audit: not yet performed.
