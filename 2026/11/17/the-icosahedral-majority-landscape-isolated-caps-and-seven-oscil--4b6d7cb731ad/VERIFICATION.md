---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification

This verification describes the exact finite-state computations used in the result, not an independent audit. The exhaustive domain is all 4096 labelled binary states of the 12-vertex icosahedral graph. `check_finite.py` is standard-library-only; `check_symmetry.py` requires NetworkX 2.8 or newer (the successful recorded replay used 3.6.1). Run them in the same directory. Both were executed successfully from the actual delivered source contents, generating the included output logs and 82-row state-orbit certificate.

The first checker builds the graph from two poles and two five-cycles, derives integer masks, constructs the full 4096-entry deterministic transition map, and checks every point of the claimed \(F^{7}=F^{5}\) identity. It explicitly enumerates fixed points, normalized primitive two-cycles, all first-entry times and the basin partitions; it checks that the 12 closed-neighborhood states are exactly the nonunanimous fixed states and have singleton basins.

The second checker starts from an independently specified 30-edge graph and a different direct voting routine. It compares that graph with the canonical built-in icosahedral graph, enumerates all 120 automorphisms, checks equivariance on every state, enumerates the seven temporal-cycle symmetry classes, and independently recomputes entrance/basin histograms. It also writes all 82 geometric state-orbit representatives to `state_orbits.csv`; state-orbit sizes total 4096 and the seven geometric cycle-class sizes total 156.

Limitations: exhaustive correctness is for the 12-vertex icosahedral graph under this one synchronous rule only. A passed script is a reproducible finite proof conditional on ordinary Python integer/combinatorial semantics, not a formal external or expert certification. Historical priority remains qualified by an inaccessible relevant 1980 article. No independent mathematical audit has been conducted.
