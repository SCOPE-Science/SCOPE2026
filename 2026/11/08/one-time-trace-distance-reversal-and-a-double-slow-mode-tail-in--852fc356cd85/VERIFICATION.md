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

## Reproducible checks

Run `python verify.py` with Python 3, NumPy and SciPy. This verifies an exact rational telescoping identity for all \(3\leq N\leq50\) and \(1\leq m<N\), samples the exact continuous-time Markov matrix exponential for seven sizes and 201 times each, checks monotonicity and the unique sampled crossing, tests leading asymptotic coefficient consistency at five sizes, and checks independent-emitter nonreversal for 18 sizes. The program was executed successfully and reported 2,745 passing deterministic checks. The checks are deterministic and finite; no global uniqueness or asymptotic theorem follows merely from their execution.

## Analytical coverage and limits

All-size correctness instead follows from the holding-time representation, strict ordering of the endpoint and interior rates, log-concavity of exponential-convolution survival, and explicit Erlang/asymptotic convolution. The claim is for an ideal zero-temperature symmetric Dicke ladder and diagonal initial states. It establishes unique trace-distance crossing but only existence for the mean-excitation crossing. Independent publication-priority assessment has not been performed.
