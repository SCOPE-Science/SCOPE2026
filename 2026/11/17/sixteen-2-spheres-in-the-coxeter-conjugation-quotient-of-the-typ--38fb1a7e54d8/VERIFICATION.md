---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-18.md",
      "INDEPENDENT_AUDIT_2026-11-18.json"
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

Frozen exact Z[φ] group traversal code constructs all 14,400 H4 matrices; a separate numerical-rank matrix BFS independently reproduced the 280-element absolute-order interval with ranks (1,60,158,60,1) and rank-two orbit sizes 3 and 5, plus 15-orbits 4+10+4. The inspected exact script checks modular screening followed by exact minor ranks, comparabilities, quotient orbit cells (20,93,90), ∂1∂2=0 and Burnside counts. ABW shellability makes the proper-part complex simply connected; no simplex inversions and C3,C5 stabilizers generating C15 allow Armstrong, hence π1 quotient 0. Euler χ=17 implies H2 free of rank16, and simply connected finite 2-complex Whitehead yields wedge of 16 S². Numerical BFS corroboration is not the exact proof; the exact certificate algorithm was semantically inspected, not blindly relied upon.

## originality

PASS

General H4 noncrossing shellability and cyclic sieving provide the covering sphere wedge and action on elements, but not the orbit-space fundamental group or precise 16-sphere homotopy. Type F4 quotient twelve-sphere classification and B4 torsion example address other Coxeter types. No identified theorem covering H4 quotient; possible unindexed orbit-space computations remain a risk.

## value

PASS

Natural full homotopy classification of a canonical exceptional Coxeter nonfree quotient. The complementary 3/5 vertex stabilizers kill C15, a useful mechanism not implied by noncrossing Catalan counts or unsymmetrized shellability; the exact 16 summands provide a finite benchmark.

The dated certificate retains the supplied scientific assessment, sources and limitations.
