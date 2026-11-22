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

# Exact finite verification

Run `python verify.py` with Python 3.9 or newer. All input data are derived by the program from seven Fano lines; there are no external packages or data dependencies.

The two separately implemented matching recursions give 84 perfect matchings, 28 occurrences for each of the 42 edges, and even co-occurrences for every one of 861 unordered edge pairs. The pair-count histogram is \(0:84,4:21,6:168,8:168,10:84,12:168,14:168\). The gauge-fixed 15-variable Walsh–Hadamard transform is checked at each of 32768 frequencies against the direct 84-term character sum. The exact 12-level signed histogram is reported in RESULT.md.

The modulo-eight theorem is proved algebraically by expanding the sign product to quadratic order. The exhaustive computation confirms the hypotheses for the *single specified graph*, while the spanning-tree gauge proves that the 32768 reduced tests represent all \(2^{42}\) characters. The certificate does not cover weighted dimers or other graphs.

Independent audit has not been performed.
