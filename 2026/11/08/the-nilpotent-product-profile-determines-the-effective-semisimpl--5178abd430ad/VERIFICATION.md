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
# Verification

The symbolic proof in `RESULT.md` establishes the assertion for all finite nonzero unital associative rings. Its externally established premises are nilpotence of the Jacobson radical, the Artin–Wedderburn theorem, and the finite-field nilpotent-matrix count. The arguments for uniform quotient sampling, random products, and the asymptotic reconstruction are explicit there.

The standalone `verify_nil_product.py` (Python 3, standard library only) independently enumerates ring elements and their products using exact modular arithmetic, tests nilpotence by iterated matrix multiplication, and computes counts for product lengths up to four via multiplication histograms. It directly checks nine small ring presentations (full and triangular matrix rings) for 31 exact combinations and one product ring for four combinations. It compares each independently calculated count with the claimed formula, without using the formula to build its histogram.

Reproduce with `python verify_nil_product.py` in a directory containing the program. Expected final output: `VERIFY_OK: 9 directly enumerated rings and 31 matrix-ring tests, plus 4 directly enumerated product-ring tests`. A complete recorded transcript is embedded as `verification_output.txt`.

Examples include \(p_2(M_2(\mathbb F_2))=7/16\), \(p_2(M_3(\mathbb F_2))=15/64\), \(p_2(\mathrm{UT}_2(\mathbb F_2))=9/16\), and \(p_2(\mathbb F_2\times M_2(\mathbb F_2))=21/64\). These are tests, not an exhaustive proof of the universal theorem. No independent mathematical audit or certification has been carried out.
