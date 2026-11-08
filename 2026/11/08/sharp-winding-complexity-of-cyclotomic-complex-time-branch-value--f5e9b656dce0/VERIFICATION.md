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

# Verification and reproduction

The result is proved analytically by a cyclotomic norm argument and a finite-box pigeonhole argument. For nonzero \(\alpha=\sum a_j\zeta_d^j\) of coefficient budget at most \(N\), its integer norm is nonzero; the identity and conjugate embeddings contribute \(|\alpha|^2\), and the remaining \(\varphi(d)-2\) embeddings contribute factors at most \(N\). This proves the lower bound for every allowed \(d,N\). The upper proof uses \((L+1)^{\varphi(d)}\) independent sums and fewer square cells, with coefficient budget at most \(\varphi(d)L\), proving an upper bound of the same power. These are infinite arguments independent of the checker.

Run `python3 check_winding.py`, using Python 3.10 or newer and no third-party packages. The program reports finite lattice checks at \(d=3,4,6\), illustrative pigeonhole collisions at \(d=5,7,8,10,12\), and additional finite lower-bound examples at \(d=5,7,8\). It uses complex floating-point arithmetic only in those numerical illustrations, and its tolerance cannot certify the infinite group or exact algebraic norms. The proof explicitly establishes all nonzero and boundary cases.

No independent audit has been performed. The claimed originality is limited to inspected literature and searches. The result does not specify the branch-singularity set for any one selected local solution germ beyond the global continuation setting already established by the cited literature.

Finite checker output (the final line is its success marker):

```text
LATTICE_MINIMUM_OK 3
LATTICE_MINIMUM_OK 4
LATTICE_MINIMUM_OK 6
PIGEONHOLE_AND_NORM_SANITY_OK 5 4 budget 1 normalized_size 1.0
PIGEONHOLE_AND_NORM_SANITY_OK 7 6 budget 3 normalized_size 0.246979604
PIGEONHOLE_AND_NORM_SANITY_OK 8 4 budget 1 normalized_size 1.0
PIGEONHOLE_AND_NORM_SANITY_OK 10 4 budget 2 normalized_size 0.618033989
PIGEONHOLE_AND_NORM_SANITY_OK 12 4 budget 2 normalized_size 0.51763809
FINITE_LOWER_BOUND_OK 5 4 0.3819660113
FINITE_LOWER_BOUND_OK 7 3 0.2469796037
FINITE_LOWER_BOUND_OK 8 4 0.4142135624
CYCLOTOMIC_WINDING_CHECK_OK
```
