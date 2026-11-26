---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
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

In a simple cubic graph each line-graph edge lies in exactly one designated original-vertex triangle, and at an original edge the two local contributions to indegree sum to two. Each permutation of (0,1,2) has one orientation and (1,1,1) has two, each weighted z. This gives the nine-state transfer with the stated edge complementation and rail swap at closure. The extreme states 00 and 22 are symmetric singleton blocks of eigenvalue one. The state pairs (01,10) and (12,21) have symmetric/antisymmetric eigenvalues 2z+1 and 2z−1. On (02,11,20) the odd vector has eigenvalue one and the symmetric two-dimensional matrix has diagonal 1,4z² and off-diagonal √2, yielding the stated two roots. Ordinary versus swapped trace gives the two polynomials and their difference. For odd n the odd power is strictly increasing, even across its stationary point, so the root and limit follow; for even n the difference is at least two. At z=1 the dominant eigenvalue is (5+√17)/2 and both traces have coefficient one there, establishing the common entropy when divided by 3n. A separately written exact orientation enumerator with local constraint propagation reproduced the full polynomials by agreement at 2n+1 distinct integer points for both seams at n=3,4,5.

## originality

PASS

The supported distinction is the full vacancy/chirality polynomial and all-z evaluated seam trace. There is actual overlap with the fully packed endpoint and with a known isolated unweighted count, but no inspected covering finite-ladder trace for variable fugacity.

## value

PASS

The two closures share a natural bulk model but not its finite response; the all-length polynomial identifies a nontrivial odd/even reversal as a local vacancy penalty is changed, a precise small-fugacity scale, and a constant unweighted excess. These distinctions depend on the genuinely weighted partition functions, not merely on the existing isolated count, fully packed endpoint, or general transfer method.

The dated certificate retains the supplied scientific assessment, sources and limitations.
