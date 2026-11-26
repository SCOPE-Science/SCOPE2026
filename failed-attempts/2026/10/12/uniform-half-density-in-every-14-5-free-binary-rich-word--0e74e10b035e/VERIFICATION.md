---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

CMR Theorem 1 has both suffix branches f(h^n(v_n)) and f(g(h^n(v_n))) for every n, with the suffix, branch and ternary preimage allowed to depend on n. Its 14/5-free hypothesis excludes any factor of exponent at least 14/5; it does not require that the supremum be strictly less. Directly, the binary image imbalance of f is (-1,0,1) on the three letters, and this row is unchanged by each of h and g. Every letter block of either suffix has imbalance at most one and length at least 2^n (at least 3·2^n in the g branch). A factor uses at most |u|/2^n complete blocks, at most two fragments of a finite block maximum length M_n, and at most p_n letters preceding the chosen suffix. This proves the claimed inequality with C_n=p_n+2M_n, even for factors wholly in the discarded prefix. Taking limsup in length at fixed n, then allowing n to increase, proves uniform half-density. The finite source checks are regressions only; no finite replay is needed for these identities or proves the suffix theorem.

## originality

FAIL

This is a correct direct corollary of a substantially stronger published suffix theorem with the identical domain. It uses only the displayed substitutions and the standard bounded loss at the two ends of a block decomposition. A literal general half-density sentence is not needed for prior coverage; no additional non-implied part survives.

## value

FAIL

Uniform factor frequency is a natural observable, but as a standalone finding this is just an elementary block-length/weight estimate on the already published exact structure. It contributes neither a discrepancy rate beyond that implication nor information on a larger class, and the family of constants is just an equivalent way to state the limit. The calculation is useful as exposition of the structural theorem, not as a new standalone scientific result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
