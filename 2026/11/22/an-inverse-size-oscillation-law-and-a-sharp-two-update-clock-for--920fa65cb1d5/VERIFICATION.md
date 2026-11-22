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

# Reproducibility and limitations

The analytic transition classification and its all-length/local-limit arguments appear in `RESULT.md`. Independent direct-neighborhood exhaustive functional-graph enumeration (`verify_labelled.py`) was run on every labelled configuration of the graphs with two through six deleted pairs, including the full 531,441-state six-pair case. Weighted pair-type enumeration (`verify_profiles.py`) was independently run at every size from two through twelve deleted pairs, testing the fixed, immediate two-cycle, and eventual two-cycle basin formula, and first-entry cutoff for every one of its profile types. In both programs, assertions passed. The actual observed terminal output is provided in `verification_output.txt`.

The implementation uses Python 3 and the standard library only. Run `python3 verify_labelled.py --extended` and `python3 verify_profiles.py` in the extracted package. The computations are finite exact checks and do not independently establish any infinitely quantified theorem or asymptotic; those rely on the proof, including the nondegenerate lattice local central limit theorem and its conditional Gaussian form. No third-party or independent scientific validation was performed.
