---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification
Run `python3 check.py` with Python 3 (standard library only) from the directory containing the file and compare the deterministic JSON output with `expected_output.json` byte-for-byte.

The script enumerates all simple base graphs on two, three, and four vertices with edge \(\{0,1\}\), and additional seeded samples on five and six vertices. For each case it enumerates the complete matching complex of the two-endpoint-unwhiskered graph, checks the specified two-stage pairing for legality, verifies the entire oriented nonempty Hasse diagram has no directed cycle, compares critical cells with independent perfect/near-perfect matching counts, and calculates all mod-two homology via exact boundary reduction. For even orders it also builds the proposed integral cycles, verifies every alternating boundary is zero and checks the unit top-face pairing matrix. It also explicitly checks the augmented empty-face pairing with the original edge. This tests finite instances only; the written symbolic proof, not the sample, is the all-graph argument.

The universal integer primitive inclusion is justified by the symbolic unit pairing matrix between explicit integral cycles and maximal-face cocycles; the finite integer cycle tests corroborate this step but do not certify arbitrary graph order. Full-text priority comparison has residual access and indexing limitations. There has been no independent mathematical audit.
