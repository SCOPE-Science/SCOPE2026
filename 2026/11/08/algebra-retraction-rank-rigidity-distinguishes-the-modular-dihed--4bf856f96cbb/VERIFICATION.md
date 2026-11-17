---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-10.md",
      "INDEPENDENT_AUDIT_2026-11-10.json"
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

Characteristic-two group algebra of a finite 2-group is local with cotangent space dim 2. Explicit group-basis multiplication gives the square-zero radical cone: Q8 exactly the four-dimensional central cA ideal, D8 union of two five-dimensional spaces meeting in cA. A nontrivial proper algebra retract has cotangent dimension one; the group relations force its generators to be square-zero, excluding Q8 because cA lies in J^2. For D8 each normalized nonzero tangent direction has q^4 square-zero representatives and q choices of splitting, giving 2q^5 maps of vector rank two; rank one augmentation and rank eight identity. Independently implemented GF2 exhaustive generator-image/evaluation test confirms D8 (1,64,1) and Q8 (1,1), and GF4 exhaustive augmentation-ideal square-zero census confirms D8 central/noncentral (256,1536), Q8 (256,0). Characteristic-two arbitrary-field proof is algebraic, not inferred from the finite tests.

## originality

PASS

Best-of-knowledge distinct exact embedded-retract and idempotent-endomorphism rank distributions in D8 and Q8 modular group algebras. Closest earlier result concerns regular multiplication ranks/square-zero cones, and 2021 group-algebra comparison has no accessible confirmation of this precise count. Prior ring-theoretic structural fact alone does not give 2q^5 without analyzing cotangent images and retraction splittings.

## value

PASS

An explicit complete rank spectrum and embedding/splitting census for algebra retracts is a natural structural invariant distinguishing notoriously similar modular group algebras. The q-dependence and strict Q8 rigidity go beyond a relabeling or a few experimental values.

The dated certificate retains the supplied scientific assessment, sources and limitations.
