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
# Verification

The proof is contained in `RESULT.md`. The reproducible finite checker is `verify_edge_tilt.py`. Running `python verify_edge_tilt.py` with a standard Python 3 interpreter produced `PASS exact assertions: 520`.

The checker enumerated every spanning tree on \(K_{a,b}\) for nine ordered part sizes from \((2,2)\) through \((4,4)\), each at the five conductances \(0,1/3,1,2,7\). It independently compared exact weighted tree partition functions, all cross-part leaf covariances, the full aggregate joint distribution across weights, and baseline aggregate independence. The largest case contains 4,096 labeled spanning trees. The four rational identities behind the covariance factorization were also checked symbolically, with zero residuals.

These tests are finite and cannot prove statements about every integer part size or real conductance. The analytical counting and symmetry arguments in `RESULT.md` are the complete proof. Historical originality has not been independently validated.
