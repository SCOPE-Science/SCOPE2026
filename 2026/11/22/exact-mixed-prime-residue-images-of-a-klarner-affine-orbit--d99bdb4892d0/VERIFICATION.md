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

# Reproducible checks

Execute `python3 verify.py` in the directory containing the standalone checker. It performs an exact breadth-first fixed-point closure of the three affine maps modulo each tested modulus and compares **the whole reachable set**, not just its size, against the theorem's independently constructed finite union. It additionally checks the cardinality formula.

The completed run returned `PASS 70 exact modular-image and count comparisons`. The 56 mixed-modulus tests comprise \(b=1,\dots,7\) and \(u\in\{1,5,7,11,13,17,25,35\}\). Fourteen odd-modulus checks corroborate the auxiliary surjectivity lemma. The checker also asserts the exact residue images for moduli \(6\) and \(18\).

These are finite tests only. The universal claim follows from the algebraic proof: exact odd-modulus coverage, forced terminal forms for odd orbit words, exhaustive congruence lifting, and counting by \(3\)-adic valuation. No external proof certification or independent mathematical audit is asserted. The ordinary asymptotic density of the integer orbit is outside the theorem.
