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

For any nonzero periodic solution, if no zero occurs then x_t−x_(t−1)=1 and all residues are visited: contradiction. Rotate so x_(N−1)=0. The nonzero mask b_j must have weight divisible by 3 and completely reconstructs x_j=Σ_(i=0)^j b_(i−k) mod3. Mask equality, exact primitivity, and nonlinear recurrence are necessary and sufficient; hence enumerating all nonzero binary masks, all 1<=N<=22 and each k modN is exhaustive for the FINITE claim. Independently implemented exact C++17 enumeration processed 176,160,517 masks, finding only (4,2),(4,3),(9,4),(9,6),(19,5),(19,15),(22,8),(22,15), with 1,1,3,3,7,7,7,7 zero-anchored words, each one cyclic orbit. This does not classify longer periods or basins.

## originality

PASS

Finch 2026 and its older distinguished-seed table contain period-four classification and observed periods 9,19,22 for special seeds; Resultary Nov 2 establishes only the all-seed gap below 10 and nine-cycle uniqueness. No checked source yields the complete 1..22 all-initial-condition, all-delay orbit-uniqueness census. Best-of-knowledge PASS retains explicit unavailable full-text priority risks.

## value

PASS

The exact cutoff follows the first four actually observed attainable primitive lengths 4,9,19,22 in a naturally studied nonlinear ternary lag recurrence, not a contrived single instance. A full all-seed and all-lag classification through 22 excludes entire intervening period ranges and fixes unique orbit geometry, useful as a rigorous boundary for later basin/large-period work even without a global theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
