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

# Verification notes

The theorem is proved for the infinite admissible family in `RESULT.md`. The central neighbor-count identity and Cauchy--Schwarz equality case are exact algebra; their correctness does not depend on finite enumeration.

For computational cross-checking, run `python3 check_kg_majority.py`. The program requires only Python 3's standard library; it uses a fixed random seed. It enumerates all 1,024 states of the five-point example, then independently evaluates the neighbor-count formula and direct majority on five sample graph orders, using 7,500 deterministic pseudorandom cases. For the 1-modulo-four cases it constructs and checks the explicit cyclic half-regular witness. The resulting output is in `checks.txt`.

These checks are not an exhaustive test for graph orders eight or larger and do not constitute an independent external audit. Originality comparison is based on inspected accessible literature and available records rather than proof of historical uniqueness. No claim is made about primitive two-cycles or the remaining residues.
