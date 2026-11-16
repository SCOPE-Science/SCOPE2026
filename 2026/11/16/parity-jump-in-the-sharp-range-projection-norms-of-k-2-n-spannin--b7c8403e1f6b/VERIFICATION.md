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

The previously known exact identity for the unnormalized signed spanning-tree enumerator of \(K_{2,n}\) is rederived by classifying spanning trees by the unique double-incident right vertex. The nonzero multiplier support is a radius-one disagreement set, with a balanced-sign slice deleted when \(n\) is even. The deleted slice has Fourier coefficients obtained from the identity \(\sum_r\binom{2m}{r}B_r z^r=\binom{2m}{m}(1-z^2)^m\), which supplies the **new range-projection norm formula** after summing absolute kernel values.

Run `python3 check.py` from this directory. The checker constructs the graph and independently enumerates **all** spanning trees as connected acyclic subsets for \(2\le n\le8\), then evaluates every Walsh coefficient and every Fourier multiplier of the range projection using exact integer arithmetic. It verifies the norms as reduced rational numbers and checks balanced-slice Fourier values through dimension 50. The final marker is `K2N_TREE_SUPPORT_EXACT_CHECKS_PASS`.

These finite checks do not establish an infinite theorem on their own; the proof covers every integer \(n\ge2\). Independent mathematical validation and exhaustive historical-priority search have not been performed.
