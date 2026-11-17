---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

For each d=a-b!=0 set s=a+b; cubic phase difference equals d[(3s²+d²)/4+lambda*s]. Its level fibers are invariant under R_lambda(s)=-s-4lambda/3. Fourier orthogonality gives one independent sum on each fiber, and composition of reflections generates translations by offset differences. Odd functions on F/H have dimension (p^(m-h)-1)/2. Pairing d with -d by Hermitian conjugacy and adding q-1 traceless diagonals yields real nullity (q-1)(p^(m-h)+1)/2; rank is q² minus this quantity. Full span requires at least m+1 offsets. One-offset singleton/two-point fiber row norms, with normalized Fourier output, give sqrt(q),sqrt(2),1,0 at the claimed multiplicities. Rank-one support consequences follow from offdiagonal pair products plus trace. Independently calculated direct cubic incidence ranks q=5,7,11 for one/two offsets; these finite checks do not prove the general formula.

## originality

FAIL

The published finite-parabola field-span law has, for every slope set C, the identical reflection equations f(c-s)=-f(s), additive-quotient nullity (q/|H|-1)/2 and sharp m+1 line threshold. For EACH nonzero Hermitian difference d the cubic fiber after invertible affine scaling is precisely s²-cs with c=-4lambda/3; thus that older theorem applies blockwise and yields the claimed entire kernel, real dimension, and offset threshold. Its singleton/two-point fiber structure also immediately gives the displayed one-mask singular spectrum; the remaining rank-one statements follow by standard offdiagonal product recovery. The distinct terminology and Hermitian packaging do not create a mathematically independent main finding.

## value

FAIL

The tomography interpretation is relevant, but the principal novelty/value proposition—the precise additive-span threshold and nullity—is a direct blockwise corollary of the already published general finite-parabola line theorem. The remaining one-mask row-norm counts and offdiagonal support algebra are immediate exercises from the same fibers, not a separately motivated unknown invariant or structural advance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
