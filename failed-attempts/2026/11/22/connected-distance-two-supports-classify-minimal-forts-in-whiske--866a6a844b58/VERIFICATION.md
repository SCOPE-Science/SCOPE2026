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

Each selected core forces inclusion of its mate in a fort; an unselected core's mate is required with one selected core neighbor, forbidden with zero, and removable with at least two. No nonempty fort has empty core support. In a tree, three fort neighbors at an outside vertex allow an entire branch to be dropped. Once there are at most two, retaining one component of the two-step link graph requires no new mates and gives a smaller fort if the graph is disconnected. Conversely, any subfort's support must take both ends or neither across each link since the middle core's mate is absent, so connectedness proves minimality. On a path the supports are contiguous length-k parity runs; their weights are 2k plus the number of ends that do not touch a core endpoint. For even n the two maximal parity runs each touch one endpoint; for odd n one maximal run touches both endpoints and the other touches neither. They give the only size-n+1 forts. Singletons at endpoints give the only size-three forts; endpoint intervals and interior intervals realize the intervening odd and even weights. The total is the sum of interval counts over the two parity classes. Each nonempty A gives a distinct fort. Independent replay: python3 /workspace/review_checks.py 1 tests the defining neighbor condition and proper containment on all labelled cores through order 5 (1,1,3,16,125 trees) and combs through order 8, with exact families and comb coefficients; the finite check is not the proof.

## originality

FAIL

Cameron–Li Theorem 3.3 on arbitrary trees directly yields the main characterization. The link graph is the suppressed alternating subtree allowed by their cut condition, and the comb polynomial and size claims are mechanical counts of intervals in its two parity classes. This is demonstrated prior coverage, not a failure to find the same polynomial in print.

## value

FAIL

The corona coordinates are convenient, but the only residual results are the direct interval count on a path and a union-of-forts lower bound. They do not supply a distinct structural or extremal result beyond the covered characterization. The rejection is not a correctness objection or an objection to the graph family itself.

The dated certificate retains the supplied scientific assessment, sources and limitations.
