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

Run `python3 check_derangement_walsh.py` with Python 3.10 or newer and only the standard library. The script directly enumerates all \(2^{11}=2048\) gauge-normalized hollow sign matrices, each evaluated as a signed sum over all \(44\) derangements. It then independently constructs the complete length-\(2^{20}\) indicator and runs an integer fast Walsh–Hadamard transform to enumerate **all** off-diagonal frequencies.

The two evaluations verify the same absolute-value histogram. Further assertions check the total number of frequencies, \(\ell^2\) Parseval identity, exact zero and nonzero counts after restoring the five diagonal frequency coordinates, the least positive multiplier, the \(1269/256\) endpoint norm, and the \(169/1024\) hollow-sign permanent zero probability.

Expected final marker: `DERANGEMENT_FIVE_EXACT_PASS`. Finite exhaustive arithmetic establishes the stated finite coefficient identity when the checker and proof's gauge reduction are trusted; this is not independent mathematical auditing or evidence of any large-order extension.
