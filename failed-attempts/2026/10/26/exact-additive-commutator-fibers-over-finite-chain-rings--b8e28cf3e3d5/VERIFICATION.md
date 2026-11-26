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

Removing a scalar diagonal from each matrix leaves three independent coordinates; the target trace-zero coordinates are the three signed wedge minors. There is no division by two, and the scalar lifts contribute q^(2m). In dimension three the exterior-square action of SL_3 on the dual of R^3 is the inverse-transpose action using the volume form. A primitive vector completes to a basis, whose determinant can be corrected by scaling a different column, so each target valuation has one orbit, even for targets π^s times a primitive lift. Use h=π^s e1∧e2. For first factor u of valuation a<=s divide by π^a in R/(π^(m-a)); primitives in the quotient extend to a basis, so the wedge image is exactly the two-forms which wedge to zero with the divided primitive u. This condition is π^(s-a) times its third coordinate equal to zero, giving q^(s-a) choices there, all nonunits, and q^(2(m-a))-q^(2(m-a-1)) choices for the first two coordinates. The image has q^(2(m-a)) elements and each fiber q^(m+2a). Summing gives the stated nonzero count; for h=0 all vectors are eligible, with the zero first vector giving q^(3m) choices. The formulas are positive for every trace-zero target and all other targets are excluded by the trace identity over a commutative ring. The frozen checker is a bounded cross-product test, not an independent matrix multiplication or a proof at general q,m. The independent check python3 -B /workspace/reproduce_finite.py 2 exhausts 65,536 literal ordered matrix pairs in each of Z/4, F2[epsilon]/epsilon^2 and F4, including non-trace-zero targets and nonprime residue size. All counts agree; zero fibers are 6400, 6400, and 5056. The frozen checker was not run.

## originality

FAIL

The inspected distinct Resultary record proves the exact zero-wedge count at every depth, including all quotient rings, using the same signed-minor model and invariance under changes of basis. Taking differences of successive congruence counts and dividing by the cardinality of the target valuation orbit recovers the entire nonzero formula. Thus the result is covered by a mechanical implication, though the comparator is later-dated and does not explicitly state all the nonzero fibers. This is not a ruling on historical priority.

## value

FAIL

A mixed-characteristic distribution for additive matrix commutators is a natural invariant, and its profile could be useful in place of mere surjectivity. Here the exact profile is a mechanical re-expression of verified all-quotient determinantal counts via uniform lifts and valuation orbits. No mathematically distinct exact invariant remains in this narrow claim; the alternate direct wedge count is not a substantive surviving result on its own.

The dated certificate retains the supplied scientific assessment, sources and limitations.
