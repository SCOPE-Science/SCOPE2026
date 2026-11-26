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

Reassessed the complete corrected RESULT.md under repairs/3. The original proof called an endpoint-deletion overlap a cyclic shift, which is false even for aba and bab. The repaired proof uses P_i=Q_{i+1} (indices 1 to n−1); reversing both parents yields P_{i+1}=Q_i, forcing two-periodicity and the opposite alternating phases. Endpoint deletions give the two outputs; the count vectors force different deleted letters, and internal deletions introduce distinct equal pairs, so no further common outputs exist. Equal outer letters can always be stripped from a common output: a violating endpoint would force identical parents, and deleting an equal outer symbol can be moved inward across its repeat. At length one the base overlap is one and gives no edge. At even length the parity of the output multiplicities specifies the deleted letter, and the mirror-position disagreement proof shows that reinsertion of this letter cannot produce two palindromes. In odd length the two central symbols are distinct exactly off the isolates; the maximal initial run in their two-letter alphabet and the remaining tail are invariant under every edge. Splitting by its last symbol yields two smaller components with exactly one connecting flip, proving the stated spectrum, including r=m and q=2. Radius-one flips give a matching saturating the nonisolates; ordering the two central symbols gives an independent set of the matching bound size. The repaired proof also verifies the one-read example directly. Both frozen checkers and VERIFICATION.md were inspected, not run; their finite checks are not the all-length proof. No numerical claim was changed.

## originality

PASS

On the repaired text, credit prior exact coverage of the ambient edge criterion and the one-read recursion (which nearly gives the two-read recursion by itself). The supported distinct claim is the all-alphabet component spectrum of the retained forest and the sharp two-read capacity with its optimal construction. Neither the pairwise criterion, total edge count, nor the binomial-tree shape alone is the originality basis.

## value

PASS

Palindrome sources impose a natural symmetry and one extra distinct trace changes the possible codebooks. The exact all-q, all-length capacity and a local optimal selection rule quantify that benefit, and the component spectrum explains how the higher read threshold breaks the one-read graph into small trees. The result is valuable beyond a new edge total or another description of a known tree shape.

The dated certificate retains the supplied scientific assessment, sources and limitations.
