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

# Reproducibility and limits

Run `python3 verify_extended_hasse.py` with Python 3 standard library in the same directory. It produces `EXTENDED_CIANI_HASSE_OK` and checks three independently computed degree-\(p-1\) coefficient vectors modulo each prime in \(\{5,7,11,13,17,19,23,29\}\): expansion of the quartic in six monomial types, the transformed classical Deuring coefficient, and expansion of the genus-one quotient's square-completed quartic. This command was executed successfully against the included file.

The finite computations do not establish the universal identity; the mathematical proof derives divisibility at the double-conic parameter, shows degree and leading coefficient, classifies the zeros on smooth fibers by the elliptic quotient, excludes extraneous roots at the two other singular parameters, and uses degree to force the exact boundary multiplicity. Root simplicity and degree-\(2\) extension splitting are classical properties of the Legendre–Deuring polynomial. The argument is confined to prime characteristics at least five and to the displayed natural coefficient extension. There has been no independent mathematical audit.
