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

# Verification of the three-node bound

The included `CHECK.py` runs with standard Python 3; no downloaded mathematical data or nonstandard modules are required. It proves the rational polynomial identities implementing the three Galois-conjugate squared distances and verifies the 53-adic images exactly. It then tests all \(3^6=729\) possible residue assignments, independently constructing anchored Gram and five-by-five Cayley–Menger determinants for every assignment.

Observed checks: `Gram / Cayley-Menger determinant crosscheck: 729/729`; `nonzero mod 53: 729/729`; `zero residues: 0`. The four-bin nonzero-residue histogram is \((233,211,215,70)\), which sums to \(729\).

Completeness of this *finite* test is established by the proof in RESULT.md: any hypothetical four-node configuration is mapped, via the explicit cyclic cubic field and its homomorphism modulo \(53\), into one of the tested assignments. The kernel formula, the positivity of its roots, and the planar Gram rank argument are mathematical premises separately given in the proof, not consequences of the numerical checker. This is a self-review only, with no independent audit or external certification.
