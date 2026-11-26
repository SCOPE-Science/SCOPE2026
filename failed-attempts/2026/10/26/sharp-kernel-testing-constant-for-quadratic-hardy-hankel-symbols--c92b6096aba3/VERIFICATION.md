---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

The Hardy Hankel corner in the specified bases is [[conj(a),conj(b)],[conj(b),0]]. With b nonzero its norm is |b|Λ, where Λ−Λ⁻¹=|a|/|b|=t, as follows from the trace and determinant of the Gram matrix. Aligning bw with a gives the kernel profile F_t(r)=(1−r²)((t+r)²+1). Writing s=Λ⁻², at r=√s/2 the squared quotient is (1−s/4)(1+s²/4), differing from 25/27 by (8−3s)(3s−2)²/432. At s=2/3 this radius is the actual maximum by the derivative test and strict concavity for t>0, so the sharpness and sole mixed equality class are valid. Pure monomials attain ratio one at w=0. The Garsia identification uses T_{conj ψ}k_w=conj(ψ(w))k_w and orthogonal projection. Read the finite checker and verification note; the quoted tests are not a substitute for this all-coefficient computation.

## originality

FAIL

Distinct indexed record 8fb488666656 explicitly states the identical sharp bound, nonzero complex quadratic domain, equality class and maximizing kernel. This is demonstrated equivalent coverage, not an inference about who had priority or about ordering within the day. The frozen claim has no distinct residual theorem on its stated domain.

## value

FAIL

The best testing loss for quadratics is a natural invariant, but this submission supplies the same exact invariant and equality classification as a distinct record. The short explicit-radius proof is a useful exposition; no independent quantitative, structural or broader new claim is established by it.

The dated certificate retains the supplied scientific assessment, sources and limitations.
