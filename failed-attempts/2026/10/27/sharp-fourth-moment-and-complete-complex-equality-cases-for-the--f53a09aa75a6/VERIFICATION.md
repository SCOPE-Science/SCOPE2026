---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

For Haar probability on the ordinary four-torus, the 36 ordered two-edge pairs have 6 singleton, 12 double and 1 six-element sum fibers. The latter consists of the three perfect matchings with both orderings. Thus the unweighted witness gives (6+48+36)/36=5/2. For arbitrary complex coefficients Parseval gives 2S²−sum |a|⁴ plus eight times the real part of the three distinct cross products of matching products. Grouping squared magnitudes into matching masses b_j gives the upper bound 3S²−(3/2) sum b_j². Equality requires all three masses equal, equality within each pair of magnitudes, and all three matching products aligned. Since S>0, their products then agree and the phase factorization follows by choosing a unit square root of a_12 a_13/a_23 after normalizing magnitudes. The converse is immediate. This checks the unrestricted-complex statement, not only the finite count. The supplied checker was inspected, not executed; no formal verification or external attestation is inferred.

## originality

FAIL

An existing indexed all-squarefree-layer result explicitly includes degree two in its scope and proof; its n=4,k=2 specialization gives both the identical constant and identical full coefficient equality family. A six-root result also optimizes the identical coefficient quartic after relabeling. The failure is demonstrated coverage, not inability to exclude unknown sources.

## value

FAIL

This is a natural and instructive collision example, but the submitted theorem is an exact parameter substitution of an existing broader result and its optimization is duplicated under six-root relabeling. The small direct proof adds exposition without a distinct invariant, boundary theorem or reusable extension established in the frozen claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
