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

Independent replay /workspace/replay/3.py (with forms.py) tests all 1023 forms by the degree-four Macaulay rank criterion instead of the supplied chart Gröbner loops. Euler reduces singularity to the three partials; these quadratics have no projective common zero iff they are a regular sequence, in which case their quotient Hilbert series is (1+t)^3, equivalently the degree-four map is surjective. The replay obtains 336 smooth forms, 154 admissible forms, 392 pencils and eight nets; the mask sets match both frozen outputs. Ordered coset extensions exhaust the subspaces; a four-space would contain 15 distinct nets. The 168 coordinate substitutions give one orbit and stabilizer 21, and each rational member point set is a Fano line appearing once per net. At each rational zero P the tangent restriction along P+tQ has vanishing quadratic coefficient, independently checked as the reverse directional derivative at Q in direction P, with nonzero cubic coefficient. The 48 group elements of order seven partition into eight distinct six-element nonidentity parts of the Sylow groups, one per net stabilizer, establishing equivariance and bijectivity.

## originality

FAIL

The earlier Resultary census gives the complete eight-row projective classification of all smooth nets, including exact basis 100,421,523, orbit size 8 and stabilizer 21 for this very orbit. Restricting the earlier table by the definition requires only testing tangent incidence of its eight explicit representatives' seven members, not classifying new linear systems. Direct crosswalk: in published row order the numbers of tangent-filling members are 4,3,3,7,4,3,0,0; only the identical basis row qualifies. The remaining geometric properties are finite checks on seven already tabulated cubics; the Singer correspondence follows from the orbit and standard Sylow counts. The maximal dimension upper bound also follows from the pre-existing general theorem. This is demonstrable stronger catalogue coverage, not an inference from matching counts or wording.

## value

FAIL

The incidence interpretation is natural, but as a new classification this is a routine filter of eight previously listed representative systems, retaining the very same displayed basis and known stabilizer. The line/flex checks on its seven members and the Sylow consequence do not establish a separate gap beyond that finite lookup and its elementary checks.

The dated certificate retains the supplied scientific assessment, sources and limitations.
