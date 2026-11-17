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

# Verification

Execute `python3 CHECK.py` from the same directory as the bundled script. No external packages or source files are required. The script constructs the full five-by-five Frobenius–Perron matrix, uses exact rational arithmetic to verify the invariant density, 1,001 all-time total-variation identities for eleven time indices across ninety-one admissible geometries, and checks the geometric two-state reduction. Floating-point comparisons independently test the KL entropy identity at ninety geometries, three constant-slope maximal-entropy instances, and four prescribed spectral moduli. The expected and obtained output is:

`VERIFY_OK exact_transfer_cases=91 exact_tv=1001 entropy_KL_cases=90 parry_equality=3 tunable_rates=4`

All infinite statements are proved in `RESULT.md`; sampling does not certify convergence for arbitrary real cut positions. No independent audit has been performed.
