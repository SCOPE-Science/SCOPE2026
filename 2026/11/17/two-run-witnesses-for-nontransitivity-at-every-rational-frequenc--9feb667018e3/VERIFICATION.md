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

The analytic proof is self-contained after the stated digit-transition rule and uses exact integers; it does not infer infinite behavior from finite samples. The critical assertions are: (i) residual discrepancy after every completed run is between negative denominator and negative one; (ii) the first marker run requires exactly its specified initial zero count, except for one possible shifted imitation; (iii) the modular choice of the second zero count forces that imitation to produce a one-run longer by exactly one.

The standalone Python 3 file `check_marker.py` uses only the standard library. Run `python3 check_marker.py` in the package directory. It constructs the witness for coprime pairs and independently enumerates all reachable transition-rule states, tracking marker occurrences by a prefix automaton. Each test is bounded to 150 symbols, and it verifies witness admissibility and absence of later marker occurrences within that bound. It prints the cases and ends with `All passed` on success. These are finite consistency checks, not an exhaustive certificate of the theorem for all parameters or lengths.

Primary source checks: the exact successor rule, run formula and language closure were read in Reyes (2026), especially Lemmas 2.4, 2.5 and 2.7. No proof dependency relies on the unavailable full text of Becker–Baraviera (2023). Independently replicated checks by other researchers have not been performed.
