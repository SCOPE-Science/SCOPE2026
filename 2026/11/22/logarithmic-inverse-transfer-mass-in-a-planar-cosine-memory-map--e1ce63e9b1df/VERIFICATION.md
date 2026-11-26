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

In the shear coordinates (x,V) with V=y+ex, the scalar equation is x cos(θ−ωx)=q with θ=dV, ω=de≠0, q=(U−a)/B and B=bc≠0. On the two-sided cosine-zero lattice z_j=(θ−(j+1/2)π)/ω, a fixed phase neighborhood of radius π/3 has |sin|≥1/2. For sufficiently distant centers the derivative has a fixed nonzero sign and the endpoint values bracket q. Conversely, |cos|=|q/x| forces every sufficiently distant solution into one of these neighborhoods. Analyticity gives finitely many remaining roots in a compact interval. The x=0 possibility at q=0 and possible central coincidences or singular roots are included in this finite remainder; distant roots remain distinct and regular. Independently expanding the scalar equation gives x_j−z_j=(-1)^j q/(ωz_j)+O(|z_j|^-3) and g'(x_j)=(-1)^jωz_j+O(|z_j|^-1). The determinant in the original coordinates is B g'(x_j), so the reciprocal difference from 1/(|Bω||z_j|) is summable. The two lattice rays give count 2|ω|R/π+O(1) and weight 2 log R/(π|B|)+O(1); the cutoff displacement changes at most a bounded number of edge terms. For compact target rectangles all distant estimates, including regularity, hold uniformly with a suitably enlarged source cutoff; the removed source strip has bounded area after the unit-Jacobian shear, avoiding any false uniform bound on the weights at a fold. The change-of-variables/area formula gives the bounded measurable target area law. For all target null sets the preimage on the regular locus is null by countably many local inverse charts, and the critical locus is null by Fubini (discrete y zeros at each x), which also handles completion-measurability. Every positive-area target has a bounded positive-area subset with infinite preimage area. Countable unions of finite pushforward-measure sets therefore cannot cover the plane. No claim of finite density, periodic coordinates, or forward recurrence is made. The source's finite bisection check was inspected, not run.

## originality

PASS

There is verified same-map forward-dynamics coverage and a closely analogous linear inverse count for a different cosine-flux map. The supported contribution is the target-wise full-plane inverse branch and inverse-Jacobian asymptotics for this map, especially the uniform remote-branch area law and associated non-sigma-finite pushforward. The standard area formula is not itself new. Full text of the original map paper was unavailable in the bounded lawful checks, which limits rather than decides the priority comparison.

## value

PASS

The sharp inverse-volume growth is not a root count alone: the cosine frequency and memory strength change the sheet density, yet cancel out of the logarithmic transfer coefficient. The bounded-target area theorem resolves the full-plane failure of sigma-finiteness even though inverse images of null target sets are null. This is a structural statement for a named nonlinear map and does not rely on practical bounded-state dynamics or extrapolated numerical data.

The dated certificate retains the supplied scientific assessment, sources and limitations.
