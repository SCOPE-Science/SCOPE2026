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

# Reproducibility and proof limits

The complete proof is given in RESULT.md. To independently reproduce the finite checks, run `python3 local_checker.py` using only the Python standard library. Its output was recorded in `local_checker_output.json`.

The checker directly evaluates \(F=x^3+y^3+z^3-3xyz\) for every ordered residue triple at 18 selected prime-power moduli, including moduli \(3,9,27,81\), and confirms the exact local counts. At each of the first three transitions in the ternary tower, it enumerates the lower-level solutions and checks whether they admit an upper-level lift; the observed fractions are exactly one third.

Finite enumeration is not an infinite-level certificate. The infinite-level theorem relies on the explicit expansion \(F(1+3a,3b,3c)-1=9H(a,b,c)\), the unit derivative of \(H\), and the full lift-fiber calculation. Results for additional target norms or other prime powers of three are not asserted. No independent mathematical audit has been performed.
