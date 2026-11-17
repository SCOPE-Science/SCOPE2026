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

# Verification of the sharp return-frequency theorem

The proof is analytical: the one-step mass-loss inequality is a complete scalar maximization for \(p\ge1\); each visit contracts the selected future \(p\)-mass by its optimal factor; initial/final visit estimates give the global count; the explicit sparse vector attains its asymptotic coefficient.

The attached `checker.py` passed 42,168 comparisons and identity tests over sampled exponents and radii. The diagnostic includes direct-grid optimization and strict sparse-geometric bounds. The computation does not enumerate all vectors and does not prove the infinite result; it checks algebra and test cases.

The theorem assumes \(\alpha>0\), \(0<\varepsilon<1\), finite \(p\ge1\), and a fixed target \(e_0\). No independent validation has been carried out.
