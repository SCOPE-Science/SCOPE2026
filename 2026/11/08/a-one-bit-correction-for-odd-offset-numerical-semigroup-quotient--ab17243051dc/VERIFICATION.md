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

The exact-integer script `verify_exact.py` independently constructs shortest paths for all residue classes of the original semigroup modulo its least generator, then restricts to multiples of the quotient divisor to get the Frobenius number. It compares this value to the closed formula for 125,586 parameter tuples in the indicated ranges and prints the number of cases in the odd-remainder branch and those with positive corrections.

To reproduce, run `python3 verify_exact.py` and compare standard output with `verification_output.txt`. All computations use Python integers and a standard-library heap implementation, with no nonstandard dependencies. The proof of the infinite claim is the mathematical derivation in `RESULT.md`; the verification range does not certify an infinite statement. Literature searches do not guarantee novelty, and independent review has not been performed.
