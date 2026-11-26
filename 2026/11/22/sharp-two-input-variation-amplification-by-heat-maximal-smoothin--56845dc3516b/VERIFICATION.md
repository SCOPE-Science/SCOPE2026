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

For the combinatorial P3 Laplacian the constant, odd (1,0,−1), and even (1,−2,1) modes have eigenvalues 0,1,3. For mode coefficients m,u,v and z=e^(−t), the three coordinates are m+uz+vz^3, m−2vz^3, m−uz+vz^3. Including z=0 does not change the supremum. In the input quotient V=2 max(|u|,3|v|). On any segment, each coordinate supremum is Lipschitz as a maximum of affine functions of the segment parameter. Where its segment derivative exists, it equals the slope of any active affine function (that function supports the maximum there); this proves the segment argument even on exceptional lines. With active endpoint parameters x,y in [0,1], and beta in [0,1] for the middle branch max(0,−2v), the two oriented edge derivatives are x du+(x^3+2 beta)dv and y du−(y^3+2 beta)dv. Dualizing the output l1 norm gives two cases: (3(x+y)+|x^3−y^3|)/6 ≤ 1, and (3|x−y|+x^3+y^3+4 beta)/6 ≤ 4/3. For x≥y both increase in x, so set x=1 and use 3y−y^3≤2 and y^3≤3y respectively; the reverse ordering is symmetric. Absolute continuity along the segment gives the global estimate. At the two positive rational inputs the first endpoint cubic is strictly increasing and the last strictly decreasing; the maxima are exactly (13,12,10) and (15,11,10), with input/output variations 3 and 4. For P2 the output edge difference is half the input edge difference, from clipping both coordinates at their mean. For a fixed P3 heat step the odd and even quotient modes decay by e^(−t) and e^(−3t), so its norm is exactly e^(−t), attained on the odd mode. Replay of exact witness: python3 /workspace/checks/frozen_exact.py 2. The submitted checker was inspected, not executed: its numerical witness tests and time grids are supplementary. For signed data the proof only extends to a supremum without taking input absolute values.

## originality

PASS

The checked comparison supports a distinct coefficient for the nonlinear supremum over time on P3, not a known bound on a linear heat step or a one-input smoothing bound. The P2 identity by itself is elementary and is treated as the boundary comparison, not the main novelty.

## value

PASS

The three-site result is a minimal nontrivial example in which maximizing over a contractive heat family makes perturbations expand. Its exact coefficient and strictly positive witnesses are a useful benchmark for nonlinear maximal-semigroup stability. The P2 comparison shows this is a genuine onset for unit open paths, not an arbitrary three-site parameter slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
