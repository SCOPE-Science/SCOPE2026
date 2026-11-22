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

# Reproduction and boundaries

Use `python3 verify_93.py` to check the 176 normalized incidence completions, their cycle-type isomorphisms to the three representatives, the 512-input one-shore transition tables, algebraically sufficient iterate identities, phase weights, basin formulas and exact sharp-transient witnesses. The script uses only the Python 3 standard library. This run produced `PASS`.

Separately use `g++ -O2 -std=c++17 check_full_states.cpp -o check_full_states` and then `./check_full_states` to enumerate 262144 full configurations for *each* of the three explicitly encoded incidence graphs. The independently written functional-graph calculation yielded period-one orbit counts 98, 96 and 92; period-two orbit counts 4753, 4560 and 4186; maximum entry times four, four and three. It ended `PASS all 786432 states`.

No previously generated output or external dataset is an input to either checker. The finite verification establishes exact facts for the three listed graphs. The generalization from these calculations to every isomorphic labelled copy follows from graph-isomorphism invariance, not numerical extrapolation. There is no independent external audit.
