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

The 36 literal length-four factors have 24 active overlap vertices. Contracting the forced paths leaves the bidirected prism; its tree cofactor is 75 and fixed-first-arc BEST gives 75*2^6=4800, with no rotation factor because 0120 appears exactly once. The transposition quotient has cofactor 5 with odd total voltage, so its 5*2^3 rooted tours lift to 40 symmetric cycles. In the three-cycle quotient the total voltage is zero, closing a lift too early. Six unique palindromic triples obstruct reversal, four individually fixed factors obstruct reversal followed by a transposition, and squaring reversal followed by a three-cycle yields a forbidden nonidentity relabeling. Burnside gives 820 and 410. An independent departure-order enumeration verified the witness file, 4800 tours, the full fixed-point multiset (4800 once, 40 three times, zero eight times), and both orbit totals; replay: python3 /workspace/branches/reproduce_frozen_math.py 3.

## originality

FAIL

A distinct indexed Resultary record, 2e6d8e176d7d, independently states and verifies the same full count and stabilizer census for the same 36 literal factors with the same rotation, relabeling and reversal conventions. Its orbit-size statement also yields the same stabilizer proportions. A second distinct record, 000c778d28d0, covers the 4800 count and the witness. These are demonstrable catalogue overlaps, not a finding of earlier publication or historical priority: the matched path dates are later than the frozen path date. The analytical prism/voltage argument is a distinction in proof, not a different counting or symmetry claim in the Finding.

## value

FAIL

The first nonbinary onto-word extension is a natural finite test case, and the prism reduction and cover calculation give an informative structural explanation. However, the submitted exact invariant is fully covered, including the symmetry census; no separate general structural theorem or genuinely new invariant is established as the Finding. The covered census does not meet the incremental value standard for a narrow exact fact.

The dated certificate retains the supplied scientific assessment, sources and limitations.
