---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

The cyclic subspace has one bright direction P_E v per distinct eigenvalue with nonzero sink projection. Its orthogonal complement reduces both the adjacency and the dissipative generator; on the bright block there is no eigenvector of zero loss, hence that finite block decays. Ring eigenvalues are strictly decreasing on the chosen half range and every ring spectral weight at 0 is m_k/n. I checked the collision lemma: the Ramanujan trace and squared trace give φ(m)+c_m(2)≤2μ(m). Odd m>1 is impossible; if 4 divides m, all nonnegative conjugates sum to zero and m=4. For m=2q with q odd, φ(q)≤−3μ(q) forces q=3 (q=1 fails, and φ(q)≥4 for odd q≥5). m=1 gives 2. Applying the lemma to a_j and −a_k gives exactly the three listed pairs and three distinct collision energies. At a collision, the v,w projections have squared norms (q+q′)/2 and inner product (q−q′)/2, with the signs from the two transverse sectors; their dark component has weight 2qq′/(q+q′). The noncollision terms are zero. Applying the exact endpoint/interior ring multiplicities gives 4/(3n) twice for 4|n and 2/n once for 6|n, and the bright rank follows by counting distinct levels. The dark dimension is positive even at n=3, and the mixed-state absorption is the normalized bright trace. Independent exact cyclotomic and rational Krylov replays verify finite instances, including S(w)=7/18 at n=12.

## originality

FAIL

The stronger spectral input for the exact same prism, including the complete 4- and 6-divisibility collision census with Fourier indices, is in an earlier published record. Both advertised single-sink invariants are routine projection consequences of those data. The earlier paper's average-mixing rank is not the absorber's bright rank, and the survival formula need not be printed there for this implication to hold. This is demonstrated prior coverage of the arithmetic core, not a conclusion from an inaccessible paper.

## value

FAIL

The prism and opposite-rung capture are natural, and the correct formulas can be useful illustrations. However, the exact arithmetic information is already known for the same graph. Bright rank is a count of the listed levels, and survival is one routine two-sector projection with the already indexed mode multiplicities. There is no independently resolved obstruction or newly established threshold beyond those mechanically implied by the prior data, nor a surviving separately motivated result in the frozen claim that meets the value standard.

The dated certificate retains the supplied scientific assessment, sources and limitations.
