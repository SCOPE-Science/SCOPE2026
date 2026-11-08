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
Execute `python3 verify.py` with Python 3 and the standard library only. The output for the reviewed copy was `PASS 2389 supplementary tests; direct face enumeration, exact ranks, independent Gaussian mixture integration, numerical samples`.

The script checks the face-vector identity against a separately enumerated original-face crossing test for a set of normals in dimensions \(3\) through \(8\), verifies exact permutation ranks, examines the top-rank face-vector tie, and compares one-dimensional Gaussian-mixture quadratures against direct normal samples. The random seed is fixed. These checks are finite and do not certify all dimensions; the analytic proof in `RESULT.md` supplies the full quantifier coverage.

The claim treats \(0<h<1\). The limit \(h\uparrow1\) is a one-sided limit, not a statement about hyperplanes containing a vertex at \(h=1\). Independent external mathematical validation has not been performed.
