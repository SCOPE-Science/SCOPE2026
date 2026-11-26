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

For every real strictly proper candidate, p_λ(z)=z^n−σ−λd(z) is monic. Bounding the product of its n roots at μ and L by ρ^n and using Lp_μ(0)−μp_L(0)=−σ(L−μ) gives ρ^n≥(L−μ)/(L+μ). The constant numerator −2σ/(L+μ) makes p_λ(z)=z^n−σ(1−2λ/(L+μ)), attaining that bound exactly at either endpoint, including the repeated zero-root case at the midpoint. The optimizer satisfies the same signed n-step recurrence as b_k. Its subtraction gives the stated linear error recurrence, so interleaved error subsequences have factor at most q=(L−μ)/(L+μ) per block, and a nonzero endpoint mode realizes it in the worst case. Line 44 incorrectly writes equality between the fixed-A spectral norm and the maximum over the whole allowable interval; only ≤ is true in general, as obtained from the maximum over spec(A). That local correction immediately proves the same bound and does not change the theorem. The argument is exact for either sign and does not require n≥4.

## originality

FAIL

The prior source explicitly proves the n-order lower bound in the same class and states the attaining first-order filter for each sign. Its first-order filters composed with w=z^n have precisely the required denominator and bounds and are exactly the claimed filters. This makes the full equality a direct consequence of inspected prior results, even though the paper does not print these high-order special cases. The two real compositions work separately for every n, including even antiperiodic n, so no unsupported real rotation is needed.

## value

FAIL

Exact attainment is worthwhile for genuinely unresolved pole geometries. In these two families the stated construction is just the prior signed one-pole optimum run on each residue class; polynomial substitution gives the per-step rate, and the matching lower theorem already applies. There is no nonmechanical remainder such as a wider pole geometry, a classification of optimal numerators, or a new boundary for attainability.

The dated certificate retains the supplied scientific assessment, sources and limitations.
