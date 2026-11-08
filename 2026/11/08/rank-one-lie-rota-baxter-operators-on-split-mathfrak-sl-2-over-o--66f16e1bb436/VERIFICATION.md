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
# Reproducible mathematical checks

The two standalone files `verify_prime_fields.py` and `verify_gf9.py` run with unmodified Python 3 and no third-party modules. The first constructs \(\mathfrak{sl}_2(\mathbb F_p)\) explicitly for \(p=3,5,7\); the second independently constructs \(\mathbb F_9=\mathbb F_3[t]/(t^2+1)\) from its two-dimensional coefficient arithmetic. Each enumerates all ordered nonzero pairs \((a,b)\), forms the rank-one map \(R(x)=\operatorname{tr}(bx)a\), evaluates every basis-pair instance of the original weight-zero Lie Rota–Baxter equation, and compares membership with the proposed closed families. A rank-one operator has exactly \(q-1\) nonzero factorizations of this form; division by that factor gives the reported labeled-map counts.

## Recorded results
The exact output of both scripts is embedded as `direct_checks.txt`. Verification markers are `SL2_RANKONE_RB_DIRECT_PASS` and `SL2_RANKONE_RB_GF9_DIRECT_PASS`. At \(q=3,5,7,9\), the computed full rank-one populations are \(50,244,678,1448\); the square-zero populations are \(32,144,384,800\); the rank-one idempotent populations are \(9,25,49,81\). Every record matches the stated polynomial formulas. The scripts also compute self-adjoint and square-zero family intersections, independently of the formula counts.

## Limits
Finite experiments do not prove general formulas. The all-field proof is given in `RESULT.md`, especially the invariant-pairing reduction and rational normalizer count. The checks do not enumerate the full rank-two or rank-three solution loci, do not test scheme-theoretic reducedness, and do not constitute independent peer review.
