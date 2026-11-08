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

# Reproduction and evidence

Run `python3 check_symbolic.py` from the directory containing the included code (requires SymPy). It constructs the nine-state phase-transfer matrix over exact rational polynomial functions, checks the claimed generating function by exact cancellation, then constructs chip-mass coefficients directly from all phase words for sizes 2 through 8. The exact captured output is in `symbolic_output.txt`.

Run `python3 check_states.py` in the same directory (Python standard library only). This independent program directly iterates the threshold dynamics over all chip configurations with each vertex in the range \([0,2d_v-1]\) for sizes 2 through 6; every primitive-three configuration necessarily lies in this range by the interval classification and complement. It computes primitive-three status without using the transfer matrix and checks the full period-three count, both mass supports and complement symmetry. The captured output is in `state_output.txt`.

The algebraic proof in `RESULT.md` establishes the theorem for every \(n\ge2\). The symbolic calculation certifies a finite-dimensional rational identity, not infinitely many individually simulated graph sizes; the exhaustive checks cover exactly their stated finite ranges. The verification does not establish complete historical novelty, all possible periods, eventual basins, or independent validation.
