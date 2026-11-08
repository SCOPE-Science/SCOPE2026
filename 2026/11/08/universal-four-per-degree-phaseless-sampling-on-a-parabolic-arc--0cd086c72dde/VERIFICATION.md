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

## Analytical checks

1. The only possible term of degree \(4d\) in the curve intensity comes from the product of the two leading polynomial terms; it equals \(|a_d|^2(T^2+T^4)^d\). Therefore the \(T^{4d-1}\) coefficient vanishes identically.
2. The generalized Vandermonde determinant equals the ordinary Vandermonde times \(\sum_j t_j\) and is nonzero under the theorem hypotheses.
3. The two fiber reflections \(T\mapsto i-T\) and \(T\mapsto -i-T\) force the ratio of any two matching nonzero polynomials to be periodic by \(2i\); nonconstant rational functions cannot be periodic.
4. For four distinct zero-sum nodes in degree one, a nonzero Hermitian kernel matrix is necessarily indefinite. The explicit matrix for nodes \(-3,-1,1,3\) has determinant \(-85/4\).

## Standalone exact checker

Execute `python3 verify.py` with SymPy installed. The checker uses exact integer and Gaussian-integer symbolic operations and prints `PARABOLIC_PHASE_RETRIEVAL_EXACT_CHECKS_PASS 22`. It checks four finite dimensions, four explicit generalized Vandermonde matrices, reconstruction of four intensity polynomials and the degree-one boundary obstruction. These calculations corroborate, but do not establish, the theorem for unbounded degrees or arbitrary node configurations.

## Scope of verification

No general-purpose infinite theorem prover, external expert certification or independent audit is claimed. A fixed-node finite-dimensional stability constant follows by compactness; its numerical value was not estimated. Novelty is assessed relative to inspected sources, not proven by failure of search queries.
