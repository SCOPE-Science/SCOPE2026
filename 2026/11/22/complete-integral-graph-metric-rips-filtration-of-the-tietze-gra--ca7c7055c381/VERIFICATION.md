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

# Reproduction of the exact integral homotopy classification

Place `verify_tietze.py` and `collapse_certificate.json` together, then run

```sh
python3 verify_tietze.py collapse_certificate.json
```

The verifier reads the exact labeled graph, checks it is cubic with exactly one triangle and diameter three, reconstructs every pairwise distance and enumerates every Rips face at radii one, two and three. At radius two it recomputes 319 nonempty faces, validates all 119 proposed elementary collapses as sequential free-face deletions, validates an eleven-edge spanning tree in the residual complex, and computes all triangular attaching words after contracting the tree. The 27 specified generator cancellations are validated *in order* by finding a remaining two-cell whose word is precisely the single generator, with sign. The resulting zero-skeleton has one point, no one-cells and four trivially attached two-cells. This yields the integral wedge of four two-spheres.

The mod-two boundary-rank checks at radii one and two are an independent finite arithmetic cross-check, not a proof of integral torsion-freeness. The integral homotopy conclusion follows instead from the simplicial and CW collapses. Radius-zero and radius-three outcomes are immediate from the graph's twelve vertices and diameter three. The output in `verification_output.txt` was obtained by running the supplied verifier with the supplied certificate.

Scientific limit: a proof of one fully enumerated finite graph does not establish results for all cubic graphs, any local-expansion family or continuum graph metrics. This is a self-review; no external or independent validation is claimed.
