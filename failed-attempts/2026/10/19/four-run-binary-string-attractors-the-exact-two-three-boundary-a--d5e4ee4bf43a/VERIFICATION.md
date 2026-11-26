---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

Both singleton letters must be hit and 10 occurs only at the central B/C boundary, so the outer-run pair is impossible. Longest unary factors force the stated length dominance in each remaining run pair. In A/B the 10 test forces the last B position and 01 forces the last A position unless b=1; reverse-complement gives C/D. For B/C the 10 and 01 tests give the two endpoint disjunctions. All 01-type factors whose exponents fit both boundaries are covered by the 01 disjunction. The two one-boundary-only regimes are decided by their shortest distinguishing factors, 01^(d+1) and 0^(a+1)1, which give t<=d+1 and z>=c-a. Every factor passing through the central transition contains both endpoints of that transition and is met. The middle-run count follows by taking b=1, c=1, or both greater than one; in the last case only offsets (1,1) and (b,c) can remain. When b>=d the last positions of A,B,C hit all three boundaries and include a longest run of each letter. Otherwise the last of A and the first positions of C,D do the same. Thus the minimum is three exactly when all three two-position families are empty, giving the two claimed regions including the strict and one-unit boundaries. Independent direct occurrence-interval testing confirmed every predicted pair and the three-position witnesses on 260 tuples: python3 /workspace/branches/exact_review_checks.py 4. The frozen checker was inspected, not executed. Neither finite box substitutes for the arbitrary-run argument.

## originality

FAIL

A distinct indexed Resultary theorem explicitly gives the identical two-versus-three boundary, every two-position witness and its count on the identical positive four-run domain. Its four families are an endpoint split of the frozen three, not different solutions. This establishes full catalogue coverage; it does not establish priority or provenance. The matched catalogue path is later, and the frozen verification note assigns no first-public date to the new theorem.

## value

PASS

As mathematical content the result explains exactly when the alphabet-size lower bound is attainable in a natural alternating run family, including the one-unit thresholds that coarse run-length dominance misses. A fixed number of comparisons replaces enumeration of factors and gives all two-position witnesses, not just the optimum size. This is useful content but not a separate contribution beyond the exact matched record.

The dated certificate retains the supplied scientific assessment, sources and limitations.
