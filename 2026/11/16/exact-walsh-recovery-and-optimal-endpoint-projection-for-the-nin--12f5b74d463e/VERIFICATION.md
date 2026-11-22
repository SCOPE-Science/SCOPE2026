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

The nine labelled vertices and twelve nearest-neighbour edges define a 12-bit cube; spanning trees are precisely connected acyclic 8-edge subsets. I independently generated all C(12,8)=495 candidate subsets and found 192 trees, four center-adjacent edge incidences 112 and eight perimeter incidences 136. An integer 12-stage Walsh transform over all 4096 sign patterns gave precisely the stated 15 absolute-value frequencies: zeros=1186, nonzeros=2910, minimum positive 4, maximum 192. The parity identity N_odd(S) congruent to sum over included-edge tree counts mod 2 proves 4-divisibility; mask 116 attains W=4, giving sharp condition number 192/4=48. A second complete Walsh transform of the nonzero-support indicator gave kernel numerator L1 sum 40976 and ratio 40976/4096=2561/256. General averaging of any projection over 4096 translations preserves the invariant range, the idempotency on that range and does not increase endpoint norm, producing the unique Fourier support projector; hence global minimality. This is exact finite verification, not a higher-grid-size theorem.

## originality

PASS

Compared the actual theorem and its implications against the listed primary source material and published mathematical records, including aliases and substantially broader methods. No decisive prior coverage was found in the accessible evidence; this is a bounded best-of-knowledge originality finding, with residual risks explicitly documented.

## value

PASS

The first genuinely two-dimensional free-boundary square grid with an interior vertex gives a natural finite benchmark beyond width-two ladders. Its exact 1186-dimensional nullspace, sharp deconvolution gap and optimal endpoint amplification are intrinsic, linked recovery invariants not implied by the classical 192 spanning-tree count. Full census is meaningful for this canonical smallest interior-grid case; it makes no extrapolation to all square grids.

The dated certificate retains the supplied scientific assessment, sources and limitations.
