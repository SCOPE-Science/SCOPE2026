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

The proof classifies all nonempty finite tournaments in counting-free first-order logic with two reusable variables, without a quantifier-depth bound. The critical checks are: (i) source/sink peeling yields unique head/tail chains and a nonempty source-free, sink-free core when the tournament is nontransitive; (ii) the recursively displayed formulas \(\sigma_r,\theta_r\) use only two variable names and identify the respective peeling positions; (iii) a two-pebble response can always be found inside the core from both directions because every core vertex has both an in- and an out-neighbor there; (iv) all head/tail pairs of the allowed sizes are realized by attaching transitive chains to a core of arbitrary order at least three; and (v) at minimal order, the only possible core is a directed triangle.

`verify_tournament_fo2.py` compares 1,699 finite tournament models by simultaneous set-valued two-variable type refinement, and crosschecks the exact peeling invariants. Expected output: `verify_tournament_fo2.out`.

`verify_tournament_pebbles.py` computes greatest fixed points of legal two-pebble positions, with moves in either structure, for 157 pairs of finite tournaments. Expected output: `verify_tournament_pebbles.out`.

Run the programs independently with Python 3. They have no external dependencies and are finite corroborations, not exhaustive checks of all tournament orders or proofs of infinity. No independent mathematical audit has been performed. Historical priority cannot be established by negative search results alone.
