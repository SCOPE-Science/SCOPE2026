---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-11.md",
      "INDEPENDENT_AUDIT_2026-11-11.json"
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

PASS: With r+1 colours on r nonempty pairwise-complete parts, any proper final colouring either has r monochromatic parts or one uniquely bichromatic fully seeded part. The missing-colour rule cannot start from any incomplete monochromatic pattern. In a split pattern, every vertex of the split part must be seeded, and at most one monochromatic part may have zero seeds; the converse follows by the unique forced first action. Counting (r+1)!/2 allocations, (2^{n_j}-2) surjective split assignments, and seeded-subset factors A_i proves the entire polynomial and its probability substitution. Minimum seed n_j+r-2 and multiplicity follow directly. Independent definitional brute force for K_{2,2,2}, four colours, gave coefficients 288,432,288,96 for domains 3..6; this is finite corroboration only.

## originality

FAIL

FAIL: The complete 2026-10-13 theorem "One spare color forces a unique split part in complete multipartite graphs" states the same if-and-only-if classification, identical domain polynomial, probability polynomial, minimum seed, and multiplicity for the identical r>=3, n_i>=1, r+1 palette. It is earlier published exact mathematical coverage; no surviving independent final claim.

## value

PASS

PASS as an exact structural enumeration for a natural first-surplus forced-colouring problem, with a meaningful sharp minimum-domain threshold and full polynomial. It is useful mathematics but already published, so value does not rescue originality.

The dated certificate retains the supplied scientific assessment, sources and limitations.
