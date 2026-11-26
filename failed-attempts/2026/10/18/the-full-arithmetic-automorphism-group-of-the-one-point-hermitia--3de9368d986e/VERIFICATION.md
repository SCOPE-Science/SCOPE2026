---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

The gradient proves smoothness and subtracting the s-Frobenius conjugate gives unique K-point P=[0:0:1]. In fact projectivity of every K-automorphism follows directly: Y=0 cuts out exactly (s+1)P, so the complete hyperplane linear series is invariant under any K-automorphism, giving the plane extension over K. This verifies the step without relying on geometric descent. After fixing the P and tangent flag and normalizing the middle diagonal entry to 1, form comparison gives λ=a^(s+1)=f=f^s, then (λ−1)η lies in F_s, forcing λ=f=1. The off-diagonal entry imposes d=−a v^s and the middle coefficient is h+h^s=−v^(s+1). Multiplication gives the quoted law, and choosing v' with v'/v outside F_s for v nonzero proves the center statement. Norm and trace give s+1 and s fibres, respectively, including characteristic two. Independently computed the exact stabilizer over F16 using bit-polynomial arithmetic modulo x^4+x+1, with η=x. For every nonzero a set f=a^5 from the necessary coefficient equalities, then tested all (v,d,h) in F16³ for scalar form preservation. Exactly the 320 stated normalized matrices survived, including all possible h, and the result was compared as a set rather than only a count.

## originality

FAIL

An earlier distinct published record d634e729a082 proves the same full abstract arithmetic automorphism group for every s≥2, hence strictly dominates the frozen s≥3 range. Its result includes identical normalized triangular representatives, norm/trace constraints, semidirect product and order. A second earlier record df9fe3714bc9 already computes the exact same rational projective stabilizer. This is demonstrated prior coverage, not an access-based failure.

## value

FAIL

The arithmetic group is a natural invariant, and the abstract/projective distinction is useful, but the frozen finding contributes no new invariant, parameter case, or consequence beyond the existing stronger all-s full-group theorem. Recomputing that known group for a smaller range does not meet the scientific value criterion.

The dated certificate retains the supplied scientific assessment, sources and limitations.
