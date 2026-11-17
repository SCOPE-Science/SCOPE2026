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
# Reproducible checks and limits

Run with Python 3 (standard library only):

```sh
python3 verify_direct.py
python3 verify_transfer.py
```

`verify_direct.py` constructs each direct labelled complete-graph trajectory, detects its first repeat and exact primitive period, and checks against the cyclic-support longest-run theorem for every \(q=4,5,6,7\) and \(n=2,3,4,5,6\). It checked all 218210 states in 20 cases without disagreement; `direct_output.txt` gives the per-case temporal histograms.

`verify_transfer.py` constructs the integer-weighted finite-state transfer without any dynamical simulation and compares its coefficients to independently enumerated cyclic palette subsets for \(4\le q\le9\), all run-length cutoffs. It additionally checks the Stirling surjection identity for all \(2\le n\le9\), including the sharp last transient layer. All 33 cutoff comparisons passed; see `transfer_output.txt`.

The all-size theorem follows from the displayed monotone support-erosion proof, unique cyclic automaton state labels and labelled-surjection exponential series. Finite program executions do not prove infinite-size assertions, historical novelty or mathematical independence. The relevant 1993 full text was not accessible, and independent audit has not been performed.
