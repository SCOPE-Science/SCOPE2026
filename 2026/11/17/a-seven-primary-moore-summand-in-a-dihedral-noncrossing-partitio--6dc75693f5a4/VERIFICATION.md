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

# Verification of the integral quotient complex

Run `python3 verify.py certificate.json` in the directory containing the extracted files. Standard-library Python 3 is sufficient. The verifier constructs all \(877\) set partitions of seven points, identifies \(429\) noncrossing partitions, excludes the two lattice bounds, and takes whole-chain orbits under the explicit \(14\)-element dihedral group.

The finite checks verify the cell counts \((47,542,1954,2680,1231)\), Burnside fixed-chain counts, all signed incidences, every boundary composite, and exactly \(3221\) integral unit chain contractions. The resulting differential is the nonzero one-row map from \(\mathbb Z^{10}\) whose nonzero entries have greatest common divisor seven. The certificate records each pivot and final matrix and is compared byte-for-byte with the regenerated certificate. The expected final success marker is `VERIFY_OK`.

As an independent mathematical consistency check, the free order-seven rotation quotient has \(H_3\cong\mathbb Z/7\) by Cartan–Leray, and reflection inversion is trivial on this third group-homology degree; involution-quotient transfer localized at seven predicts the surviving \(\mathbb Z/7\) class. This does not determine the free rank or rule out two-primary torsion.

Shellability and the rank-six wedge theorem, Armstrong's orbit-space fundamental-group theorem, and the two-connected four-dimensional cellular attachment classification are mathematical prerequisites proved in the cited literature or by the argument in `RESULT.md`, not experimentally certified by this script. No assertion of independent or formal verification is made.
