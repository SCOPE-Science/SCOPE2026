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

Install Python 3.10+ and the package declared in `requirements.txt` (`python -m pip install -r requirements.txt`). Then run `python verify_components.py` and `python verify_parity.py` in the folder containing these files. The corresponding captured stdout files are `components.log` and `parity.log`.

The SCC verifier constructs actual single-vertex closed-neighborhood minority transitions, identifies all terminal strongly connected components and compares their complete vertex sets with the proposed maximum-cut classes for 25 instances at sizes 2–6. It checks 36,400 labelled states.

The independent bitset verifier evaluates the exact cut directly and enumerates the complete maximizing population, checks that every allowed update at a maximizer remains a maximizer, computes the rank-count census and verifies parity correspondences for sizes 2–8. It checks 757,296 labelled states on 42 graph instances and all 15 paired cases for odd sizes 3, 5 and 7.

The all-size conclusions depend on the constructive proof (including its pigeonhole improvement step), the Boolean-inclusion graph connectivity argument and the explicit parity-extension bijection, not the finite experiments. Code tests do not determine historical novelty or furnish independent scientific review.
