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

PASS: Independently enumerated all set partitions via restricted growth words and independently imposed four-point crossing and consecutive-arc nesting predicates. Both family sizes n=2..5 are 2,5,14,42. Complete Walsh butterflies on 2^binom(n,2) frequencies yield respective zero counts (1,1),(0,0),(16,16),(0,119), equal signed histograms through n4 and rank gap 1024/905 at n5. Original 22-row spectrum.csv multiplicity sums are 1024 for each class and zeros 0/119. As an additional structural check, the source generates type-A root antichains yielding the same NN support. Affine Walsh frequency reindexing and phase multiplication preserve zero count; inequivalence follows.

## originality

PASS

PASS for the comparative n5 NC-versus-NN rank separation. A stronger prior n-all modulo-4 congruence theorem for noncrossing partitions was read in full and ALREADY implies NC5 nonvanishing (since Cat5=42≡2 mod4); this NC half is not novel. It says nothing about nonnesting 119 zero modes or identical small-order histograms, so the combined first contrast is not a corollary. The general type-A Catalan bijection does not preserve pair-incidence Walsh data.

## value

PASS

PASS: Natural same-block embedding tests whether classical Catalan-bijection equinumerosity can arise via a linear-affine Fourier equivalence. The first n5 exact 119-nullspace obstruction is a motivated finite boundary and reflects a real change in convolution recoverability.

The dated certificate retains the supplied scientific assessment, sources and limitations.
