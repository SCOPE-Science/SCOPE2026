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

# Verification method and limits

Run `python3 verify.py` with a Python 3 interpreter. The script uses only the standard library and the coefficient table printed in the source's 2016 Example 3.3.4. It explicitly evaluates every coefficient triple after reduction to the field with nine elements, compares all 45 distinct lines with independently generated secants of the ten rational points of \(x^2+y^2+z^2=0\), and verifies all 91 projective-point multiplicities.

It then checks that Frobenius permutes the 45 lines with nine fixed and 18 conjugate pairs, and confirms that the nine rational lines cover all 13 \(\mathbb F_3\)-projective points with incidence correction 23. The full-form source list is also checked in characteristic 19: its 45 lines meet at 120 triple, 45 quadruple and 36 quintuple points, matching the classical source table. The exact arithmetic output is in `verify_output.txt` and ends in `VERIFY_OK`.

Conic secant incidence identities, the proof of the odd-extension no-extra-point assertion, and the all-extension zeta factorization are given in `RESULT.md`; the finite script does not constitute a substitute for those mathematical arguments. The specialized curve is reduced and no conclusion is drawn about other models or historical priority. Independent audit has not been performed.
