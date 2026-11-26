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

On the unit grid a nonflat cell has both slope-to-secant ratios in [0,lambda] and a flat cell has zero slopes. Each normalized derivative is in the convex hull of 6t(1-t), 3(1-t)^2, 3t^2, and 3(1-2t)^2 when 0<=lambda<=3, so its integral absolute value is one. Minmod along an input line segment is piecewise affine, switching between the two secant inputs and zero. One secant-direction column thus has variation one in its own cell by the same square test, and at most two disjoint, optional neighboring pure Hermite basis terms, each of variation 8 lambda/27 by their single turning points at 1/3 and 2/3. Summing columns and integrating along the line segment proves the global bound, including ties (every continuous piecewise-linear scalar restriction is absolutely continuous). With two knots there are no slopes, with three one adjacent slope can vary, and with four or more both can vary. A perturbation of size 1/4 in the unique smaller positive secant next to secants of size 2 realizes the full number without selector changes, even at lambda=0 or 3. For n>=3, first secants (1,1) force the normalized first-cell derivative to be t[(6-2 lambda)+(3 lambda-6)t]; it is negative just right of zero for lambda>3 and just left of one for lambda<0, giving excess variation. Reviewed check.py and its finite diagnostic scope; no uploaded script was run. This rejection is not a mathematical counterexample.

## originality

FAIL

The principal exact two-input result is already known at unit scale on a broader domain, and the remaining formula is a mechanical specialization and rescaling of its published proof using the classical [0,3]^2 Hermite slope square. The earlier Resultary minimax proof explicitly gives the step-column decomposition, the exact 8/27 integrals, the homotopy bound and a same-secant extremizer. Replacing the two coefficient ranges [0,1] by [0,lambda] leaves the central integral equal to 1 by Huynh's four-corner criterion, multiplies each off-cell term by lambda, and deleting unavailable neighbors changes their count to min(2,n-2). The same extremizer, retaining only the available adjacent cells, gives sharpness. Thus the all-scale formula is not asserted verbatim by the earlier theorem, but its extra cases introduce no new norm calculation. The sharp one-input endpoint check is elementary slope monotonicity on the axis (0,lambda), also not a surviving original contribution.

## value

FAIL

The stability question and its known 43/27 coefficient are scientifically meaningful, but the remaining alterations only count absent boundary cells, multiply previously computed terms by the slope scale, and check the standard monotonicity axis. They do not supply a nonroutine additional stability invariant. Narrowing to the scaled or short-grid cases alone would retain only that mechanical extension, so no valuable distinct repair is supplied.

The dated certificate retains the supplied scientific assessment, sources and limitations.
