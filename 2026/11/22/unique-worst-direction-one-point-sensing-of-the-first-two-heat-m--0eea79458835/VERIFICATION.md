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

# Verification and reproducibility

The included `verify.py` uses Python and SymPy. Run `python verify.py` after installing the dependency from `requirements.txt`. The recorded execution returned `PASS 20610 supplementary tests; u_short 0.30901699437494745 u_infinite 0.4256309996486727`.

The exact symbolic checks concern the asymptotic Gram determinant coefficient, short-horizon maximizer equation, and limiting cubic resultant. The finite numerical tests independently compare the direct smallest Gramian eigenvalue with its inverse formula on random spatial designs over ten observation horizons, and test strict logarithmic midpoint inequalities at sampled logit values. The full universal uniqueness and horizon limits depend on the analytic proof in `RESULT.md`, not on extrapolation from samples. Numerical optimization near zero horizon can experience cancellation; this checker uses horizons no shorter than `0.002` for finite trials, while the short-horizon limit is established symbolically.

No independent audit has been performed. The literature comparison is evidence-based but not a certification of publication priority.
