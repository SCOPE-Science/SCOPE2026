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

For m,n>=3, every two-cell set lies inside a row-column cross and is not total dominating, while precisely the distinct-row/distinct-column triples are minimal; count 6 C(m,3) C(n,3). A product-edge slide changes both coordinates and must place the moved cell in a previously unoccupied row and column: each of three selected cells has (m-3)(n-3) choices. If min(m,n)=3 this freezes all states. At (4,4) completing the matching to four pairs partitions 96 states into 24 K4. For min>=4,max>=5 three explicit legal slide templates implement generating row/column exchanges, connecting all partial matchings; one-coordinate jumps with spare slots connect all n,m except (3,3). Independently generated state graphs for (3,3),(3,5),(4,4),(4,5),(5,5) and obtained predicted degrees/components; direct_check.py and matching_check.py source inspected. The infinite result rests on the written templates, not finite enumeration.

## originality

PASS

Best-of-knowledge slide-configuration mobility phase diagram for the categorical product, not the previously known minimum total domination number or minimal-set polynomial. The all-size minimum triples are explicitly credited to published direct-product total domination work; Kazemi cross-product work and same-day complete minimal-set census do not give constrained one-edge token-slide components or the (4,4) obstruction. Other token-slide literature concerns independent sets, identifying codes or different graph products. No matching general reconfiguration theorem observed.

## value

PASS

A natural mobility invariant for minimum total-dominating configurations has a genuine sharp 3/4/5 spare-coordinate transition, an exceptional 24-component critical case and exact regularity. Unlike merely counting known minimum sets, the edge-adjacency constraint creates structural dynamics and a useful constructive connectivity classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
