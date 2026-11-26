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

With the unnormalized transform, expanding the character into products of forced-edge indicators gives the factorial formula in the record. Every nonempty proper forced subset of at most four edges must be acyclic of maximum degree two. A path forest with j edges and b nontrivial components has 2^b orientations on its contracted blocks, (n-j-1)! orders of directed blocks modulo rotation, and division by two for reversal. This counts actual expanded cycles even in the two-block case, where one should not count simple graph cycles on the contracted vertices. The proof bounds all orders n≥18 by M_n minus twice |S|(n-2)!, which is strictly positive, without using a numerical extrapolation. Independently enumerated the at most four-edge masks on K8, testing admissibility by connected component edge counts and maximum degrees, and evaluated all 17 resulting signatures at all 12 orders 6–17. Exactly (9,(4,9,6,0)) and (10,(3,3,0,0)) canceled. Checking degree sequences within connected components gave precisely triangle or three-star, with one disjoint edge only for the n=9 support. Every support of size ≤4 has at most eight incident vertices, so this enumeration includes all realizable types at each tested order; both cancelling types fit at their indicated orders. Replay: python3 /workspace/independent_checks.py 3. Direct labelling gives 6300 and 960 zero characters, and diagonalization of counting convolution gives the verified band dimensions 66712 and 164221, with ranks 60412 and 163261. The proof concerns unoriented cycles and only the low-degree band, not global invertibility.

## originality

PASS

The older all-frequency binary-order result already covers some orders and the K9 full-spectrum census anticipates the order-nine nullity problem. Neither available statement yields the complete degree-four support classification for all n, in particular the two exact order-ten motifs and the absence of every other low-degree zero at every nonexceptional order. The conclusion stands on that uniform motif classification, not on a stand-alone K9 histogram or on nonvanishing at already covered orders.

## value

PASS

This is a motivated exact information-loss classification for low-degree observables on an infinite family of tour incidence cubes. The sign cancellation criterion identifies both the exceptional vertex orders and the precise edge motifs that cannot be recovered, not just a finite census or a one-mask zero. The counts identify the size of the resulting inverse problem. It says nothing about conditioning or higher-degree invertibility.

The dated certificate retains the supplied scientific assessment, sources and limitations.
