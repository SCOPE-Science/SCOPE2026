---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Reassessed the repaired statement with the original positive D1,D2,L, finite N and stationary uniform initial law. The original proof's displayed mean bracket rate (RESULT.md lines 54–60) dropped k² while using angular derivatives, so it could not yield the energy in line 64 for general L as written. The repaired proof uses tagged martingale coefficients sqrt(2D1)(1+k sum_j partial_j chi) and -sqrt(2D2)k partial_j chi, yielding 2D1+2<E,SE> for E=chi. The bounded corrector preserves the long-time variance. Divergence cancellation yields Haar, the mean-zero coercive corrector exists, and its energy equals <f_a,chi>. Completion of the square gives the deficit energy about a times S^{-1}g, with g the unit-amplitude tagged drift. B S^{-1}g is the sum of pair-sine frequencies times k/(D1+D2), vanishing only at N=1; this settles all nonzero amplitudes and the a=0 boundary is explicit. The positive lower gain holds at a≠0. Full-current averaging gives the entropy expression with both inverse diffusivities. The energy-norm series at zero has leading deficit a^4 from orthogonal pair modes, with eigenvalue k²(4D1+2D2) and squared norm 1/2; conjugation by angle translation removes odd powers. This recovers the stated coefficient and fixed-parameter O(a^6). The supplied Galerkin script was inspected, not executed; finite truncations are not the proof.

## originality

PASS

Best of current knowledge for the unchanged many-follower claim only: the indexed prior pair formula, stationary-law and entropy inputs, and generic skew-drift energy bound do not establish non-saturation at every nonzero coupling for N≥2 plus the explicit fourth-order defect. The repaired result does not claim novelty for those inputs, the N=1 equality, or the abstract bound. Primary and corpus full-text access limitations remain.

## value

PASS

Adding a second noisy follower is a natural structural change to the same model with a previously sharp transport–dissipation frontier. The non-saturation classification rules out any many-follower recovery of the two-particle efficiency at finite nonzero coupling, not only near zero. Its exact coefficient isolates cross-follower interactions and quantifies their leading loss for unequal diffusivities. This answers a transport question not settled by the previously known entropy rate or by a formal non-strict bound. The normalization repair preserves that mathematical value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
