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

Run `python3 check.py` in the folder containing this file and `RESULT.md`. The checker uses only the Python standard library and asserts all eleven direct binomial-cube digit values, the cyclic exponent multiplicity vector, the cyclic autocorrelation, and the four exact monic cyclotomic remainders. It checks direct integer Franel sums for indices below \(160\); exact residue histograms at every depth through \(r=8\); separate digit enumeration through \(r=4\); and the closed variance identity at all those depths.

The proof for all \(r\) and all \(N\) is deductive: digitwise Lucas factorization, Fourier inversion on the group of ten units, exact polynomial remainders, and aligned base-eleven block summation. The checker is finite corroboration, not a substitute for these arguments. The self-review passed; no independent audit has been performed.
