---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
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

The rational witness is correct. An independent exact symbolic replay (branches/replay_05.py) constructed the integer conics from the stated coefficients and verified all five first-nullcline brackets and the second-nullcline margins by sign of the cleared quadratics and strictly positive denominators. The margins exceed 1/1000; the decreasing-in-x first response at the right endpoint keeps its positive branch defined throughout the bracket range. The primitive resultant is square-free of degree four and exact root counts give one in each requested x-interval; the optional numerical pairs agree. The analytical upper bound for the witness follows because the nonzero first determinant turns Q1 into an irreducible affine hyperbola and the brackets rule out any common component. Bézout makes four the total multiplicity, so the four intersections are transverse. An open neighborhood keeps the coefficients positive, the determinant nonzero and all strict sign brackets, giving exactly four throughout. The broader wording about a sharp upper bound needed to exclude nonisolated points: the admissible choice phi1=phi2=2/(1+x+y) has a segment of positive equilibria. The repaired RESULT.md and SLOGAN.txt state the precise bound on isolated equilibria and prove it: an arbitrary nonempty positive nullcline comes from an irreducible conic for independent density forms or a single line when they are proportional; distinct curves intersect at most four times, and a shared positive branch has no isolated points. The corrected scope preserves the witness and does not assert attraction or full-model equilibria. The supplied verifier was read, not run.

## originality

PASS

The distinct supported result is an exact, positive, four-intersection witness with an open neighborhood in the specified reciprocal-affine family, not the response form, isocline geometry or upper bound. Bravo de la Parra–Sanz gives the identical form and upper bound but reports an unsuccessful numerical search for the four-positive case. An earlier same-form fast-dispersal reference is now acknowledged explicitly; no universal priority is asserted. Its unavailable full text leaves a material but unverified overlap risk, not a negative finding. The unrelated four-interior-equilibrium Allee-effect example does not imply four for this constrained family.

## value

PASS

The four-positive case is a concrete missing extremal regime identified in the published model study, not an arbitrary parameter slice. Exact attainability and transversality give a useful reproducible test case and a nonzero open parameter regime, without conflating persistence with attraction. Qualifying the bound by isolation resolves the degenerate common-curve case and retains this scientific contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
