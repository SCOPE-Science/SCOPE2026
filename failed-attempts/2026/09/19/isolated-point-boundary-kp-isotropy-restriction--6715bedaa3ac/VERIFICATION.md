---
{
  "schema_version": 1,
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-01.md",
      "INDEPENDENT_AUDIT_2026-10-01.json"
    ]
  },
  "lean_verification": {
    "status": "unknown",
    "evidence": null
  },
  "expert_attestation": {
    "status": "unknown",
    "evidence": null
  }
}
---

# Independent mathematical audit

## correctness

PASS

The isolated-point criterion is correct: a singleton Steinberg characteristic function is locally constant only when the arrow singleton is open, etaleness sends this to an open unit singleton, and an isolated unit cuts compact-open bisections down to singleton isotropy arrows. The corner and source-fiber identifications follow from support. The finite-dimensional graded obstruction is also correct: a nonzero periodicity element gives a homogeneous invertible corner element of nonzero degree, so any nonzero homogeneous vector generates nonzero vectors in infinitely many distinct grades.

## originality

FAIL

Two earlier 2026-09-18 SCOPE records were inspected from their actual Git blobs and already prove the exact isolated-unit point-mass criterion, the one-vertex/two-loop counterexample to arXiv:2609.20230v1, and the corner/source-fiber repair. One of them states the equivalence 1_{gamma} in A_R(G) iff {x} is open for an arbitrary Hausdorff ample groupoid. Thus the headline theorem and source correction are directly covered before this 2026-09-19 record. The additional finite-dimensional graded periodicity lemma was not found in those earlier records, but it does not make the unchanged final package original as a whole under the requested one-final-claim bar.

## value

PASS

As mathematics, the isolated-point boundary is a useful foundational correction to a representation-theoretic construction, and the finite-dimensional graded periodicity obstruction is a clean structural consequence relevant to the source paper. Value survives even though originality of the unchanged package does not.

The dated certificate retains the supplied scientific assessment, sources and limitations.
