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

The attached `check.py` is standalone Python 3 standard-library code. Execute it from the directory containing the accompanying proof as `python3 check.py`. Its captured genuine output is `check_output.txt`, ending in `VERIFY_OK cases=24 symmetric_cases=15`.

The checker computes \(U_n\) by the signed recurrence for each tested pair, verifies the strong-divisibility consequences and \((u^2-1)b=a+uc\), and computes the Apéry set by Dijkstra shortest paths in each finite residue graph modulo \(a\). It derives the Frobenius number and genus from the full shortest-path residue table and compares symmetry with \(2g=F+1\). For symmetric test cases it checks the respective Frobenius formulas and, where the modulus is small enough, independently recomputes the entire rectangular Apéry set modulo a different generator. The 24 tests include supplementary \(u=2\) boundary cases, though the proved statement has \(u\ge3\).

These are exact finite integer computations; they do not establish the infinite theorem. The parameter-uniform argument is in `RESULT.md`, based on divisibility, unique canonical monomials, the rectangular Apéry criterion, and the three-generator symmetry theorem. Algebraic exponents and all arithmetic checks are interpreted over the integers. No independent external mathematical audit has been performed.
