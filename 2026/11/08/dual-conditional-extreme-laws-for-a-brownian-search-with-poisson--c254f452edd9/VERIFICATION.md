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

# Verification and reproduction

The proof uses killed Brownian boundary-value equations with \(Df''=rf\), an independent-cycle decomposition, exact finite geometric sums, and explicitly displayed asymptotic expansions. It does not rely on an exhaustive numerical enumeration or a computer-assisted infinite proof.

Run `python3 check_current.py` using the Python standard library. The checker evaluates one-cycle normalization, truncated-geometric summation formulas with the finite remainder retained, conditional probabilities, high-maximum count selection, and Gumbel/low-rate asymptotic diagnostics on specified parameter grids. It prints a single PASS line on success, or exits unsuccessfully on an assertion failure.

The limiting assertions are verified in the written proof. Finite checks only provide reproducibility and numerical consistency evidence. No external or independent verification has been performed.
