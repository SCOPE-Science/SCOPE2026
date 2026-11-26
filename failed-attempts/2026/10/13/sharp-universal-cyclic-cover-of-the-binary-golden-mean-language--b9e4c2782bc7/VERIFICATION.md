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

The cyclic host avoids 11 across the join, but the required n-factors need only avoid it internally. A closed walk in the order-(n-1) overlap graph spells the cyclic host by reading the first letter at each step: overlap identifies the subsequent letters modulo the walk length. Conversely the successive windows of a cover traverse all arcs. Strong connectivity follows by going through all zeros. Removing one copy of every arc leaves a nonnegative integer flow of divergence +1 at vertices starting 0 and ending 1, -1 at vertices starting 1 and ending 0. Decompose into unit source-to-sink paths and cycles; r initial zeros force at least r steps on each such path. Appending r zeros achieves r and matches each sink bijectively by reversing the move on its terminal run. Connectivity and balance give an Euler tour. Independently, with m=n-1, for k=1,...,m-1 there are F_(m-k) sources with at least k leading zeros (choose an internally admissible suffix ending in 1). Summing yields F_(m+1)-1; the empty sum at n=2 is correct. There are F_(n+2) required arcs, hence the stated length and surplus. A separate literal cyclic-word enumeration (`python3 /workspace/branches/frozen_math_checks.py`) confirmed minima 3, 6, 10, 17 for n=2 through 5; it is not used for the all-order conclusion.

## originality

FAIL

A distinct same-day Resultary record, 50305dee27be, contains the identical all-order formula and the same sharp run-length lower bound, bijective zero-append augmentation and Eulerian construction, explicitly as proved background to its census. This establishes equivalent coverage, not which author or record was first. The October 18 overlap corroborates coverage and adds a more specific window-multiset construction; it does not establish earlier priority. No distinct scientific remainder survives in the assigned statement.

## value

FAIL

The shortest cycle length of this natural language is a meaningful invariant in itself, but the assigned contribution duplicates the exact formula and constructive proof already verified in a distinct indexed record. It supplies no new optimizer classification, count, or independently useful structural fact beyond that coverage. A different summation of the same augmentation cost does not rescue it.

The dated certificate retains the supplied scientific assessment, sources and limitations.
