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

A shared one-coordinate gives at most four differing reads, hence admissible supports are disjoint. For two disjoint supports the number of differing reads is eight minus the number of cycle edges internal to their four occupied coordinates. Among k disjoint supports there are at least 4k−n fully occupied edges, and at most binomial(k,2) for k≥3: there is at most one transition per unordered label pair; an internal occupied edge isolates its label from any other, so that case gives at most 1+binomial(k−1,2). These exclude three words at n=7,8 and four at n=9. The same edge count for four points or the bound d_p≤n proves the shorter exclusions; the small witnesses satisfy the ordered-pair threshold. For n=2k≥10 every occupied position in the tour construction has a unique label, and a simple 4-regular connected graph's tour uses each label twice. Inserting a common zero destroys, but cannot create, occupied adjacencies. Conversely at even equality the entire cycle is occupied; a loop would have an adjacent edge to another label, and repeated undirected edges would violate the two-label condition. Thus the sequence gives a connected simple 4-regular graph and an Euler circuit. Independently encoded each read as 2x_i+x_{i+1} and used exact compatibility-clique recursion max(C(S−v),1+C((S−v)∩N(v))); this gave 1,1,1,1,1,2,2,3,5 for n=2 through 10. The proof is unbounded; the frozen verification report and script were inspected, not rerun.

## originality

FAIL

The earlier distinct Resultary record d90c6eb8b504 states both the same all-length binary exact-Hamming-weight-two d_p≥7 maximum (including every short cutoff) and the same even n≥10 iff Euler-tour characterization. It also goes further at n=10. This is exact coverage of both central claims, not a literature-access or bibliographic uncertainty. The comparison with Zhao–Chang is not needed to establish the failure.

## value

FAIL

The sharp cutoff and optimizer correspondence would be useful for sparse pair-channel codes as unknown facts, but the frozen Finding delivers exactly the previously available theorem. It adds no independent count, excluded class, boundary or structural consequence; replaying the same extremal function and correspondence is not a new scientific contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
