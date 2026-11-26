---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

The homogeneous difference recurrence on a circular word has a three-periodic nonzero solution or is zero; hence a nonzero difference exists exactly for 3|n. Fixing the kernel difference with zeros in residue r, both admissible sources force the unflipped bits to zero and the flipped neighbors to be unequal, independently giving blocks (0,b_j,1 XOR b_j). Their output is one outside residue r and 1 XOR b_(j-1) XOR b_j in residue r. This cyclic difference map has constants as its two-element kernel and image the even-parity words, giving exactly the claimed Y_r and two preimages per r. Two different r require every output site to be one. The all-one output has the three periodic single-one sources; the other element in its full linear coset is the inadmissible all-one source. Every other multiple fiber has exactly one kernel-difference type and thus size two. Trace of the nth power of the two-state adjacency matrix gives L_n. Summing 2A_2+3A_3 and subtracting from L_n gives A_1; summing all positive fibers proves the image/codebook count. This includes n=3 (one singleton and one triple, no doubles). The failure probability on admissible sources is (3·2^m-3)/L_(3m) on multiples of three and zero otherwise. Independent enumeration through n=18 corroborated these counts and every Y_r, including the pair counts by difference. The comparison to the Fibonacci-cube XOR record in the prior-work prose should distinguish path from cycle, but that does not affect the claim or proof.

## originality

FAIL

Two distinct indexed records already give the same one-step theorem on the same indexed cyclic no-11 language, including every positive-fiber count, image, and unique all-one triple. Both explicitly classify all collision inputs by kernel difference. The target's more explicit Y_r output test is not verbatim in those records, but the image of their two-choice collision blocks under the same local map is exactly a cyclic binary difference plus a constant; this gives Y_r immediately, not a new unaccounted classification. This establishes overlap and mechanical implication, not a chronological priority award: both indexed records carry the same date as the target, and within-day order is not established.

## value

FAIL

Exact inverse fibers are a natural and useful constrained-readout question, but here the main quantitative answer is the same as the existing indexed answers. The only characterized difference is the coordinates of the ambiguous outputs, which come directly from one local rule evaluation on the already explicit collision blocks and the elementary cyclic difference parity test. This is a useful presentation for decoding, not an independently substantial exact invariant beyond the covered result under the review standard. No surviving claim warrants a repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
