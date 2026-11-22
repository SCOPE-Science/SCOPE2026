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

## Independent reproducibility instructions

Run `python verify.py` from the package directory using Python 3 and no external packages. The script explicitly defines the multiplication laws of four representative nonabelian groups of order eight and 27, enumerates homomorphisms from images of generators, independently verifies their images and the center/commutator facts, independently counts all surjective homomorphism rules at two input sites, and evaluates the shift-power identity on 75 reproducible random examples for each group. The verified two-site totals are 64 for \(D_4\), 192 for \(Q_8\), 7776 for the order-27 Heisenberg group and 972 for the order-27 modular group. Its input seed is fixed for deterministic replay.

The program's success is finite corroboration only. The proof in `RESULT.md` derives the stated result for every prime, every nonabelian group of order \(p^3\), and every bi-infinite configuration without relying on enumeration, probabilistic tests, or assumptions about the smallest groups. The local-rule count follows from the structural proof, not the numerical examples. The review does not certify historical novelty or independent validation.
