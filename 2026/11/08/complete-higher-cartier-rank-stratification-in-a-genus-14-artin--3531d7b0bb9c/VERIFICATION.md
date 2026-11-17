---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-10.md",
      "INDEPENDENT_AUDIT_2026-11-10.json"
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

The Artin–Schreier cover has a single pole of order 8 prime to p=5; genus g=(p-1)(8-1)/2=14, and a 14-differential basis x^i y^j dx with 5i+8j<=26. The unrooted Cartier matrix entry M_{(u,l),(i,j)}=(-1)^{j-l} binom(j,l)[x^{5u+4}](x^i F^{j-l}) is a polynomial over characteristic five. Four constant pivots reduce first rank to 4+rank[[2a,a²+2b],[-2b,-2e]] with determinant proportional to Δ=ae+2a²b-b²; its rank 2,1,0 produces first ranks 6,5,4. Frobenius-twisted products M^[5]M, M^[25]M^[5]M, M^[125]M^[25]M^[5]M have ranks as stated: b!=0 gives 3,1,0; b=0 gives second rank 1 exactly at ae^5+1=0 and 2 otherwise, higher zero. The characteristic-five polynomial identities in the inspected verify_cartier.py support the all-algebraic-closure assertions. Independent construction and direct rank multiplication for seven F5 tuples checked all listed special profiles, including the codim-two anomaly; these finite checks do not themselves prove the infinite-field result.

## originality

PASS

The exact six-stratum higher Cartier iteration profile on the full five-parameter monic degree-eight one-pole family is more specific than the already-known two-parameter genus-fourteen first-Cartier-rank tangent-divisor result. Prior general bounds and degree-specific examples do not imply the explicit b=0,ae^5+1=0 second-rank jump. An inaccessible relevant primary paper is recorded as a risk, not treated as failure.

## value

PASS

This is a natural complete coefficient-family classification of higher Cartier nilpotence, not an arbitrary sample. The Frobenius-twisted codimension-two second-rank exception has generic first Cartier rank, proving a-number alone cannot identify the nilpotent structure. The exact six strata, irreducible quadric rank divisor and hidden higher-rank sublocus are relevant to moduli of Artin–Schreier Jacobians.

The dated certificate retains the supplied scientific assessment, sources and limitations.
