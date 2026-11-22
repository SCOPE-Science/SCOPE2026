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

# Verification of the alternating parity state count

The supplied programs run with the Python 3 standard library. From the directory containing the extracted files, run `python3 check_literal.py` and `python3 check_states.py`. Their exact captured stdout appears in `check_literal.out` and `check_states.out`.

`check_literal.py` enumerates every binary word through length 12 (8,191 words) and every alternating-pattern length 1–12, counting positional embeddings directly by index combinations, and compares 98,292 outputs to the proposed cyclic machine. `check_states.py` separately builds the full prefix-vector automaton by deterministic recurrence and enumerates its orbit for lengths 1–90; it checks 12,372 labeled transitions, 510 relevant cyclic periods, and performs Moore partition-refinement minimization on all reachable states (6,186 states in total over the parameter sweep).

The formal all-length argument is the generalized-binomial reflection identity; its congruence modulo powers of two; reachability using `(01)^s`; and the Lucas-mask output's exact cyclic period, yielding distinguishability by common suffixes. Each of these four logical steps is required. Finite enumeration cannot substitute for the infinite proof and neither a timeout nor a lack of sampled counterexamples is a theorem.

**Scientific limits:** This covers only the parity-output machine for alternating binary patterns. Historical priority remains uncertain where accessible full literature is lacking. Independent audit and independent expert validation have not been performed.
