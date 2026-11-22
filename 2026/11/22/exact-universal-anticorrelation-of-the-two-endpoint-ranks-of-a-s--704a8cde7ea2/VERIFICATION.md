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

# Reproduction and limits

Run `python3 check_endpoint_ranks.py` with Python 3 and the standard library. The program exhaustively enumerates signs and permutations of distinct powers-of-two increments for horizons one through six, checking 36 exact rational moment identities and 92 finite magnitude sign cases. All these tests passed.

The proof covers arbitrary symmetric atomless i.i.d. real increments and all positive integer horizons. Finite enumeration does not establish that generality; it is verified by conditioning on the independent signs of overlapping block sums, the two-/three-block identities, and complete enumeration of all block-length compositions in the analytical proof. No randomness, simulation fitting, numerical tolerance, or external input is required by the checker. The results do not establish the joint rank distribution, an asymmetric law, or distribution-free behavior when ties are possible.
