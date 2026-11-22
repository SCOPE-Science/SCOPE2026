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

At N=2m the full even-modulation subgroup sums to m times the congruence condition j≡k mod m. The resulting 2-by-2 coordinate blocks Q_j have determinant D=r^(2m-2)(1-r²)²>0 and endpoint-maximal trace T=(1+r²)(1+r^(2m-2)), so their extremal eigenvalues are exactly the claimed sharp frame bounds. Independently assembled full complex Gabor synthesis/frame matrices for nine (m,r) settings and checked both extremal eigenvalues. Algebra gives T/sqrt(D)=2 coth(s) cosh((m-1)s), and log derivative (m-1)tanh((m-1)s)-2/sinh(2s) crosses zero once. Monotone root comparison implies (m-1)s→z* solving z*tanh z=1, with sharp condition coefficient 4/(z*²-1). m=2 yields r=√2-1 and κ=(2+√3)². Finite sample checks are supplemental to the general block argument.

## originality

PASS

Asipchuk–De Carli–Rodriguez (2026) prove finite Gabor block equivalence whenever a sampling set is a subgroup, precisely the structural input used here, but not the explicit circular graph-distance exponential profile, maximally ill-conditioned block or global unique taper asymptotic. Faulhuber–Shafkulovska study continuous oversampled exponential Gabor frames rather than the critical finite cycle. Resultary geometric cyclic one-sided exponential and radial placement results are close but use respectively g(j)=rho^j and determinant/placement optimization, not this exact symmetric profile and condition number. Older polyphase formulas may cover parts.

## value

PASS

Positive circular exponential windows are natural localization profiles for discrete Gabor reconstruction. The theorem gives sharp all-N stability and identifies a unique conditioning optimum, proving both endpoint failure and unavoidable quadratic optimal condition deterioration. The exact growth constant is useful without claiming a new general block theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
