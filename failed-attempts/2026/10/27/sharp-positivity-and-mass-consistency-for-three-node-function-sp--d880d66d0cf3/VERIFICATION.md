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

When s is nonzero the nodal matrix has determinant 2s(1−c) and forces D. Independently, exact quadrature of the derivatives of the cosine/cosh forces equal endpoint weights q, and the derivative of the sine/sinh gives 2cq+h_mid=2s/k. The derivative of their product gives h_mid+2(2c²−1)q=2sc/k by the double-frequency identity in both cases. Solving gives q=s/[k(1+2c)] and h_mid=2(1+c)q; direct multiplication of the forced D gives the SBP identity. At sin ω=0 a zero sample vector of sin(ωx) has nonzero center derivative; at 1+2cos ω=0 the zero endpoint diagonal entries of D violate the boundary identity. The sign chart therefore gives exactly the two open residue bands, and the condition number follows from the ordered positive exponential weights. Differentiating the excess-mass numerators gives 2sinh λ(sinh λ−λ) and 2sin ω(ω−sin ω), both strictly positive on the respective exponential and first trigonometric domains. On the second positive band the logarithmic derivative of the half-mass is strictly positive since cot(ω−π)>1/√3>1/ω; the endpoint limits are zero and infinity. Independently solving the stated equation numerically gives 4.028701322025359624. Replay: use the nodal matrices in RESULT.md lines 26–40 and scalar identities in lines 42–59; the packaged verify_fsbp.py was inspected, not executed. The mass statements for trigonometric fitting apply only in the fundamental period; positivity, not mass, repeats in all aliases. No fully discrete PDE property was validated.

## originality

FAIL

Distinct catalogue theorems cover both trigonometric bands and the exact normalized midpoint frequency, and a direct continuation of the explicitly tabulated midpoint matrices gives the exponential norm, hence its condition number. A stronger indexed exponential obstruction independently excludes three closed mass-exact nodes. This establishes coverage, not priority or dependence between entries.

## value

FAIL

Positive fixed-grid fitting and correct physical mass are worthwhile numerical design questions. However, the exact bands, normalized root and mass infeasibility are supplied by the matching stronger results. The remaining appearance of a new exponential condition number is the immediate diagonal weight ratio after continuing an already explicit matrix, not a distinct conditioning theorem that survives the comparison. No new numerical stability or higher-period mass result is proved.

The dated certificate retains the supplied scientific assessment, sources and limitations.
