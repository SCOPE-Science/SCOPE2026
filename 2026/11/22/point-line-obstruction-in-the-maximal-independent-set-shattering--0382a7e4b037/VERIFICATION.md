---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Reproducibility and scope
Run `python3 verify_heawood.py` using Python 3.10 or later, with no third-party packages required. Expected output begins `HEAWOOD_MIS_SHATTER_PASS` and reports the counts 37 concepts, 16,384 supports, face coefficients 1, 14, 70, 154, 77 and facet-orbit sizes 14, 21, 56.

The verifier constructs the seven Fano lines independently from the nonzero binary vectors in three coordinates. It enumerates all 16,384 vertex subsets, tests independence and domination, and confirms that precisely 37 sets are the geometric families in the proof. It checks all query supports against the trace definition, verifies the exact geometric classification, and constructs the full automorphism group from all Fano point collineations and a point-line polarity. It then confirms all facet sizes and orbits. This is a complete finite check for the specified graph, not an infinite proof or independent external certification.

The mathematical proof and the trace witnesses appear in `RESULT.md`. No human or independent mathematical audit has been performed.
