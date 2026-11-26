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

Reconstructed the certificate for every integer d>=3 and real t>0. Write v=e1+e2, k=t(t+1), s=2t+1, m=d-2 and D=ms²+2. The endpoint tv has barycentric weights (1,t,t)/s at 0,e1+tv,e2+tv. All other endpoints are exposed: select each basis point uniquely with a positive maximum coefficient while choosing the sign of the sum of the first two coefficients to select the segment endpoint; a strictly negative objective exposes 0. For the d stated contacts, equal distances reduce to B=sA-k, and the barycenter condition to 2A/s+mB=1. This gives the stated A,B and strictly positive weights A/s,A/s,B,...,B; the first two columns have determinant s, and the other columns are independent standard basis vectors. The common squared radius is 1-2B+2A²+mB² and reduces to the stated polynomial quotient. Subtracting squared-distance scores ||z||²-2<c,z> gives clearances 1-2B at 0, 2(A-B) at unshifted e1,e2, 4tA-2t² at shifted e_j for j>=3, and 1-2B+4tA-2t² at tv; substitution gives the stated formulas with strictly positive numerators throughout the domain. The weighted squared-distance identity at any competing center gives R² plus squared displacement from c. For the diameter, the mixed difference e_i+tv-e_j has squared norm 2t²+||e_i-e_j||²+2t v·(e_i-e_j). Its maximum needs i among 1,2 and j>=3, and all other mixed differences, distances from 0, and within-copy distances are strictly smaller. Strict convexity in either point excludes nonvertices as equality cases for both the enclosing sphere and the diameter. The contact and diameter-graph counts and t=1 specialization follow, including m=1; t=0 is excluded. Replay: frozen RESULT.md equations and the score identity above; check_pentasm.py and VERIFICATION.md inspected but no frozen code run. Finite checks are not used as proof.

## originality

PASS

The exact metric theorem for the prescribed orthonormal-coordinate family survived comparison. The pentasm construction, unit-displacement realization, and smallest-ball certificate technique are known. The closest distinct indexed metric result has a different radius-diameter relation and different equality structure, so is not a stronger theorem covering this family.

## value

PASS

Pentasms are a named few-vertex family from polytope classification, and the orthonormal realization and positive scalar displacement are natural. A radius computed once would be routine; this result instead identifies a fixed minimal support simplex with strictly positive slack at other vertices for the entire positive-parameter family, and shows all and only its contacts are endpoints of diameters even though radius is not half the diameter. The complete metric classification is useful for exact containment witnesses and diameter-graph examples without rerunning a dimension-dependent ball search. It does not transfer to arbitrary realizations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
