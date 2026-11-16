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
# Reproducible finite verification

Execute `python3 checks/check_cyclomatic.py` with Python 3.8 or later (standard library only). It independently tests, for each \(2\le n\le8\) and every \(0\le k\le n-1\):

1. Connected edge-mask enumeration using a disjoint-set connectivity test, compared with the asserted \(\binom n{k+1}2^{n-k-1}\) count.
2. Complete integer Walsh--Hadamard transform, separately compared at every character against the combinatorial Krawtchouk coefficient formula; **669,920** individual coefficients across all slices.
3. Parseval's identity, the exact least positive and largest absolute multiplier values, and the unicyclic rank formula including the perfect-square case \(n=4\).

Expected final marker: `CONNECTED_FIXED_EXCESS_KRAWTCHOUK_PASS coefficients= 669920`.

The symbolic all-integer proof applies to all \(n\) and \(k\) in scope; these computations are independent finite consistency checks, not a proof of the unrestricted theorem and not an independent mathematical audit. The literature comparison is bounded; the higher-excess root multiplicities are expressed by a finite binomial test rather than a closed arithmetic classification.
