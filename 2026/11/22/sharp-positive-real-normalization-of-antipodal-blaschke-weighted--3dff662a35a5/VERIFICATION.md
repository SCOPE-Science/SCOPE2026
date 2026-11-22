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

# Verification of mathematical statements
The weighted-kernel formula follows by orthogonal deletion of the two evaluation vectors of the ordinary Bergman kernel. A Python 3 / SymPy script `CHECK.py` exactly checks the polynomial cancellation, Fourier-boundary numerator factorization, and the two equality pairs. Nonnegativity rests on the factors \(1-t^2>0\), \(1-u\ge0\), and \(1+t^2+2tc\ge(1-t)^2>0\), not on numerical sampling. Strict positivity in the interior is established by separate harmonic strong minimum principles; the polynomial margin is then an exact analytic consequence. Historical originality has not been independently audited.
