---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

The iid continuous-score representation gives the exact degree identity via the left larger and right smaller score counts. Deleting the finitely many marked scores leaves independent iid uniforms and changes the signed, centered empirical process by O(r/sqrt(n)) uniformly. For a fixed vector of marks, the remaining signed empirical sums have a joint Gaussian limit with kernel min(u,v)-uv by the bounded-summand triangular-array CLT (condition on the marks, use Cramér–Wold, then integrate bounded characteristic functions). This gives the same independent bridge and marks as the package's Donsker argument. In that argument the strict empirical count has left-continuous jumps, so the usual càdlàg version of the D[0,1] statement uses <=, differing uniformly by at most 1/sqrt(n) almost surely; the exact strict inversion identity is unchanged. Moving the cut from floor(n/2) to i-1 inserts or deletes O(sqrt(n)) indicators; conditionally on the score their centered sum has standard deviation O(n^(1/4)) and the omitted self term has magnitude at most one. This yields the stated t(1-2U) drift. Integrating bridge kernels gives 1/6 on the noise diagonal and 1/12 off the diagonal; the drift adds t^2/3 on each diagonal. The finite variance also follows by conditioning on the marked score, with independent Bernoulli neighbor tests. For different vertices the shared edge contributes 1/4 and each other vertex contributes net 1/12 from the three possible overlapping pairs in a triple of labels, giving (n+1)/12.

## originality

FAIL

Chapuy's Theorem 1 gives the stronger uniform-permutation discrepancy-field limit in C([0,1]^2). The claimed shared-bridge law, including independence of the evaluation marks and the critical-window drift, follows by an exact rectangle-count identity, deletion of finitely many permutation points, and continuous evaluation of that known field. The rejection is based on a demonstrated implication, not on a search miss or on mere similarity to the known one-point degree law.

## value

FAIL

The central-window interpretation is natural and could be pedagogically useful, but the frozen finding claims only the finite marked evaluations and moments of a field already known for the same probability model. The necessary reduction is elementary and uniform, and the finite moment claims are covered by existing exact covariance information. No independent rate, growing-window result, or other non-mechanically-implied remainder was established on this record. Thus it does not qualify as a standalone new finding under the stated value standard.

The dated certificate retains the supplied scientific assessment, sources and limitations.
