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

# Reproducibility and scientific limits

Execute `python3 CHECK.py` from the extracted artifact directory. The self-contained script requires the Python 3 standard library. It checks all 3969 pairs of nonempty row/column subsets of the order-six Fourier matrix and all 1089 pairs of four-element affine row/column orbits of the order-21 Fourier matrix. It compares exact modular ranks against the subgroup-coset prediction. At order 21 the orbit sizes recover all 35,820,225 ordered row/column pairs and the rank-two count 66150; the counts at ranks three and four are auxiliary verifier diagnostics, not claimed as a universal theorem.

Primes and primitive roots are reverified by the script. The proof that finite-field ranks equal complex ranks uses cyclotomic integrality and the explicit absolute norm ceiling \((k!)^{\varphi(N)}\), plus the two distinct chosen prime factors of a hypothetical vanishing norm. No numerical singular-value threshold or floating-point rank is used. The universal analytic statement and the all-prime semiprime formula follow from the proof in RESULT.md, not from finite checks.

For this new mathematical argument, only a self-review has been performed; independent audit and independent validation remain unperformed. The strongest priority risk is possible coverage in historical full text or an unindexed statement.
