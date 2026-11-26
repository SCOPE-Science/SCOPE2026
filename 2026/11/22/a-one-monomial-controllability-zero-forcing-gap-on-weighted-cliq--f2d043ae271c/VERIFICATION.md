---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

I reconstructed the all-parameter PBH test directly from the support of a putative invisible eigenvector. Omitting two nongateways on either side permits their difference mode. Otherwise each clique has at least one selected nongateway, because p,q≥3. For a Laplacian eigenvector vanishing on the inputs, that selected row forces x_U+x_A=0, where x_A is the sole omitted nongateway value if present and zero otherwise; similarly x_V+x_B=0. If x_U≠0, the omitted-nongateway row forces eigenvalue pa. The gateway row is then pa x_U+t(x_U−x_V), so positivity of t gives x_V=x_U≠0; the right omitted-nongateway row forces qb=pa. The argument starting from x_V is symmetric. If both gateway values are zero the whole vector vanishes. Thus the only additional obstruction has two unselected gateways, one omitted nongateway each, and equal clique spectral scales. Conversely the vector with values +1 at the two gateways and −1 at the omitted nongateways is exactly an invisible eigenvector in this case. Independently the quotient characteristic polynomial can be recovered by starting at t=0 with λ²(λ−pa)(λ−qb) and subtracting the bridge rank-one term tλ[(λ−a)(λ−qb)+(λ−b)(λ−pa)]. This yields both claimed collision factors; conjugation to irreducible symmetric tridiagonal form proves simplicity and the end rows preclude a zero end entry. For ordinary zero forcing, omitted twin pairs obstruct propagation, and leaving both gateways plus one nongateway each white stalls. Otherwise a blue gateway, or a clique with every nongateway blue, starts forces that clear its own clique, cross the bridge, then clear the other side. Binomial counting gives the quoted C and Z polynomials and both leading coefficients; the only difference is the least-degree monomial off resonance. RESULT.md lines 35–76 supply the full proof. The supplementary symbolic_certificate.py and verify.py were inspected, not executed here. At integer examples full modular rank implies full rational rank; modular deficiency alone is not a rational noncontrollability certificate, and the exact proof is needed for the full positive-real statement. Nothing here bounds control energy or conditioning.

## originality

PASS

The graph zero-forcing polynomial, the PBH method, and examples of fixed-Laplacian control by a non-zero-forcing set are already known. The added content is the complete dedicated-input classification on the internally uniform weighted one-bridge family and the exact bridge-independent spectral boundary where the two notions agree. Inspected related statements do not cover that narrower quantitative claim; this is provisional as to historical priority.

## value

PASS

This natural two-community dynamical family gives an explicit example in which a graph-level robust criterion can be sharpened for every dedicated actuator subset and every positive bridge strength. The equality of internal spectral scales, rather than equality of clique weights or sizes separately, predicts exactly when a compact mode removes the extra smallest placements. The exact census and its one-monomial discrepancy make the example a useful structural benchmark, not a claim about quantitative control performance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
