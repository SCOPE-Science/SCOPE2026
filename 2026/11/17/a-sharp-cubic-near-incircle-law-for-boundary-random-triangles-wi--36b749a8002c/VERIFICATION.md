---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-17.md",
      "INDEPENDENT_AUDIT_2026-11-17.json"
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

The host triangle is the unique inradius-maximizing inscribed triangle: an r-disk in a contained triangle must coincide with unique host incircle and force all three tangency support lines. Near-maximal sample triples thus localize at distinct host corners. Each of six inward motions has positive linear loss: at vertex A toward B, lambda=r(s-c)/(bc), and toward C lambda=r(s-b)/(bc). The eight local arclength charts have loss sum(lambda_i t_i)+O(||t||²); positive slopes give a uniformly bounded rescaled simplex. Six sample permutations cancel simplex volume 1/3!, yielding K=P^-3 product_i(sum_routes 1/lambda_i), equivalent to the announced abc/semiperimeter formula. Conditional route probabilities factor and scaled coordinates converge in total variation to uniform three-simplex by L1 convergence of densities. Writing u=(s-a)/s etc, p=uv+uw+vw, q=uvw, G=(p-q)^3/(8q²); Maclaurin/AM-GM yield G>=64/27 with equilateral equality.

## originality

PASS

The result is for N=3 independent arclength-uniform points on fixed triangular boundary and the near-host-incircle upper tail. Full Resultary prior boundary-triangle work computes expected hull area for all N, or N->infinity maximal triangle area, not this inradius rare-event law; cyclic circle inradius distribution is a different support geometry. The inspected Edelman–Strang random-triangle paper treats normal/Gaussian angle-space law rather than a fixed triangular host. Best-of-knowledge originality with residual possibility of an earlier general corner-cone rare-event theorem.

## value

PASS

Sharp near-extremal endpoint probability, its explicit continuous shape coefficient and equilateral optimizer, and a marked total-variation simplex/independent-route limit form a natural nontrivial geometric probability theorem. The inradius observable is geometrically distinct from area/perimeter; complete local-tail classification for any triangle is worthwhile despite a three-point finite sample.

The dated certificate retains the supplied scientific assessment, sources and limitations.
