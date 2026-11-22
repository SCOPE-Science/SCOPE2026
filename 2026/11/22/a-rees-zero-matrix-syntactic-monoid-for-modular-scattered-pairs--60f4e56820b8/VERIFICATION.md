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

Run `python3 check_rees.py` with standard Python 3. For every \(m=2,3,4,5,6,7\), it constructs a finite complete DFA with a sink, enumerates its distinct transformations by BFS under both letters, associates each transformation to the proposed algebraic signature, and verifies all multiplication steps. It reports the respective monoid orders \(34,110,258,502,866,1374\), equal to \(4m^3+2\). Direct enumeration checks all \(8191\) binary words of lengths 0 through 12 for each modulus against the defining language, for a total of 49,146 words checked.

The mathematical claim for every modulus is supported by the four proof steps in RESULT.md: morphism, all-signature realization, two-sided-context separation, and algebraic identification. No finite computation, however extensive, is an exhaustive check over infinitely many moduli or words. Independent expert audit remains unperformed. The program uses no external dependencies.
