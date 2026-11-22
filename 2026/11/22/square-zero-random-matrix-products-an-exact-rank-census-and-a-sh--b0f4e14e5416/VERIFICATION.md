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
The included `verify_squarezero_product.py` is executable with Python 3 using only the standard library. Run `python3 verify_squarezero_product.py`. It exhaustively computes the product \(AB\), tests \((AB)^2=0\), and independently calculates ranks \(\operatorname{rank}A\) and \(\operatorname{rank}(ABA)\) for small prime fields. The exact Gaussian-binomial formula is evaluated separately using an integer Pascal recurrence. See `verification_output.txt` for captured output and the `VERIFY_OK` marker.

The finite checks do not establish the infinite-dimensional asymptotic or cover extension fields; those conclusions follow from the full symbolic proof using Gaussian-binomial inequalities and a convergent translated theta bound. No independent mathematical audit was performed.
