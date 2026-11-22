---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-18.md",
      "INDEPENDENT_AUDIT_2026-11-18.json"
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

The proof uses the unique Gaussian top-r set T (uniform over N), and conditional on forbidden T the unique cheapest one-coordinate swap to T′. Johnson independence ensures T′ is permitted. Its missing min-in/max-out elements are independently uniform among r and s options, giving per-permitted-basis selection probability N^{-1}(1+d(B)/(rs)). Squaring and using sum d=lambda rs plus sum d^2=lambda rs+8mu (four common Johnson neighbors for any distance-two forbidden pair) yields the stated collision formula. Rook-grid independent-set bound d<=min(r,s) gives the sharp global range. Independently enumerated all 720 Gaussian coordinate orderings for n=6,r=3 for two nonbasis pairs, reproducing 18 times 1/18 and spectrum (4 at 1/20, 10 at 1/18, 4 at 11/180), with collision values 1/18 and 113/2025. Finite checks are not a general proof; the all-n argument is the counting proof. Inspected RESULT.md blob 71e09512df7c87efd79b075b7568af154a427c44 and METADATA.json d5cce8bd5d0e4fa1a0c59343fa39f5ca9afc34ba.

## originality

PASS

Best-of-knowledge new intrinsic Euclidean exposure probabilities, pointwise normal-cone law and pair-sensitive two-direction collision invariant, compared by implications rather than matching mu or polytope terminology.

## value

PASS

Determines genuinely geometric normal-fan probabilities for a natural broad class of matroid base polytopes, where combinatorial f-vectors and lattice invariants do not determine individual exposure weights. Pair-collision distinguishes concrete polytopes with same n,r,lambda by mu; sharp range and equality witnesses are mathematically motivated and usable, not arbitrary finite arithmetic.

The dated certificate retains the supplied scientific assessment, sources and limitations.
