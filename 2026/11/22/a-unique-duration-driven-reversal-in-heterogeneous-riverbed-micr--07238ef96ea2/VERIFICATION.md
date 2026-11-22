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

# Computational checks and limitations

`check.py` uses only Python 3 standard-library modules. Running `python3 check.py` checks the two independent phase-map compositions against the closed-form swap formula, repeatedly tests the strict monotonic ratio on admissible positive rate arrays, and locates the stated example crossover. It includes an **exact Fraction-based** alternating-series enclosure of the four exponentials at the two rational bracket endpoints; this last test is a bona fide rational sign certificate for that finite example. The check completed with 36,020 supplementary comparisons and bracket signs consistent with the stated theorem.

No program can establish the universal sign classification from a finite random grid. The actual global proof is the affine composition identity, strict logarithmic derivative and endpoint limits reconstructed in RESULT.md. This verification does not assess empirical parameter calibration, any inaccessible article's full text, or independent historical priority. No independent audit has been conducted.
