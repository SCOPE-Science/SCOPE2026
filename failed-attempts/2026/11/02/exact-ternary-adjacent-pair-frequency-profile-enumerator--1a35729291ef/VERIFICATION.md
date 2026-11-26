---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

The directed Euler-trail criterion is necessary and sufficient for nonempty support; on adjoining an arc from end to start, the balanced weakly connected multigraph admits an Euler circuit. The loop-only and two-vertex terms exclude detached loops. All-three-active off-diagonal support is connected on three vertices. Cycle net flows are (k,k,k) at balance and (k,k−1,k−1) for one ordered endpoint pair; arbitrary antiparallel pairs give the factors (1−z²)^(-3). The subtraction of two-vertex and zero supports and the sixfold endpoint multiplier are correct. Independently cleared the denominators to verify the full rational identity, checked the pole coefficient 7/12 at z=1, and enumerated the reachable (profile, last symbol) pairs by single-symbol extension through n=20. This gives the advertised coefficients including the single zero-profile at n=1 and also A_20=125607. Replay: `python3 /workspace/branches/frozen_replay.py 2`.

## originality

FAIL

A distinct matching Resultary record indexed on the same UTC date gives the very same endpoint-free ternary linear count for every positive number of transitions and explicitly states the same singleton case. Its displayed series differs from the frozen series by exactly 1, as confirmed by polynomial subtraction. This is verified equivalent coverage, not a directional priority judgment. An additional, later-dated entry states the same full series directly. The leading asymptotic also follows from earlier published work independently of the catalog match.

## value

FAIL

Exact finite-length counts of linear Markov types are a meaningful refinement of an asymptotic estimate, but the indexed overlap already supplies this precise refinement, the empty-profile case, and the noiseless-capacity interpretation. The alternative organization by active support does not yield a distinct mathematical consequence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
