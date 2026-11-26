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

Odd pentagons require at least one frustrated edge each; each edge is counted twice, so at least six edges are frustrated. At equality the frustrated edges are a perfect matching in the face dual. The associated bond signs multiply to +1 on every face and hence on every cycle, so they integrate to one spin assignment up to reversal. Independently I built G(10,2), verified its isomorphism to the frozen edge list, and traversed the entire 2^19-state slice with one spin fixed using Gray-code cut updates. Reversal bijects the two slices. The maximum cut is 24 with 125 winners in that slice, giving energy −18J and 250 ground assignments. BFS and exact spin-product sums for all ordered pairs gave distance numerators (250,−150,50,−30,50,−62) over 250; reversal makes the means zero. For N=250C I computed det(xI−N) by fraction-free elimination at 21 distinct integers, including the four rational roots. Equality at those points certifies the degree-20 factorization (x−8)(x−48)^5(x−72)^4(x−408)^4(x²−944x+22784)^3. Dividing the roots by 250 gives the stated spectrum. The simple smallest root is 8, the row sum of N, and the largest is 472+200√5, proving the ratio and that the uniform line is the unique minimizing direction. Finite-temperature differentiation at zero probe field gives beta times the spin covariance; the finite spectral gap makes the Gibbs measure converge to uniform on the ground set. Thus the result is for the ordered Curie limit, not a derivative of a selected ground-state spin pattern.

## originality

PASS

Credit existing ground-state counts and magnetization sectors, the uniform-mode coefficient, and the implied distance-one and distance-two entries. The reviewed result adds the full distance-resolved local-field response, notably distances three through five, and its exact spectrum and anisotropy; none of the decisive inspected sources gives these on this graph in this ensemble.

## value

PASS

Uniform magnetization measurements only address the uniform direction. The complete covariance quantifies the static response to every local field, establishes the absence of silent modes, and shows that the least responsive mode is uniform despite much larger responses to some nonuniform fields. The exact gap between these responses is a useful benchmark on a natural, strongly frustrated finite graph; the familiar 250-state count and uniform scalar alone are not the contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
