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

PASS

A completed one-run bracketed by zeros has length km. Its visible preceding zero-run cannot exceed m, and if that zero-run is left-bracketed by a one it must have length exactly m (too short would expose the second forbidden family, too long the third). For a terminal one-run following a left-bracketed zero-run of length a, its visible length is at most ka. Conversely, these constraints let one fill the first and last partial runs into generators: an initial one-run can be a suffix of any sufficiently long generator, an initial zero-run can be lengthened as required, and a terminal zero-run can always be completed. This also treats words consisting of a single run. Thus avoidance suffices. Both one-letter end deletions of every proposed obstruction occur, including 0^m1^(km)0 across a generator boundary and 0^(m+1)1^(km) in a larger generator; this proves minimality. The lengths are r+2 and (k+1)m+2, giving the series, including cancellation for k=1. Intersecting with 10^+1^+ and pumping in the initial 1/zero-run proves nonregularity for every k. Bounded but infinitely often positive counts give growth entropy zero. In a separate bounded reproduction, I closed the set of concatenation suffixes of length at most 15 under appending generators with m<=16, collected factors through length 16 from each suffix-plus-generator, and identified absent words with admissible prefix and suffix of length one less. Larger generators can be replaced by m=16 for this bounded factor census (all observed runs or run fragments in such a generator still fit). The family lists matched for k=1,...,6, with respective cumulative counts 14, 15, 16, 15, 16, 16. This check does not prove the unbounded statement. The frozen checker was inspected, not run.

## originality

FAIL

An earlier dated distinct Resultary record provably states the same full theorem on the same coded system. The failure is existing exact coverage, not a proof defect or an unavailable source.

## value

FAIL

The complete minimal-obstruction description would be useful for this independently motivated family of non-sofic coded shifts, but as a proposed narrow exact invariant it is already available, as are its length and nonregularity consequences. The frozen record supplies no distinct scientifically useful remainder.

The dated certificate retains the supplied scientific assessment, sources and limitations.
