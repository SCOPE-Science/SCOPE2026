---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-11.md",
      "INDEPENDENT_AUDIT_2026-11-11.json"
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

For fixed one-column inconsistent y=ux*+r0 with u*r0=0, rotational invariance reduces to e1,e2. Haar P=QQ* gives R_H=|P12|^2/P11^2=((1-U)/U)V with independent U~Beta(delta ell,delta(n-ell)) and V~Beta(delta,delta(n-2)). Independent gamma splitting yields R_H=B Z/W with Z~Gamma(delta), W~Gamma(delta ell), B~Beta(delta(n-ell),delta(ell-1)), B=1 at ell=1; Gaussian projection independently gives R_G=Z/W. For ell>1, B in (0,1) and positive beta-prime density yields strict all-t threshold stochastic order. Gamma inverse moments finite exactly q<delta ell, and beta moments/regular variation yield sharp tail constant. Analytic derivation is consistent for both real delta=1/2 and complex delta=1; independent checks recovered real E(RG)=1/3 and E(RH)=1/7 at (n,ell)=(8,5), and complex 1/2,3/10 at (6,3). Finite checks are not distributional proof.

## originality

FAIL

FAIL: A published November 2, 2026 theorem, Independent beta attenuation of Gaussian least-squares sketch error by a Haar sketch (Resultary), proves precisely the independent Beta-squared-error law, strict stochastic tail ordering, all finite/infinite moments and leading tail coefficient for every REAL rank-one design and arbitrarily many right-hand sides; the assigned scalar REAL theorem is a strict special case. The assigned extra COMPLEX field uses the same gamma/Beta algebra with shape delta=1 instead of 1/2 and is not a separately motivated structural novelty. Existing Epperly–Webber proves complex first moments. Equal mathematical claims are covered despite different notation and narrower parameters.

## value

FAIL

FAIL: The motivating all-threshold independent Beta coupling and tail attenuation are already established in a broader real rank-one setting; the only additional complex scalar adaptation is a routine field substitution with standard complex-Gaussian gamma shapes. No independent unknown reliability invariant or mathematical reason for that minor extension has been demonstrated, although the mathematics is correct.

The dated certificate retains the supplied scientific assessment, sources and limitations.
