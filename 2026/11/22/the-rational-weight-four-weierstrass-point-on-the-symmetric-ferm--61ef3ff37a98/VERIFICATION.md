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

# Verification record

The code file `d11_weierstrass_check.py` is an exact Python 3 rational-arithmetic certificate with no third-party dependencies. Run `python3 d11_weierstrass_check.py`. It verifies the formal identity \(y^{11}+1+t^{11}=0\) to precision \(t^{14}\), the exact order-eleven cancellation, the five leading coefficients, and rank jumps in the full standard invariant monomial basis. Expected output begins with `PASS: five upstairs orders 1,3,5,11,13; gap sequence 1,2,3,6,7; weight 4.`

Independent analytic checks: \(\Delta(P)=-2\) and \(\partial F/\partial Y(P)=11\) make the chosen local residue factor a unit; the quotient ramification index is \(2\), and its Riemann–Hurwitz genus is \(5\). These facts turn the exact finite-jet certificate into a determination of the complete canonical vanishing sequence. The code is not a proof of the geometry or a substitute for the cited invariant-differential theorem. No external independent audit has been performed.
