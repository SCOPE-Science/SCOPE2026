---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-17.md",
      "INDEPENDENT_AUDIT_2026-11-17.json"
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

The 12 tetrahedral rotations form A4; the standard real rotation representation has character 3 on identity, -1 on three half-turns and 0 on eight order-three elements. Its matrix coefficients plus constants form 10D Wigner degree0+1 subspace, with full-group normalized Haar/counting isometry. The image projector has P_{gh}=(1+3chi(g^-1 h))/12, diagonal 5/6 and off diagonal -1/6 (half-turn) or 1/12 (3-cycle). Erasing two nodes gives I-R_E^*R_E, whose two nonunit eigenvalues are 1-(5/6±P_{gh}); these are 0,1/3 for half-turn and 1/12,1/4 for order three, with eight unit eigenvalues. Exactly 12*3/2=18 halfturn and 12*8/2=48 order-three unordered pairs; unit-weights fixed at 1/12. Independently enumerated all even permutations, verified exact rational projector idempotence on 12x12, all 66 classifications and spectra, plus one-erasure eigenvalue 1/6. The explicit delta-supported half-turn witness follows from the character difference and matches the continuous trace formula. Exact representation/projection proof covers every pair, with exhaustive finite computation as cross-check.

## originality

PASS

Gräf–Potts (2009) Section 4 explicitly gives the full 12-node tetrahedral rotation-group cubature, so that background is already covered. Scott/general finite-frame erasure and group representation identities are classical, but the inspected 2009 paper supplies no 10-of-12 erasure classification or sharp two-eigenvalue spectrum. Price–McEwen 2023 and McEwen et al. 2015 provide general Wigner transforms/other rotation sampling designs. Resultary prior icosahedral twelve-node Wigner spectra concern a different group and bandlimit. The complete half-turn/3-cycle classification is best-of-knowledge new, with a bounded residual risk from generic frame-erasure tables.

## value

PASS

A natural smallest-cardinality complete sampling problem: Wigner degree0+1 space dimension 10, tetrahedral cubature has exactly 12 fixed nodes. The 48 successful and 18 obstructed minimal 10-node subsets, optimal sqrt(12) stability and explicit invisible trace modes are meaningful complete missing-data classification, not mere restatement of known full 12-node isometry.

The dated certificate retains the supplied scientific assessment, sources and limitations.
