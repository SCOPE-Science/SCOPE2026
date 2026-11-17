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

# Verification and reproducibility

The proof is analytic. To reproduce it for any specified nonnegative unbounded selfadjoint \(H\), set \(A=H^{1/2}\), equip \(\operatorname{dom}A\) with its graph inner product, and use the unitary \(W=(I+H)^{1/2}\) from that graph space onto the Hilbert space. Invoke the published von Neumann disjoint-domain unitary \(U\) for \(A\), and take \(\mathcal D=W^{-1}U\operatorname{dom}A\), \(T=A|_{\mathcal D}\). The spectral-measure test \(\lambda^2/(1+\lambda)\asymp\lambda\) at large \(\lambda\) verifies \(W\operatorname{dom}H=\operatorname{dom}A\). Consequently \(\mathcal D\) is graph dense and avoids \(\operatorname{dom}H\), which proves \(\operatorname{dom}(T^*T)=\{0\}\), while \(\overline T^{\,*}\overline T=H\). The bounded reverse implication is direct from the boundedness of \(\overline T\).

The only non-elementary invoked lemma is the classical von Neumann domain-separation theorem, given and cited in Arlinskiĭ–Zagrebnov (arXiv:1312.6502). The theorem is not re-proved here and no external certification is represented. There are no software dependencies or numerical tests. The result concerns an existential graph core, not a computationally specified basis. Independent audit is not performed.
