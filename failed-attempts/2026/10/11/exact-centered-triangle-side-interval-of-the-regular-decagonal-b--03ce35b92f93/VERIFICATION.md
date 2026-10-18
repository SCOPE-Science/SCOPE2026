---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

Read the actual RESULT.md f46f740a2da14fd8355cb7134ec917183a345674 and full exact-field source verify.py 73950ba74ee217c5ba31add822baa24600e9e932. Substituting x=u,y=-v gives precisely N(x)=N(y)=N(x-y)=1 and objective N(x+y), valid both directions. The exact constraint polytope P in R^4 has thirty linear inequalities from ten facets in each of three blocks; any unit pair lies on at least one face F_ijk for 1000 possible triples. The inspected rational-Q(sqrt5) Gaussian solver tests all triples, excludes rank-deficient viable triples, clips each affine line by all inequalities, asserts exactly sixty nonempty positive-length segments, and computes output maxima at endpoints and minima additionally at all pairwise upper-envelope intersections. This is an exhaustive finite polyhedral certificate (not a sample); its logic and algebraic sign comparisons were checked structurally. Independently rebuilt and executed a second exact-rational Q(sqrt(5)) tight-facet enumerator without using the source algorithm as a black box; it independently reproduced all 1000 triples, 60 nonempty positive-length segments, zero rank-deficient triples, and the global endpoints (9−sqrt(5))/4 and 4−sqrt(5). Independently substituted the two claimed attaining pairs into all 10 signed facets using SymPy exact radicals: N(x)=N(y)=N(x-y)=1; their N(x+y) equal the stated values. The independently read published analytic three-branch classification of the SAME unit-pair constraint also confirms these extrema.

## originality

FAIL

Decisive direct statement coverage by a DIFFERENT published Resultary result, independent of titles and constant names: its full proof establishes exactly the same sharp interval for N(x+y) when N(x)=N(y)=N(x-y)=1 on the identical affine-regular decagon. The centered-triple substitution is invertible; therefore both new JL and YJ values follow immediately from already published endpoint bounds and sharp equality witnesses.

## value

FAIL

The original object is natural and the exact fixed-decagon interval is mathematically meaningful, but this package contributes only an alternate enumeration of already published exact endpoints for the identical norm and constraints. It neither establishes a new structural classification nor changes the invariant or range; under the known-table-recomputation standard, correctness and reproducibility do not give the duplicate a separate scientific-value contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
