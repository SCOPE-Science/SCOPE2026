---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-13.md",
      "INDEPENDENT_AUDIT_2026-11-13.json"
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

PASS: The lattice slice at height j in t Q_{r,c} has binom(t+cj+r,r) points for r>=4, c>=0, t>=0, so the exact sum j=0..t is a degree-(r+1) Ehrhart polynomial. Its top twist coefficients are c^r S_r(t)/r! and c^(r-1)(t+(r+1)/2)S_(r-1)(t)/(r-1)!. Bernoulli B_{2h}!=0 gives first-tier e_{r+1-2h} coefficient binom(r+1,2h)B_{2h}/(r!(r+1)), and the odd Bernoulli cancellation yields second-tier e_{r-2h} coefficient (r+1)binom(r,2h)B_{2h}/[2r(r-1)!]. Top two degrees and constant are positive; alternating even Bernoulli signs make precisely r+1-4j and r-4j (j>=1) negative when those degrees >=1. Each coefficient is polynomial in c with nonzero leading term, so simultaneous eventual c0(r) exists. Independent exact slice/polynomial checks in bounded r corroborated rather than replaced this uniform proof.

## originality

PASS

PASS (best knowledge): Liu–Tang–Tao–Zhang introduced the exact smooth simplex-fiber family, its minimal-facet characterization and one eventual negative coefficient (degree r-3), all credited. The complete sign vector including the c^(r-1) Bernoulli cancellation tier and unbounded exact count of negative coefficients was not identified in available primary description or full relevant distinct Resultary comparisons. Original full paper inaccessible with VPN disconnected, so a plausible implicit stronger theorem remains residual risk, not novelty proof.

## value

PASS

PASS: A full infinite-dimensional eventual coefficient-sign classification at the sharp minimal smooth facet threshold is a natural structural completion of known Ehrhart-positivity counterexamples. It identifies simultaneous negative coefficients and the second twist-order cancellation effect rather than merely reproducing a known single negative coefficient.

The dated certificate retains the supplied scientific assessment, sources and limitations.
