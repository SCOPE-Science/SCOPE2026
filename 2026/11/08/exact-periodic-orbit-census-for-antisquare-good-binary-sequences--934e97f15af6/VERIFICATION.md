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

Run `python3 VERIFY.py` using the Python standard library. The code constructs the full five-bit de Bruijn transfer graph from the eight forbidden factors and verifies the exact characteristic polynomial from traces using Newton's identities. It checks the generating-function recurrence against exact graph traces through length 40; brute-force checks all cyclic binary strings of lengths 1–16 (131070 words); independently scans antisquares directly for all length-1–10 cyclic strings (2046 cases); and checks finite Pansiot-code forbidden-pattern equivalence through length 11 (4094 cases).

Actual execution output:

`VERIFY_OK transfer_states=32 transfer_edges=44 matrix_trace_n=1..40 characteristic_polynomial_degree=32 run_pair_formula_n=1..40 mobius_orbits_n=1..40 brute_periodic_words=131070 direct_antisquare_cases=2046 finite_pansiot_cases=4094`

The infinite proof combines an exact cyclic run decomposition with a formal generating-function identity. The finite tests are consistency checks, not a substitute for that proof. No independent mathematical audit has been performed.
