---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-14.md",
      "INDEPENDENT_AUDIT_2026-11-14.json"
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

Conditioning on independent gamma increments U,V,Z and one shared pathwise gamma diffusivity D, Wick/Isserlis yields R=(M_L²+2(α+1)K_{L,g})/[3(α+1)N_L−αM_L²] with M=E v(U), N=E v(U)² and K=E c(U,Z,V)². For H>1/2 the positive decreasing tempered covariance C_H gives strictly declining K with g by gamma-subordinator coupling and a positive far-gap heterogeneous-diffusivity floor. Integration gives v(s)=a s−b+ρ(s) with exponentially decaying remainder; gamma Laplace transform gives M=aL−b+O(e^-cL), N−M²=a²L/η+O(Le^-cL), while bounded K is uniform g≥0. This yields R=1/(2α+3)−3(α+1)/((2α+3)²ηL)+O(L^-2) uniformly in gap. For fixed g dominated convergence K→Eρ(Z_g)²/4 yields the L^-2 gap signal and g=0 coefficient. Independently checked H=1 explicit kernel identities and large-L first/second coefficients numerically across several α,η,g. H<1 limit and parameter-uniformity are NOT claimed.

## originality

PASS

PASS for exact two-window squared-displacement covariance, strict gap separation and its uniform long-window expansion with a gap-sensitive second-order coefficient. The far-gap nonzero floor is already implied by original one-window kurtosis and is not independently novel; the primary full text does not state the joint two-window theorem.

## value

PASS

Two-window squared-increment volatility is a natural diagnostic distinguishing shared quenched heterogeneity from finite-range Gaussian memory. Exact gap-uniform L^-1 and gap-sensitive L^-2 coefficients quantify physically different effects in a well-defined stochastic transport model beyond its known one-time kurtosis.

The dated certificate retains the supplied scientific assessment, sources and limitations.
