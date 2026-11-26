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

Every selected vertex that is isolated in the selected subgraph can be mapped to its rung mate, and every nonisolated selected vertex to an external private neighbor. Neither assignments of the same kind nor mixed assignments can coincide, so |D|≤n; an entire row attains this. At size n, full and empty columns are equinumerous. Only empty columns can supply external private neighbors to full columns, and each empty vertex must be used, which forbids neighboring singleton columns. Full columns cannot touch singleton columns either, since the latter would then have no private neighbor. With only singletons, a selected interior vertex loses its private neighbor exactly when one adjacent column selects its row and the other the opposite row; period two is necessary and sufficient, including the vacuous constraint at n=2. With only full and empty columns every column meets exactly one unlike neighbor, so these edges are the unique perfect matching of the even column path. This gives exactly the stated words. The two checkerboards are the only independent words, and complementing pairs the extremizers.

## originality

FAIL

A distinct indexed Resultary record, --ee60eed8ab77, states the identical upper-domination number, classification by the same six words with the same parity restriction, and exact census for the same labelled open ladder. The direct private-neighbor proof differs from the matched finite-state proof, but the scientific classification and both stated corollaries are covered. This conclusion rests on the statement comparison, not on catalogue chronology alone.

## value

PASS

The structural equality question is natural independently of its originality: the scalar domination number alone does not describe the maximal layer, and the proof explains why the even-only sets arise from the open path’s perfect matching. The classification is substantive, although this record adds no distinct classification beyond the exact match.

The dated certificate retains the supplied scientific assessment, sources and limitations.
