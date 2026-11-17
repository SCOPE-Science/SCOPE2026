---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-13.md",
      "INDEPENDENT_AUDIT_2026-11-13.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Frozen proof reconstructs the mean-zero q-point L4 bound c_q=q-2+1/(q-1) and centered cubic moment m_q=(q-2)/sqrt(q-1), the fourth moment expansion of independent Fourier coordinates, and q>=5 positive mixed-energy remainder. The critical q4 case reduces after v=sqrt(sum (Xj/T)^2) to P(t,v)=3t^4+2t²+1-(8/sqrt3)tv+(2/3)v². Its minimizer is v=2sqrt3 t when t<=1/(2sqrt3), strictly positive, otherwise v=1 with exact factor (sqrt3 t-1)^2(3t²+2sqrt3 t+5)/3; equality forces one axis, then Fourier inversion forces scalar character. Independently verified scalar factorization, 800 sampled q=4 Fourier arrays on 2/3 axes, and exact q=2/3 additive witness moments 21 and 77. The unrestricted q,d claim rests on analytic proof, not finite checks.

## originality

PASS

The previous sharp cross theorem begins at group order five and two axes; the audited order-four endpoint and any-axis rigidity use a distinct extremal argument, not covered by inspected published text.

## value

PASS

Resolving exact previously excluded smallest admissible group order four is a sharp structural endpoint, with complete equality rigidity for arbitrary number of coordinate axes. The discrete threshold distinguishes q>=4 from explicit q2/3 failures and makes the result useful in finite-group Fourier extension.

The dated certificate retains the supplied scientific assessment, sources and limitations.
