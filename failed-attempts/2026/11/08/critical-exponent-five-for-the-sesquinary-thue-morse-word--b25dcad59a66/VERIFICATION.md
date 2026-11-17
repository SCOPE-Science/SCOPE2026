---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

Dekking digit recurrence gives x triples (y_n,1-y_n,y_n) and even-index y triples (y_2n,y_2n,1-y_(2n+1)). The y word has no four alternating or six identical consecutive letters. Any period p not divisible by 3 makes a 5p+1 repeated factor of y constant or of x alternating, contradicting the local obstructions. For p=3q, monotone surjective desubstitution F(j)=2floor(j/3)+1_(j mod3=2) converts the full 5p+1 repeated factor of y to period 2q with sufficient length, a strict period descent; x period divisible by 3 reduces to y. The factor x[18:33]=(101)^5 exists by the recurrence. Independent digit-extraction comparison of 12,000 indices and searches for p=1..44 confirm boundaries, but universal bound is proof-based.

## originality

FAIL

Decisive exact prior published on 2026-11-02 proves the same word, same digit recurrence, same theorem "no factor of length 5p+1 has period p for any p>=1", and the identical length-15 witness (101)^5 at index 18. Full published RESULT.md read, including proof and all assumptions. The newer submitted argument uses a different descent description but has no new substantive conclusion; this is strictly covered, not a priority ambiguity.

## value

FAIL

The critical exponent 5 is an important, natural conjecture and theorem in itself, but the identical complete statement was already proved and published November 2. Another presentation of the same theorem, without a distinct new classification, cannot be accepted as an original contribution; correctness and independent finite checks are not value sufficient.

The dated certificate retains the supplied scientific assessment, sources and limitations.
