---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

For an ambient Gaussian X=RU, the absolute edge projections divided by √2 are standard folded normals, and E R³ gives precisely the stated ambient gamma ratio. A diagonal sign switch along each tree removes every sign on a forest, so orders one and two and every nontriangle summand at order three, including repetitions, cancel across signings. Unit triangle projections have, up to orientations, correlations (−1/2,−1/2,−1/2) in the balanced case and (1/2,1/2,1/2) in the unbalanced case. Polar integration gives the balanced F_−, and the common-factor Gaussian decomposition gives the unbalanced F_+. To certify positivity without decimal inequalities, Cauchy–Schwarz gives E f³ ≥ (E f²)²/E f, with E f²=1/6+√3/π>47/66 from √3>12/7 and π<22/7, while F_− E f=3/(2π)<1/2<(47/66)². The ordered expansion has six copies per triangle, proving the comparison even with isolated vertices or a deficient zonotope span. Independent high-precision quadrature gave 0.14915548175434147 for the gap (replay: /workspace/branches/independent-replays/audit_width_gaussian.py). The frozen checker was read, not run; RESULT also mentions a triangle-with-leaf diagnostic not present in that script, which tests only the triangle. This does not affect the analytic finding.

## originality

FAIL

The signed comparison is not stated verbatim by the unsigned antecedent, but the entire moment difference is a mechanical consequence of its exact Gaussian motif formulas and classical forest switching. In particular the previously evaluated unsigned three-edge star has the identical Gaussian product law as the unbalanced signed triangle, not merely a similar numerical result. Both constants, their roles in the cubic expansion, and the radial normalization method were available. The change from intrinsic to ambient normalization is the standard chi moment with the dimension changed. This is a finding of mechanically covered substance, not a claim that a prior source printed the signed theorem verbatim.

## value

FAIL

Unbalanced triangles and ambient widths are natural, but this precise invariant requires only forest switching, the two already evaluated motif laws and elementary rescaling. The finding neither adds an independently useful unknown Gaussian identity nor reaches higher moments or switching information beyond the mechanically implied count. Under the narrow exact-invariant standard, this is a routine signed specialization, not a separate surviving contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
