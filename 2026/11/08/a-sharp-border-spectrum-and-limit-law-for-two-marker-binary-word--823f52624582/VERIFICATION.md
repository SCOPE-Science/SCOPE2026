---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-11.md",
      "INDEPENDENT_AUDIT_2026-11-11.json"
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

A proper common prefix/suffix cannot contain both ones because identical two-marker alignment would force the suffix offset to zero. Zero-only borders contribute at most min(a,c); one-marker border uniquely has length a+c+1 and occurs precisely for b>=max(a,c), with full endpoint cases including n=2. Counting disjoint gap regions yields explicit integer interval A_n(t) and asymmetric/diagonal D_n(t); the enumerator splits into geometric sums H1+H2. Piecewise counts N_n(t)=n f(t/n)/2+O(1) uniformly in t and normalization C(n,2) establish uniform O(1/n) local limit and integrated moments. Inspect original verifier KMP prefix-function test on every two-one word 2<=n<=90, GF coefficients to m<=35, selected n<=2000 checks, but do not replace proof by finite tests.

## originality

PASS

Holub-Shallit random-word paper measures unrestricted fixed-alphabet typical longest borders O(1), not exactly two 1s with linear scaling. Harju-Nowotka treats conjugate border-correlation, Abelian-border work changes equality notion. No inspected specialized source supplied the exact A_n+D_n distribution or f(x) limit; still possible an obscure fixed-weight period paper contains equivalent data.

## value

PASS

Exact longest-border census in the canonical sparse nontrivial binary composition class; it exhibits linear-length borders unlike bounded-length typical unrestricted words. The complete finite spectrum, rational generating function and nondegenerate scaling law provide reusable baselines for fixed-content word combinatorics and string overlap algorithms.

The dated certificate retains the supplied scientific assessment, sources and limitations.
