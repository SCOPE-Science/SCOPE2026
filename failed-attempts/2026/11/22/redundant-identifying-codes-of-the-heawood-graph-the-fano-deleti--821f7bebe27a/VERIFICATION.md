---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

FAIL

Under the frozen Finding's literal definition (for every selected s, S minus s is identifying), S=∅ qualifies vacuously. This contradicts the no-large-omissions assertion, the polynomial's zero constant term, and minimum size ten. In fact, with that literal condition ∅ is the only inclusion-minimal valid set. Step 1 omits this counterexample. The C++ checker explicitly filters out the zero mask via `if(ok && c)`; the Python checker also excludes it by its stronger two-selected-elements tests. For the standard convention requiring S itself to be an identifying code, the mathematics checks out: the only forbidden triples for omissions of size at most four occur in a closed neighborhood or in the four-element symmetric difference at an incidence. A pure triple is forbidden precisely by collinearity or concurrency; in a mixed triple two incidences violate domination, zero incidences violate the four-element symmetric-difference test at the intersection of the two lines and its join to the point, and one incidence passes both tests. This yields the cap and matching four-types and excludes mixed five-sets and pure five-caps. Independent script /workspace/review-evidence/heawood.py tested all 16,384 subsets directly by deleting one vertex and comparing traces, rejected the one vacuous candidate by requiring nonemptiness, matched every corrected feasible mask to the geometry and found the stated polynomial, 98 inclusion-minimal codes, and group/orbits 336 and 14+84. This validates the conventional version only; no corrected claim is submitted because substantive novelty does not survive.

## originality

FAIL

Distinct published Resultary record c643059055bf covers the same conventional one-erasure Heawood problem, the minimum, the full cardinality polynomial and the exact 14+84 geometric types. Its proof is finite and exhaustive; a different proof is not a distinct claimed invariant. The remaining triple classification, minimality and symmetry are elementary consequences of the matched polynomial and family, detailed below. Same-day dates do not establish which result was first; this is a statement-coverage judgment, not a chronological priority claim.

## value

FAIL

The Heawood one-failure configuration census is motivated, but the precise census and optimum geometries are already supplied by the matching result. The residual observations are a direct shadow count and basis-transitivity consequences of that geometry, not an independently needed new invariant. Fixing the empty-code definition alone would not rescue the finding.

The dated certificate retains the supplied scientific assessment, sources and limitations.
