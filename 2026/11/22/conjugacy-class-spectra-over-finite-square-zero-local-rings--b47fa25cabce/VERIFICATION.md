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

# Reproducibility and scope of verification

The theorem is proved in `RESULT.md` through reduction modulo the square-zero radical, field centralizer classification, exact disjoint counts of quadratic subalgebras, and orbit–stabilizer. The finite verification below is a consistency check, not an infinite proof or an external certification.

Run `python check_commuting.py` using a standard Python 3 interpreter with NumPy installed. The script implements ring addition and multiplication tables, builds the invertible two-by-two matrices by residue determinant, then checks each ordered matrix pair by full two-by-two products. It aggregates centralizers and compares the exact resulting histogram against the theorem's row formulas. This tests all pairs, not random samples, in each listed ring.

| Finite ring | Group size | Conjugacy classes | Ordered commuting pairs | Result |
|---|---:|---:|---:|---|
| \(\mathbb F_2[\varepsilon]/(\varepsilon^2)\) | 96 | 14 | 1344 | PASS |
| \(\mathbb F_2[u,v]/(u,v)^2\) | 1536 | 88 | 135168 | PASS |
| \(\mathbb F_3[\varepsilon]/(\varepsilon^2)\) | 3888 | 78 | 303264 | PASS |
| \(\mathbb Z/4\mathbb Z\) | 96 | 14 | 1344 | PASS |
| \((\mathbb Z/4\mathbb Z)[u]/(2u,u^2)\) | 1536 | 88 | 135168 | PASS |

The checker output, including the complete observed centralizer-size histograms, is preserved in `checker_output.txt`. In particular, the independent order-eight examples agree despite differing characteristics.

## Limitations
The script exhausts only the stated finite rings; it does not prove the formulas for all \(q,d\). The mathematical proof supplies the general quantifiers. Results for higher-degree matrices, nonsquare-zero radicals and singular matrices are not claimed. No independent mathematical audit has been performed.
