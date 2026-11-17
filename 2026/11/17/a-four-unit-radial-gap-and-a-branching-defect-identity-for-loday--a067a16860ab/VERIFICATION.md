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

# Verification procedure
Run `python3 verify.py` from the directory containing this file and `verify.py` (Python standard library only).

The script independently enumerates all plane full binary trees through 11 internal nodes, reconstructs every tree's full Loday-coordinate tuple, checks the fixed coordinate sum, and computes the local branching penalties. It then compares both routes to the squared radius, checks four-divisibility, and tests the exact first- and second-shell counts. It also checks the root's polynomial identity over 2,401 integer pairs.

Expected last line:

`LODAY_RADIAL_QUANTIZATION_CHECKS_PASSED profiles=82499 dimensions=11 algebraic_pairs=2401`

The all-dimensional statement follows from the root polynomial identity and induction given in `RESULT.md`; enumeration through 11 nodes cannot independently certify an assertion quantified over all trees. The previously established canonical vertex description and barycenter are source-dependent inputs. No independent audit has been performed.
