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

Run `python3 verify.py` with Python 3 and no external dependencies. It regenerates all sixteen labelled vertices, the 1,820 four-point determinants as integer polynomial coefficient dictionaries, the two isolated rigid maximizers, the six movable-apex base quadruples, and coefficientwise inequalities for the remaining 1,812. It also verifies all possible symbolic equality collapses at the first-parameter boundary and independently compares the formula against exact numerical enumeration for 72 parameter triples. Successful replay: `PARKING_TETRA_EXACT_PASS symbolic_quadruples=1820 coefficientwise=1812 rigid=2 facet=6 sample_parameter_triples=72 zero_first_checks=5`.

The continuous parameter result follows from exact polynomial inequalities, not from the 72 numerical cases. Nonvertex equality is deduced analytically from determinant multiaffinity and equality-orbit intersection patterns. The general vertex description relies on the published primary source, and historical priority remains provisional. Independent audit has not been performed.
