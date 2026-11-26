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

The six pivot lines together with the anticanonical vector form a unimodular Picard basis, so projecting onto the other 21 coefficients gives integral kernel coordinates. I generated the double-sixes by the skew-row and complementary cross-incidence conditions, rather than by the stated roots. This yielded 36 supports, each summing to 4(-K), and the sorted 21-column minor had determinant -65536. Integer Smith reduction gave 1^6,2^14,4, and Smith reductions of the augmented coinvariant presentation agreed for all eleven partitions. The pair map has the stated mod-two rank 15, annihilates the double-six columns and is equivariant by its index formula. The coefficient sum modulo four descends because 12 is divisible by 4, is invariant, and is onto because one kernel vector has odd sum. It forces one order-four summand to survive in every coinvariant quotient; there cannot be a second since 2Q has order two. Mod-two coinvariants and the pair-orbit count give the remaining summands. The arithmetic proof uses only the induced S6 action of the stable sextuple; it does not assert that every partition is realized over each field. Independent replay: python3 /workspace/branches/reproductions/double_sixes.py (SymPy 1.14.0).

## originality

PASS

The underlying abelian group is prior work. The supported distinct result is the S6-equivariant pair-module identification together with its uniform integral coinvariant consequence. The closest inspected material does not supply the module identification or calculate this arithmetic invariant.

## value

PASS

The explicit module map explains, for every stable sextuple, why only orbits on pairs determine the surviving number of cyclic factors, while a four-torsion obstruction always survives. This is a useful arithmetic refinement of a naturally motivated integral reconstruction obstruction, not just another calculation of the geometric index or a table of Smith forms. It does not identify Q with Picard or Brauer torsion or extend the classification to general W(E6) actions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
