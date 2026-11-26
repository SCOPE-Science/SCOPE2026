---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
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

The three monochromatic output loads sum to at most 12, and every length-n word for n≥4 contributes at least once. Size 12 would require exactly the twelve one-heavy vectors U, which overload every mixed pair. In a size-11 code at least ten vectors must be one-heavy. With eleven, the omitted vector must hit all three mixed pairs, so is a B_i. With ten, the remaining word has two heavy labels i,j and monochromatic saturation forces exactly one omission at each. Both omissions must hit ij; they therefore lie in {A_i^j,B_i}×{A_j^i,B_j}. When the third coordinate is zero, one omitted B suffices to repair both remaining mixed loads and is necessary. When it is one, both B's must be removed. Every such choice meets all six loads. These families are disjoint and the added word and missing members are determined by the codebook, so the labeled count is 3+3[3(n−3)+(n−4)]=12n−36, with zero interior choices at n=4. Separately, /workspace/reproduction/check_5.py uses exact load-vector dynamic programming over the full simplex, making no one-heavy restriction; it confirms capacity 11 and counts 12 through 108 in increments of 12 for n=4–12 (check_5.out). The all-length proof is by incidences, not extrapolation.

## originality

PASS

The capacity eleven is prior background, explicitly not claimed as new. The supported distinct claim is the full two-family characterization and labeled optimizer count at L=4 for every n≥4. Available primary passages and the strongest catalogue comparisons do not establish this equality census. The earlier capacity source cited indirectly remains unidentified.

## value

PASS

At the natural small list allowance just below the higher-list regime, the exact equality structures show why an extremizer need not have the large-list one-heavy saturation pattern. The distinction between deleting one one-heavy vector and adding a two-heavy vector after two forced omissions determines all optimal codebooks, their finite-length boundary and their exact multiplicity. This is useful structural information beyond an already known capacity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
