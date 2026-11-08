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
# Verification and reproducibility

Execute `python3 artifacts/verify.py` with Python 3 and no third-party modules. The script computes complete Fibonacci residue cycles, exact rational probabilities, direct subset counts, and integer dynamic-programming counts of nonadjacent summands. It tests the four displayed Zeckendorf–Niven constants, seven weight-modulus configurations, 35 residue-specific coefficient triples, 105 cutoff comparisons, and 21 independent small-cutoff subset censuses.

**Mathematical scope:** The finite program cannot prove the unrestricted two-term asymptotic; the proof in `RESULT.md` establishes it by counting all first-order forbidden index pairs and bounding their intersections. The cutoff-dependent \(O(L^{k-2})\) constant is not computed explicitly by the verifier. The script does not claim any external certification or historical-priority determination.
