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

Re-derived the side-facet equation using the base vectors' mutual product −1/(d−1), then projected the origin onto that hyperplane and onto the base plane. The side feet have a regular base at positive height with nonzero radius, and the old base foot is the new apex at negative height, so the origin is strictly between the base centroid and the apex and hence interior to a full-dimensional simplex. Central reflection preserves the fixed origin and commutes with projection, so reorienting after each step legitimately gives the stated rational map on q,t>0. The regularity condition is q=(d−1)/(d+1) by equating lateral and base edge squares. Differentiation at (q,t)=((d−1)/(d+1),1/d) gives the displayed entries, trace −2/d, and determinant 1. A root of unity would make the sum of the eigenvalue and its reciprocal a rational algebraic integer, impossible here. Cayley–Hamilton gives (J^N)₁₂=J₁₂ sin(Nθ)/sin θ; a zero would force the multiplier to have finite order dividing 2N. The chain rule thus gives a nonzero centered derivative for every N, and the countable union of isolated zero sets on the connected open altitude yields simultaneous nonreturn. Independently evaluating (q,t)=(1/2,1/9) gives (2,1), (1/8,1/3), (2/9,1/11), (121/50,11/19); the fourth squared lateral/base ratio is (1+1/q)/3=57/121, as in the cited tetrahedral computation.

## originality

PASS

The four-pedal tetrahedral counterexample and the local four-step tetrahedral obstruction are credited as covered cases. Neither those results nor the planar and concentric spatial return theorems give the all-dimensional, all-positive-time co-countable nonreturn statement or its nonresonant linearization.

## value

PASS

The natural question raised by exact planar and isolated tetrahedral pedal behavior is whether another finite time restores the simplex shape. The theorem gives a strong negative answer for generic points along an altitude in every higher dimension, not a list of nonreturn examples at selected times. The two-variable recurrence and non-torsion spectrum explain the distinction and may be useful in studying exceptional positions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
