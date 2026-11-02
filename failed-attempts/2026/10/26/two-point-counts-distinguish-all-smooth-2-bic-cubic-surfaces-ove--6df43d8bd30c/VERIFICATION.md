---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-29.md",
      "INDEPENDENT_AUDIT_2026-10-29.json"
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

Every geometrically smooth 2-bic cubic F_A=Σa_ij X_i²X_j over F2 has invertible A: gradient is A^T X^[2] and Euler identity identifies nonzero kernel vector with geometric singularity. Anticanonical embedding makes F2-isomorphism projectively linear, so classification is GL4(F2) matrix congruence A↦G^T A G (order 20160). Independently enumerated all 65536 binary 4×4 matrices, exactly 20160 invertible; under 12 elementary transvections obtained ten disjoint orbits with sizes (420,3360,5040,1120,1120,4032,420,1260,3360,28), summing to 20160; separately computed every representative’s F2 and F4 projective point count using explicit F4 multiplication, obtaining ten distinct ordered signatures ((7,45),(7,21),(7,29),(3,21),(9,33),(5,25),(3,29),(11,29),(9,17),(15,45)). N1 alone repeats. This is exhaustive of the stated finite domain, not an extrapolation to general fields or cubics.

## originality

FAIL

FAIL due to substantive published PRIOR COVERAGE, not inaccessible literature: Karaoğlu (2021) publishes the full isomorphism-class classification of all cubic surfaces over F2 (including this ten-class smooth 2-bic subfamily) and expressly links a comprehensive per-class online atlas of point lists over each F_{2^k} for k≤6. The actual accompanying publicly indexed DicksonSurfaces dataset contains reports Orb<i>_q2.pdf and Orb<i>_q4.pdf for every prior class and maps F_i to Orbit_i. Hence each class’s (N1,N2) is already a deterministic existing-table/database lookup. Restriction to 2-bic subset and observation that ten existing ordered pairs differ is an immediate finite table implication; wording need not match. Prior article Section6 was read in full context. Some individual binary PDF reports could not be downloaded, but publication of all point lists and class identifiers is explicit, and the new arithmetic counts were independently checked; no insufficiency-of-evidence shortcut.

## value

FAIL

FAIL under the same scientific-value standard because the main exact numerical signatures and complete class identities were already supplied by the published full 141-class atlas. Recognizing that these ten published pairs are distinct is a straightforward comparison of a known table, not a new structural lemma, missing classification, or unknown natural invariant; correctness and reproducibility do not by themselves establish new value. Rejection is because of existing-table recomputation, not because the problem is finite or lacks a downstream theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
