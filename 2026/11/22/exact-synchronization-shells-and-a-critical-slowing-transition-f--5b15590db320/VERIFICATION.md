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

# Reproducible verification

Run the two standalone standard-library programs with `python3 verify_direct.py` and `python3 verify_formula.py` from the package root. The saved `verification_output.txt` is the concatenation of their standard outputs, in that order.

`verify_direct.py` independently constructs every incoming word-overlap neighborhood, applies synchronous NOR to every input bitmask for eight instances (all with at most sixteen vertices), and checks first periodic-entry populations against the claimed integer recursions. It also checks that every orbit has entered the uniform two-cycle by the asserted upper bound and that an extremal initial condition exists.

`verify_formula.py` enumerates complete Boolean NOR-tree truth tables separately from graph dynamics, and checks Bernoulli\((1/3)\) cumulative probabilities for the binary depth-three graph by exact rational weighted enumeration of its 256 labelled inputs.

The programs were executed against the content shipped here. They test the particular finite instances only. The proof for arbitrary word length and alphabet size, and its asymptotic probability statements, do not follow from these finite checks alone; their analytic arguments are given in `RESULT.md`.
