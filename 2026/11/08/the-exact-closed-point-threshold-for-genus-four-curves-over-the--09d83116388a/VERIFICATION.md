---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
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

The degree-nine squarefree polynomial x^9−x gives a smooth genus-four hyperelliptic normalization with one rational point at infinity. Over F9, x^9−x=0 so N2=10. For x in F81 outside F9, v=x^9−x obeys v^9=−v, v^40=−1 and is a nonsquare, giving N4=10 and B4=(N4−N2)/4=0. Independently enumerated the 81-element field using u^4+u−1, confirming nine-element F9 and no additional points. Aubry–Herbaut–Monaldi Proposition 2.2 implies B_r>0 whenever (q^(r/4)−1)^2 >=2g; exact inequalities at q=3,g=4,r=5 establish the upper threshold and monotonicity covers r>5. This proof uses the published theorem as an input, not an unverified finite extrapolation.

## originality

PASS

The primary source giving universal closed-point bounds states exact thresholds for genus <=3 but not rho(3,4); its upper bound alone does not give the required degree-four obstruction. Xarles counts genus4 curves only over F2, a distinct base field; the nearby Resultary exact thresholds concern F2, F4 and F5, not F3. A classical hyperelliptic point-count identity may independently imply the lower witness and is recorded as a priority risk.

## value

PASS

The next genus beyond published exact rho tables gives a natural finite-field arithmetic invariant, not a contrived small-sample check. The theorem closes the exact universal upper/lower gap using a structural trace-zero nonsquare obstruction rather than a brute-force genus-four census.

The dated certificate retains the supplied scientific assessment, sources and limitations.
