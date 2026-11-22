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

# Reproducible finite checks

Run `python3 verify_fifth.py` with Python 3. No external libraries or data are required. The script enumerates all inputs modulo \(5^k\) for every \(1\le k\le8\), constructs the proposed output multiplicities independently using direct quadratic root enumeration, and asserts exact equality of the complete fiber dictionaries. It also asserts the closed image-count formulas and that total multiplicity equals the input modulus.

Executed output: image counts \(1,3,7,31,147,731,3647,18231\); eight successful complete-fiber checks and 488,280 input evaluations. The proof in `RESULT.md` establishes the claim for all higher powers; finite checks cannot establish that universal quantifier. Full-text comparison to the 1991 Dickson/Galois-ring paper remains outstanding; only the abstract was accessible.
