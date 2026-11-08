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

# Verification

The proof establishes the exact invariant loss-free eigenspace for all integer star degrees and arbitrary positive real couplings and rates. The accompanying `verify_star.py` uses exact integer symmetric amplitude coordinates to construct the full two-boson Hamiltonian without using the proposed incidence projector, then checks that the collision-observability nullity equals the proposed formula. A separate exact rational incidence calculation checks the projector and uniform-pair capture law. The short-time or finite-size checks do not constitute the all-size proof.

To reproduce, execute `python3 verify_star.py` with a Python 3 environment containing SymPy. It should print `EXACT_OK` for each of 13 test cases and finally `STAR_EXACT_ALL_OK`. The tested star degrees range from two through eight leaves; two leaves are a boundary sanity check outside the theorem, while three through eight check the theorem itself. The positive-weight patterns include unit weights and nonuniform small integers. Exact symbolic ranks, inverse Gram identities and diagonal projector entries use rational arithmetic; no floating-point tolerance appears.

The projector yields eventual pair-capture probabilities, not finite-time decay constants. No other hopping graphs, vanishing couplings, on-site detuning, added interactions, or unexamined experimental conditions are covered. Historical priority is provisional and is not established by finite tests or an unsuccessful literature search.
