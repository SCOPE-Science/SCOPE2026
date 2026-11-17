---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-09.md",
      "INDEPENDENT_AUDIT_2026-11-09.json"
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

A valid labeling has pairwise nonadjacent zero sites. For each k<n/2 the k induced colour-difference constraints on n−k positive vertices form a forest; there are n/(n−k)·binom(n−k,k) possible zero sets and exactly 2^(n−2k) consistent colourings. When k=n/2 the two alternating zero sets each have two proper two-colourings iff n/2 is even, yielding the exceptional term 4·1_(4|n) t^(n/2). The weighted cyclic matching trace with transfer matrix [[2t,t],[1,0]] adds the correction 2(−1)^(n/2)t^(n/2) for even n. Maximal feasible zeros give exact minimum multiplicities 4/2n/n². Independent direct trinary-label enumeration verified every coefficient for n=3..10, and the source verifier supplies further finite transfer checks; the all-n statement rests on the combinatorial proof.

## originality

FAIL

Exact earlier published complete singleton two-rainbow domination polynomial of labelled cycles, including identical parity correction, matching-type transfer trace and all minimum multiplicities, mathematically covers every final claim.

## value

FAIL

The natural full labelled-cycle invariant is mathematically worthwhile in principle, but the very same complete distribution and 4/2n/n² minimum counts were already proved in an earlier broader theorem, with the same transfer/matching identity. The submitted presentation adds no motivated remaining mathematical fact beyond rederivation/renaming of known exact results.

The dated certificate retains the supplied scientific assessment, sources and limitations.
