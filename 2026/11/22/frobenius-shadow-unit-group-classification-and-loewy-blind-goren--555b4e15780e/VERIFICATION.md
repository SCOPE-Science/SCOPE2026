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

# Direct reproducibility checks

Execute `python3 verify_units.py` with the Python 3 standard library. The checker performs the following direct finite computations rather than treating a log as a proof:

- Complete direct polynomial-multiplication tests for all \(128\) principal units of \(\mathbb F_2[x,y]/(x^2,y^4)\), all \(32\) of \(\mathbb F_2[x,y]/(x^2,y^3)\), and all \(243\) of \(\mathbb F_3[x,y]/(x^2,y^3)\). Their predicted elementary-divisor multiplicities and cumulative order distributions agree.
- Direct multiplication power tests on independent random coefficient samples of size \(80\) in each of the two characteristic-three collision rings.
- Full enumeration of each of the two \(177147\)-element principal-unit groups over \(\mathbb F_3\) via independent coefficientwise Frobenius support, giving exact order histogram \(1,59048,118098\) for orders \(1,3,9\).
- Checks of the collision formulas for primes \(3,5,7,11\) and extension-field degree \(2\), and an additional nonrectangular standard-monomial set.

The script finishes with `PRINCIPAL_UNIT_COLLISION_VERIFIED`. Direct multiplication samples and full Frobenius-supported counts are finite corroboration only. The unlimited prime, extension-field and monomial-ideal assertions are deduced from the explicit algebraic proof in `RESULT.md`.
