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

# Verification record

The exact integer checker `checks/verify_partition_formula.py` enumerates balanced dual frequencies for cyclic groups of orders 4, 5, 6, 7, 8, 9, 10, 12 and for indicated noncyclic direct-product groups. It derives signed values from the equality-partition formula, not from the claimed seven-case spectrum, then checks all seven-case multiplicities and ranks. This is a deterministic finite verification of instances, not a proof for unbounded group orders.

The independent program `checks/verify_direct_character_sums.py` forms the injective four-colouring set and directly sums complex character values for cyclic orders 4, 5, 6, 8 and the tested noncyclic palettes of orders 4 and 8. Its float tolerance was \(10^{-6}\); exactness for arbitrary groups is established in the written Möbius inversion proof instead. Both programs completed with all tests passing.

The signed values and spectrum are for unnormalized convolution. Distinct character types may yield equal signed values, so the histogram is formed by adding their multiplicities. No statement here represents independent validation or formal proof certification.
