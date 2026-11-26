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

The identity follows from PQP=aP and QPQ=aQ: C²=−a(P−Q)², and (P−Q)²C=(1−a)C. If a is neither 0 nor 1, C cannot vanish (commutation would force a=a²) and the cubic prevents nilpotence. For an independent census, fix the image U and kernel W of P and choose the image line of Q first. If it equals U, the q^m choices contribute P and q^m−1 square-zero commutators. Each image line in W contributes q^(m−1) commuting choices and (q−1)q^(m−1) nonzero square-zero choices. The other image lines have unique representatives u+w with w≠0 and u a fixed generator of U. For each such line, a prescribed trace a imposes ψ(u)=a and ψ(w)=1−a on the projecting functional, giving q^(m−1) choices. Trace 0 gives square zero; at trace 1 the unique functional vanishing on W gives square zero and the other q^(m−1)−1 give index three; other traces give nonnilpotence. This recovers all four counts including q=2 and m=1. The index-three construction just requires two nonzero orthogonal vectors in W and so works over every field for m≥2. Inspected the finite-field verifier and its scope as frozen evidence; no frozen code was run.

## originality

FAIL

A distinct earlier indexed record gives the entire similarity-type census for the same ordered rank-one idempotent pairs. Coarsening its classes recovers all four counts exactly. Its proof's cubic identity and index-three construction use only field algebra, so making those statements explicit over arbitrary fields does not leave a distinct mathematical result.

## value

FAIL

An exact nilpotency-index census is a meaningful invariant in isolation, but this one only merges entries from an existing stronger census. Its arbitrary-field addendum is immediate from the same rank-one block identity and construction and does not supply a substantive surviving contribution. No repair is warranted.

The dated certificate retains the supplied scientific assessment, sources and limitations.
