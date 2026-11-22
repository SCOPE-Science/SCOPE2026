---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-17.md",
      "INDEPENDENT_AUDIT_2026-11-17.json"
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

Starting from the exact published centered tent-weight numerator, m=n+4 gives reciprocal coefficients c_(4+t)=Σ_A W_m(A)W_m(mt−4A) for −4≤t≤4. Direct finite quadratic sums in classes n=4h+1,4h+3 give five explicit cubic-in-h coefficients. The reciprocal transform Q(z)=z⁴F_n(z+z^(−1)) produces a quartic F with F(−2)=n+4>0, F(−3)<0, positive leading coefficient, so one root on (−∞,−3) and one in (−3,−2). The exact coefficients of F(−2−u) have signs +,−,−,+,+ (or a zero cubic at h=0), hence at most two positive roots by Descartes, proving those distinct simple roots exhaustive below −2. Positive coefficients exclude y>2; Deng–Fu unit-circle Fejér strict positivity excludes −2≤y≤2. The remaining reduced roots are conjugate nonreal; reciprocal quadratic lifting gives exactly four inside and four outside, no unit-circle or multiple roots. Independently reconstructed tent sums and reduced roots for odd n=1,3,5,7,9,11,17,31,43; source CHECK.py validates symbolic identities for all h. Tests alone do not replace the full analytic sign proof.

## originality

PASS

Best-of-knowledge: substantive comparison of the exact claim and implications with closest published scientific results, including generalizations and potential near-equivalences; residual priority risks explicitly retained.

## value

PASS

The exact all-odd-denominator root-type and simplicity classification at the first nontrivial even gap four is a natural finite-parameter question for a canonical Bergman zero slice, sharpening a general count and large-n condensation. Uniform separation of the two negative interior roots by a fixed algebraic boundary is a concrete reusable structural fact, not a trivial asymptotic substitution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
