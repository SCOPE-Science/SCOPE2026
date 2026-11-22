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

# Verification

Run `python3 VERIFY.py` using Python 3 with no third-party dependencies. This reconstructs the actual parity-bipartition incidence matrices of Boolean hypercubes, deletes the prescribed matching edges and computes exact rank over \(\mathbb F_2\) using row-bitset elimination and selected independent column elimination.

Exhaustive subsets: \(n=2\) (2 cases), \(n=4\) (16 cases), \(n=6\) (65,536 cases). Deterministically sampled subsets: \(n=8\) (240 cases). Total: 65,794 subset-rank comparisons. The checker additionally confirms all baseline and full-removal ranks and checks odd baselines in dimensions 1, 3, 5 and 7. The captured output is `verification_output.txt`. These are **finite verification checks** only; the proof in `RESULT.md` independently establishes the all-even-dimension statement. No external or independent scientific audit has been performed.
