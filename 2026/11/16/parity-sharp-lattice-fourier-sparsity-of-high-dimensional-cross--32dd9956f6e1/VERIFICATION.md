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

For fixed d>=5, the radius-Laplace integral factors exactly as 2^d s^(d-1)/prod_j(s^2+(2*pi*k_j)^2). Inversion gives entire confluent divided differences with odd f(y)=y^m sin(sqrt(y))/sqrt(y) and even g(y)=y^(m-1)(cos(sqrt(y))-1). At integer-frequency nodes odd f=0; even g=g' =0, including zero by the m>=3 restriction. The derivative at a positive duplicated odd node is y^(m-1)/2; at a positive tripled even node g''=-y^(m-2)/4. These residues force generic pair/triple nonvanishing, while other supports lie in higher-codimension intersections. Count generic positive-coordinate collisions by sign choices and choose(d,2) or choose(d,3); zero nodes and extra collisions contribute one lower N-power. Independent mpmath confluent-residue comparisons for d=5,6,7,8 matched isolated collision formulas at 20+ relative digits. The code checks finite samples only; the Hermite proof establishes all fixed d.

## originality

PASS

Best-of-knowledge: actual proof and cited primary/read indexed comparisons distinguish the specific result from older general tools and different objects; this is not a guarantee of priority.

## value

PASS

A canonical ℓ1 lattice polytope has unexpectedly sparse integer Fourier samples, with an exact parity-driven support-codimension change. The quantified high-d leading constants answer a natural Fourier-sparsity question relevant to lattice periodization and harmonic sampling; they are not just a named substitution of a textbook integral.

The dated certificate retains the supplied scientific assessment, sources and limitations.
