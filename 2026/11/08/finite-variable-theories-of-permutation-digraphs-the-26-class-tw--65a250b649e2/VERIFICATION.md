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

# Reproducibility and verification

`permutation_probe.py` exhausts all pairs of nonempty permutation cycle types up to the specified orders and implements generic counting-free finite-variable tuple-color refinement using **sets** of one-coordinate extension colors. It checks 946 pairs at width one, 2145 at width two, and 406 at width three; total 3497; all match the stated classification. It is not a full search over all finite sizes.

`permutation_spectrum.py` is a separate combinatorial checker. It computes 26 exceptional two-variable classes, their minimum orders (maximum 10), and two independent coefficient recurrences for the Euler-product identity through degree 30 at widths three through seven; it also checks 1860 canonical-minimum inequalities. Output is preserved in `permutation_probe.out` and `permutation_spectrum.out`.

With Python 3 and no third-party libraries or network, execute `python3 permutation_probe.py` and `python3 permutation_spectrum.py` in the directory containing the four artifacts. Compare stdout byte-for-byte to the `.out` files. These programs do not replace the infinite-round pebble argument or certify historical originality.
