---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-09.md",
      "INDEPENDENT_AUDIT_2026-11-09.json"
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

Contracting k compatible prescribed arrows in Ewens permutations gives theta^c/(theta+n-k)_k probabilities; summing descending ordered image pairs yields p_n=(n-1)(n+2theta-2)/[2(n+theta-1)(n+theta-2)]. Conditioning on F_i=1 deletes the fixed letter and reduces to Ewens on n-1 labels. For remote positions conditional descent has probability p_(n-1); at incidence the probabilities are (i-1)/(theta+n-2) and (n-i)/(theta+n-2). Multiplying by q_n=theta/(theta+n-1) and subtracting q_n p_n gives all entries and the stated remote factor. Summing over all i,j yields exactly the n=3 aggregate sign boundary; signs valid for theta>0. The proof and finite exact arithmetic are sound, but originality is refuted by published equivalent full result.

## originality

FAIL

Decisive literal full-claim prior coverage: Full matrix and all ordinary-difference corollaries are printed verbatim in earlier published Resultary Nov 8 record.

## value

FAIL

The positional covariance sign pattern is intrinsically interesting, but it is already completely established with stronger cyclic information in a published same-object, all-parameter theorem. The present package gives no new motivated independent invariant or nontrivial strengthening; recomputing a covered matrix cannot receive mathematical value PASS.

The dated certificate retains the supplied scientific assessment, sources and limitations.
