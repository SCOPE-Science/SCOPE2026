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

# Reproducibility

Run `python3 verify_base.py` and `python3 verify_extensions.py` with Python 3 in the directory containing the included programs. Their deterministic terminal output should match `verify_base.out` and `verify_extensions.out` byte-for-byte, respectively.

`verify_base.py` independently constructs regular paperfolding bits from the odd-part definition and exhausts all starting positions of every shorter factor for \(k=6,7,8\). It checks the parity separation of all length-seven factors and the complete length-sixteen multiplicity histogram \((3:16,4:47,5:1)\) in the order-eight prefix.

`verify_extensions.py` constructs bits by the independent recurrence \(x_{2j}=1-(j\bmod2)\), \(x_{2j+1}=x_j\), and uses sorted suffixes with adjacent longest-common-prefix comparisons. It verifies the exact global shortest unique length and both starts for \(8\le k\le12\), including the predicted suffix multiplicity at one below the threshold.

**Limits:** The programs independently establish the finite base-case assertions and check additional instances. They do not certify the all-length theorem by computation; Lemmas 1–3 and the simultaneous (A)/(B) induction in `RESULT.md` establish the infinite claim. No external independent validation has been performed.
