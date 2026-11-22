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

# Reproduction and limits

The exact geometric incidence matrix is \(35\times28\), with a row for each unordered four-four partition of the eight Cayley-octad labels and a column for each unordered two-label bitangent. An entry is one precisely when both labels of that bitangent lie in the same half of the partition. This follows from the standard theta-refinement criterion for Steiner complexes.

For exact reproduction, place `verify.py` and `certificate.json` in the same directory, and execute `python3 verify.py certificate.json` (Python 3, standard library only). The verifier enumerates every row and column, checks two equivalent constructions of the entries and their row and column sums, computes the full Gram matrix, verifies the seven rational kernel witnesses, checks adjacent-transposition equivariance, and applies all \(474\) elementary integer operations from the certificate to the original matrix. It checks that the result is exactly the rectangular diagonal matrix with nonzero factors \(1^{\times7},2^{\times13},6\), followed by seven zero diagonal factors. It also verifies ranks modulo \(2\), \(3\), and \(5\) are \(7,20,21\), respectively.

All recorded elementary operations are invertible over \(\mathbb Z\); their exact replay proves the claimed Smith form independently of any floating-point calculation or experimental extrapolation. The rational-kernel argument in RESULT.md supplies an independent structural rank proof. An additional exact calculation using SymPy's Smith-form routine agreed with the certificate.

Limitations: the certificate proves a finite integer matrix claim, while applicability to each smooth even-theta-marked quartic relies on the classical, cited geometric identification. These checks are not a formal proof-assistant development, independent professional audit, or determination of historical priority. No external validation of a submitted artifact is claimed.
