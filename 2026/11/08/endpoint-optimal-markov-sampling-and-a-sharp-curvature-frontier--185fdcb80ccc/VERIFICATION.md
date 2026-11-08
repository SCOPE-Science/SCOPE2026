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

From the containing package, run `python checks/verify.py` using Python 3 and SymPy. The script is standalone, invokes no network services, and reconstructs symbolic and exact-rational identities rather than reading external logs.

Checked: exact four-moment stationary fixed point; endpoint risk formulas; endpoint derivatives; the square decomposition controlling one derivative; the nonpositive-derivative factor in the opposite regime; 600 exact finite-path moment comparisons; and 306 rational parameter cases checking the stationary moments, fixed-point equations, and global endpoint comparisons. Each check completes with a PASS message.

Limits: rational samples are finite and cannot establish the optimizer theorem or originality. The infinite family is certified only by the analytic algebraic inequalities in the proof; no external independent audit has been carried out. Stationary mean-square error is not a claim of almost-sure convergence to the full objective's minimizer.
