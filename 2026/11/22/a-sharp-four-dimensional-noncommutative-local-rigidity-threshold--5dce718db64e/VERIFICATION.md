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

# Reproducible mathematical checks

Execute `python3 verify.py` using a Python 3 installation. No external packages are required. The program uses finite-field row elimination over \(\mathbb F_2\), \(\mathbb F_4\), and \(\mathbb F_8\), with explicit irreducible moduli, and builds the full linear derivation constraint system from the multiplication tensor.

For each of the two-dimensional reference algebra and four-dimensional indecomposable witness it computes the ordinary derivation kernel and the complete linear pointwise-locality kernel from **every** vector of each tested finite field. The two-dimensional reference is a control, not a claimed original result. In the four-dimensional witness it tests the nondegeneracy of the multiplication matrix and reproduces the equal dimensions \(5\) and \(5\). It also checks directly that the proposed square-scaling derivation exists for each of the \(8\), \(192\), and \(3584\) noncommutative two-by-two multiplication matrices over these fields.

The exact checker transcript is `verification_output.txt` and must end with `VERIFY_OK`. These exhaustive checks do **not** prove the theorem over arbitrary characteristic-two fields; the symbolic derivation identities and pointwise spanning argument in `RESULT.md` provide the all-field proof. They likewise do not certify mathematical priority or supply independent review.
