---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-12.md",
      "INDEPENDENT_AUDIT_2026-11-12.json"
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

For each residue r=qu+v modulo a=qk, the map from coefficient triples to nonnegative (j,h) with h<=u+jk and j(k+1)+(q-1)h<=N-u-v is bijective. Its cheapest pair (0,0), second costs k+1 or min(q-1,k+1), and monotonicity upon adding a prove all W0,W1. Residue sum/max gives g0,g1,n0,n1 and exact gluing deficit. Independent capped-denumerant dynamic program verifies 110 parameter pairs and residuewise thresholds; finite work is corroborative.

## originality

PASS

Exact positive gluing deficit, q-dependent second Apéry table and first generalized genus hold for a two-parameter lacunary family beyond the known general gluing upper/equality theorem; however the q=4 shifted-square subfamily was previously solved and is explicitly not claimed as uncovered.

## value

PASS

The exact deficit quantifies when and how sharply a natural general gluing bound fails and provides all residuewise two-representation thresholds on an infinite nonarithmetic semigroup family, beyond a textbook restatement of equality.

The dated certificate retains the supplied scientific assessment, sources and limitations.
