---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-10.md",
      "INDEPENDENT_AUDIT_2026-11-10.json"
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

In cubic GP(n,2), for a 1-limited dominating D, counting cut edges yields |V\D|≤|E(D,V\D)|≤|D| hence |D|≥n. Both full shores attain n. Equality is equivalent to exactly one crossing edge incident at every vertex, i.e. perfect-matching cut vertex bipartition. The 256-state four-column shift graph has only cyclic SCCs of sizes 1,1,5,5 with deterministic internal edges, proving 2+10*1_{5|n} minimum-set colorings and 1+5*1_{5|n} unordered cuts. Independently reconstructed all 256 states and 160 valid arcs and cyclic SCCs.

## originality

FAIL

FAIL: An earlier Nov2 full published classification of every perfect matching cut of GP(n,2) counts exactly 1+5*1_{5|n} cuts and 2+10*1_{5|n} labeled vertex colorings, including precisely the two constant and period-five patterns. Elementary inequality |D|≥n and equality=cut is already established general theory. Thus Nov8 1-limited minimum-set census is a direct restatement/consequence of an earlier complete theorem.

## value

FAIL

FAIL as a new finding because all solutions and their cardinalities are already enumerated for this exact infinite GP(n,2) family; the invariant change from cuts to 1-limited domination adds only a short known equality equivalence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
