---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-18.md",
      "INDEPENDENT_AUDIT_2026-11-18.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

PASS: Let A=H^(1/2) unbounded selfadjoint and E=dom A with graph norm. W=(I+H)^(1/2) is unitary E→Hilbert space, and spectral measure shows W(dom H)=dom A because λ²/(1+λ) and λ are comparable for λ≥1, including arbitrary kernel and spectral type. The credited von Neumann theorem gives unitary U with U dom A∩dom A={0}. Thus D=W^-1 U dom A is graph dense, D∩dom H=0. For T=A restricted to D, closure T=A and T*=A, while dom(T*T)=D∩dom(A²)={0}, yet (closure T)*closure T=H. If H is bounded, closure T is bounded everywhere and T* is bounded everywhere, so dom T*T=dom T nonzero; converse holds. Checked source proof quantifiers including H≥0 with no injectivity/compactness conditions and distinguished unclosed vs closed products. Main nonstandard theorem is the credited 1929 von Neumann separating-unitary theorem, checked in Arlinskiĭ–Zagrebnov. No computation can replace this analytic proof.

## originality

PASS

PASS, best of knowledge with meaningful priority qualification: the 2015 Arlinskiĭ–Zagrebnov paper prominently quotes domain-disjoint unitaries and constructs closed proper restrictions/form subspaces, but not a graph-dense core disjoint from dom H with exact prescribed closed product. Hassi–de Snoo 2026 Theorem 5.4 and Proposition 6.4 give some closable or block essentially selfadjoint pathologies without arbitrary H prescription. A historical equivalent via graph-space transport could exist and must be considered residual risk.

## value

PASS

PASS: The sharp bounded-versus-unbounded classification for every preassigned nonnegative selfadjoint spectral operator, preserving exactly its kernel, multiplicities, and continuous spectrum in closure-product H while dom(T*T) is zero, provides a structural separation of core closure and adjoint-product domains in unbounded-operator theory.

The dated certificate retains the supplied scientific assessment, sources and limitations.
