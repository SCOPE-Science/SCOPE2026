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

The unique a^n factor defines exactly one run of length n for each symbol a. Deleting a there destroys that factor, whereas deleting a in another run preserves it and cannot join two a-runs. Root both latter outputs at the preserved factor: equality of the resulting linear strings forces all source letters between the deleted indices to agree. Different deleted symbols are distinguished by letter counts. Thus the mass of each descendant is its source run length divided by q^n. For lengths at most n−2, count bounded runs via the q^(n−ℓ−2) extensions of each factor b a^ℓ c with b,c ≠ a. For ℓ=n−1 there are q occurrences of a^(n−1), exactly two in the length-n run. This covers n=2 and the zero multiplicity for binary runs of length n−1. The total number also agrees with the count of unequal consecutive letters, (q−1)q^(n−1). The supplied verifier and log were inspected, not executed; their finite results are corroboration only.

## originality

FAIL

A distinct, same-day indexed theorem directly covers the run-bijection in the identical rotation-only convention. The probability spectrum follows mechanically from that bijection and the de Bruijn factor frequencies; it need not be printed in the broader record. This establishes coverage, not a priority order between the records.

## value

FAIL

Knowing the complete likelihood histogram for a fixed cyclic deletion source is mathematically natural, and the symbol-anchor proof is concise. As a separate finding, however, the histogram is mechanically implied by the broader run-bijection and elementary factor counts. No distinct useful invariant or nonroutine extension remains in the frozen claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
