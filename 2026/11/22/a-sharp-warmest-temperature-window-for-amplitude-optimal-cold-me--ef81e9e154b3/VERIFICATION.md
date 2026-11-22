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

# Reproduction and scientific verification

Reproduce from the supplied `check.py` using `python3 check.py` in a standard Python 3 interpreter. It uses only `math`, generates a dense parameter grid including boundary mean, small and large cold offsets, and compares a direct Simpson-rule angular integral with separately evaluated analytic integrals and derivative signs. The intended successful output is `PASS: 1835 numerical and independent-integral assertions`.

Independent of computation, the proof in RESULT.md verifies (a) differentiation with the moving cold threshold, (b) uniqueness of the stationarity equation, (c) exclusion of the regime crossing the upper temperature cutoff by strict pointwise kernel decrease, and (d) strict monotonicity of the normalized optimum-temperature fraction by a derivative factorization. Those steps establish the claim for all stated real parameters; numerical tests alone do not.

The main boundary \(\mu=L\) is treated separately, and \(\delta>0\) reaches the upper sharp constant \(3/4\) only in a limit. No external or independent audit is represented by this document. Historical priority remains conditional on coverage of literature not inspected in full.
