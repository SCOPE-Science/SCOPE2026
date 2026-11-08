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

# Reproducible verification

Running `python3 verify_tietze_torsion.py` from a directory containing the program uses the Python standard library only. It generates `tietze_certificate.json`, reconstructs integral matrices on the canonical weight-three reduced Świątkowski bases, and verifies the following exact checks:

- The cubic graph has twelve vertices and eighteen edges; the top, middle and next weight-three chain groups have respective ranks \(1760\), \(4752\), and \(4104\).
- The integral top matrix \(D_3\) has rank \(1759\) modulo two and full column rank modulo \(3\), \(5\), and \(101\). This proves injectivity over \(\mathbb Q\) and \(\mathbb Z\).
- A \(224\)-term integral chain \(c\) with coefficients one satisfies \(D_3c=2w\); the nonzero coordinates of \(w\) are exactly \(360\) coefficients \(\pm1\). Their complete index/coefficient list is in `tietze_certificate.json`.
- The next differential satisfies \(D_2w=0\) and \(D_2D_3=0\) on all \(1760\) top basis generators. An integer boundary for \(w\) would force \(c\) divisible by two, which is false.

The resulting order-two homology statement uses the published reduced-complex comparison theorem for continuous configuration spaces. That topological identification is a literature premise, not asserted to be independently reproved by the finite script. The other homological degrees and full invariant-factor decomposition remain uncomputed.
