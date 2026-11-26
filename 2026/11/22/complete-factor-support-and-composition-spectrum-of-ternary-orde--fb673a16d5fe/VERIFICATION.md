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

The frozen proof's parenthetical asserting three reciprocal nonself pairs at 000 was inaccurate. The corrected full RESULT.md at /workspace/repairs/3/RESULT.md identifies the two distinct antipodal pairs: {0001,0002} contributes exactly one outgoing edge and {1000,2000} exactly one incoming edge; 0000 is excluded. Thus the claimed unit in/out degrees and zero flow are correct. Every nonzero vertex pair has total outdegree 3 and total indegree 3, so opposite flows justify the 13 coordinates. Each 40-edge support chooses exactly one member of every pair, and a directed Euler circuit exists exactly when the flow vanishes and the nonzero-degree underlying graph is connected. The independently reproduced census used all 27 coordinates, so it did not depend on the reduction. It confirmed 274624 balanced, 218564 connected and 56060 disconnected selections and every row at j=8..19, with no other j. The 13 antipodal pairs beginning with zero force exactly 13 zeros in any realizing word. The repaired text also correctly says that the C++ code Gray-enumerates each half, not just one. No statement, count or code changed.

## originality

PASS

The distinct claim is an exact census of labeled order-four factor supports, including failures of connectivity and composition stratification. It is not a new maximum-period theorem or existence statement. Correcting the degree explanation does not change that claim.

## value

PASS

For the natural maximal order-four avoidance problem the census determines which local balance solutions cannot be realized as cyclic supports and exactly which compositions are possible. Connectivity eliminates 56060 balanced choices; the complete composition table is additional information not implied by one maximizing example or the extremal bound. The proof repair retains this substantive content.

The dated certificate retains the supplied scientific assessment, sources and limitations.
