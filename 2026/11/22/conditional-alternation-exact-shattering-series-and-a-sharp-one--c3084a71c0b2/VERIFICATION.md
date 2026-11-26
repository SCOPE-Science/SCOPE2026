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

The forbidden-factor DFA follows from the four proper-prefix suffixes. A state set is exactly the set of possible suffix states for one queried trace. Free positions union the two possible images, whereas selected positions create two separate branches. Inclusion is preserved by both images and their unions; retaining only minimal state sets therefore preserves the existence of a trace with no completion, at every subsequent indicator prefix. The complete 14-state table and each potential inequality were rebuilt and checked independently. In a second calculation retaining all state sets and storing actual suffixes of length at most two rather than proper-prefix masks, there were 18 reachable nonrejecting states and five nonrejecting equivalence classes; the exact rational resolvent and potential bound agree. Equivalently, in the printed table let X be the continuation series at state 0, Y at 2, and w=tz. States 0,1,3 have the same series; 2,4,11 have the same series; the pairs (5,12), (7,9) have the same continuation series by their zero loop and shared transitions. The recurrences give X=(1+wY)/(1−t), Y=[1+w(1+t−t²)]/[1−t−wt²(2−t)], verifying the fraction identically. Each allowed step has 3s−1≤D_i−D_j, so 3k−n≤4. The state 6 after 11 runs through 8,11,13 upon reading 001, and 13 repeats that loop; zero through two padding zeros are legal after any such prefix, including 11. These attain the sharp bound in all three residue classes from length two, with n=1 established by the initial transition on 1 and n=0 by the empty support. A separate direct trace enumeration through n=9 confirmed the computation and coefficients. The 14-state presentation need not be minimal, and no minimality is claimed.

## originality

PASS

The supported precise gap is the explicit support enumerator and sharp finite-length maximum for the two-factor language 000/011, not the general idea of regular-language recognizability, transfer matrices, or VC dimension in symbolic dynamics. Nearby exact support enumerators change the forbidden set, and broader independence entropy addresses a different quantifier. No equivalent formula or mechanically dominating inspected result was found for this fixed pair.

## value

PASS

This is a natural low-memory constrained family whose use of adaptive completion makes individual local forbidden-pattern checks insufficient to count or maximize shattered supports. The exact one-third law with its finite-boundary correction distinguishes it from nearby length-three constraints, and the coefficientwise result and explicit support automaton delimit the full feasible coordinate sets, not just a handful of examples or a generic regularity theorem. These are directly usable as exact comparisons in classifying the behavior of small forbidden-factor languages.

The dated certificate retains the supplied scientific assessment, sources and limitations.
