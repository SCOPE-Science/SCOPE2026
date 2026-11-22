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

# Verification and reproducibility

Run `python3 verify.py` with the supplied standalone Python 3 program. No external packages or network services are needed.

The program generates all ordered full binary trees with up to ten leaves, evaluates the root label, evaluates the preferred-left parity independently by direct traversal and by a two-context recurrence, and checks that the values agree. It verifies all five-leaf witness strings and their labels and parity signatures, exhaustive replacement-context preservation of labels and parity flips through contexts with at most seven leaves, the four-way fringe partition and two-way signed parity cancellation, the exact two- and four-pattern avoidance recurrences, and the quantitative error inequality for each observed colour. It also checks the proper-colouring condition against all single rotations in trees with up to eight leaves.

**Mathematical verification.** The all-order proof requires the quasigroup-bijection step, the first-fringe-occurrence selection argument, the two-context parity calculation, the exact avoidance generating function and the positive-coefficient analytic estimate. The finite tests corroborate these steps; none is an infinite certification. Source priority has only been checked against available literature and records; independent auditing has not been performed.
