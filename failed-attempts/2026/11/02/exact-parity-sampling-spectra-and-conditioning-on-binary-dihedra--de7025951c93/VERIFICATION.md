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

The actual stated spectrum, rank, condition ratios and matrix shift hold. The two within-circle blocks have discrete Fourier eigenvalues Nc_j by character orthogonality; the cross blocks vanish except on the constant modes, where they split the two eigenvalues by ±N in even degree and vanish in odd degree. The physical evaluation Gram multiplies this by ell+1, leaving rank and ratios unchanged. The allowed residues are cyclically consecutive in the step-two ordering; they give the stated ranks after counting the positive constant modes, including ell=0. For even ell<N, the constant eigenvalue is 2N. Counts are at most two, and there is an occupied nonzero singleton for 0<ell<N−2: otherwise there would either be only residue zero, or the block of consecutive weights would have to visit all m residues with all nonzero counts equal to two (length 2m−1). At ell=N−2 every nonzero allowed residue appears twice. The text at RESULT.md line 77 has a false intermediate assertion for ell≥N: e.g. m=4, ell=10 gives c_2=c_6=3 when s=1. The correct bound is 2s≤c_j≤2s+2, from 2ms+1≤ell+1≤2m(s+1)−1 and cyclically consecutive residues. The constant block attains both bounds, proving the claimed ratio without the false assertion. The shift adds four copies of each allowed residue, leaves U_ell(0) fixed, and hence adds 4N times the parity projector, exactly 4m(I+(-1)^ell J). Inspected the frozen verification notes and artifacts/verify.py; no supplied code was executed.

## originality

FAIL

A distinct indexed result gives the complete spectrum, all ranks, and the common Fourier/constant basis for a strictly broader configuration. The added condition-number and matrix-shift statements are mechanical consequences of those available exact formulas. This is a finding of mathematical coverage, not a claim about which same-date record came first.

## value

FAIL

Exact spectra and interpolation cutoffs would be useful in isolation but are already covered in a broader indexed theorem. The surviving explicit conditioning ratio is a comparison of extrema of the known levels, and the shift is a direct evaluation of the known sine kernel at the same sample angles. Neither remaining claim gives a nonmechanically implied invariant warranting a repaired finding.

The dated certificate retains the supplied scientific assessment, sources and limitations.
