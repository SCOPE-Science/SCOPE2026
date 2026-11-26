---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

At every coordinate nullcline the finite multiplier times zero is exactly zero, without requiring any uniform bound on multipliers. The row r=e_i^T Q is nonzero because its diagonal entry is d_i+κ and d_i>0. Writing s=e_i^T Q² gives the defect −h²su/2+O(h³||u||); on the compact positive nullcline ball the remainder is uniform. The maximum absolute value of a linear functional on that shifted ball is |su_0|+ε||proj_(r^⊥)s||, with the stated Gram-error formula for Δ². A positive Δ gives a fixed (not h-dependent) positive state with a nonzero leading coefficient. Every nullcline meets the positive cone, for instance with u_i=d_i/(d_i+κ) and all other entries 1. For κ>0, Qe_i has nonzero projection on the constant mode and nonconstant modes at distinct eigenvalues. As a separate direct witness, at the above u, (Qu)_j=κ+w_ji κ/(d_i+κ)>0 for j≠i (taking missing weights as zero), so (Q²u)_i=−sum_j w_ij(Qu)_j<0. For κ=0, simultaneous row proportionality L²=CL implies CL=LC, so neighboring diagonal factors agree and connectedness makes them constant. The simple zero mode and one other eigenvalue give precisely the uniform complete graph, for which the proposed scalar step is the exact positive semigroup. For the unweighted vertex criterion a universal vertex has Le_i=ne_i−1; at a nonuniversal vertex, a distance-two position has zero L entry and positive L² entry. For the two-vertex star K_2 both vertices are universal: the leaf illustration concerns noncentral leaves of stars with a unique center, while the iff covers K_2 without exception. In the killed clique the two squared spectral masses of Qe_i are κ²/n and (n−1)(c+κ)²/n; their weighted variance for eigenvalue gap c gives the stated constant and asymptotic. The positive three-vertex path witness also gives (Lu)_1=0, (L²u)_1=1 as claimed. The analytic argument covers all stated finite graphs. The supplied checker was inspected but not executed; its tiny-graph checks are not needed to justify the proof.

## originality

PASS

The supported new contribution is the sharp shifted-nullcline defect constant together with its vanishing classification for this graph class and the weak-killing clique asymptotic. The old-state scheme form and Taylor identities on nonzero residuals are prior work; this is not a claim to invent those or to disprove second-order schemes outside the stated class.

## value

PASS

Local-order conditions for denominator-modified positive integrators can silently exclude states with zero residual in one coordinate. This theorem specifies an unavoidable quantitative defect and exactly identifies an otherwise valid graph family where the defect disappears and the approach is exact. It is useful for determining whether a positivity-preserving design needs an additional residual evaluation or nonlocal correction; the killed hyperbolic examples make the issue substantive rather than a pathology of equilibrium degeneracy.

The dated certificate retains the supplied scientific assessment, sources and limitations.
