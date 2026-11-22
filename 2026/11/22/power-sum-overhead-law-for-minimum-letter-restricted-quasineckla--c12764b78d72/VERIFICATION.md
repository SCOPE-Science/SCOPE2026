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

The proof's decisive steps are the exact bijection between quasinecklaces and successor-constrained zero-run blocks, the Burnside fixed-point count, and the bounded-degree separation between isolated and non-isolated zero runs. They are given in `RESULT.md` and can be reconstructed independently of any experiment.

Execute `python3 verification/verify_quasinecklace.py` to reproduce the computations. The observed output in `verification/verification_output.txt` reports 126 exhaustive content slices (107054 direct words) and 770 further coefficient and Burnside comparisons. Direct word enumeration tests the definition of quasinecklaces, rotational minimality tests ordinary necklaces, and the coefficient-side calculation is a separately coded dynamic polynomial multiplication. The two-zero closed form is checked where applicable.

Finite testing does not establish the theorem at arbitrary lengths. The symbolic proof covers all parameter values, including \(m=0\), the maximum zero-run boundary, repeated maximal runs, and the effect of nontrivial rotations. Independent scientific audit has not been performed.
