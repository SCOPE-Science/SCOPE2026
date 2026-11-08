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
Run `python3 verify_split.py` in the directory containing the extracted files, with standard Python 3 and no third-party dependencies. It enumerates 49 exact two-module tagged states, writes the entire `support_table.csv` table, independently obtains all nine support-size coefficient matrices, compares their surjection-weighted totals to the displayed symbolic formulas, and independently evolves every binary-size pair of 3-state graph assignments for \(1\le a,b\le6\), \(a+b\le10\), totaling 306,729 states. The captured execution result is `verify_split.out`. The exact 49-case table supplies finite evidence for the general theorem; labelled experiments alone are not an infinite proof. 

The proof of lifting from the certificate to arbitrary integers \(a\ge3\), \(b\ge2\) is the complete surjection/inclusion-exclusion identity in `RESULT.md`. The source and the certificate are self-contained. The general literature's qualitative convergence theorem is not claimed as newly established. No independent scientific audit or external certification has been performed.
