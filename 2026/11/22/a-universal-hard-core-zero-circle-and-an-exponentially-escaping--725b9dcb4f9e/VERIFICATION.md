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

# Reproducibility and verification

`verify.py` is a self-contained Python 3 program requiring SymPy. Its `polynomial_from_graph` function independently enumerates independent vertex sets on the explicit \(2m+1\)-vertex tree for \(1\le m\le7\), comparing the full polynomial to the algebraic expression. Its exact Sturm root counts check the three real intervals, endpoints, degree and square-free status for \(1\le m\le16\). Replaying the actual packaged program produced `ALL_EXACT_CHECKS_PASSED 103`.

These finite computations do not certify a theorem about every \(m\). The all-size proof is analytic: Rouché dominance on the circle, exact real monotonicity, the multiple-root obstruction, and the Möbius limiting argument. No independent scientific audit has been performed. Claims about angular zero-density and arbitrary spider arm-length profiles remain unproved here.
