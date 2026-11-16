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

# Computational verification

Invoke `python CHECK.py` with Python 3.8+ and no third-party packages. The checked output is `CHECK_OK prime=1009 order14_root=904 disconnected=560 translation_orbits=42 rank_pairs=1764 lower_minor_checks=8`.

The exhaustive loop enumerates all 16,383 nonempty supports, identifies the 560 disconnected under circular distance four, partitions these into 42 translation orbits, and checks all 1,764 representative Fourier restrictions at the exact prime 1009. Independently shifting the row and column sets preserves complex rank. A nonzero modular minor forces the corresponding cyclotomic determinant to be nonzero over the complex numbers. The lower-witness test checks four 3-by-3 and four 4-by-4 cyclotomic minors over the same field. No random sampling, floating-point rank tolerance, or external data is involved.

The analytical step connecting STFT magnitude arrays to recovered pair-products, and the logical completeness of the orbit reduction, are written out in `RESULT.md`. The certificate alone should not be interpreted as a theorem about other lengths, noise stability, or numerical inversion accuracy. Independent audit has not been performed.
