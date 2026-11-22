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

The calculation assumes \(0<a<b\), \(L_0>0\), \(\Delta>0\), and one capped additive impulse. `CHECK.py` uses only Python's standard library and tests the explicit single-aerator peak, the optimal balancing site, the exact benchmark \((a,b,L_0)=(1,2,1)\), 150 deterministic parameter instances, 45,000 alternative candidate sites, and the leading weak-dose expansion. Run `python3 CHECK.py` from the same directory. A successful replay produced `PASS 48022 diagnostic assertions`.

Numerical comparisons are not a substitute for the proof of unique global minimax placement. That proof follows from monotonicity of upstream risk and post-intervention peak, comparison with sites at or after the unassisted sag, and an explicit crossing. The dose transition is algebraic, and the weak-dose displacement is asymptotic via the pristine sag's nonzero negative second derivative. No external-data fitting or independent audit is represented.
