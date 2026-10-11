---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
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

The published rank-four seed supplies the target disc. Adding any number of Jordan three-blocks and at most one Jordan two-block preserves partial-isometry status, adds exactly the required rank, and does not enlarge the numerical range after the center is restricted so that both centered Jordan discs lie inside the seed disc. The parity calculation gives the stated dimension formula, and zero padding handles larger dimensions. The published low-rank theorem gives impossibility through rank three.

## originality

FAIL

The rank-four seed and the sharp impossibility through rank three are published. Once the rank-four disc is known, the claimed all-higher-rank existence follows routinely from two classical facts: nilpotent Jordan shifts are partial isometries with centered disc numerical ranges, and numerical ranges of direct sums are convex hulls of the summand ranges. Copies of the rank-two and rank-one Jordan shifts can realize every extra rank while their discs sit strictly inside the published seed disc. Under the audit rule that direct corollaries assembled from prior results are covered even without identical wording, the higher-rank half does not clear originality.

## value

FAIL

The threshold is a natural summary, but after the published rank-four seed and low-rank obstruction are known, the higher-rank construction is a textbook direct-sum padding exercise with standard Jordan blocks. It does not introduce a new mechanism or difficult boundary beyond recombining established ingredients.

The dated certificate retains the supplied scientific assessment, sources and limitations.
