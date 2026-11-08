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

# Verification of the fixed-step anti-Niven construction

Run `python3 verification/check_anti_niven.py` with standard Python 3; there are no external dependencies. The script checks ten odd bases, including composite \(9,15,21,25,27,33\), and checks CRT local admissibility for every prime up to the chosen finite cutoff, the two-level low-digit identity, and the modular conditions for every term. For bases \(3\) and \(5\), it builds the actual separated-digit integer, computes the full digit sums of the enormous progression members and verifies all gcds. Expected terminal message: `VERIFY_OK bases=10 complete_literal_bases=2 modular_checks=10`.

The infinite proof depends on the following elementary facts, each proved in `RESULT.md`: (i) for every odd base and each prime \(q\le U\) there is a residue for \(P\) making both \(P\) and \(P-(b-1)\) nonzero modulo \(q\) and compatible with the base constraints; (ii) CRT yields arbitrarily large such \(P\); (iii) the multiplicative order of \(b\) modulo \(PQ\) exists; and (iv) the explicit sums of powers have disjoint digit positions. Finite tests alone do not prove these universal steps.

The theorem does not determine the odd-base maximum length, the smallest possible start, or existence for general differences.
