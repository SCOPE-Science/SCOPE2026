---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

Conditioned on labels, deleting the equal-label edges preserves each individual acceptance test. The greedy-path mean is obtained by conditioning on the first vertex and dropping its two neighbors; relative order on either remaining path is uniform. This gives m r_m=m+2 sum_{j=0}^{m−2}r_j and the stated generating function by its first-order differential equation. The cycle edge-difference vector of independent fair binary labels is uniform on even-parity masks, each having two label preimages. A path of length m in vertices specifies m+1 bits; for m<=n−2 at least one bit remains free, so a fixed start has probability 2^(−m−1). At m=n−1 all bits are specified, with two zero bits, which is possible precisely for even n. A spanning path has one zero bit, feasible for odd n, and all-one bits give the full conflict cycle for even n, whose first choice leaves P_(n−3). These yield (1) including the triangle. The Taylor integral gives r_m=am+b+(-1)^(m+1)2^(m+1)B_m and 1+b−3a=0. Subtracting the weighted linear tail cancels exactly on both parities. For odd n the residual starts B_(n−1)+3B_n, followed by the alternating tail starting positively at B_(n+1); for even n it starts B_(n−3)/(2n)+B_(n−1), followed by the alternating tail starting positively at B_n. All B_j are positive, strictly decreasing to zero, and the inequality 1−2(1−t)<=exp(-2(1−t))<=1 gives the two-sided beta estimate with relative error at most 4/(j+3). The first terms then yield exactly the two claimed limits. An independent enumeration of all priorities and label assignments through n=7 gave 2/3,31/48,19/30,911/1440,177/280; exact Taylor intervals at n=20,21,50,51,100,101 corroborate the positive exponentially well-resolved scaled differences.

## originality

PASS

Best-of-knowledge for the exact one-attempt periodic law, its strict sign at every size and the two factorial constants; not for the infinite-line density, greedy path recurrence, or repeated-proposal variants.

## value

PASS

Periodic finite cycles are the natural boundary-free finite geometry for the established one-dimensional model. The result supplies a benchmark whose sign is uniform but whose two leading factorial scales differ by a whole factor of n. Neither local convergence nor finite simulations can resolve that small structured correction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
