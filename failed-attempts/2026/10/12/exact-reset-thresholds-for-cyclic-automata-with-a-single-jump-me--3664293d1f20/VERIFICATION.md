---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

Modulo gcd(n,h), b is the identity and a is a common translation, so distinct residue classes cannot merge. When coprime, the +h cyclic order makes 0 the predecessor of h. For any proper nonempty interval, inverse b adds 0 at the left only if the old left endpoint is h, deletes only a right endpoint if it shrinks, and otherwise leaves the interval fixed. Empty preimages cannot subsequently become full; after the first full preimage it remains full, so use only the prefix of the reverse scan through first attainment. Each of the at least n-1 growth steps adds one point; between two such steps the left endpoint must move from 0 to h by decrements of one and non-growing b steps cannot help. The n-2 gaps thus cost at least n-h rotations each. Starting from {h}, inverse b gives {0,h}; shifting by h via inverse a^(n-h) and applying inverse b extends the successive intervals through all of Q. The bound and word coincide, including n=2, with no rotations between growth steps.

## originality

FAIL

A distinct Resultary record proves the identical all-parameter directed unit-cost formula and word, and also proves literal uniqueness. This is demonstrable coverage, not an attribution or precedence decision based on catalogue dates. The prior classical h=1 case and the papers giving a criterion or upper witness alone would not suffice for this conclusion.

## value

FAIL

An exact directed threshold across linear and quadratic regimes is mathematically useful. The audited finding does not add a new invariant or independently stated structural theorem beyond the distinct published exact result, which even identifies the unique shortest word. A different proof of the threshold in this record does not establish a further scientific claim of the proposed scope.

The dated certificate retains the supplied scientific assessment, sources and limitations.
