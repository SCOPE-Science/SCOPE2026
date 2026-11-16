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

# Computational verification

Run `python3 checks/verify.py` with Python 3 and NumPy. The script constructs every set partition as a restricted-growth word and tests the noncrossing property using its forbidden alternating-pair definition. It creates the co-block edge bitmask, independently calculates the exact integer Walsh transform in the dimensions where complete enumeration is feasible, and compares it with the formula in the theorem.

**Actual checks completed:** all 2,131,018 Walsh coefficients for orders two through seven; all chord-constraint pair counts at orders two through ten; 200 direct signed sums each for orders eight, nine, ten; and binary Catalan parity/critical-distance checks for all dimensions two through five hundred. The output in `checks/verification_output.txt` was obtained by running the included source, not transcribed from unrelated runs.

**Limits:** Tests at orders eight through ten sample frequencies rather than exhaust them. No finite test proves the universal theorem. The all-order argument uses the character expansion, the exact chord-splitting bijection, the known Catalan valuation formula, and a parity count of Boolean frequencies. Independent mathematical validation has not been performed.
