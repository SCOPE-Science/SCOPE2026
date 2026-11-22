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

Execute `python3 verify_char2_fermat_picard.py` with Python 3's standard library. Expected marker: `CHAR2_FERMAT_CUBIC_INTEGRAL_PICARD_TORUS_OK`.

The verifier checks all \(27\) line point sets inside \(\mathbb P^3(\mathbb F_4)\), the \(45\) distinct triple incidences and all \(135\) branches. It constructs the normalization graph, the exact Frobenius involution, and two independent fundamental-cycle coordinate systems with \(\operatorname{rank}_{\mathbb F_2}(F-I)=32\) and trace zero. The infinite-field-family conclusion follows from the explicit finite étale splitting over \(\mathbb F_4\) and the stated integral involution-lattice classification; this is not an exhaustive numerical sample of all finite fields. There is no independent external mathematical audit or historical priority certification.
