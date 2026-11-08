# Scientific assessment

**Correctness — PASS.** The stationary angular OU covariance and exact Green–Kubo integral are reconstructed from the stated SDE. The proof verifies the small-inertia slope, strict zero-chirality increase, the large-inertia cancellation bound for every nonzero drift, and uniform localization of all weak-chirality optimizers. The only numerical role is consistency checking with `verify.py`; finite evaluations do not prove the all-parameter theorem.

**Originality — PASS, qualified.** Scholz et al. (2018), Eqs. (3),(8),(9), already give the exact same chirality-dependent orientational covariance and full incomplete-gamma diffusivity; no exact kernel or nonmonotonicity is claimed new. Tiwari et al. (2026) provide nonchiral rotational-inertia analysis, while Pattanayak et al. (2025) study chiral particles with overdamped angular dynamics. Ai et al. (2024) already describe chiral rotational-inertia diffusion peaks in dense systems, but the full text was unavailable; the priority of any sharp free-swimmer weak-chirality asymptotics against that paper is not independently resolved. The added theorem is the all-nonzero-chirality existence and every-maximizer singular optimum scaling with its sharp constant, proved from a known transport expression rather than restating it.

**Value — PASS.** This gives a natural and sharp transport-design scale for the physically meaningful rotational relaxation parameter, and quantitatively distinguishes arbitrarily weak chirality from exactly zero chirality. It is not a narrow arbitrary parameter slice or a tiny finite numerical improvement.

**Limitations.** The model is free-space, stationary and noninteracting. There is no uniqueness claim for finite nonzero chirality, no interacting/glassy generalization, and publication priority remains conditional on further full-text comparison.

Self-review: passed. Independent audit: not yet performed.
