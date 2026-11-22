---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-18.md",
      "INDEPENDENT_AUDIT_2026-11-18.json"
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

Open-path step basis h^(k)=1_{i<k} gives an exact l1 jump coordinate representation and reduces linear quotient norm to max step response. Shifts satisfy V(S^s x)<=2V(x); for h^(m), nonnegative negative and positive jump contributions are disjoint if n>=2m, giving 2-p0 without cancellation. Boxcar telescoping gives edge derivative (x_(i+m)-x_i)/m. For step h^(k) the cyclic difference count is 2min{k,n-k,m,n-m} minus the omitted closing edge 1_{k>=m}, yielding exact two branches. Binomial powers meet local-support hypothesis, with p0=2^{-r}; Fourier nonconstant modes decay for fixed n. Independent exhaustive step tests all 496 n,m pairs n=2..31 match the formula. The n>=2r+2 boundary is essential; no beyond-threshold assertion is made.

## originality

PASS

This is not periodic BV contraction: the operator wraps at the boundary while the seminorm deletes the closing edge. Nochetto–Salgado construct a boundary-adjusted continuous TVD finite-element interpolation, while Carneiro–Finder–Sousa analyze maximal convolutions on a continuous torus. Resultary cyclic Gini-boxcar formulas use all-pairs variation, not this open-path variation; none inspected directly implies the exact 2-p0 mass law or all-width phase diagram.

## value

PASS

The sharp stability loss from a single boundary convention mismatch is a concrete numerical-analysis phenomenon. The complete width threshold m>=ceil(2n/3) and initial nonmonotone transient for a mixing kernel are natural operator-norm classifications and practical warnings about data wrap versus open-path metrics.

The dated certificate retains the supplied scientific assessment, sources and limitations.
