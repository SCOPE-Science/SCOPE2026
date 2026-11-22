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
# Verification record

The supplied `checker.py` uses only the Python standard library and constructs a generic insertion-based greedy-subsequence automaton, independently of the three-gap deletion-witness argument. Run `python3 checker.py` from the directory containing the files. It checked 455 triples of nonnegative zero gaps with total at most 12 and compared all shortest distinguishing insertions against the claimed formula. It also checked 368 polynomial coefficients for 16 height thresholds and 23 zero counts. Expected terminal output: `PASS exact_generic_insertion=455 polynomial_coefficients=368`.

The infinite polynomial identity follows from the zero-/one-/two-marker witness classification and a disjoint status enumeration; the checker alone does not establish it. The limit theorem follows from convergence of uniform weak three-part compositions to the standard 2-simplex and exact inclusion-exclusion, not from a simulation. Independent audit is not yet performed.
