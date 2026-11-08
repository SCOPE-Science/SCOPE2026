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

# Verification record

The included `verify.py` uses only the Python 3 standard library. It enumerates the \(\binom{n}{n/2}\) balanced nearest-neighbor step words for each even \(n\) from 4 through 18, without invoking the path-transfer formula to classify regularity. For each word it computes its height span, tests every cyclic run position, and records the regular flag and the number of distinct full-span runs. Separately it computes \(W_{n,h}\) by repeated adjacency-vector multiplication and checks the exact marked-run identity \(\sum\text{runs}=2n\sum_hW_{n,h}\) at each \(n\). It also checks the finite double-run upper bound and the relation to the exact idempotent sum. It also independently constructs every graph endomorphism for \(n=4,6,8\) and directly tests the defining semigroup regularity and idempotency identities against the predicted totals. The command `python3 verify.py` completed with `VERIFY_OK`.

These checks cover finite cases, not all dimensions. The proof of the asserted asymptotic relative error depends on the nonoverlap of two full spans, an operator-norm estimate for the path transfer matrix, and two distinct cubic-root spectral variational costs. No external independent audit was performed.
