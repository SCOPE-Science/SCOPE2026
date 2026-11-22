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

# Verification information

The theorem has an analytic proof using a standard iid packet-word representation, a generalized cycle count for walks with increments \(+1\) and \(-(a-1)\), elementary binomial summation, a multiplicative Chernoff bound, and a local binomial central limit argument. The separate program \(\texttt{verify.py}\) checks exact path counts for packet counts \(a=2,3,4,5,6,7,8\), many finite horizons, the lattice plateau identity, and direct enumeration of several finite packet shuffles.

Execute with \(\texttt{python verify.py}\) using Python 3 and its standard library only. Assertion failures stop the program. Finite checks cannot establish the infinite statement or scientific novelty; those require the stated proof and literature comparison. No independent audit has been performed.
