---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

For a labeled simple prism with n>=3 the two neighboring columns are distinct even at n=3. In each row of a missing vertex, the left and right row bits plus its rung bit give exactly the number of selected neighbors. Adjacent distinct nonzero codes would force a missing vertex with two such neighbors, so no ignored pair is used by any valid cyclic word. Conversely the overlap transitions among the ten retained pairs impose exactly these row tests. A closed walk with fixed initial column is one labeled word and each selected vertex contributes one z, so the trace counts subsets without a rotation factor. Independent exact integer-polynomial subset expansion and direct adjacency enumeration at n=3,4 in /workspace/branches/95334656-7bb5-4b48-89fb-d50f7e87acdf/check_prism_independent.py (output check_prism_output.txt beside it) reproduced det(I-tM)=q2 q5 and both stated base polynomials. Jacobi's formal determinant differentiation gives the trace series. The first two formal traces are (1+2z+z^2) and (1+2z^2+z^4), which are not graph cases and are removed. The order-seven recurrence is for the entire polynomial sequence, so fixed-weight coefficients can couple to other weights under coefficient extraction. Independently, any nonempty complement has induced minimum degree two or more and contains a cycle; shortest-cycle vertex sets attain the lower bound on complement size. The only triangles are the two n=3 rims. For n>=4 a four-cycle either is a rim (only at n=4) or uses two adjacent rungs; no four-cycle can use four distinct rung edges. This gives maxima 3,4,2n-4 with counts 2,6,n. Large-n validity is proved by the local trace and girth arguments, not inferred from either bounded script.

## originality

FAIL

A distinct, inspected Resultary finding gives the same complete labeled-prism enumeration in complementary variables. The generating factors agree identically under the weight reversal, not just at z=1 or in a few small cases. Its full polynomial entails both exceptional and general extremal counts; it also derives additional coefficients and an asymptotic. Catalogue dates and the distinct record identities do not establish priority or the relation between the two derivations. This decision records equivalent existing mathematical coverage, not earlier authorship.

## value

FAIL

A complete cardinality enumerator for a natural family would be useful if distinct, but the matched record already gives this one for every circumference and size. Reversing weights and extracting the largest proper sizes contributes no distinct enumerative invariant. The direct extremizer description follows by the elementary shortest-cycle argument and does not rescue the overall claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
