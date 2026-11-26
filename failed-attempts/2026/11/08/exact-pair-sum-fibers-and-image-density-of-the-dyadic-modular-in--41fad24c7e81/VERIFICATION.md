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

For odd inputs, t=s/(uv), so the zero slice has q/2 ordered pairs and nonzero s,t must have the same positive valuation h. Divide by 2^h and translate by the integral half of s. The resulting square roots modulo 2^(k-h) must be even for h=1 and odd otherwise; each lifts 2^h times. The odd-unit squaring kernel has size four from modulus 8 onward (x²=1 forces x=±1 modulo half the modulus), giving all unit targets 1 mod 8, with the two smaller moduli checked separately. Nonzero even square counts follow by extracting the root valuation; zero roots are multiples of 2^ceil((k-h)/2). As t varies, these targets cover all of the specified parity, so the h>=2 support contributes q²/192+5/3 and the h=1 support contributes (q/4) times q/48+5/3 for even k or q/48+4/3 for odd k, plus the origin. For energy the equal-sum quadruple parametrization reduces to a product zero modulo 2^K, K=k-3, with odd variable sum and precisely one odd factor. The two even factors have K*2^(K-1) admissible pairs (directly for K=1, otherwise truncate the valuation after dividing both by 2). Including the 128 lifts gives 3(k-3)q²/2. Orthogonality gives the stated q^(-2) normalization. The verification note and uploaded checker were read, not executed. A separate bounded direct convolution replay /workspace/branches/replay_frozen.py matched all fibers, image size and energy for k=4–9, including zero fibers by equality of support dictionaries.

## originality

FAIL

A distinct indexed result on the dyadic cubic graph implies the complete inverse-graph law via a target bijection and the parity filter on the product. Thus the different second coordinate does not produce new fiber data. Its indexed date is not used to infer order or priority. The odd-residue-field hyperbola result and classical moment literature alone would not establish this coverage.

## value

FAIL

The density and fiber law are natural invariants, but they are obtained by a target substitution and parity restriction of the complete indexed cubic fiber table; the support and energy then use already given square averages. The frozen claim does not leave an additional nonmechanical invariant or structural result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
