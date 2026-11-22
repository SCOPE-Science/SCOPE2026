---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-17.md",
      "INDEPENDENT_AUDIT_2026-11-17.json"
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

Given power spectrum and nonzero coefficients on S=H union(a+H), ratios are unit-modulus phases. Equality of nonzero conjugate mixed cubic entries forces rho(0)=1, rho|H=chi a character and rho(a+h)=alpha chi(h). Below polyspectral order q+1 at most q-1 inputs are in a+H; a sum within S can only have quotient count 0 or1 mod q, so arbitrary alpha remains invisible. The first closure at q copies of a yields alpha^q=chi(qa), exactly the condition for extending chi and alpha to a full group character (hence physical translation); nonroot alpha supplies genuine lower-order nontranslation ambiguity. For sparse fixed entries, recursive generation of the invariant factors of H, generator closures, cross-coset recursions, and one q-fold tuple suffice with 1+(h-1-d)+d+(h-1)+1=2h entries. Less than 2h nonzero monomial phase rows have positive-dimensional torus kernel, whereas the translation group is finite: hence cannot uniformly separate all phases. Exactly two cosets, all nonzero Fourier coefficients, exact mixed conjugate polyspectra, and magnitudes already known are indispensable assumptions.

## originality

PASS

Agulnick–Busick-Warner use holomorphic higher-order autocorrelations for general finite abelian groups, with nonconjugate zero-sum Fourier tuples and broader sufficient order bounds; those do not assert this exact mixed conjugate two-coset q+1 closure or 2h sparse row design. Babanskyy examines holomorphic zero-sum phase lattices on cyclic exact unit supports and C_{2pq} orbit-stable supports, not arbitrary finite abelian two-coset conjugate polyspectra. Schefler–Zhao–Zhong study polynomial invariant monomial separating sets for complex finite group representations, sharing phase-lattice methodology but not this precise power-known Laurent-monomial minimum and explicit support-specific design. Resultary asymmetric bispectrum work concerns interval Fourier supports rather than two cosets. Best-of-knowledge PASS with recorded risks; no failure-to-find-is-proof-of-novelty inference.

## value

PASS

Exact sparse phase retrieval on a structurally natural two-coset frequency support is important for correlation-order and sample-budget planning. Sharp classification of all residual phases, universal first resolving order, and smallest sufficient entry count provide exact mathematics beyond a generic invariant-theory framework.

The dated certificate retains the supplied scientific assessment, sources and limitations.
