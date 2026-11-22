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

`check_certificate.py` is self-contained and requires Python 3 only. It generates all 247 subsets with at least two vertices, all 48 coordinate-symmetry maps, and their twenty canonical orbits. Every printed tour is independently reconstructed from its listed vertex labels and checked using integer Hamming distances; both endpoint surrogate bounds are evaluated exactly. The script asserts the completeness of the orbit list, not just correctness of the listed examples.

The result for uncountably many real exponents does not follow from sampling: the proof applies Hölder interpolation between exponents two and \(p_*\), and a monotone three-distance comparison for all larger exponents. The strict equality classification is based on the exact integer witness table. Historical priority has not been independently certified.
