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

# Reproducing the finite-field enumeration

Run `python3 verify_direct.py` and `python3 verify_pairlines.py` with Python 3. They require no nonstandard modules. The first enumerates all normalized rational points and lines over \(\mathbb F_5[t]/(t^3+t+1)\) and evaluates the homogeneous sextic directly. The second works over the independently defined irreducible cubic field \(\mathbb F_5[u]/(u^3+u+4)\) and constructs lines from pairs of curve points. Both contain assertions for the complete point spectrum and the uncovered count. The first checks every rational-line weight and double-counting constraints; the second checks the full six-secant configuration by a logically complete pair-generation argument.

The irreducibility of each cubic follows from having no root in \(\mathbb F_5\). A projective point or line is uniquely represented as \((1,x,y)\), \((0,1,y)\), or \((0,0,1)\); all \(15751\) representatives are enumerated, so no chart is omitted. All operations take place in exact modular integer arithmetic. There is no floating-point arithmetic, timeout-based exclusion, probabilistic sampling, or unstated dependency. An independent external audit has not been performed.
