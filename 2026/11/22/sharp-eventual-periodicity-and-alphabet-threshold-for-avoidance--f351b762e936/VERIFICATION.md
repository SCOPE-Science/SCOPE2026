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

# Verification record

Two independent Python 3 programs, `verify_direct.py` and `verify_graph.py`, were executed successfully. Both independently calculate admissibility from complete symbol multiplicities, rather than accept claimed counts as inputs. The first exhaustively tests binary lengths through 13 and mixed return-block concatenations of lengths up to four choices. The second enumerates all legal binary five-context vertices and six-letter transitions, checks the exact 12-vertex/10-edge structure, propagates walk counts through length 100, and verifies every edge of each claimed return. The finite-state graph description and the concatenation argument, not the finite test horizon, establish all unbounded conclusions. Asymptotic entropy follows by subadditivity.

Review status: self-reviewed. Independent validation: not performed. No independent certification is asserted. Historical-priority qualification: unindexed calculations could contain an equivalent result.
