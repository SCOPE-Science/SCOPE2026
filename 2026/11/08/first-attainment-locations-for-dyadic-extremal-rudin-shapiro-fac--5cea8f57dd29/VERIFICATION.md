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

# Reproducibility and verified scope

Run `python3 verify.py` in the extracted artifact directory. This standalone checker computes the signs directly from the parity of adjacent `11` occurrences in each nonnegative integer. It compares all contiguous length-\(2^k\) sums over starts \(0\) through \(12\cdot2^k\), identifies the exact first maximum and minimum and compares them to the four displayed formulas for every \(2\le k\le16\). The furthest predicted first minimum is before \(12\cdot2^k\), so each claimed earliest witness is inside the finite search interval. It also checks the full signed canonical blocks, sums, prefix maxima, and least maximizing prefix indices for \(k\le16\).

Observed output: `PASS: recursive prefix-extremum certificates and 15 complete finite scans`. These exhaustive **finite** checks do not prove the infinitely quantified statement. The proof in RESULT.md instead verifies the exact block recursion, closed prefix extrema and first-attainment indices, strict bounds for the two possible block orders, and the first eligible signed adjacent-block pairs. No independent audit has been performed.
