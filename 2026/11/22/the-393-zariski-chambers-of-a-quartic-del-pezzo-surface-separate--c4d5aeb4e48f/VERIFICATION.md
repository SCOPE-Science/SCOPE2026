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

# Reproducibility

Run `python3 check.py spectra.csv` in a directory containing the two embedded artifacts, using Python 3.10 or newer and no third-party dependencies. It exits only after checking geometric exceptional-divisor intersections, 393 independent sets, all 1920 signed permutation automorphisms, exact 18 conjugacy-class orbits, each member's induced 393-face cycle structure, an independent invariant-orbit-subset fixed-count method, and uniqueness of all 18 393-face spectra. The CSV is an exact exhaustive class certificate, not random data. It was regenerated from the embedded source code and compared byte-for-byte against the packaged CSV.

There is no finite-field experiment standing in place of an infinite-field theorem: the uniformity follows from the universal geometric chamber-support and Weyl action. Realization over finite fields of size at least four is cited to Trepalin. The computed invariant is not the full surface zeta function and does not classify the surface up to isomorphism. No external independent validation has occurred.
