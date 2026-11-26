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

A connected 24-vertex graph has a 23-dimensional cut space. Switching by a vertex set multiplies every matching character by the parity sign of that set, so the 8,192 cut cosets determine the magnitude histogram and each nonzero coset splits equally by sign. An independent DFS-tree quotient and integer Walsh transform gave absolute counts 4781,2536,647,136,66,16,9,1 at magnitudes 0,8,16,24,32,40,48,64, reproducing the entire ambient signed table, rank, nullity and condition number. The reduced signed split is section-dependent and was not compared across different trees. The inverse transform of the quotient support indicator gives absolute numerator sum 164610 and normalization 8192: the full kernel vanishes off the cut annihilator, with the same absolute sum 82305/4096 after normalization. A real or complex projection conjugated by translations continues to map into, and act identically on, the range; averaging is contractive and gives the unique diagonal projection. Its endpoint norms are exactly the kernel's absolute sum. Singleton multipliers equal 64 minus twice edge occupancy. All eight 32-occupancy edges were identified, specifically the two inward incident edges at each of the four cells (±3/2,±3/2).

## originality

PASS

The full independent-edge signed spectrum and exact endpoint projection constant on this graph are supported as distinct to the best of current knowledge. The tiling count, Kasteleyn encoding, general averaging method, Aztec divisibility and the analogous corner cancellation for another graph are not claimed as new.

## value

PASS

The Aztec diamond is a standard planar matching family and independent signs on all its edges are a natural perturbation, not a selected list of test signings. The full low-order spectrum supplies exact cancellation and stable-recovery data unavailable from the tiling count or divisibility, and the evaluated minimal endpoint norm quantifies the cost of extracting the recoverable subspace. It is an exact benchmark for comparing matching families and future higher-order calculations. The norm is for a projection, not for inverse convolution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
