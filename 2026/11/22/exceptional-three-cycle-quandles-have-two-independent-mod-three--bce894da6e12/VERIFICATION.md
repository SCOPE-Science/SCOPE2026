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

For right conjugation the four signed normalized boundary terms in RESULT.md are correct and cancel under d2 by self-distributivity. I independently generated oriented support triples, computed conjugation by relabeling through the inverse of the acting cycle, and removed a directed spanning tree of pair coordinates. On its span d2 is an isomorphism onto the augmentation-zero subgroup, so projection to non-tree pair coordinates identifies ker(d2) with a space of dimension 1521 or 4761 (and preserves d3 rank). Exact elimination over F2 and F3 over all 60840 and 333270 normalized triples gave d3 ranks (1520,1519) and (4761,4759), with the n=5 control giving (360,360). Replay: python3 /workspace/checks/1.py 5 6 7; complete output /workspace/checks/1.txt. The frozen checker and CHECK_OUTPUT were inspected, not executed. The finite connected injective quandle finiteness theorem and torsion-free H1=Z justify interpreting the mod-prime dimensions as counts of p-primary summands, not as torsion exponents.

## originality

PASS

Bounded pass for the four exceptional normalized coefficient ranks, not for the general method, Schur multipliers or the n=5 control. The directly relevant odd-cycle theorem explicitly omits these cases.

## value

PASS

The two degrees are singled out by exceptional Schur multipliers and by an explicit gap in the general k-cycle classification, not by an arbitrary size cutoff. The exact 2- and 3-primary generator counts constrain future integral calculations in both exceptions and distinguish their 2-primary behavior.

The dated certificate retains the supplied scientific assessment, sources and limitations.
