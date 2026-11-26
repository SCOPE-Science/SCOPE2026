---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
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

All unordered choices are exhausted by DD, DS, DX, SS and SX under part swap and independent healthy-vertex permutations. The grounded matrix retains the full degrees of the defective graph and is positive definite. Before deletion the zero-sum directions within the two parts have eigenvalue n, and the two class-constant directions give the 2×2 block with diagonal n and off-diagonal -sqrt(rs). This yields the displayed inverse and its squared trace. Deleting the missing-link incidence vector restricted to followers gives a rank-one downdate, with denominator 1-z^T H z positive by positive definiteness; this still works when one or both endpoints are pinned. For the positive mode lambda the Lyapunov equations give zero position-velocity covariance, velocity variance 1/(2 lambda), and position variance 1/(2 lambda^2) for white acceleration noise and matched gains. Exact independent replay recovered all five rational costs, the shifted positive coefficient lists for DS, DX and SX relative to DD, and the sign of J_DD-J_SS: Q(3)=-581, while all coefficients of Q(t+4) are positive. Thus the five-class minimization is strict between classes at every allowed integer; SS gives 2 binom(n-1,2) pairs and DD one. Exact direct inversion matched 245 pairs at n=3,...,7 and confirmed the first-order disagreement at n=4 and 5. The all-size first-order switch is a cited comparison, not a consequence of the square trace. The all-size second-order result rests on the sign certificates, not the finite replay. Frozen verifier inspected, not executed; independent calculation details at /workspace/evidence/defective_biclique_exact.md.

## originality

PASS

No equivalent or dominating theorem found in the inspected material. The indexed results with the same single deletion optimize the first inverse moment; the indexed near-balanced inverse-square result does not have a missing link. The matched-damping interpretation and low-rank algebra are established methods, not claims of novelty.

## value

PASS

One link deletion is a natural minimal fault, and the square trace models a specific white-noise position covariance rather than an arbitrary extra statistic. Exact strict comparison of all five pair classes changes the design recommendation at two actual network sizes, identifies every optimal intervention and gives its cost on the full family. This is an exact benchmark, not a claim about multiple faults, other damping laws or transients.

The dated certificate retains the supplied scientific assessment, sources and limitations.
