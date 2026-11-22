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

PASS — On a connected graph a primitive two-cycle has complementary first/second firing sets by the Laplacian kernel. For a given binary first firing set S, each vertex has c_v cross-cut neighbors and exactly c_v legal initial chip heights, all independently choosable and weighted by z^{3f+(1−f)(3−c)}[c]_z. The 16-state row-column transfer uses successive binary rung columns; trace T^n/2 counts prism orbits and trace T^n J/2 counts the twisted seam. The anti-row-swap restriction is 6-dimensional and has exact polynomial characteristic factor (λ²−z^10)(λ²+λ z³(1+z)²−z^8)(λ²+λ z⁵(1+z)²−z^12). I independently constructed and symbolically checked this matrix/determinant from the formula, not from saved log, and independently expanded trace coefficients n=3,…,7; signed coefficients are strictly positive on all 4n+1 supported exponents and zero outside, with center +4/−2. Lucas root recurrence yields integer n/(n−j)binom(n−j,j) and all-n coefficientwise sign by the j=0 term. Complementing chip heights by 5−x gives z^10n reciprocity. The finite tests corroborate an all-n characteristic-polynomial argument; n≥3 avoids degeneracies.

## originality

PASS

PASS — Previously published exact unweighted prism versus Möbius period-two total counts and parity signs at z=1 were inspected in full; they cannot imply any particular coefficient sign. General maximum-cut mass-support and cyclic chip-firing mass distributions likewise do not give the entire prism/Möbius coefficientwise disparity. The full primary 2012 Jiang–Scully–Zhang paper treats possible firing patterns and general behavior, not a mass-resolved graph seam-polynomial in inspected text. The exact six-state polynomial identity and strict sign at each mass are a real refinement, with early chip-firing-priority uncertainty retained.

## value

PASS

PASS — The coefficientwise mass sign says the seam twist reorders *every conserved-energy sector* in a contiguous natural support interval, not just total populations; this is a motivated strengthening for a conservative dynamical system. Closed binomial coefficients and unusual size-invariant central coefficient are informative exact invariants with direct use for fixed-mass comparison, rather than numerical extrapolation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
