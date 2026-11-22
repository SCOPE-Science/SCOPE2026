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

# Reproducible verification

Run `python3 checks/verify.py` from the directory where all embedded files are saved. The script uses only the Python standard library; its final line begins `VERIFY_OK` upon success.

The code makes exact rational comparisons with explicit positive-term Taylor and remainder enclosures for exponential functions. Those inequalities independently certify the strict separation witness at threshold \(h=1/4\). It also tests 1,100 random threshold/lag cases by an independent monotone-interval root search, 8,008 grid comparisons with the predicted global optimum, and 30 higher-threshold cases. The reported maximum numerical discrepancy on the independent superlevel crossing tests was less than \(6\times10^{-15}\).

The analytic proof in RESULT.md covers all positive thresholds and nonnegative lags. Finite numerical tests are supplementary. The script does not establish whether an equivalent theorem appears in unexamined historical literature, does not prove unique threshold preference crossover, and does not evaluate real flood hazards. Independent external audit has not been performed.
