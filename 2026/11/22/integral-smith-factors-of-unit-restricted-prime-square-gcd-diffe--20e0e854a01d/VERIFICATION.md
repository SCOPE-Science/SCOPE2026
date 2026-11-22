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
# Reproducibility and checks

`verify.py` uses Python 3 and SymPy 1.14 (standard integer matrix and Smith-normal-form operations). Invoke `python verify.py` from the directory containing it. The expected completion line begins `VERIFY_OK`.

The script directly builds the actual unit-residue GCD matrix and compares **every** integer Smith factor for \(p=2,3,5\). It checks the kernel's block identity at primes \(3,5,7,11,13\), and computes all determinantal divisors for both reduced blocks for each odd prime below \(102\). It checks the multiplicity and divisibility chain of the predicted factors.

The unbounded proof is separate from the checker: use the unimodular decomposition (1)--(3) and the four determinantal divisors of \(K\) established in `RESULT.md`. No numerical verification certifies the all-prime statement. The cited scientific works were compared by object and actual implications; absolute historical novelty remains subject to independent bibliographic investigation. No external independent audit has been performed.
