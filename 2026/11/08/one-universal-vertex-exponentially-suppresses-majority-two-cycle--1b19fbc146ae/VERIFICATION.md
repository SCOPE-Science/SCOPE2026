---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-12.md",
      "INDEPENDENT_AUDIT_2026-11-12.json"
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

With n complementary pairs, an old vertex sees k-s_i ones, and the new universal vertex sees k-c. On C_n the central k=n layer is invariant: 00 and 11 pairs exchange, mixed pairs remain fixed; outside it every state becomes unanimous after one update. Therefore fixed=2+2^n and primitive-two states=C(2n,n)-2^n. On H_n, every pair becomes homogeneous after one update, with exactly two unanimous fixed states; homogeneous-pair states in the two central weights n,n+1 are primitive 2-cycles, giving 2*C(n,ceil(n/2)) states, and all other states enter consensus by update two. Stirling yields P_C~1/sqrt(pi*n), P_H~2^-n*sqrt(2/(pi*n)), ratio~sqrt(2)*2^-n. Independent bitwise open-neighbor updater checked every labelled initial state for n=2..5, reproducing formulas; finite checks corroborate, not replace all-n case split.

## originality

PASS

Best-of-knowledge distinct exact result after comparing named equivalent, broader and database formulations; known subclaims explicitly credited, with residual priority risks.

## value

PASS

An exact immediate-period and sharp transient classification quantifies how one added universal vertex exponentially suppresses synchronous majority oscillation on a natural dense multipartite graph; the asymptotic contrast is a motivated structural perturbation rather than a scalar restatement of eventual period two.

The dated certificate retains the supplied scientific assessment, sources and limitations.
