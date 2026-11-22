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

# Verification guide

The exact theorem is established by the proved nonloop-pair uniqueness lemma, deterministic removal of the largest contiguous label block, and the independent insertion-gap count. The code checks finite consequences but is not an infinite proof.

Run `python3 verify.py` with Python 3.9 or later from the same directory. No third-party packages are used. This program enumerates all increasing-nesting words by directly inserting a new maximum-label block into every available position, constructs each directed adjacent-pair spectrum directly, and groups all sources by their spectra. A separately written recurrence acts **only on the spectrum**, reduces the largest letter and multiplies the observable compatible-gap counts. Its output is compared against the direct grouping counts for every profile.

Checked parameters: \(k=2,3,4\) with \(1\le n\le5\), and \(k=5\) with \(1\le n\le4\). Each parameter set additionally checks the known source-count product and the claimed maximum fiber. For \(k\ge3\), it checks unique maximizing profile for \(n\ge2\), all singleton-block equivalences and exactly \(n!\) singleton profiles. For \(k=2\), it checks that all profiles are singleton. All these checks completed successfully in the stated environment using the delivered script.

All tested spectra are derived from actual source words, and the profile-only routine also checks the inferred boundary symbol at every reduction. Necessary-and-sufficient realization for arbitrary candidate matrices is proved in the prose but is not independently tested on the complete space of invalid matrices. The program does not attempt to check unbounded cases; the proof is the source of the universal quantifiers. No independent external review or formal certification was conducted.
