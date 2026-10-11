---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
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

Thresholding the attained distances of an injective tuple gives a strict partition chain from the discrete to indiscrete partition, and every such chain defines an ultrametric by first-merge level. dc-homogeneity identifies tuple orbits with these finite order types. Thus injective orbit count is the classical ultradissimilarity/partition-chain number \(a_n\). Allowing repetitions first chooses an equality partition, giving the Stirling transform, and Lengyel's recurrence immediately yields \(b_n=2a_n\). The verifier checks the finite combinatorics.

## originality

FAIL

Bartoš et al. already prove that all finite two-sorted ultrametric spaces form the Fraïssé age of the dc-homogeneous limit. OEIS A005121 already identifies ultradissimilarity relations with partition-lattice chains and records the Lengyel recurrence. In a homogeneous relational structure, labeled tuple orbits are exactly finite labeled age types. Therefore the injective count is a direct translation of the prior framework and classical enumeration, while the all-tuple factor-two law is a routine equality-partition Stirling transform plus the published recurrence.

## value

FAIL

The result is a clean cross-language identification, but the injective count is immediate from homogeneity plus the classical partition-chain encoding, and the repeated-tuple formula is a routine Stirling transform whose factor two is the classical recurrence. This is expository packaging rather than an independently substantive theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
