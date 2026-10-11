---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-06.md",
      "INDEPENDENT_AUDIT_2026-10-06.json"
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

Writing \(N=qM+r\), the sparse weighted sum differs from the first \(M\) weighted iterates of \(f^q\) by at most one bounded term, while replacing \(N\) by \(qM\) creates an \(o(1)\) normalized error. This proves the exact factor-\(1/q\) limsup identity and the identical statement for mean absolute weight, hence preservation of nontriviality and equality of correlated-point sets. The full-entropy conclusion then follows from the standard Bowen subset-entropy power law \(h_{\rm top}(f^q,Y)=q h_{\rm top}(f,Y)\).

## originality

PASS

The defining recent paper uses the same correlated-set notation and records the Bowen entropy power law, including cyclic-decomposition applications, but the inspected full text does not state the exact sparse-weight identity or a general permanence theorem saying that arbitrary Bohr chaotic systems pass the property to every positive iterate. Current Resultary search returned the assigned statement as the exact hit and no stronger published transfer theorem. Best-of-knowledge originality therefore survives, with the elementary nature of the observation treated separately under value.

## value

FAIL

The entire transfer law is a bounded-error reindexing of the defining weighted average, and the entropy consequence is immediate after applying the standard power law. It introduces no new dynamical mechanism, boundary phenomenon, difficult invariant, or nontrivial classification; under the common value standard it is a routine consequence of the definitions rather than an independently worthwhile mathematical gap.

The dated certificate retains the supplied scientific assessment, sources and limitations.
