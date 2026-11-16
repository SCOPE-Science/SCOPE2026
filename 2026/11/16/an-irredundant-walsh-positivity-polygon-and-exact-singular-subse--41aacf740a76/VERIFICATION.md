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

# Reproducibility and scope

The complete proof and Fourier normalization are given in `RESULT.md`; `check.py` is a standalone Python 3 standard-library exact rational arithmetic checker. Run `python check.py` from the directory holding these files. Expected output:

`PASS: 25 dimension/scale pairs, 125 exact polygon vertex and full Walsh-spectrum tests; 3820 vertex-grid witness values; pure-shell witnesses checked.`

The finite checks cover cube dimensions \(2\) through \(6\), and decay fractions \(1/4,1/3,1/2,2/3,3/4\). They establish neither the universal theorem nor uniqueness of the literature claim. The proof is analytic and combinatorial for every dimension \(d\ge2\) and every real \(0<r<1\). No independent audit was conducted.
