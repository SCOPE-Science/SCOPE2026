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

After eliminating e1 the quadric has a nondegenerate alternating polar form and five binary points, so is nonsplit. The proposed isotropic basis gives the split Segre form over F4. I checked the displayed cubic factorization independently by evaluating at all 16 F4 pairs on the S=U=1 chart; both sides have degree at most 3 in each affine variable, so interpolation guarantees the homogeneous identity. The distinct factors are smooth graphs, with complete degree-three Segre embeddings. On T=V=1 they meet at U=U^4, giving four reduced intersections; T or V zero forces both zero, giving the fifth transverse intersection because the two graph projections have zero Frobenius derivative in opposite directions. Independently, the Vandermonde rank drop and e1/e2 force exactly four equal nonzero coordinates and one zero. The connected normalization with five simple intersections gives arithmetic genus four. Odd Frobenius powers exchange the components and even powers preserve both split P1s, giving the stated counts. The connected Picard torus has characters the kernel of the incidence map from the five oriented edges to two vertices, rank four, with every edge orientation reversed by Frobenius, hence the fourth power of the norm-one torus. This is not a calculation for the naive power-sum reduction.

## originality

FAIL

An earlier distinct published record gives the same model, decomposition, rational transverse nodes, genus, and all-extension counts, and supplies all graph data determining the torus by standard normalization and descent. A different factorization proof is not a distinct finding.

## value

FAIL

The geometry of this specific degeneration is intrinsically useful, but the submission repeats an exact known degeneration and count; the only additional invariant is the routine signed-cycle-lattice consequence of the known data. No independently valuable new remainder is established.

The dated certificate retains the supplied scientific assessment, sources and limitations.
