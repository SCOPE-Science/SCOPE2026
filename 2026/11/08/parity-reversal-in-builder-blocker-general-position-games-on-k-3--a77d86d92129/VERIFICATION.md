---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-12.md",
      "INDEPENDENT_AUDIT_2026-11-12.json"
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

For K3□Kn, pairwise distance≤2 makes a triple illegal exactly when the selected K_{3,n} edges contain a three-edge path. Legal states are bipartite star forests. All maximal states have 3,n,n+1 edges. Two-in-one-row play has high locks at a column pair plus third-row edge (n+1) and middle locks with three occupied distinct columns (n). Responding to off-row deviations and who moves at n−1 filled columns gives the parity outcome for each opening player. Independent exact minimax recurrence over all legal selected subsets for n=3,4,5,6 gives (4,3),(4,5),(6,5),(6,7) matching formulas; infinite proof is the exhaustive strategic case reasoning.

## originality

PASS

No comparable exact Builder-first and Blocker-first minimax values on K3 square Kn were found. The primary Builder–Blocker general-position game paper treats other graph families. Earlier general-position enumeration on rook graphs describes feasible and maximal sets but not adversarial move-order choice. The distinct parity-dependent strategic theorem is not implied by static extremal set sizes.

## value

PASS

Adversarial general-position games ask for forced terminal sizes rather than static extremal sizes. The natural narrow family K3□Kn has a complete parity-reversing optimal-play classification, with explicit high and middle locking strategies, a structural behavioral distinction not mechanically inferable from known maximal-set cardinalities.

The dated certificate retains the supplied scientific assessment, sources and limitations.
