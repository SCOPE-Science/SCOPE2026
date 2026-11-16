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

Run `python check.py` and `python crosscheck.py` in the directory containing these files, using Python 3 only. Both emit a terminal `PASS`; any unexpected result raises an assertion. Every signal is a tuple of exponents in \(\{0,1,2\}\), with the initial exponent set to zero for the unique global-phase representative.

`check.py` uses difference-class counts and a closed form for every orbit element. `crosscheck.py` uses exact arithmetic in the Eisenstein integer basis and a generator-based orbit traversal; it independently checks all periodic spectra and fiber partitions. Both explore the *full* finite domain at lengths one through six, not a sample or probabilistic test.

The exact spectral class counts are \(1,2,4,7,13,30\); the orbit counts are \(1,2,4,7,13,32\). At length six the only nontrivial intensity class comprises 18 normalized words in three orbits of six. Its exact autocorrelation is \((6,0,0,3,0,0)\), so the complete unscaled Fourier intensity vector is \((9,3,9,3,9,3)\).

The checks neither establish novelty against unpublished tables nor extend the theorem to lengths beyond six; independent audit has not been performed.
