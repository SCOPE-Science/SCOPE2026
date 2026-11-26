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

Every private leaf forces either itself or its support into a dominating set, so each support is internally dominated even after adding bridge edges; all other vertices have only internal neighbors. Restricting to blocks and taking unions are inverse size-preserving maps. The joining tree on connected blocks makes a connected simple graph. Independently partitioning dominating sets of the 36-edge seed by the subset of its 17 nonleaf vertices reproduced all 23 nonzero coefficients, D(-4)=0 and D'(-4)=1100417597440000. Replay: python3 /workspace/branches/independent-checks/check_domination.py with the frozen package directory as input. The K2 and P3 factors evaluate to 8 and -20, so multiplicities add to exactly k. Every integer at least 2 is a sum of 2s and 3s; the proof does not cover order 33k+1 or claim optimality of the minimum order.

## originality

FAIL

No explicit statement of the combined family was located, but the full quantifier range and polynomial product are a mechanical corollary of the cited irrelevant-edge theorem and the cited 33-vertex seed. The new-looking order and exact-multiplicity parameters introduce no additional graph-theoretic step.

## value

FAIL

The connectivity and multiplicity questions are motivated, but this particular family follows by unconditional application of the known irrelevant-edge criterion to the already published seed, with K2/P3 padding and elementary parity. There is no new obstruction, seed or threshold result; for example the skipped order 33k+1 is not shown impossible. The correct immediate corollary is useful exposition but does not add a distinct scientific result at the stated standard.

The dated certificate retains the supplied scientific assessment, sources and limitations.
