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

For a proper square board, a non-cell colour occurs in the open neighbourhood once for each endpoint palette containing it; the cell colour occurs zero times. Thus defects are precisely equal row and column palettes. In the named n+1 palette this means equal omissions, including with an unused colour. Each colour occupies a matching of size n-a_s on both sides, so the omitted rows and columns of that colour have equal sizes and induce all a_s² defective cells of that component. These components partition both index sets; Σa_s=n. The nonnegative integer terms a_s(a_s−1) give the bound and exact equality criterion; parity follows modulo two. Deleting row and column 0 of the addition table modulo n+1 leaves respective omissions i and j, so just the n diagonal cells are defective. A complete cyclic Latin board with one unused colour realizes n². The n+2 chromatic background follows from the AVD bound and the obstruction. RESULT.md lines 19–33 suffice for every n≥2. The supporting verification/check_rook.py was inspected, not executed; its direct multiplicity checks and enumerations at n=2,3 are only finite corroboration.

## originality

FAIL

The earlier 2026-10-13 rook-graph odd-colouring proof already gives both the per-cell palette test and equality of every row/column omission count. Because multiplicities in this graph are at most two, odd and singleton witnesses are identical. Counting all pairs in the earlier argument instead of just one mechanically gives the bicliques, their sum-of-squares size and the equality criterion. The two endpoints use routine restrictions of the cyclic addition table. This is mechanical coverage, not a claim that the earlier source states the formula verbatim. The same-day proper conflict-free record separately confirms the two ingredients but is not used to infer priority.

## value

FAIL

The subthreshold failure count is a natural diagnostic, and its concise presentation is useful, but the complete defect relation already follows immediately from the earlier rook proof. Counting its blocks, using a_s²≥a_s, and dropping a row and column of the cyclic table do not supply an independently substantive new exact fact. No stronger enumeration or classification of the actual minimizer colourings is proved.

The dated certificate retains the supplied scientific assessment, sources and limitations.
