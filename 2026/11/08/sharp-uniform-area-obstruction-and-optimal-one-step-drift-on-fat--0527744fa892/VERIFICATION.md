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

# Reproducibility and scientific limits

The analytic identities to check are (i) the three inverse images \((w+q_i)/\beta\); (ii) the admissibility criterion \(w+q_i-q_j\in\Delta_\beta\); (iii) the seven open regions for \(\beta=\sqrt2\) and their total inverse-selection weights; and (iv) the exact ratio \((2-\sqrt2)^2/[2(1+\sqrt2)^2]=17-12\sqrt2\). They are derived in RESULT.md, rather than inferred from numerical output.

Run `python3 verify_density.py` in a Python environment with the standard library. The code checks interior points for seven expansion parameters, three independent coin choices, and a high-precision radical identity; its observed clean run comprises 105858 finite comparisons. Decimal arithmetic is used to avoid boundary ambiguities and is not an interval proof of general identities. The geometric partition and exact algebra establish the general theorem. No external independent mathematical audit has been performed.
