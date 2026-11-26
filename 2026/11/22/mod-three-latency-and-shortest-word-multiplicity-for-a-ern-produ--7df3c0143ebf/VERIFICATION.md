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

Reverse preimages of b can add just 0 (set contains 1 but not 0); omitting any nonincreasing inverse b preserves ultimate full coverage by monotonicity. Starting at a target singleton, productive steps leave circular intervals starting at 0. To expand again the interval must start at 1, requiring n-1 inverse rotations. The n-1 growths and n-2 minimal internal runs force W_n at equality. One extra letter is at a rotation boundary or gives an insertion of b into W_n. In the j-th split, the reverse interval at the insertion has length n-j and first point t+1 modulo n. Its endpoint is 0 precisely at t=j; shrinking makes coverage impossible with n total b's. Other interior offsets fix the interval; t=0 doubles b harmlessly, while t=n-1 represents the next doubling or W_nb. This verifies the single-factor family rather than relying on finite testing. On C_3 the post-initial set is {1,2}; a^2 b collapses, while a^0 b and a^1 b fix the set. In a nondivisible split, t=2 mod 3 collapses immediately, t=0 does not, and t=1 collapses exactly when the remaining exponent is 2 mod 3 (n=1 mod 3). Boundary extensions cannot help. At n=3 both factors share unique W_3=baab; n=4,5 and all later nondivisible cases have the eligible (n-2,n-3) split. Of the (3k-1)*2k or 3k*k pairs exactly 2k or k violate t!=j, giving the stated counts. Inspected verify.py and its recorded CHECK_OK; subset-pair BFS n=3..16 and witnesses through 200 are not all-size proof and the uploaded script was not executed.

## originality

PASS

The repaired claim is the literal shortest-word classification and multiplicity, not a new threshold or a new single-factor candidate list. The inspected threshold, table and single-factor antecedents do not provide the exact modular intersection.

## value

PASS

A shortest threshold gives no measure of how many optimal common controls there are. The complete residue-dependent classification reveals one word versus two different quadratic growth laws, uniformly in the larger factor, for the first nontrivial fixed small Černý factor. The count survives independently of the credited latency formula.

The dated certificate retains the supplied scientific assessment, sources and limitations.
