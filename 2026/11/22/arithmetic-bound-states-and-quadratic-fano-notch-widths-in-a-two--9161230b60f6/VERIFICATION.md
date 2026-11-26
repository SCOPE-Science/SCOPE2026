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

For E=2cos(k) in the open band the lead recurrence has only the two oscillating solutions, so an embedded square-summable vector vanishes on the lead and hence at the coupled root. Each Dirichlet arm eigenvalue is simple with nonzero endpoint amplitude. A dark state requires both arms, and cancellation at the root leaves one vector per common frequency. The sine grids meet at s/d for s=1,...,d-1, with d=gcd(m+1,n+1). The endpoint resolvent is the minor-to-determinant path ratio; eliminating the arms and root yields the point potential 1/H and T=(4-E^2)H^2/[1+(4-E^2)H^2]. At an arm eigenvalue the arm solvability condition instead forces the root amplitude to zero; a resonant arm amplitude can enforce the root equation while lead scattering is free. Thus the limiting value T=1 is physical including at the undetuned coincidence. In the split interval H has opposite infinite endpoint limits and H'>0. To check the center asymptotics, set u=(E-E_s)/delta and multiply H by delta: on compact subsets of 0<u<1 this is -A/u-B/(u-1)+O(delta), where A,B are the positive sine-squared residues. The limiting root at u=A/(A+B) is simple; the remaining resolvents are analytic near E_s, giving u=A/(A+B)+O(delta). This yields the length ratio and H'(E_*)=(A+B)^3/(AB delta^2)+O(delta^-1). Throughout the interval the uniform lower bound H'>=(A+B)/delta^2 suffices for uniqueness against the bounded derivatives of the two half-height curves; a two-sided order estimate up to the poles, as the wording may suggest, is not needed and is not uniform. On the delta^2 window the root stays a distance of order delta from both poles, with H''=O(delta^-3), so Taylor expansion gives H(E_*+Gamma delta^2 x) -> x/(2 sin(theta_s)) and reflection -> 1/(1+x^2). This yields the two local half-widths separately, with Gamma as stated and Gamma=1/16 for m=n=1. Replay: RESULT.md lines 25–69, especially the residue and centered-rescaling computation. The uploaded checker was inspected, not executed; its width tests are finite comparisons with the coded coefficient, not a symbolic or exhaustive certificate.

## originality

PASS

Credit is limited to the explicit joint split-window classification for uniformly detuned open path arms, particularly the sharp real-axis linewidth and symmetric scaling profile at each arithmetic common mode. The general exact scattering mechanism, dark-state arithmetic, and quadratic narrowing in other single-contact systems are substantial prior ingredients rather than independently new principles. The strongest same-day triangular-bouquet match has a different local singularity and does not specialize to this claim.

## value

PASS

The precise real-axis width distinguishes the distances between transparency points (order delta) and the observable half-height notch (order delta^2). An explicit coefficient resolves how the two open path lengths and common-mode index set the much smaller scattering scale, which is not supplied by dark-state counting alone. The result is useful as a fully specified benchmark for one-channel scattering, without claiming generic new Fano physics.

The dated certificate retains the supplied scientific assessment, sources and limitations.
