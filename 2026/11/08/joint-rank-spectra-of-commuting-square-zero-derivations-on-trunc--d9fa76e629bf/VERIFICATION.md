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

# Verification and limits

Run the independent original-equation checker from this directory as `python3 check_commuting_derivations.py`. It reconstructs each derivation as a concrete matrix on \(k[t]/(t^N)\) and directly multiplies matrices to test \(D_i^2=0\) and \([D_i,D_j]=0\). It compares every member with the mathematically proposed union of linear components, and for five configurations also computes complete individual-rank-vector histograms by matrix row reduction, comparing with the coefficient formula. The exact captured output is in `CHECKS.txt`; every listed configuration passed.

Finite checks include \(N=2,3,4,5,6,7,8,9\) over \(\mathbb F_2\), relevant cases over \(\mathbb F_4\) and \(\mathbb F_8\), and tuples through arity four. The checker does not attempt all dimensions or all finite fields; the proof for general \(N\), arbitrary characteristic-two fields, and all tuple lengths is contained in `RESULT.md`.

The checked scientific scope excludes the original equation scheme's nonreduced structure, higher nilpotence exponents and conjugacy classes. A historical priority comparison is provisional because full text of one relevant 2015 paper was inaccessible. Independent audit and external certification were not performed.
