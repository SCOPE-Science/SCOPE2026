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

# Reproduction and scope

Run `python3 verify.py` using Python's standard library. The program enumerates exactly all \(321\)-avoiding permutations for lengths one through nine, obtains distinct standardized one-deletion outputs independently of bond counts, and compares all \((a,d)\) joint histograms with coefficients of the trivariate algebraic formula. Recorded output at review time ended with `VERIFY_OK`, with all nine lengths checked. The algorithm's finite range is explicit; all-length results depend on the written combinatorial proof and analytic singularity argument, not extrapolation from these checks.

For the limiting joint law, the singularity and regular denominator can be checked symbolically from \(T=C(z/[1-(u-1)z])\). The limiting probability generating function \((8/(9-v))^2\) has value one at \(v=1\) and coefficients \(64(j+1)/(81\cdot9^j)\) summing to one. The mean identity is limited to \(n\ge2\). No external independent validation has been conducted.
