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

The distinct-word fiber and counting formulas hold. At each length, sliding windows realize every one-count between the extrema. Extension and shortening show that the extrema are equivalent to shortest lengths reaching specified one-count lower bounds and longest lengths respecting upper bounds. The relevant shortest lengths min(b,c)+2 and b+c+3 determine the unordered inner pair; n−1−min(a,d) and the outer-gap sum determine the unordered outer pair. Among the two nonreversed orders with both pairs unequal, write A>α for the outer gaps and B>β for the inner gaps. The only possibly differing maximum is the longest factor with at most one one: minus one, the two maxima are max(A+B,B+β) and max(A+β,α+B,B+β). They coincide iff β≥A. Equal pairs already collapse the candidate list to the reversal orbit; the conditional formula is correct as a set of distinct words, not an unqualified iff for membership of an inner-swapped tuple that may equal a listed word. For n=3 the all-zero-factor maximum needs the convention 0 if absent. Sorting a four-word representative as a<d≤b<c gives n=7+4x+3y+2z+t with all four parameters nonnegative, proving the generating series and first fiber. Palindromes give S_n, partitioning the words gives the remaining counts, and the pole at 1 of order four yields n³/144 and the limiting fraction 1/6; other poles have order at most two.

## originality

FAIL

A distinct inspected indexed record (Resultary 2026/11/8, defdb2ae056f) gives the same all-length weight-three fibers and their enumeration for exactly the same observation. Its formulas imply all the frozen counts and the same limiting fraction. This is demonstrable equivalent coverage with no distinct surviving assertion, not a finding that the later-dated path predates the frozen record or evidence of dependency. The earlier five-run record independently already covers the length-seven onset and witnesses, though not the full classification.

## value

PASS

As mathematics, a full inverse-image classification for the joint binary window extrema at weight three identifies exactly when reversal is not the only ambiguity, supplies the sharp smallest example, and shows that ambiguity persists at positive limiting prevalence. It addresses a natural reconstruction boundary, not just a one-off finite check. This value judgment does not supply distinct content beyond the indexed equivalent.

The dated certificate retains the supplied scientific assessment, sources and limitations.
