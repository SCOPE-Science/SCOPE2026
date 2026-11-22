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

# Exact checks and boundaries
Run `python3 verify.py` using Python 3 standard library. The program enumerates all 1,441 labelled trees on 2–6 vertices by Prüfer codes and compares independent selected-edge enumeration to a rooted parity-state dynamic program, including sharp tree-type equality and root independence. It directly evaluates 2,142 signed permutation sums for every selected edge subset of every labelled tree on 2–5 vertices and verifies their predicted vanishing pattern. Expected output starts with `PASS 1441` and ends with `2142 exact signed Fourier multipliers`.

The all-order theorem is proved symbolically; no finite experiment is cited as an infinite proof. The nonvanishing input uses the published even-sequence theorem of Celano--Sieger--Spiro, and the remaining tree-rank extremum follows by the displayed independent recurrence inequalities. The code does not establish bibliographic uniqueness, which is evaluated separately in the source comparison.
