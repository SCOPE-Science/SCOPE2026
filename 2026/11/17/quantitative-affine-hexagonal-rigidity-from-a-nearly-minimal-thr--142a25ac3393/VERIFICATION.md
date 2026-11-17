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

# Verification notes

- Reconstruct the inequality from \(v_1+v_2+v_3=0\) and \(R\) for the three complementary indices.
- Check that the three midpoints of the canonical hexagon equal \(v_1/c\), \(-v_3/c\), \(v_2/c\), respectively.
- Check supporting-functionals' endpoint errors and the inequality \(N_H(z)\le1+2\kappa N_H(z)\).
- Inspect and run `checker.py` (Python 3 standard library). The exact rational tests give coefficient checks and finite polygon consistency only.
- The universal inclusions and Banach–Mazur gap are proved analytically, without computer enumeration or any assertion that the displayed constants are sharp.
- Independent external audit has not been performed.
