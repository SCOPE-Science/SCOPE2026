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

The statements in the Finding hold, but the proof of stochastic order in RESULT.md line 57 is false as written. For n=4, m=2, and consecutive draws 3,1, the alleged monotone coupling gives O₂=2 and O₃=1. An independent proof uses the same draw space without the pointwise inference. Let E count empties among the first m+1 boxes before the new draw. At threshold ℓ, crossing up can occur only when E=ℓ and box m+1 is empty, followed by a draw avoiding the ℓ empties. Crossing down needs E=ℓ and box m+1 occupied, followed by a draw hitting an empty. Exchangeability gives the respective conditional probabilities ℓ/(m+1) and 1−ℓ/(m+1) for the box state. Subtracting yields P(O_{m+1}≥ℓ)−P(O_m≥ℓ)=[ℓ(n−m−1)/(n(m+1))] P(E=ℓ). This is nonnegative for 1≤m≤n−2, and strictly positive at ℓ=m+1 because the first m−1 draws can all avoid the eligible boxes. The 0-to-1 transition is deterministic. Conditioning on a forbidden target set gives the factorial moments, and the size-one restriction identity gives the exact covariance. The cyclic-tail difference on j∼x√n satisfies n(a_n(j)−a_{n−1}(j))→(x²/2)e^(−x²/2); the product bounds in the frozen proof justify summation. The Rayleigh and empty-box variance constants give the stated correlation scale.

## originality

FAIL

The occupancy law, both exact expressions, exact covariance and both leading constants are covered by an exact-joint-law record. A distinct reverse-likelihood-ratio record states the same strict stochastic order and transform covariance inequality, as consequences of a stronger same-model order. Thus the whole Finding is covered, irrespective of unresolved chronology between same-day records.

## value

FAIL

The dependence question is natural and the exact law is useful, but this submission adds neither a new invariant nor a stronger dependence statement beyond the exact-law and likelihood-ratio records. The purported simpler proof of the strict order relies on a false pointwise claim and therefore does not supply an independent useful method as submitted.

The dated certificate retains the supplied scientific assessment, sources and limitations.
