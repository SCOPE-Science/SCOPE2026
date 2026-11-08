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

# Reproduction and limitations

Run `python check.py` from this directory with Python, NumPy and SymPy. The captured output is in `checks.txt`. The script checks symbolic identities and evaluates 193,536 finite candidate/sampling combinations, including endpoints of the sampling simplex and many positive-definite rational parameter pairs. The proof's strict inequalities use exact algebra and convexity, not numerical sampling; the computation is neither exhaustive over real parameters nor an independent audit.

The exact domain is \(0<c\le d<1\), \(2c^2+d<1\); the minimax objective is the sharp conditional expected squared-\(H\)-norm retention after *one* exact two-coordinate minimization. No general multistep or adaptive-sampling optimality is established.
