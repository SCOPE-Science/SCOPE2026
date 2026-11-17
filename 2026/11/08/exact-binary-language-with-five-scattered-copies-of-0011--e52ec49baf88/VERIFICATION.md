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

Letters before the second zero (ones) and after the penultimate one (zeros) are inactive; removal leaves a word beginning 00 and ending 11, every letter active. A monotonically sorted core has C(a,2)C(b,2), never five. An inversion forces 001011 as subsequence with precisely five embeddings; any extra active position contributes a sixth. Reconstruction gives four uniquely located freely insertable inactive zones and stars-and-bars. Independent direct subsequence recurrence versus regular parser checked all lengths 0–16, not extrapolation; the proof covers arbitrary finite lengths.

## originality

PASS

Prior generic enumerators imply eventual polynomiality and offer a primitive-word algorithm, but the inspected source does not evaluate the exact exceptional (0011,5) language. Bruda already explicitly identified that case as exceptional for maximal-degree criteria; claim only unique core, unambiguous whole regular language, exact all-length binomial formula.

## value

PASS

The exceptional (0011,5) multiplicity instance is singled out by existing enumerative work; an exact unambiguous regular language and all-length count resolves a concrete open-looking special case and can serve as benchmark for primitive-core algorithms, without claiming general pattern enumeration.

The dated certificate retains the supplied scientific assessment, sources and limitations.
