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

The standalone `verify.py` reproduces the exact rational substitution factor-frequency computation for lengths two through ten, all sixteen hidden two-block balance relations, all thirty-two adjacent-run pattern frequencies, the absence of five consecutive equal signs, and independent nearest-neighbor sign frequencies.

It separately verifies that a substituted prefix of length \(2^{18}\) agrees at each position with the binary-digit parity definition, then enumerates complete runs in that prefix and compares empirical joint frequencies with the proved exact limits. The finite prefix is not used as proof of any infinite assertion; the proof uses primitivity and the terminating exact factor-frequency recursion in `RESULT.md`.

Reproduction command: `python3 verify.py`.

Expected final output: `VERIFY_OK exact_block_frequencies=2..10 sign_run_pairs=32 prefix=262144 runs=131072`.

Scientific limits: no result on higher-order run Markov structure, rates of convergence, or uniqueness of historical priority. Independent audit has not been performed.
