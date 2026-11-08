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

# Reproducibility and boundaries

Run `python verify.py` using Python 3. The script enumerates all indexed words for fourteen specified small alphabet/order/multiplicity triples, recomputes every length-\(k\) cyclic occurrence and its residue modulo \(n\), and evaluates every reflection axis directly against symbol equality. It also directly verifies each exceptional construction for ten odd multiplicities, and the displayed even-multiplicity witness.

Expected final line: `VERIFY_OK configurations=14 words=92219 perfect_labeled=700 symmetric_labeled=180 witnesses=21`.

The finite enumeration is a regression against definitional mistakes only. The unbounded theorem rests on the fixed-palindromic-window counting inequality and on symbolic constructive arguments. No independent external audit or machine proof is asserted.
