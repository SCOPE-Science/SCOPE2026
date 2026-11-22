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

# Reproducibility of the finite checks

The included `verify.py` uses only the Python 3 standard library; run `python3 verify.py` from the directory containing the file. A run on the unmodified standalone script returned:

```
PASS: 36 exact independent multinomial enumeration instances; 1556964 assertions and arithmetic conditions checked.
PASS: deterministic roughness identity, pair-collision upper coupling, Poisson parameter, triple-error bound, independent-set zero coefficient.
LIMIT: finite checks do not establish asymptotics or the Chen-Stein theorem.
```

For \(3\le n\le8\) and \(1\le N\le6\), every labelled category sequence is enumerated (at most \(262{,}144\) possible per case). The script verifies the identity \(D_{n,N}=2N-2T_{n,N}\), the order \(0\le T_{n,N}\le U_{n,N}\), the finite Stirling/independent-set saturation formula, the exact mean \(\mathbb E U_{n,N}=N(N-1)/n\), and the upper bounds on mismatch probability and expected proxy gap. It also checks the formal Poisson error bound is nonnegative. Exact rational comparisons are used for numerical probability checks.

The infinite Poisson and Gaussian limits rely on the full proof in RESULT.md and on Arratia–Goldstein–Gordon Theorem 1, rather than on enumeration. In particular, the theorem's norm is twice the standard total-variation distance used in the statement; this normalization is explicitly accounted for.
