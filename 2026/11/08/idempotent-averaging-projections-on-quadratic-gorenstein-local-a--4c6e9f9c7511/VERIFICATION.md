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

# Verification record

The original algebra multiplication is explicitly implemented in `checks/exhaustive.cpp`. It evaluates the two polynomial identities \(P^2=P\) and \(P(xP(y))=P(x)P(y)\) on every algebra basis pair. Multilinearity extends these tests to every pair of algebra elements for each candidate map. All linear maps are enumerated over \(\mathbb F_2\) in the two-dimensional hyperbolic case; other configurations exhaust maps fixing \(1\), justified independently by the local-unitality proof.

The exact observed rank profiles, including the zero map when appropriate, are recorded in `checks/verification_output.txt`. The finite-subspace script independently enumerates row-echelon subspaces and verifies nondegenerate and totally isotropic counts, and checks the odd-field orthogonal product formulas. Outputs agree with the theoretical polynomial for all recorded configurations.

The proof for arbitrary fields and dimensions is mathematical and is not inferred from finite experiments. The scripts test prime fields only, despite the theorem covering finite extension fields through the structural formula; no claim is made that computation covered extension-field multiplication or general geometric scheme structure. All verification is same-model, not an independent audit.
