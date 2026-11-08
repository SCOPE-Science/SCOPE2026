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

# Verification record

Run `python3 verify_ternary_fuss_3adic.py` using Python 3 and the standard library. This self-contained script obtains each \(\nu_3(C_n)\) separately using Legendre's factorial valuation sums, compares it with the digit-reduction formula, reconstructs every coefficient of \(P_r(t)\) using the second-order recurrence, and checks equality for all \(0\le n<3^r\) and all \(0\le r\le9\). It separately calculates 150 exact binomial numbers and checks the precise mean and variance identities with rational arithmetic. The expected terminal output begins `VERIFY_OK levels=0..9 individual_index_checks=29524 direct_large_binomials=150 recurrence=PASS digit_formula=PASS exact_mean_variance=PASS`.

The source code and its assertions are directly inspectable, and the script was executed successfully on the embedded, final source bytes. This is finite corroboration: it cannot establish the general identity for every \(r\). The unrestricted proof appears in `RESULT.md`. No independent mathematical audit or external formal certification was conducted.
