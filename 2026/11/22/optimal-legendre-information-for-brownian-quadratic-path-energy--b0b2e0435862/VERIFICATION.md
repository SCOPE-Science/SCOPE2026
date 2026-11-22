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

The standalone `verify.py` uses Python's standard library and performs exact rational checks of the full low-degree Gram matrix, finite subset maximization, and the general rational tail expression. Run `python3 verify.py` in the same directory as the other files. Its run produced all PASS messages, including exact Gram identities through degree 13, strict optimality among all subsets of the first 13 modes for budgets 1 through 7, and exact tail identities through budget 100. The finite checks are supporting reproducibility evidence and are not proofs over all indices or all sensing subspaces. Those infinite statements are justified by the monotone parity-chain compression and spectral min-max arguments in `RESULT.md`.

Independent reproduction and independent audit have not been performed. The general Fourier-expansion machinery and the two-coefficient conditional moments are prior results, not new claims here.
