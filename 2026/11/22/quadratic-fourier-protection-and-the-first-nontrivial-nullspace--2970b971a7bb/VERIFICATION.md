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

Successor arcs form increasing directed paths, bijectively giving placements with no repeated source or destination. Unnormalized counting convolution is diagonal in the Walsh basis. All signs are 1 modulo 2. The Touchard identity T_(n+1)=x(T_n+T_n') and T_n''=0 modulo 2 give B_(n+2)=B_(n+1)+B_n modulo 2, with period 1,1,0. Deleting the target of a marked arc is injective into partitions on n−1 letters, giving the claimed union bound. Dobiński log-convexity makes B_n/B_(n−1) nondecreasing; a fixed positive Poisson atom at any integer larger than a putative ratio bound proves divergence. Together with B_7>4 B_6 this proves positivity from n=7. For n=3,4 the odd totals exclude zeros, and exact finite checks give the negative examples and positivity for n=5,6. Fresh columnwise rook enumeration with direct signed counting (not the supplied transform) reproduced the minima (5,1,−1),(15,5,−1),(52,22,2),(203,99,25), and at n=5 precisely 162 zero coefficients, degree histogram {3:10,4:12,5:42,6:48,7:33,8:14,9:3}, and witness counts (23,26,3,0). The exact finite run covers orders 3–6, not singularity at later even-Bell orders.

## originality

PASS

The Bell parity recurrence and rook/set-partition interpretation are not novel. The supported distinct claims are about the specific signed spectrum: finite-band protection and its first singular-order census. No materially equivalent or stronger result establishing those claims was found in the bounded comparisons.

## value

PASS

The natural staircase support is fixed by the one-in/one-out incidence constraints. Its exact first nontrivial loss of information, with every quadratic statistic still recoverable but ten cubic modes missing, is a useful benchmark in that fixed encoding. The uniform fixed-band estimate also measures asymptotic stability; it is not a claim of full invertibility in all orders.

The dated certificate retains the supplied scientific assessment, sources and limitations.
