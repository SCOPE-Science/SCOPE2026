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

# Reproducibility

Run `python3 verify.py` with standard-library Python 3. It exhaustively checks one-line permutations grouped by cycle type for \(2\le n\le8\), computes exactly the subwords through the guaranteed maximum length, and checks prescribed-length witness construction for all observed words. It also checks 4,560 deterministic twelve-letter constructions and the fixed-point-free involution threshold for six even orders. The expected stdout is in `checks.txt`.

The unrestricted proof is the combinatorial directed-edge packing argument, not extrapolation from finite enumeration. The relative CW argument uses the published homotopy type of the complete injective-word complex. No independent mathematical audit has been performed. Results concerning higher homology, full homotopy type, and priority against inaccessible literature are outside this verification.
