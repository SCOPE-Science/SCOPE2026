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

# Verification summary

Execute `python3 checker.py` in the extracted package directory. The exact checker uses only Python's standard library, directly computes \(\binom{4n}{n}\pmod3\) for \(0\leq n<2600\), and verifies the signed digit rule without using a Lucas-digit binomial computation as its independent reference. It also checks exact three-residue counts on \(0\leq n<3^L\) for all \(0\leq L\leq7\), the two cubic integer-matrix identities, and their recurrences through the first fourteen levels. Its actual execution output began `VERIFY_OK levels=8 direct_indices=2600 matrix_charpolys=2 rational_recurrences=28`.

The analytic proof additionally needs (i) the Kummer no-carry criterion, (ii) Lucas's digitwise congruence, (iii) the explicitly displayed symmetric matrices and their real spectra, and (iv) ternary digit-cylinder decomposition for every cutoff. The finite checker tests but does not replace these arguments. The unsigned support is established in prior literature and is not presented as new. No independent audit has been carried out.
