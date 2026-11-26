---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

On either open triangle the mixed density is h(max(u,v)); positivity implies h>=0 almost everywhere. Conversely, that density plus the diagonal line density f has both marginals uniform by f=k-tk' and k(1)=1. Integrating the conditional mass for u<=v gives u k(v), as desired. Thus p=integral f and Tonelli for the copula integral gives rho=3 integral t^2 f. The upper endpoint follows by subtracting b^2 from the moment weight and comparing with the upper step at b=1-p; the integral has strict sign unless the generators agree a.e. For the lower deficit, the primitive of 4t(a^2-t^2) divided by the square of the endpoint cancels with subtraction of 4(a^2-t^2), leaving 3t^2-2a^2 below a. Above a the primitive is a^4, leaving the nonnegative factor (t^2-a^2)(3t^2+a^2)/t^2. At a=sqrt(p), vanishing forces h=0 below a and f=0 above a; local absolute continuity then gives k=a below a, hence f=a there. Both step generators satisfy the copula criterion. Fixed-p convex interpolation and the forced constant endpoint generators establish the full closed region. Independently checked both kernel identities and 216 rational admissible generator examples using /workspace/reproductions/frozen_diagnostics.py 3. The frozen checker was not executed; none of these examples substitutes for proof.

## originality

PASS

Best of current knowledge for the sharp joint fixed-diagonal-mass envelope with its lower deficit and rigidity. The copula family, marginal/rank formulas, known extremal examples, and standard upper fixed-mass rearrangement principle are not the originality claim.

## value

PASS

Exact coincidence and rank concordance encode different dependence properties. At each tie mass this theorem gives the precise information that one statistic does and does not determine about the other, with identifiable endpoints and an exact lower deficit even for merely measurable generators. The result does not generalize the range to arbitrary copulas or make an estimation claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
