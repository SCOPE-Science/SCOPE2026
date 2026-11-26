---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

The graph uses the full follower principal Laplacian, with degrees n and 1. Core–leaf index permutations give exactly four possible placement types. Eliminating the unit leaf diagonal leaves a core matrix A=diag(d_i)-11^T, with d_i=n for a core with a follower leaf and n+1 otherwise; the determinant version at t!=0 gives the four factorizations in the proof. Independently, at zero, H=A^{-1} has entries delta_ij/d_i+(1/d_i)(1/d_j)/(1-sum_i 1/d_i), while block inversion gives follower inverse blocks H, HT^T, TH, I+THT^T for the leaf-to-core incidence T. This directly gives tr(L_FF^{-2}) as the squared Frobenius norm, with exact agreement for the four rational costs and comparisons. The critical difference CC minus CL_d is -(3n^2-4n-16)/(n+2)^2, positive at n=3 and negative for all n>=4. CL_s and LL both exceed CC, the latter by a quartic whose coefficients in n-3 are all positive. Hence there are exactly six minimizers at n=3, cost 124/25, and exactly binom(n,2) at every n>=4. Also independently obtained exact J1 gaps relative to CL_d: 2/(n+2), 4(n+1)/[n(n+2)] and (n^3-4n-2)/[(n+1)(n+2)] for CC, CL_s and LL respectively; all are positive for n>=3. Exact direct inversion of all 245 pairs for n=3,...,7 agreed (at n=4, J2 minimum 27/4, J1 minimum 31/6). Finite checks corroborate, while the symbolic signs prove the infinite claim. Uploaded verifier inspected, not executed. Independent replay: python3 /workspace/evidence/corona_exact.py (SymPy).

## originality

PASS

Best of available evidence: the ground graph and leader problem are known for other noise models, and the reciprocal-square functional itself is established. The exact global four-core switch for the squared inverse on these grounded clique coronas was not found in the inspected earlier statements or implied by them.

## value

PASS

A symmetric graph with one private leaf per core is a minimal model in which pinning a leaf and pinning its core are genuinely different. An exact all-size reversal relative to the usual inverse trace, with all optimizers and costs, makes the given moment distinction an actionable design boundary and provides a benchmark for grounded spectral optimization. This does not claim generalization to other graphs, leader counts, weights or inverse powers.

The dated certificate retains the supplied scientific assessment, sources and limitations.
