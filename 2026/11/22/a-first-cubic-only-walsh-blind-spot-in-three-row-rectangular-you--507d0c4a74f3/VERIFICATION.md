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

## Exact checks

`python3 verify_sparse_three_row.py` was executed using the standard library and returned PASS. Every degree-one through degree-three character on the \(3\times10\) cell cube was evaluated twice using independent constructions (bitset XOR over all 286 shapes; and an inclusion-exclusion formula for cell-containment counts). Reported zero counts are \(0,0,30\), with complete comparison of the fifteen orbit representatives and the half-turn pairing. The same checks for widths two, six and fourteen establish the first-zero degrees and two versus three versus two cancellation pattern. Central-cell duality and odd-total parity prove the auxiliary statements for odd widths and widths divisible by four.

## Limits

No complete \(2^{30}\)-frequency transform, general-width recurrence, or independence certificate is claimed. Finite calculations prove finite exhaustive ranges because all supports within the specified Hamming weights were enumerated, not because of statistical sampling. Claims beyond those ranges remain unproved.
