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

For any point in a cyclic gap its nearest surviving vertex is an endpoint, and the furthest such point is the midpoint of a largest gap. This gives the exact planar support minimum cos(πg/n), including g=n for a singleton and zero for a semicircle gap. Orthogonal decomposition lets each planar support be minimized separately at fixed nonnegative component lengths. For positive supports the increasing/decreasing terms in the maximum balance at the minimum; for negative supports one maximizes the smaller of the two absolute contributions, again by balancing. If the signs are mixed or a support is zero at least one contribution is nonnegative, and a pure direction in the nonpositive factor attains zero. If one factor is absent the remaining length varies in [0,1], giving min(0,r). A negative planar support needs g>n/2; with d deletions g<=d+1 and equality means all deletions occupy one gap. At d=floor(n/2) this is exactly the cyclic block condition, with a unique largest gap; the positive lengths at the unique critical radial balance force both midpoint directions. Emptying a factor costs strictly more than its own threshold and the other factor must still be negative. This gives the global minimum count, the pq sets and the sine factors. In S_4,5 positivity requires an intact square and at most two pentagon deletions, with two permitted only when nonadjacent; negativity through k=4 consists exactly of the 4×5 adjacent-block pairs at k=4. Subtracting from binomial totals gives all zeros. Independent bounded replay by enumerating the subsets of {0,...,8} of sizes 0 through 4, computing cyclic gaps and applying the signed formula, returned the five stated triples and critical cosine −0.28315848617949646; sign decisions can be replayed exactly by comparing twice each gap to its polygon size. Equality of the positive and negative planar magnitudes yields the complementary angles. The replay is finite; the analytic argument establishes the universal result. VERIFICATION.md, verify.py and verify_hulls.py were inspected, not run. The volume-optimality context was checked in the cited preprint; full deletion and nonorthogonal configurations are outside scope.

## originality

PASS

Best-of-knowledge pass for the signed residual covering formula and erasure classification. Do not credit the intact covering cosine or the square–pentagon volume optimum as new. The intact closest match does not reach post-deletion support parameters of either sign, and the other competing results measure different invariants or use distinct site families.

## value

PASS

A signed all-pattern invariant identifies more than loss of positive covering margin: it resolves equality at a hemisphere, the strict failure boundary, every extremal block, and its direction. This gives a useful resilience classification for a natural family that includes a motivated volume-optimal example; the nine-site census illustrates rather than supplies the main result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
