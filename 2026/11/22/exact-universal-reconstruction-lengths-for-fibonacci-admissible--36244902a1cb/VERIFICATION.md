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

# Verification of the all-length reconstruction criterion

The exhaustive finite certificate is independently realized in `verify_windows.py` (direct window sums) and `verify_correlations.py` (prefix-lattice difference autocorrelation). The former visits every binary word satisfying `11` avoidance by recursive generation; the latter visits all binary tuples then filters. Both partition the finite domain by complete exact integer observations. The three special lengths give counts of admissible words \(55,233,1597\); fiber counts \(30,127,826\); and, in both implementations, no fiber outside its reversal orbit.

`verify_construction.py` checks admissibility, word length, distinctness, nonreversality and complete observation agreement for 88 factorizable test lengths below \(150\). This third check is explicitly finite: the proof that all remaining lengths possess such witnesses is the integer factor lemma and interleaving identity in `RESULT.md`, not an inference from the loop bound.

Reproduction: `python3 verify_windows.py`; `python3 verify_correlations.py`; `python3 verify_construction.py`. All run with the Python standard library and do not require external data, solvers, network access or cached state. No independent validation has been carried out.
