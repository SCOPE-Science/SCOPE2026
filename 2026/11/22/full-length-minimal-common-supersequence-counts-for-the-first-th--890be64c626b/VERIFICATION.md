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

# Verification and limits

The result has an all-parameter proof using unique embeddings, a local no-replacement condition, and a finite offset transition table. The programs below perform separate finite cross-checks; they are not substitutes for the proof.

Run `python3 verification/grid_count.py` (Python 3, standard library only) to check all 45 alphabet/repetition cases. Run `g++ -std=c++17 -O2 verification/exhaustive.cpp -o /tmp/mcs-check && /tmp/mcs-check` to enumerate actual distinct outputs and deletion minimality for seven independently chosen cases. The expected exact stdout is embedded as `verification/grid_count.out` and `verification/exhaustive.out`.

Tests include lengths beyond the first period, the boundary cases, and a binary-power/Fibonacci distinction. The complete infinite theorem is justified by the proof, not finite observation. The alphabet-size restriction and absence of a general-length spectrum remain explicit limitations.
