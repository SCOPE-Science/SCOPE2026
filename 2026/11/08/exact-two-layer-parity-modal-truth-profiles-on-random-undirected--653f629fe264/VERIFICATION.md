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

An alternating-matrix basis-completion argument with S=[1,d] shows the precise graph count 2^{binom(n-2,2)} for d in even hyperplane excluding 0 and 1, and t even orthogonal to d. The zero and all-one exceptional trajectories follow from A1=d. Summing gives the marginal law. Independently enumerated all edge masks and all labelled state pairs for n=2..6, including n=2. Universal proof does not rely on finite enumeration.

## originality

PASS

No inspected Resultary or primary theorem states the dependent joint law of (A1,A^2 1) for a single random alternating adjacency matrix. Janzer–Yip Lemma 3.4 already gives the uniform even first state, which is credited. Symmetric-matrix completion is a standard tool, not claimed novel by itself.

## value

PASS

A natural complete finite-model law for two synchronous GF(2) neighborhood iterations, at the first time the observed predicate depends on the same adjacency used for the next aggregation. Exact exceptional atoms and orthogonality constraint matter for parity-modal finite-model semantics and cannot be replaced by independent-layer approximations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
