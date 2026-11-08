# Self-review: Nonreversible return laws give a single sharp Crank–Nicolson positivity window

## Correctness — PASS

The universal claim is established by an exact, all-dimension first-return generating-function identity for the diagonal of a uniformized finite Markov resolvent. For a nonabsorbing state its reciprocal is strictly increasing in the geometric return parameter; transient never-return probability is explicitly included. The Cayley identity therefore converts the full entrywise positivity requirement to a single interval. Stationary return limits classify each state; global threshold and closed-block classification follow. The directed three-cycle computation is exact, not empirical. The standalone verifier passed 5,754 symbolic and exact-rational assertions; finite assertions are not the proof of universal quantifiers.

## Originality — PASS (qualified)

The closest prior, *A resolvent-return law for Crank–Nicolson positivity on reversible Markov chains* (2026, public record `https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-a-resolvent-return-law-for-crank-nicolson-positivity-on-reversib--d475df91cd2a`), already contains the general diagonal resolvent criterion, reversible sharp threshold and irreducible unconditional classification. Those are not newly claimed. Its actual statement expressly does not classify nonreversible reentrant step windows. The current first-return monotonicity proof removes reversibility even for complex-spectrum generators and handles all reducible chains. Fallat–Tsatsomeros (2002) supplies classical Cayley M-matrix identities; Horváth (1998) gives broad RK positivity radii; Blanes–Iserles–Macnamara (2021) develops different positivity-preserving graph-Laplacian integrators. No inspected primary full-text portion supplies the exact universal nonreversible one-interval law. Strongest remaining risk: an equivalent stochastic-Cayley theorem may already be implicit in older Markov renewal literature, and the Horváth full paper was not available for a complete comparison. Missing search hits are not a priority proof.

## Value — PASS

The gap is mathematical: real-spectrum reversible formulas cannot justify the no-reentrance property for nonreversible generators. Exact integrator positivity on directed CTMCs matters for probability preservation, even when the Runge–Kutta method is not uniformly positivity preserving across all problems. The first-return theorem gives a complete natural fixed-generator step classification, while the directed three-cycle shows an explicit nontrivial critical step \(1+\sqrt5\). The reducible/unconditional taxonomy is a natural consequence of the main theorem and is not elevated to an independent contribution. No wider nonlinear or high-order claim is made.

## Closest literature and limits

Blanes–Iserles–Macnamara, arXiv:2102.08242v1 (2021; full HTML v2 inspected); Fallat–Tsatsomeros, ELA 9 (2002), pages 190–196 (primary PDF inspected); Horváth, Applied Numerical Mathematics 28 (1998), bibliographic abstract only; the 2026 reversible-chain finding cited above (full RESULT.md inspected). General first-return identities are taken as standard. The numerical certificate is finite and supplementary; no independent validation has occurred.

Self-review: passed. Independent audit: not yet performed.
