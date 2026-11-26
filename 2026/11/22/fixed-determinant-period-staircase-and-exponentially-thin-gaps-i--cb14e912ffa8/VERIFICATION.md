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

Summing the finite Green sequence ∑_{j=0}^n r^j sin((j+1)θ)/sin θ gives the claimed phase and amplitude, with A(0)=(r−1)^2. The zero of Φ_n−π is at π/(n+1−1/(r−1))+O_r(n^−4), and the growing amplitude means each target root is an angular displacement O_r(r^−n/n²) above it. For either target the crossing equation is strictly monotone in a phase band of size O(1/n) around π: the phase derivative is n+O_r(1) and the arcsine derivative is O_r(r^−n). Subtracting the equations for the two target levels gives an angular separation asymptotic to (r−1)π/(r^{n+3}n²); multiplication by 2r sin θ gives 2π²(r−1)r^−n/(r²n³). Consecutive phase roots have angular separation asymptotic to π/n², giving 2rπ²/n³ and then the stated ratio. In the open window, the two threshold signs give X_n<0 and X_{n−1}>r^−2. For an explicit check of the earlier signs, at the upper angular endpoint the (n−1)st phase is at most π+O_r(r^{−n+1}/n). Hence for j≤n−2 the phase is below π by subtracting at least θ of order 1/n; fixed sufficiently large j also have positive phase, and the finitely many smaller j have positive limits from the finite Green sequence. The proof's alternative wording about being below π at the last positive iterate need not hold for j=n−1; that sign is supplied separately by the threshold, as above. The actual orbit therefore first reaches two negative coordinates at step n and resets in the next two steps. Nothing before then is (1,1), since the second coordinate is less than 1 after every preceding strictly positive first coordinate, and the first coordinate at step n+1 is negative. Strict signs give a neighborhood with the same itinerary, and the two negative branch maps compose to a constant reset, stronger than just zero derivative.

## originality

PASS

Qualified to the fixed-D all-large-n staircase and its sharp window and gap constants. The reset map, two-step reset, crossing equations, and conditional n+2 return are prior. The exponential-gap mechanism is also prior on a different path; the matching ratio at the shared limiting point is not by itself distinctive.

## value

PASS

Fixed determinant is a natural experimental and theoretical slice already present in the numerical literature. Certifying every sufficiently high primitive period with nonzero width and extracting the exponential separation from its polynomial-width neighbor gives information that finite threshold diagrams can miss. The constants separate trace-only tuning from simultaneous trace/determinant tuning.

The dated certificate retains the supplied scientific assessment, sources and limitations.
