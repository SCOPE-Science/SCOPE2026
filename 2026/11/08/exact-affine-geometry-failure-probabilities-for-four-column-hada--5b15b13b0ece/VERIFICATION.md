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

# Reproducible verification

Use Python 3.10 or later with its standard library; no network dependencies:

```sh
python verify.py
```

The script performs integer-only computations. It enumerates all \(\binom84=70\) four-column supports and all row-subset sizes \(4\le m\le8\), and checks both exact formula branches against directly computed ranks. In dimension four it verifies one canonical support of each affine orbit for all \(4\le m\le16\). It also counts the twelve coplanar four-vertex cube sets and checks the exact \(54/70\) versus \(12/70\) failure benchmark. The supplied output is `verify_output.txt` and ends in `PASSED 450 assertions`.

The rank routine works modulo \(101\). Because the rows consist of four \(\pm1\) entries, any nonzero \(4\times4\) determinant has absolute value at most \(16\) by Hadamard's inequality and is not divisible by \(101\). Therefore the modular maximal-minor test is exact for real rank in these four-column matrices.

These finite checks do not certify the theorem for untested dimensions: that scope follows from the complete occupancy and cube-incidence proof in `RESULT.md`. No independent audit or external validation has been performed.
