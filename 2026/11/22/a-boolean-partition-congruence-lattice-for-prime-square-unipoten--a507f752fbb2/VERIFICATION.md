---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Reproducibility and scope

Execute `python verify.py` using an unmodified Python 3 interpreter. The verifier exhausts all set partitions of the four-element and nine-element quandles, testing preservation of both operations in both argument positions. It also checks all fiber-collapse subset relations for \(p=5\), without enumerating every partition of 25 elements. The expected terminal line is `PRIME_SQUARE_QUANDLE_CONGRUENCES_VERIFIED`.

The computation cannot prove the theorem for arbitrary primes; the proof in `RESULT.md` is the mathematical certificate. The lattice identification rests on the prime-order translation-invariant equivalence lemma and the cross-fiber-collapse implication. The checker uses the original cyclic-residue operation rather than the coordinate-normal-form code. No external mathematical certification or independent audit has occurred.
