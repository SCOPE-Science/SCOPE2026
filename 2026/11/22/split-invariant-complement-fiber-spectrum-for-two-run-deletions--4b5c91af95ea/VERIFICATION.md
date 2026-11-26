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

For a strictly order-preserving deletion of 0^a1^b from (01)^n, each source block leaves F=01, A=1, B=0, or E=empty. The A's precede the B's, and at most one E can occur, after the A's and before the B's. Each adjacent 01 in the output is precisely an F, since the only possible new 01 boundary would require a B followed by an A. Thus the output determines the nonempty tokens. The E-free embeddings give binom(n,k) singleton outputs, disjoint from outputs with E by the number of F's. In the E case the prescribed central gap of s full blocks gives exactly s+1 embeddings; there are k-2 other gaps distributing n-k+1-s full blocks. This gives binom(n-t-1,k-3) for t=s+1 in the stated range, independently of the run split, and puts all full blocks in a single gap for the unique maximal fiber. The sum of histogram entries is the stated output count; to count embeddings directly, increment the selected one-block indices by one so that the combined zero and shifted one indices form a strict k-subset of [n+1]. At n=k-1 only one singleton output occurs, and for n<k-1 there is no embedding. The n=6,k=4 example gives 19,3,2,1 fibers at sizes 1,2,3,4 as stated.

## originality

PASS

Pass for the complete split-independent embedding-fiber law at arbitrary two-run pattern length k>=3, not for already overlapping distinct-output counts at k=3 or for elementary total embedding counts. The strongest restricted overlap matches the k=3 number of residuals but supplies no multiplicity histogram for the target family. A nearby full histogram is for a three-run pattern, not for this family.

## value

PASS

The object is a natural refinement of prescribed complement enumeration: it distinguishes uniquely recoverable deletion embeddings from highly ambiguous residuals. The law determines every multiplicity and its count in an unbounded family and shows that changing the relative run lengths at fixed total does not change these collision statistics. It is stronger than recovering a known short-pattern output count or the immediate embedding total.

The dated certificate retains the supplied scientific assessment, sources and limitations.
