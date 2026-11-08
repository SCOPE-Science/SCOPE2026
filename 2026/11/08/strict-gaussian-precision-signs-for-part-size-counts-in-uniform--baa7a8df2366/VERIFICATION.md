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

The standalone `verify.py` uses only Python's standard library and was run on the packaged source. It completed with `VERIFY_OK exact_assertions= 3737`.

The script exactly enumerates \(2^{n-1}\) cut patterns at every size \(2\le n\le12\), compares rational moments against the derived formulas, verifies the negative distinct-size covariances, checks the deterministic size-sum identity, and checks exact rational covariance/precision inverses for \(1\le m\le14\). It also checks the scalar sign inequality through \(m=29\). Symbolic arguments in `RESULT.md` establish all-dimensional claims; the finite checks are not exhaustive proofs of them. Independent audit remains not performed.
