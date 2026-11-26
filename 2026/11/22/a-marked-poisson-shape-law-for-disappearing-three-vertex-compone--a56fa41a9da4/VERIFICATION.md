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

Unwrapping a two-edge host spanning tree yields a unique short arc because the complementary gap is longer than 4m; each consecutive gap is at most m, and the third host edge exists iff a+b≤m. For each triple, degree summation gives 6m−2e external edges, with e=2 or 3. The exact mean follows from the two gap counts and the internal connectivity probabilities. Tree events have weights (1+O(p))p²q^(6m). Since q^(6m)=e^(−c)/(n log² n) and mp/log n→1/6, the grid sum per available mark tends to e^(−c)/36 times volume. In any fixed mixed factorial moment, overlapping marked candidates contribute zero; their product weights sum to O(1/n) since O(m²) candidates meet one given triple and all weights are O(1/(nm²)). Disjoint candidates share at most 9 per pair closed-edge prescriptions, so their uniform correction tends to one. The continuity-set factorial moments give independent Poisson counts, with tightness from the bounded expected total. Actual retained triangle counts have expectation O(p). Uniform choice among existing components is justified by conditioning on non-emptiness: for a continuous bounded mark test, average it over the finite count (zero on empty), a bounded continuous functional in the finite point-measure topology. Integrating the limiting intensity gives mass e^(−c)/18, host-triangle fraction 3/4 and center fractions 1/4, 1/2, 1/4. An independent exact replay verified the finite mean for (n,m,p)=(13,2,1/3),(19,3,2/5) and the joint correction for all 4,427 disjoint candidate pairs at (19,2); it is not evidence for the infinite limit by itself. Replay: /workspace/branches/bdef64f8-d031-46b4-bc70-3de5e3bebc99/reproduce_band_triples.py. The malformed prior-work link in the frozen prose is a bibliographic issue; the checked identifier appears below.

## originality

PASS

The prior scalar extinction law and the standard Poisson method are not new. The specific joint spatial, normalized gap and retained center intensity is not supplied by the compared works.

## value

PASS

At an already known extinction window, the explicit intensity answers a separate geometric question: host triangles have half of the gap-grid area but three quarters of the retained components, while retained cycles themselves vanish. Joint gap and center information is unavailable from the scalar mean or limit and is useful for distinguishing host geometry from retained topology.

The dated certificate retains the supplied scientific assessment, sources and limitations.
