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

# Reproduction
Run `python verify.py` in the directory containing `WEIL_TABLE.csv` using Python 3 and NumPy. Successful execution prints `C6_F11_WEIL_69_TYPES_101_CURVES_VERIFIED`.

The program checks irreducibility of each quotient defining polynomial through the multiplicative identity for all nonzero quotient elements; independently enumerates the \(11\)-field rational point counts using two polynomial quotient models at each of four extension degrees; reconstructs and checks the complete degree-eight Hasse–Weil numerators; verifies \(69\) distinct polynomials and their multiplicities, the \(11\)-rank distribution and the unique two rank-zero parameters; and computes the Cartier rank at each of those two parameters.

The finite certificate is exhaustive for the stated \(101\) rational parameter pairs. It is not an assertion about parameters in extensions or an external mathematical audit.
